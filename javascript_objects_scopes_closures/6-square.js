#!/usr/bin/node
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    if (c === undefined) {
      // Set default character as 'X' if C parameter is undefined
      c = 'X';
    }
    // Otherwise, print square using the 'C' character
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        // Append 'c' character onto each row
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
