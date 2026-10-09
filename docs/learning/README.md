# Aprendizado

Esta área acompanha o **desenvolvimento profissional do operador**. A memória do projeto (o que o projeto sabe) fica em [../../brain/index.md](../../brain/index.md), não aqui.

Exemplo da separação:

- `brain/gotchas/github-readme-precedence.md` registra um fato do projeto: o GitHub exibe `.github/README.md` no lugar do README da raiz.
- [GLOSSARY.md](GLOSSARY.md) explica um conceito: o que é um repositório.

## Nível de treinamento

`TRAINING_LEVEL = 1`

| Nível | Nome | A IA faz | O operador faz |
|---|---|---|---|
| 1 | Guided | Explica, apresenta opções, mostra riscos, estrutura o raciocínio | Toma decisões importantes com apoio |
| 2 | Assisted | Dá contexto, executa tarefas mecânicas, revisa, questiona decisões | Prioriza, investiga, decide a arquitetura, implementa as partes críticas |
| 3 | Professional | Fornece ticket, contexto de negócio, ferramentas, evidência | Atua como um membro real do time |

O nível muda somente por decisão do operador, registrada em `brain/decisions/`, com proof of work do [LEARNING-PATH.md](LEARNING-PATH.md). Passar de Guided para Assisted exige capacidade crescente e demonstrada de interpretar tickets, priorizar, implementar, testar e explicar decisões; ler sobre isso não basta. Quando o nível mudar, atualize a linha `TRAINING_LEVEL` aqui, no [../../README.md](../../README.md) e no [../../AGENTS.md](../../AGENTS.md); o `tools/check_docs.py` falha se eles divergirem.

## Arquivos

- [LEARNING-PATH.md](LEARNING-PATH.md): competências e seus status.
- [GLOSSARY.md](GLOSSARY.md): conceitos usados até agora.
- `journal/`: uma entrada por sessão relevante, usando [journal/_TEMPLATE.md](journal/_TEMPLATE.md).
