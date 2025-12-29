# Extração de coleção

![](../../assets/images/app-development/extract-collection.png)

## Informações gerais
A etapa “Extração de Coleção” é usada para converter um campo de array em uma lista plana. Este campo pode ser obtido de uma fonte externa ou de um campo (propriedade) de um componente de array.

Nesta etapa, o array é analisado e o processamento de cada elemento do array (entrada ou objeto) é iniciado como um fluxo de dados interno separado. Cada um desses threads é executado independentemente um do outro. Fluxos de dados analisados usando a etapa “Extração de Coleção” podem ser reagrupados através da etapa “Agrupar por”.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Caminho do modelo     | -                | Caminho para um campo de array no modelo de dados |

## Casos
- **Processamento de Array de Dados**: Usado para extrair e processar cada elemento do array de dados de forma independente.
- **Divisão e Agrupamento Subsequente**: Adequado para cenários onde é necessário dividir estruturas de dados complexas em elementos mais simples para processamento e análise adicionais.

## Exceções
- **Necessidade de especificar a fonte e o caminho exatos**: A indicação incorreta da fonte ou do caminho para o campo de array pode levar a erros no processamento de dados.

## Cenário de aplicação

Este componente permite o processamento de dados de armazém de clientes, adicionando novos registros usando as etapas **extração de coleção** e **execução de script**. Após a execução do fluxo de dados, cada registro recebe dados adicionais de campo.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1Q1czyILIGHc7tVwPYpkgHIFfI87p5WvQ/view?usp=sharing).