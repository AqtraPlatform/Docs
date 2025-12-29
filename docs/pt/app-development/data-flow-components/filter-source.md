# Fonte do Filtro

![](../../assets/images/app-development/filter-source.png)

## Informações gerais
A etapa “Fonte do Filtro” é usada para filtrar o fluxo de dados no dataflow. Ela permite ramificar fluxos de dados com base no valor do campo selecionado e no operador de teste especificado, como igual, diferente, maior e menor.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor   | Propósito |
|-----------------------|-------------------|-----------|
| Nome da etapa         | -                 | Nome da etapa |
| Etapa de origem       | -                 | Selecionando a etapa anterior |
| Campo de origem       | -                 | Campo a ser filtrado |
| Operador              | igual, diferente, maior, menor | Operador para comparar valores de campo |
| Comparar com nulo     | verdadeiro, falso  | Indica se deve comparar com nulo |
| Valor de filtro       | -                 | Valor a ser filtrado |

## Casos
- **Ramificação do Fluxo de Dados**: Usado para dividir um fluxo de dados com base em condições específicas definidas no filtro.
- **Segmentação de Dados**: Adequado para situações em que você precisa tratar diferentes segmentos de dados de maneira diferente, dependendo dos critérios especificados.

## Exceções
- **Precisão da Configuração do Filtro**: Um filtro configurado incorretamente pode resultar na perda de dados importantes ou na inclusão de dados desnecessários no processamento.
- **Dependência do campo selecionado**: A eficácia da filtragem depende da escolha correta do campo e do operador de comparação apropriado.

## Cenário de aplicação

Este componente é uma interface com três botões: `ExecuteFilterSource`, `ExecuteFilterSourceNotEqual`, e `ExecuteFilterSourceGreat`, cada um dos quais aciona um fluxo de dados dependendo da entrada no campo `First`. Diferentes cenários de teste incluem verificar condições de igualdade, desigualdade e maior/menor que o valor especificado.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1OO5SymRdhmv3oED2EPG4twG5mypsqqs9/view?usp=sharing).