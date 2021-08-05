#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let col = 0; col < this.width; col += 1) {
        console.log(c.repeat(this.height));
      }
    }
  }
};

/*
module.export = class Square extends square {
  charPrint (c = 'X') {
    if (c === undefined) {
      super.print();
    } else {
      for (let i = 0; i < super.height; i++) {
        for (let j = 0; j < super.width; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
};
*/
