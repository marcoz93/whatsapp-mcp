# Programa de pesquisa arquitetural

Este programa investiga uma parte ortogonal do problema por vez. Seu objetivo é produzir conhecimento reutilizável antes de escolher telas, agentes, bancos de dados ou fluxos definitivos.

O sistema continua em **design time**. Resultado de pesquisa não é decisão arquitetural automática.

## Linguagem de evidência

Todo resultado relevante deve ser marcado como:

- **Evidência:** algo observado diretamente em uma fonte, produto ou caso real.
- **Inferência:** conclusão derivada da comparação entre evidências.
- **Hipótese:** explicação ou solução que ainda precisa ser testada.
- **Decisão:** escolha explícita do projeto, com razão e consequências registradas.

Essa separação impede que uma interface conhecida do mercado seja confundida com a estrutura real do nosso problema.

## Ciclo de cada pesquisa

1. Formular a pergunta e a decisão que ela poderá informar.
2. Revisar o corpus local e localizar os eixos afetados.
3. Levantar teoria, pesquisas acadêmicas e trabalhos anteriores.
4. Procurar produtos e nichos adjacentes que resolveram partes do problema.
5. Fazer engenharia reversa das entidades, estados, relações, informações e ações.
6. Comparar as alternativas por uma matriz morfológica.
7. Registrar conflitos, lacunas e hipóteses testáveis.
8. Validar as hipóteses com casos reais antes de converter resultados em arquitetura.
9. Atualizar os eixos proprietários, o mapa de fontes e o mapa de lacunas.

Quando houver pesquisa paralela, a rodada padrão separa três olhares: mercado e interfaces existentes; teoria e interação humano–IA; requisitos e arquitetura da informação. A síntese é feita depois, preservando divergências.

## Critério de conclusão de um bloco

Um bloco pode ser encerrado quando contém:

- pergunta e escopo explícitos;
- fontes primárias rastreáveis;
- paisagem de soluções e padrões existentes;
- requisitos inferidos e suas evidências;
- alternativas ainda abertas;
- lacunas que nenhuma referência resolveu;
- hipóteses e método de validação;
- ligação com os eixos arquiteturais afetados.

## Fila de pesquisa

| Ordem | Bloco | Pergunta principal | Estado |
|---:|---|---|---|
| 01 | [Painel de atividades e interface humano–agentes](01-activity-dashboard-and-human-agent-interface.md) | O que uma pessoa precisa ver, compreender e controlar para coordenar humanos e agentes? | Primeira rodada concluída; validação pendente |
| 02 | Ontologia e ciclo da unidade de trabalho | Qual é o objeto coordenado: objetivo, missão, caso, projeto, thread, compromisso ou tarefa? | Pendente |
| 03 | Identificação e roteamento de threads | Como reconhecer continuidade, mudança de assunto e contexto compartilhado? | Pendente |
| 04 | Fronteiras, especialização e formação de equipes | Quando reutilizar um agente, criar outro ou formar um time? | Pendente |
| 05 | Persistência e ativação | O que é contínuo, temporário, episódico, dormente ou encerrado? | Pendente |
| 06 | Memória e promoção de contexto | O que fica local, compartilhado, organizacional ou descartável? | Pendente |
| 07 | Compromissos, autoridade e delegação | Quem pode prometer, aprovar, executar, interromper e responder pelo quê? | Pendente |
| 08 | Coordenação, dependências e handoffs | Como representar espera, bloqueio, precedência, negociação e transferência? | Pendente |
| 09 | Avaliação, aprendizagem e melhoria | Como distinguir atividade, progresso, resultado, qualidade e recorrência? | Pendente |
| 10 | Canais, ingestão e operação | Como conectar WhatsApp e outros canais sem acoplar a arquitetura ao transporte? | Pendente |

## Regra de avanço

Não é necessário terminar toda a fila antes de prototipar. Um protótipo, porém, deve declarar quais hipóteses testa e não pode ser tratado como arquitetura final por ter se tornado visível.
