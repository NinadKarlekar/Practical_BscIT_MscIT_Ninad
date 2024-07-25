// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract conversion {

    // Declaring state variables of different unsigned integer types
    uint   a = 5;    // Default unsigned integer type
    uint8  b = 10;   // 8-bit unsigned integer
    uint16 c = 15;   // 16-bit unsigned integer

    // A function to convert and add the values of a, b, and c
    function convert() public view returns (uint) {
        uint result = a + uint(b) + uint(c); // Convert b and c to uint and add them to a
        return result; // Return the result
    }
}
