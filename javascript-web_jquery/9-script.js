/* global $ */
// Wait for page DOM to load
$(document).ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    // Update text of <hello> element with the fetched translation
    $('#hello').text(data.hello);
  });
});
