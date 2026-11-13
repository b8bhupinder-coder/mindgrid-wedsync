#!/usr/bin/env python3
"""
WedSync / MindGrid Complete Application Builder
Combines PRD specifications, design tokens, and all 6 MVP screens into a unified,
production-grade iOS-first web application.
"""

import os
import re

WORKSPACE = "/Users/bhupindersingh/Downloads/Lets Engage"

def read_file(rel_path):
    with open(os.path.join(WORKSPACE, rel_path), "r", encoding="utf-8") as f:
        return f.read()

def main():
    print("Reading original screen files...")
    welcome_html = read_file("welcome_event_join/code.html")
    timeline1_html = read_file("timeline_itinerary_1/code.html")
    venue_html = read_file("venue_logistics/code.html")
    rsvp1_html = read_file("rsvp_menu_selection_1/code.html")
    dj1_html = read_file("dj_booth_vibe/code.html")
    admin1_html = read_file("organizer_admin_dashboard_1/code.html")

    # Extract main content from each
    def extract_main(html):
        m = re.search(r'<main[^>]*>(.*?)</main>', html, re.DOTALL)
        return m.group(1) if m else ""

    welcome_main = extract_main(welcome_html)
    timeline_main = extract_main(timeline1_html)
    venue_main = extract_main(venue_html)
    rsvp_main = extract_main(rsvp1_html)
    dj_main = extract_main(dj1_html)
    admin_main = extract_main(admin1_html)

    print(f"Extracted mains: welcome({len(welcome_main)}), timeline({len(timeline_main)}), venue({len(venue_main)}), rsvp({len(rsvp_main)}), dj({len(dj_main)}), admin({len(admin_main)})")

if __name__ == "__main__":
    main()
