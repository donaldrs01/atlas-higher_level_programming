#!/usr/bin/node

class Rectangle {
  width;
  height;

  constructor (w, h) {
    /* Establish parameters for SUCCESSFUL creation,
        not the ones to avoid for unsuccessful creation of class */
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
