# WedSync • MindGrid (iOS Wedding Guest & Planning Experience)

> An iOS-first wedding guest portal and event planning progressive web app for Sophie & Julian's wedding weekend at **Villa Cimbrone, Ravello, Amalfi Coast, Italy** (September 18–20, 2026).

[![Live Demo](https://img.shields.io/badge/Live_Demo-GitHub_Pages-rose?style=for-the-badge&logo=github)](https://b8bhupinder-coder.github.io/mindgrid-wedsync/)
[![iOS First](https://img.shields.io/badge/Design-iOS_HIG_&_Editorial-amber?style=for-the-badge&logo=apple)](https://b8bhupinder-coder.github.io/mindgrid-wedsync/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.x-blue?style=for-the-badge&logo=tailwindcss)](https://tailwindcss.com/)

---

## 🌟 Overview & Key MVP Screens

This application synthesizes high-fashion editorial romance with the tactile fluidity of Apple Human Interface Guidelines (HIG).

1. **Screen 1: Welcome & Event Join / Onboarding**
   - Monogram seal (S&J), Ravello golden-hour editorial card.
   - 4-digit PIN unlock (`2 0 2 6`) with auto-advancing fields.
   - Interactive QR scanner simulation with animated laser line.
   - Phone OTP 4-digit verification modal (`8 4 9 2`).
   - One-tap demo guest login (Julianna & Marcus Vance).

2. **Screen 2: Home / Timeline Itinerary**
   - Real-time countdown ticker (Days, Hours, Minutes, Seconds until Sept 19, 2026).
   - "Offline Ready • Cached to Local Storage" status badge.
   - **1-Tap Sync to Apple Calendar**: Generates and downloads RFC 5545 `.ics` file containing all 5 weekend wedding itinerary events with alarms and location coordinates.
   - Segmented multi-day tabs: Day 1 (Arrival), Day 2 (Ceremony & Banquet), Day 3 (Farewell Brunch).
   - Interactive milestone reminders with toast confirmations.

3. **Screen 3: Event Detail & Venue Map Logistics**
   - Interactive Apple MapKit-styled map canvas covering Villa Cimbrone and Ravello.
   - 4 Interactive Pins: Villa Cimbrone, Piazza Duomo Shuttle, Guest Parking Lot B, and Hotel Caruso.
   - Dynamic pin detail drawer and deep links to Apple Maps navigation.
   - Cobblestone pedestrian path notice & Golf Cart mobility assistance request toggle.
   - Italian Black Tie Optional dress code with visual Mediterranean color swatches.
   - Wedding Concierge call & WhatsApp trigger modal.

4. **Screen 4: Interactive RSVP & Dining Selection**
   - Multi-attendee management (Julianna Vance + Marcus Vance).
   - Attendance switch: "Joyfully Accepts" vs "Regretfully Declines".
   - Entrée radio cards:
     - Tuscan Herb Roasted Beef Tenderloin
     - Pan-Seared Mediterranean Sea Bass
     - Handmade Ricotta & Wild Mushroom Agnolotti (Vegetarian)
   - Interactive dietary restriction chips (Gluten-Free, Dairy-Free, Nut Allergy, Shellfish, Vegan).
   - Real-time synchronization with the Organizer Admin Dashboard.

5. **Screen 5: DJ Booth & Vibe**
   - Live "On the Decks" player card with rotating vinyl disc animation and live sound wave frequency equalizer bars.
   - Strict 3-song request quota per guest with progress meter.
   - Search bar with instant queue submission.
   - Genre filter chips: Top Voted (Live), Disco Classics, Late Night Anthems, Slow Dances, Italian Classics.
   - Live crowdsourced upvote buttons with instant dynamic queue re-sorting.

6. **Screen 6: Organizer Admin Dashboard**
   - Live KPI Bento Grid: Total Confirmed Guests, Dietary Alerts, Apple Calendar Synced %, DJ Requests.
   - RSVP Lock switch to disable guest changes.
   - Broadcast Push Notification modal with quick presets that dispatch alerts to the **Dynamic Island** with audio chime.
   - 1-Click Catering Manifest CSV export and DJ Playlist CSV export.
   - Live searchable guest roster with table seating and dietary alerts.

---

## 🎨 Dual Theme System

- **WedSync Editorial Romance (Light Mode)**: Warm alabaster canvas, terracotta rose `#7c2628`, vintage gilded gold `#775a19`, and soft sage `#384836`.
- **Nocturne & Champagne (Dark Mode)**: Obsidian baseline `#141316`, luminescent glass, champagne gold `#d4a373`, and rose gold `#ffb59a`.

---

## 📱 Device Simulation Controls

- **iPhone 16 Pro**: Authentic titanium chassis with interactive **Dynamic Island**, status bar, and home indicator.
- **iPad Mini**: Tablet-width layout.
- **Full Window**: Responsive edge-to-edge web app view.
- **Persona Switcher**: Toggle between **Guest View** and **Host Admin View**.

---

## 🚀 Running Locally

```bash
# Clone the repository
git clone https://github.com/b8bhupinder-coder/mindgrid-wedsync.git
cd mindgrid-wedsync

# Start the zero-dependency Python server
python3 server.py
```

Then open [http://127.0.0.1:3000](http://127.0.0.1:3000) in your browser.

---

## 📄 License
MIT License. Created for Sophie & Julian's Wedding Celebration.
