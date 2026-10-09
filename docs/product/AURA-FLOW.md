# Aura Flow (codinome)

> **STATUS: SUPERSEDED**
>
> Este documento pertence ao posicionamento anterior da AURA, vertical de saúde. A direção atual de produto é o Aura Ops — Enterprise Agentic Automation Platform.
>
> Fonte da verdade atual: [docs/product/AURA-OPS.md](AURA-OPS.md). Por que mudou: decisão 0007.

Status: **conceito** (na época). Tudo abaixo é hipótese, salvo indicação em contrário. Nenhuma arquitetura técnica é definida aqui, de propósito.

## Problema (hipótese)

Negócios premium baseados em agendamento perdem receita entre o primeiro contato e o atendimento realizado: respostas lentas perdem leads, a falta de confirmações causa no-shows e a recepção repete as mesmas mensagens o dia inteiro.

## Usuários (hipótese)

| Persona | Papel | Quer |
|---|---|---|
| Dono/gestor | Comprador | Agenda mais cheia, menos no-shows, visibilidade do funil |
| Recepção | Usuário do dia a dia | Menos mensagens repetitivas, menos erros de agendamento |
| Profissional | Usuário indireto | Agenda precisa |
| Cliente final | Recebe as mensagens | Respostas rápidas, agendamento e reagendamento fáceis |

## Jornada

```text
lead → qualificação → serviço → profissional → disponibilidade
     → agendamento → confirmação → lembrete → comparecimento → follow-up → analytics
```

| Etapa | O que o Aura Flow faria (hipótese) |
|---|---|
| Lead | Capturar um contato recebido por um canal |
| Qualificação | Perguntar o que a pessoa deseja (administrativo/comercial, nunca clínico) |
| Serviço | Mapear o pedido para um serviço do catálogo do negócio |
| Profissional | Escolher quem pode realizá-lo |
| Disponibilidade | Encontrar horários livres |
| Agendamento | Reservar o horário |
| Confirmação | Obter confirmação explícita do cliente |
| Lembrete | Lembrar antes do atendimento |
| Comparecimento | Registrar compareceu / no-show / cancelado |
| Follow-up | Mensagem pós-atendimento, sugestão de novo agendamento |
| Analytics | Números de funil e de no-show para o dono |

## Objetivos (hipótese)

- Reduzir no-shows.
- Reduzir o tempo até a primeira resposta aos leads.
- Reduzir mensagens manuais da recepção.
- Dar ao dono uma visão do funil.

## Fora de escopo (decisão)

- Nenhum diagnóstico médico, triagem ou orientação clínica.
- Nenhum prontuário médico ou dado clínico.
- Nenhum pagamento na primeira versão.
- Nenhum dado real de cliente até que um piloto seja explicitamente aprovado.

## Métricas hipotéticas

Estas são métricas candidatas. Qualquer valor produzido antes de um piloto real é **simulado**.

| Métrica | Definição |
|---|---|
| Taxa de no-show | No-shows / atendimentos confirmados |
| Taxa de lead para agendamento | Agendamentos / leads |
| Tempo até a primeira resposta | Tempo mediano entre o lead e a primeira resposta |
| Mensagens manuais por agendamento | Mensagens enviadas pela equipe / agendamentos |

## Riscos

- Mensagens erradas ou duplicadas prejudicam a relação do cliente com seus próprios clientes.
- Clientes podem escrever informações clínicas espontaneamente; o produto não deve armazená-las nem agir sobre elas.
- Provedores de canal (WhatsApp) restringem mensagens automatizadas e cobram por conversa.
- Agendamento duplicado (double booking) se a disponibilidade não for a única fonte da verdade.

## Integrações futuras (não iniciadas)

- Google Calendar (disponibilidade e agendamento), Stage 5.
- WhatsApp (canal de mensagens), Stage 5.
- Outras (Instagram, formulário web, software de clínica existente): desconhecido.
