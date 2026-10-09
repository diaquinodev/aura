# AURA (codinome)

Toda afirmação é classificada:

- **FACT**: verificado, ou verdadeiro por definição deste projeto.
- **HYPOTHESIS**: acreditamos, mas não foi validado.
- **DECISION**: escolhido por nós; pode ser revisto.
- **UNKNOWN**: questão em aberto.

O posicionamento anterior (SaaS vertical para clínicas, "Aura Studio") está registrado em `brain/decisions/0007-pivot-to-enterprise-agentic-automation.md`.

## Contexto

- **FACT**: AURA é uma empresa simulada. Não tem clientes, receita nem funcionários reais.
- **FACT**: "AURA" e "Aura Ops" são codinomes. A disponibilidade das marcas não foi verificada.
- **DECISION**: AURA é B2B: automação inteligente e auditável de processos corporativos por meio de agentes de IA, integrações, dados e workflows human-in-the-loop.
- **DECISION**: O primeiro domínio é Finance & Operations, especificamente Accounts Payable. Um workflow real primeiro.

## Mercado

- **HYPOTHESIS**: Empresas de médio e grande porte ainda executam boa parte do Accounts Payable manualmente, e a automação existente (OCR, RPA, módulos de ERP) cobre o caminho feliz, mas não as exceptions.
- **HYPOTHESIS**: A necessidade não atendida é o tratamento de exceptions com evidências e auditabilidade, não a simples extração de dados.
- **UNKNOWN**: Tamanho do mercado, região e qual porte de empresa obtém mais valor.

## Clientes-alvo

- **HYPOTHESIS**: Empresas de médio e grande porte com um time de Finanças dedicado, um ERP e alto volume mensal de faturas.
- **HYPOTHESIS**: O comprador é o Finance Manager ou o CFO; os usuários do dia a dia são analistas de Finanças e de Compras; Compliance pode bloquear a adoção.

## Problemas que pretendemos resolver

- **HYPOTHESIS**: Analistas gastam a maior parte do tempo redigitando dados e correndo atrás de divergências.
- **HYPOTHESIS**: Exceptions (divergência com o PO, recebimento ausente, duplicidades) causam atrasos de pagamento e multas.
- **HYPOTHESIS**: Aprovações e investigações acontecem fora do sistema, enfraquecendo o audit trail.

## Proposta de valor inicial

- **HYPOTHESIS**: "Menos intervenções manuais e resolução mais rápida de exceptions, com cada decisão explicada e auditada, e um humano aprovando toda ação financeira."

## Modelo de negócio

- **DECISION**: SaaS B2B.
- **HYPOTHESIS**: Assinatura por workflow, mais um componente de uso (documentos processados) para cobrir os custos de IA.
- **UNKNOWN**: Faixa de preço, e se o custo de IA por documento permite margem nos volumes do mid-market.

## Riscos

- **Correção financeira**: um erro de automação causa um pagamento incorreto. Mitigação: validação determinística e aprovação humana (`docs/architecture/README.md`).
- **Controles e compliance**: a automação não pode quebrar a segregação de funções nem o audit trail.
- **Integração**: ERPs reais são heterogêneos; o ERP simulado pode subestimar o esforço.
- **Concorrência**: existem fornecedores de ERP e especialistas em automação de AP. **UNKNOWN**: como a AURA se diferenciaria além do tratamento de exceptions.
- **Escopo**: o enquadramento como "plataforma" convida a construir muitos domínios ao mesmo tempo. Mitigação: um workflow primeiro.
- **Integridade**: a simulação nunca deve ser apresentada como realidade (veja [../../README.md](../../README.md)).

## Hipóteses não validadas a testar primeiro

1. O tratamento de exceptions, e não a extração, é o principal custo em Accounts Payable.
2. A investigação assistida por IA reduz de forma mensurável o tempo de resolução de exceptions.
3. Líderes de Finanças aceitam recomendações de IA se cada uma for explicada e auditada.
