---
layout: page
permalink: /publications/
title: publications
description: Research papers and manuscripts.
nav: true
nav_order: 4
---

<style>
  .publications ol.bibliography > li > .row {
    display: grid;
    grid-template-columns: 10rem minmax(0, 1fr);
    gap: 2rem;
    margin-right: 0;
    margin-left: 0;
  }

  .publications ol.bibliography > li > .row > [class*="col"] {
    width: auto;
    max-width: none;
    padding-right: 0;
    padding-left: 0;
  }

  .publications .abbr figure {
    width: 100%;
    margin: 0.5rem 0 0;
    aspect-ratio: 1;
  }

  .publications .abbr figure img.preview {
    width: 100%;
    height: 100%;
    object-fit: contain;
  }

  @media (max-width: 575.98px) {
    .publications ol.bibliography > li > .row {
      grid-template-columns: 7rem minmax(0, 1fr);
      gap: 1rem;
    }
  }
</style>

{% include bib_search.liquid %}

<div class="publications">

{% bibliography %}

</div>
