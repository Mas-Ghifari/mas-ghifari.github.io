---
layout: single
title: "Invited Lectures & Visiting Professorships"
permalink: /lectures/invited/
author_profile: true
---

Below is the record of invited lectures, visiting professorships, and workshop speaking engagements across national and international institutions.

---

<table>
  <thead>
    <tr>
      <th style="width: 8%; text-align: center;">No.</th>
      <th style="width: 18%; text-align: center;">Date / Year</th>
      <th>Event / Teaching Activity</th>
      <th>Institution / Location</th>
    </tr>
  </thead>
  <tbody>
    {% assign index = 0 %}
    {% for item in site.data.portfolio.invited_lectures %}
      {% assign index = index | plus: 1 %}
      <tr>
        <td style="text-align: center;">{{ index }}</td>
        <td style="text-align: center;">{{ item.date }}</td>
        <td><b>{{ item.title }}</b></td>
        <td>{{ item.institution }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>
