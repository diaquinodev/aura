# AGENTS.md

## Missão

Construir a AURA de forma incremental, verificável e educativa. O operador é um profissional em treinamento; o trabalho precisa ensinar, não apenas entregar.

## Fontes de verdade

| Assunto | Arquivo canônico |
|---|---|
| Visão geral do projeto (só marcos) | [README.md](README.md) |
| Status operacional atual | [docs/status/CURRENT.md](docs/status/CURRENT.md) |
| Empresa, mercado, hipóteses | [docs/company/COMPANY.md](docs/company/COMPANY.md) |
| Escopo do produto e workflow de referência | [docs/product/AURA-OPS.md](docs/product/AURA-OPS.md) |
| Princípios de arquitetura | [docs/architecture/README.md](docs/architecture/README.md) |
| Organizações sintéticas e personas | [simulation/AURA-SYN-001.md](simulation/AURA-SYN-001.md) |
| Roadmap | [docs/product/ROADMAP.md](docs/product/ROADMAP.md) |
| Como o trabalho flui, ferramentas (pstack) | [docs/process/WORKING-MODEL.md](docs/process/WORKING-MODEL.md) |
| Comunicação corporativa, templates | [docs/process/COMMUNICATION.md](docs/process/COMMUNICATION.md) |
| Ritual de início e fim de sessão | [docs/process/SESSION-LIFECYCLE.md](docs/process/SESSION-LIFECYCLE.md) |
| Níveis de treinamento, trilha de aprendizado | [docs/learning/README.md](docs/learning/README.md) |
| Memória do projeto | [brain/index.md](brain/index.md) |

## Princípios de engenharia

- A menor solução correta.
- Evidência acima de suposições; testes acima de afirmações.
- Enforcement determinístico (scripts, testes, CI) acima de lembretes escritos.
- Nenhum agente, abstração ou diretório sem um problema concreto que ele resolva.
- Deterministic first, IA onde existe incerteza. Nenhuma tecnologia sem problema concreto ([docs/architecture/README.md](docs/architecture/README.md), princípio 4).
- A partir do Stage 1, documentação sozinha não é progresso. O que conta, formato de evidência, rótulos SYNTHETIC/REAL, padrões de PR e de commit: [docs/process/WORKING-MODEL.md](docs/process/WORKING-MODEL.md), "Progresso válido e proof of work".
- Agentes recomendam; humanos aprovam ações financeiras até que haja evidência para mais autonomia.
- Nunca descrever uma capability como IMPLEMENTED ou VERIFIED sem evidência.

## Modo de treinamento

`TRAINING_LEVEL = 1` (Guided). Em decisões relevantes, explique: o que estamos fazendo, por que uma empresa faria isso, o conceito, como aparece no trabalho real e a resposta curta de entrevista. Não transforme mudanças triviais em aula. Não suba o nível por conta própria; só o operador muda o nível.

## Comunicação

Todo o conteúdo é em português do Brasil: saída para o operador (chat, relatórios, explicações, status), documentação, issues e PRs. Termos que o mercado usa em inglês continuam em inglês. Código, nomes de arquivos e mensagens de commit (Conventional Commits) ficam em inglês (decisão 0005).

Sempre que um PR estiver aguardando review ou merge do operador, passe os links diretos: a página do PR, onde fica o botão de merge (`https://github.com/<owner>/<repo>/pull/<N>`), e o diff (`.../pull/<N>/files`).

Dentro da simulação, comunique como uma empresa de tecnologia real: termos reais quando nomeiam algo real, voz adequada a cada papel, orientação a resultado. Siga [docs/process/COMMUNICATION.md](docs/process/COMMUNICATION.md) para explicação de termos por nível, correções leves do operador e templates (ticket, status, daily, incidente, RCA, review, reunião).

## Documentação

Uma mudança que altera escopo, stage, processo ou uma decisão atualiza o arquivo canônico correspondente acima. O estado de cada sessão vai para `docs/status/CURRENT.md`; o README só muda por posicionamento, marcos, capabilities entregues ou arquitetura de alto nível. Linke em vez de duplicar. Rode `python tools/check_docs.py` antes de terminar.

## Memória

- `brain/` é a memória do projeto; `docs/learning/` é o treinamento do operador. Não misture.
- Uma sessão não cria fato permanente. Descobertas não validadas vão para `brain/inbox/`.
- Carregue `brain/index.md` primeiro e depois só os arquivos específicos necessários.

## Git

- `main` é o baseline estável. Todo trabalho depois do commit de baseline do Stage 0 acontece numa branch e chega à `main` por PR.
- Não altere trabalho não relacionado. Não crie remotes, não faça push nem publique sem autorização explícita.

## Segurança

Nunca commite nem exiba secrets. `.env` e credenciais ficam fora do Git.

## Dados sintéticos

Todas as organizações, pessoas, documentos, transações e métricas são fictícios. Nenhum dado real de fatura, fornecedor, pagamento ou pessoa.

## Honestidade

Nunca apresente um cliente, métrica ou incidente simulado como real. Rotule hipóteses como hipóteses.
