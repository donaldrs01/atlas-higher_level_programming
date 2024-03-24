#!/usr/bin/node
exports.esrever = function (list) {
  const reversedList = [];
  // Start at last element, proceed backwards through list
  for (let i = list.length - 1; i >= 0; i--) {
    // Use push() method to add items to new array
    reversedList.push(list[i]);
  }
  return reversedList;
};
