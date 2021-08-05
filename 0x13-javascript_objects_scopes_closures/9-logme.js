#!/usr/bin/node

exports.logMe = function (item) {
  if (!this.argsCount) {
    this.argsCount = 0;
  }
  console.log(`${this.argsCount++}: ${item}`);
};

/*
#!/usr/bin/Node
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
*/

/*
let order = 0;
exports.logMe = function (item) {
  console.log(`${count++}: ${item}`);
};
*/

/*
#!/usr/bin/Node
let count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  this.count += 1;
};
*/

/*
exports.logMe = function (item) {
  console.log(`${ord
er++}:
*/
