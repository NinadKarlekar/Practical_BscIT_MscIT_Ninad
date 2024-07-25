// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract decision{

    function even(uint n) public pure returns(bool){
        if(n%2==0){
            return true;
        }
        else{
            return false;
        }
    }
}