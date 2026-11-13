---
name: WedSync Editorial Romance
colors:
  surface: '#fef8f4'
  surface-dim: '#dfd9d5'
  surface-bright: '#fef8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f9f2ef'
  surface-container: '#f3ede9'
  surface-container-high: '#ede7e3'
  surface-container-highest: '#e7e1de'
  on-surface: '#1d1b19'
  on-surface-variant: '#564241'
  inverse-surface: '#32302e'
  inverse-on-surface: '#f6f0ec'
  outline: '#897270'
  outline-variant: '#dcc0be'
  surface-tint: '#9e3f3f'
  primary: '#7c2628'
  on-primary: '#ffffff'
  primary-container: '#9b3d3d'
  on-primary-container: '#ffc7c4'
  inverse-primary: '#ffb3b0'
  secondary: '#775a19'
  on-secondary: '#ffffff'
  secondary-container: '#fed488'
  on-secondary-container: '#785a1a'
  tertiary: '#384836'
  on-tertiary: '#ffffff'
  tertiary-container: '#4f604c'
  on-tertiary-container: '#c6d9c0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad8'
  primary-fixed-dim: '#ffb3b0'
  on-primary-fixed: '#410006'
  on-primary-fixed-variant: '#7f282a'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#d5e8cf'
  tertiary-fixed-dim: '#b9ccb3'
  on-tertiary-fixed: '#101f0f'
  on-tertiary-fixed-variant: '#3b4b38'
  background: '#fef8f4'
  on-background: '#1d1b19'
  surface-variant: '#e7e1de'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 22px
    fontWeight: '500'
    lineHeight: 28px
  title-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 17px
    fontWeight: '600'
    lineHeight: 22px
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 17px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 15px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: 18px
    letterSpacing: 0.02em
  caption-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 11px
    fontWeight: '500'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-sm: 0.75rem
  margin: 1.25rem
  margin-sm: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

This design system synthesizes high-fashion editorial romance with the tactile clarity of Apple Human Interface Guidelines (HIG). Built for seamless guest management, RSVP workflows, and celebratory day-of coordination, the UI delivers an intimate, serene, and celebratory ambiance without compromising iOS operational rigor.

### Aesthetic Foundation
- **Editorial Chic Meets iOS Fluidity:** Refined typographic pairings combined with standard Apple navigation paradigms (large titles, inline toolbars, sensory haptics, sheet presentations).
- **Sensory Nuance:** Warm alabaster backdrops, gossamer-thin frosted glass overlays, and delicate micro-borders deliver depth without visual weight.
- **Tone:** Reverent, poised, celebratory, and frictionless. Interactions feel like flipping through a heavy-weight custom invitation suite that dynamically updates.

## Colors

The palette balances warm organic celebration hues with functional iOS neutral surfaces.

- **Primary (`#9B3D3D` Terracotta Rose):** Used for focal CTAs, critical confirmation actions, heart states, and major milestones. Supports an interactive state variant at `#B85B5B`.
- **Secondary (`#C5A059` Vintage Gilded Gold):** Reserved for celebratory accents, VIP/Registry emblems, badges, and delicate timeline markers.
- **Tertiary (`#7A8C76` Soft Sage):** Governs positive statuses (RSVP Confirmed, Attending, Seated), nature cues, and soothing secondary confirmations.
- **Neutral Dark (`#1F1D1B` Obsidian Charcoal):** High-contrast, warm-tinted ink ensuring AAA text accessibility across body and headline copy.
- **Canvas & Substrates:** Primary canvas anchors at `#FAF7F2` (Warm Champagne Ivory), while nested module panels and grouped table backgrounds transition through `#F5EFEB`.
- **Dividers & Strokes:** Soft 1px rules styled with `rgba(31, 29, 27, 0.06)` for gentle structural boundaries.

## Typography

Typographic scale is structured around iOS human interface proportions while imparting editorial polish.

- **Headlines (`Playfair Display`):** Brings bespoke stationery character to couple titles, countdowns, event sections, and major sheet titles.
- **Interface & Metrics (`Plus Jakarta Sans`):** Selected for its crisp geometric legibility, geometric balance, and optical clarity at small sizes on Retina displays. It manages all operational layers—guest counts, meal selections, timestamps, and interactive controls.
- **Hierarchy Rules:** Never use the serif family below 20px. System labels, tabular numeric data, and tracking numbers strictly utilize `Plus Jakarta Sans` with appropriate tracking (`caption-sm` features +0.04em letter-spacing for uppercase badges).

