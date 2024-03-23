#!/usr/bin/node
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    /* Calls constructor of parent (Rectangle)
        Use same size attribute for height/width, which creates
        instance of Square with these attributes */
    super(size, size);
  }
}

module.exports = Square;
