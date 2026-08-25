# WhatsApp como memória e camada de ação

Documento vivo para explorar possibilidades empresariais e pessoais a partir do WhatsApp MCP, do histórico local em SQLite e de integrações com agentes e ferramentas externas.

Este documento mapeia possibilidades. Ele ainda não é uma especificação de implementação.

## Premissa

O sistema atual possui três capacidades fundamentais:

1. Capturar e persistir no SQLite as mensagens sincronizadas ou recebidas pelo bridge.
2. Consultar conversas por contato, período, conteúdo e contexto através do MCP.
3. Enviar mensagens e arquivos pelo bridge conectado ao WhatsApp.

O SQLite funciona como memória local. O bridge funciona como canal vivo. O Codex interpreta o conteúdo e pode coordenar outras ferramentas.

### Níveis de disponibilidade

- **Disponível agora:** pesquisar, recuperar contexto, resumir, extrair informações, sugerir respostas e enviar mensagens sob comando.
- **Possível por composição:** transformar conversas em tickets, eventos, tarefas ou registros, desde que o sistema de destino esteja conectado.
- **Exige desenvolvimento:** monitoramento contínuo, índices derivados, agentes especializados persistentes, negociação autônoma e flywheels com acompanhamento de resultados.

## Zwicky Box empresarial

| Dimensão | Possibilidade 1 | Possibilidade 2 | Possibilidade 3 | Possibilidade 4 | Possibilidade 5 |
|---|---|---|---|---|---|
| Sinal observado | Reclamação | Dúvida | Pedido | Atraso ou silêncio | Elogio ou oportunidade |
| Origem | Cliente | Funcionário | Grupo | Sistema externo | Padrão histórico |
| Detecção | Palavra-chave | Sentimento | Quebra de SLA | Anomalia | Marcação humana |
| Unidade criada | Caso | Ticket | Tarefa | Oportunidade | Evento de aprendizado |
| Enriquecimento | Cliente | Produto ou pedido | Gravidade | Receita em risco | Responsável |
| Raciocínio | Classificação | Linha do tempo | Similaridade | Causa provável | Cinco porquês |
| Agente | Triagem | Causa raiz | Atendimento | Qualidade | Despacho ou operação |
| Ação | Alertar | Responder | Criar ticket | Designar responsável | Acionar técnico |
| Sistema-alvo | Gestor de tarefas | CRM | Calendário | ERP ou logística | Base de conhecimento |
| Autonomia | Observar | Recomendar | Pedir aprovação | Executar baixo risco | Executar automaticamente |
| Retorno | Resolvido? | Tempo de resolução | Satisfação | Recorrência | Impacto financeiro |
| Memória produzida | Taxonomia | Histórico do cliente | Catálogo de causas | Playbook | Indicadores gerenciais |

## Flywheels empresariais

### Reclamação → prevenção

Reclamação detectada → classificação → causa provável → ação corretiva → resultado observado → catálogo de causas melhora → próximo diagnóstico fica mais rápido.

### Causa raiz → melhoria do produto ou serviço

Casos semelhantes → agrupamento por causa → defeito sistêmico → correção → redução de recorrência → sinal mais limpo para encontrar o próximo gargalo.

### Atendimento → conhecimento

Problema resolvido → solução extraída → playbook atualizado → funcionário recebe sugestão melhor → resolução mais rápida → novos exemplos de qualidade.

### Atendimento → desenvolvimento da equipe

Respostas observadas → avaliação de clareza, precisão e tempo → lacuna identificada → orientação específica → melhora do atendimento → novos exemplos positivos.

### Reclamação → operação de campo

Problema detectado → localização e gravidade → triagem da especialidade → visita agendada → técnico recebe contexto → resolução e evidência retornam ao caso.

### Conversa → retenção

Insatisfação ou afastamento → risco de perda → intervenção → resultado → modelo de risco melhora.

