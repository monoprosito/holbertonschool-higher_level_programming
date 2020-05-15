const $headerElem = $('header');
const $divRedHeader = $('DIV#toggle_header');

$divRedHeader.on('click', () => {
  const currentClass = $headerElem.attr('class');

  if (currentClass === 'green') {
    $headerElem.toggleClass(`${currentClass} red`);
  }

  if (currentClass === 'red') {
    $headerElem.toggleClass(`${currentClass} green`);
  }
});
