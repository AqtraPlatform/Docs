# Fluxo de Trabalho

## O que é fluxo de trabalho? {: #workflow }

Fluxo de trabalho é um mecanismo para gerenciar estados e tarefas em vários scripts de componentes na plataforma. Ele permite organizar a execução sequencial de tarefas, mantendo estados e proporcionando a capacidade de reiniciar em caso de falha.

### Como criar um fluxo de trabalho?

1. **Abrir Toolbox**: Abra o menu Toolbox na janela de componentes e vá para a aba Flows.
2. **Adicionar Fluxo de Trabalho**: Clique no ícone de Fluxo de Trabalho e arraste-o para o espaço de trabalho. Um novo fluxo de trabalho aparecerá para ser configurado.

Usando o construtor visual de Fluxo de Trabalho, você pode configurar um script de fluxo de trabalho:

- **Adicionar Estágios e Passos**: O editor permite adicionar Estágios e Passos que formam a lógica do fluxo de trabalho.
- **Configuração de Sequência**: Os scripts são executados de cima para baixo e da esquerda para a direita, permitindo criar um fluxo consistente de tarefas.

### Parâmetros do Fluxo de Trabalho

- **Nome do fluxo de trabalho**: O nome usado para identificar o fluxo de trabalho no componente.
- **Restringir Acesso**: Quando definido como "Sim", cria um contexto de segurança para o fluxo de trabalho.

### Editando Estágios e Passos do Fluxo de Trabalho

- **Adicionar Estágios**: Usando o botão "+", você pode adicionar novos estágios.
- **Excluir Estágios**: O botão "X" permite excluir estágios desnecessários.
- **Editar Estágios**: Apenas o nome do estágio pode ser alterado.
- **Adicionar e Excluir Passos**: Passos podem ser adicionados e removidos dentro dos estágios, definindo ações específicas do fluxo de trabalho.

## Grupo de Notificações

Componentes para enviar notificações e confirmações:

- [Passos de Notificações](notifications-steps.md) - Visão geral dos passos de notificação
- [Enviar Notificação](send-notification.md) - Enviar notificações para usuários
- [Enviar Notificação Modelada](send-templated-notification.md) - Enviar notificações baseadas em modelo
- [Obter Confirmação do Usuário](get-user-confirmation.md) - Solicitar confirmação do usuário

## Grupo de Integrações

Componentes para integrar com outros sistemas:

- [Passos de Integrações](integrations-steps.md) - Visão geral dos passos de integração
- [Executar Fluxo de Dados](execute-data-flow.md) - Executar fluxo de dados a partir do fluxo de trabalho

## Grupo Comum

Operações comuns de fluxo de trabalho:

- [Passos Comuns](common-steps.md) - Visão geral dos passos comuns
- [Atualizar Modelo](update-model.md) - Atualizar modelo de dados
- [Finalizar](finish.md) - Completar a execução do fluxo de trabalho
- [Atualizar Campo do Modelo](update-model-field.md) - Atualizar campo específico do modelo
- [Resetar para Rascunho](reset-to-draft.md) - Resetar fluxo de trabalho para o estado de rascunho

## Grupo de Condições

Lógica condicional e ramificação:

- [Passos de Condições](conditions-steps.md) - Visão geral dos passos de condição
- [Caso Switch](switch-case.md) - Ramificação switch-case
- [Condição If](if-condition.md) - Ramificação condicional