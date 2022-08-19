/*!
* Start Bootstrap - Creative v7.0.6 (https://startbootstrap.com/theme/creative)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-creative/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    }
    ;

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

    // Activate SimpleLightbox plugin for portfolio items
    new SimpleLightbox({
        elements: '#portfolio a.portfolio-box'
    });

    document.getElementById("adv").onclick = function () {
        more();
    };

    function more(obj) {
        var button = document.getElementById("adv");

        var content = document.getElementById("showMore");
        if (content.style.display === "none") {
            content.style.display = "";
            button.style.color = "#f4624a";

        } else {
            content.style.display = "none";
            button.style.color = "white";

        }
    }

});

var slider = document.getElementById("max_value");
var output = document.getElementById("max_posts");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function () {

    if (slider.value === "100000") {
        output.innerHTML = "100000+"
    } else {
        output.innerHTML = this.value;
    }
}


var input = document.getElementById("end_date");
      var today = new Date();
      var day = today.getDate();

      // Set month to string to add leading 0
      var mon = String(today.getMonth()+1); //January is 0!
      var yr = today.getFullYear();

        if(mon.length < 2) { mon = "0" + mon; }
        if(day.length < 2) { dayn = "0" + day; }

        var date = String( yr + '-' + mon + '-' + day );

      input.disabled = false;
      input.setAttribute('max', date);


