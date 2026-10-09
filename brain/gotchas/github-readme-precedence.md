# `.github/README.md` substitui o README da raiz no GitHub

**Sintoma:** a página do repositório no GitHub mostra um README diferente do `README.md` da raiz.

**Causa:** o GitHub escolhe o README a exibir nesta ordem: `.github/`, depois a raiz do repositório, depois `docs/`. Um `README.md` dentro de `.github/` tem prioridade.

**Regra:** não crie `.github/README.md`. Coloque notas de workflow nos próprios arquivos de workflow ou em `docs/`.

**Fonte:** documentação do GitHub ("About READMEs"). Encontrado no Bootstrap 01 durante a revisão da estrutura proposta; ainda não observado em um remoto real (não existe nenhum).
