odoo.define('my_website.main', function (require) {
    "use strict";

	$(function(){
	    jarallax(document.querySelectorAll('.jarallax'));
        jarallax(document.querySelectorAll('.jarallax-keep-img'), {
            keepImg: true,
        });
	});

});
