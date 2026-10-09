# Índice do brain

Memória operacional do projeto. Leia este arquivo e depois abra apenas as entradas de que precisar. Mantenha cada linha com uma frase; este arquivo é um índice, não uma enciclopédia.

## Decisões

Escolhas duradouras. Formato: linha de cabeçalho com Status, Owner, Data; depois Contexto, Decisão, Justificativa, Trade-offs e alternativas, Impacto. Registre a decisão, não a discussão.

- [0001](decisions/0001-memory-routing.md): `brain/` guarda a memória do projeto, `docs/learning/` guarda o treinamento do operador; fatos, lições de workflow e falhas recorrentes vão para lugares diferentes.
- [0002](decisions/0002-create-on-first-content.md): diretórios e docs são criados quando recebem conteúdo real, não com antecedência.
- [0003](decisions/0003-synthetic-data-only.md): apenas organizações, documentos e dados sintéticos até que um piloto seja explicitamente aprovado (justificativa atualizada pela 0007).
- [0004](decisions/0004-docs-check-script.md): links Markdown e o nível de treinamento são verificados por um script Python que usa só a biblioteca padrão.
- [0005](decisions/0005-repo-language.md): todo o conteúdo e a saída em português do Brasil; código, arquivos e commits em inglês.
- [0006](decisions/0006-communication-policy-location.md): a política de comunicação fica em `docs/process/COMMUNICATION.md`, referenciada a partir do `AGENTS.md`; ainda sem Rule nem Skill.
- [0007](decisions/0007-pivot-to-enterprise-agentic-automation.md): pivot de SaaS vertical de saúde para automação agêntica corporativa; Aura Ops, começando por Accounts Payable. Registra a direção anterior.
- [0008](decisions/0008-synthetic-tenant-identifiers.md): organizações sintéticas usam IDs `AURA-SYN-NNN`, não nomes com cara de marca.
- [0009](decisions/0009-tooling-and-work-management.md): venv + pip + pyproject; GitHub Issues, Milestones como sprints, Actions para CI; repositório privado.

## Insights

Observações que podem ser relevantes. Formato: Observação, Por que importa, Evidência, Impacto possível, Precisa de validação?

- [no-show-first-metric](insights/no-show-first-metric.md): SUPERSEDED pela 0007; a lição de "uma métrica clara primeiro" continua válida.
- [communication-evals](insights/communication-evals.md): pontuar status updates, comunicações de incidente e defesas de decisão do operador com base em uma rubrica.

## Gotchas

Problemas não óbvios já enfrentados ou confirmados.

- [github-readme-precedence](gotchas/github-readme-precedence.md): `.github/README.md` substituiria o README da raiz no GitHub.

## Investigações

Investigações técnicas. Nenhuma ainda; `brain/investigations/` é criado junto com a primeira.

## Inbox

Candidatos não validados. Promova para outra categoria ou exclua após a revisão.

- [reflect-edit-targets](inbox/reflect-edit-targets.md): onde o `/reflect` gravaria suas edições de skill, e elas sobreviveriam a uma atualização do plugin?
