// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Arrays {

    // Declaring an array
    uint[] public array1 = [1, 2, 3, 4, 5];
    
    function fetch(uint index) public view returns (uint) {
        require(index < array1.length, "Index out of bounds");
        return array1[index];
    }
}
