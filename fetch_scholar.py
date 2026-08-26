import os
import datetime
from scholarly import scholarly

# Ganti dengan Google Scholar ID Anda (dari URL profil Scholar)
SCHOLAR_ID = "MVLUQvMAAAAJ"

def main():
    print(f"Mengambil data publikasi untuk Scholar ID: {SCHOLAR_ID}")
    author = scholarly.search_author_id(SCHOLAR_ID)
    scholarly.fill(author, sections=['publications'])
    
    os.makedirs("_publications", exist_ok=True)
    
    for pub in author['publications']:
        scholarly.fill(pub)
        bib = pub.get('bib', {})
        
        title = bib.get('title', 'Untitled')
        year = bib.get('pub_year', '2025')
        pub_url = pub.get('pub_url', '')
        venue = bib.get('venue', bib.get('journal', bib.get('conference', '')))
        author_list = bib.get('author', '')
        
        # Buat nama file aman dari judul
        safe_title = "".join([c if c.isalnum() else "-" for c in title[:30].lower()]).strip("-")
        filename = f"_publications/{year}-{safe_title}.md"
        
        content = f"""---
title: "{title}"
collection: publications
permalink: /publication/{year}-{safe_title}
date: {year}-01-01
venue: '{venue}'
paperurl: '{pub_url}'
citation: '{author_list} ({year}). "{title}." <i>{venue}</i>.'
---
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
    print("Selesai memperbarui folder _publications!")

if __name__ == "__main__":
    main()
