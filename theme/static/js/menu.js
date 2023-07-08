document.addEventListener("DOMContentLoaded", function() {
    const menuToggle = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");
    const languages = document.querySelector(".languages");
    const mobileBackground = document.querySelector('.mobile-background');

    menuToggle.addEventListener("click", () => {
      menu.classList.toggle("active");
      languages.classList.toggle("active");
      mobileBackground.classList.toggle('active');
    });

    const menuItemsList = document.querySelector(".menu-items-list");
    menuItemsList.addEventListener("click", (event) => {
        menu.classList.toggle("active");
        languages.classList.toggle("active");
        mobileBackground.classList.toggle('active');
    })
  });
