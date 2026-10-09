# 0008 Identificadores de tenants sintéticos

**Status:** Aceita · **Owner:** Operador · **Data:** 2026-10-09 (Stage 0 closeout) · **Resolve:** item do inbox "Nexa pode colidir com empresas reais"

## Contexto

O primeiro cliente sintético se chamava "Nexa Group". "Nexa" é usado por empresas reais, então um leitor do portfólio poderia confundir um cliente simulado com um real.

## Decisão

Organizações sintéticas usam um ID explicitamente sintético, `AURA-SYN-NNN`, mais um nome de exibição descritivo. A primeira é `AURA-SYN-001 — Synthetic Finance Enterprise` (`simulation/AURA-SYN-001.md`).

## Justificativa

Um ID não pode ser confundido com uma marca e não precisa de verificação de marca registrada. Também escala para futuros tenants e datasets.

## Trade-offs e alternativas

- Nome inventado com cara de marca: mais natural no role-play, mas cada nome precisa de uma verificação de colisão.
- Custo aceito: "AURA-SYN-001" soa menos natural em reuniões simuladas; o nome de exibição é usado no texto corrido.

## Impacto

Todas as referências a "Nexa Group" nos docs atuais foram substituídas. Os journals históricos mantêm o nome original.
