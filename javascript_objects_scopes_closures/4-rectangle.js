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

  rotate () {
    // Swap width and height values
    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    // Multiply width/height values by 2
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
