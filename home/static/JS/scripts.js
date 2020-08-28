// vars
const introSpeakerBtn = document.querySelector('.intro-speaker-btn')
const introSpeakersSection = document.querySelector('.introducting-speaker-section')
const addSponsorBtn = document.querySelector('.add-sponsors-btn')
const addSponsorSection = document.querySelector('.add-sponsor-form')
const VolunteerBtn = document.querySelector('.volunteer-btn')
const volunteerSection = document.querySelector('.volunteer-form')

const tedTab = document.querySelector('.ted-tab')
const tedxTab = document.querySelector('.tedx-tab')
const tedxlavasanTab = document.querySelector('.tedxlavasan-tab')
const abouttedtext = document.querySelector('.abouttedtext')

const historyTab = document.querySelector('.history-tab')
const attrTab = document.querySelector('.attr-tab')
const whattoseeTab = document.querySelector('.whattosee-tab')
const aboutlavasantext = document.querySelector('.aboutlavasantext')

const navLinks = document.querySelector('.nav-links')
const navMenu = document.querySelector('.nav-menu')
const navLink = document.querySelectorAll('.nav-links a')
const container = document.querySelector('.container')

const HomeArrow = document.querySelector('.arrow-down')

//listeners
introSpeakerBtn.addEventListener('click', function() { SectionShow(introSpeakersSection) })
addSponsorBtn.addEventListener('click', function() { SectionShow(addSponsorSection) })
VolunteerBtn.addEventListener('click', function() { SectionShow(volunteerSection) })
HomeArrow.addEventListener('click', function() { abouttedSection.scrollIntoView({ behavior: 'smooth' }) })
window.addEventListener('scroll', scrollFn)
window.addEventListener('DOMContentLoaded', runTime)

function runTime() {
    HideSection(introSpeakersSection)
    HideSection(addSponsorSection)
    HideSection(volunteerSection)
    scrollFn()
    map()
    tedTab.click()
    historyTab.click()

}

function abouttedsection() {
    tedTab.addEventListener('click', function() {
        tedTab.classList.remove('tab-on')
        tedxTab.classList.remove('tab-on')
        tedxlavasanTab.classList.remove('tab-on')

        tedTab.classList.add('tab-on')
        abouttedtext.innerHTML = "درباره تد"
    })
    tedxTab.addEventListener('click', function() {
        tedTab.classList.remove('tab-on')
        tedxTab.classList.remove('tab-on')
        tedxlavasanTab.classList.remove('tab-on')

        tedxTab.classList.add('tab-on')
        abouttedtext.innerHTML = "درباره تدکس"
    })
    tedxlavasanTab.addEventListener('click', function() {
        tedTab.classList.remove('tab-on')
        tedxTab.classList.remove('tab-on')
        tedxlavasanTab.classList.remove('tab-on')

        tedxlavasanTab.classList.add('tab-on')
        abouttedtext.innerHTML = "درباره تدکس لواسان"
    })
}

function aboutlavasansection() {
    historyTab.addEventListener('click', function() {
        historyTab.classList.remove('tab-on')
        attrTab.classList.remove('tab-on')
        whattoseeTab.classList.remove('tab-on')

        historyTab.classList.add('tab-on')
        aboutlavasantext.innerHTML = "تاریخچه"
    })
    attrTab.addEventListener('click', function() {
        historyTab.classList.remove('tab-on')
        attrTab.classList.remove('tab-on')
        whattoseeTab.classList.remove('tab-on')

        attrTab.classList.add('tab-on')
        aboutlavasantext.innerHTML = "ویژگی های شهر"
    })
    whattoseeTab.addEventListener('click', function() {
        historyTab.classList.remove('tab-on')
        attrTab.classList.remove('tab-on')
        whattoseeTab.classList.remove('tab-on')

        whattoseeTab.classList.add('tab-on')
        aboutlavasantext.innerHTML = "دیدنی ها"
    })
}


//funcs
function SectionShow(section) {
    // console.log(section);
    if (section.classList.contains("hide")) {
        section.style.display = 'flex'

        setTimeout(function() {
            section.classList.remove("hide")
        }, 100)
    } else {
        section.classList.add("hide")

        setTimeout(function() {
            section.style.display = 'none'
        }, 300);
    };
};

function HideSection(section) {
    section.classList.add("hide")

    setTimeout(function() {
        section.style.display = 'none'
    }, 300);
}

// map
function map() {
    var map = L.map('map').setView([35.81781315869664, 51.6353988647461], 15);
    L.tileLayer('https://api.maptiler.com/maps/streets/{z}/{x}/{y}.png?key=8x7yGIOEBdKVjAChWqmG', {
        attribution: '<a href="https://www.maptiler.com/copyright/" target="_blank">&copy; MapTiler</a> <a href="https://www.openstreetmap.org/copyright" target="_blank">&copy; OpenStreetMap contributors</a>',
    }).addTo(map);

    var marker = L.marker([35.81781315869664, 51.6353988647461], { opacity: 0.9, title: 'false' }).addTo(map);
    marker.bindPopup('popup').openPopup();
}


