---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

[Journal Articles](#journal-articles)\
[Conference Papers](#conference-papers)\
[White Papers](#white-papers)\
[Academic](#academic)\
[Presentations](#presentations)

{% if site.author.googlescholar %}
  You can also find my articles on <u><a href="{{site.author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

## Journal Articles
{% for post in site.publications reversed %}
  {% if post.pubtype == 'journal' %}
    <div class="publication-entry">
      {% if post.coverimage %}
        <div class="publication-image">
          <img src="{{ post.coverimage | prepend: "/images/" | prepend: base_path }}" alt="{{ post.title }} cover image"> <!-- add cover image, image name: post title -->
        </div>
        <div class="publication-info">
          {% include archive-single.html %}
        </div>
      {% else %}
        {% include archive-single.html %}
      {% endif %}
    </div>
    <style>
      .publication-entry {
        display: flex;
        margin-bottom: 20px;
      }
      .publication-image {
        flex: 0 0 200px;
        margin-right: 20px;
      }
      .publication-image img {
        max-width: 100%;
        height: auto;
      }
      .publication-info {
        flex: 1;
      }
    </style>
  {% endif %}
{% endfor %}


## Conference Papers
{% for post in site.publications reversed %}
  {% if post.pubtype == 'conference' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

## White Papers
{% for post in site.publications reversed %}
  {% if post.pubtype == 'whitepaper' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}


## Academic
{% for post in site.publications reversed %}
  {% if post.pubtype == 'academic' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Presentations
{% for post in site.publications reversed %}
  {% if post.pubtype == 'presentation' %}
      {% include archive-single.html %}
  {% endif %}
{% endfor %}
