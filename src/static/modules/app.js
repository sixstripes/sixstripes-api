function app() {
  const search = document.querySelector(".search-input");

  function update() {
    console.log("foi");
  }

  search.addEventListener("change", update);
  console.log("caceta")
}

window.app = app;
