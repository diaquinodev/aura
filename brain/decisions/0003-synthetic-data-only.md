# 0003 Apenas dados sintéticos

**Status:** Aceita · **Owner:** Operador · **Data:** 2026-10-08 (Bootstrap 01)

> **Atualização 2026-10-09 (decisão 0007):** o domínio mudou de negócios ligados à saúde para Finance & Operations corporativo. A decisão continua válida: faturas, dados de fornecedores e de pagamentos reais são pessoais e confidenciais (a LGPD continua se aplicando a dados pessoais), então todas as organizações, documentos e transações continuam sintéticos. A prontidão para piloto agora é o Stage 10, e os datasets sintéticos são o Stage 3. O texto original abaixo foi mantido como escrito.

## Contexto

Os segmentos-alvo (dermatologia, odontologia, estética) são ligados à saúde. Dados reais de clientes trariam obrigações legais (por exemplo, a LGPD) que o projeto ainda não consegue cumprir, e um portfólio que confunde simulação e realidade perde credibilidade.

## Decisão

Todos os clientes, pessoas e métricas são fictícios até que um piloto seja explicitamente aprovado no Stage 9. Nenhum dado clínico, diagnóstico ou prontuário médico em nenhum estágio planejado atualmente.

## Justificativa

Elimina o risco legal e mantém o portfólio honesto.

## Trade-offs e alternativas

Usar dados reais anonimizados: ainda é arriscado coletar e anonimizar corretamente; nenhum benefício nesta fase.

## Impacto

O Stage 2 precisa produzir dados sintéticos realistas o bastante para exercitar o produto. O `.gitignore` exclui arquivos de banco de dados locais e `data/local/`.
