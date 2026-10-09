# 0004 Script de verificação de docs

**Status:** Aceita · **Owner:** Operador · **Data:** 2026-10-08 (Bootstrap 01)

## Contexto

Repositórios só de documentação se degradam com links quebrados e fatos que divergem entre arquivos. O nível de treinamento aparece em três arquivos (README, AGENTS, README de learning) porque cada público precisa dele no próprio lugar.

## Decisão

`tools/check_docs.py` (apenas biblioteca padrão do Python) falha quando um link Markdown relativo aponta para um arquivo inexistente ou quando as linhas `TRAINING_LEVEL = N` divergem.

## Justificativa

Enforcement determinístico em vez de lembretes. Nenhuma dependência adicionada; pode rodar em CI depois, sem alterações.

## Trade-offs e alternativas

- Um pacote de linter de Markdown: adiciona uma dependência para uma única verificação.
- Revisão manual: é esquecida.

## Impacto

Rode `python tools/check_docs.py` antes de encerrar uma sessão. Estenda o script apenas quando uma nova classe de erro de documentação realmente acontecer.
