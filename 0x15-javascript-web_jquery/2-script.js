const $headerElem = $('header');
const $divRedHeader = $('div#red_header');

$divRedHeader.on('click', function () {
  $headerElem.css('color', '#FF0000');
});
