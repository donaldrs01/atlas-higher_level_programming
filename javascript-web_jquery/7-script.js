/* global $ */
// Wait for page DOM to load
$(document).ready(function () {
  // GET request to API to extract character name
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (data) {
    // From data, update text of #character with fetched name
    $('#character').text(data.name);
  });
});
