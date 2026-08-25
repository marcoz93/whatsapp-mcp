# The Architecture of Complexity

## Estado desta nota

Esta é uma nota de fonte para o processo de design. Ela registra os conceitos de Herbert A. Simon e explicita nossa derivação provisória sobre a ordem de construção da arquitetura. Não representa uma arquitetura aprovada.

## Fonte primária

Herbert A. Simon. **The Architecture of Complexity**. *Proceedings of the American Philosophical Society*, volume 106, número 6, 1962, páginas 467-482.

- [Cópia local preservada](simon-1962-the-architecture-of-complexity.pdf)
- [Cópia disponibilizada pela Carnegie Mellon](https://www.andrew.cmu.edu/course/15-440/assets/READINGS/simon-architecture-of-complexity-1962.pdf)
- [Registro no arquivo institucional de Herbert Simon](https://digitalcollections.library.cmu.edu/search?purl=http%3A%2F%2Fdoi.library.cmu.edu%2F10.1184%2Fpmc%2Fsimon%2Fbox00064%2Ffld04924%2Fbdl0001%2Fdoc0001)

A cópia local possui 16 páginas, 2.594.390 bytes e SHA-256 `18500628dca4f5b27a15e13dbc3ac2559e38beb60355f102af32b4dfa7615d5a`.

## Pergunta que esta fonte abre para o projeto

Antes de desenhar agentes, equipes ou workflows, quais formas intermediárias precisam ser estáveis para permitir que o restante do sistema seja construído, interrompido, retomado e ampliado sem colapsar?

## Conceitos de Simon

### Complexidade organizada

Um sistema complexo possui muitas partes que interagem de maneira não simples. Conhecer as partes e as regras de interação não torna trivial inferir o comportamento do todo.

### Hierarquia como composição

Hierarquia significa uma estrutura de subsistemas dentro de subsistemas até um nível tratado como elementar. Não significa necessariamente cadeia de autoridade. A unidade considerada elementar depende do propósito da análise.

### Fronteiras pela intensidade das interações

Em sistemas sociais, agrupamentos podem ser identificados pela densidade das interações: as relações internas tendem a ser mais fortes ou frequentes que as externas. Distância física e canal não determinam sozinhos a fronteira de um subsistema.

### Span

O span é o número de subsistemas diretamente contidos em outro sistema. Hierarquias muito planas têm span largo; hierarquias mais profundas introduzem níveis intermediários. O paper não estabelece um span universalmente correto.

### Formas intermediárias estáveis

Na parábola de Hora e Tempus, os dois constroem relógios com aproximadamente mil peças. Tempus monta o relógio como uma sequência única e perde todo o trabalho parcial quando é interrompido. Hora produz subconjuntos estáveis de cerca de dez peças e combina esses subconjuntos em níveis sucessivos. Uma interrupção destrói apenas a montagem local.

A tese é que sistemas complexos podem surgir e evoluir muito mais rapidamente quando existem formas intermediárias estáveis que se tornam blocos para novas construções.

### Quase decomponibilidade

Os subsistemas não são completamente independentes. Em um sistema quase decomponível:

1. no curto prazo, o comportamento de cada subsistema é aproximadamente independente dos demais;
2. no longo prazo, o comportamento de um subsistema depende dos outros principalmente por propriedades agregadas.

Isso normalmente ocorre quando as interações internas são mais fortes que as interações entre subsistemas.

### Separação de escalas de tempo

Dinâmicas rápidas tendem a ocorrer dentro dos componentes; dinâmicas mais lentas aparecem nas relações entre componentes e nos níveis superiores. Um acontecimento local não precisa reconfigurar imediatamente a organização inteira.

### Compreensão e representação

Hierarquias quase decomponíveis permitem descrever sistemas complexos sem enumerar todas as interações entre suas partes elementares. Os níveis superiores podem operar com propriedades agregadas dos inferiores.

Simon também diferencia descrições de estado e de processo. Uma descrição de processo representa as regras que geram a evolução do sistema e pode ser muito mais econômica que a enumeração de todos os estados observados.

### Redundância e descrição econômica

Sistemas hierárquicos podem ser descritos de forma compacta porque reutilizam poucos tipos de subsistema, apresentam muitas conexões fracas ou ausentes e permitem recodificar sequências em regras geradoras.

## Derivação provisória para nosso design time

Esta seção é nossa interpretação da fonte.

A arquitetura não deveria começar pelo agente, pelo router ou pelo WhatsApp. Ela deveria começar pelas estruturas que permanecem válidas quando executores, modelos e canais são substituídos.

Uma possível ordem de dependência é:

1. **identidade, tempo, acontecimentos e proveniência**;
2. **unidades estáveis de trabalho e contexto**;
3. **estado, memória e ciclo de vida locais**;
4. **interfaces, compromissos e autoridade**;
5. **composição em casos, projetos, equipes e organizações**;
6. **agentes, roteamento e protocolos**;
7. **canais, interfaces e ferramentas**.

O agente passa a ser um executor sobre estruturas duráveis, não o recipiente exclusivo de identidade, memória, estado ou responsabilidade.

## Candidatos a formas intermediárias estáveis

Ainda precisamos verificar quais destas entidades realmente sustentam a composição:

- fio;
- objetivo;
- caso;
- compromisso;
- missão;
- projeto;
- rotina;
- programa;
- equipe;
- organização.

Uma entidade não se torna estável apenas porque recebeu um nome. Ela precisa possuir identidade, limites, estado preservável, ciclo de vida e interfaces explícitas.

## Teste de estabilidade estrutural

Uma candidata é uma boa forma intermediária se:

1. pode ser pausada e retomada sem reconstrução global;
2. preserva identidade, estado e histórico;
3. pode trocar de agente executor;
4. consegue operar localmente por algum tempo;
5. expõe somente o necessário aos outros subsistemas;
6. pode ser combinada em uma unidade maior;
7. contém falhas e mudanças internas;
8. oferece um estado agregado sem copiar toda sua memória.

## Relação com outras fontes

| Fonte | Contribuição complementar |
|---|---|
| [Gaia](../gaia/) | Define organização, papéis, responsabilidades, permissões, atividades e protocolos |
| [Singh](../commitments-in-multiagent-systems/) | Distingue compromissos internos de compromissos sociais entre unidades autônomas |
| Simon | Oferece o princípio de composição hierárquica, estabilidade intermediária e quase decomponibilidade |

## Relação com nossos eixos

| Conceito | Eixos mais diretamente envolvidos |
|---|---|
| Fronteiras por interação | [Identificação e roteamento](../../02-identification-and-routing/) e [equipes](../../06-teams-and-organization/) |
| Formas intermediárias estáveis | [Objetivos e objetos de trabalho](../../03-goals-and-work-objects/) e [persistência](../../07-persistence-and-lifecycle/) |
| Quase decomponibilidade | [Distribuição e coordenação](../../04-task-distribution-and-coordination/) e [arquitetura dos agentes](../../05-agent-architecture/) |
| Estado e descrição de processo | [Persistência](../../07-persistence-and-lifecycle/) e [memória](../../08-memory-and-knowledge/) |
| Interfaces e agregação | [Comunicação](../../01-communication-and-events/) e [governança](../../09-governance-authority-and-evaluation/) |

## Perguntas ainda abertas

- Quais são nossas menores unidades estáveis, e para qual perspectiva?
- Que medida de intensidade de interação deve determinar suas fronteiras?
- Qual estado interno pode permanecer oculto e qual agregado deve subir?
- Quais unidades podem operar de forma aproximadamente independente no curto prazo?
- Que mudanças locais exigem propagação imediata e quais podem esperar agregação?
- Qual é o span administrável em cada nível?
- Como detectar uma decomposição ruim, na qual interações externas são tão fortes quanto as internas?
- Quais estruturas devem existir antes de qualquer agente poder ser criado?

## Limite da aplicação

Simon fornece princípios para compreender, construir e descrever sistemas complexos; ele não escolhe nossa ontologia, nossos níveis ou nossas fronteiras. Usar a linguagem de hierarquia sem medir dependências reais apenas esconderia a complexidade em novas caixas.
