# Referências de produtos e implementações

Esta pasta registra produtos, interfaces e implementações contemporâneas que podem informar o design. Eles servem como evidência de possibilidades e escolhas, não como definições da nossa arquitetura.

## PromptQL

### Fonte

- [Site](https://promptql.io/)
- [Aplicativo multiplayer](https://promptql.io/multiplayer-cowork)
- [Produto](https://promptql.io/product)
- [Arquitetura](https://promptql.io/why-promptql-works)
- [Documentação](https://promptql.io/en/docs)
- [Multiplayer AI SDK](https://promptql.io/multiplayer-ai-sdk)
- [Segurança](https://promptql.io/security)
- [PromptQL Tag](https://promptql.io/tag)
- [I don't keep a TODO list anymore](https://promptql.io/blog/i-dont-keep-a-todo-list-anymore)

Inspeção realizada em 25 de agosto de 2026. O produto e o SDK podem mudar; afirmações abaixo se limitam ao material público observado nessa data.

### O que é uma thread no modelo apresentado

PromptQL trata a thread como uma **unidade de trabalho persistente e compartilhada**, não apenas como uma sequência de mensagens.

Dentro dela:

- várias pessoas e o agente colaboram em tempo real;
- discussão e execução permanecem juntas;
- participantes podem chamar especialistas por menção sem reiniciar o trabalho;
- o agente continua executando enquanto humanos refinam a resposta;
- contexto e rastros de decisão são preservados;
- resultados podem virar dashboards, aplicativos, apresentações e outros artefatos;
- a unidade pode permanecer ativa na nuvem e acordar por agenda ou evento externo;
- novas execuções escrevem o estado atualizado de volta na thread.

O depoimento publicado pela empresa descreve a thread como “trabalho já em movimento”, em oposição a uma tarefa parada em uma fila. Isso sugere uma unidade que combina contexto, processo e continuidade.

### Estruturas relacionadas

| Estrutura observada | Função aparente |
|---|---|
| Thread | Contêiner local de discussão, execução, participantes, estado e resultados |
| Shared wiki | Memória organizacional reutilizável entre threads |
| Context update | Transformação de uma correção ou regra surgida no trabalho em conhecimento durável |
| Scope | Limite de visibilidade para contexto pessoal, interno, confidencial ou de cliente |
| User permissions | Autoridade preservada por participante; ações executadas como uma pessoa real |
| Agent | Participante executor dentro do espaço compartilhado |
| Heartbeat | Persistência operacional que reativa a thread por agenda, webhook, e-mail, ticket ou alerta |
| Artifact | Resultado executável ou consultável produzido a partir da thread |
| Channel | Espaço aberto, privado ou restrito que agrupa threads e participantes |

### Duas camadas de memória

O produto separa implicitamente:

1. **contexto da thread**, específico do trabalho em andamento;
2. **wiki compartilhada**, onde definições, regras, exceções e aprendizados passam a servir outras threads.

O conhecimento não sobe automaticamente sem controle: o produto apresenta sugestões de atualização, revisão humana, histórico, autoria, reversão e escopos.

Essa separação é diretamente relevante para nosso eixo de memória: uma correção local não deve contaminar toda a organização sem validação, mas um aprendizado confirmado também não deve permanecer preso à conversa original.

### Persistência e reativação

O chamado heartbeat mostra uma distinção útil entre:

- a identidade persistente da thread;
- as execuções temporárias do agente;
- os eventos que despertam uma nova execução;
- o estado gravado novamente ao final.

Isso coincide com nossa distinção entre agente persistente, execução por ativação e unidade de trabalho com ciclo de vida próprio.

### Governança

O material público apresenta:

- contexto governado por escopos;
- permissões reais de cada participante;
- acesso intermediado a dados e ferramentas;
- execução em sandbox;
- versionamento, autoria, auditoria e reversão de conhecimento;
- threads privadas ou canais restritos para trabalho sensível.

Portanto, a thread não aparece como um recipiente com acesso irrestrito. Participação, memória e ação mantêm limites próprios.

### O que podemos aproveitar

1. **Thread como contêiner de trabalho em movimento**, e não como sinônimo de chat.
2. **Humanos e agentes na mesma unidade**, sem handoff para um sistema de tickets separado.
3. **Discussão, execução, estado e artefatos juntos**, preservando o rastro de decisão.
4. **Especialistas chamados para a thread**, sem criar um agente permanente para cada participante.
5. **Identidade persistente com execuções episódicas**, ativadas por pessoas, agendas ou eventos.
6. **Memória local e memória compartilhada separadas**, com promoção governada de conhecimento.
7. **Artefatos como estado operacional**, não apenas como anexos da conversa.
8. **Permissões por pessoa e escopo**, em vez de uma autoridade única herdada pelo agente.

### O que PromptQL não demonstra resolver

O material público inspecionado não formaliza:

- descoberta automática de vários fios semânticos dentro da mesma conversa;
- roteamento de mensagens externas para a thread correta;
- critérios para dividir ou fundir threads;
- diferença formal entre thread, caso, projeto, missão e rotina;
- compromissos sociais, devedor, credor e condições de satisfação;
- hierarquia recursiva de threads ou composição explícita em programas;
- statecharts gerais para ciclos de vida diferentes;
- ontologia pública completa da thread.

PromptQL parece partir de uma thread já criada ou explicitamente escolhida. Nosso problema anterior começa um nível antes: identificar a que unidade de trabalho cada acontecimento pertence.

### Síntese comparativa

```text
PromptQL observado
evento ou pessoa → thread explícita → colaboração e execução → estado e artefatos
                                           ↓
                                   wiki compartilhada

Nosso problema ampliado
comunicação multicanal → identificação e roteamento → unidade de trabalho
                                                    → colaboração e execução
                                                    → memória governada
```

### Hipótese provisória

PromptQL oferece uma referência forte para a **anatomia interna e a experiência de uso de uma thread**. Ele não substitui nosso router nem resolve sozinho a ontologia que determina quando uma thread nasce, se divide, se combina ou termina.

A thread candidata do nosso sistema pode precisar conter, no mínimo:

- identidade;
- propósito ou objetivo associado;
- participantes humanos e agentes;
- contexto local;
- estado e ciclo de vida;
- acontecimentos e decisões;
- compromissos e próximas ações;
- artefatos;
- gatilhos de reativação;
- escopo de acesso;
- relações com unidades maiores e menores.

Essa lista permanece como hipótese de design, não como esquema aprovado.
