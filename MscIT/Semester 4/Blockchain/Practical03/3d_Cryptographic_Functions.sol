// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Crypto {
    function hash(string memory _text,uint _num,address _addr) public pure returns (bytes32) {
            return keccak256(abi.encodePacked(_text, _num, _addr));
            }

    function collision(string memory _text, string memory _anotherText)public pure returns (bytes32){
                return keccak256(abi.encodePacked(_text, _anotherText));
            }
}
        
 //hash is same for collision
 //0x5f38993891425af42a69bd3cbabdc916f093d4f444455134d4371f4ddd17bd08 - shlok shivkar
 //0x5f38993891425af42a69bd3cbabdc916f093d4f444455134d4371f4ddd17bd08 - shl okshivkar

contract GuessTheWord {
    bytes32 public answer = 0x5f38993891425af42a69bd3cbabdc916f093d4f444455134d4371f4ddd17bd08;
    
    function guess(string memory _word) public view returns (bool) {
     return keccak256(abi.encodePacked(_word)) == answer;
    }
}