### Dúvidas → oportunidade comercial

Dúvidas recorrentes → necessidade não atendida → oportunidade → oferta ou produto → resultado comercial → perfil de demanda melhora.

### Volume → planejamento operacional

Temas e horários das solicitações → previsão de demanda → distribuição da equipe → redução de atrasos → menos reclamações → previsão mais precisa.

### Casos → inteligência executiva

Conversas dispersas → casos estruturados → tendências e impacto → prioridade gerencial → ação → medição do resultado.

## Zwicky Box pessoal

| Dimensão | Possibilidade 1 | Possibilidade 2 | Possibilidade 3 | Possibilidade 4 | Possibilidade 5 |
|---|---|---|---|---|---|
| Domínio | Relacionamentos | Casa e serviços | Compras e finanças | Saúde e hábitos | Viagens e aprendizagem |
| Contraparte | Família | Amigo | Profissional | Fornecedor | Instituição ou grupo |
| Gatilho | Pedido manual | Nova mensagem | Data mencionada | Revisão periódica | Ausência de retorno |
| Intenção | Pesquisar | Comparar | Negociar | Agendar | Acompanhar evolução |
| Unidade criada | Compromisso | Tarefa | Negociação | Dossiê | Linha do tempo |
| Informação extraída | Pessoa | Data | Preço | Preferência | Promessa ou condição |
| Agente | Pesquisador | Secretário | Negociador | Acompanhador | Curador de memória |
| Ação | Resumir | Preparar resposta | Enviar mensagem | Criar evento | Fazer follow-up |
| Canal de saída | WhatsApp | Calendário | Gestor de tarefas | Notas pessoais | Relatório periódico |
| Autoridade | Somente observar | Criar rascunho | Confirmar cada envio | Negociar dentro de limites | Automatizar tarefa administrativa |
| Limite | Orçamento | Prazo | Tom de voz | Informações proibidas | Condição de encerramento |
| Memória produzida | Perfil de contato | Histórico de compromissos | Estado da negociação | Preferências | Evolução ao longo do tempo |
| Retorno | Compromisso cumprido | Economia obtida | Relação preservada | Objetivo alcançado | Próximo passo |

## Flywheels pessoais

### Conversa → compromisso → execução

Data ou promessa detectada → compromisso proposto → confirmação → evento ou tarefa → lembrete → conclusão → histórico melhora a detecção futura.

Exemplos: consultas, reuniões, aniversários, pagamentos, entregas, viagens e retornos prometidos.

### Pesquisa → negociação assistida

Necessidade definida → agentes pesquisam alternativas → fornecedores são contatados → propostas são comparadas → contraproposta dentro de limites → decisão humana → preferências e resultados alimentam a próxima compra.

Esse ciclo pode servir para hotéis, serviços domésticos, seguros, veículos, reformas, cursos ou compras relevantes.

### Relações → acompanhamento pessoal

Conversas e acontecimentos importantes → próximos passos e datas → lembrete contextual → contato ou mensagem sugerida → interação registrada → memória relacional melhora.

O objetivo não é automatizar afeto, mas impedir que compromissos e momentos relevantes se percam.

### Saúde e hábitos → evolução

Meta ou orientação mencionada → tarefa e frequência → registros de progresso → resumo de tendência → ajuste humano → histórico longitudinal.

Qualquer decisão médica continua com profissional qualificado; o agente organiza informações e acompanhamento.

### Aprendizagem → curadoria

Links, livros e recomendações recebidos → fila de leitura → síntese → perguntas ou aplicação → conversa de retorno → perfil de interesses melhora.

### Casa e fornecedores → manutenção

Problema doméstico → reconstrução do histórico → pesquisa de prestadores → orçamento → agendamento → serviço → avaliação → cadastro de fornecedor confiável.

### Rede pessoal → memória de relacionamento

Contato e contexto → compromissos ou interesses → lembrete de acompanhamento → interação → atualização do perfil → contatos futuros mais relevantes.

