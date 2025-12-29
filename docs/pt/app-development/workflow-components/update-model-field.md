# Atualizar campo do modelo

![](../../assets/images/app-development/update-model-field.png)

## Informações gerais
A etapa “Atualizar Campo do Modelo” dentro do fluxo de trabalho é usada para atualizar um campo específico no modelo. Esta etapa permite que você altere os valores de campos individuais no modelo de dados, o que é particularmente útil para a gestão dinâmica de dados durante a execução do fluxo de trabalho.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Propósito |
|-----------------------|-----------|
| Nome da etapa         | Nome da etapa “Atualizar Campo do Modelo” |
| Campo do modelo       | Campo do modelo que você deseja atualizar |
| Valor                 | Valor para o qual o campo será atualizado |
| Campo de origem       | Campo de origem cujo valor será usado para a atualização |

## Casos
- **Atualização de Dados Dinâmicos**: Usado para alterar valores no modelo com base em dados gerados durante o fluxo de trabalho, como atualizar o status de uma tarefa ou mudar opções de configuração.

## Exceções
- **Precisão e Relevância dos Dados**: Certifique-se de que os dados atualizados sejam precisos e estejam atualizados para evitar consequências indesejáveis.
- **Compreensão do Impacto das Mudanças**: É importante entender o impacto da atualização de um campo no modelo e na lógica geral do fluxo de trabalho, especialmente em sistemas complexos com dependências interligadas.