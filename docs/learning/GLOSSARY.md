# Glossário

Apenas termos relevantes e recorrentes já usados no projeto. Cresce junto com o projeto. Formato: termo, explicação simples, exemplo na Aura, exemplo numa empresa real.

## Engenharia

**Repository**
Uma pasta cujo histórico completo de alterações é rastreado pelo Git.
*Na Aura:* `d:\CURSOR-AGENTE`, depois que o `git init` for executado.
*Numa empresa real:* cada produto ou serviço costuma ter seu próprio repositório no GitHub/GitLab.

**Branch**
Uma linha paralela de alterações, para que o trabalho aconteça sem mexer na versão principal.
*Na Aura:* cada Bootstrap ou ticket terá sua própria branch assim que o Git existir.
*Numa empresa real:* todo ticket ganha uma branch como `feature/AUR-12-booking`; a `main` continua pronta para deploy.

**Commit**
Um snapshot salvo de alterações, com uma mensagem explicando o porquê.
*Na Aura:* o primeiro commit vai conter a fundação do Stage 0.
*Numa empresa real:* os revisores leem as mensagens de commit para entender a intenção; meses depois, o `git blame` aponta de volta para elas.

**Pull Request (PR)**
Uma solicitação para fazer merge de uma branch na `main`, onde outras pessoas revisam a alteração.
*Na Aura:* ainda não usado; planejado para quando existirem um remote e um workflow de branches.
*Numa empresa real:* nenhum código chega à produção sem um PR aprovado e a CI passando.

**CI (Continuous Integration)**
Verificações automatizadas (testes, linters) executadas a cada alteração.
*Na Aura:* o `tools/check_docs.py` é a primeira verificação que vai rodar na CI (Stage 1).
*Numa empresa real:* uma CI vermelha bloqueia o merge, então código quebrado não chega à `main`.

**Tenant**
Uma organização cliente num sistema compartilhado (multi-tenant), isolada das demais.
*Na Aura:* cada organização sintética (a primeira: AURA-SYN-001) será um tenant.
*Numa empresa real:* a Clínica A nunca pode ver os agendamentos da Clínica B, mesmo que ambas usem o mesmo banco de dados.

**Observability**
A capacidade de entender o que um sistema em execução está fazendo a partir de seus logs, métricas e traces.
*Na Aura:* planejado para o Stage 7.
*Numa empresa real:* quando um agendamento falha, um trace mostra qual etapa e qual chamada externa falharam.

**Proof of work**
Evidência que permite a outra pessoa verificar que o trabalho foi feito e compreendido: código, testes, PRs, execuções de CI, métricas, case studies.
*Na Aura:* a partir do Stage 1, um marco sem isso não está concluído.
*Numa empresa real:* um pedido de promoção cita PRs entregues e impacto medido, não "familiarizado com Kafka".

**Baseline**
O valor medido de algo antes de uma alteração, para que a alteração possa ser comparada com ele.
*Na Aura:* contagem de duplicatas antes e depois de uma correção, rotulada como SYNTHETIC.
*Numa empresa real:* "a latência p95 era de 800 ms antes do cache; 300 ms depois."

## Agentes de IA

**Agent**
Um modelo de IA capaz de executar ações com ferramentas (ler arquivos, rodar comandos), não apenas responder.
*Na Aura:* o agente do Cursor que escreveu o Stage 0 seguindo o `AGENTS.md`.
*Numa empresa real:* um agente abre um PR corrigindo um erro de lint; uma pessoa o revisa.

**Skill**
Um procedimento escrito e reutilizável que um agente carrega para um tipo específico de tarefa.
*Na Aura:* skills do pstack como `/how` e `/reflect`, usadas a partir do plugin.
*Numa empresa real:* uma skill de "release" diz ao agente exatamente quais etapas e verificações uma release exige.

**Rule**
Instruções persistentes aplicadas automaticamente a um agente.
*Na Aura:* `AGENTS.md`.
*Numa empresa real:* "nunca faça commit de secrets" fica numa rule, para que ninguém precise repetir.

**Hook**
Código executado automaticamente quando um evento específico acontece.
*Na Aura:* nenhum ainda.
*Numa empresa real:* um hook de pre-commit bloqueia um commit que contém uma API key.

**MCP (Model Context Protocol)**
Um padrão para conectar um agente de IA a ferramentas e dados externos.
*Na Aura:* candidato para conectar o Jira no Bootstrap 02.
*Numa empresa real:* o agente lê um ticket do Jira por meio de um servidor MCP, em vez de alguém copiar e colar.

**Eval**
Um teste repetível que mede o quão bem um sistema de IA (ou o resultado de uma pessoa) executa uma tarefa.
*Na Aura:* evals de comunicação propostas (`brain/insights/communication-evals.md`).
*Numa empresa real:* 200 mensagens de clientes de amostra passam pelo agente; a proporção de agendamentos corretos é acompanhada a cada release.

## Agile e entrega

**Stakeholder**
Qualquer pessoa afetada por um trabalho ou com influência sobre ele.
*Na Aura:* o Finance Manager da AURA-SYN-001 (comprador), os Finance Analysts (usuários), Compliance (pode bloquear) e o operador atuando como Product.
*Numa empresa real:* antes de mudar o fluxo de agendamento, o PM se alinha com Vendas, Suporte e Engenharia.

**Backlog**
A lista ordenada do trabalho ainda não feito.
*Na Aura:* será criado no Jira no Bootstrap 02.
*Numa empresa real:* o product manager mantém os itens de maior valor no topo.

