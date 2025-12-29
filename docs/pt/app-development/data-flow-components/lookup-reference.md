# Referência de Consulta

![](../../assets/images/app-development/lookup-reference.png)

## Informações Gerais
O passo “Referência de Consulta” é utilizado para buscar referências a instâncias de componentes por chaves externas. Este processo requer que pelo menos uma propriedade com a flag “Chave Primária” esteja configurada no componente a ser pesquisado.

A busca é realizada por esta propriedade, e o resultado da busca na forma de Id (inteiro) do registro encontrado será gravado na variável especificada no “Nome do Campo.” Se nenhuma instância de um componente com tal chave for encontrada, a variável será nula.

## Parâmetros
**Configurações do Passo:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome do passo         | -                | Nome do passo |
| Passo de origem       | -                | Selecionando o passo anterior |
| Componente            | -                | Componente que está sendo pesquisado |
| Nome do campo         | -                | Nome do campo onde o resultado da busca será gravado |

## Casos
- **Busca por Chave Primária**: Usado para determinar a disponibilidade e identificar instâncias de componentes por identificadores únicos.
- **Vinculação de Dados de Componentes**: Adequado para scripts onde você deseja vincular dados de diferentes componentes com base em chaves únicas.

## Exceções
- **Requisito de Chave Primária**: O componente deve ter uma chave primária configurada para garantir uma busca bem-sucedida.
- **Tratamento de Registros Ausentes**: Se não houver uma instância com a chave especificada, o valor da variável será nulo, o que pode exigir processamento adicional.

## Cenário de Aplicação

Este componente utiliza o passo de Referência de Consulta para encontrar o ID do registro na tabela "Tarefa de Ordenação" com base no número de ordenação inserido. Após inserir o número de ordenação e executar o fluxo de dados, o ID do registro correspondente é exibido na interface.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1LZzqHGc7I5IdAVLmK6H1_ItODiiruSAJ/view?usp=sharing)