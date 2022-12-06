export const title = "Welcome to my page";
export const layout = "layouts/main.njk";

export default (data) => (
  <>
    <h1>{data.title}</h1>
    <p class="">This is my first post using lume. I hope you like it!</p>
  </>
);

// https://lume.land/plugins/jsx_preact/ 
