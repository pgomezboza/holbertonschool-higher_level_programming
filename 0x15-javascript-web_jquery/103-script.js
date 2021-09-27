// script that fetches and prints how to say “Hello”
// depending on the language

const url = 'https://www.fourtonfish.com/hellosalut/?lang=';

$(function () {
  $('INPUT#btn_translate').click(() => $.get(url + $('INPUT#language_code').val(), (data) => $('DIV#hello').text(data.hello)));
  $('INPUT#language_code').keypress((event) => {
    if (event.which === 13) {
      $.get(url + $('INPUT#language_code').val(), (data) => $('DIV#hello').text(data.hello));
    }
  });
});
