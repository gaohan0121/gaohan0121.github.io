---
layout: default
permalink: /blog/
title: blog
nav: true
nav_order: 2
pagination:
  enabled: true
  collection: posts
  permalink: /page/:num/
  per_page: 5
  sort_field: date
  sort_reverse: true
  trail:
    before: 1
    after: 3
---

<style>
  .academic-blog-filters {
    display: flex;
    flex-direction: column;
    gap: 3rem;
    margin: 1.6rem 0 2.1rem;
    padding: 2.5rem 0;
    border-bottom: 1px solid var(--global-divider-color);
    font-size: 1.08rem;
  }

  .academic-blog-filter-row {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 0.85rem;
  }

  .academic-blog-topic {
    display: inline-flex;
    align-items: center;
    white-space: nowrap;
  }

  .academic-blog-topic:not(:last-child)::after {
    margin-left: 0.85rem;
    color: var(--global-text-color-light);
    content: "\2022";
  }

  .academic-blog-filter,
  .academic-blog-filter:hover {
    text-decoration: none;
  }

  .academic-blog-filter i {
    color: var(--global-text-color-light);
  }

  .academic-blog-featured {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
    margin: 0 0 2rem;
  }

  .academic-blog-card {
    position: relative;
    height: 100%;
    min-height: 11rem;
    padding: 1.15rem 1.25rem;
    color: var(--global-text-color);
    background: var(--global-card-bg-color, var(--global-bg-color));
    border: 1px solid var(--global-divider-color);
    border-radius: 0.35rem;
    box-shadow: 0 2px 8px color-mix(in srgb, var(--global-text-color) 12%, transparent);
    transition:
      transform 0.2s ease,
      box-shadow 0.2s ease;
  }

  .academic-blog-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 5px 14px color-mix(in srgb, var(--global-text-color) 16%, transparent);
  }

  .academic-blog-card h3 {
    margin: 0 1.4rem 0.6rem 0;
    color: var(--global-text-color);
    font-size: 1.35rem;
  }

  .academic-blog-pin {
    position: absolute;
    top: 1rem;
    right: 1rem;
    color: var(--global-text-color);
  }

  .academic-blog-card .post-meta {
    margin-bottom: 0;
  }

  @media (max-width: 767.98px) {
    .academic-blog-filters {
      gap: 1rem;
      padding: 1.4rem 0.25rem;
      font-size: 0.95rem;
    }

    .academic-blog-filter-row {
      gap: 0.7rem 0.9rem;
    }

    .academic-blog-topic:not(:last-child)::after {
      margin-left: 0.9rem;
    }

    .academic-blog-featured {
      grid-template-columns: 1fr;
    }

    .academic-blog-card {
      min-height: 0;
    }
  }
</style>

<div class="post">

{% assign blog_name_size = site.blog_name | size %}
{% assign blog_description_size = site.blog_description | size %}
{% if blog_name_size > 0 or blog_description_size > 0 %}

  <div class="header-bar">
    <h1>{{ site.blog_name }}</h1>
    <h2>{{ site.blog_description }}</h2>
  </div>
{% endif %}

{% if site.display_tags and site.display_tags.size > 0 or site.display_categories and site.display_categories.size > 0 %}

  <nav class="academic-blog-filters" aria-label="Blog topics">
    <div class="academic-blog-filter-row">
      {% for tag in site.display_tags limit: 5 %}
        <span class="academic-blog-topic">
          <a class="academic-blog-filter" href="{{ tag | slugify | prepend: '/blog/tag/' | relative_url }}"><i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }}</a>
        </span>
      {% endfor %}
    </div>
    <div class="academic-blog-filter-row">
      {% for tag in site.display_tags offset: 5 %}
        <span class="academic-blog-topic">
          <a class="academic-blog-filter" href="{{ tag | slugify | prepend: '/blog/tag/' | relative_url }}"><i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }}</a>
        </span>
      {% endfor %}
      {% for category in site.display_categories %}
        <span class="academic-blog-topic">
          <a class="academic-blog-filter" href="{{ category | slugify | prepend: '/blog/category/' | relative_url }}"><i class="fa-solid fa-tag fa-sm"></i> {{ category }}</a>
        </span>
      {% endfor %}
    </div>
  </nav>
{% endif %}

{% assign featured_posts = site.posts | where: "featured", "true" %}
{% if featured_posts.size > 0 %}

  <div class="academic-blog-featured" aria-label="Featured posts">
    {% for post in featured_posts %}
      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
      {% assign year = post.date | date: "%Y" %}
      <article class="academic-blog-card">
        <i class="academic-blog-pin fa-solid fa-thumbtack fa-xs" aria-hidden="true"></i>
        <h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.description }}</p>
        <p class="post-meta">
          {{ read_time }} min read &nbsp; &middot; &nbsp;
          <a href="{{ year | prepend: '/blog/' | relative_url }}"><i class="fa-solid fa-calendar fa-sm"></i> {{ year }}</a>
        </p>
      </article>
    {% endfor %}
  </div>
  <hr>
{% endif %}

  <ul class="post-list">
    {% if page.pagination.enabled %}
      {% assign postlist = paginator.posts %}
    {% else %}
      {% assign postlist = site.posts %}
    {% endif %}

    {% for post in postlist %}
      {% assign read_time = post.content | number_of_words | divided_by: 180 | plus: 1 %}
      {% assign year = post.date | date: "%Y" %}
      {% assign tags = post.tags | join: "" %}
      {% assign categories = post.categories | join: "" %}
      <li>
        <h3><a class="post-title" href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p>{{ post.description }}</p>
        <p class="post-meta">{{ read_time }} min read &nbsp; &middot; &nbsp; {{ post.date | date: '%B %d, %Y' }}</p>
        <p class="post-tags">
          <a href="{{ year | prepend: '/blog/' | relative_url }}"><i class="fa-solid fa-calendar fa-sm"></i> {{ year }}</a>
          {% if tags != "" %}
            &nbsp; &middot; &nbsp;
            {% for tag in post.tags %}
              <a href="{{ tag | slugify | prepend: '/blog/tag/' | relative_url }}"><i class="fa-solid fa-hashtag fa-sm"></i> {{ tag }}</a>{% unless forloop.last %}&nbsp;{% endunless %}
            {% endfor %}
          {% endif %}
          {% if categories != "" %}
            &nbsp; &middot; &nbsp;
            {% for category in post.categories %}
              <a href="{{ category | slugify | prepend: '/blog/category/' | relative_url }}"><i class="fa-solid fa-tag fa-sm"></i> {{ category }}</a>{% unless forloop.last %}&nbsp;{% endunless %}
            {% endfor %}
          {% endif %}
        </p>
      </li>
    {% endfor %}

  </ul>

{% if page.pagination.enabled %}
{% include pagination.liquid %}
{% endif %}

</div>
