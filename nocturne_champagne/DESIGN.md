---
name: Nocturne & Champagne
colors:
  surface: '#141316'
  surface-dim: '#141316'
  surface-bright: '#3a383c'
  surface-container-lowest: '#0f0e11'
  surface-container-low: '#1c1b1e'
  surface-container: '#201f22'
  surface-container-high: '#2b292d'
  surface-container-highest: '#363437'
  on-surface: '#e6e1e5'
  on-surface-variant: '#d4c4b7'
  inverse-surface: '#e6e1e5'
  inverse-on-surface: '#313033'
  outline: '#9c8e82'
  outline-variant: '#50453b'
  surface-tint: '#f0bd8b'
  primary: '#f2be8c'
  on-primary: '#482904'
  primary-container: '#d4a373'
  on-primary-container: '#5b3912'
  inverse-primary: '#7d562d'
  secondary: '#ffb59a'
  on-secondary: '#53210c'
  secondary-container: '#723922'
  on-secondary-container: '#f5a587'
  tertiary: '#ffb5b3'
  on-tertiary: '#5c171b'
  tertiary-container: '#f6908f'
  on-tertiary-container: '#72272a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcbd'
  primary-fixed-dim: '#f0bd8b'
  on-primary-fixed: '#2c1600'
  on-primary-fixed-variant: '#623f18'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb59a'
  on-secondary-fixed: '#380d00'
  on-secondary-fixed-variant: '#6f3720'
  tertiary-fixed: '#ffdad8'
  tertiary-fixed-dim: '#ffb3b1'
  on-tertiary-fixed: '#3f0209'
  on-tertiary-fixed-variant: '#7a2d30'
  background: '#141316'
  on-background: '#e6e1e5'
  surface-variant: '#363437'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: '600'
    lineHeight: 3.5rem
    letterSpacing: -0.03em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 2.25rem
    fontWeight: '600'
    lineHeight: 2.75rem
    letterSpacing: -0.025em
  headline-lg:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: '600'
    lineHeight: 2.5rem
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Inter
    fontSize: 1.625rem
    fontWeight: '600'
    lineHeight: 2rem
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Inter
    fontSize: 1.375rem
    fontWeight: '500'
    lineHeight: 1.875rem
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '500'
    lineHeight: 1.625rem
    letterSpacing: -0.005em
  body-lg:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: 1.625rem
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: 1.375rem
    letterSpacing: 0.005em
  body-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '400'
    lineHeight: 1.125rem
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '500'
    lineHeight: 1.25rem
    letterSpacing: 0.02em
  label-md:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: 1rem
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 0.6875rem
    fontWeight: '600'
    lineHeight: 0.875rem
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-md: 1.5rem
  gutter-lg: 2rem
  margin: 1rem
  margin-md: 2rem
  margin-lg: 3rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2.5rem
---

## Brand & Style

This design system crafts a sanctuary of bespoke luxury, blending the intimacy of haute couture wedding curation with the precision of high-performance guest logistics. Designed for discerning couples, elite planners, and high-profile guests, the aesthetic conveys quiet opulence, effortless calm, and digital craftsmanship reminiscent of high-end bespoke iOS applications.

The design movement is **Tactile Minimalism with Luminescent Glass**. It pairs deep obsidian and charcoal grounds with razor-thin, luminous metallic borders, warm champagne ambient lighting, and perfectly weighted typography. Every interaction feels deliberate, weighted, and haptic—balancing celebratory elegance with uncompromising clarity under evening lighting conditions.

## Colors

The palette draws inspiration from candlelit architectural courtyards and burnished metallurgy.

- **Obsidian Baseline (`#121114`)**: Root canvas foundation providing infinite depth without harsh pure black.
- **Charcoal Layer 1 (`#1a181d`)**: Elevated card and sheet surfaces.
- **Charcoal Layer 2 (`#252229`)**: Nested inputs, chips, and interactive states.
- **Champagne Primary (`#d4a373`)**: Key action anchors, primary highlights, celebration indicators, and delicate linear rims.
- **Rose Gold Secondary (`#e29578`)**: Timelines, guest dietary tags, secondary milestones, and warm active pills.
- **Burnished Blush Tertiary (`#c96b6b`)**: Critical notices, urgent RSVP confirmations, and delicate status points.
- **Text & Borders**: Off-white primary text (`#f8f6f5`), muted sand secondary text (`#a8a3a0`), and luminous borders rendered in 8–15% champagne alpha overlays (`rgba(212, 163, 115, 0.12)`).

## Typography

Typography relies entirely on the precision and optical neutrality of Inter. To evoke high luxury rather than generic SaaS, weight pairings are deliberate: medium-weight headings feature negative tracking (`-0.02em` to `-0.03em`) for a sculpted, editorial cadence. 

Micro-labels, schedule metadata, and registry identifiers leverage uppercase `label-md` and `label-sm` with expanded tracking (`0.05em` to `0.08em`) to mimic stamped card stock. Numbers in guest headcounts, seat assignments, and run-of-show timestamps use tabular figures (`font-variant-numeric: tabular-nums`) to maintain visual alignment across dense logistical displays.

