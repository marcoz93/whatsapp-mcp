# Arquitetura de coordenação entre humanos e agentes

Este diretório preserva a exploração de design de um sistema independente de canal para coordenar comunicação, objetivos, trabalho, humanos e agentes.

O conteúdo ainda não é uma especificação final nem um plano de implementação. Cada pasta representa um eixo que deve permanecer conceitualmente separado dos demais.

## Mapa dos eixos

| Pasta | Pergunta central |
|---|---|
| `01-communication-and-events` | O que aconteceu na comunicação? |
| `02-identification-and-routing` | A que assunto, fio, objetivo ou contexto isso pertence? |
| `03-goals-and-work-objects` | O que queremos alcançar e que tipo de trabalho é este? |
| `04-task-distribution-and-coordination` | Quem faz o quê, quando e dependendo de quem? |
| `05-agent-architecture` | O que é um agente e como ele funciona? |
| `06-teams-and-organization` | Como humanos, agentes e papéis são organizados coletivamente? |
| `07-persistence-and-lifecycle` | Por quanto tempo cada entidade existe e como muda? |
| `08-memory-and-knowledge` | O que cada entidade sabe, acessa e preserva? |
| `09-governance-authority-and-evaluation` | O que pode, deve ou não pode ser feito, e como o resultado é avaliado? |

## Pastas transversais

| Pasta | Função |
|---|---|
| `90-integrated-models` | Relacionar os eixos em árvores, matrizes, statecharts e arquiteturas. |
| `91-prior-art-and-sources` | Registrar fontes, autores, formalizações reutilizáveis e limitações. |
| `99-coverage-gaps-and-open-questions` | Controlar o que já foi explorado, lacunas, contradições e perguntas abertas. |

## Regra de organização

Uma definição pertence ao eixo que responde por ela. Modelos que cruzam vários eixos apenas referenciam essas definições; não as duplicam.

O documento [WhatsApp como memória e camada de ação](../whatsapp-zwicky-box.md) preserva a exploração inicial que deu origem a este corpus.
