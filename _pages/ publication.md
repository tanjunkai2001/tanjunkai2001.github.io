---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

<!-- Journal Publications (Sorted by date, newest first) -->
<h2>Journal Publications</h2>
<div class="publications">
  {% assign journal_pubs = site.publications | where: "type", "journal" | sort: "date" | reverse %}
  {% for post in journal_pubs %}
    {% include archive-single.html %}
  {% endfor %}
</div>

<!-- Conference Publications (Sorted by date, newest first) -->
<h2>Conference Publications</h2>
<div class="publications">
  {% assign conf_pubs = site.publications | where: "type", "conference" | sort: "date" | reverse %}
  {% for post in conf_pubs %}
    {% include archive-single.html %}
  {% endfor %}
</div>