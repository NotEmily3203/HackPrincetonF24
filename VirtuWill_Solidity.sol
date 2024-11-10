// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SimpleOwnerContract {
    // Define the owner of the contract
    address public ownerWallet;
    string public ownerName;
    
    // Define the beneficiary
    address public beneficiaryWallet;
    string public beneficiaryName;

    // Define the IPFS hash as a string
    string public ipfsHash;

    // Define the trusted oracle address
    address public oracle;

    // Define check-in parameters
    uint256 public checkInPeriod = 1000; // Check-in period in seconds
    uint256 public lastCheckIn;        // Timestamp of the last check-in by the owner

    // Events to log actions in the contract
    event OwnerAssigned(address indexed ownerWallet, string ownerName);
    event BeneficiaryAssigned(address indexed beneficiaryWallet, string beneficiaryName);
    event IpfsAssigned(string ipfsHash);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event FundsHeld(address indexed from, uint256 amount);
    event FundsTransferred(address indexed from, address indexed to, uint256 amount);
    event CheckIn(address indexed owner, uint256 timestamp);

    // Modifier to restrict access to the oracle
    modifier onlyOracle() {
        require(msg.sender == oracle, "Only the oracle can perform this action.");
        _;
    }

    // Constructor to initialize the contract with owner, beneficiary, and oracle information
    // The deployer can send any amount of Ether to hold in the contract
    constructor(
        string memory _ownerName,
        string memory _beneficiaryName,
        address _beneficiaryWallet,
        string memory _ipfsHash,
        address _oracle
    ) payable {
        // Set up initial contract state
        ownerWallet = msg.sender;
        ownerName = _ownerName;
        beneficiaryWallet = _beneficiaryWallet;
        beneficiaryName = _beneficiaryName;
        ipfsHash = _ipfsHash;
        oracle = _oracle;
        lastCheckIn = block.timestamp;

        emit OwnerAssigned(ownerWallet, _ownerName);
        emit BeneficiaryAssigned(beneficiaryWallet, _beneficiaryName);
        emit IpfsAssigned(_ipfsHash);
        emit FundsHeld(ownerWallet, msg.value); // Log the initial fund deposit
    }

    // Check-in function to update the last check-in timestamp
    function checkIn() public {
        require(msg.sender == ownerWallet, "Only the owner can check in.");
        lastCheckIn = block.timestamp;
        emit CheckIn(msg.sender, lastCheckIn);
    }

    // View function to check if the owner is considered deceased
    function isOwnerDeceased() public view returns (bool) {
        return (block.timestamp > lastCheckIn + checkInPeriod);
    }

    // Function to transfer all contract funds to the beneficiary upon owner's death
    function transferFundsToBeneficiary() external onlyOracle {
        require(isOwnerDeceased(), "Owner is still active.");

        uint256 contractBalance = address(this).balance;
        require(contractBalance > 0, "No funds to transfer.");

        // Transfer the contract's Ether balance to the beneficiary
        (bool success, ) = beneficiaryWallet.call{value: contractBalance}("");
        require(success, "Transfer of funds failed.");

        // Emit event for final transfer
        emit FundsTransferred(address(this), beneficiaryWallet, contractBalance);

        // Update ownership details
        emit OwnershipTransferred(ownerWallet, beneficiaryWallet);
        ownerWallet = beneficiaryWallet; // Transfer ownership to the beneficiary
        ownerName = beneficiaryName;
    }

    // Function to check the contract balance
    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }

    // Function to receive Ether into the contract
    receive() external payable {}

    // Fallback function to receive Ether if calldata is not empty
    fallback() external payable {}
}
