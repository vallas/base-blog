---
layout: layouts/post.njk 
title: FaceAI
templateClass: tmpl-post
menu:
  visible: true
  order: 2
---

<script>
import { setup, tw } from "https://esm.sh/twind@0.16.16";
import { getStyleTag, virtualSheet } from "https://esm.sh/twind@0.16.16/sheets";

</script>

<h1 style="center"></h1>

# Hello world

<script>
navigator.clipboard.writeText("This is the text to be copied").then(() => {
  console.log('Content copied to clipboard');
  /* Resolved - text copied to clipboard successfully */
},() => {
  console.error('Failed to copy');
  /* Rejected - text failed to copy to the clipboard */
});
</script>
