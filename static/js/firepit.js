(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);throw new Error("Cannot find module '"+o+"'")}var f=n[o]={exports:{}};t[o][0].call(f.exports,function(e){var n=t[o][1][e];return s(n?n:e)},f,f.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){

},{}]},{},[1])
$(window).scroll(function () {

    if ($(window).scrollTop() > 100) {
      $('.navfix').addClass('navbar-fixed-top');
    }
    if ($(window).scrollTop() < 101) {
      $('.navfix').removeClass('navbar-fixed-top');
    }
  });

$(function(){
	var image_count = 1;
	$('#add-image').click(function(){
		var id = '#id_form-'+image_count+'-image';
		$(id).removeClass('hidden');
		image_count += 1;
	});
	$('#remove-image').click(function(){
		var id = '#id_form-'+(image_count-1)+'-image';
		$(id).val('');
		$(id).addClass('hidden');
		image_count -= 1;
	});
});

