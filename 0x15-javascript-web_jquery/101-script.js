// script that adds, removes and clears LI elements
// from a list when the user clicks:

$(function () {
  $('DIV#add_item').click(() => $('ul.my_list').append('<li>Item</li>'));
  $('DIV#remove_item').click(() => $('ul.my_list li').last().remove());
  $('DIV#clear_list').click(() => $('ul.my_list').empty());
});
