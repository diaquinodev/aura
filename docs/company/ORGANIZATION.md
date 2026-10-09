# Organização (conceitual)

> Estas áreas representam **responsabilidades de negócio**. Elas **não** significam que existe um agente de IA por departamento. Agentes são introduzidos apenas quando há benefício mensurável, registrado como decisão em `brain/decisions/`.

```text
AURA
├── Product            o que construir e por quê
├── Engineering        construir e manter o software
├── Quality            provar que funciona (testes, evals, aceite)
├── Platform           CI/CD, ambientes, segurança, observabilidade
├── Operations         incidentes, plantão, runbooks
└── Customer Success   onboarding, suporte, feedback de clientes (simulados)
```

| Área | Responsável por | Hoje |
|---|---|---|
| Product | Definição do problema, roadmap, priorização | Operador, com orientação de IA |
| Engineering | Código, design, reviews | Operador, com assistência de IA |
| Quality | Estratégia de testes, critérios de aceite | Não iniciado |
| Platform | Git, CI, ambientes, segredos | Não iniciado (Git não inicializado) |
| Operations | Incidentes e recuperação | Não iniciado (Stage 8) |
| Customer Success | Feedback de cliente simulado (AURA-SYN-001) | Não iniciado (Stage 2) |

Estas são as áreas internas da AURA. Os stakeholders do lado do cliente (Finance, Procurement, Compliance na AURA-SYN-001) são personas em [../../simulation/AURA-SYN-001.md](../../simulation/AURA-SYN-001.md).

No Stage 0, todos os papéis são exercidos pelo operador. A IA atua como mentora e assistente, não como um departamento.
