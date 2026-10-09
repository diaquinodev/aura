# 0006 Onde fica a política de comunicação

**Status:** Aceita, revisão do operador pendente · **Owner:** Operador · **Data:** 2026-10-08

## Contexto

A política de comunicação corporativa precisa valer em toda interação da simulação e sobreviver além do histórico do chat. O operador sugeriu uma Skill do Cursor ou uma Rule específica do simulador. O repositório não tem `.cursor/rules/` nem skills de projeto; o `AGENTS.md` já é aplicado automaticamente.

## Decisão

Política canônica e templates em `docs/process/COMMUNICATION.md`. O `AGENTS.md` ganha uma seção curta de Comunicação que aponta para ele. Nenhuma Rule do Cursor e nenhuma Skill por enquanto.

## Justificativa

- A política tem uma parte sempre ativa (tom, explicação de termos, correções leves) e uma parte sob demanda (templates). O `AGENTS.md` já cobre a parte sempre ativa; um doc linkado cobre a parte sob demanda.
- O `AGENTS.md` e docs em Markdown funcionam entre ferramentas (Cursor, Claude Code, Codex); rules `.mdc` e skills são específicas de cada ferramenta.
- Um humano lê o mesmo arquivo que o agente segue: a política também é material de treinamento.

## Trade-offs e alternativas

- **Rule do Cursor (`.cursor/rules/*.mdc`, sempre aplicada):** garantida no contexto, mas duplica o que o `AGENTS.md` faz e consome contexto em toda requisição, inclusive em trabalho fora da simulação.
- **Skill (`corporate-communication`):** carregada só quando relevante, o que economiza contexto. Mas um agente pode não carregá-la durante uma interação casual, e a política deve estar sempre ativa.
- **Custo aceito:** um agente precisa seguir um link para ver os templates. Se os agentes pularem isso repetidamente, revisitar (candidato a `/correct`).

## Impacto

Funcionalidades futuras da simulação (reuniões no Bootstrap 02, communication evals) referenciam `docs/process/COMMUNICATION.md` em vez de redefinir formatos. Os registros de decisão agora usam o formato unificado em `brain/index.md`.
