/* global $ */
// Wait for page DOM to load
$(document).ready(function () {
  // Click event that triggers toggle function
  $('#toggle_header').click(function () {
    // On click, use toggleClass to switch between font colors for <header>
    $('header').toggleClass('red green');
  });
});
