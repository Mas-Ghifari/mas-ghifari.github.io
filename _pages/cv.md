---
layout: single
title: "Interactive Curriculum Vitae"
permalink: /cv/
author_profile: true
---

<style>
  /* Base Style untuk Kotak Filter (Mode Terang) */
  .cv-filter-card {
    background-color: #ffffff !important;
    border: 1px solid #cbd5e1 !important;
    padding: 20px !important;
    border-radius: 8px !important;
    margin-bottom: 25px !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
  }

  .cv-filter-card h4,
  .cv-filter-card label,
  .cv-filter-card span {
    color: #0f172a !important; /* Teks Hitam Pekat */
    -webkit-text-fill-color: #0f172a !important;
    opacity: 1 !important;
  }

  .cv-filter-card input[type="checkbox"] {
    accent-color: #0284c7 !important;
    margin-right: 6px !important;
    cursor: pointer !important;
  }

  /* Force Dark Mode Override (Saat Tema Berubah Gelap) */
  html[data-theme="dark"] .cv-filter-card,
  body.dark-mode .cv-filter-card,
  body[data-theme="dark"] .cv-filter-card,
  .dark .cv-filter-card {
    background-color: #1e293b !important; /* Latar Belakang Kotak Jadi Abu-Abu Gelap */
    border-color: #334155 !important;
  }

  html[data-theme="dark"] .cv-filter-card h4,
  html[data-theme="dark"] .cv-filter-card label,
  body.dark-mode .cv-filter-card h4,
  body.dark-mode .cv-filter-card label,
  body[data-theme="dark"] .cv-filter-card h4,
  body[data-theme="dark"] .cv-filter-card label,
  .dark .cv-filter-card h4,
  .dark .cv-filter-card label {
    color: #f8fafc !important; /* Teks Berubah Jadi Putih Terang */
    -webkit-text-fill-color: #f8fafc !important;
  }

  /* Lembar Dokumen CV (Selalu Berbentuk Kertas Putih) */
  .cv-document-box {
    background-color: #ffffff !important;
    border: 1px solid #d1d5db !important;
    padding: 30px !important;
    border-radius: 6px !important;
  }

  .cv-document-box,
  .cv-document-box *,
  .cv-document-box h2,
  .cv-document-box h3,
  .cv-document-box p,
  .cv-document-box li,
  .cv-document-box td,
  .cv-document-box th {
    color: #0f172a !important;
    -webkit-text-fill-color: #0f172a !important;
  }

  .cv-document-box a {
    color: #0284c7 !important;
    -webkit-text-fill-color: #0284c7 !important;
  }
</style>

