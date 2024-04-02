#!/usr/bin/node
const request = require('request');
const URL = process.argv[2];

request(URL, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  // Parse response body as JSON
  const todos = JSON.parse(body);
  // Create object to store completed task counter
  const completedTasks = {};

  todos.forEach(todo => {
    if (todo.completed) {
        // If userID exists, increment the count
      if (completedTasks[todo.userID]) {
        completedTasks[todo.userId]++;
      } else {
        // If userID doesn't exist, this is their first task, so initialize to 1
        completedTasks[todo.userId] = 1;
      }
    }
  });
  // Print counter
  console.log(completedTasks);
});
