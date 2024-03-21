#!/usr/bin/node

/*
Check for number of arguments
Subtract 2 because argv[0] is path to node.js and argv[1] is path to script
*/
const number_of_args = process.argv.length - 2;

// Print statement based on number of arugments
if (number_of_args === 0) {
    console.log('No argument');
} else if (number_of_args === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
