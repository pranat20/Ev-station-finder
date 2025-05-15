

(function() {
  "use strict";

  


  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  
  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  if (mobileNavToggleBtn) {
    mobileNavToggleBtn.addEventListener('click', mobileNavToogle);
  }
  
  

  

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function(e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Auto generate the carousel indicators
   */
  document.querySelectorAll('.carousel-indicators').forEach((carouselIndicator) => {
    carouselIndicator.closest('.carousel').querySelectorAll('.carousel-item').forEach((carouselItem, index) => {
      if (index === 0) {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}" class="active"></li>`;
      } else {
        carouselIndicator.innerHTML += `<li data-bs-target="#${carouselIndicator.closest('.carousel').id}" data-bs-slide-to="${index}"></li>`;
      }
    });
  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function(swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  function showFeaturePopup(event) {
    event.preventDefault();
    document.getElementById("feature-overlay").style.display = "block";
  }

  function closeFeaturePopup() {
    document.getElementById("feature-overlay").style.display = "none";
  }

  // main.js

  document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector(".php-email-form");
    
    if (form) {
        form.addEventListener("submit", function(e) {
            e.preventDefault();  // Prevent default submission

            const name = form.querySelector("[name='name']").value;
            const email = form.querySelector("[name='email']").value;
            const subject = form.querySelector("[name='subject']").value;
            const message = form.querySelector("[name='message']").value;

            // Simple validation check
            if (!name || !email || !subject || !message) {
                alert("Please fill out all fields.");
                return;
            }

            // If form is valid, submit it
            form.submit();
        });
    }
});


document.addEventListener("DOMContentLoaded", function () {
  const msg = document.getElementById("success-msg");
  if (msg) {
      setTimeout(() => {
          msg.style.opacity = "0";
      }, 7000); // fades after 5 seconds
  }
});


document.addEventListener("DOMContentLoaded", function() {
  var successMessage = document.getElementById('successMessage');
  if (successMessage) {
      setTimeout(function() {
          successMessage.style.transition = "opacity 1s ease-out";
          successMessage.style.opacity = 0;
          setTimeout(function() {
              successMessage.style.display = "none";
          }, 1000); // 1 second after fade-out
      }, 3000); // 3 seconds delay before fading
  }
});

document.addEventListener("DOMContentLoaded", function() {
 
  const messages = document.querySelectorAll(".messages li");

  
  messages.forEach(msg => {
    
    setTimeout(() => {
      msg.classList.add("fade-out");
      
      
      setTimeout(() => {
        msg.remove();  // Remove the message completely after fade
      }, 2000); // Wait for the fade-out transition to complete
    }, 1000); // 3-second delay before fading out
  });
});




  
})();






