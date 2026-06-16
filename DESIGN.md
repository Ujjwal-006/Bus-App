---
name: TRAJET Transit System
colors:
  surface: '#faf9fd'
  surface-dim: '#dad9de'
  surface-bright: '#faf9fd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f8'
  surface-container: '#eeedf2'
  surface-container-high: '#e9e7ec'
  surface-container-highest: '#e3e2e7'
  on-surface: '#1a1b1f'
  on-surface-variant: '#43474f'
  inverse-surface: '#2f3034'
  inverse-on-surface: '#f1f0f5'
  outline: '#747780'
  outline-variant: '#c4c6d0'
  surface-tint: '#415e91'
  primary: '#001737'
  on-primary: '#ffffff'
  primary-container: '#042b5b'
  on-primary-container: '#7794ca'
  inverse-primary: '#abc7ff'
  secondary: '#0060ab'
  on-secondary: '#ffffff'
  secondary-container: '#61a9ff'
  on-secondary-container: '#003c6f'
  tertiary: '#001a24'
  on-tertiary: '#ffffff'
  tertiary-container: '#00303f'
  on-tertiary-container: '#509cba'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e3ff'
  primary-fixed-dim: '#abc7ff'
  on-primary-fixed: '#001b3f'
  on-primary-fixed-variant: '#284678'
  secondary-fixed: '#d3e3ff'
  secondary-fixed-dim: '#a3c9ff'
  on-secondary-fixed: '#001c39'
  on-secondary-fixed-variant: '#004882'
  tertiary-fixed: '#bce9ff'
  tertiary-fixed-dim: '#86d0f0'
  on-tertiary-fixed: '#001f29'
  on-tertiary-fixed-variant: '#004d63'
  background: '#faf9fd'
  on-background: '#1a1b1f'
  surface-variant: '#e3e2e7'
typography:
  display-hero:
    fontFamily: Inter
    fontSize: 90px
    fontWeight: '800'
    lineHeight: '0.9'
    letterSpacing: -0.04em
  display-hero-mobile:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  container-max: 1440px
---

## Brand & Style

The design system is rooted in the principles of Swiss International Style—clarity, precision, and a grid-based hierarchy—reimagined for a futuristic transit context. It targets a sophisticated audience that values efficiency, reliability, and technical excellence. 

The aesthetic is **Modern Minimalist with Glassmorphic accents**. It avoids decorative excess in favor of structural integrity. The emotional response should be one of "calm authority"—a platform that feels both cutting-edge and deeply dependable. The UI utilizes massive, high-impact typography contrasted against generous whitespace and thin, technical borders to create a sense of architectural scale.

## Colors

The palette is a monochrome-adjacent blue scale that emphasizes depth and technical precision.
- **Primary (Dark Navy):** Used for core branding, primary actions, and high-contrast headings.
- **Accent (Blue):** Reserved for interactive elements, focus states, and primary navigational cues.
- **Badge (Soft Cyan):** A functional color used for status indicators, tags, and secondary highlights.
- **Surface & Background:** A crisp, "cool" white environment (#F8FBFD) supported by a Light Blue (#E2F0FF) for subtle structural sectioning.
- **Typography:** Primary text uses the Dark Navy for maximum legibility, while metadata and secondary labels utilize Text Gray.

## Typography

This design system utilizes a dual-font strategy to balance impact with technical clarity.
- **Inter (Headlines):** Set with tight tracking and aggressive line heights for a bold, editorial feel. The `display-hero` style is the centerpiece of the system, designed to command attention.
- **Manrope (Body & Technical):** Chosen for its geometric, modern proportions. Body text should be set with slightly expanded letter spacing to ensure readability in high-density transit data environments.
- **Hierarchy:** Use all-caps labels for metadata and technical specs to reinforce the "instrument panel" aesthetic.

## Layout & Spacing

The layout follows a strict **12-column fixed grid** on desktop, transitioning to a **4-column fluid grid** on mobile. 

- **Alignment:** Everything must align to a 4px baseline grid. 
- **Whitespace:** Use generous margins (64px+) between major sections to allow the bold typography to breathe. 
- **Data Density:** While the overall layout is airy, functional data modules (like schedules or route lists) should use a compact 8px/16px spacing rhythm to keep information scannable.
- **Breakpoints:** Mobile (<768px), Tablet (768px - 1024px), Desktop (>1024px).

## Elevation & Depth

This design system avoids traditional heavy dropshadows, favoring a "Tectonic" layering approach:
- **Thin Outlines:** Most containers use a 1px border (#E2F0FF or semi-transparent Navy) to define boundaries.
- **Glassmorphism:** High-priority floating elements (modals, navigation bars, hover cards) utilize a backdrop-filter blur of 20px with a 60% opaque white fill. This creates a "frosted" look that feels futuristic and premium.
- **Layering:** Depth is communicated through color blocks. The primary background is the lowest layer, with "Light Blue" surfaces acting as intermediate containers.

## Shapes

The shape language is predominantly **geometric and sharp**.
- **Buttons & Small Components:** Use a 2px radius. This "near-sharp" look communicates precision and fits the Swiss-inspired aesthetic.
- **Cards & Primary Containers:** Use a slightly softer 8px radius (rounded-lg equivalent) to subtly differentiate content areas from interactive controls.
- **Icons:** Should be stroke-based (2px weight) with squared ends to match the typography.

## Components

- **Buttons:** Primary buttons are Solid Navy (#042B5B) with white text and a 2px radius. Secondary buttons use the Navy as a 1px outline with a transparent background. Transitions should be a swift 150ms ease-out.
- **Input Fields:** 1px border (#5D6875 at 20% opacity). On focus, the border shifts to the Accent Blue (#2A7CCF) with no glow.
- **Chips/Badges:** Use the Soft Cyan (#8DD7F7) background with Dark Navy text. These should be rectangular with the standard 2px radius.
- **Cards:** White or Glassmorphic backgrounds. Borders are 1px #E2F0FF. Content within cards should follow the 24px internal padding rule.
- **Transit Indicators:** Use monospaced numbers (within the Manrope family) for time and platform data to ensure vertical alignment in lists.
- **Navigation Bar:** A top-mounted, glassmorphic blur-bar with a 1px bottom border. Links are in Dark Navy, using the `label-caps` typography style.