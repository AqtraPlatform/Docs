# Fluxo de Dados

## O que é fluxo de dados? {: #dataflow }

Fluxo de dados, ou data flow, na plataforma é um componente chave que permite aos usuários processar e transformar dados dentro de uma aplicação. Esta é uma ferramenta poderosa para integrar dados, processar eventos e automatizar processos de negócios.

O fluxo de dados é construído na plataforma usando um 'editor visual' do fluxo de dados:

O editor visual de fluxo de dados é um designer intuitivo para criar e gerenciar fluxos de dados. Esta ferramenta permite que os usuários criem sequencialmente um conjunto de Estágios e Passos para implementar scripts complexos de processamento de dados.

- **Adicionar Estágio**: Isso é feito pressionando o ícone "+" no painel de controle do fluxo de dados. Você pode adicionar um número ilimitado de estágios dependendo das necessidades do seu script.
- **Excluir Estágio**: Para excluir um estágio, use o botão "X" no bloco de estágio selecionado.
- **Editar Estágio**: Você pode apenas editar o nome do estágio selecionado.
- **Adicionar Passo**: Um novo passo é adicionado pressionando o botão "ADICIONAR PASSO" no estágio apropriado. Os usuários podem escolher tipos de passo a partir dos grupos de atividades propostos.
- **Excluir Passo**: Para excluir um passo, clique no ícone "X" no bloco de passo selecionado.

## Grupo de Entrada

Componentes para recuperar e importar dados:

- [Passos de Entrada](input-steps.md) - Visão geral dos passos de entrada
- [Obter Valores do Conector](get-values-from-connector.md) - Recuperar dados de conectores
- [Assinar Conector](subscribe-to-connector.md) - Assinar atualizações de dados
- [Obter Modelo de Ação](get-action-model.md) - Recuperar modelo de ação
- [Obter Modelo de Fluxo de Trabalho](get-workflow-model.md) - Recuperar modelo de fluxo de trabalho
- [Obter Modelo Vazio](get-empty-model.md) - Criar modelo de dados vazio
- [Proxy Obter Entrada](proxy-get-entry.md) - Recuperação de entrada proxy
- [Proxy Consultar Entrada](proxy-query-entry.md) - Execução de consulta proxy
- [Obter Modelo Bruto](get-raw-model.md) - Recuperar modelo de dados brutos
- [Importar Arquivo](import-file.md) - Importar dados de arquivos

## Grupo de Transformação de Modelo

Componentes para transformação e processamento de dados:

- [Passos de Transformação de Modelo](model-transformation-steps.md) - Visão geral dos passos de transformação
- [Transformar Modelo](transform-model.md) - Transformar modelos de dados
- [Juntar Modelos](join-modes.md) - Juntar múltiplos modelos de dados
- [Extrair Coleções](extract-collections.md) - Extrair dados de coleções
- [Filtrar Fonte](filter-source.md) - Filtrar fontes de dados
- [Consulta de Referência](lookup-reference.md) - Consulta de referência
- [Executar Script](execute-script.md) - Executar scripts personalizados
- [Consultar Entidade por Filtro](query-entity-by-filter.md) - Consultas baseadas em filtro
- [Selecionar Muitos](select-many.md) - Seleção múltipla
- [Obter Entidade por ID](get-entity-by-id.md) - Recuperar por identificador
- [Carregar Catálogos por Chave](load-catalogs-by-key.md) - Carregar dados de catálogo
- [Distinto](distinct.md) - Obter valores distintos
- [Agrupar Por](group-by.md) - Agrupar dados
- [Calcular Array](calculate-array.md) - Cálculos de array
- [Matemática Simples](simple-math.md) - Operações matemáticas
- [Executar Fluxo de Dados](execute-dataflow.md) - Executar fluxo de dados aninhado
- [Obter Informações do Arquivo](get-file-info.md) - Recuperar informações do arquivo

## Grupo de Contextos de Usuário

Componentes para gerenciamento e autenticação de usuários:

- [Passos de Contextos de Usuário](user-contexts-steps.md) - Visão geral dos passos de contexto de usuário
- [Registrar Contexto para Modelo](register-context-for-model.md) - Registrar contexto de modelo
- [Registrar Usuário Externo](register-external-user.md) - Registro de usuário externo
- [Preparar Chaves Externas](prepare-external-keys.md) - Preparar chaves de autenticação
- [Atribuir Papel de Contexto para Modelo](assign-context-role-for-model.md) - Atribuir papéis
- [Obter Código de Uso Único para Usuário](get-one-time-code-for-user.md) - Gerar OTP
- [Confirmar Código de Uso Único para Usuário](confirm-one-time-code-for-user.md) - Verificar OTP
- [Atualizar ou Criar Informações do Usuário](update-or-create-user-info.md) - Gerenciamento de informações do usuário
- [Obter Informações do Usuário](get-user-info.md) - Recuperar dados do usuário
- [Login com Senha](login-with-password.md) - Autenticação por senha
- [Solicitar Redefinição de Senha do Usuário](reset-user-password-request.md) - Redefinição de senha
- [Confirmar Solicitação de Email do Usuário](confirm-user-email-request.md) - Verificação de email
- [Enviar Notificação com Modelo](send-templated-notification.md) - Notificações baseadas em modelo
- [Enviar Notificação](send-notification.md) - Enviar notificações
- [Remover Papéis Atribuídos para Usuário](remove-assigned-roles-for-user.md) - Remover papéis do usuário

## Grupo de Saída

Componentes para saída de dados e ações:

- [Passos de Saída](output-steps.md) - Visão geral dos passos de saída
- [Armazenar Entrada via Barramento](store-entry-over-bus.md) - Armazenar dados via barramento de mensagens
- [Atualizar Entrada](update-entry.md) - Atualizar entradas de dados
- [Atualização de Entrada Diferida](deferred-update-entry.md) - Atualizações diferidas
- [Aplicar Operações de Atualização Diferida](apply-deferred-update-operations.md) - Aplicar operações diferidas
- [Executar Chamada de API](execute-api-call.md) - Chamadas de API externas
- [Escrever Resposta](write-response.md) - Escrever dados de resposta
- [Ação de Formulário](form-action.md) - Ações de envio de formulário
- [Executar Fluxo de Trabalho](execute-workflow.md) - Executar fluxo de trabalho
- [Exportar para Arquivo](export-to-file.md) - Exportar dados para arquivos
- [Renderizar Modelo](render-template.md) - Renderização de modelo