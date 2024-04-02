/* global $ */
// Wait for page DOM to load
$(document).ready(function () {
  // Click event with 'add_item' ID
  $('#add_item').click(function () {
    // On click, add new <li> element to the <ul>
    $('ul.my_list').append('<li>Item</li>');
  });
});
