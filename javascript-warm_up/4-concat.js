#!/usr/bin/node

const concatenatedString = process.argv[2] + ' is ' + process.argv[3];
// Conditional if no arguments are present
if (process.argv[2] === undefined) {
  console.log('undefined is undefined');
} else if (process.argv[3] === undefined) {
// Conditional if 1 argument is present
  console.log(process.argv[2] + ' is undefined');
} else {
// Conditional if 2 arguments are present
  console.log(concatenatedString);
}
