# Proposed Database Schema (Relational)

## Customer
- CustomerID (PK)
- FirstName
- LastName
- Email (unique)
- Phone
- CreatedAt

## Asset
- AssetID (PK)
- AssetType
- AssetName
- Status
- HourlyRate
- DailyRate
- LastServiceDate

## Reservation
- ReservationID (PK)
- CustomerID (FK)
- AssetID (FK)
- StartDateTime
- EndDateTime
- Status
- TotalPrice
- CreatedAt

## Payment
- PaymentID (PK)
- ReservationID (FK)
- Provider
- ProviderTxnID
- Amount
- PaymentStatus
- PaidAt

## Indexes (performance)
- Reservation.StartDateTime
- Reservation.AssetID
- Reservation.Status
These support fast availability checks as records grow across seasons.
