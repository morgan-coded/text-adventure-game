# Testing Strategy

Testing must reflect real dock conditions: interruptions, simultaneous requests, and seasonal spikes.

## Unit Testing (examples)
- Reservation creation logic
- Inventory locking logic (prevent double-booking)
- Payment validation logic
Example: attempt to book the same asset at the same time from two test users; system should block one.

## Integration Testing (examples)
- A confirmed reservation updates public availability and admin dashboard immediately.
- Cancellation updates availability and triggers correct customer messaging.
- Maintenance hold removes asset from availability everywhere.

## User Acceptance Testing (UAT)
Performed by owners + dock staff using realistic scenarios:
- mock "full day" workflow: walk-ins, phone bookings, cancellations, weather delays
Acceptance criteria:
- dock staff can complete tasks faster than binder workflow
- minimal confusion / no technical help needed to complete core workflows
