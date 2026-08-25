# Descobertas atuais: identificação e roteamento

## Conversa não é fio

A conversa é o local onde mensagens aparecem. Um fio é a continuidade semântica de um assunto, objetivo, problema, decisão ou compromisso.

Uma conversa pode conter vários fios intercalados:

```text
Conversa com a esposa
├── fio: consertar o carro
└── fio: compras da casa
```

Um mesmo fio também pode atravessar várias conversas, pessoas ou canais.

## As duas decisões do router

O router precisa responder, separadamente:

1. A qual fio este acontecimento pertence?
2. Qual projeto, programa, caso ou agente é responsável pelo fio?

Ele não precisa resolver o problema; precisa encaminhá-lo com contexto e grau de confiança.

## Operações possíveis

Para cada acontecimento, o router pode:

- Vincular a um fio existente.
- Reabrir um fio encerrado quando o mesmo problema retornou.
- Criar nova ocorrência relacionada a um fio anterior.
- Criar um novo fio.
- Dividir uma mensagem entre vários fios.
- Vincular o mesmo acontecimento a mais de um fio.
- Manter numa caixa de identificação quando houver ambiguidade.
- Ignorar como conteúdo sem relevância operacional.

## Critérios candidatos

- Pessoas e grupos envolvidos.
- Tema e entidades mencionadas.
- Objetivo ou problema afetado.
- Proximidade temporal.
- Estado atual dos fios candidatos.
- Compromissos e perguntas ainda abertos.
- Relações com mensagens anteriores.

## Confiança e correção

| Situação | Tratamento provisório |
|---|---|
| Correspondência clara | Vincular automaticamente |
| Correspondência provável | Vincular e registrar confiança |
| Duas alternativas plausíveis | Sugerir opções |
| Vários fios reais | Vincular ou dividir |
| Nenhum candidato | Criar fio ou pedir classificação |
| Erro posterior | Mover, desvincular ou unir sem perder a mensagem original |

## Fronteira

Roteamento termina quando o acontecimento foi associado ao contexto correto. Distribuir trabalho é responsabilidade de [distribuição e coordenação](../04-task-distribution-and-coordination/current-findings.md).