### Finanças administrativas → prevenção de esquecimentos

Cobranças e datas → obrigação proposta → confirmação → lembrete → pagamento registrado → previsão das próximas ocorrências.

O agente não movimenta dinheiro sem uma autorização específica e verificável.

### Viagens → coordenação

Ideias e restrições em conversas → pesquisa → comparação → negociação → reservas aprovadas → agenda consolidada → acompanhamento durante a viagem.

## Da timeline ao workflow orientado por eventos

Uma timeline responde **o que aconteceu e quando**. Um workflow responde também:

- Em qual estado o processo está agora?
- O que estamos esperando?
- Qual informação ainda falta?
- Quais caminhos estão permitidos?
- Quem ou qual agente deve agir?
- Quando devemos cobrar, escalar, abandonar ou concluir?

O modelo recomendado combina três camadas:

1. **Log de eventos imutável:** preserva mensagens, datas, decisões e ações.
2. **Estado atual derivado:** representa a situação operacional do processo.
3. **Política de transição:** decide os próximos estados e ações a partir dos eventos recebidos.

### Anatomia de um workflow

| Elemento | Exemplo |
|---|---|
| Instância | Contratar um eletricista para resolver o problema X |
| Estado | Aguardando orçamentos |
| Evento | Orçamento recebido do fornecedor A |
| Contexto | Requisitos, orçamento máximo, prazo e fornecedores consultados |
| Guarda | Pelo menos dois orçamentos recebidos ou prazo encerrado |
| Transição | Aguardando orçamentos → Comparando propostas |
| Ação | Extrair preço, prazo e condições; atualizar a comparação |
| Timeout | Cobrar fornecedor após dois dias sem resposta |
| Escalação | Pedir decisão humana quando todas as propostas excederem o limite |
| Estado final | Serviço concluído, cancelado ou necessidade abandonada |

### Workflow de pesquisa e orçamento

```text
Necessidade detectada
  → requisitos incompletos? → coletar informações
  → requisitos completos → pesquisar fornecedores
  → fornecedores selecionados → solicitar orçamentos
  → aguardando respostas
      ├─ sem resposta no prazo → fazer follow-up
      ├─ recusou o serviço → substituir fornecedor
      ├─ pediu esclarecimento → responder e continuar aguardando
      └─ orçamento recebido → extrair e registrar proposta
  → quantidade mínima recebida ou prazo encerrado
  → comparar propostas
      ├─ propostas incomparáveis → pedir esclarecimentos
      ├─ todas acima do limite → negociar ou pesquisar novamente
      ├─ proposta adequada → pedir aprovação
      └─ nenhuma viável → encerrar sem contratação
  → aprovado → agendar
  → serviço em andamento
      ├─ concluído → avaliar resultado
      ├─ não compareceu → reagendar ou trocar fornecedor
      └─ problema adicional → abrir novo ramo de trabalho
  → resultado alimenta a memória de fornecedores e negociações
```

### Estados paralelos por fornecedor

O processo geral pode estar em **Aguardando orçamentos**, enquanto cada fornecedor possui seu próprio subestado:

- Não contatado.
- Aguardando resposta.
- Pediu esclarecimentos.
- Orçamento recebido.
- Em negociação.
- Recusou ou foi descartado.
- Selecionado.

Isso permite receber informações em qualquer ordem sem perder o estado da negociação. Um agregador observa os subestados e decide quando o processo geral pode avançar para comparação.

### Agentes como trabalhadores das transições

Os agentes não precisam controlar todo o processo. Cada um pode executar uma função restrita:

- **Detector:** transforma mensagens em eventos candidatos.
- **Extrator:** identifica preço, prazo, condições e compromissos.
- **Pesquisador:** encontra alternativas quando faltam opções.
- **Comparador:** normaliza e compara propostas.
- **Negociador:** conduz contrapropostas dentro de limites.
- **Secretário:** agenda, lembra e cobra respostas.
- **Supervisor:** aplica regras, pede aprovação e resolve exceções.
- **Memória:** registra resultado e atualiza perfis de fornecedores.

