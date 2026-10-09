# 0002 Criar diretórios no primeiro conteúdo

**Status:** Aceita, revisão do operador pendente · **Owner:** Operador · **Data:** 2026-10-08 (Bootstrap 01)

> **Atualização 2026-10-09 (Pivot 01):** `docs/architecture/` e `simulation/` foram criados assim que tiveram conteúdo real (princípios de arquitetura; a primeira organização sintética). `brain/investigations/` e `.github/` continuam adiados.

## Contexto

O brief do Bootstrap 01 propunha `simulation/`, `docs/architecture/`, `.github/README.md` e várias subpastas vazias em `brain/`. Nenhuma tinha conteúdo ainda.

## Decisão

Criar um diretório ou documento apenas quando ele receber conteúdo real. Adiados: `simulation/` (Stage 2), `docs/architecture/` (primeira decisão de arquitetura), `brain/investigations/` (primeira investigação), `.github/` (primeiro workflow, Stage 3). Sem arquivos `.gitkeep`.

## Justificativa

Estrutura vazia parece progresso, mas não diz nada a um engenheiro novo, e arquivos placeholder ficam desatualizados. Além disso, `.github/README.md` substituiria o README da raiz no GitHub (ver `brain/gotchas/github-readme-precedence.md`).

## Trade-offs e alternativas

Criar a árvore completa com `.gitkeep`: mostra a intenção, mas adiciona arquivos sem nenhuma informação.

## Impacto

Os locais planejados estão listados em `docs/README.md` e `brain/index.md` para que ninguém invente um lugar diferente para eles.
