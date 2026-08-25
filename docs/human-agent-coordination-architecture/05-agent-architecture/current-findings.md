# Descobertas atuais: arquitetura dos agentes

## Distinções fundamentais

```text
modelo ≠ habilidade ≠ papel ≠ agente ≠ execução
```

- **Modelo:** mecanismo de raciocínio.
- **Habilidade:** capacidade reutilizável.
- **Papel:** comportamento e responsabilidade esperados na organização.
- **Agente:** identidade responsável, com objetivos, autoridade e memória acessível.
- **Execução:** período em que um agente é ativado para trabalhar.

## Composição provisória de um agente

```text
identidade
+ responsabilidade
+ objetivos
+ autoridade
+ memória permitida
+ capacidades e ferramentas
+ relações organizacionais
+ prestação de contas
```

O agente pode acordar por evento, prazo, rotina ou chamada humana, trabalhar e voltar a ficar inativo. Sua continuidade não depende de manter o modelo executando permanentemente.

## Funções já identificadas

- Router.
- Coordenador.
- Detector ou extrator.
- Pesquisador.
- Comparador.
- Negociador.
- Secretário.
- Executor.
- Supervisor.
- Auditor.

Essas funções podem ser papéis exercidos por um mesmo agente ou por agentes diferentes.

## Critério para criar outro agente

Criar outro agente quando surgir uma responsabilidade estável que precise de memória, regras, permissões ou avaliação próprias.

```text
apenas outro assunto
→ novo fio

outro resultado dentro da mesma responsabilidade
→ novo caso ou projeto sob o mesmo agente

habilidade pontual
→ especialista temporário

responsabilidade contínua com memória reutilizável
→ novo agente

informações ou permissões incompatíveis
→ agente separado ou isolado
```

## Conhecimento não basta para definir identidade

Agentes diferentes podem consultar uma base comum. A responsabilidade define a identidade; o conhecimento define a memória à qual o agente tem acesso.
