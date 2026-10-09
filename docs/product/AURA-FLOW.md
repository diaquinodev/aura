# Aura Flow (codename)

> **STATUS: SUPERSEDED**
>
> This document belongs to the previous vertical-health positioning of AURA. The current product direction is Aura Ops — Enterprise Agentic Automation Platform.
>
> Current source of truth: [docs/product/AURA-OPS.md](AURA-OPS.md). Why it changed: decision 0007.

Status: **concept** (at the time). Everything below is a hypothesis unless marked otherwise. No technical architecture is defined here on purpose.

## Problem (hypothesis)

Appointment-based premium businesses lose revenue between first contact and attended appointment: slow replies lose leads, missing confirmations cause no-shows, and front-desk staff repeat the same messages all day.

## Users (hypothesis)

| Persona | Role | Wants |
|---|---|---|
| Owner/manager | Buyer | Fuller agenda, fewer no-shows, funnel visibility |
| Front desk | Daily user | Less repetitive messaging, fewer scheduling mistakes |
| Professional | Indirect user | Accurate agenda |
| End client | Receives messages | Fast answers, easy booking and rescheduling |

## Journey

```text
lead → qualification → service → professional → availability
     → booking → confirmation → reminder → attendance → follow-up → analytics
```

| Step | What Aura Flow would do (hypothesis) |
|---|---|
| Lead | Capture an inbound contact from a channel |
| Qualification | Ask what the person wants (administrative/commercial, never clinical) |
| Service | Map the request to a service in the business catalog |
| Professional | Pick who can perform it |
| Availability | Find open slots |
| Booking | Reserve the slot |
| Confirmation | Get explicit confirmation from the client |
| Reminder | Remind before the appointment |
| Attendance | Record attended / no-show / cancelled |
| Follow-up | Post-visit message, rebooking suggestion |
| Analytics | Funnel and no-show numbers for the owner |

## Goals (hypothesis)

- Reduce no-shows.
- Reduce time-to-first-reply for leads.
- Reduce manual front-desk messaging.
- Give the owner a funnel view.

## Non-goals (decision)

- No medical diagnosis, triage or clinical advice.
- No medical records (prontuário) or clinical data.
- No payments in the first version.
- No real customer data until a pilot is explicitly approved.

## Hypothetical metrics

These are candidate metrics. Any value produced before a real pilot is **simulated**.

| Metric | Definition |
|---|---|
| No-show rate | No-shows / confirmed appointments |
| Lead-to-booking rate | Bookings / leads |
| Time to first reply | Median time from lead to first response |
| Manual messages per booking | Messages sent by staff / bookings |

## Risks

- Wrong or duplicated messages harm the customer's client relationship.
- Clients may write clinical information spontaneously; the product must not store or act on it.
- Channel providers (WhatsApp) restrict automated messaging and charge per conversation.
- Double booking if availability is not the single source of truth.

## Future integrations (not started)

- Google Calendar (availability and booking), Stage 5.
- WhatsApp (messaging channel), Stage 5.
- Others (Instagram, web form, existing clinic software): unknown.
