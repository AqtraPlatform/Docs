# Transform model

![](../../assets/images/app-development/transform-model.png)

## Informações gerais
A etapa “Transform Model” é utilizada para mapear e transformar campos no modelo de dados. Isso envolve a alteração de nomes de campos e a remoção de campos desnecessários do modelo. A etapa cria uma nova cópia do modelo de fluxo de dados, permitindo que você modifique sua estrutura, o que é frequentemente usado para minimizar a resposta como um modelo de dados. Também pode ser utilizado para otimizar o modelo de dados após a realização de várias operações de agrupamento (Group by).

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Mapeamento de campos  | -                | Mapeando e alterando campos no modelo de dados |

## Casos
- **Otimização do Modelo de Dados**: Usado para alterar a estrutura do modelo de dados, incluindo renomear ou excluir campos.

## Exceções
- **Importância do Mapeamento Preciso**: Erros na configuração de “Mapeamento de Campos” podem resultar em alterações indesejadas no modelo de dados.
- **Dependência dos Dados de Origem**: A aplicação correta da etapa requer uma compreensão precisa da estrutura dos dados de origem.

## Cenário de aplicação

Este componente contém um fluxo de dados utilizado para transformação de dados de acordo com regras especificadas. O fluxo de dados inclui etapas como Extrair Coleção e Executar Script, que permitem adicionar novos registros a arrays de dados de clientes.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1buQNdkjcnY8wgIUM9TjjI7KoikEcSmv3/view?usp=sharing)