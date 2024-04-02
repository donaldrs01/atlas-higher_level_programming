/* global $ */
// Wait for page DOM to load
$(document).ready(function () {
  // When elem with id 'red_header' is clicked:
  $('#red_header').click(function () {
    // Add 'red' class to <header> element
    $('header').addClass('red');
  });
});
