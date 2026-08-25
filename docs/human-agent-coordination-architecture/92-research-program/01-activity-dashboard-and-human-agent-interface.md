# Pesquisa 01 — painel de atividades e interface humano–agentes

**Estado:** primeira rodada concluída em 25 de agosto de 2026; nenhuma interface aprovada.

## Pergunta central

> O que uma pessoa precisa ver, compreender e controlar para coordenar trabalho realizado por humanos e agentes?

O painel não deve ser projetado como um lugar para “ver agentes trabalhando”. Ele deve ajudar uma pessoa a perceber situações, tomar decisões e intervir na realização de objetivos.

## Perguntas que a interface precisa responder

1. O que exige minha atenção agora?
2. O que mudou desde minha última visita?
3. Quais objetivos estão avançando e quais apenas acumulam atividade?
4. Quem ou qual agente é responsável por cada próximo passo?
5. O que está esperando resposta, bloqueado, atrasado ou em risco?
6. Que compromisso foi assumido, por quem e para quando?
7. O que um agente está fazendo, por que começou e com qual autoridade?
8. O que foi apenas sugerido, aprovado, executado, observado e verificado?
9. Que informação sustenta uma classificação, recomendação ou ação?
10. Qual contexto o agente recebeu e de qual memória ele se valeu?
11. Que ação externa está prestes a acontecer e ela pode ser desfeita?
12. Onde há conflito de prioridade, responsável, prazo ou interpretação?
13. O sistema está vendo o universo inteiro ou uma amostra desatualizada?
14. Posso corrigir, pausar, assumir, delegar ou cancelar sem perder o histórico?
15. Consigo reconstruir depois quem decidiu e o que efetivamente ocorreu?

## Como esta rodada foi conduzida

Três frentes independentes pesquisaram:

- produtos de mercado e interfaces de coordenação;
- literatura de interação humano–IA, automação e supervisão;
- requisitos de arquitetura da informação, proveniência e controle.

O resultado abaixo é uma síntese inicial para orientar engenharia reversa e validação, não um desenho de tela.

## O que o mercado já resolveu

Nenhuma categoria encontrada resolve o problema inteiro. Cada nicho tornou uma parte observável e controlável.

