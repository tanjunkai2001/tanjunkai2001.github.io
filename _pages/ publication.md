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

## Journal Articles (First Author/First Student Author)

{% for post in site.publications reversed %}
  {% if post.pubtype == 'journal' %}
    {% include archive-single_V2.html %}
  {% endif %}
{% endfor %}


## Conference Papers
{% for post in site.publications reversed %}
  {% if post.pubtype == 'conference' %}
      {% include archive-single_V1.html %}
  {% endif %}
{% endfor %}

## White Papers
{% for post in site.publications reversed %}
  {% if post.pubtype == 'whitepaper' %}
      {% include archive-single_V1.html %}
  {% endif %}
{% endfor %}


## Academic
{% for post in site.publications reversed %}
  {% if post.pubtype == 'academic' %}
      {% include archive-single_V3.html %}
  {% endif %}
{% endfor %}

## Presentations
{% for post in site.publications reversed %}
  {% if post.pubtype == 'presentation' %}
      {% include archive-single_V1.html %}
  {% endif %}
{% endfor %}
