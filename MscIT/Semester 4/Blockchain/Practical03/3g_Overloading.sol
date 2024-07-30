// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract FunctionOverloading {
    // Function with one parameter
    function sum(uint a) public pure returns (uint) {
        return a + 10;
    }

    // Overloaded function with two parameters
    function sum(uint a, uint b) public pure returns (uint) {
        return a + b;
    }

    // Overloaded function with three parameters
    function sum(uint a, uint b, uint c) public pure returns (uint) {
        return a + b + c;
    }

    // Examples of calling overloaded functions
    function exampleUsage() public pure returns (uint, uint, uint) {
        uint result1 = sum(5);            // Calls the first sum function
        uint result2 = sum(5, 10);        // Calls the second sum function
        uint result3 = sum(5, 10, 15);    // Calls the third sum function

        return (result1, result2, result3);
    }
}
