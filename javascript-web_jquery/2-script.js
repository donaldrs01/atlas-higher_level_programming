/* global $ */
// Wait for page DOM to load
$(document).ready(function () {
  // When elem with id 'red_header' is clicked:
  $('#red_header').click(function () {
    // Target header and change text color
    $('header').css('color', '#FF0000');
  });
});
