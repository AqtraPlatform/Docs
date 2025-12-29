# Distinct

![](../../assets/images/app-development/distinct.png)

## Informações gerais
A etapa Distinct é usada para eliminar entradas duplicadas do fluxo de dados, deixando apenas valores únicos. Esse processo ajuda a otimizar o processamento de dados, eliminando duplicatas e reduzindo a quantidade de dados analisados.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito                           |
|-----------------------|------------------|--------------------------------------|
| Nome da etapa         | -                | Nome da etapa no fluxo de dados        |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Chaves                | -                | Chaves para verificar a exclusividade      |

## Casos
- **Limpeza de Dados**: Remoção de entradas duplicadas para simplificar a análise.
- **Preparação para agregação**: Pré-limpeza de dados antes de realizar operações de agregação.

## Exceções
- **Seleção de chaves**: Seleção incorreta de chaves pode resultar na perda de dados importantes.
- **Perda de informação**: Risco de perder parte dos dados se a etapa for configurada incorretamente.

## Cenário de aplicação

Este componente verifica a disponibilidade de campos na etapa Distinct. O botão "Distinct" é clicado na interface. Se a etapa funcionar corretamente, uma linha "execute" com uma prévia da resposta HTTP deve aparecer na aba Network, contendo dados para três registros.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1dA9EzzJOn9sWBYhdvL__AcI1kJ5qNNLd/view?usp=sharing).