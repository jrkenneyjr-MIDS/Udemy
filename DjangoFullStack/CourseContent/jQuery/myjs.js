var count = 0
$('h1').click(function(){
  count++
  $(this).text("count: " + count)
})

$('input').eq(0).keypress(function(){
  if(event.which === 13) {
    $('h3').toggleClass('turnRed')
  }
})

$('h1').on('dblclick', function(){
  $(this).toggleClass('turnBlue')
})

$('input').eq(1).on('click', function(){
  $(".container").slideUp(3000)
})
