// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract StringExample {
    // State variable to store a string
    string public greeting = "Hello, ";

    // Function to concatenate strings
    // @param _name: The string to concatenate with the greeting
    // @return: The concatenated result
    function concatenate(string memory _name) public view returns (string memory) {
        return string(abi.encodePacked(greeting, _name)); // Concatenate 'greeting' with '_name'
    }

    // Function to compare two strings
    // @param _a: The first string for comparison
    // @param _b: The second string for comparison
    // @return: True if the strings are equal, false otherwise
    function compareStrings(string memory _a, string memory _b) public pure returns (bool) {
        return keccak256(abi.encodePacked(_a)) == keccak256(abi.encodePacked(_b)); // Compare hashes of the strings
    }

    // Function to update the greeting
    // @param _newGreeting: The new greeting string to set
    function updateGreeting(string memory _newGreeting) public {
        greeting = _newGreeting; // Update the 'greeting' state variable
    }
}
