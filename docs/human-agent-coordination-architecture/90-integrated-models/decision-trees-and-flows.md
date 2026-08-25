# Árvores de decisão e fluxos já discutidos

Estes modelos conectam os eixos. As definições permanecem nos documentos de descobertas de cada eixo.

## Fluxo abstrato do sistema

```mermaid
flowchart LR
    W["Mundo real"] --> C["Comunicação"]
    C --> G["Objetivos e compromissos"]
    G --> O["Organização"]
    O --> A["Humanos e agentes"]
    A --> X["Ações"]
    X --> W

    K["Conhecimento e memória"] --- C
    K --- G
    K --- O
    K --- A

    N["Regras e autoridade"] --- G
    N --- O
    N --- A
```

## Fluxo operacional

```text
comunicação
→ identificar acontecimentos
→ separar ou localizar fios
→ encontrar ou criar objetivo, caso, projeto ou processo
→ localizar o papel responsável
→ localizar ou ativar humano ou agente
→ atualizar memória e estado
→ identificar o próximo impedimento
→ agir, aguardar, perguntar, agendar ou concluir
→ observar o resultado
→ devolver aprendizado ao nível adequado
```

## Árvore de classificação do trabalho

```mermaid
flowchart TD
    M["Nova mensagem ou acontecimento"] --> A{"Existe algo que exige atenção?"}
    A -->|"Não"| K["Guardar como contexto ou ignorar"]
    A -->|"Sim"| S{"Há mais de um assunto?"}
    S -->|"Sim"| D["Dividir em acontecimentos"]
    S -->|"Não"| I["Tratar como um acontecimento"]
    D --> E
    I --> E
    E{"Pertence a um fio existente?"}
    E -->|"Sim"| U["Atualizar o fio e seu estado"]
    E -->|"Não"| F{"Continua um fio encerrado?"}
    F -->|"Mesmo problema"| R["Reabrir o fio"]
    F -->|"Nova ocorrência"| N["Criar fio relacionado"]
    F -->|"Não"| T{"Qual é a natureza do trabalho?"}
    T -->|"Caminho conhecido e repetível"| PR["Instância de processo"]
    T -->|"Objetivo único com término"| PJ["Projeto"]
    T -->|"Situação evolutiva"| CA["Caso"]
    T -->|"Repete em ciclos"| RT["Rotina"]
    T -->|"Responsabilidade sem término"| PG["Programa contínuo"]
```

## Árvore para decidir se precisamos de outro agente

```mermaid
flowchart TD
    W["Novo fio, caso, projeto ou programa"] --> C{"Existe agente com essa responsabilidade?"}
    C -->|"Não"| P{"A responsabilidade será estável ou recorrente?"}
    P -->|"Não"| H["Humano ou agente superior coordena"]
    P -->|"Sim"| NA["Criar novo agente responsável"]
    C -->|"Sim"| K{"Precisa do conhecimento desse agente?"}
    K -->|"Sim"| A{"Objetivo, regras e permissões são compatíveis?"}
    K -->|"Não"| SP{"Basta habilidade temporária?"}
    A -->|"Sim"| CH["Criar fio ou caso sob o agente existente"]
    A -->|"Não"| ISO["Criar agente separado ou isolado"]
    SP -->|"Sim"| TEMP["Chamar especialista temporário"]
    SP -->|"Não"| ST{"O conhecimento será reutilizado?"}
    ST -->|"Não"| CH
    ST -->|"Sim"| NA
```

## Árvore da próxima ação

```mermaid
flowchart TD
    E["Fio atualizado"] --> Q{"Qual é o próximo impedimento?"}
    Q -->|"Precisamos agir"| A{"Há autorização?"}
    Q -->|"Outra pessoa deve responder"| W["Aguardar e definir prazo"]
    Q -->|"Falta informação"| I{"Onde está a informação?"}
    Q -->|"Depende de data"| D["Agendar reativação"]
    Q -->|"Objetivo atingido"| C["Concluir e registrar aprendizado"]
    Q -->|"Não vale continuar"| X["Cancelar ou arquivar"]
    A -->|"Sim"| EX["Executar e registrar"]
    A -->|"Não"| AP["Preparar e pedir aprovação"]
    I -->|"Na memória"| V["Verificar e utilizar"]
    I -->|"Em sistema ou documento"| B["Buscar e verificar"]
    I -->|"Com outra pessoa"| PE["Perguntar e aguardar"]
    I -->|"Desconhecida"| HU["Pedir orientação humana"]
```

## Pedido de informação

```text
informação solicitada
→ classificar tipo, finalidade e sensibilidade
→ conhecida, verificada, atual e permitida? → responder
→ conhecida, mas não verificada? → confirmar
→ inferida? → confirmar ou responder com ressalva
→ disponível em sistema? → buscar e validar
→ pesquisável externamente? → acionar pesquisador
→ depende de pessoa? → perguntar e aguardar
→ conflitante? → reconciliar fontes
→ restrita? → pedir autorização ou recusar
→ indisponível? → propor alternativa ou encerrar ramo
```

## Referências internas

- [Comunicação](../01-communication-and-events/current-findings.md)
- [Identificação e roteamento](../02-identification-and-routing/current-findings.md)
- [Objetivos e objetos de trabalho](../03-goals-and-work-objects/current-findings.md)
- [Distribuição e coordenação](../04-task-distribution-and-coordination/current-findings.md)
- [Arquitetura dos agentes](../05-agent-architecture/current-findings.md)
- [Persistência](../07-persistence-and-lifecycle/current-findings.md)
- [Memória](../08-memory-and-knowledge/current-findings.md)
- [Governança](../09-governance-authority-and-evaluation/current-findings.md)
