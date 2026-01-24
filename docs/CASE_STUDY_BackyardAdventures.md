# Case Study: Backyard Adventures (BackyardAdventures)

Backyard Adventures (BA) offers boat and kayak rentals and guided tours in Jacksonville, Florida. The business receives interest from advertising but struggles to convert that interest into confirmed bookings.

## Current workflow (problem)
BA relies on a binder-and-spreadsheet process. During peak times, overlapping phone calls and walk-ins increase the chance of:
- double-bookings
- inconsistent customer communication
- poor visibility into equipment status (available/reserved/checked out/maintenance)
- lost revenue from after-hours booking demand

## Proposed system (high-level)
A centralized, web-based reservation + inventory system that supports:
- mobile-first customer booking flow
- real-time availability and inventory locking to prevent conflicts
- admin dashboard for dock staff (calendar + search + quick edits)
- automated confirmations and reminders
- basic reporting for owners (utilization, revenue by category, cancellation rate, booking channels)

## Scope (initial release)
In-scope:
- browse offerings, check availability, reserve equipment, collect payment, send confirmation
- staff tools for phone bookings, walk-ins, cancellations, maintenance holds
- reporting basics

Out-of-scope (initial):
- advanced marketing automation
- custom native mobile apps

## Feasibility (summary)
- Technical: standard web stack + relational DB + payment gateway; key risks are dock internet reliability and secure handling of customer data.
- Economic: small business build estimated around $6k–$10k upfront plus ~$50–$100/month hosting/monitoring; benefits include reduced admin time and fewer booking errors.
- Operational: adoption depends on dock workflows; phased rollout + training recommended.
