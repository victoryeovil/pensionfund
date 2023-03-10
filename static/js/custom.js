
  (function ($) {
  
  "use strict";

    // NAVBAR
    $('.navbar-nav .nav-link').click(function(){
        $(".navbar-collapse").collapse('hide');
    });

    // CUSTOM LINK 
    $('.custom-link').click(function(){
    var el = $(this).attr('href');
    var elWrapped = $(el);
    var header_height = $('.navbar').height() + 10;

    scrollToDiv(elWrapped,header_height);
    return false;

    function scrollToDiv(element,navheight){
      var offset = element.offset();
      var offsetTop = offset.top;
      var totalScroll = offsetTop-navheight;

      $('body,html').animate({
      scrollTop: totalScroll
      }, 300);
  }
});
    
  })(window.jQuery);


// Javascript by Sander Sats

var keepAlive = $(".sblogos").data("keep-alive");
var interval = $(".sblogos").data("interval");
var random = $(".sblogos").data("random");

$(function() {
  // creates interval according to parameters
  function fadeCaller() {
    if (random == "true" || random == 1) {
        setInterval(fadeImage, interval);
    } else {
      setInterval(fadeImage, keepAlive);
    }
  }

  function fadeImage() {
    // save sponsor logo boxes for further use
    var $hiddenBoxes = $('.sblogos .sblogos__col:not(:visible)');
    var $visibleBoxes = $('.sblogos .sblogos__col:visible');
    var $visibleBox;
    // if too few boxes, use random
    if ((random == "true" || random == 1) || ($hiddenBoxes.length < $visibleBoxes.length)) {
      $visibleBox = $visibleBoxes.not('.active, .sb-animation-pause').random();
    } else {
      $visibleBox = $visibleBoxes.not('.active, .sb-animation-pause').first();
      // don't fire function when no free boxes
      if ($visibleBox.length) {
        setTimeout(fadeImage, interval);
      }
    }
        var $hiddenBox = $hiddenBoxes.not('.active, .sb-animation-pause').random();
    if (!$hiddenBoxes.length) return;

    var $hiddenContent = $hiddenBox.find('a');
    if (!$hiddenContent.length) return;

    $hiddenBox.addClass('active');
    $visibleBox.addClass('active');
    var $visibleContent = $visibleBox.find('a').addClass('prev');
    $visibleBox.append($hiddenContent.addClass('next'));

    setTimeout(function() {
      $visibleBox.find('a').addClass('transition');
    }, 100);

    $visibleBox.data('timeoutId', setTimeout(function() {
      $visibleBox.find('a').removeClass('transition');
      $hiddenBox.append($visibleContent.removeClass('prev'));
      $visibleBox.removeClass('active');
      $hiddenBox.removeClass('active');
      $hiddenContent.removeClass('next');
    }, keepAlive));
  }

  $('body').on('mouseenter', '.sblogos__col', function() {
    $(this).addClass('sb-animation-pause');
  });
  $('body').on('mouseleave', '.sblogos__col', function() {
    $(this).removeClass('sb-animation-pause');
  });
  fadeCaller();
});

$.fn.random = function(){
  var ret = $();
  if(this.length > 0) {
    ret = ret.add(this[Math.floor((Math.random() * this.length))]);
  }
  return ret;
};