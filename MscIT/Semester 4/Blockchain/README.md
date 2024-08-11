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

```

</details>

<br>


2d. Arrays

<details>
<summary>CODE</summary>

```solidity

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


```

</details>

<br>


2e. Enums

<details>
<summary>CODE</summary>

```solidity

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Enums {

    // Define an enumeration called 'week_days' to represent the days of the week
    enum week_days {Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday}
    
    // Declare a state variable 'choice' of type 'week_days'
    week_days choice;

    // A function to set the value of 'choice' to 'Friday'
    function set_value() public {
        choice = week_days.Friday;
    }

    // A function to return the current value of 'choice'
    function get_choice() public view returns (week_days) {
        return choice;
    }
}


```

</details>

<br>


2f. Structs

<details>
<summary>CODE</summary>

```solidity

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Structs {

    // Declaring a struct named 'Book' to represent book details
    struct Book {
        string name;       // The name of the book
        string writer;     // The writer/author of the book
        uint price;        // The price of the book
        bool available;    // Availability status of the book (true if available)
    }

    // Declaring a state variable 'book1' of type 'Book'
    Book book1;

    // Initializing a Book struct with details for 'book2'
    Book book2 = Book("Harry Potter", "J.K.Rowling", 300, true);

    // A function to set details for 'book1'
    function set_book_detail() public {
        // Setting the details of 'book1'
        book1 = Book("Introducing Ethereum and Solidity", "Chris Dannen", 250, true);
    }

    // A function to get the details of 'book2'
    function book1_info() public view returns (string memory, string memory, uint, bool) { 
        // Returning the details of 'book2'
        return(book2.name, book2.writer, book2.price, book2.available); 
    }

    // A function to get the details of 'book1'
    function book2_info() public view returns (string memory, string memory, uint, bool) {
        // Returning the details of 'book1'
        return (book1.name, book1.writer, book1.price, book1.available);
    }

}


```

</details>

<br>



2g. Mappings

<details>
<summary>CODE</summary>

```solidity

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


```

</details>

<br>



2h. Conversions, Ether Units, Special Variables


<details>
<summary>CODE</summary>

```solidity

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


```

</details>

<br>


2i. Strings


<details>
<summary>CODE</summary>

```solidity

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract StringExample {
    // State variable to store a string
    string public greeting = "Hello, ";

    // Function to concatenate strings
    // @param _name: The string to concatenate with the greeting
    // @return: The concatenated result
    function concatenate(string memory _name) public view returns (string memory) {
        return string(abi.encodePacked(greeting, _name)); // Concatenate 'greeting' with '_name'
    }

    // Function to compare two strings
    // @param _a: The first string for comparison
    // @param _b: The second string for comparison
    // @return: True if the strings are equal, false otherwise
    function compareStrings(string memory _a, string memory _b) public pure returns (bool) {
        return keccak256(abi.encodePacked(_a)) == keccak256(abi.encodePacked(_b)); // Compare hashes of the strings
    }

    // Function to update the greeting
    // @param _newGreeting: The new greeting string to set
    function updateGreeting(string memory _newGreeting) public {
        greeting = _newGreeting; // Update the 'greeting' state variable
    }
}


```

</details>

<br>

***********


## Prac3

3a. Functions

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract Addition {

    int public input1;
    int public input2;
    
    function setInputs(int _input1, int _input2) public {
        input1 = _input1;
        input2 = _input2;
    }

    function additions() public view returns(int) {
        return input1 + input2;
    }

    function subtract() public view returns(int) {
        return input1 - input2;
    }
}

```

</details>

<br>

3b. Fallback Function

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract fallbackfn {

    // Event to log details when fallback or receive function is called
    event Log(string func, address sender, uint value, bytes data);

    // Fallback function to handle calls to the contract with data or no matching function
    fallback() external payable {
        emit Log("fallback", msg.sender, msg.value, msg.data); // Emit log with details
    }

    // Receive function to handle plain ether transfers
    receive() external payable {
        emit Log("receive", msg.sender, msg.value, ""); // Emit log with details (msg.data is empty)
        //msg.data is empty hence no need to specify it and mark it as empty string

    }
}

```

</details>

<br>

3c. Mathematical functions

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract MathOperations {
    // addMod computes (x + y) % k
    // mulMod computes (x * y) % k

    // Function to compute modular addition and multiplication
    // @return addModResult: Result of (x + y) % k
    // @return mulModResult: Result of (x * y) % k
    function computeMod() public pure returns (uint addModResult, uint mulModResult) {
        uint x = 3;
        uint y = 2;
        uint k = 6;
        addModResult = addmod(x, y, k); // Compute (x + y) % k
        mulModResult = mulmod(x, y, k); // Compute (x * y) % k
    }
}

```

</details>

<br>

3d. Cryptographic functions

<details>
<summary>CODE</summary>