## Layout & Spacing

The layout model implements an iOS-native dynamic column architecture that transitions seamlessly to an editorial 12-column desktop grid.

- **Mobile (<768px)**: 4-column fluid layout with `1rem` margins and `1rem` gutters. Content prioritizes edge-to-edge modular cards with unified horizontal padding (`space-md`). Sticky bottom accessory bars anchor critical actions (e.g., RSVP submission, table seating maps).
- **Tablet (768px - 1024px)**: 8-column layout with `2rem` margins and `1.5rem` gutters, allowing split-screen guest rosters and multi-tier itineraries.
- **Desktop (>1024px)**: 12-column layout maxed at 1280px with `3rem` margins and `2rem` gutters, leaving deliberate atmospheric margins.

Spacing follows an 8pt structural rhythm, using micro-steps (4px, 8px) for tightly grouped logistics data, and macro-steps (24px, 40px) to breathe formal pause between distinct wedding phases.

## Elevation & Depth

Visual hierarchy does not rely on heavy drop shadows, which dilute the richness of deep charcoal substrates. Depth is engineered through three unified mechanics:

1. **Luminescent Tonal Stratification**: Base canvas `#121114` sits at the floor. Elevated modules step up to `#1a181d`, and interactive nested sub-containers utilize `#252229`. 
2. **Metallic Rim Lighting**: Cards and sheets feature a razor-thin border (`1px`) with a linear gradient falling from `rgba(212, 163, 115, 0.24)` at the top edge to `rgba(255, 255, 255, 0.03)` at the bottom, mimicking ambient chandelier light grazing dark lacquered wood.
3. **Atmospheric Glows**: Floating modals and primary RSVP triggers emit an ultra-diffused, warm shadow: `0 12px 32px -4px rgba(212, 163, 115, 0.15), 0 4px 12px rgba(0, 0, 0, 0.4)`.
4. **Frosted Translucency**: Sticky navigation headers and floating modal backdrops apply backdrop blur (`blur(20px) saturate(180%)`) over an 80% opacity obsidian wash (`rgba(18, 17, 20, 0.8)`).

## Shapes

The design uses balanced, modern iOS rounded geometries (`roundedness: 2`). Standard containers, interactive inputs, and itinerary cards feature an 8px (`0.5rem`) base corner radius. Hero modules and sheet modals expand to 16px (`1rem`), while primary CTA pills, category badges, and quick-status tags resolve in soft, pill-shaped caps (`9999px`) to maintain human warmth and tactile comfort.

## Components

### Buttons
- **Primary Action (RSVP / Confirm)**: Champagne background (`#d4a373`) with rich obsidian text (`#121114`), bold Inter typography, full pill shape (`rounded-full`), and an ambient warm glow on hover. Pressed states compress slightly (`scale(0.98)`).
- **Secondary Action (Manage Plus-One / View Itinerary)**: Dark charcoal fill (`#1a181d`) with 1px luminescent border (`rgba(212, 163, 115, 0.2)`), off-white text (`#f8f6f5`), transitioning to champagne text and border on focus.
- **Ghost/Tertiary**: Transparent fill with muted sand text (`#a8a3a0`), activating to `#d4a373` text with subtle background tint (`rgba(212, 163, 115, 0.08)`).

### Cards
- Constructed with `#1a181d` surface fill, `0.5rem` to `1rem` radius, and hairline gradient border. Internal padding matches `space-lg` (`1.5rem`). Dividers within cards use soft horizontal champagne fades (`rgba(212, 163, 115, 0.08)`).

### Input Fields & Selectors
- Background `#252229`, framed by a subtle border (`rgba(255, 255, 255, 0.08)`). Placeholder text rests in `#716d75`. On focus, the border shifts to crisp champagne (`#d4a373`) accompanied by a subtle 2px champagne ring glow (`rgba(212, 163, 115, 0.25)`). Input labels are set in uppercase `label-sm` with active champagne highlights.

### Chips & Badges
- **Status Chips (Attending / Dietary / VIP Table)**: Compact pill shapes using 12% tinted alpha backgrounds (Champagne `#d4a373` for VIPs, Rose Gold `#e29578` for Ceremony markers, Blush `#c96b6b` for dietary alerts) framed with matching hairline borders and high-legibility contrasting labels.

### Checkboxes & Radios
- Custom rounded squares (checkboxes) and rings (radios) in `#252229` with `rgba(212, 163, 115, 0.3)` perimeter. When active, surfaces fill with `#d4a373`, holding a deep obsidian checkmark or nested radio dot.

### Lists & Timelines
- Multi-day timelines feature vertical hairline champagne guide-rules connecting glowing milestone nodes (4px dots). Guest lists employ alternating subtle hover highlights (`rgba(255, 255, 255, 0.02)`) with right-aligned tabular seating metadata.

### Bespoke Domain Components
- **Seating Escort Card**: A digital stationery tile incorporating subtle noise texture, gold foil-inspired typography, and explicit table, seat, and meal indicator quadrants.
- **Run-of-Show Countdown Bar**: Fixed bottom or top micro-bar displaying live wedding timeline progression with illuminated progress track and real-time transit alerts for guests.