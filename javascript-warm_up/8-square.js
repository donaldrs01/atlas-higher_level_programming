#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (Number.isInteger(size)) {
  for (let i = 0; i < size; i++) {
    // Iterate over each row in square
    let row = '';
    for (let j = 0; j < size; j++) {
      // append 'X' to each 'row' variable inside each column
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