navMenu.addEventListener('click', function() {
    navLinks.classList.toggle('nav-show')
    container.classList.toggle('show-menu-highlight')
    document.querySelector('.l1').classList.toggle('toggle')
    document.querySelector('.l2').classList.toggle('toggle')
    document.querySelector('.l3').classList.toggle('toggle')


});


const abouttabsSmall = document.querySelectorAll('.small')
const abouttabsLarge = document.querySelectorAll('.large')
    // media q


function mediaq() {
    var mobile = window.matchMedia("(max-width: 620px)")
    var tablet = window.matchMedia("(max-width: 960px)")
    if (mobile.matches) {
        // mobile
        smallQuery()
        abouttedsection()
        aboutlavasansection()

    } else if (tablet.matches) {
        abouttedsection()
        aboutlavasansection()
        console.log('tablets');
        smallQuery()
    } else {
        // laptops
        navLinks.classList.remove('nav-show')

        abouttabsSmall.forEach(element => {
            element.classList.add('nodisplay')
        })

        window.onscroll = function() {
            // under home section
            if (document.documentElement.scrollTop > 165) {
                navLinks.classList.remove('nav-home')
                navLinks.classList.remove('nav-show-desktop')
                container.classList.remove('show-menu-highlight')
                navMenu.classList.remove('hide')
                document.querySelector('.l1').classList.remove('toggle')
                document.querySelector('.l2').classList.remove('toggle')
                document.querySelector('.l3').classList.remove('toggle')
            } else {
                // home section
                navLinks.classList.add('nav-home')
                navLinks.classList.add('nav-show-desktop')
                navMenu.classList.add('hide')
            };

            if (navLinks.classList.contains("nav-show-desktop")) {
                navLinks.classList.add('nav-show-desktop')

            } else {
                navLinks.classList.remove('nav-show-desktop')

            };
        };

    }
}
mediaq()

function smallQuery() {
    window.onscroll = function() {
        if (document.documentElement.scrollTop > 165) {
            // under home section
            navLinks.classList.remove('nav-home')
            navLinks.classList.remove('nav-show')
            container.classList.remove('show-menu-highlight')
            navMenu.classList.remove('hide')
            document.querySelector('.l1').classList.remove('toggle')
            document.querySelector('.l2').classList.remove('toggle')
            document.querySelector('.l3').classList.remove('toggle')
        } else {
            // home section
            navLinks.classList.add('nav-home')
            navLinks.classList.add('nav-show')
            navMenu.classList.add('hide')
        };

        if (navLinks.classList.contains("nav-show")) {
            navLinks.classList.add('nav-show')

        } else {
            navLinks.classList.remove('nav-show')

        };
    };
    abouttabsLarge.forEach(element => {
        element.classList.add('nodisplay')
    });
}

// sections const
const HomeSection = document.querySelector('.home')
const speakersSection = document.querySelector('.speakers')
const sponsorsSection = document.querySelector('.sponsors-section')
const teamSection = document.querySelector('.team-section')
let abouttedSection;
let aboutlavasanSection;

const abouttedSections = document.querySelectorAll('.aboutted')
const aboutlavasanSections = document.querySelectorAll('.aboutlavasan')
abouttedSections.forEach(element => {
    if (element.classList.contains("nodisplay")) {
        console.log('n')
    } else {
        abouttedSection = element
        console.log(element);
    }
})
aboutlavasanSections.forEach(element => {
    if (element.classList.contains("nodisplay")) {
        console.log('n')
    } else {
        aboutlavasanSection = element
        console.log(element);
    }
})

// change nav color on scroll
function changecl(a, section) {
    const y = window.scrollY
    const e = section.offsetTop;

    if (y >= e) {
        navLink.forEach(link => {
            link.style.color = '#fff'
            link.style.fontWeight = 500
            link.style.opacity = 0.8
        });
        navLink[a].style.fontWeight = 'bold'
        navLink[a].style.color = 'var(--red)'
        navLink[a].style.opacity = 1
    }

}

function scrollFn() {
    changecl(0, HomeSection)
    changecl(1, abouttedSection)
    changecl(2, speakersSection)
    changecl(3, sponsorsSection)
    changecl(4, aboutlavasanSection)
    changecl(5, teamSection)
};

// scroll to section on nav click
function scrollToSection(linkIndex, section) {
    navLink[linkIndex].addEventListener('click', function() {
        section.scrollIntoView({ behavior: 'smooth' })
    });
};
scrollToSection(0, HomeSection)
scrollToSection(1, abouttedSection)
scrollToSection(2, speakersSection)
scrollToSection(3, sponsorsSection)
scrollToSection(4, aboutlavasanSection)
scrollToSection(5, teamSection)