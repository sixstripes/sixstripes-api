function app() {
  const search = document.querySelector(".search-input");
  const navLinks = document.querySelectorAll('a[data-link]');
  
  function update() {
    const searchChild = document.querySelector('div[data-role="search:results"]');
    const notFound = document.querySelector('.not-found');
    
    if (search.value.length > 3 && !searchChild && !notFound) {
      const tag = document.createElement("p");
      const text = document.createTextNode("Não encontrado");
      tag.appendChild(text);
      
      search.parentNode.appendChild(tag).classList.add("not-found");
    }

    if (search.value.length < 4 && notFound) {
      notFound.parentNode.removeChild(notFound);
    }

    if (notFound) {
      const closeSearch = document.querySelector('.menu-content > div > i');

      closeSearch.addEventListener("click", function () {
        notFound.parentNode.removeChild(notFound);
      });
    }
  }

  for (var i = 0; i < navLinks.length; i++) {
    navLinks[i].addEventListener('click', function () {
      if (this.getAttribute('data-link') === 'docs') {
        navLinks[1].classList.remove('-active');
        
        this.classList.add('-active');
      }
      
      if (this.getAttribute('data-link') === 'collaborate') {
        navLinks[0].classList.remove('-active');

        this.classList.add('-active');
      }
    });
  }

  search.addEventListener("keyup", update);
}

window.app = app;
