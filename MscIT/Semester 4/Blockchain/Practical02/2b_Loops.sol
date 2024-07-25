// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Loop {
    function summation(uint256 n) public pure returns (uint256) {
        uint256 sum = 0;
        for (uint256 i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }

    function sumWhile(uint256 n) public pure returns (uint256) {
        uint256 sum = 0;
        uint256 i = 1;
        while (i <= n) {
            sum += i;
            i++;
        }
        return sum;
    }

    function sumDoWhile(uint256 n) public pure returns (uint256) {
        uint256 sum = 0;
        uint256 i = 1;
        do {
            sum += i;
            i++;
        } while (i <= n);
        return sum;
    }
}