<!-- Panel Kontrol Pilih Kategori (Sembunyi saat di-print) -->
<div class="no-print cv-filter-card">
  <h4 style="margin-top: 0; margin-bottom: 12px;"><i class="fa-solid fa-sliders"></i> Customize Your CV Output:</h4>
  
  <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-bottom: 15px;">
    <label><input type="checkbox" id="chk-edu" checked onchange="toggleSection('sec-edu')"> Education Background</label>
    <label><input type="checkbox" id="chk-grants" checked onchange="toggleSection('sec-grants')"> Research Grants</label>
    <label><input type="checkbox" id="chk-pubs" checked onchange="toggleSection('sec-pubs')"> Publications</label>
    <label><input type="checkbox" id="chk-ipr" checked onchange="toggleSection('sec-ipr')"> Intellectual Property (IPR)</label>
    <label><input type="checkbox" id="chk-talks" checked onchange="toggleSection('sec-teaching')"> Teaching & Invited Lectures</label>
    <label><input type="checkbox" id="chk-certs" checked onchange="toggleSection('sec-certifications')"> Certifications</label>
    <label><input type="checkbox" id="chk-orgs" checked onchange="toggleSection('sec-affiliations')"> Professional Affiliations</label>
    <label><input type="checkbox" id="chk-services" checked onchange="toggleSection('sec-community')"> Community Services</label>
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
        {% assign sorted_grants = site.data.portfolio.grants | sort: "year" | reverse %}
        {% for item in sorted_grants limit: 20 %}
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
      {% comment %} 
        1. Filter paper yang BUKAN Under Review 
        2. Urutkan berdasarkan tahun (sort: "year") 
        3. Dibalik dari yang terbaru ke lama (reverse) 
        4. Batasi maksimal 20 publikasi (limit: 20)
      {% endcomment %}
      {% assign published_papers = site.data.portfolio.publications | where_exp: "item", "item.type != 'Manuscript Under Review'" | sort: "year" | reverse %}
      
      {% for item in published_papers limit: 20 %}
      <li>
        {{ item.authors }} ({{ item.year }}). 
        <b>"
          {% if item.doi %}
            <a href="{{ item.doi }}" target="_blank" style="color: inherit; text-decoration: none;">{{ item.title }}</a>
          {% elsif item.url %}
            <a href="{{ item.url }}" target="_blank" style="color: inherit; text-decoration: none;">{{ item.title }}</a>
          {% else %}
            {{ item.title }}
          {% endif %}
        "</b>. 
        <i>{{ item.venue }}</i>.
        {% if item.type %} <span style="font-size: 0.85em; color: #555;">[{{ item.type }}]</span>{% endif %}
      </li>
      {% endfor %}
    </ol>
  </div>

  <!-- Section: IPR -->
  <div id="sec-ipr" class="cv-section">
    <h3 style="margin-top: 20px;">INTELLECTUAL PROPERTY RIGHTS (IPR)</h3>
    <ul>
      {% for item in site.data.portfolio.ipr %}
        {% if item.type != "Draft / Planned" %}
        <li><b>{{ item.type }}</b>: {{ item.title }} (Reg No: {{ item.number }}{% if item.year %}, {{ item.year }}{% endif %})</li>
        {% endif %}
      {% endfor %}
    </ul>
  </div>

  <!-- Section: Teaching & Invited Lectures -->
  <div id="sec-teaching" class="cv-section">
    <h3 style="margin-top: 20px;">TEACHING & INVITED LECTURES</h3>
    
    <p style="margin-bottom: 6px; font-weight: bold; font-size: 0.95em;">Regular Courses</p>
    <ul style="margin-top: 0; margin-bottom: 15px;">
      {% for item in site.data.portfolio.regular_lectures %}
      <li>
        <b>{{ item.course_title }}</b> ({{ item.level }}) &mdash; {{ item.institution }} 
        <span style="color: #555;">[{{ item.academic_years }}]</span>
      </li>
      {% endfor %}
    </ul>

    <p style="margin-bottom: 6px; font-weight: bold; font-size: 0.95em;">Invited Lectures & Visiting Professorships</p>
    <ul style="margin-top: 0; margin-bottom: 15px;">
      {% for item in site.data.portfolio.invited_lectures %}
      <li>
        <b>{{ item.title }}</b> &mdash; {{ item.institution }} 
        <span style="color: #555;">({{ item.date }})</span>
      </li>
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
  <div id="sec-certifications" class="cv-section">
    <h3 style="margin-top: 20px;">PROFESSIONAL CERTIFICATIONS</h3>
    <ul>
      {% for item in site.data.portfolio.certifications %}
      <li>
        <b>{{ item.title }}</b> &mdash; {{ item.provider }} ({{ item.year }})
        {% if item.url and item.url != "" %}
          [<a href="{{ item.url }}" target="_blank">Certificate</a>]
        {% endif %}
      </li>
      {% endfor %}
    </ul>
  </div>

  <!-- Section: Professional Affiliations -->
  <div id="sec-affiliations" class="cv-section">
    <h3 style="margin-top: 20px;">PROFESSIONAL AFFILIATIONS</h3>
    <ul>
      {% for item in site.data.portfolio.organizations %}
      <li><b>{{ item.name }}</b> &mdash; {{ item.role }} ({{ item.level }}) [{{ item.period }}]</li>
      {% endfor %}
    </ul>
  </div>

  <!-- Section: Community Services -->
  <div id="sec-community" class="cv-section">
    <h3 style="margin-top: 20px;">COMMUNITY SERVICES</h3>
    <ul>
      {% for item in site.data.portfolio.community_services %}
      <li><b>{{ item.title }}</b> {% if item.funder and item.funder != "" %}<i>({{ item.funder }})</i>{% endif %} &mdash; {{ item.year }}</li>
      {% endfor %}
    </ul>
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
