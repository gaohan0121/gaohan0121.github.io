---
layout: about
title: about
permalink: /
subtitle: Undergraduate Student · Software Engineering · Xi'an Jiaotong University

profile:
  align: right
  image: profile.jpg
  image_circular: true
  more_info: >
    <p>Xi'an Jiaotong Univ.</p>
    <p>28 Xianning W. Rd.</p>
    <p>Xi'an 710049, China</p>

selected_papers: true
social: true

announcements:
  enabled: false

latest_posts:
  enabled: false
---

<style>
  .post-header .post-title {
    font-weight: 700;
  }

  .post article h2 {
    text-transform: capitalize;
  }

  @media (min-width: 576px) {
    .profile.float-right {
      width: 22%;
    }
  }

  .academic-news {
    --news-date-width: 4.8rem;
    --news-column-gap: 2.2rem;
    --news-axis-left: 5.88rem;

    position: relative;
    margin: 0.85rem 0 2rem;
    overflow: hidden;
  }

  .academic-news::before {
    position: absolute;
    top: 0.55rem;
    bottom: 0.55rem;
    left: var(--news-axis-left);
    width: 2px;
    content: "";
    background: var(--global-theme-color);
    opacity: 0.28;
  }

  .academic-news-item {
    position: relative;
    display: grid;
    grid-template-columns: var(--news-date-width) 1fr;
    column-gap: var(--news-column-gap);
    margin-bottom: 1rem;
  }

  .academic-news-item::before {
    position: absolute;
    top: 0.74em;
    left: calc(var(--news-axis-left) - 0.3rem);
    z-index: 1;
    width: 0.6rem;
    height: 0.6rem;
    content: "";
    background: var(--global-theme-color);
    border-radius: 50%;
    transform: translateY(-50%);
  }

  .academic-news-item:last-child {
    margin-bottom: 0;
  }

  .academic-news-date {
    font-weight: 600;
    text-align: right;
    white-space: nowrap;
  }

  .academic-news-content strong {
    font-weight: 600;
  }

  .academic-entry {
    margin-bottom: 0.2rem;
  }

  .academic-entry:last-child {
    margin-bottom: 0;
  }

  .academic-entry-meta {
    color: var(--global-text-color-light);
    font-size: 0.95rem;
  }

  .academic-list {
    margin: 0 0 1.75rem;
    padding: 0;
    list-style: none;
  }

  .academic-list > li {
    position: relative;
    margin-bottom: 0.7rem;
    padding-left: 1.65rem;
  }

  .academic-list > li:last-child {
    margin-bottom: 0;
  }

  .academic-list > li::before {
    position: absolute;
    top: 0.72em;
    left: 0.18rem;
    width: 0.65rem;
    height: 0.65rem;
    content: "";
    background: var(--global-bg-color);
    border: 2px solid var(--global-theme-color);
    border-radius: 50%;
    transform: translateY(-50%);
  }

  .academic-education {
    margin-bottom: 1.75rem;
  }

  @media (max-width: 575.98px) {
    .profile.float-right {
      float: none !important;
      width: 72%;
      max-width: 240px;
      margin-right: auto;
      margin-bottom: 1rem;
      margin-left: auto;
    }

    .academic-news {
      --news-date-width: 3.1rem;
      --news-column-gap: 2rem;
      --news-axis-left: 4.1rem;
    }
  }
</style>

I am an undergraduate student in Software Engineering at Xi'an Jiaotong University. I have passed both the College English Test Band 4 (CET-4) and Band 6 (CET-6), with a CET-6 score of **647**.

In 2027, I will begin graduate study in Software Engineering at the School of Software Technology, Zhejiang University (Ningbo).

Currently I work on Multimodal Large Language Models (MLLMs) for Hyperspectral Image Change Detection (HSICD), Synthetic Aperture Radar (SAR)-RGB cross-modal retrieval, and Multi-Agent Systems (MAS).

> 你目前看到的是一个未完成的版本，仅作为格式参考，不保证任何内容的真实性。

## News

<div class="academic-news" aria-label="Academic news">
  <div class="academic-news-item">
    <div class="academic-news-date">2027</div>
    <div class="academic-news-content"><strong>Graduate study</strong> at the School of Software Technology, Zhejiang University (Ningbo).</div>
  </div>
  <div class="academic-news-item">
    <div class="academic-news-date">2026</div>
    <div class="academic-news-content">Admitted to Zhejiang University through the recommended graduate admission pathway.</div>
  </div>
  <div class="academic-news-item">
    <div class="academic-news-date">2025</div>
    <div class="academic-news-content">Received the University Second-Class Scholarship and was recognized as an Outstanding Student Leader.</div>
  </div>
  <div class="academic-news-item">
    <div class="academic-news-date">2024</div>
    <div class="academic-news-content">Received the University Third-Class Scholarship and was recognized as an Outstanding Student Leader.</div>
  </div>
  <div class="academic-news-item">
    <div class="academic-news-date">2023</div>
    <div class="academic-news-content">Began the B.E. program in Software Engineering at Xi'an Jiaotong University.</div>
  </div>
</div>

<div style="clear: both;"></div>

## Education

<ul class="academic-list academic-education">
  <li>
    <div class="academic-entry">
      <strong>Zhejiang University</strong>
      <div>Software Engineering</div>
      <div class="academic-entry-meta">School of Software Technology, Ningbo · From 2027</div>
    </div>
  </li>
  <li>
    <div class="academic-entry">
      <strong>Xi'an Jiaotong University</strong>
      <div>B.E. in Software Engineering</div>
      <div class="academic-entry-meta">School of Software Engineering · 2023-2027</div>
    </div>
  </li>
</ul>

## Honors

<ul class="academic-list">
  <li>University Second-Class Scholarship, 2025</li>
  <li>University Third-Class Scholarship, 2024</li>
  <li>Outstanding Student Leader, 2024 and 2025</li>
  <li>Honorable Mention, Mathematical Contest in Modeling/Interdisciplinary Contest in Modeling (MCM/ICM)</li>
</ul>

## Research Interests

<ul class="academic-list">
  <li>Multimodal Large Language Models (MLLMs)</li>
  <li>Remote Sensing Foundation Models (RSFMs)</li>
  <li>Vision-Language Learning (VLL)</li>
  <li>Hyperspectral Image Change Detection (HSICD)</li>
  <li>Synthetic Aperture Radar (SAR)-RGB Cross-modal Retrieval</li>
  <li>Agentic Artificial Intelligence (Agentic AI) and Multi-Agent Systems (MAS)</li>
</ul>
