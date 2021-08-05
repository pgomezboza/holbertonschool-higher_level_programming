#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const row = 'X'.repeat(this.width);
    for (let col = 0; col < this.height; col += 1) {
      console.log(row);
    }
  }
};
