# Data Grid

![](../../assets/images/app-development/data-grid.png)

## Informações gerais
Data Grid é um poderoso componente de UI projetado para exibir e interagir com grandes quantidades de dados em forma tabular. Este componente é ideal para apresentar dados em linhas e colunas, além de fornecer funcionalidades de ordenação e filtragem.

## Parâmetros
**Propriedades do Componente:**

| Grupo de Configurações | Campo de Configuração | Opções de Valor        | Propósito                          |
|------------------------|-----------------------|-------------------------|-------------------------------------|
| (Configurações globais)        | Nome                  | -                       | Nome do Componente de UI no sistema   |
|                        | Colunas               | -                       | Definindo colunas e suas propriedades   |
|                        | Componente            | Multiseleção de Catálogo | Contém uma lista de todos os Componentes |
|                        | Filtros estáticos     | Botão                  | Usado para especificar filtros estáticos |
|                        | Filtros dinâmicos     | Botão                  | A propriedade é usada para especificar filtros dinâmicos |
|                        | Tamanho da página     | -                       | Tamanho da página                     |
|                        | Recarregamento manual  | -                       | Recarregamento manual de dados          |
|                        | Modo de seleção       | nenhum, único, múltiplo, caixa de seleção | Modo de seleção de itens          |
|                        | ID de automação       | -                       | ID para automação     |
| Eventos                | Ao carregar fonte de dados | -                   | Evento de carregamento da fonte de dados |
|                        | Ao selecionar linhas  | -                       | Evento de seleção de linha |
|                        | Ao carregar           | -                       | Evento de carregamento do componente |
|                        | Ao mudar tabela       | -                       | Evento de mudança de tabela |
|                        | Ao mudar cabeçalho    | -                       | Evento de mudança de cabeçalho |
|                        | Ao mudar linha        | -                       | Evento de mudança de linha |
|                        | Ao mudar célula       | -                       | Evento de mudança de célula |

**Propriedades CSS:**

| Grupo de Configurações | Campo de Configuração | Opções de Valor        | Propósito                          |
|------------------------|-----------------------|-------------------------|-------------------------------------|
| Layout                 | Largura               | -                       | Largura do componente                   |
|                        | Altura                | -                       | Altura do componente                   |
|                        | Margem                | -                       | Preenchimento externo                      |
|                        | Preenchimento         | -                       | Preenchimento interno                   |
|                        | Visível               | -                       | Visibilidade do componente                |
|                        | Oculto                | -                       | Ocultando um Componente                  |
| Aparência              | Raio de Canto         | -                       | Raio do canto                   |
|                        | Espessura da Borda    | -                       | Espessura da borda                       |
| Pincel                 | Fundo                 | -                       | Cor de fundo                           |
|                        | Pincel da Borda       | -                       | Cor da borda                          |

**Modelo de Configuração do DataGrid**

As seguintes configurações são usadas para modificar as colunas do componente de UI DataGrid: 

| Campo de Configuração | Opções de Valor                           | Propósito                                              |
|-----------------------|-------------------------------------------|---------------------------------------------------------|
| Valor de tradução     | -                                         | Cabeçalho da coluna                                       |
| Mostrar cabeçalho     | verdadeiro, falso                         | Esta propriedade permite personalizar a exibição do cabeçalho da coluna |
| Ordenável             | verdadeiro, falso                         | A propriedade permite configurar a capacidade de ordenar a tabela pela coluna selecionada |
| Filtrável             | verdadeiro, falso                         | Esta propriedade permite configurar a capacidade de filtrar a tabela pela coluna selecionada |
| Visível               | verdadeiro, falso                         | A propriedade determina a visibilidade da coluna                   |
| Texto simples         | verdadeiro, falso                         | Propriedade para exibir uma coluna como texto simples    |
| Largura               | -                                         | Largura da coluna na tabela                                |
| Formato de exibição   | -                                         | Formato de exibição dos dados da coluna                       |
| Ícone                 | Disponível apenas para Editar registro, Abrir aplicativo | Uma propriedade que contém uma seleção de ícones disponíveis         |
| Tipo de comando       | Abrir aplicativo, Editar registro        | A propriedade permite selecionar a ação que será realizada ao clicar na coluna |
| Adicionar campo       | Botão                                     | A propriedade permite adicionar campos para saída na coluna   |

## Casos
- **Exibição de Dados**: Ideal para exibir dados de forma tabular fácil de entender.
- **Painéis Administrativos**: Amplamente utilizado em interfaces de gerenciamento para visualização e edição de dados.
- **Aplicações de Análise**: Permite analisar e classificar grandes quantidades de informações.

## Exceções
- **Visualização Limitada**: Data Grid não é adequado para visualizações de dados complexas, como gráficos ou tabelas.
- **Processamento de Dados**: O componente é projetado para exibir dados, não para processar ou calcular dados.