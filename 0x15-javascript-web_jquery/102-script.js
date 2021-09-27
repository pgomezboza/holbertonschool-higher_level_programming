// script that fetches and prints how to say “Hello”
// depending on the language

const url = 'https://fourtonfish.com/hellosalut/?lang=';

$(function () {
  $('INPUT#btn_translate').click(() => $.get(url + $('INPUT#language_code').val(), (data) => $('DIV#hello').text(data.hello)));
});
