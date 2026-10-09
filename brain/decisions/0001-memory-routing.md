# 0001 Roteamento da memória

**Status:** Aceita, revisão do operador pendente · **Owner:** Operador · **Data:** 2026-10-08 (Bootstrap 01)

## Contexto

O projeto precisa poder ser retomado depois de meses, mas um transcript que só cresce é ilegível e inseguro como memória: o palpite de uma sessão viraria um "fato" permanente. O aprendizado do operador e o conhecimento do projeto têm públicos diferentes.

## Decisão

| Tipo | Vai para |
|---|---|
| Fato, decisão, gotcha, insight do projeto | `brain/` (índice, depois o arquivo específico) |
| Descoberta não validada | `brain/inbox/` |
| Aprendizado e evolução do operador | `docs/learning/` (journal, trilha, glossário) |
| Lição sobre como trabalhamos | `/reflect` (pstack), após verificar que é reutilizável |
| Erro que os agentes continuam repetindo | `/correct` (pstack) |

## Justificativa

Separar os públicos mantém cada arquivo pequeno e legível. O inbox impede que observações isoladas virem regras.

## Trade-offs e alternativas

- Um único `NOTES.md`: simples, mas mistura públicos e cresce sem limite.
- Guardar tudo via `/reflect`: transformaria fatos de sessão em edições de skill.

## Impacto

Todo fim de sessão precisa de uma etapa curta de roteamento (ver `docs/process/SESSION-LIFECYCLE.md`). O inbox precisa ser revisado, ou vira uma gaveta de bagunça.
