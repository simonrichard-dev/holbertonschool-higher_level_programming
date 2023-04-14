#!/usr/bin/node
const Rect = require('./4-rectangle')

class Square extends Rect {
  constructor (size) {
    super(size);
    if (size <= 0) {
      this.width = undefined;
      this.height = undefined;
    } else {
      this.width = size;
      this.height = size;
    }
  }
}

module.exports = Square;
