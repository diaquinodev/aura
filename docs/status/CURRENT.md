# Status atual

Retrato operacional. Atualize ao fim de toda sessão que o altere. O README muda apenas em marcos. Regras de evidência: [../process/WORKING-MODEL.md](../process/WORKING-MODEL.md).

**Última atualização:** 2026-10-09 (Bootstrap 02, primeiro PR)

| Campo | Valor |
|---|---|
| Stage atual | Stage 1 — Engineering Core: em andamento |
| Sprint atual | Sprint 1 (milestone do GitHub): #1 esqueleto, #2 CI, #3 schemas, #4 validação |
| Feature atual | Esqueleto do serviço + CI (`feat/service-skeleton`, fecha #1 e #2) |
| Problema atual | Accounts Payable inteligente, primeira fatia: validação determinística de faturas e 3-way match ([../product/AURA-OPS.md](../product/AURA-OPS.md)) |
| Baseline atual | Nenhuma ainda; não há lógica de domínio para medir |
| Evidência atual | `GET /health` → 200 (pytest local; execução real com uvicorn); resultado de CI no primeiro PR |
| Nível de treinamento atual | `TRAINING_LEVEL = 1` (Guided) |
| Próximo marco | Definition of done do Stage 1 ([../product/ROADMAP.md](../product/ROADMAP.md)) |

## Riscos atuais

| Risco | Impacto | Mitigação | Responsável |
|---|---|---|---|
| Sem lockfile de dependências | O CI pode instalar versões mais novas que as locais | Aceito por enquanto (decisão 0009) | Engineering |
| Sem board no GitHub Projects | Sprint visível apenas como milestones | `gh auth refresh -s project`, depois criar o board | Operador |
| `/setup-pstack` não executado | As skills do pstack usam os modelos padrão | Executar `/setup-pstack` | Operador |
| O enquadramento como plataforma convida scope creep | Muitos domínios construídos pela metade | "Um workflow real primeiro" (decisão 0007) | Operador |

## Decisões pendentes do operador

Revisar as decisões 0001, 0002 e 0006; política de tolerância de preço para o #5 (refinement).
