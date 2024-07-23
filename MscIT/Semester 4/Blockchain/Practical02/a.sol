// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract PrimitiveDataTypes {

    // State variables (global variables)
    uint8   a = 20; 
    uint256 b = 35;
    int     c = 10;
    int8    d = 3;

    bool    flag = true;
    address public addr;

    // Constructor to automatically set the address to the deployer's address
    constructor() {
        addr = msg.sender;
    }

    // Operations in Solidity
    uint public addition    = a + b;
    int  public subtraction = c - d;
    int  public multiply    = d * c;
    int  public division    = c / d;
    int  public moduloDiv   = c % d;
    int  public increment   = ++c;
    int  public decrement   = --d;

}
