# AURA-SYN-001 — Synthetic Finance Enterprise

```text
TYPE:          SYNTHETIC ORGANIZATION
ID:            AURA-SYN-001
DISPLAY NAME:  Synthetic Finance Enterprise
```

Esta organização é fictícia e não representa nenhuma empresa real. Convenção de identificadores: decisão 0008.

## Perfil

- Empresa de médio a grande porte, com várias unidades de negócio.
- Departamentos relevantes para a Aura: Finanças, Compras, Operações, Atendimento ao Cliente, Compliance.
- Processa um alto volume mensal de faturas de fornecedores; o volume exato é **TBD** até a criação dos datasets sintéticos (Stage 3).
- Usa um ERP (simulado no Stage 5) como sistema de registro de fornecedores, pedidos de compra e pagamentos.

## Personas

Nenhum agente. Estes são stakeholders de negócio que geram solicitações, decisões e feedback na simulação.

### Finance Analyst
- **Objetivos:** processar faturas corretamente e no prazo; zerar a fila de exceptions.
- **Dores:** redigitar dados, correr atrás de divergências por e-mail, backlog de fechamento do mês.
- **Conhecimento técnico:** planilhas, telas do ERP; não programa.
- **Autoridade de decisão:** aprova dentro de um limite baixo; escala acima dele.
- **Pedidos típicos:** "Por que esta fatura está travada?" / "O sistema consegue pegar duplicidades?"

### Finance Manager
- **Objetivos:** cumprir os SLAs de pagamento, controlar o risco, reportar KPIs à liderança.
- **Dores:** nenhuma visibilidade da fila; multas por atraso de pagamento; apontamentos de auditoria.
- **Conhecimento técnico:** dashboards de business intelligence.
- **Autoridade de decisão:** aprovações de alto valor; define a política de aprovação junto com Compliance.
- **Pedidos típicos:** "Qual é a nossa taxa de exceptions este mês?" / "Quem aprovou este pagamento?"

### Procurement Analyst
- **Objetivos:** pedidos de compra precisos e relações saudáveis com fornecedores.
- **Dores:** faturas que não batem com o PO; fornecedores perguntando sobre o status do pagamento.
- **Conhecimento técnico:** módulo de compras do ERP.
- **Autoridade de decisão:** altera POs; confirma o recebimento (goods receipt).
- **Pedidos típicos:** "O fornecedor diz que faturou o preço combinado; por que a divergência?"

### Operations Manager
- **Objetivos:** um processo de ponta a ponta previsível e mensurável.
- **Dores:** passagens de bastão entre Finanças e Compras; nenhuma visão de um dono único do processo.
- **Conhecimento técnico:** mapeamento de processos, KPIs.
- **Autoridade de decisão:** mudanças de processo e prioridades entre os times.
- **Pedidos típicos:** "Onde está o gargalo no processamento de faturas?"

### Engineering / Platform (lado da AURA)
- **Objetivos:** um Aura Ops confiável, seguro e observável.
- **Dores:** requisitos pouco claros, integrações instáveis, qualidade da IA não medida.
- **Conhecimento técnico:** alto.
- **Autoridade de decisão:** design técnico e release; não define política de negócio.
- **Pedidos típicos:** "Quais são os critérios de aceite?" / "Qual é o volume esperado?"

### Compliance
- **Objetivos:** controles efetivos, segregação de funções, audit trail completo.
- **Dores:** aprovações fora do sistema; decisões da IA que ninguém consegue explicar.
- **Conhecimento técnico:** frameworks de controles; pouca profundidade técnica.
- **Autoridade de decisão:** pode bloquear um release ou uma automação que enfraqueça os controles.
- **Pedidos típicos:** "Mostre todas as ações que a IA tomou nesta fatura e quem as aprovou."
