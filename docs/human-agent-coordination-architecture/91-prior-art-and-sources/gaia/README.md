# Gaia

## Estado desta nota

Esta é uma nota de fonte, não a arquitetura do projeto. Ela registra o que Gaia propõe, relaciona a proposta aos nossos eixos e preserva seus limites sem transferir para Gaia a propriedade das nossas definições.

## Fontes primárias

- Michael Wooldridge, Nicholas R. Jennings e David Kinny. [The Gaia Methodology for Agent-Oriented Analysis and Design](https://www.cs.ox.ac.uk/people/michael.wooldridge/pubs/jaamas2000b.pdf), 2000.
- Franco Zambonelli, Nicholas R. Jennings e Michael Wooldridge. [Developing Multiagent Systems: The Gaia Methodology](https://dl.acm.org/doi/10.1145/958961.958963), 2003 — extensão da metodologia original.

## Por que Gaia fica separada

Gaia é transversal: ela relaciona organização, papéis, responsabilidades, permissões, atividades, protocolos, agentes e serviços. Colocá-la dentro de apenas um eixo esconderia parte da contribuição; copiá-la em todos os eixos criaria definições concorrentes.

A regra é:

- esta nota explica Gaia;
- cada eixo continua responsável pelos conceitos do nosso projeto;
- modelos integrados conectam os eixos;
- o mapa de lacunas registra o que ainda não resolvemos.

## Modelo conceitual original

Gaia trata um sistema multiagente como uma **organização computacional**. Sua análise parte de papéis e interações, antes de decidir quais agentes concretos existirão.

Um papel é caracterizado por:

- **responsabilidades**: o que deve acontecer e o que deve permanecer verdadeiro;
- **permissões**: quais recursos e informações podem ser usados;
- **atividades**: ações executadas pelo próprio papel;
- **protocolos**: interações do papel com outros papéis.

As responsabilidades são divididas em:

- **liveness**: propriedades de progresso — algo desejável eventualmente acontece;
- **safety**: invariantes — estados indesejáveis nunca devem ocorrer.

O método produz dois modelos na análise:

1. **modelo de papéis**, com papéis e suas propriedades;
2. **modelo de interações**, com os protocolos entre papéis.

No design, esses modelos são refinados em:

1. **modelo de agentes**, que agrega papéis em tipos de agente;
2. **modelo de serviços**, que descreve as funções oferecidas;
3. **modelo de acquaintances**, que mostra quem precisa se comunicar com quem.

Papéis e agentes não têm relação um-para-um: um agente pode exercer vários papéis, e um papel pode ser exercido por mais de um agente.

## Relação com nossos eixos

| Conceito de Gaia | Eixo proprietário no nosso corpus | Uso possível |
|---|---|---|
| Organização computacional | [Equipes e organização](../../06-teams-and-organization/) | Estruturar o coletivo sem reduzir o sistema a agentes isolados |
| Papel | [Equipes e organização](../../06-teams-and-organization/) | Separar posição organizacional de identidade de agente |
| Responsabilidade | [Objetivos e objetos de trabalho](../../03-goals-and-work-objects/) e [governança](../../09-governance-authority-and-evaluation/) | Distinguir resultado esperado de obrigação normativa |
| Permissão | [Governança](../../09-governance-authority-and-evaluation/) e [memória](../../08-memory-and-knowledge/) | Controlar ação e acesso a contexto |
| Atividade | [Distribuição e coordenação](../../04-task-distribution-and-coordination/) | Representar trabalho interno que não exige interação |
| Protocolo | [Comunicação](../../01-communication-and-events/) e [distribuição](../../04-task-distribution-and-coordination/) | Especificar interações sem confundi-las com mensagens brutas |
| Tipo de agente e serviços | [Arquitetura dos agentes](../../05-agent-architecture/) | Derivar identidades executoras depois da análise organizacional |
| Acquaintances | [Equipes e organização](../../06-teams-and-organization/) e [comunicação](../../01-communication-and-events/) | Mapear dependências de comunicação |
| Liveness e safety | [Persistência](../../07-persistence-and-lifecycle/) e [governança](../../09-governance-authority-and-evaluation/) | Expressar progresso e invariantes ao longo do tempo |

## Pressupostos e limites da versão original

A versão original simplifica deliberadamente o problema. Entre seus limites:

- presume uma organização relativamente estática;
- não desenvolve criação e remoção dinâmica de papéis;
- não trata profundamente agentes com interesses conflitantes;
- pressupõe capacidades e serviços relativamente estáveis;
- modela permissões principalmente como acesso a informação;
- deixa sistemas abertos, estruturas organizacionais mais ricas e semântica formal completa como extensões;
- não desenvolve em detalhe papéis coletivos exercidos por vários indivíduos.

Esses limites não invalidam Gaia. Eles mostram exatamente onde nossa arquitetura precisa complementar a fonte: roteamento dinâmico de assuntos, agentes e equipes temporários, memória seletiva, compromissos sociais, negociação, mudança de papéis e coexistência entre trabalho contínuo e missões com término.

## Consequência provisória para o projeto

Gaia nos oferece uma linguagem organizacional e um processo de passagem de papéis para agentes. Ela não resolve sozinha identificação de fios, compromissos sociais, persistência dinâmica ou execução em canais reais. Portanto, será usada como uma lente transversal, não como arquitetura final.
