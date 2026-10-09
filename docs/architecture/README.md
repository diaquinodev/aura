# Arquitetura

Status: **princípios + esqueleto do serviço**. Só a API FastAPI com `GET /health` existe; o restante está PLANNED. O design técnico detalhado chega ao longo do Stage 1 e dos stages seguintes.

## Visão conceitual

O diagrama de arquitetura vive em um único lugar, o [README](../../README.md), para não divergir. Ele marca o que está implementado e o que está planejado.

## Vocabulário de status

Usado em toda a documentação para capacidades e componentes.

| Status | Significado |
|---|---|
| PLANNED | Pretendido; nada construído |
| IN DEVELOPMENT | Trabalho iniciado; ainda não utilizável |
| IMPLEMENTED | Construído e executável |
| VERIFIED | Implementado e comprovado por teste, eval ou evidência reproduzível |

## Princípio 1: deterministic first, IA onde existe incerteza

| Determinístico: código, SQL, schema, constraints, regras, testes | Probabilístico: pode justificar IA |
|---|---|
| `invoice_total == expected_total` | Interpretar um documento não estruturado |
| `purchase_order_exists` | Classificação semântica (que tipo de solicitação é esta?) |
| Detecção de documentos duplicados | Recuperar contexto relevante |
| Transições de status e validação | Investigação assistida de uma exception |
| Limites de aprovação | Resumos e recomendações |
| 3-way match dentro da tolerância | Interface em linguagem natural |

Se uma etapa pode ser expressa como regra, ela é uma regra. Um LLM, agente, servidor MCP ou pipeline de RAG só é introduzido onde lida com incerteza real, e essa necessidade é registrada como decisão.

## Princípio 2: human-in-the-loop para ações de negócio

```text
Recomendação do agente → Política → Aprovação humana → Ação
```

- Agentes **recomendam**; eles não executam ações financeiras.
- A **política** (determinística) decide quem precisa aprovar, com base em valor, fornecedor e risco.
- A autonomia só aumenta com evidências (evals, histórico de auditoria), por tipo de ação, registrada como decisão.

## Princípio 3: tudo auditável

Cada ação de negócio registra suas entradas, os resultados das regras, as saídas da IA (com modelo e versão), a decisão, quem a tomou e quando. Se não está no log de auditoria, não aconteceu.

## Princípio 4: nenhuma tecnologia sem problema

Nenhuma tecnologia entra na AURA por ser popular. RAG, MCP, frameworks de agentes, Redis, bancos de dados vetoriais, orquestração, Kubernetes, Kafka ou uma plataforma de observabilidade precisam de:

```text
PROBLEMA → REQUISITO → ALTERNATIVAS → DECISÃO → IMPLEMENTAÇÃO → EVIDÊNCIA
```

registrado em `brain/decisions/`. Sem um problema concreto, a tecnologia é rejeitada ou adiada.

## Princípio 5: agentes por último, e avaliados

```text
Regras de negócio → Motor determinístico → APIs → Dados → Casos de falha → Assistência de agentes
```

Nenhum agente antes de um problema que precise de um. Agentes são **avaliados, não apenas demonstrados**: sucesso na tarefa, erros de ferramenta, alucinações, escalonamentos para humanos, latência, tokens, custo, falhas de segurança. Cada métrica só é adicionada quando pode de fato ser medida.

## Simulator (PLANNED)

O simulador é mais do que material de treinamento. Ele também é:

- **cenários reproduzíveis**: o mesmo cenário roda contra diferentes versões da solução;
- **eval harness**: os resultados são comparados entre versões (Cenário 001 → versão A → resultado; Cenário 001 → versão B → resultado);
- **gerador de incidentes**: falhas injetadas de propósito, de forma reproduzível.

Organizações sintéticas como `simulation/AURA-SYN-001.md` são sua primeira entrada. Todos os seus resultados são SYNTHETIC.