```solidity
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


```

</details>

<br>

3e. Function Modifiers

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract FunctionModifier {
    address public owner;
    uint256 public x = 100;
    bool public locked;

    constructor() {
        // Set the transaction sender as the owner of the contract.
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }

    modifier validAddress(address _addr) {
        require(_addr != address(0), "Not valid address");
        _;
    }

    function changeOwner(address _newOwner)
        public
        onlyOwner
        validAddress(_newOwner)
    {
        owner = _newOwner;
    }

    modifier noReentrancy() {
        require(!locked, "No reentrancy");
        locked = true;
        _;
        locked = false;
    }

    function decrement(uint256 i) public noReentrancy {
        x -= i;
        if (i > 1) {
            decrement(i - 1);
        }
    }
}

```

</details>

<br>

3f. View and Pure Functions

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.3;

contract ViewAndPure {
    uint public x = 1;

    // Promise not to modify the state.
    function addToX(uint y) public view returns (uint) {
        return x + y;
    }

    // Promise not to modify or read from the state.
    function add(uint i, uint j) public pure returns (uint) {
        return i + j;
    }
}
```

</details>

<br>

3g. Function Overloading

<details>
<summary>CODE</summary>

```solidity
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

```

</details>

<br>

******************************************************

## Prac4

4a. Withdrawal Pattern

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.13;

contract withdrawalPattern{
    address public richest;
    uint public mostSent;

    mapping (address=>uint) pendingWithdrawals;
    error NotEnoughEther();

    constructor() payable{
        richest = msg.sender;
        mostSent = msg.value;
    }

    function becomeRichest() public payable{
        if (msg.value <= mostSent) revert NotEnoughEther();
        pendingWithdrawals[richest] += msg.value;
        richest = msg.sender;
        mostSent = msg.value;
    }

    function withdraw() public {
        uint amount = pendingWithdrawals[msg.sender];
        pendingWithdrawals[msg.sender] = 0;
        payable (msg.sender).transfer(amount);
    }

}
```

</details>

<br>

4b. Restricted Access

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;
contract AccessRestriction {

    address public owner = msg.sender;
    uint public creationTime = block.timestamp;
    
    error Unauthorized();
    error TooEarly();
    error NotEnoughEther();
    
    modifier onlyBy(address account){
        if (msg.sender != account)
        revert Unauthorized();
        _;
    }

    modifier costs(uint amount) {
        if (msg.value < amount)
            revert NotEnoughEther();
            _;
        if (msg.value > amount)
            payable(msg.sender).transfer(msg.value - amount);
    }

    modifier onlyAfter(uint time) {
        if (block.timestamp < time)
            revert TooEarly();
            _;
    }

    function changeOwner(address newOwner)public onlyBy(owner){
        owner = newOwner;
    }

    function disown()public onlyBy(owner) onlyAfter(creationTime + 6 weeks){
        delete owner;
    }

    function forceOwnerChange(address newOwner)public payable costs(200 ether){
        owner = newOwner;
        // just some example condition
        if (uint160(owner) & 0 == 1)
            return;
    }
}

```

</details>

<br>

******************************************************

## Prac5

5a. Contracts and Inheritance

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract C{

    uint private data;
    uint public info;


    constructor()  {
        info = 10;
        }

        function increment(uint a) private pure returns(uint){ 
            return a + 1; 
        }
        
        function updateData(uint a) public {
            data = a;
        }

        function getData() public view returns(uint) {
            return data;
        }
        function compute(uint a, uint b) internal pure returns (uint) {
            return a + b;
        }
}
        

        
contract D {

    function readData() public returns(uint) {
        C c = new C();
        c.updateData(7);
        return c.getData();
    }
}
                

contract E is C {

    uint private result;
    C private c;
    
    constructor()  {
        c = new C();
    }

    function getComputedResult() public {
        result = compute(3, 6);
    }

    function getResult() public view returns(uint) {
        return result; 
    }
}



```

</details>

<br>

5b. Constructors

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract constructors{

    string str;
    uint amount;

    constructor(){
        str  = "Shlok is learning Solidity";
        amount = 10;
    }

    function const()public view returns(string memory,uint){
        return (str,amount);
 
    }

}
```

</details>

<br>

5c. Abstract Contracts

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

abstract contract Main {
    // Define an abstract function that can be overridden
    function add(uint a, uint b) public virtual pure returns (uint);
}

contract Adder is Main {
    // Override the add function from the Main contract
    function add(uint a, uint b) public override pure returns (uint) {
        return a + b;
    }
}

```

</details>

<br>

5d. Interfaces

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

interface adder{
    function add(uint a, uint b)external pure returns(uint);
}

contract adderContract is adder{
    function add(uint a, uint b)external pure returns(uint){
        return a+b;
    }
}

```

</details>

<br>

******************************************************

