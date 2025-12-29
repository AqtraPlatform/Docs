# Carregar catálogos por chave

![](../../assets/images/app-development/load-catalogs-by-key.png)

## Informações gerais
A etapa “Carregar Catálogos por Chave” funciona de maneira semelhante à etapa “Obter Entidade por ID”, mas em vez de exigir um ID de componente específico, ela identifica automaticamente qualquer campo do tipo Catálogo no modelo de dados. Dependendo da escolha do usuário, a etapa recupera a entrada completa vinculada ao campo do tipo Catálogo selecionado. Assim, permite obter informações completas de qualquer link nos dados sem precisar especificar um ID específico.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |

## Casos
- **Identificação Automática e Download dos Dados Vinculados**: Usado para identificar e carregar automaticamente dados vinculados a campos de Catálogo.
- **Extração de Dados Flexível**: Adequado para scripts que requerem flexibilidade na seleção e extração de dados de vários componentes relacionados.

## Exceções
- **Carga Excessiva ao Trabalhar com um Grande Número de Catálogos**: Se houver um grande número de catálogos sendo abertos, pode levar mais tempo para processá-los.
- **Substituição Injustificada da etapa “Obter entidade por ID” pela etapa “Carregar catálogos por chave”**: Se o número de catálogos vinculados não exceder alguns, é melhor usar a etapa “Obter entidade por ID” para melhor desempenho.

## Cenário de aplicação

Este componente permite criar um fluxo de dados começando pela obtenção de um modelo de dados vazio. Em seguida, é usado para recuperar o identificador do registro com catálogos, após o qual carrega esses catálogos e exibe seus dados no frontend.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1_GImBJ3UCDo-T1dL6c85-wWgcUfpJIz3/view?usp=sharing).