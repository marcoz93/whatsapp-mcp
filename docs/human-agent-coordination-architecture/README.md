# Arquitetura de coordenação entre humanos e agentes

Este diretório preserva a exploração de design de um sistema independente de canal para coordenar comunicação, objetivos, trabalho, humanos e agentes.

O conteúdo ainda não é uma especificação final nem um plano de implementação. Cada pasta representa um eixo que deve permanecer conceitualmente separado dos demais.

## Mapa dos eixos

| Pasta | Pergunta central | Conteúdo atual |
|---|---|---|
| `01-communication-and-events` | O que aconteceu na comunicação? | [Descobertas](01-communication-and-events/current-findings.md) |
| `02-identification-and-routing` | A que assunto, fio, objetivo ou contexto isso pertence? | [Descobertas](02-identification-and-routing/current-findings.md) |
| `03-goals-and-work-objects` | O que queremos alcançar e que tipo de trabalho é este? | [Descobertas](03-goals-and-work-objects/current-findings.md) |
| `04-task-distribution-and-coordination` | Quem faz o quê, quando e dependendo de quem? | [Descobertas](04-task-distribution-and-coordination/current-findings.md) |
| `05-agent-architecture` | O que é um agente e como ele funciona? | [Descobertas](05-agent-architecture/current-findings.md) |
| `06-teams-and-organization` | Como humanos, agentes e papéis são organizados coletivamente? | [Descobertas](06-teams-and-organization/current-findings.md) |
| `07-persistence-and-lifecycle` | Por quanto tempo cada entidade existe e como muda? | [Descobertas](07-persistence-and-lifecycle/current-findings.md) |
| `08-memory-and-knowledge` | O que cada entidade sabe, acessa e preserva? | [Descobertas](08-memory-and-knowledge/current-findings.md) |
| `09-governance-authority-and-evaluation` | O que pode, deve ou não pode ser feito, e como o resultado é avaliado? | [Descobertas](09-governance-authority-and-evaluation/current-findings.md) |

## Pastas transversais

| Pasta | Função | Conteúdo atual |
|---|---|---|
| `90-integrated-models` | Relacionar os eixos em árvores, matrizes, statecharts e arquiteturas. | [Árvores e fluxos](90-integrated-models/decision-trees-and-flows.md) |
| `91-prior-art-and-sources` | Registrar fontes, autores, formalizações reutilizáveis e limitações. | [Mapa de fontes](91-prior-art-and-sources/source-map.md) |
| `92-research-program` | Investigar uma pergunta arquitetural por vez e transformar referências em requisitos verificáveis. | [Programa de pesquisa](92-research-program/README.md) |
| `99-coverage-gaps-and-open-questions` | Controlar o que já foi explorado, lacunas, contradições e perguntas abertas. | [Mapa de cobertura](99-coverage-gaps-and-open-questions/coverage-map.md) |

## Regra de organização

Uma definição pertence ao eixo que responde por ela. Modelos que cruzam vários eixos apenas referenciam essas definições; não as duplicam.

O documento [WhatsApp como memória e camada de ação](../whatsapp-zwicky-box.md) preserva a exploração inicial que deu origem a este corpus.
