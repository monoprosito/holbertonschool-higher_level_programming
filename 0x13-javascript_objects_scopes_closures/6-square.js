#!/usr/bin/node

// Print function with custom characters to represent the Square

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c) {
    super.print(c);
  }
};
