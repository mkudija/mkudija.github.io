/**
 * Particleground demo
 * @author Jonathan Nicol - @mrjnicol
 */

 // https://github.com/jnicol/particleground

document.addEventListener('DOMContentLoaded', function () {
  particleground(document.getElementById('particleground'), {
    dotColor: '#F0F0F0',
    lineColor: '#F0F0F0'
  });
  var intro = document.getElementById('intro');
  intro.style.marginTop = - intro.offsetHeight / 2 + 'px';
}, false);


/*
// jQuery plugin example:
$(document).ready(function() {
  $('#particles').particleground({
    dotColor: '#5cbdaa',
    lineColor: '#5cbdaa'
  });
  $('.intro').css({
    'margin-top': -($('.intro').height() / 2)
  });
});
*/