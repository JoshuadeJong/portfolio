$(function() {
  $(".typed").typed({
    strings: [
      "./josh.sh info<br/>" +
      "<span class='caret'>$</span> skills: coding, data analytics, machine learning, optimization <br/> ^100" +
      "<span class='caret'>$</span> job: Software Developer at <a href='http://www.expeditors.com//'>Expeditors CHQ</a><br/> ^100" +
      "<span class='caret'>$</span> alias: MaanMan<br/> ^100" +
      "<span class='caret'>$</span> hobbies: cooking, cello, video games, and beer<br/> ^300" +
      "<span class='caret'>$</span> highlight:  <a href=''>Seattle Fire Dispatch</a>, <a href=''>System Monitoring Solution</a><br/>"
    ],
    showCursor: true,
    cursorChar: '_',
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
