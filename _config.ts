import lume from "lume/mod.ts";
import date from "lume/plugins/date.ts";
import postcss from "lume/plugins/postcss.ts";
import terser from "lume/plugins/terser.ts";
import codeHighlight from "lume/plugins/code_highlight.ts";
import windi from "lume/plugins/windi_css.ts";
import basePath from "lume/plugins/base_path.ts";
import slugifyUrls from "lume/plugins/slugify_urls.ts";
import resolveUrls from "lume/plugins/resolve_urls.ts";
import netlifyCMS from "lume/plugins/netlify_cms.ts";
import gpm from "https://deno.land/x/gpm@v0.4.1/mod.ts";
import jsx from "lume/plugins/jsx.ts";
import mdx from "https://raw.githubusercontent.com/lumeland/experimental-plugins/main/remark-mdx/mod.ts";
import onDemand from "lume/plugins/on_demand.ts";

const site = lume({
  // location: new URL("https://myweb.netlify.app"),
});

site
  
  .ignore("README.md")
  .copy("favicon.ico")
  .copy("img")  
  .use(postcss())
  .use(terser())
  .use(date())
  .use(windi())
  .use(codeHighlight())
  .use(basePath())
  .use(slugifyUrls({ alphanumeric: false }))
  .use(resolveUrls())
  .use(netlifyCMS({ netlifyIdentity: true }))
  .use(jsx())
  .use(mdx())
  .use(onDemand())
  .addEventListener(
    "beforeBuild",
    () => gpm(["oom-components/searcher"], "js/vendor"),
  );

export default site;
