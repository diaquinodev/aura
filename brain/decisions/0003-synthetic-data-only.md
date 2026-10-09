# 0003 Synthetic data only

**Status:** Accepted · **Owner:** Operator · **Date:** 2026-10-08 (Bootstrap 01)

> **Update 2026-10-09 (decision 0007):** the domain changed from health-adjacent businesses to enterprise Finance & Operations. The decision still holds: real invoices, supplier and payment data are personal and confidential (LGPD still applies to personal data), so all organizations, documents and transactions remain synthetic. Pilot readiness is now Stage 10 and synthetic datasets are Stage 3. The original text below is kept as written.

## Context

Target segments (dermatology, dentistry, aesthetics) are health-adjacent. Real client data would bring legal obligations (for example LGPD) the project cannot meet yet, and a portfolio that blurs simulation and reality loses credibility.

## Decision

All customers, people and metrics are fictional until a pilot is explicitly approved in Stage 9. No clinical data, diagnosis or medical records at any stage currently planned.

## Rationale

Removes legal risk and keeps the portfolio honest.

## Trade-offs and alternatives

Use anonymized real data: still risky to collect and anonymize correctly; no benefit at this stage.

## Impact

Stage 2 must produce synthetic data realistic enough to exercise the product. `.gitignore` excludes local database files and `data/local/`.
