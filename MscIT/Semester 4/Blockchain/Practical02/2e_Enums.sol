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