## Layout & Spacing

The layout model respects Apple's standard portrait-first viewport while providing generous breathing room reminiscent of print invitations.

- **Layout Grid:** Single-column fluid layout with dynamic margins on phone viewports (`margin-sm: 1rem` up to standard `margin: 1.25rem`). Multi-column card grids on iPads deploy an 8-column layout with `gutter: 1.5rem`.
- **Vertical Flow:** Standard iOS bottom navigation bars and floating toolbars preserve 34pt bottom safe area margins. Content stacks conform to 4pt/8pt modular increments.
- **Nested Density:** Card interiors apply `space-lg` (24px) for featured event summaries and `space-md` (16px) for compact list groupings (e.g., guest registry lists and itinerary items).

## Elevation & Depth

Visual hierarchy uses physical sheet elevations combined with iOS material diffusion rather than heavy synthetic drop shadows.

- **Base Layer:** `#FAF7F2` solid background.
- **Frosted Glass Cards (System Thin Material):** Background `rgba(255, 255, 255, 0.65)` layered with `backdrop-filter: blur(20px) saturate(180%)`. Border: `1px solid rgba(255, 255, 255, 0.6)`. Shadow: `0 8px 32px 0 rgba(31, 29, 27, 0.04)`.
- **Floating Modals & Sheets:** Elevated surface `rgba(255, 255, 255, 0.88)` with `backdrop-filter: blur(28px)`, bound by `0 16px 40px -8px rgba(31, 29, 27, 0.08)` and a faint top highlight edge.
- **Interactive Taps:** Elements compress inward subtly on active state (`transform: scale(0.98)` alongside standard iOS haptic feedback) rather than projecting forward with drop shadows.

## Shapes

Shapes feature organic, generous curves that evoke invitations, wax seals, and contemporary iOS continuous corners (squircle).

- **Standard Containers & Cards:** Configured with 20px–24px outer border radiuses (`rounded-xl`), creating soft pockets of information.
- **Pill Elements:** Buttons, chips, search pills, and segmented control highlights use full pill styling (`border-radius: 9999px`).
- **Inner Nested Radii:** For components enclosed within cards, radii step down to 12px (`rounded-md`) to ensure concentric corner curves.

## Components

### Buttons & Action Controls
- **Primary Action Button:** Full-width pill (`height: 52px`), Terracotta Rose fill (`#9B3D3D`), crisp white label (`Plus Jakarta Sans, 16px, weight 600`), and subtle inner top stroke (`rgba(255, 255, 255, 0.2)`).
- **Secondary Action Button:** Frosted glass pill with 1px border `rgba(31, 29, 27, 0.12)`, text `#1F1D1B`.
- **Text & Inline Actions:** Gilded gold or terracotta interactive labels accompanied by iOS SF-style chevron icons.

### Segmented Controls & Pills
- **iOS Segmented Tab Track:** Recessed capsule container filled with `rgba(0, 0, 0, 0.04)`, 4px inner padding.
- **Active Thumb:** Floating pill of solid white with soft ambient shadow `rgba(0, 0, 0, 0.06)`, text weight transitioning to semi-bold Obsidian.
- **Filter Chips:** Pill shape with 8px horizontal padding, defaulting to translucent white and activating to Terracotta or Sage with white text.

### Guest & Itinerary Cards
- **RSVP Card:** Frosted translucent substrate, 20px corner radius, hairline 1px border (`rgba(31, 29, 27, 0.06)`). Top right status pill indicating Sage Green (`#7A8C76`) "Attending" or Terracotta "Awaiting".
- **Timeline Milestone Item:** Vertical hair-stroke trail punctuated by warm gold `#C5A059` node bullets, featuring serif headings for the key event and sans-serif auxiliary text for the time and location.

### Input Fields & Pickers
- **Text Inputs:** Floating label style or clean inset box (`height: 50px`), filled with `rgba(255, 255, 255, 0.7)`, focused boundary highlighting with Terracotta Rose (`#9B3D3D`, 1.5px border).
- **Checkboxes & Radios:** Circular selection wells with spring animations. Selected checkboxes present a smooth fill in Terracotta with a centered white check icon.