| Padrão | Referências | O que podemos extrair |
|---|---|---|
| Conversa e contexto compartilhado | [PromptQL](https://promptql.io/product) | Threads preservam colaboração e contexto; respostas podem se transformar em ativos reutilizáveis. |
| Trabalho estruturado | [Linear](https://linear.app/docs/conceptual-model?_rsc=1bead), [Jira com Rovo](https://support.atlassian.com/jira-software-cloud/docs/collaborate-on-work-items-with-ai-agents/) | Projeto, issue, responsável, estado, dependência e ciclo formam a espinha dorsal; o agente participa do trabalho. |
| Atendimento e filas | [Zendesk](https://support.zendesk.com/hc/en-us/articles/6712096584090-Understanding-how-omnichannel-routing-uses-queues-to-route-work-to-agents), [Intercom Fin](https://www.intercom.com/help/en/articles/12396892-manage-fin-ai-agent-s-escalation-guidance-and-rules) | Filas, SLA, prioridade, escalonamento e tomada humana aparecem quando a capacidade de atenção é escassa. |
| Incidentes e comando | [PagerDuty](https://support.pagerduty.com/main/docs/incidents), [incident.io](https://docs.incident.io/incidents/lifecycle) | Severidade, papel, timeline, ação, comunicação e resolução são coordenados em torno de uma situação com impacto. |
| Execução e observabilidade de agentes | [Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/how-to-monitor-agents-dashboard), [LangSmith](https://docs.langchain.com/langsmith/observability-concepts), [AgentOps](https://docs.agentops.ai/v1/introduction), [Arize Phoenix](https://arize.com/docs/phoenix/) | Runs, traces, passos, ferramentas, latência, custo, erros e avaliações permitem inspecionar como a execução aconteceu. |

### Padrões recorrentes

- **Evidência:** produtos maduros coordenam o trabalho em torno de um objeto de domínio — ticket, issue, incidente, caso ou thread — e não em torno de um agente isolado.
- **Evidência:** detalhes aparecem progressivamente: contexto, unidade de trabalho, execução, passos, eventos e artefatos.
- **Evidência:** existem três graus frequentes de intervenção humana: orientar, revisar e assumir.
- **Evidência:** operação ao vivo e registro durável são separados, mas ligados por uma timeline.
- **Evidência:** filas aparecem onde muitas situações disputam pouca atenção humana.
- **Inferência:** alertas, aprovações e trabalho pendente não devem ser misturados, pois exigem decisões diferentes.
- **Inferência:** ferramentas de observabilidade explicam uma execução, mas ainda não coordenam bem objetivos, compromissos e dependências entre vários humanos e agentes.

## Fundamentos de interação humano–agentes

| Fundamento | Fonte primária | Consequência para o painel |
|---|---|---|
| Iniciativa mista | [Horvitz, 1999](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/11/chi99horvitz.pdf) | Humano e sistema podem iniciar ações; custo da interrupção e incerteza devem influenciar quando pedir atenção. |
| Tipos e níveis de automação | [Parasuraman, Sheridan e Wickens, 2000](https://pubmed.ncbi.nlm.nih.gov/11760769/) | Aquisição, análise, decisão e ação podem ter autonomias diferentes; não existe apenas “manual” ou “automático”. |
| Consciência situacional | [Endsley, 1995](https://doi.org/10.1518/001872095779049543) | A interface precisa apoiar percepção do estado, compreensão do significado e projeção do que acontecerá. |
| Confiança calibrada | [Lee e See, 2004](https://doi.org/10.1518/hfes.46.1.50_30392) | Mostrar capacidade, limites e evidências é melhor do que incentivar confiança genérica. |
| Delegação ajustável | [Miller e Parasuraman, 2007](https://doi.org/10.1518/001872007779598037) | Autoridade pode variar por tarefa, etapa, risco e situação. |
| Modelos mentais compartilhados | [Scheutz et al., 2017](https://hrilab.tufts.edu/publications/scheutzetal17smm/) | Objetivo, plano, papéis, estado e desvios precisam ser inteligíveis para toda a equipe. |
| Diretrizes de interação com IA | [Amershi et al., 2019](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/) | Expectativas, correção, feedback e explicações devem aparecer no momento apropriado. |
| Governança de risco | [NIST AI RMF](https://doi.org/10.6028/NIST.AI.100-1) | Risco, responsabilidade, monitoramento e tratamento precisam existir além da execução técnica. |

### Síntese desses fundamentos

A interface deve tornar observáveis quatro camadas distintas:

1. **Situação:** o que existe agora e o que mudou.
2. **Interpretação:** por que isso importa e qual resultado está em risco.
3. **Intenção:** o que humanos e agentes pretendem fazer.
4. **Controle:** o que pode ser autorizado, corrigido, interrompido ou assumido.

Uma porcentagem de “confiança” isolada não cobre essas camadas.

## Hipótese estrutural inicial

Não parece haver uma única tela central suficiente. A menor estrutura que explica os padrões encontrados é:

```text
torre de controle
  → fila de atenção
    → unidade de trabalho
      → execução ou compromisso
        → evento, evidência ou artefato
```

Isto produz uma hipótese de navegação:

```text
visão geral → exceção → contexto → ação → proveniência
```

O agente aparece como participante e executor com identidade, capacidade, autoridade e histórico. A entidade principal continua sendo a unidade de trabalho que conduz a um objetivo.

Essa hipótese deve ser testada contra casos reais. “Unidade de trabalho” pode se concretizar como missão, caso, projeto, incidente, compromisso, tarefa ou combinação hierárquica desses tipos.

## Oito vistas candidatas

Estas são responsabilidades informacionais; ainda não sabemos se se tornarão oito telas, painéis combinados ou modos de uma mesma interface.

| Vista candidata | Pergunta dominante | Conteúdo necessário |
|---|---|---|
| Torre de controle | Onde o sistema precisa de atenção? | objetivos, saúde, risco, prazos, bloqueios, exceções e mudanças recentes |
| Filas e triagem | O que devo decidir agora? | prioridade, razão da entrada, SLA, impacto, responsável sugerido e ação disponível |
| Unidade de trabalho | Qual é a situação completa? | objetivo, threads, participantes, estado, próximos passos, dependências, compromissos e timeline |
| Compromissos e calendário | Quem prometeu o quê e para quando? | credor, devedor, conteúdo, prazo, condição, estado e quebra de compromisso |
| Operação dos agentes | Quem está ativo e dentro de quais limites? | missão, capacidade, contexto, autoridade, estado, carga, custo e último resultado |
| Revisão e autoridade | Que intervenção humana é necessária? | proposta, evidência, impacto, alvo, diferença, reversibilidade, aprovador e validade |
| Run e trace | Como esta execução chegou ao resultado? | passos, ferramentas, entradas, saídas, erros, latência, custo, versões e correlações |
| Memória, artefatos e auditoria | O que foi preservado e pode ser provado? | origem, escopo, versão, validade, acesso, promoções de memória e cadeia de decisões |

## Modelo informacional mínimo inferido

Entidades que o painel provavelmente precisará relacionar:

- objetivo e unidade de trabalho;
- thread e evento de comunicação;
- pessoa, agente, papel e equipe;
- compromisso, tarefa e dependência;
- run, passo e chamada de ferramenta;
- memória, evidência e artefato;
- regra de autoridade e aprovação;
- estado e transição.

Relações candidatas:

```text
canal → thread → unidade de trabalho → compromissos
unidade de trabalho → runs → ferramentas/memórias → artefatos
ação ou efeito → iniciado, autorizado e executado por pessoa/agente/política
```

O segundo bloco do programa deverá testar essa ontologia; ela ainda não está fechada.

## Matriz informação → decisão → ação

| Informação visível | Decisão apoiada | Ação possível |
|---|---|---|
| motivo da entrada na fila | merece atenção agora? | priorizar, adiar ou dispensar |
| objetivo, estado e desvio | o plano ainda é válido? | manter, replanejar ou encerrar |
| responsável e próximo passo | a responsabilidade está clara? | atribuir, cobrar ou assumir |
| dependência e espera | existe bloqueio real? | destravar, escalar ou renegociar |
| proposta e evidência | a recomendação é adequada? | aprovar, editar ou rejeitar |
| alvo, impacto e reversibilidade | a ação externa é segura? | executar, restringir ou exigir outra aprovação |
| trace e versões | a execução é confiável e reproduzível? | aceitar, repetir, corrigir ou investigar |
| origem e escopo da memória | o contexto pode ser usado aqui? | promover, limitar, corrigir ou esquecer |
| prazo, SLA e risco | quando intervir? | antecipar, escalonar ou repriorizar |
| efeito observado | o objetivo foi realmente alcançado? | verificar, reabrir ou aprender |

## Requisitos de confiança, autoridade e proveniência

O registro precisa permitir navegar pela cadeia:

```text
mensagem → roteamento → unidade de trabalho → run → ferramenta
→ artefato ou memória → aprovação → efeito externo → verificação
```

Para isso, a interface deve preservar:

- identificadores estáveis, timestamps, origem e correlação;
- diferença entre observado, inferido, proposto, aprovado, executado e verificado;
- versões de agente, modelo, ferramenta, política, memória e artefato;
- completude e atualidade da sincronização;
- quem iniciou, autorizou, executou, alterou e verificou;
- prévia, diferença, alvo, impacto e reversibilidade antes de ações relevantes;
- pausa, cancelamento, tomada humana e compensação quando tecnicamente possíveis.

[W3C PROV](https://www.w3.org/TR/prov-overview/), [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-view-execution-details.html) e [OpenAI Agents SDK tracing](https://openai.github.io/openai-agents-python/tracing/) são referências úteis para essa cadeia, embora nenhuma modele sozinha toda a coordenação.

## O que não deve dominar a interface

- fluxo bruto de mensagens como página inicial;
- todos os logs, tokens, prompts e passos internos por padrão;
- raciocínio interno do modelo como se fosse evidência auditável;
- métricas de vaidade sobre quantidade de atividade;
- um único Kanban misturando objetivos, conversas, tarefas, agentes e runs;
- memórias sem origem, escopo, validade ou mecanismo de correção;
- “confiança” numérica sem base, consequência e alternativa;
- configuração administrativa misturada à tomada de decisão operacional.

## Lacunas encontradas

Não encontramos uma solução que integre satisfatoriamente:

- tickets, projetos, incidentes, compromissos e execuções de agentes no mesmo modelo de coordenação;
- aprovações com conteúdo exato, versão, validade, efeito e reversibilidade explícitos;
- dependências de projeto ligadas diretamente ao trace que executou o trabalho;
- prioridade comum entre impacto, risco, custo, SLA, incerteza e atenção humana;
- supervisão em vários níveis: portfólio, missão, unidade de trabalho e execução;
- espera, bloqueio e negociação entre múltiplos agentes;
- descoberta semântica de threads e roteamento entre assuntos sobrepostos.

Portanto, a oportunidade não parece ser copiar um dashboard existente, mas compor princípios já maduros de vários nichos em torno de uma ontologia coerente.

## Próxima rodada de pesquisa

1. Fazer engenharia reversa visual de cinco referências: PromptQL, LangSmith, Zendesk, PagerDuty e Jira com Rovo.
2. Catalogar, para cada uma, objetos, hierarquia, estados, filas, ações humanas, evidências e limitações.
3. Construir a matriz morfológica das alternativas de interface.
4. Percorrer casos reais: reclamação de cliente, orçamento, viagem, suporte contínuo, ação externa irreversível e conversa com múltiplas threads.
5. Testar as tarefas de operador, gestor e auditor em cada caso.
6. Só então produzir wireframes que explicitem quais hipóteses estão sendo testadas.

## Critérios de validação

- tempo para perceber uma situação relevante;
- tempo e qualidade da intervenção;
- recuperação de contexto depois de uma ausência;
- custo de atenção e quantidade de interrupções;
- clareza de responsável, autoridade e próximo passo;
- capacidade de reconstruir decisões e efeitos;
- escalabilidade entre uma missão e um portfólio;
- proteção de privacidade e limites de memória;
- velocidade para corrigir classificações, planos e ações equivocadas.

## Eixos arquiteturais afetados

Esta pesquisa informa principalmente:

- [identificação e roteamento](../02-identification-and-routing/current-findings.md);
- [objetivos e objetos de trabalho](../03-goals-and-work-objects/current-findings.md);
- [distribuição e coordenação](../04-task-distribution-and-coordination/current-findings.md);
- [arquitetura dos agentes](../05-agent-architecture/current-findings.md);
- [memória e conhecimento](../08-memory-and-knowledge/current-findings.md);
- [governança, autoridade e avaliação](../09-governance-authority-and-evaluation/current-findings.md).

As definições continuam pertencendo a esses eixos. Este documento registra a pesquisa transversal que poderá justificá-las.
