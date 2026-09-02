---
layout: single
title: "Services"
permalink: /services/
author_profile: true
---

Below is the record of professional affiliations, academic reviews, community services, and institutional contributions.

---

<h3>PROFESSIONAL AFFILIATIONS & MEMBERSHIPS</h3>

<table>
  <thead>
    <tr>
      <th style="width: 20%; text-align: center;">Year</th>
      <th>Organization Name</th>
      <th style="width: 30%;">Position / Level</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.portfolio.organizations %}
      <tr>
        <td style="text-align: center;">{{ item.period }}</td>
        <td><b>{{ item.name }}</b></td>
        <td>{{ item.role }} / {{ item.level }}</td>
      </tr>
    {% endfor %}
  </tbody>
</table>

<hr style="margin: 30px 0;">

<h3>PROFESSIONAL CERTIFICATIONS</h3>

<table>
  <thead>
    <tr>
      <th style="width: 15%; text-align: center;">Year</th>
      <th>Certification Title</th>
      <th style="width: 25%;">Provider</th>
      <th style="width: 20%; text-align: center;">Certificate</th>
    </tr>
  </thead>
  <tbody>
    {% for item in site.data.portfolio.certifications %}
      <tr>
        <td style="text-align: center;">{{ item.year }}</td>
        <td><b>{{ item.title }}</b></td>
        <td>{{ item.provider }}</td>
        <td style="text-align: center;">
          {% if item.url and item.url != "" %}
            <a href="{{ item.url }}" target="_blank">View Certificate</a>
          {% else %}
            -
          {% endif %}
        </td>
      </tr>
    {% endfor %}
  </tbody>
</table>

<hr style="margin: 30px 0;">

<h3>COMMUNITY SERVICES & OUTREACH</h3>

<ul>
  {% for item in site.data.portfolio.community_services %}
    <li>
      <b>{{ item.year }}</b>: {{ item.title }}
      {% if item.funder and item.funder != "" %}
        <i>({{ item.funder }})</i>
      {% endif %}
    </li>
  {% endfor %}
</ul>