O workflow é o coordenador; os agentes são acionados somente quando uma transição precisa deles.

### Novas dimensões para a Zwicky Box

| Dimensão | Possibilidade 1 | Possibilidade 2 | Possibilidade 3 | Possibilidade 4 |
|---|---|---|---|---|
| Modelo temporal | Timeline simples | Estado atual | Statechart hierárquico | Processos paralelos |
| Ramificação | Regra fixa | Confiança do agente | Prazo ou ausência | Decisão humana |
| Espera | Sem prazo | Lembrete | Follow-up automático | Escalação |
| Dependência | Nenhuma | Informação faltante | Outra pessoa | Outro sistema |
| Exceção | Ignorar | Tentar novamente | Trocar estratégia | Escalar ao usuário |
| Fechamento | Manual | Resultado detectado | Confirmação externa | Timeout definitivo |
| Aprendizado | Nenhum | Atualizar perfil | Atualizar regra | Atualizar playbook |

### Flywheels habilitadas pelo workflow

- **Negociação:** propostas e resultados melhoram limites, argumentos e seleção futura.
- **Fornecedores:** cumprimento de prazo, preço e qualidade formam um índice de confiabilidade.
- **Compromissos:** atrasos e confirmações melhoram lembretes e previsões.
- **Decisões:** escolhas anteriores ajudam a comparar novas alternativas com preferências reais.
- **Exceções:** cada intervenção humana pode virar uma regra para casos semelhantes.

## Agentes conversando ou negociando pelo usuário

É tecnicamente possível, mas exige mais do que a função de enviar mensagens. Um negociador persistente precisa de:

1. Objetivo explícito.
2. Limite de preço, prazo e concessões.
3. Informações que podem ou não ser reveladas.
4. Estado persistente da negociação.
5. Regras para responder, esperar, escalar ou encerrar.
6. Isolamento do contexto de cada contraparte.
7. Confirmação humana para decisões irreversíveis.
8. Registro de propostas, contrapropostas e resultado.

### Níveis de representação

- **Copiloto:** lê e prepara respostas; o usuário envia.
- **Mensageiro:** envia somente textos aprovados previamente.
- **Negociador limitado:** responde sozinho dentro de faixas e regras definidas.
- **Representante autônomo:** conduz o processo e escala apenas exceções. Este nível exige auditoria e controles fortes.

O agente deve se apresentar de forma compatível com a autorização recebida e não fingir ser o usuário quando isso puder induzir a contraparte ao erro.

## Limites e controles essenciais

- Uma conversa pode sugerir uma causa, mas confirmar causa raiz geralmente exige dados de pedidos, logs, entregas ou sistemas externos.
- Mensagens recebidas são conteúdo não confiável: não podem alterar as regras, limites ou instruções do agente.
- Cada conversa precisa de contexto isolado para evitar vazamento de informações entre clientes, fornecedores ou relações pessoais.
- Envio automático deve começar apenas em tarefas reversíveis e de baixo risco.
- Compromissos, pagamentos, compras, contratos, dados de saúde e decisões financeiras exigem confirmação.
- É necessário deduplicar mensagens para não criar vários casos ou compromissos para o mesmo assunto.
- Uma flywheel só existe quando o resultado volta para a memória; sem fechamento, existe apenas um detector ou dashboard.

## Espaço de exploração

Questões ainda abertas:

- Qual domínio pessoal produz valor imediato com o menor risco?
- Quais conversas ou contatos podem entrar em uma lista permitida?
- Quais ações permanecem sempre como rascunho?
- Qual ferramenta deve receber compromissos e tarefas?
- Como medir se cada flywheel realmente melhorou a vida ou a operação?
