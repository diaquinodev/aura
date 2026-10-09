# Aura Ops (codinome)

Status: **conceito**. Nada neste documento está implementado. As afirmações são hipóteses, salvo indicação em contrário.

> Plataforma de automação inteligente para processos operacionais corporativos, combinando agentes de IA, APIs, dados, regras de negócio e aprovação humana.

## Estratégia de escopo (decisão)

O Aura Ops poderá, no futuro, cobrir Finance Operations, Procurement, Customer Operations, Compliance, Sales Operations e Backoffice. **Um workflow real primeiro:** o primeiro e único domínio, até que seu workflow esteja completo de ponta a ponta, é **Finance & Operations → Accounts Payable**.

## Problema (hipótese)

Empresas recebem faturas e solicitações de pagamento que precisam ser recebidas, interpretadas, validadas, conferidas contra sistemas, verificadas contra regras, investigadas quando divergem, aprovadas, registradas e auditadas. Em muitas organizações, a maior parte disso é manual: analistas redigitam dados, correm atrás de divergências por e-mail e as aprovações acontecem fora de qualquer audit trail. O custo hipotético é tempo de analista, pagamentos em atraso (multas, perda de descontos por pagamento antecipado), pagamentos duplicados e controles fracos.

## Usuários

Definidos como personas sintéticas em [../../simulation/AURA-SYN-001.md](../../simulation/AURA-SYN-001.md).

## Workflow de referência: Accounts Payable inteligente

Apenas conceitual; nenhuma etapa está implementada. A coluna **Tipo** aplica a fronteira definida em [../architecture/README.md](../architecture/README.md).

| # | Etapa | O que acontece | Tipo |
|---|---|---|---|
| 1 | Documento / solicitação | Chega uma fatura ou solicitação de pagamento | — |
| 2 | Entrada (intake) | Registrar, atribuir um ID, detectar o canal | Determinístico |
| 3 | Parsing do documento | Extrair fornecedor, valores, itens e datas de um documento não estruturado | Probabilístico |
| 4 | Validação de dados | Campos obrigatórios, formatos, dígito verificador do identificador fiscal, totais que fecham | Determinístico |
| 5 | Consulta ao ERP / banco de dados | Localizar fornecedor, pedido de compra (PO), recebimento (goods receipt) | Determinístico |
| 6 | Regras de negócio | Limites de aprovação, status do fornecedor, condições de pagamento | Determinístico |
| 7 | 3-way match | PO vs recebimento vs fatura: quantidades e preços dentro da tolerância | Determinístico |
| 8 | Detecção de divergências | Sinalizar divergências, duplicidades e documentos ausentes como exceptions | Determinístico |
| 9 | Investigação por IA | Reunir contexto sobre uma exception (histórico, e-mails, casos similares) e explicar a causa provável | Probabilístico |
| 10 | Recomendação | Propor aprovar / rejeitar / solicitar correção, com evidências | Probabilístico |
| 11 | Aprovação humana | Uma pessoa autorizada decide; a política define quem | Humano |
| 12 | Ação de negócio | Registrar no ERP, agendar pagamento, notificar o fornecedor | Determinístico |
| 13 | Log de auditoria | Registro imutável das entradas, resultados das regras, saídas da IA, da decisão e de quem a tomou | Determinístico |
| 14 | Observabilidade | Traces, latência, custo e taxas de erro por etapa | Determinístico |
| 15 | Avaliação | Medir acurácia do parsing, qualidade das recomendações e tempo de tratamento de exceptions | Harness determinístico sobre saídas probabilísticas |

## Objetivos (hipótese)

- Reduzir o tempo de tratamento manual por fatura.
- Resolver exceptions mais rápido, com evidências anexadas.
- Zero pagamentos duplicados.
- Toda ação financeira é rastreável até uma decisão humana ou uma política aprovada.

## Fora de escopo (decisão)

- Agentes não executam ações financeiras de forma autônoma (veja [../architecture/README.md](../architecture/README.md)).
- Nenhuma conexão real com ERP, banco ou fornecedor até a prontidão para piloto (Stage 10).
- Nenhum outro domínio até que Accounts Payable esteja completo.
- Nenhum dado real de empresa, fatura ou pessoa.

## Métricas hipotéticas

Qualquer valor produzido antes de um piloto real é **simulado**.

| Métrica | Definição |
|---|---|
| Taxa touchless | Faturas processadas sem nenhuma etapa manual / total de faturas |
| Tempo de resolução de exceptions | Tempo mediano entre a sinalização da exception e a decisão |
| Acurácia do parsing | Campos extraídos corretamente / campos avaliados (conjunto de eval) |
| Concordância com recomendações | Recomendações da IA aceitas pelos aprovadores / recomendações |
| Pagamentos duplicados | Contagem; meta zero |

## Riscos

- Uma extração ou recomendação incorreta da IA leva a um pagamento incorreto. Mitigação: validação determinística e aprovação humana antes de qualquer ação.
- Automação excessiva corrói os controles financeiros e a segregação de funções.
- ERPs reais variam muito; um ERP simulado pode esconder a complexidade de integração.
- O custo e a latência de LLM por fatura podem superar o valor gerado em volumes baixos. **UNKNOWN** até ser medido.
