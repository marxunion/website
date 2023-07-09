document.addEventListener("DOMContentLoaded", () => {
    const menuToggle = document.querySelector(".menu-toggle");
    const menu = document.querySelector(".menu");
    const languages = document.querySelector(".languages");
    const mobileBackground = document.querySelector('.mobile-background');

    function closeMenu(){
        menu.classList.toggle("active");
        languages.classList.toggle("active");
        mobileBackground.classList.toggle('active');
    }

    menuToggle.addEventListener("click",  () => {
        closeMenu();
    });

    const menuItemsList = document.querySelector(".menu-items-list");
    menuItemsList.addEventListener("click", (event) => {
        console.log('menuItemsList');
        closeMenu();
    });
    const mobileMenuBackground = document.querySelector(".mobile-background");
    mobileMenuBackground.addEventListener("click", (event) => {
        console.log('mobileMenuBackground');
        closeMenu();
    });
    const languagesList = document.querySelector('.languages-list');
    languagesList.addEventListener("click", (event) => {
        console.log('languagesList');
        closeMenu();
    });
  });
