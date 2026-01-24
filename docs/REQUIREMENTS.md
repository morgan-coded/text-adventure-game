# Requirements

## Functional Requirements (FR)
FR1: Online reservations with real-time availability
- Customers can book without calling.
- System prevents overlapping bookings via inventory locking / conflict prevention.

FR2: Inventory and maintenance tracking
- Each asset has a status: available, reserved, checked out, maintenance.
- Maintenance holds remove assets from public availability immediately.

FR3: Automated confirmations and reminders
- Immediate confirmation on booking.
- Reminder messaging day-before (email; SMS optional).

FR4: Administrative dashboard
- Calendar view, list/search view, quick edits (modify/cancel), discount tools.
- Override controls for phone bookings and walk-ins.

FR5: Reporting
- Revenue by category
- Utilization by asset
- Cancellation rates
- Booking channel mix

## Non-Functional Requirements (NFR)
Security & privacy:
- HTTPS
- role-based access
- use payment gateway; do not store full credit card numbers
- least-privilege access + secure backups

Performance & reliability:
- mobile-first experience
- core pages load quickly (target: ~2 seconds on typical mobile connections)

Usability:
- seasonal staff should learn core workflows in under an hour
- booking flow must be readable outdoors and easy under interruptions

## Use Cases

Use Case A: Customer booking (mobile)
1) User selects Rentals and chooses category/asset.
2) System shows availability calendar (unavailable dates disabled).
3) User selects date/time; system calculates total and offers add-ons.
4) Checkout holds asset for a short window (e.g., 15 minutes), collects contact info + payment.
5) System confirms booking and sends receipt/arrival instructions.

Use Case B: Staff phone booking
1) Staff opens admin calendar for requested date/time.
2) System shows remaining inventory and maintenance holds.
3) Staff selects an available asset, enters customer details, applies discount if needed, confirms.
4) System sends confirmation and updates availability instantly.
5) If customer changes times, system checks conflicts before saving.
