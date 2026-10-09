# Onde o `/reflect` gravaria suas edições?

**Preocupação candidata (não validada):** o `/reflect` do pstack é descrito como roteando cada aprendizado "para uma edição concreta em uma skill existente". Este repositório não tem skills próprias; as únicas skills instaladas ficam no cache do plugin (`~/.cursor/plugins/cache/cursor-public/pstack/<hash>/skills/`). Edições ali provavelmente seriam perdidas quando o plugin fosse atualizado, e valeriam para todos os projetos, não só para a Aura.

**Para validar:** na primeira execução real do `/reflect`, verificar qual arquivo ele propõe alterar antes de aceitar.

**Se confirmado:** promover para `brain/gotchas/` e decidir se lições de workflow específicas do projeto pertencem ao `AGENTS.md` ou a uma skill de projeto.
