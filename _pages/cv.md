---
layout: single
title: "Interactive Curriculum Vitae"
permalink: /cv/
author_profile: true
---

<!-- Panel Kontrol Pilih Kategori (Sembunyi saat di-print) -->
<div class="no-print" style="background: #f8f9fa; border: 1px solid #e9ecef; padding: 20px; border-radius: 8px; margin-bottom: 25px;">
  <h4 style="margin-top: 0; margin-bottom: 12px; color: #333;"><i class="fa-solid fa-sliders"></i> Customize Your CV Output:</h4>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-bottom: 15px;">
    <label><input type="checkbox" id="chk-edu" checked onchange="toggleSection('sec-edu')"> Education Background</label>
    <label><input type="checkbox" id="chk-grants" checked onchange="toggleSection('sec-grants')"> Research Grants</label>
    <label><input type="checkbox" id="chk-pubs" checked onchange="toggleSection('sec-pubs')"> Publications</label>
    <label><input type="checkbox" id="chk-ipr" checked onchange="toggleSection('sec-ipr')"> Intellectual Property (IPR)</label>
    <label><input type="checkbox" id="chk-talks" checked onchange="toggleSection('sec-talks')"> Invited Talks & Visiting</label>
    <label><input type="checkbox" id="chk-lectures" checked onchange="toggleSection('sec-lectures')"> Regular Teaching Experience</label>
    <label><input type="checkbox" id="chk-certs" checked onchange="toggleSection('sec-certs')"> Certifications</label>
    <label><input type="checkbox" id="chk-orgs" checked onchange="toggleSection('sec-orgs')"> Professional Affiliations</label>
    <label><input type="checkbox" id="chk-services" checked onchange="toggleSection('sec-services')"> Community Services</label>
  </div>

  <button onclick="window.print()" class="btn btn--primary btn--large">
    <i class="fa-solid fa-file-pdf"></i> Download Selected CV (PDF)
  </button>
</div>

<!-- Lembaran Dokumen CV -->
<div class="cv-document-box">
  <div style="text-align: center; margin-bottom: 25px;">
    <h2 style="margin: 0; padding: 0; color: #111;">Dr. Nasy'an Taufiq Al Ghifari</h2>
    <p style="margin: 5px 0; font-size: 1.1em; color: #444;">Assistant Professor in Computer Science / Data Mining Expert</p>
    <p style="margin: 0; font-size: 0.95em; color: #666;">Universitas Muhammadiyah Yogyakarta | Email: nasyan.taufiq@umy.ac.id</p>
  </div>

  <hr style="border: 0; border-top: 2px solid #333; margin-bottom: 20px;">

  <!-- Section: Education -->
  <div id="sec-edu" class="cv-section">
    <h3>EDUCATION BACKGROUND</h3>
    <ul>
      {% for item in site.data.portfolio.education %}
      <li><b>{{ item.degree }}</b> &mdash; {{ item.institution }} ({{ item.year }})</li>
      {% endfor %}
    </ul>
  </div>

  <!-- Section: Research Grants -->
  <div id="sec-grants" class="cv-section">
    <h3 style="margin-top: 20px;">ACQUIRED RESEARCH GRANTS</h3>
    <table>
      <thead>
        <tr><th style="width: 12%;">Year</th><th>Research Title</th><th style="width: 20%;">Funder</th></tr>
      </thead>
      <tbody>
        {% for item in site.data.portfolio.grants %}
        <tr>
          <td style="text-align: center;">{{ item.year }}</td>
          <td>{{ item.title }} <i>({{ item.role }})</i></td>
          <td>{{ item.funding }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>

  <!-- Section: Publications -->
  <div id="sec-pubs" class="cv-section">
    <h3 style="margin-top: 20px;">PUBLICATIONS</h3>
    <ol>
      {% for item in site.data.portfolio.publications %}
        {% comment %} Filter: Hanya tampilkan paper yang BUKAN status Under Review {% endcomment %}
        {% if item.type != "Manuscript Under Review" %}
          <li>
            {{ item.authors }} ({{ item.year }}). <b>"{{ item.title }}"</b>. <i>{{ item.venue }}</i>.
            {% if item.type %} <span style="font-size: 0.85em; color: #555;">[{{ item.type }}]</span>{% endif %}
          </li>
        {% endif %}
      {% endfor %}
    </ol>
  </div>

  <!-- Section: IPR -->
  <div id="sec-ipr" class="cv-section">
    <h3 style="margin-top: 20px;">INTELLECTUAL PROPERTY RIGHTS (IPR)</h3>
    <ul>
      {% for item in site.data.portfolio.ipr %}
      <li><b>{{ item.type }}</b>: {{ item.title }} (Reg No: {{ item.number }}, {{ item.year }})</li>
      {% endfor %}
    </ul>
  </div>

  <!-- Section: Invited Talks -->
  <div id="sec-talks" class="cv-section">
    <h3 style="margin-top: 20px;">INVITED LECTURES & VISITING PROFESSORSHIPS</h3>
    <ul>
      {% for item in site.data.portfolio.invited_talks %}
      <li><b>{{ item.teaching_activity }}</b> &mdash; {{ item.location }} ({{ item.year }})</li>
      {% endfor %}
    </ul>
  </div>

  <!-- Section: Regular Lectures -->
  <div id="sec-lectures" class="cv-section">
    <h3 style="margin-top: 20px;">REGULAR TEACHING EXPERIENCE</h3>
    <table>
      <thead>
        <tr><th>Course Title</th><th style="width: 15%;">Level</th><th>Institution / Department</th><th style="width: 20%;">Academic Years</th></tr>
      </thead>
      <tbody>
        {% for item in site.data.portfolio.regular_lectures %}
        <tr>
          <td><b>{{ item.course_title }}</b></td>
          <td style="text-align: center;">{{ item.level }}</td>
          <td>{{ item.institution }}</td>
          <td style="text-align: center;">{{ item.academic_years }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>

  <!-- Section: Certifications -->
  <div id="sec-certs" class="cv-section">
    <h3 style="margin-top: 20px;">PROFESSIONAL CERTIFICATIONS</h3>
    <ul>
      {% for item in site.data.portfolio.certifications %}
      <li><b>{{ item.title }}</b> &mdash; {{ item.provider }} ({{ item.year }})</li>
      {% endfor %}
    </ul>
  </div>

  <!-- Section: Organizations -->
  <div id="sec-orgs" class="cv-section">
    <h3 style="margin-top: 20px;">PROFESSIONAL AFFILIATIONS</h3>
    <ul>
      {% for item in site.data.portfolio.organizations %}
      <li><b>{{ item.name }}</b> &mdash; {{ item.role }} ({{ item.year }})</li>
      {% endfor %}
    </ul>
  </div>

  <!-- Section: Community Services -->
  <div id="sec-services" class="cv-section">
    <h3 style="margin-top: 20px;">COMMUNITY SERVICES</h3>
    <ul>
      {% for item in site.data.portfolio.community_services %}
      <li><b>{{ item.title }}</b> {% if item.venue %}({{ item.venue }}){% endif %} &mdash; {{ item.year }}</li>
      {% endfor %}
    </ul>
  </div>
</div>

<script>
function toggleSection(sectionId) {
  var sec = document.getElementById(sectionId);
  if (sec) {
    if (sec.style.display === "none") {
      sec.style.display = "block";
    } else {
      sec.style.display = "none";
    }
  }
}
</script>
