---
layout: single
title: "Regular Lectures"
permalink: /lectures/regular/
author_profile: true
---

Below is the record of regular teaching activities across undergraduate and postgraduate programs.

---

<h3>UNDERGRADUATE COURSES</h3>

<table>
  <thead>
    <tr>
      <th style="width: 8%; text-align: center;">No.</th>
      <th>Course Title</th>
      <th style="width: 15%; text-align: center;">Level</th>
      <th>Institution / Department</th>
      <th style="width: 20%; text-align: center;">Academic Years</th>
    </tr>
  </thead>
  <tbody>
    {% assign ug_index = 0 %}
    {% for item in site.data.portfolio.regular_lectures %}
      {% if item.level == "Bachelor" %}
        {% assign ug_index = ug_index | plus: 1 %}
        <tr>
          <td style="text-align: center;">{{ ug_index }}</td>
          <td>
            <b>{{ item.course_title }}</b>
            {% if item.indonesian_title %}<br><i>({{ item.indonesian_title }})</i>{% endif %}
          </td>
          <td style="text-align: center;">{{ item.level }}</td>
          <td>{{ item.institution }}</td>
          <td style="text-align: center;">{{ item.academic_years }}</td>
        </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>

<hr style="margin: 30px 0;">

<h3>POSTGRADUATE COURSES</h3>

<table>
  <thead>
    <tr>
      <th style="width: 8%; text-align: center;">No.</th>
      <th>Course Title</th>
      <th style="width: 15%; text-align: center;">Level</th>
      <th>Institution / Department</th>
      <th style="width: 20%; text-align: center;">Academic Years</th>
    </tr>
  </thead>
  <tbody>
    {% assign pg_index = 0 %}
    {% for item in site.data.portfolio.regular_lectures %}
      {% if item.level == "Master" or item.level == "Doctoral" %}
        {% assign pg_index = pg_index | plus: 1 %}
        <tr>
          <td style="text-align: center;">{{ pg_index }}</td>
          <td>
            <b>{{ item.course_title }}</b>
            {% if item.indonesian_title %}<br><i>({{ item.indonesian_title }})</i>{% endif %}
          </td>
          <td style="text-align: center;">{{ item.level }}</td>
          <td>{{ item.institution }}</td>
          <td style="text-align: center;">{{ item.academic_years }}</td>
        </tr>
      {% endif %}
    {% endfor %}
  </tbody>
</table>
