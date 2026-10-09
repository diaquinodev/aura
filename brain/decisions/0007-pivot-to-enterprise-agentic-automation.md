# 0007 Pivot de SaaS vertical de saúde para automação agêntica corporativa

**Status:** Aceita · **Owner:** Operador · **Data:** 2026-10-09 (Pivot 01) · **Substitui:** o posicionamento definido no Bootstrap 01

## Contexto

O Bootstrap 01 posicionou o projeto como um SaaS vertical para negócios baseados em agendamento. Antes de existir qualquer código de produto, o operador reavaliou a direção frente aos objetivos reais do projeto: um laboratório de Agentic AI Engineering, uma simulação corporativa realista e um portfólio alinhado ao mercado corporativo de AI engineering.

## Direção anterior

Registrada aqui porque o Git ainda não estava inicializado e os documentos sobrescritos não têm histórico de versões.

- **Empresa:** "Aura Studio", software B2B para negócios premium de dermatologia, odontologia, estética, cabelo/beleza e bem-estar.
- **Produto:** "Aura Flow", automação de lead → qualificação → agendamento → confirmação → lembrete → comparecimento → follow-up → analytics.
- **Hipóteses principais:** no-shows estão entre as três maiores dores; um único produto serve aos cinco segmentos; os donos pagariam só por confirmações/lembretes.
- **Roadmap:** 0 Foundation, 1 Work Management, 2 Synthetic Company, 3 Core Product, 4 Scheduling, 5 Integrations (Google Calendar, WhatsApp), 6 Agentic Engineering, 7 Observability & Evals, 8 Reliability, 9 Pilot Readiness.
- **Doc completo do produto:** mantido como superseded em `docs/product/AURA-FLOW.md`.

## Nova direção

- **Empresa:** AURA, uma empresa B2B fictícia de automação inteligente e auditável de processos corporativos com agentes de IA, integrações, dados e workflows human-in-the-loop.
- **Produto:** Aura Ops (`docs/product/AURA-OPS.md`).
- **Primeiro domínio:** Finance & Operations, especificamente Accounts Payable. Um workflow real primeiro; outros domínios só depois que ele estiver completo.
- **Primeiro cliente sintético:** Nexa Group. *Atualização 2026-10-09: renomeado para `AURA-SYN-001 — Synthetic Finance Enterprise` (`simulation/AURA-SYN-001.md`), decisão 0008.*

## Justificativa

- Accounts Payable tem uma estrutura determinística rica (pedidos de compra, recebimentos, faturas, 3-way match) e incerteza real (interpretação de documentos, investigação de divergências). Isso o torna um bom laboratório para a fronteira entre regras e IA, que é a habilidade central de enterprise AI engineering.
- Por natureza, exige aprovação humana, auditoria e controles, então human-in-the-loop e auditabilidade são requisitos, não enfeite.
- Corresponde mais de perto ao tipo de trabalho para o qual times corporativos de IA/automação estão contratando do que um produto de agendamento. Isto é um julgamento do operador, não validado com dados de mercado.

## Benefícios

- Alinhamento mais forte entre o portfólio e as vagas corporativas.
- A exposição regulatória ligada à saúde (dados clínicos) sai do scope.
- O workflow exercita SQL, integrações, regras, agentes, evals e auditoria em um único fluxo coerente.

## Trade-offs

- Finanças é menos intuitivo para o operador do que um fluxo de agendamento; é preciso mais aprendizado de domínio (AP, 3-way match, controles) antes da engenharia.
- Um enquadramento de "plataforma" convida a scope creep. Mitigado por "um workflow real primeiro".
- Erros financeiros custam mais caro que erros de agendamento, mesmo em simulação: o design precisa modelar aprovação e auditoria desde o início.
- A prática de integração com mensageria/calendário (WhatsApp, Google Calendar) sai do roadmap.

## Consequências

- README, empresa, organização, roadmap, regras dos agentes, exemplos de comunicação e glossário atualizados.
- `docs/product/AURA-FLOW.md` e `brain/insights/no-show-first-metric.md` marcados como SUPERSEDED, não excluídos.
- A decisão 0003 (apenas dados sintéticos) continua válida, com nova justificativa.
- `docs/architecture/`, `docs/status/` e `simulation/` criados porque agora têm conteúdo real (consistente com a 0002).
