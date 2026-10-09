# Ciclo de vida da sessão

Uma sessão é um bloco focado de trabalho (com ou sem um agente de IA). O objetivo é conseguir retomar o trabalho meses depois a partir de um contexto curado, não de transcrições.

## Início da sessão

1. **Identificar o objetivo.** Uma frase: o que estará pronto quando esta sessão terminar?
2. **Recuperar o contexto mínimo.** Leia [../../brain/index.md](../../brain/index.md) e, depois, apenas os arquivos relevantes para o objetivo. `/recall` pode ajudar após uma pausa longa.
3. **Verificar o estado do Git.** `git status`, `git branch --show-current`, `git log -5 --oneline`.
4. **Verificar o backlog**, quando ele existir (Stage 2).
5. **Identificar o nível de treinamento** em [../learning/README.md](../learning/README.md).

## Durante a sessão

Registre apenas decisões, descobertas e evidências. Não transcreva a conversa. Ideias não validadas vão para `brain/inbox/`.

## Fim da sessão

Escreva uma entrada no journal a partir de [../learning/journal/_TEMPLATE.md](../learning/journal/_TEMPLATE.md) que cubra:

1. **Resumo do trabalho**: o que foi feito.
2. **Decisões**: o que foi decidido e por quê. As duradouras também vão para `brain/decisions/`.
3. **Evidências**: comandos, testes e seus resultados.
4. **Perguntas em aberto**: o que ainda não foi resolvido.
5. **Aprendizado**: o que o operador deve estudar ou revisar.
6. **Insights**: ideias de produto ou de processo. As que valem a pena manter vão para `brain/insights/`.
7. **Próxima sessão**: o próximo passo lógico.
8. **Reflexão**: se a sessão ensinou algo sobre *como trabalhamos*, considere `/reflect`. Isso não substitui o registro factual acima.

Em seguida, rode `python tools/check_docs.py` e revise o `git diff` antes de fazer o commit. Última pergunta: esta sessão produziu engenharia executável? Se não, verifique o documentation budget em [WORKING-MODEL.md](WORKING-MODEL.md).
