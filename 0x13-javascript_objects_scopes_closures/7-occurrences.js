#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};

/*
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let i;
  for (i of list) {
    if (i === searchElement) {
      count++;
    }
  }
  return (count);
};
*/

/*
exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (const i in list) {
    if (list[i] === searchElement) {
      counter += 1;
    }
  }
  return (counter);
};
*/
