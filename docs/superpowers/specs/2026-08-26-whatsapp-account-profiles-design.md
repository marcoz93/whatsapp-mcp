# Perfis isolados de contas do WhatsApp

## Objetivo

Permitir manter mais de uma conta do WhatsApp preparada neste computador, com apenas uma conectada ao bridge e exposta ao agente por vez, sem misturar sessões, mensagens, mídias ou envios.

## Decisão

Cada número será um perfil físico independente. Um seletor determinará o único perfil ativo; bridge e MCP usarão a mesma seleção.

```text
whatsapp-bridge/profiles/
├── empresa/
│   ├── whatsapp.db
│   ├── messages.db
│   └── media/
└── pessoal/
    ├── whatsapp.db
    ├── messages.db
    └── media/
```

Não haverá merge nem diff entre os bancos. Cada perfil preserva sua própria verdade e volta a sincronizar quando for reativado.

## Seleção do perfil

O perfil será escolhido explicitamente por um seletor, que gravará o nome em um único arquivo local `.active-profile`. Bridge Go e servidor MCP Python lerão esse mesmo arquivo; não haverá duas configurações independentes que possam divergir.

Regras:

- apenas um bridge pode usar a porta local `8080`;
- a troca falha se o bridge anterior ainda estiver ativo;
- bridge e MCP são reiniciados depois da troca, evitando conexões antigas com SQLite;
- um perfil desconhecido nunca é criado silenciosamente;
- o perfil atual fica visível por nome e identidade da conta conectada.
- `.active-profile`, bancos, sessões e mídias ficam ignorados pelo Git.

O comportamento existente sem perfil explícito será preservado apenas durante a migração do banco atual.

## Isolamento para o agente

O agente não recebe acesso aos bancos inativos. O servidor MCP abre somente o `messages.db` do perfil selecionado e envia exclusivamente pelo bridge que usa a mesma seleção.

Para evitar confusão causada pelo contexto da própria conversa:

- o MCP expõe a identidade do perfil ativo;
- resultados de consulta identificam o perfil de origem;
- ações de envio recebem o perfil esperado;
- o servidor rejeita o envio se o perfil esperado não coincidir com o ativo;
- a mensagem de erro informa qual perfil está ativo, sem tentar escolher automaticamente.

Assim, uma instrução antiga sobre a conta empresarial não consegue provocar silenciosamente um envio pela conta pessoal.

## Troca de conta

O fluxo operacional será:

1. parar bridge e MCP;
2. selecionar um perfil existente ou criar deliberadamente um perfil vazio;
3. iniciar o bridge;
4. escanear o QR somente se o perfil ainda não tiver sessão;
5. confirmar a identidade conectada;
6. iniciar o MCP apontando para o mesmo perfil.

A conta atualmente conectada será migrada para o primeiro perfil antes da criação do segundo. A pasta original será preservada até a cópia ser verificada.

## Limite conhecido

Uma conta inativa não será monitorada em tempo real. Ao ser reativada, o WhatsApp pode entregar mensagens pendentes e sincronizar histórico, mas este modo não deve ser usado quando a captura contínua e completa de ambas as contas for requisito. Nesse caso, o próximo desenho será executar dois bridges simultâneos, cada um com porta e MCP próprios.

## Verificação

A implementação será considerada correta quando:

- cada perfil conservar sessão, mensagens e mídias separadas;
- alternar o perfil não alterar o banco inativo;
- o bridge e o MCP recusarem configurações divergentes;
- leituras mostrarem a identidade ativa;
- envios com perfil incorreto forem recusados;
- retornar ao primeiro perfil restaurar suas conversas sem novo QR;
- o fluxo atual de uma única conta continuar funcionando durante a migração.

## Fora de escopo

- executar duas contas simultaneamente;
- pesquisar as duas contas em uma única consulta;
- unir ou deduplicar históricos;
- escolher automaticamente por qual número enviar;
- construir uma interface gráfica para alternar perfis.
