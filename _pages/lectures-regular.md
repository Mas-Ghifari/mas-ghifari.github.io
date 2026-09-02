---
layout: single
title: "Regular Lectures"
permalink: /lectures/regular/
author_profile: true
---

Below is the record of regular teaching activities across undergraduate and postgraduate programs.

---

### UNDERGRADUATE COURSES

| No. | Course Title | Level | Institution / Department | Academic Years |
| :---: | :--- | :---: | :--- | :--- |
{% assign ug_index = 0 %}
{% for item in site.data.portfolio.regular_lectures %}
  {% if item.level == "Bachelor" %}
    {% assign ug_index = ug_index | plus: 1 %}
| {{ ug_index }} | **{{ item.course_title }}**{% if item.indonesian_title %} <br> *({{ item.indonesian_title }})*{% endif %} | {{ item.level }} | {{ item.institution }} | {{ item.academic_years }} |
  {% endif %}
{% endfor %}

---

### POSTGRADUATE COURSES

| No. | Course Title | Level | Institution / Department | Academic Years |
| :---: | :--- | :---: | :--- | :--- |
{% assign pg_index = 0 %}
{% for item in site.data.portfolio.regular_lectures %}
  {% if item.level == "Master" or item.level == "Doctoral" %}
    {% assign pg_index = pg_index | plus: 1 %}
| {{ pg_index }} | **{{ item.course_title }}**{% if item.indonesian_title %} <br> *({{ item.indonesian_title }})*{% endif %} | {{ item.level }} | {{ item.institution }} | {{ item.academic_years }} |
  {% endif %}
{% endfor %}
