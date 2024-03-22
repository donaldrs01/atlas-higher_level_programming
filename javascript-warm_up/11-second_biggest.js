#!/usr/bin/node
// Count # of args passed
const numArgs = process.argv.length - 2;

if (numArgs < 2) {
  console.log(0);
} else {
  /* Create new int array starting from index 2
    Then applies parseInt to each element of new array */
  const ints = process.argv.slice(2).map(arg => parseInt(arg));
  // Rearranges new int array into descending order
  ints.sort((a, b) => b - a);
  // Prints the second integer in descending int array (second largest)
  console.log(ints[1]);
}
