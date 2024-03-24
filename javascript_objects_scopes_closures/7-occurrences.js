#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let occurenceCount = 0;
  // Iterate over passed list
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      // Add to count if current element matches search element
      occurenceCount++;
    }
  }
  return occurenceCount;
};