**Epic**
Um grande bloco de trabalho dividido em várias stories.
*Na Aura:* "3-way match" poderia ser um epic.
*Numa empresa real:* "Lembretes por WhatsApp" é um epic; "enviar lembrete 24h antes" é uma story.

**Story**
Uma pequena entrega de valor visível ao usuário, com critérios de aceite.
*Na Aura:* "Como recepção, quero confirmação automática para não ter que mandar mensagem para cada cliente."
*Numa empresa real:* as stories são dimensionadas para caber em uma sprint.

**Acceptance criteria**
As condições que precisam ser verdadeiras para uma story ser considerada concluída, escritas antes da implementação.
*Na Aura:* "Uma fatura cujo total difere do PO acima da tolerância é sinalizada como exception e nunca é aprovada automaticamente."
*Numa empresa real:* QA e o PM verificam os critérios antes de aceitar a entrega.

**Refinement**
Uma sessão em que o time esclarece escopo, requisitos e critérios de aceite antes de um ticket ir para implementação.
*Na Aura:* os tickets vão começar como sintomas de negócio e ser refinados antes que alguém proponha uma solução.
*Numa empresa real:* um ticket não está "pronto" para a sprint até passar por refinement.

**Sprint**
Um intervalo de tempo fixo (geralmente 2 semanas) em que o time se compromete com um conjunto de itens do backlog.
*Na Aura:* apresentada no Bootstrap 02.
*Numa empresa real:* sprint planning no início, review e retrospectiva no final.

**Blocker**
Algo que impede uma tarefa de avançar até que outra pessoa aja.
*Na Aura:* "Bloqueado: o Git não está inicializado, então o workflow de branches não pode começar."
*Numa empresa real:* os blockers são levantados na daily para que alguém os remova no mesmo dia.

**Trade-off**
Ganhar uma propriedade aceitando um custo em outra; a base de toda decisão técnica.
*Na Aura:* a decisão 0006 troca contexto garantido (uma Rule) por portabilidade e menor custo de contexto (um doc linkado).
*Numa empresa real:* "O cache reduz a latência, mas corre o risco de mostrar disponibilidade desatualizada."

**Escalation**
Levar uma decisão ou um problema a quem é dono dele, com contexto e uma recomendação.
*Na Aura:* um engenheiro escala para Product quando uma correção muda o que os clientes veem.
*Numa empresa real:* um engenheiro de plantão escala um P1 para o incident commander após 15 minutos sem mitigação.

## Finance & Operations

**Accounts Payable (AP)**
O processo de receber, conferir, aprovar e pagar o que uma empresa deve aos seus fornecedores.
*Na Aura:* o primeiro e único domínio do Aura Ops.
*Numa empresa real:* um time de AP processa milhares de faturas de fornecedores por mês e as fecha antes do fim do mês.

**3-way match**
Um controle que compara o pedido de compra, o recebimento da mercadoria e a fatura antes do pagamento; uma forma de conciliação.
*Na Aura:* etapa 7 do workflow de referência, totalmente determinística.
*Numa empresa real:* se a fatura cobra 100 unidades, mas só 90 foram recebidas, o pagamento fica retido.

**Exception**
Um caso que falha numa verificação automatizada e precisa de investigação ou de uma decisão humana.
*Na Aura:* onde a investigação por IA agrega valor (etapa 9).
*Numa empresa real:* os analistas de AP passam a maior parte do dia trabalhando a fila de exceptions, não o caminho feliz.

**Human-in-the-loop (HITL)**
Um design em que uma pessoa revisa ou aprova antes que uma decisão automatizada tenha efeito.
*Na Aura:* os agentes recomendam; uma pessoa autorizada aprova toda ação financeira.
*Numa empresa real:* uma IA sinaliza um pagamento suspeito; um controller confirma antes de ele ser bloqueado.

**SLA (Service Level Agreement)**
Uma meta assumida para um serviço, como tempo de resposta ou de processamento.
*Na Aura:* o Finance Manager da AURA-SYN-001 acompanha o SLA de pagamento.
*Numa empresa real:* "95% das faturas aprovadas pagas dentro do prazo do fornecedor."

**Audit trail**
Um registro completo e resistente a adulteração de quem fez o quê, quando e com base em quais dados.
*Na Aura:* etapa 13; inclui as saídas da IA e a versão do modelo que as produziu.
*Numa empresa real:* auditores externos fazem amostragem de pagamentos e pedem o trail completo de cada um.

## Operações

**Incident**
Um evento não planejado que degrada o serviço para os usuários.
*Na Aura:* simulado no Stage 8; sempre rotulado como simulado.
*Numa empresa real:* os lembretes param de ser enviados; alguém é acionado, corrige o problema e escreve um postmortem.

**Severity**
O quão grave é o impacto de um incidente, geralmente de P0/P1 (crítico) a P3/P4 (menor). Define a velocidade de resposta e quem é envolvido.
*Na Aura:* "P1: as faturas não podem ser enviadas para aprovação."
*Numa empresa real:* um P1 aciona o plantão imediatamente; um P3 espera o horário comercial.

**RCA (Root Cause Analysis)**
Uma análise escrita e sem culpados (blameless) após um incidente: impacto, linha do tempo, causa raiz e ações para evitar recorrência.
*Na Aura:* template em `docs/process/COMMUNICATION.md`.
*Numa empresa real:* as RCAs são revisadas numa reunião de postmortem e seus itens de ação acompanhados até a conclusão.
