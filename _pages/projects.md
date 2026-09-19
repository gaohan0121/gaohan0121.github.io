---
layout: page
title: projects
permalink: /projects/
description: Selected research and engineering projects.
nav: true
nav_order: 4
horizontal: true
---

<div class="projects">
{% assign sorted_projects = site.projects | sort: "importance" %}
<div class="container">
  <div class="row row-cols-1">
  {% for project in sorted_projects %}
    {% include projects_horizontal.liquid %}
  {% endfor %}
  </div>
</div>
</div>
