import os
import re

# Paste teks BibTeX dari Google Scholar ke dalam file 'publications.bib'
bib_file_path = "publications.bib"

if not os.path.exists(bib_file_path):
    print("File publications.bib tidak ditemukan!")
    exit()

with open(bib_file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Split tiap entri BibTeX
entries = content.split("@")
os.makedirs("_publications", exist_ok=True)

for entry in entries:
    if not entry.strip():
        continue
    
    title_match = re.search(r'title\s*=\s*[\"{](.*?)[\"}]', entry, re.IGNORECASE | re.DOTALL)
    author_match = re.search(r'author\s*=\s*[\"{](.*?)[\"}]', entry, re.IGNORECASE | re.DOTALL)
    year_match = re.search(r'year\s*=\s*[\"{](\d{4})[\"}]', entry, re.IGNORECASE)
    journal_match = re.search(r'(journal|booktitle)\s*=\s*[\"{](.*?)[\"}]', entry, re.IGNORECASE | re.DOTALL)
    
    if title_match:
        title = title_match.group(1).replace('\n', ' ').strip()
        year = year_match.group(1) if year_match else "2025"
        author = author_match.group(1).replace('\n', ' ').strip() if author_match else "Nasy'an Taufiq Al Ghifari"
        venue = journal_match.group(2).replace('\n', ' ').strip() if journal_match else ""
        
        safe_title = "".join([c if c.isalnum() else "-" for c in title[:30].lower()]).strip("-")
        filename = f"_publications/{year}-{safe_title}.md"
        
        md_content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{safe_title}
date: {year}-01-01
venue: '{venue}'
citation: '{author} ({year}). "{title}." <i>{venue}</i>.'
---
"""
        with open(filename, "w", encoding="utf-8") as out:
            out.write(md_content)

print("Berhasil mengonversi file BibTeX ke folder _publications!")
