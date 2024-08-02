# BlockChain

M. Sc (Information Technology)
BlockChain



## Index



| Sr.No. | Name | README |
| --- | --- | --- |
| [Prac1A](/MscIT/Semester%204/Blockchain/Practical01/) <br> [Prac1B](/MscIT/Semester%204/Blockchain/Practical01/) <br> [Prac1C](/MscIT/Semester%204/Blockchain/Practical01/) <br> [Prac1D](/MscIT/Semester%204/Blockchain/Practical01/) <br> [Prac1E](/MscIT/Semester%204/Blockchain/Practical01/) | a) A simple client class that generates the private and public keys by using the built-in Python RSA algorithm and test it. <br> b) A transaction class to send and receive money and test it. <br> c) Create multiple transactions and display them. <br> d) Create a blockchain, a genesis block and execute it. <br> e) Create a mining function and test it and Add blocks to the miner and dump the blockchain. | [Prac1A](#prac1) <br> [Prac1B](#prac1) <br> [Prac1C](#prac1) <br> [Prac1D](#prac1) <br> [Prac1E](#prac1) |
| [Prac2A](/MscIT/Semester%204/Blockchain/Practical02/) <br> [Prac2B](/MscIT/Semester%204/Blockchain/Practical02/) <br> [Prac2C](/MscIT/Semester%204/Blockchain/Practical02/) <br> [Prac2D](/MscIT/Semester%204/Blockchain/Practical02/) <br> [Prac2E](/MscIT/Semester%204/Blockchain/Practical02/) <br> [Prac2F](/MscIT/Semester%204/Blockchain/Practical02/) <br> [Prac2G](/MscIT/Semester%204/Blockchain/Practical02/) <br> [Prac2H](/MscIT/Semester%204/Blockchain/Practical02/) <br> [Prac2I](/MscIT/Semester%204/Blockchain/Practical02/) | a) Variable and Operators <br> b) Loops <br> c) Decision Making <br> d) Arrays <br> e) Enums <br> f) Structs <br> g) Mappings <br> h) Conversions, Ether Units, Special Variables <br> i) Strings | [Prac2A](#prac2) <br> [Prac2B](#prac2) <br> [Prac2C](#prac2) <br> [Prac2D](#prac2) <br> [Prac2E](#prac2) <br> [Prac2F](#prac2) <br> [Prac2G](#prac2) <br> [Prac2H](#prac2) <br> [Prac2I](#prac2) |
| [Prac3A](/MscIT/Semester%204/Blockchain/Practical03/) <br> [Prac3B](/MscIT/Semester%204/Blockchain/Practical03/) <br> [Prac3C](/MscIT/Semester%204/Blockchain/Practical03/) <br> [Prac3D](/MscIT/Semester%204/Blockchain/Practical03/) <br> [Prac3E](/MscIT/Semester%204/Blockchain/Practical03/) <br> [Prac3F](/MscIT/Semester%204/Blockchain/Practical03/) <br> [Prac3G](/MscIT/Semester%204/Blockchain/Practical03/) | a) Functions <br> b) Fallback Function <br> c) Mathematical functions <br> d) Cryptographic functions <br> e) Function Modifiers <br> f) View and Pure Functions <br> g) Function Overloading | [Prac3A](#prac3) <br> [Prac3B](#prac3) <br> [Prac3C](#prac3) <br> [Prac3D](#prac3) <br> [Prac3E](#prac3) <br> [Prac3F](#prac3) <br> [Prac3G](#prac3) |
| [Prac4A](/MscIT/Semester%204/Blockchain/Practical04/) <br> [Prac4B](/MscIT/Semester%204/Blockchain/Practical04/) | a) Withdrawal Pattern <br> b) Restricted Access | [Prac4A](#prac4) <br> [Prac4B](#prac4) |
| [Prac5A](/MscIT/Semester%204/Blockchain/Practical05/) <br> [Prac5B](/MscIT/Semester%204/Blockchain/Practical05/) <br> [Prac5C](/MscIT/Semester%204/Blockchain/Practical05/) <br> [Prac5D](/MscIT/Semester%204/Blockchain/Practical05/) | a) Contracts and Inheritance <br> b) Constructors <br> c) Abstract Contracts <br> d) Interfaces | [Prac5A](#prac5) <br> [Prac5B](#prac5) <br> [Prac5C](#prac5) <br> [Prac5D](#prac5) |
| [Prac6A](/MscIT/Semester%204/Blockchain/Practical06/) <br> [Prac6B](/MscIT/Semester%204/Blockchain/Practical06/) <br> [Prac6C](/MscIT/Semester%204/Blockchain/Practical06/) <br> [Prac6D](/MscIT/Semester%204/Blockchain/Practical06/) | a) Libraries  <br> b) Assembly  <br> c) Error handling  <br> d) Events | [Prac6A](#prac6) <br> [Prac6B](#prac6) <br> [Prac6C](#prac6) <br> [Prac6D](#prac6) |
| [Prac7](/MscIT/Semester%204/Blockchain/Practical07/) | Install hyperledger fabric | [Prac7](#prac7) |
| [Prac8](/MscIT/Semester%204/Blockchain/Practical08/) | Demonstrate the running of the blockchain node (create node using Solidity and run) | [Prac8](#prac8) |
| [Prac9](/MscIT/Semester%204/Blockchain/Practical09/) | Demonstrate the use of Bitcoin Core API | [Prac9](#prac9) |



******************
---------------------



# Blockchain Practicals

## Prac1

1a. A simple client class that generates the private and public keys using the built-in Python RSA algorithm and test it.

<details>
<summary>CODE</summary>

```python

#pip install cryptodome  OR
#pip install pycryptodome

#1A.- A simple client class that generates the private and public keys by using the built-in Python RSA algorithm and test it.

import Crypto
import binascii

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self):
        # Creating random number for key
        random = Crypto.Random.new().read
        # Creating new public key and private key
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
        
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
        
Demo = Client()
print(Demo.identity)




```

</details>

<br>


1b. A transaction class to send and receive money and test it.


<details>
<summary>CODE</summary>

```python

#1B.- A transaction class to send and receive money and test it.
import Crypto
import binascii

import datetime
import collections

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA

class Client:
    def __init__(self):
        # Creating random number for key
        random = Crypto.Random.new().read
        # Creating new public key and private key
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)
        
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')
    


class Transaction:
    def __init__(self, sender, receiver, value):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict({
            'sender': identity,
            'receiver': self.receiver,
            'value': self.value,
            'time': self.time
        })

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

Ninad = Client()
print("-"*50)
print("Ninad Key")
print(Ninad.identity)

KS = Client()
print("-"*50)
print("KS Key")
print(KS.identity)

t = Transaction(Ninad, KS.identity, 10.0)
print("-"*50)
print("Transaction Sign")
signature = t.sign_transaction()
print(signature)
print("-"*50)

```

</details>

<br>



1c. Create multiple transactions and display them.


<details>
<summary>CODE</summary>

```python

## Prac 1C: Aim: To create multiple transactions and display them.

#!pip install pycryptodome

import Crypto
import binascii

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

import datetime
import collections

import hashlib
from hashlib import sha256



class Client:
    def __init__(self):
        # Creating random number for key
        random = Crypto.Random.new().read
        # Creating new public key and private key
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format="DER")).decode(
            "ascii"
        )


# Demo = Client()
# print(Demo.identity)


class Transaction:
    def __init__(self, sender, receiver, value):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict(
            {
                "sender": identity,
                "receiver": self.receiver,
                "value": self.value,
                "time": self.time,
            }
        )

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode("utf8"))
        return binascii.hexlify(signer.sign(h)).decode("ascii")



    def sha256(message):
        return hashlib.sha256(message.encode("ascii")).hexdigest

    def mine(message, difficulty=1):
        assert difficulty >= 1
        prefix = "1" * difficulty
        for i in range(1000):
            digest = sha256(str(hash(message)) + str(i))

        if digest.startwith(prefix):
            print("after" + str(i) + "iteration found nonce:" + digest)
            return digest


class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    last_block_hash = ""

    def display_transaction(transaction):
        dict = transaction.to_dict()
        print("Sender: " + dict["sender"])
        print("-----")
        print("Receiver: " + dict["receiver"]) 
        print("-----")
        print("Value: " + str(dict["value"]))
        print("-----")
        print("Time: " + str(dict["time"]))
        print("-----")

    TPCoins = []

    def dump_blockchain(self):
        print("Number of blocks in chain" + str(len(self)))
        for x in range(len(Block.TPCoins)):  
            block_temp = Block.TPCoins[x]  
            print("block #" + str(x))
            for transaction in block_temp.verified_transactions:
                Block.display_transaction(transaction) 
                print("-------")

    last_transaction_index = 0

    transactions = []

    Ninad = Client()
    ks = Client()
    vighnesh = Client()
    sairaj = Client()

    t1 = Transaction(Ninad, ks.identity, 15.0)
    t1.sign_transaction()
    transactions.append(t1)

    t2 = Transaction(Ninad, vighnesh.identity, 6.0)
    t2.sign_transaction()
    transactions.append(t2)

    t3 = Transaction(Ninad, sairaj.identity, 16.0)
    t3.sign_transaction()
    transactions.append(t3)

    t4 = Transaction(vighnesh, Ninad.identity, 8.0)
    t4.sign_transaction()
    transactions.append(t4)

    t5 = Transaction(vighnesh, ks.identity, 19.0)
    t5.sign_transaction()
    transactions.append(t5)

    t6 = Transaction(vighnesh, sairaj.identity, 35.0)
    t6.sign_transaction()
    transactions.append(t6)

    t7 = Transaction(sairaj, vighnesh.identity, 5.0)
    t7.sign_transaction()
    transactions.append(t7)

    t8 = Transaction(sairaj, Ninad.identity, 12.0)
    t8.sign_transaction()
    transactions.append(t8)

    t9 = Transaction(sairaj, ks.identity, 25.0)
    t9.sign_transaction()
    transactions.append(t9)

    t10 = Transaction(Ninad, ks.identity, 1.0)
    t10.sign_transaction()
    transactions.append(t10)

    for transaction in transactions:
        display_transaction(transaction)
        print("*" * 50)


```

</details>

<br>


1d. Create a blockchain, a genesis block and execute it.


<details>
<summary>CODE</summary>

```python

# AIm 1D - Create a blockchain, a genesis block and execute it.

#!pip install pycryptodome

import Crypto
import binascii
import datetime
import collections

from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5


class Client:
    def __init__(self):
        # Creating random number for key
        random = Crypto.Random.new().read
        # Creating new public key and private key
        self._private_key = RSA.generate(1024, random)
        self._public_key = self._private_key.publickey()
        self._signer = PKCS1_v1_5.new(self._private_key)

    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format="DER")).decode(
            "ascii"
        )


class Transaction:
    def __init__(self, sender, receiver, value):
        self.sender = sender
        self.receiver = receiver
        self.value = value
        self.time = datetime.datetime.now()

    def to_dict(self):
        if self.sender == "Genesis":
            identity = "Genesis"
        else:
            identity = self.sender.identity

        return collections.OrderedDict(
            {
                "sender": identity,
                "receiver": self.receiver,
                "value": self.value,
                "time": self.time,
            }
        )

    def sign_transaction(self):
        private_key = self.sender._private_key
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode("utf8"))
        return binascii.hexlify(signer.sign(h)).decode("ascii")


class Block:
    def __init__(self):
        self.verified_transactions = []
        self.previous_block_hash = ""
        self.Nonce = ""

    last_block_hash = ""

    def display_transaction(transaction):
        dict = transaction.to_dict()
        print("Sender: " + dict["sender"])
        print("-----")
        print("Receiver: " + dict["receiver"])  # Corrected typo
        print("-----")
        print("Value: " + str(dict["value"]))
        print("-----")
        print("Time: " + str(dict["time"]))
        print("-----")


Ninad = Client()
t0 = Transaction("Genesis", Ninad.identity, 500.0)

block0 = Block()
block0.previous_block_hash = None
Nonce = None
block0.verified_transactions.append(t0)
digest = hash(block0)
last_block_hash = digest
TPCoins = []


def dump_blockchain(self):
    print("Number of blocks in chain: " + str(len(self)))
    for x in range(len(TPCoins)):
        block_temp = TPCoins[x]
        print("block #" + str(x))
    for transaction in block_temp.verified_transactions:
        Block.display_transaction(transaction)
        print("-" * 20)
    print("=" * 30)


TPCoins.append(block0)
dump_blockchain(TPCoins)


```

</details>

<br>


1e. Create a mining function and test it and Add blocks to the miner and dump the blockchain.


<details>
<summary>CODE</summary>

```python

# -*- coding: utf-8 -*-
import collections
import datetime
import binascii
# !pip install pycryptodome
import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5

class Client:
    def __init__(self):
        random=Crypto.Random.new().read
        self._private_key=RSA.generate(1024,random)
        self._public_key=self._private_key.publickey()
        self._signer=PKCS1_v1_5.new(self._private_key)
    @property
    def identity(self):
        return binascii.hexlify(self._public_key.exportKey(format='DER')).decode('ascii')

class Transaction:
    def __init__(self,sender,recipient,value):
        self.sender=sender
        self.recipient=recipient
        self.value=value
        self.time=datetime.datetime.now()

    def to_dict(self):
        if self.sender=="Genesis":
            identity="Genesis"
        else:
            identity=self.sender.identity

        return collections.OrderedDict({
            'sender':identity,
            'recipient':self.recipient,
            'value':self.value,
            'time':self.time})
    def sign_transaction(self):
        private_key=self.sender._private_key
        signer=PKCS1_v1_5.new(private_key)
        h=SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

import hashlib
def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()
def mine(message,difficulty=1):
    assert difficulty>=1
    prefix='1'*difficulty
    for i in range(1000):
        digest=sha256(str(hash(message))+str(i))
        if digest.startswith(prefix):
            print("after"+str(i)+"iterationsfoundnonce:"+digest)
            return digest

class Block:
    def __init__(self):
        self.verified_transactions=[]
        self.previous_block_hash=""
        self.Nonce=""

def display_transaction(transaction):

    dict=transaction.to_dict()
    print("sender : "+dict['sender'])
    print('-----')
    print("recipient : "+dict['recipient'])
    print('-----')
    print("value : "+str(dict['value']))
    print('-----')
    print("time : "+str(dict['time']))
    print('-----')

def dump_blockchain(self):
    print("Number of blocks in the chain :"+str(len(self)))
    for x in range(len(TPCoins)):
        block_temp=TPCoins[x]
        print("Block # "+str(x))
        for transaction in block_temp.verified_transactions:
            display_transaction(transaction)
            print('--------------')
            print('=====================================')

last_block_hash=""
TPCoins=[]
last_transaction_index=0
transactions=[]

Raja=Client()
Rani=Client()
Seema=Client()
Reema=Client()

t1=Transaction(Raja,Rani.identity,15.0)
t1.sign_transaction()
transactions.append(t1)

t2=Transaction(Raja,Seema.identity,6.0)
t2.sign_transaction()
transactions.append(t2)

t3=Transaction(Rani,Reema.identity,2.0)
t3.sign_transaction()
transactions.append(t3)

t4=Transaction(Seema,Rani.identity,4.0)
t4.sign_transaction()
transactions.append(t4)

t5=Transaction(Reema,Seema.identity,7.0)
t5.sign_transaction()
transactions.append(t5)

t6=Transaction(Rani,Seema.identity,3.0)
t6.sign_transaction()
transactions.append(t6)

t7=Transaction(Seema,Raja.identity,8.0)
t7.sign_transaction()
transactions.append(t7)

t8=Transaction(Seema,Rani.identity,1.0)
t8.sign_transaction()
transactions.append(t8)

t9=Transaction(Reema,Raja.identity,5.0)
t9.sign_transaction()
transactions.append(t9)

t10=Transaction(Reema,Rani.identity,3.0)
t10.sign_transaction()
transactions.append(t10)

#Miner1addsablock

block=Block()
for i in range(3):
    temp_transaction=transactions[last_transaction_index]
    #validatetransaction
    #if valid
    block.verified_transactions.append(temp_transaction)
    last_transaction_index+=1

block.previous_block_hash=last_block_hash
block.Nonce=mine(block,2)
digest=hash(block)
TPCoins.append(block)
last_block_hash=digest

#Miner2 adds a block

block=Block()
for i in range(3):
    temp_transaction=transactions[last_transaction_index]
    #validate transaction
    #if valid
    block.verified_transactions.append(temp_transaction)
    last_transaction_index+=1

block.previous_block_hash=last_block_hash
block.Nonce=mine(block,2)
digest=hash(block)
TPCoins.append(block)
last_block_hash=digest

#Miner3 adds a block

block=Block()
for i in range(3):
    temp_transaction=transactions[last_transaction_index]
    #validate transaction
    #if valid
    block.verified_transactions.append(temp_transaction)
    last_transaction_index+=1

block.previous_block_hash=last_block_hash
block.Nonce=mine(block,2)
digest=hash(block)
TPCoins.append(block)
last_block_hash=digest

dump_blockchain(TPCoins)

```

</details>

<br>




## Prac2
2a. Variable and Operators

<details>
<summary>CODE</summary>

```solidity

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract PrimitiveDataTypes {

    //state variables (global variable)
    uint8   a = 20; 
    uint256 b = 35;
    int     c = 10;
    int8    d = 3;

    bool    flag = true;
    address addr = 0xCA35b7d915458EF540aDe6068dFe2F44E8fa733c;
    
    // Operations in solidity

    uint public addition    = a + b;
    int  public subtraction = c - d;
    int  public multiply    = d * c;
    int  public division    = c / d;
    int  public moduloDiv   = c % d;
    int  public increment   = ++c;
    int  public decrement   = --d;

}


```

</details>

<br>


2b. Loops

<details>
<summary>CODE</summary>

```solidity

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Loop {

    function summation(uint n) public pure returns (uint) {
        uint sum = 0;
        for (uint i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }

    function sumWhile(uint n) public pure returns (uint) {
        uint sum = 0;
        uint i = 1;
        while (i <= n) {
            sum += i;
            i++;
        }
        return sum;
    }

    function sumDoWhile(uint n) public pure returns (uint) {
        uint sum = 0;
        uint i = 1;
        do {
            sum += i;
            i++;
        } while (i <= n);
        return sum;
    }


    
}

```

</details>

<br>


2c. Decision Making

<details>
<summary>CODE</summary>

```solidity

# Paste your code here

```

</details>

<br>


2d. Arrays

<details>
<summary>CODE</summary>

```solidity

# Paste your code here

```

</details>

<br>


2e. Enums

<details>
<summary>CODE</summary>

```solidity

# Paste your code here

```

</details>

<br>


2f. Structs

<details>
<summary>CODE</summary>

```solidity

# Paste your code here

```

</details>

<br>



2g. Mappings

<details>
<summary>CODE</summary>

```solidity

# Paste your code here

```

</details>

<br>



2h. Conversions, Ether Units, Special Variables


<details>
<summary>CODE</summary>

```solidity

# Paste your code here

```

</details>

<br>


2i. Strings


<details>
<summary>CODE</summary>

```solidity

# Paste your code here

```

</details>

<br>

***********


## Prac3

3a. Functions

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for functions
```

</details>

<br>

3b. Fallback Function

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for the fallback function
```

</details>

<br>

3c. Mathematical functions

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for mathematical functions
```

</details>

<br>

3d. Cryptographic functions

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for cryptographic functions
```

</details>

<br>

3e. Function Modifiers

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for function modifiers
```

</details>

<br>

3f. View and Pure Functions

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for view and pure functions
```

</details>

<br>

3g. Function Overloading

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for function overloading
```

</details>

<br>

******************************************************

## Prac4

4a. Withdrawal Pattern

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for the withdrawal pattern
```

</details>

<br>

4b. Restricted Access

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for restricted access
```

</details>

<br>

******************************************************

## Prac5

5a. Contracts and Inheritance

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for contracts and inheritance
```

</details>

<br>

5b. Constructors

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for constructors
```

</details>

<br>

5c. Abstract Contracts

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for abstract contracts
```

</details>

<br>

5d. Interfaces

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for interfaces
```

</details>

<br>

******************************************************

## Prac6

6a. Libraries 

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for libraries
```

</details>

<br>

6b. Assembly 

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for assembly
```

</details>

<br>

6c. Error handling 

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for error handling
```

</details>

<br>

6d. Events

<details>
<summary>CODE</summary>

```solidity
# Paste your code here for events
```

</details>

<br>

******************************************************

## Prac7

7. Install Hyperledger Fabric

<details>
<summary>CODE</summary>

```shell
# Paste your code here for installing Hyperledger Fabric
```

</details>

<br>

----


## Prac8

8. Demonstrate the running of the blockchain node (create node using Solidity and run)

<details>
<summary>CODE</summary>

```solidity
// Paste your Solidity code here for creating and running a blockchain node
```

</details>

<br>

******************************************************

## Prac9

9. Demonstrate the use of Bitcoin Core API

<details>
<summary>CODE</summary>

```solidity
// # Paste your code here for using the Bitcoin Core API
```

</details>

<br>

******************************************************

## Prac10

10. Build Dapps with Angular

<details>
<summary>CODE</summary>

```typescript
// Paste your Angular code here for building Dapps
```

</details>

<br>

******************************************************


