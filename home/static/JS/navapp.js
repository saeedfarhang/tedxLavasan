const navLinks = document.querySelector('.nav-links')
const navMenu = document.querySelector('.nav-menu')
const navLink = document.querySelectorAll('.nav-links a')
const container = document.querySelector('.container')

navMenu.addEventListener('click', function() {
    navLinks.classList.toggle('nav-show')
    container.classList.toggle('show-menu-highlight')
    document.querySelector('.l1').classList.toggle('toggle')
    document.querySelector('.l2').classList.toggle('toggle')
    document.querySelector('.l3').classList.toggle('toggle')
});

mediaq()

function mediaq() {
    var mobile = window.matchMedia("(max-width: 620px)")
    var tablet = window.matchMedia("(max-width: 960px)")
    if (mobile.matches) {
        // mobile
        smallQuery()

    } else if (tablet.matches) {

        smallQuery()
    } else {
        // laptops

        navLinks.classList.remove('nav-home')
        navLinks.classList.remove('nav-show-desktop')
        container.classList.remove('show-menu-highlight')
        navMenu.classList.remove('hide')
        document.querySelector('.l1').classList.remove('toggle')
        document.querySelector('.l2').classList.remove('toggle')
        document.querySelector('.l3').classList.remove('toggle')

        if (navLinks.classList.contains("nav-show-desktop")) {
            navLinks.classList.add('nav-show-desktop')

        } else {
            navLinks.classList.remove('nav-show-desktop')

        };
    };


}

function smallQuery() {

    navLinks.classList.remove('nav-home')
    navLinks.classList.remove('nav-show')
    container.classList.remove('show-menu-highlight')
    navMenu.classList.remove('hide')
    document.querySelector('.l1').classList.remove('toggle')
    document.querySelector('.l2').classList.remove('toggle')
    document.querySelector('.l3').classList.remove('toggle')


    if (navLinks.classList.contains("nav-show")) {
        navLinks.classList.add('nav-show')

    } else {
        navLinks.classList.remove('nav-show')

    };
};