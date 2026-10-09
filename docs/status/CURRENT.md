# Current status

Operational snapshot. Update at the end of every session that changes it. The README changes only on milestones. Evidence rules: [../process/WORKING-MODEL.md](../process/WORKING-MODEL.md).

**Last updated:** 2026-10-09 (Bootstrap 02, first PR)

| Field | Value |
|---|---|
| Current Stage | Stage 1 — Engineering Core: in progress |
| Current Sprint | Sprint 1 (GitHub milestone): #1 skeleton, #2 CI, #3 schemas, #4 validation |
| Current Feature | Service skeleton + CI (`feat/service-skeleton`, closes #1 and #2) |
| Current Problem | Intelligent Accounts Payable, first slice: deterministic invoice validation and 3-way match ([../product/AURA-OPS.md](../product/AURA-OPS.md)) |
| Current Baseline | None yet; no domain logic to measure |
| Current Evidence | `GET /health` → 200 (pytest locally; real uvicorn run); CI result on the first PR |
| Current Training Level | `TRAINING_LEVEL = 1` (Guided) |
| Next Milestone | Stage 1 definition of done ([../product/ROADMAP.md](../product/ROADMAP.md)) |

## Current risks

| Risk | Impact | Mitigation | Owner |
|---|---|---|---|
| No dependency lockfile | CI may install newer versions than local | Accepted for now (decision 0009) | Engineering |
| No GitHub Projects board | Sprint visible only as milestones | `gh auth refresh -s project`, then create the board | Operator |
| `/setup-pstack` not run | pstack skills use default models | Run `/setup-pstack` | Operator |
| Platform framing invites scope creep | Many half-built domains | "One real workflow first" (decision 0007) | Operator |

## Pending operator decisions

Review decisions 0001, 0002, 0006; repository-content language in 0005; price tolerance policy for #5 (refinement).
