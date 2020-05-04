function app() {
  const search = document.querySelector(".search-input");
  
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

  search.addEventListener("keyup", update);
}

window.app = app;
