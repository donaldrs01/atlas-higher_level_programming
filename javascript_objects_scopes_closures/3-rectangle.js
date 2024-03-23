#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    /* Establish parameters for SUCCESSFUL creation,
          not the ones to avoid for unsuccessful creation of class */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Iterate over each row in the rectangle
    for (let i = 0; i < this.height; i++) {
      let row = '';
      // Within each row, print X characters horizontally to create width
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}

module.exports = Rectangle;
