//
//
!function ($) {
 $(function() {

    //var $window = $(window)

    // Loading button
    $('#fat-btn')
      .click(function () {
        var btn = $(this)
        btn.button('loading')
        setTimeout(function () {
          btn.button('reset')
        }, 3000)
    })    
 })
}(window.jQuery)
