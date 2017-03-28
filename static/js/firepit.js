(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);throw new Error("Cannot find module '"+o+"'")}var f=n[o]={exports:{}};t[o][0].call(f.exports,function(e){var n=t[o][1][e];return s(n?n:e)},f,f.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){

},{}]},{},[1])
/*$(window).scroll(function () {

    if ($(window).scrollTop() > 100) {
      $('.navfix').addClass('navbar-fixed-top');
    }
    if ($(window).scrollTop() < 101) {
      $('.navfix').removeClass('navbar-fixed-top');
    }
  });
*/

$(function(){
	var image_count = 1;
	$('#add-image').click(function(){
		var id = '#id_form-'+image_count+'-image';
		$(id).removeClass('hidden');
		if(image_count<5){
			image_count += 1;
		}
	});
	$('#remove-image').click(function(){
		var id = '#id_form-'+(image_count-1)+'-image';
		$(id).val('');
		$(id).addClass('hidden');
		if(image_count>2 ){
			image_count -= 1;
		}
	});
	
	$( "#search-btn" ).click(function() {
  		$( "#id_q" ).focus();
	});

	$(".msg-modal").ready(function(){
		$('.msg-modal').delay(1000).fadeTo(2000,0);
		$('.msg-modal').on({
			mouseleave: function(){
				$(this).delay(1000).fadeTo(2000,0);
			},
			mouseenter: function(){
				if($(this).css('opacity') > .3){
					$(this).stop().fadeTo(500,1);
				}
			}
		});
	});
	$("#pro-info-header").click(function(){
		$('#product-info').toggle();
		$('#toggle-arrow').toggleClass("fa-caret-up fa-caret-down");
	});

});



