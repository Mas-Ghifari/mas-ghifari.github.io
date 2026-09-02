---
layout: single
title: "Intellectual Property Rights"
permalink: /ipr/
author_profile: true
---

Below is a list of intellectual property rights (IPRs) of various software, machine learning models, IoT frameworks, and digital platforms built by our research group. The IPRs have been granted or submitted to the Ministry of Law and Human Rights, Republic of Indonesia.

---

### Patents

<ul>
{% for item in site.data.portfolio.ipr %}
  {% if item.type == "Granted Patent" or item.type == "Patent" %}
    <li>
      <b>{{ item.title }}</b><br>
      {% if item.type == "Granted Patent" %}
        Patent Number: <code>{{ item.number }}</code>{% if item.date %} (Granted: {{ item.date }}){% endif %}.
      {% else %}
        Application Number: <code>{{ item.number }}</code>{% if item.date %} (Submitted: {{ item.date }}){% endif %}.
      {% endif %}
      {% if item.notes %}<br><small style="color: #666;"><i>Note: {{ item.notes }}</i></small>{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>

---

### Copyrights

<ul>
{% for item in site.data.portfolio.ipr %}
  {% if item.type == "Copyright" %}
    <li>
      <b>{{ item.title }}</b><br>
      Registration Number: <code>{{ item.number }}</code>{% if item.date %} (Granted: {{ item.date }}){% endif %}.
      {% if item.notes %}<br><small style="color: #666;"><i>Note: {{ item.notes }}</i></small>{% endif %}
    </li>
  {% endif %}
{% endfor %}
</ul>
