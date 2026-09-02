---
layout: single
title: "Awards and Grants"
permalink: /awards/
author_profile: true
---

### ACQUIRED RESEARCH GRANTS

| Year | Research Title | Sources of Funding |
| :---: | :--- | :--- |
{% for item in site.data.portfolio.grants %}| {{ item.year }} | {{ item.title }} **({{ item.role }})**. | {{ item.funding }} |
{% endfor %}

---

### ACADEMIC AWARDS

| Year | Award / Recognition |
| :---: | :--- |
{% for item in site.data.portfolio.awards %}| {{ item.year }} | {{ item.title }} |
{% endfor %}
