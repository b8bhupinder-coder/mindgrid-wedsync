#!/usr/bin/env python3
"""
WedSync / MindGrid Application Server
Lightweight Python server serving the integrated iOS Wedding Guest experience.
Zero third-party dependencies required (Standard Library only).
"""

import http.server
import socketserver
import os
import sys
import json
import urllib.parse
from datetime import datetime

PORT = 3000
HOST = "127.0.0.1"
WORKSPACE_DIR = os.path.dirname(os.path.abspath(__file__))
STATE_FILE = os.path.join(WORKSPACE_DIR, "app_state.json")

# Default demo state
DEFAULT_STATE = {
    "isUnlocked": False,
    "theme": "editorial", # "editorial" (light) or "nocturne" (dark)
    "currentGuest": {
        "primaryName": "Julianna Vance",
        "plusOneName": "Marcus Vance",
        "phone": "+1 (555) 382-9012",
        "table": 4,
        "isAttending": True,
        "primaryMeal": "beef",
        "primaryAllergies": ["Gluten-Free"],
        "primaryNote": "So excited to celebrate you both in beautiful Ravello!",
        "plusOneAttending": True,
        "plusOneMeal": "seabass",
        "plusOneAllergies": ["Nut Allergy"],
        "plusOneNote": ""
    },
    "rsvpLocked": False,
    "stats": {
        "totalInvited": 150,
        "totalConfirmed": 142,
        "totalDeclined": 8,
        "dietaryAlerts": 19,
        "calendarSyncedPct": 88,
        "djRequestsCount": 32
    },
    "dj": {
        "nowPlaying": {
            "title": "Signed, Sealed, Delivered",
            "artist": "Stevie Wonder",
            "album": "Tamla Motown",
            "progress": 72
        },
        "userRequestsRemaining": 2,
        "userRequestsMade": [
            {"title": "September", "artist": "Earth, Wind & Fire"}
        ],
        "songs": [
            {"id": "song-1", "title": "September", "artist": "Earth, Wind & Fire", "genre": "Disco Classics", "votes": 38, "requestedBy": "Julianna Vance", "userVoted": True},
            {"id": "song-2", "title": "Levitating", "artist": "Dua Lipa", "genre": "Late Night Anthems", "votes": 29, "requestedBy": "Liam Sterling", "userVoted": False},
            {"id": "song-3", "title": "L-O-V-E", "artist": "Nat King Cole", "genre": "Slow Dances", "votes": 24, "requestedBy": "Camille Dupont", "userVoted": False},
            {"id": "song-4", "title": "Dancing in the Moonlight", "artist": "Toploader", "genre": "Top Voted", "votes": 19, "requestedBy": "Elena Rostova", "userVoted": True},
            {"id": "song-5", "title": "This Will Be (An Everlasting Love)", "artist": "Natalie Cole", "genre": "Top Voted", "votes": 16, "requestedBy": "Matteo Rossi", "userVoted": False},
            {"id": "song-6", "title": "Gimme! Gimme! Gimme!", "artist": "ABBA", "genre": "Late Night Anthems", "votes": 15, "requestedBy": "Chloe Laurent", "userVoted": False},
            {"id": "song-7", "title": "Sarà perché ti amo", "artist": "Ricchi e Poveri", "genre": "Italian Classics", "votes": 13, "requestedBy": "Alessandro Moretti", "userVoted": False}
        ]
    },
    "broadcasts": [
        {
            "id": "b-1",
            "message": "Welcome to Ravello! Check-in and champagne reception begins at 14:00 on the Belvedere Terrace.",
            "timestamp": "12:00 PM",
            "sender": "Sophie & Julian (Hosts)"
        }
    ],
    "guestRoster": [
        {"name": "Julianna Vance", "table": 4, "entree": "Beef Tenderloin", "allergies": "Gluten-Free", "status": "Confirmed"},
        {"name": "Marcus Vance", "table": 4, "entree": "Sea Bass", "allergies": "Nut Allergy", "status": "Confirmed"},
        {"name": "Camille Dupont", "table": 2, "entree": "Sea Bass", "allergies": "Shellfish", "status": "Confirmed"},
        {"name": "Liam Sterling", "table": 7, "entree": "Truffle Agnolotti", "allergies": "Vegetarian", "status": "Confirmed"},
        {"name": "Elena Rostova", "table": 1, "entree": "Beef Tenderloin", "allergies": "None", "status": "Confirmed"},
        {"name": "Matteo Rossi", "table": 3, "entree": "Sea Bass", "allergies": "None", "status": "Confirmed"},
        {"name": "Chloe Laurent", "table": 5, "entree": "Truffle Agnolotti", "allergies": "Vegan", "status": "Confirmed"},
        {"name": "Alessandro Moretti", "table": 2, "entree": "Beef Tenderloin", "allergies": "Dairy-Free", "status": "Confirmed"},
        {"name": "David Kim", "table": 6, "entree": "Beef Tenderloin", "allergies": "None", "status": "Confirmed"},
        {"name": "Sofia Chen", "table": 6, "entree": "Sea Bass", "allergies": "Nut Allergy", "status": "Confirmed"}
    ]
}

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[WedSync Server] Error reading {STATE_FILE}: {e}")
    return DEFAULT_STATE.copy()

