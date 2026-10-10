# Modelo de trabalho

Como o trabalho vai fluir pela empresa simulada. A maior parte disto **ainda não está implementada**; a coluna "Hoje" diz o que já existe.

```text
Evento de negócio → Ticket → Triagem → Priorização → Investigação → Implementação
  → Verificação → Review → CI → Release → Feedback → Métricas → Aprendizado
```

| Etapa | Significado simples | Hoje |
|---|---|---|
| Evento de negócio | Algo acontece: uma reclamação de cliente (simulado), um bug, uma nova necessidade | Não implementado (Stage 2) |
| Ticket | O evento é registrado como uma unidade de trabalho com um resultado claro | GitHub Issues (formato: `COMMUNICATION.md`) |
| Triagem | É real, qual a urgência, quem tem o ownership? | Manual, na issue |
| Priorização | Comparado com outros trabalhos por valor, risco e custo | Milestones como sprints (`Sprint 1`, `Sprint 2`) |
| Investigação | Entender o sistema e a causa antes de mudar qualquer coisa | Manual, com pstack `/how` e `/why` |
| Implementação | Menor mudança correta em uma branch; `main` é a baseline estável, e as mudanças chegam a ela via PR | Branch + PR no GitHub |
| Verificação | Provar que funciona: testes, comandos, evidências (veja Progresso válido abaixo) | pytest + `tools/check_docs.py` |
| Review | Outra pessoa (humano ou agente) questiona a mudança | O operador revisa e faz o merge dos PRs; template de PR em `.github/` |
| CI | Verificações automatizadas em toda mudança | GitHub Actions (`.github/workflows/ci.yml`) |
| Release | A mudança chega aos usuários | Não implementado |
| Feedback | O que os usuários (simulados) dizem ou fazem | Não implementado (Stage 2) |
| Métricas | Números que mostram se a mudança ajudou | Não implementado (Stage 7) |
| Aprendizado | Decisões, gotchas e skills atualizados | `brain/` e `docs/learning/` |

## Progresso válido e proof of work

Esta seção é a fonte canônica do que conta como progresso. A pergunta que todo componente deve ajudar a responder: *que evidência existe de que este engenheiro consegue resolver problemas reais com software e IA?*

```text
ARCHITECTURE + WORKING SOFTWARE + TESTS + EVIDENCE + METRICS + EXPLANATION = VALID PROGRESS
```

### Regra rígida

A partir do Stage 1, **nenhum milestone está completo apenas com documentação.** Cada milestone produz pelo menos um dos seguintes: código executável, um teste automatizado, uma integração funcionando, um benchmark, um eval, um trace, uma métrica, um incident reproduzível, um PR com evidências ou uma demo verificável.

### Proof of work

O conjunto de evidências que permite a outra pessoa verificar que o trabalho foi realmente feito **e compreendido**: código, testes, PRs, execuções de CI, logs, traces, evals, benchmarks, registros de decisão, relatórios de incident, case studies, vídeos de demo. Ele fecha a distância entre "eu conheço esta tecnologia" e "aqui está a evidência de que eu a usei para resolver um problema".

**Proof of authorship.** Entregas relevantes registram o *porquê*, não apenas o *quê*. O operador deve ser capaz de responder: Por que esta arquitetura? Por que este banco de dados? Por que IA aqui, e por que não código determinístico? Quais modos de falha existem? Quais são os trade-offs? O que quebra em uma escala maior? Como foi verificado?

A partir do #3, o código de produto e as seções "Como foi verificado" e "Riscos" dos PRs são escritos pelo operador; o agente explica, revisa e cuida da infraestrutura de apoio.

### Evidência

Toda afirmação técnica relevante é escrita assim:

```text
CLAIM:     O processamento duplicado foi corrigido.
EVIDENCE:  10.000 eventos sintéticos executados contra a correção.
RESULT:    0 duplicados (baseline: 17). SYNTHETIC.
```

"Funciona" nunca é uma afirmação sem evidência.

- **Baseline primeiro.** Antes de otimizar ou automatizar, registre o valor atual quando for mensurável (tempo de processamento, taxa de erro, quantidade de duplicados, sucesso da tarefa, latência, tokens, custo, escalations para humanos). Nunca invente métricas só para ter números.
- **SYNTHETIC ou REAL.** Toda métrica leva um rótulo. Correto: "Em um benchmark sintético com 10.000 eventos, o processamento duplicado caiu de 17 casos para zero." Incorreto: "AURA reduziu em 100% os erros de processamento da empresa."

### Pull requests

Toda descrição de PR relevante contém:

```text
Por quê / O quê / Como foi verificado / Métricas / Riscos / Não verificado / Follow-ups
```

### Histórico do Git

O histórico do Git faz parte do portfólio: cada commit é um passo lógico com uma mensagem convencional (`feat: implement invoice validation`, `test: add matching edge cases`, `fix: prevent duplicate processing`). Nunca `updates`, `changes`, `final`, `fix stuff`.

### Case studies e engineering demos

- Um **case study** é escrito apenas para um problema relevante, não por sessão, usando [../case-studies/_TEMPLATE.md](../case-studies/_TEMPLATE.md).
- Uma **engineering demo** mostra o caminho, não apenas uma UI: problema de negócio → ticket → investigação → implementação → teste → PR → CI → resultado.

### Documentation budget

A documentação não deve crescer significativamente mais rápido que a engenharia executável. Se várias sessões consecutivas produzirem apenas documentação, pare e pergunte se há progresso técnico real antes de escrever mais.

## Ferramentas: pstack

O pstack v0.15.15 está instalado como plugin do Cursor. Seus skills são usados a partir do plugin; nenhum é copiado para este repositório. `/setup-pstack` ainda não foi executado (não há `~/.cursor/rules/pstack-models.mdc`), então os skills usam seus modelos padrão.

| Situação | Usar |
|---|---|
| Trabalho de engenharia não trivial | `/poteto-mode` |
| Preciso entender um subsistema ou onde o código deve ficar | `/how` |
| Preciso do motivo por trás de uma decisão ou regressão | `/why` |
| O operador quer entender a fundo uma parte do trabalho | `/teach` |
| Retomar o trabalho após uma pausa | `/recall` |
| Review adversarial de uma mudança | `/interrogate` |
| O próprio workflow foi ineficiente | `/reflect` |
| Os agentes continuam repetindo o mesmo erro | `/correct` |

### Regra de roteamento do que aprendemos

```text
Fatos da sessão           → docs/learning/journal/ e brain/
Aprendizado de workflow   → /reflect
Falha recorrente          → /correct
```

`/reflect` propõe edições em skills existentes. Antes de aceitar uma, confirme que a lição é reutilizável além de uma única sessão; uma experiência isolada não deve virar uma regra permanente. Veja [../../brain/inbox/reflect-edit-targets.md](../../brain/inbox/reflect-edit-targets.md).
