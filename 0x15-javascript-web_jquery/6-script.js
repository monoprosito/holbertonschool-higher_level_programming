const $headerElem = $('header');
const $updateHeaderElem = $('div#update_header');

$updateHeaderElem.on('click', () => {
  $headerElem.text('New Header!!!');
});
