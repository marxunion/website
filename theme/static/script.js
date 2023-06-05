document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");
    const languages = document.querySelector(".languages");

    menuToggle.addEventListener("click", function() {
      menu.classList.toggle("active");
      languages.classList.toggle("active");
    });
  });

  var hamburgerButton = document.getElementById('hamburger-button');
  var menuToggle = document.querySelector('.menu-toggle');
  
  hamburgerButton.addEventListener('click', function() {
    menuToggle.classList.toggle('active');
  });