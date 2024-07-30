// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract PrimitiveDataTypes {

    // State variables (global variables)
    uint8   a = 20;   // Unsigned 8-bit integer
    uint256 b = 35;   // Unsigned 256-bit integer
    int     c = 10;   // Signed integer
    int8    d = 3;    // Signed 8-bit integer

    bool    flag = true; // Boolean variable
    address public addr; // Address variable, public visibility

    // Constructor to automatically set the address to the deployer's address
    constructor() {
        addr = msg.sender; // Set addr to the address that deployed the contract
    }

    // Operations in Solidity
    uint public addition    = a + b;  // Addition of a and b
    int  public subtraction = c - d;  // Subtraction of d from c
    int  public multiply    = d * c;  // Multiplication of d and c
    int  public division    = c / d;  // Division of c by d
    int  public moduloDiv   = c % d;  // Modulo operation, remainder of c / d
    int  public increment   = ++c;    // Increment c by 1
    int  public decrement   = --d;    // Decrement d by 1

}
