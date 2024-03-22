#!/usr/bin/node

function add(a, b) {
    return a + b;
}

const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

if (Number.isInteger(num1) && Number.isInteger(num2)) {
    const sum = add(num1, num2);
    console.log(sum);
} else {
    console.log('NaN')
}