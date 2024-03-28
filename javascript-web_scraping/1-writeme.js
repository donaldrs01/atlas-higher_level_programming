#!/usr/bin/node
const fs = require('node:fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, error => {
    if (error) {
        console.error(error);
    } else {
        console.log(content)
    }
});

