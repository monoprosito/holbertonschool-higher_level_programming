$(document).ready(function () {
  const salutUri = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $helloElement = $('div#hello');

  function getSalut () {
    return $.get({
      url: salutUri,
      dataType: 'json'
    });
  }

  getSalut().then((res) => {
    $helloElement.text(res.hello);
  });
});
