#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    // convert number to string using toString() in the specified base
    return number.toString(base);
  };
};
