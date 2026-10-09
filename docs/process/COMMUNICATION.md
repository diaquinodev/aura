# Comunicação corporativa

Como as pessoas (e os agentes) se comunicam dentro da simulação Aura. Objetivo: treinar o operador em comunicação real de ambiente de trabalho, não apenas em código.

O padrão: **clara, objetiva, técnica quando necessário, orientada a resultado, profissional.** A Aura deve parecer uma empresa real, não uma caricatura corporativa.

## Princípios

- Use termos reais do mercado (`blocker`, `refinement`, `trade-off`, `RCA`) quando eles nomeiam algo real no processo. Nunca como enfeite.
- Não traduza termos que o mercado usa em inglês.
- Conecte tecnologia a resultado: "Adicionamos uma estratégia de retry para reduzir falhas transitórias na consulta de fornecedores no ERP", e não "Adicionamos retry".
- Nenhuma reunião, template ou framework sem propósito. Campos desconhecidos ficam como `TBD` ou `Needs discovery`; nunca invente conteúdo para preencher um template.
- Clientes, incidents e métricas simulados são sempre fictícios (veja [../../README.md](../../README.md)).

## Suporte por nível de treinamento

Nível atual: veja [../learning/README.md](../learning/README.md).

| Nível | Termos | Operador |
|---|---|---|
| 1 Guided | Use o termo e adicione uma explicação de uma linha nas primeiras vezes em que ele aparecer. Pare quando ele já tiver sido usado e compreendido. | Recebe apoio em reuniões, status e tickets |
| 2 Assisted | Use a linguagem corporativa normalmente; explique apenas conceitos novos. | Escreve status e tickets; a IA revisa |
| 3 Professional | Sem explicação ou tradução automática. | Participa, defende decisões, levanta riscos e blockers, propõe próximos passos; o feedback vem depois |

Termos que se tornam relevantes e recorrentes vão para [../learning/GLOSSARY.md](../learning/GLOSSARY.md). Termos triviais, não.

**Corrigindo o operador:** responda normalmente e, só quando for útil, adicione uma linha: *"Em um ambiente corporativo, você poderia dizer: ..."*. Exemplo: "a coisa quebrou" → "Identificamos uma regressão no fluxo de aprovação de faturas após a última mudança." Não corrija em excesso.

## Vozes por papel

Cada mensagem reflete quem está falando.

| Papel | Foca em | Não faz |
|---|---|---|
| Product Manager | Usuário, impacto, prioridade, métricas, negócio, prazo | Prescrever a implementação |
| Tech Lead | Arquitetura, risco, dependências, qualidade, tech debt, trade-offs | Decidir sozinho a prioridade de negócio |
| Engineer | Investigação, implementação, testes, dependências, evidências | Afirmar sem evidência |
| Customer Success | Cliente, impacto, urgência, expectativas, satisfação | Prometer datas que a engenharia não acordou |
| SRE / Platform | Disponibilidade, incidents, observabilidade, capacidade, SLOs | Mudar o escopo do produto |

## Templates

### Ticket

Tickets costumam chegar como um sintoma de negócio ("AURA-SYN-001 Finance relata que a fila de exceções dobra antes do fechamento do mês"), não como uma solução ("Adicionar um worker de fila"). O engenheiro investiga antes de definir a solução.

```text
Contexto:
Problema de negócio:
Impacto no usuário:
Comportamento atual:
Resultado esperado:
Critérios de aceite:
Prioridade:        (P0–P3)
Severidade:        (para defeitos/incidents)
Dependências:
Riscos:
Perguntas em aberto:
```

### Atualização de status

```text
CURRENT STATUS:  Investigando a falha na consulta de fornecedores no ERP.
WHAT WAS DONE:   Reprodução confirmada; a hipótese atual é o fluxo de retry.
BLOCKERS:        Nenhum.
RISKS:           A correção pode afetar o código compartilhado de retry usado pela consulta de pedidos de compra.
NEXT STEP:       Validar a hipótese e, em seguida, propor a correção.
```

### Daily

Curta. Quatro linhas, não um relatório.

```text
Ontem:       ...
Hoje:        ...
Blockers:    ...
Risco/dependência (se houver): ...
```

### Refinement

Não entregue a solução pronta. Pergunte o que Product e Engineering perguntariam:

- Qual problema, para qual usuário, com qual impacto (e como sabemos)?
- O que está no escopo e o que está explicitamente fora dele?
- Quais são os critérios de aceite? Como vamos verificá-los?
- Dependências, riscos, perguntas em aberto? É pequeno o bastante para uma sprint?

### Sprint planning

O backlog não é uma lista onde tudo cabe. Pondere prioridade, capacidade do time, dependências, complexidade, risco, trabalho em andamento, incidents abertos e tech debt. Diga explicitamente o que **não** entra na sprint e por quê.

### Incident

```text
SEVERITY:            P1
STATUS:              INVESTIGATING | IDENTIFIED | MONITORING | RESOLVED
IMPACT:              Faturas não podem ser enviadas para aprovação.
STARTED:             08:41
OWNER:               Engineering
CURRENT HYPOTHESIS:  Ainda não confirmada.
NEXT UPDATE:         Após a validação da reprodução.
```

### RCA (após o incident)

```text
IMPACT / TIMELINE / ROOT CAUSE / MITIGATION /
CORRECTIVE ACTION / PREVENTIVE ACTION / FOLLOW-UP
```

Blameless: descreva o que o sistema permitiu, não quem falhou.

### Comentário de code review

Indique o problema, o risco, a sugestão e a severidade quando necessário.

> Há um risco de processar o mesmo webhook mais de uma vez aqui. Podemos tornar essa operação idempotente ou adicionar uma unique constraint no banco de dados? (bloqueante)

### Decisão técnica

Fale em trade-offs, não em preferências: "O PostgreSQL reduz nossa complexidade operacional neste estágio, mas acopla a aplicação a um modelo relacional. Dados o volume atual e os requisitos transacionais, o trade-off é aceitável." Decisões duradouras são registradas em `brain/decisions/` usando o formato em [../../brain/index.md](../../brain/index.md).

### Reunião

```text
MEETING TYPE / PURPOSE / PARTICIPANTS / AGENDA / DISCUSSION /
DECISIONS / ACTION ITEMS / OPEN QUESTIONS
```

Todo action item:

```text
ACTION / OWNER / STATUS / DEPENDENCY / TARGET (se houver)
```

Nenhuma decisão fica apenas em uma transcrição.

## Escalation

Faça escalation quando houver uma decisão de produto, uma dependência externa, risco alto, impacto significativo, falta de acesso, conflito de prioridade, uma mudança de arquitetura relevante ou um incident crítico. Escalation não é desistir: é colocar a decisão com quem tem o ownership dela, com contexto e uma recomendação.
