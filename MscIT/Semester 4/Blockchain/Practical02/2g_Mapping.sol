// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract maps {

    // Declaring a public mapping from uint (keys) to string (values)
    mapping (uint => string) public roll_no;

    // A function to set a value in the mapping
    // @param keys: The key (uint) for the mapping
    // @param value: The value (string) to be set for the provided key
    function set(uint keys, string memory value) public {
        roll_no[keys] = value; // Set the value in the mapping for the given key
    }
}