## Prac6

6a. Libraries 

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

library Search {
   function indexOf(uint[] storage self, uint value) internal view returns (uint) {
      for (uint i = 0; i < self.length; i++) {
         if (self[i] == value) {
            return i;
         }
      }
      return type(uint).max;

   }
}

contract Test {
   uint[] data;

   constructor() {
      data.push(1);
      data.push(2);
      data.push(3);
      data.push(4);
      data.push(5);
   }

   function isValuePresent() external view returns (uint) {
      uint value = 4;
      
      // Search if value is present in the array using Library function
      uint index = Search.indexOf(data, value);
      return index;
   }
}

library MathLibrary {
   function square(uint num) internal pure returns (uint) {
      return num * num;
   }
}

contract SquareContract {
   using MathLibrary for uint;

   function calculateSquare(uint num) external pure returns (uint) {
      return num.square();
   }
}

```

</details>

<br>

6b. Assembly 

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

library Sum {
   function sumUsingInlineAssembly(uint[] memory _data) public pure returns (uint sum) {
      for (uint i = 0; i < _data.length; ++i) {
         assembly {
            // Load the value from memory at the current index
            let value := mload(add(add(_data, 0x20), mul(i, 0x20)))
            // Add the value to the sum
            sum := add(sum, value)
         }
      }
      // Return the calculated sum
      return sum;
   }
}

contract Test {
   uint[] data;

   constructor() {
      data.push(1);
      data.push(2);
      data.push(3);
      data.push(4);
      data.push(5);
   }

   function sum() external view returns (uint) {
      return Sum.sumUsingInlineAssembly(data);
   }
}

```

</details>

<br>

6c. Error handling 

<details>
<summary>CODE</summary>

```solidity
pragma solidity ^0.8.17;

contract ErrorHandlingExample {
    constructor() payable {
        // Allow the contract to receive Ether during deployment
    }

    function divide(uint256 numerator, uint256 denominator) external pure returns (uint256) {
        require(denominator != 0, "Division by zero is not allowed");
        return numerator / denominator;
    }

    function withdraw(uint256 amount) external {
        require(amount <= address(this).balance, "Insufficient balance");

        payable(msg.sender).transfer(amount);
    }

    function assertExample() external pure {
        uint256 x = 5;
        uint256 y = 10;
        assert(x < y);
    }

    function tryCatchExample() external view returns (bool) {
        try this.divide(10, 5) returns (uint256 result) {
            // Handle successful division
            return true;
        } catch Error(string memory errorMessage) {
            // Handle division error
            return false;
        }
    }
}

```

</details>

<br>

6d. Events

<details>
<summary>CODE</summary>

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

contract EventExample {

    // Define an event
    event Deposit(address indexed from, uint256 amount);
    event Withdraw(address indexed to, uint256 amount);

    // Mapping to keep track of user balances
    mapping(address => uint256) public balances;

    // Function to deposit ether into the contract
    function deposit() public payable {
        require(msg.value > 0, "Must deposit more than 0 ether");

        // Update the balance
        balances[msg.sender] += msg.value;

        // Emit the Deposit event
        emit Deposit(msg.sender, msg.value);
    }

    // Function to withdraw ether from the contract
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the balance
        balances[msg.sender] -= amount;

        // Transfer the ether
        payable(msg.sender).transfer(amount);

        // Emit the Withdraw event
        emit Withdraw(msg.sender, amount);
    }
}

```

</details>

<br>

******************************************************

## Prac7

7. Install Hyperledger Fabric

<details>
<summary>CODE</summary>

```shell
# Refer word file
```

</details>

<br>

----


## Prac8

8. Demonstrate the running of the blockchain node (create node using Solidity and run)

<details>
<summary>CODE</summary>

```solidity
// Refer word file
```

</details>

<br>

******************************************************

## Prac9

9. Demonstrate the use of Bitcoin Core API

<details>
<summary>CODE</summary>

```python
import requests

# Task 1: Get information regarding the current block
def get_current_block_info():
    response = requests.get("https://blockchain.info/latestblock")
    block_info = response.json()
    print("Current block information:")
    print("Block height:", block_info['height'])
    print("Block hash:", block_info['hash'])
    print("Block index:", block_info['block_index'])
    print("Timestamp:", block_info['time'])


# Task 3: Get balance of an address
def get_address_balance(address):
    response = requests.get(f"https://blockchain.info/q/addressbalance/{address}")
    balance = float(response.text) / 10**8
    print("Balance of address", address, ":", balance, "BTC")

# Example usage
if __name__ == "__main__":
    # Task 1: Get information regarding the current block
    get_current_block_info()
    
    # Task 3: Get balance of an address
    address = "3Dh2ft6UsqjbTNzs5zrp7uK17Gqg1Pg5u5"
    get_address_balance(address)

```

</details>

<br>

******************************************************