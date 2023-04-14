#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let line = '';
      for (let j = 0; j < this.width; j++) {
        line += 'X';
      }
      console.log(line);
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const h = this.height;
    this.height = this.width;
    this.width = h;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size);
    this.width = size;
    this.height = size;
  }
}

module.exports = Rectangle;
module.exports = Square;
