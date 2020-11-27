$(document).ready(function() {
  $('.accordion-toggler').click(function() {
    var acc = $(this).parents('.accordion');
    if ($(this).hasClass('active')) {
      $(this).removeClass('active');
      acc.find('.content').hide(2000);
    } else {
      $(this).addClass('active');
      acc.find('.content').show(2000);
    }
  })

  $('.up-toggler').click(function(event) {
    event.stopPropagation();
    $(this).parents('.accordion').insertBefore($(this).parents('.accordion').prev());
  });

  $('.down-toggler').click(function(event) {
    event.stopPropagation();
    $(this).parents('.accordion').insertAfter($(this).parents('.accordion').next());
  })
});