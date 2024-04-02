/* global $ */
// Wait for page DOM to load
$(document).ready(function () {
  // Click event on update_header
  $('#update_header').click(function () {
    // On click, update text of header
    $('header').text('New Header!!!');
  });
});
