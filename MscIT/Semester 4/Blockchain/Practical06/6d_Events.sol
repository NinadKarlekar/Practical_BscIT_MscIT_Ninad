// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract EventExample {

    // Define an event
    event Deposit(address indexed from, uint256 amount);
    event Withdraw(address indexed to, uint256 amount);

    // Mapping to keep track of user balances
    mapping(address => uint256) public balances;

    // Function to deposit ether into the contract
    function deposit() public payable {
        require(msg.value > 0, "Must deposit more than 0 ether");

        // Update the balance
        balances[msg.sender] += msg.value;

        // Emit the Deposit event
        emit Deposit(msg.sender, msg.value);
    }

    // Function to withdraw ether from the contract
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the balance
        balances[msg.sender] -= amount;

        // Transfer the ether
        payable(msg.sender).transfer(amount);

        // Emit the Withdraw event
        emit Withdraw(msg.sender, amount);
    }
}