def save_state(state):
    try:
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except Exception as e:
        print(f"[WedSync Server] Error saving {STATE_FILE}: {e}")

class WedSyncHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WORKSPACE_DIR, **kwargs)

    def end_headers(self):
        # Enable CORS and disable aggressive caching for local dev
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/state":
            state = load_state()
            data = json.dumps(state).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
            return

        elif path == "/api/export/catering.csv":
            state = load_state()
            lines = ["Guest Name,Table,Status,Entree Choice,Allergies / Dietary Restrictions"]
            for g in state.get("guestRoster", []):
                name = g.get("name", "").replace('"', '""')
                table = g.get("table", "")
                status = g.get("status", "")
                entree = g.get("entree", "").replace('"', '""')
                allergies = g.get("allergies", "").replace('"', '""')
                lines.append(f'"{name}",Table {table},{status},"{entree}","{allergies}"')
            csv_data = "\r\n".join(lines).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="wedsync_catering_manifest.csv"')
            self.send_header("Content-Length", str(len(csv_data)))
            self.end_headers()
            self.wfile.write(csv_data)
            return

        elif path == "/api/export/dj.csv":
            state = load_state()
            lines = ["Rank,Song Title,Artist,Genre,Upvotes,Requested By"]
            songs = sorted(state.get("dj", {}).get("songs", []), key=lambda x: x.get("votes", 0), reverse=True)
            for idx, s in enumerate(songs, start=1):
                title = s.get("title", "").replace('"', '""')
                artist = s.get("artist", "").replace('"', '""')
                genre = s.get("genre", "")
                votes = s.get("votes", 0)
                req_by = s.get("requestedBy", "")
                lines.append(f'{idx},"{title}","{artist}","{genre}",{votes},"{req_by}"')
            csv_data = "\r\n".join(lines).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/csv; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="wedsync_dj_requests.csv"')
            self.send_header("Content-Length", str(len(csv_data)))
            self.end_headers()
            self.wfile.write(csv_data)
            return

        elif path == "/calendar.ics" or path == "/api/calendar.ics":
            # Generate RFC 5545 iCalendar format for Apple Calendar
            ics_content = """BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//WedSync//Sophie and Julian Wedding Weekend//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
X-WR-CALNAME:Sophie & Julian Wedding Weekend
X-WR-TIMEZONE:Europe/Rome

BEGIN:VEVENT
UID:wedsync-2026-09-18-01@wedsync.local
DTSTAMP:20260901T000000Z
DTSTART;TZID=Europe/Rome:20260918T140000
DTEND;TZID=Europe/Rome:20260918T170000
SUMMARY:Guest Arrival & Champagne Welcome
DESCRIPTION:Check-in, welcome drinks, and escort to guest accommodations.
LOCATION:Villa Cimbrone Belvedere Terrace, Ravello, Italy
STATUS:CONFIRMED
BEGIN:VALARM
TRIGGER:-PT1H
ACTION:DISPLAY
DESCRIPTION:Reminder: Champagne Welcome starts in 1 hour
END:VALARM
END:VEVENT

BEGIN:VEVENT
UID:wedsync-2026-09-19-02@wedsync.local
DTSTAMP:20260901T000000Z
DTSTART;TZID=Europe/Rome:20260919T153000
DTEND;TZID=Europe/Rome:20260919T164500
SUMMARY:Ceremony & Exchange of Vows
DESCRIPTION:Wedding ceremony overlooking the Amalfi coastline. Dress code: Italian Black Tie Optional.
LOCATION:Villa Cimbrone Infinity Terrace, Ravello, Italy
STATUS:CONFIRMED
BEGIN:VALARM
TRIGGER:-PT2H
ACTION:DISPLAY
DESCRIPTION:Reminder: Wedding Ceremony in 2 hours
END:VALARM
END:VEVENT

BEGIN:VEVENT
UID:wedsync-2026-09-19-03@wedsync.local
DTSTAMP:20260901T000000Z
DTSTART;TZID=Europe/Rome:20260919T170000
DTEND;TZID=Europe/Rome:20260919T190000
SUMMARY:Cocktail Hour & Sunset Aperitivo
DESCRIPTION:Artisan charcuterie, Franciacorta, and live jazz ensemble.
LOCATION:Villa Cimbrone Rose Gardens & Cloister, Ravello, Italy
STATUS:CONFIRMED
END:VEVENT

BEGIN:VEVENT
UID:wedsync-2026-09-19-04@wedsync.local
DTSTAMP:20260901T000000Z
DTSTART;TZID=Europe/Rome:20260919T193000
DTEND;TZID=Europe/Rome:20260919T223000
SUMMARY:Dinner Banquet & Speeches
DESCRIPTION:Four-course seated banquet in the historic candlelit Gothic Crypt.
LOCATION:The Gothic Crypt, Villa Cimbrone, Ravello, Italy
STATUS:CONFIRMED
END:VEVENT

BEGIN:VEVENT
UID:wedsync-2026-09-19-05@wedsync.local
DTSTAMP:20260901T000000Z
DTSTART;TZID=Europe/Rome:20260919T230000
DTEND;TZID=Europe/Rome:20260920T030000
SUMMARY:After-Party & DJ Set
DESCRIPTION:Late-night dancing, open bar, and crowdsourced live DJ tracklist.
LOCATION:The Helipad Pavilion, Villa Cimbrone, Ravello, Italy
STATUS:CONFIRMED
END:VEVENT

END:VCALENDAR
""".replace("\n", "\r\n").encode("utf-8")

            self.send_response(200)
            self.send_header("Content-Type", "text/calendar; charset=utf-8")
            self.send_header("Content-Disposition", 'attachment; filename="sophie_julian_wedding.ics"')
            self.send_header("Content-Length", str(len(ics_content)))
            self.end_headers()
            self.wfile.write(ics_content)
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/state":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body.decode("utf-8"))
                save_state(data)
                resp = json.dumps({"status": "ok", "updated": datetime.now().isoformat()}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(resp)))
                self.end_headers()
                self.wfile.write(resp)
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(str(e).encode("utf-8"))
            return

        elif path == "/api/broadcast":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length)
            try:
                data = json.loads(body.decode("utf-8"))
                state = load_state()
                new_broadcast = {
                    "id": f"b-{int(datetime.now().timestamp())}",
                    "message": data.get("message", "Wedding Announcement"),
                    "timestamp": datetime.now().strftime("%I:%M %p"),
                    "sender": data.get("sender", "Sophie & Julian (Hosts)")
                }
                state.setdefault("broadcasts", []).insert(0, new_broadcast)
                save_state(state)
                resp = json.dumps({"status": "ok", "broadcast": new_broadcast}).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(resp)))
                self.end_headers()
                self.wfile.write(resp)
            except Exception as e:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(str(e).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

def run_server():
    port = PORT
    for try_port in [3000, 3001, 8000, 8081, 8888]:
        try:
            with socketserver.TCPServer((HOST, try_port), WedSyncHandler) as httpd:
                print(f"[WedSync Server] Running on http://{HOST}:{try_port}")
                print(f"[WedSync Server] Document root: {WORKSPACE_DIR}")
                httpd.serve_forever()
                return
        except OSError as e:
            print(f"[WedSync Server] Port {try_port} in use, trying next port...")
            continue
    print("[WedSync Server] Could not bind to any test port.")

if __name__ == "__main__":
    run_server()
