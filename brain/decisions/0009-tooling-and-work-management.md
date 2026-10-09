# 0009 Tooling Python e gestão do trabalho

**Status:** Aceita · **Owner:** Operador · **Data:** 2026-10-09 (Bootstrap 02 kickoff)

## Contexto

O Stage 1 precisa de um ambiente Python, uma definição de dependências, um lugar para tickets e sprints, e um remoto para PRs e CI.

## Decisão

- `venv` + `pip` + `pyproject.toml` (src layout, pacote `aura_ops`).
- GitHub Issues para tickets, Milestones como sprints. Board do GitHub Projects adiado: o token do `gh` não tem o scope `project`.
- Repositório privado no GitHub `diaquinodev/aura`; tornado público quando houver proof of work que valha a pena mostrar.
- GitHub Actions para CI. Jira adiado até quando acrescentar algo que o GitHub não oferece.

## Justificativa

Tudo já está instalado ou autenticado: zero ferramentas novas antes da primeira linha de código. Issues, PRs e CI em um só lugar ligam tickets a evidências automaticamente (`Closes #N`).

## Trade-offs e alternativas

- `uv`: mais rápido e tem lockfile, mas precisa ser instalado; revisitar se a reprodutibilidade virar um problema.
- Jira: mais próximo de muitas empresas, mas precisa de uma conta e de uma integração para se ligar aos PRs.
- Custo aceito: sem lockfile, então o CI pode resolver versões de dependências mais novas que as locais.

## Impacto

`.venv/` continua ignorado pelo Git. O CI instala `pip install -e ".[dev]"` a partir do `pyproject.toml`.
