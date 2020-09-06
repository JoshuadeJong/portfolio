$(function() {
  $(".typed").typed({
    strings: [
      "<content>"
    ],
    showCursor: true,
    cursorChar: '<cursor>',
    autoInsertCss: true,
    typeSpeed: 0.0001,
    startDelay: 50,
    loop: false,
    showCursor: false,
    onStart: $('.message form').hide(),
    onStop: $('.message form').show(),
    onTypingResumed: $('.message form').hide(),
    onTypingPaused: $('.message form').show(),
    onComplete: $('.message form').show(),
    onStringTyped: function(pos, self) {$('.message form').show();},
  });
  $('.message form').hide()
});
