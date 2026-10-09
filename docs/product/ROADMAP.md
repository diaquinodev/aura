# Roadmap

Baseado em capacidades, sem datas. Um stage está concluído quando sua capacidade é demonstrada com evidências, não quando o tempo passa. A ordem pode mudar; cada mudança é registrada em `brain/decisions/`. O roadmap anterior (direção de saúde) está registrado na decisão 0007.

| Stage | Nome | Capacidade | Status |
|---|---|---|---|
| 0 | Foundation | Documentação, Git, sistema de aprendizado, pstack | COMPLETE |
| 1 | Engineering Core | Serviço Python + FastAPI, testes, workflow de Git | Em andamento |
| 2 | Enterprise Simulation | Empresa sintética, personas, Jira, reuniões | Não iniciado |
| 3 | Data & Persistence | PostgreSQL, datasets sintéticos, modelo de auditoria | Não iniciado |
| 4 | Finance Workflow | Workflow de Accounts Payable inteligente de ponta a ponta | Não iniciado |
| 5 | External Integrations | ERP/APIs simulados, webhooks | Não iniciado |
| 6 | Agentic Layer | Ferramentas, agentes, MCP, orquestração onde justificado | Não iniciado |
| 7 | Evals & Observability | Tracing, qualidade, latência, custo | Não iniciado |
| 8 | Reliability & Security | Incidentes, guardrails, resiliência | Não iniciado |
| 9 | Multi-Workflow Platform | Processos corporativos adicionais, depois que o Stage 4 estiver completo | Não iniciado |
| 10 | Pilot Readiness | Avaliar se um piloto real está pronto do ponto de vista legal, técnico e ético | Não iniciado |

## Critérios de saída do Stage 0

- [x] A documentação canônica existe e passa em `python tools/check_docs.py`.
- [x] As áreas de memória (`brain/`) e de aprendizado (`docs/learning/`) existem e estão separadas.
- [x] O posicionamento está coerente após o Pivot 01.
- [x] Git inicializado pelo operador e primeiro commit feito.
- [ ] O operador revisou e aceitou (ou alterou) as decisões em `brain/decisions/`. Parcialmente feito (0007 e 0008 decididas); o restante segue para o Bootstrap 02 e não o bloqueia.

A partir do Stage 1, um stage só está completo com evidência executável (regra rígida em [../process/WORKING-MODEL.md](../process/WORKING-MODEL.md)).

## Definition of done do Stage 1

- [x] Projeto Python inicializado
- [x] Serviço FastAPI rodando localmente
- [ ] Schemas Pydantic para o domínio de faturas
- [ ] Validação determinística de faturas
- [ ] 3-way match determinístico
- [ ] Testes com pytest, incluindo edge cases
- [ ] Trabalho feito em uma branch e com merge via pull request
- [ ] CI rodando os testes em todo PR
- [ ] Um case study pequeno: **Case 001 — Deterministic 3-Way Matching Engine** (hipótese: regras financeiras determinísticas devem ser resolvidas de forma determinística antes de introduzir qualquer IA; deve incluir problema, baseline, implementação, testes, edge cases e evidências)

## Caminho de validação externa

```text
Simulação → Demo interna → Revisor externo → Feedback de usuário real → Piloto
```

Não é necessário um cliente real para começar, mas a AURA não pode ficar indefinidamente sem validação externa. Revisores candidatos: um analista financeiro, um profissional de operações, um desenvolvedor, um recrutador técnico, um profissional de dados. Nada agendado; o primeiro checkpoint candidato é após o Stage 4.
