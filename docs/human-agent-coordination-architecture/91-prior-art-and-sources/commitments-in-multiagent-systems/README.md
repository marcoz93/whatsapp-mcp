# A Conceptual Analysis of Commitments in Multiagent Systems

## Referência localizada

Munindar P. Singh. **A Conceptual Analysis of Commitments in Multiagent Systems**. Department of Computer Science, North Carolina State University, Technical Report TR-96-09, 16 de maio de 1996.

- [Cópia local preservada](singh-1996-conceptual-analysis-of-commitments.pdf)
- [PDF mantido pelo autor](https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/commit.pdf)
- [Registro institucional da NC State University Libraries](https://repository.lib.ncsu.edu/items/a51477a9-ddb3-4c93-9c26-268ee5f2fb01)
- [Publicações de Munindar P. Singh](https://www.csc2.ncsu.edu/faculty/mpsingh/papers/)

O registro institucional confirma autor, ano, número do relatório e os arquivos `TR-96-09.pdf` e `TR-96-09.ps`. Como o servidor do autor bloqueou o download automatizado, a cópia local foi recuperada de uma captura de 7 de maio de 2024 da mesma URL no Internet Archive. O arquivo tem 15 páginas, 482.137 bytes e SHA-256 `217fa1c2130da2be197984edbe24840a9c80b1276071f90bcd442f140d3a1345`.

## Questão central

Singh separa duas famílias de compromisso que aparecem na literatura de agentes:

- **compromisso interno ou psicológico**: estado do próprio agente, ligado a intenção, decisão e persistência na ação;
- **compromisso externo ou social**: relação pública entre agentes, observável no nível da interação e da organização.

O paper argumenta que elas se relacionam, mas não podem ser confundidas. Para o nosso projeto, isso impede que uma intenção privada de um agente seja tratada automaticamente como promessa, obrigação ou expectativa legítima perante outra pessoa ou agente.

## Relação preliminar com nossos eixos

| Distinção | Eixo principal | Pergunta que abre |
|---|---|---|
| Compromisso psicológico | [Arquitetura dos agentes](../../05-agent-architecture/) e [persistência](../../07-persistence-and-lifecycle/) | Com o que o agente decidiu prosseguir e quando reconsidera? |
| Compromisso social | [Governança](../../09-governance-authority-and-evaluation/) e [coordenação](../../04-task-distribution-and-coordination/) | Quem deve o quê a quem, sob qual condição? |
| Expressão por comunicação | [Comunicação e acontecimentos](../../01-communication-and-events/) | Que acontecimento cria, altera ou evidencia um compromisso? |
| Implementação em agentes compostos | [Equipes e organização](../../06-teams-and-organization/) | Como compromissos do coletivo se relacionam aos de seus participantes? |

## Limite desta leitura

Esta entrada registra a localização e a tese conceitual confirmada pelo resumo do próprio trabalho. Ainda não incorporamos como definições do projeto a ontologia, as operações ou o ciclo de vida formal dos compromissos. Isso exige leitura analítica do texto e comparação com os trabalhos posteriores do autor, sem retroprojetá-los sobre o relatório de 1996.
