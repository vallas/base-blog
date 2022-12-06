import Searcher from "./vendor/searcher/searcher.js";
// add carousel https://github.com/oom-components/carousel 
// other components: https://github.com/oom-components 

customElements.define("oom-search", Searcher);


document.addEventListener("keydown", function(e) {
  if (e.metaKey && e.code === "KeyK") {
    console.log('Alt+C working 🟢')
    const component = document.getElementById("search");
    const input = component.input;
    input.focus();
  }
});

const __filename = new URL('', import.meta.url).pathname;
console.log('Current directory: ' + __filename); 

console.log("hello")

