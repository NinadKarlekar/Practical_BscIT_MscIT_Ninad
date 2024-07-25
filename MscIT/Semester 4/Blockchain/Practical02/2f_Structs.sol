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
