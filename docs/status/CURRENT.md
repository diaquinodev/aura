# Status atual

Retrato operacional. Atualize ao fim de toda sessão que o altere. O README muda apenas em marcos. Regras de evidência: [../process/WORKING-MODEL.md](../process/WORKING-MODEL.md).

**Última atualização:** 2026-10-09 (auditoria depois do PR #9)

| Campo | Valor |
|---|---|
| Stage atual | Stage 1 — Engineering Core: em andamento |
| Sprint atual | Sprint 1 (milestone do GitHub): #1 esqueleto e #2 CI fechadas (PR #7); #3 schemas e #4 validação abertas |
| Feature atual | Nenhuma em andamento. Próxima: #3 schemas do domínio de faturas (owner: operador) |
| Problema atual | Accounts Payable inteligente, primeira fatia: validação determinística de faturas e 3-way match ([../product/AURA-OPS.md](../product/AURA-OPS.md)) |
| Baseline atual | Nenhuma ainda; não há lógica de domínio para medir |
| Evidência atual | `GET /health` → 200 (pytest local; execução real com uvicorn); CI verde nos PRs #7 e #9 |
| Nível de treinamento atual | `TRAINING_LEVEL = 1` (Guided) |
| Próximo marco | Definition of done do Stage 1 ([../product/ROADMAP.md](../product/ROADMAP.md)) |

## Fila

1. Refinement do #5: tolerância de preço absoluta, percentual ou as duas (decisão do operador).
2. #3, #4 e #5 programados pelo operador; o agente explica e revisa.
3. #6 Case 001: faturas sintéticas geradas com seed fixa e script que produz números SYNTHETIC.
4. Preparação para abrir o repositório: licença, `docs/archive/`, lockfile, varredura de secrets no histórico; depois, tornar público e ligar branch protection.

Até o Stage 1 fechar, nenhuma documentação nova além deste arquivo e dos journals.

## Riscos atuais

| Risco | Impacto | Mitigação | Responsável |
|---|---|---|---|
| Repositório privado no plano gratuito | Branch protection indisponível (HTTP 403): nada impede merge com CI vermelho; o repositório não serve como prova pública | Item 4 da fila | Operador |
| Histórico de commits com co-autoria do agente | Um leitor pode concluir que o repositório foi gerado por agente | Código de produto escrito pelo operador a partir do #3 | Operador |
| Sem lockfile de dependências | O CI pode instalar versões mais novas que as locais; os números do Case 001 não seriam reproduzíveis | Criar antes do Case 001 (item 4 ou antes do #6) | Engineering |
| Sem board no GitHub Projects | Sprint visível apenas como milestones | `gh auth refresh -s project`, depois criar o board | Operador |
| O enquadramento como plataforma convida scope creep | Muitos domínios construídos pela metade | "Um workflow real primeiro" (decisão 0007) | Operador |

## Decisões pendentes do operador

Tolerância de preço do #5 (refinement); licença (no PR de preparação para abrir o repositório); revisar as decisões 0001, 0002 e 0006.
