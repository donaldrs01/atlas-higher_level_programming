#!/usr/bin/node
// Initialize outside of function so it doesn't reset each time
let indexCount = 0;

exports.logMe = function (item) {
  // Log index value and print 'item' passed through
  console.log(indexCount + ': ' + item);
  // Increment count to account for next item
  indexCount++;
};
