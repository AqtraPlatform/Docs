# Obter modelo de fluxo de trabalho

![](../../assets/images/app-development/get-workflow-model.png)

## Informações gerais
A etapa “Obter Modelo de Fluxo de Trabalho” é usada exclusivamente em fluxos de dados que são chamados de um fluxo de trabalho. Ela permite que você obtenha o modelo e os dados do fluxo de trabalho chamador dentro do fluxo de dados atual.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração  | Opções de Valor | Propósito |
|-----------------------|-------------------|------------|
| Nome da etapa         | -                 | Nome da etapa |
| Validar valores de entrada | true, false       | Indica que os valores de entrada devem ser verificados quanto à correção antes do processamento |

## Casos
- **Integração de Fluxo de Dados e Fluxo de Trabalho**: Permite integrar o fluxo de dados com o fluxo de trabalho, proporcionando acesso ao modelo e aos dados do fluxo de trabalho chamador.

## Exceções
- **Uso Limitado**: A etapa não é destinada ao uso em fluxo de dados de entrada.

## Cenário de aplicação

O componente permite que você crie um fluxo de dados para atualizar um registro no componente de dados de origem. Ele inclui etapas como Obter modelo de fluxo de trabalho para obter o modelo do fluxo de trabalho, Atualizar entrada para atualizar o registro com os parâmetros apropriados definidos e Escrever resposta para outputar o resultado. Este componente pode ser usado para atualizar dados no componente de origem usando fluxos de trabalho e elementos de UI.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1F2ZFQlyMf6ZaxABcoOWib4T8AD8w-75Q/view?usp=sharing)