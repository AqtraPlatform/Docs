# Juntar modelos

![](../../assets/images/app-development/join-models.png)

## Informações gerais
A etapa “Juntar Modelos” é projetada para mesclar dados de duas fontes diferentes. Ela adiciona dados da fonte da “Etapa Direita” aos dados da fonte da “Etapa Esquerda” se entradas correspondentes forem encontradas em ambas as fontes.

A etapa cria um novo modelo de dados ao mesclar os fluxos de dados definidos nos parâmetros da “Etapa Esquerda” e “Etapa Direita”. A etapa aguarda a conclusão do processamento de ambos os fluxos e, em seguida, classifica e mescla os dados.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa esquerda        | -                | Fonte de dados para o lado esquerdo dos fluxos mesclados |
| Etapa direita         | -                | Fonte de dados para o lado direito dos fluxos mesclados |
| Chave esquerda        | -                | Chave para mesclar dados da fonte esquerda |
| Chave direita         | -                | Chave para mesclar dados da fonte direita |
| Mapeamento            | -                | Mapeamento de campos entre as fontes esquerda e direita |

## Casos
- **Mesclagem de Fluxos de Dados**: Usado para mesclar dois fluxos de dados diferentes em um modelo, permitindo que você analise e processe os dados mesclados.
- **Enriquecimento de Dados**: É usado para adicionar informações adicionais de um conjunto de dados a outro, melhorando assim a completude das informações.

## Exceções
- **Necessidade de uma Chave de Mesclagem Exata**: Erros na definição da “Chave Esquerda” e “Chave Direita” podem levar a uma mesclagem de dados incorreta ou ineficiente.

## Cenário de aplicação

Este componente permite **testar** e **verificar** a funcionalidade de um fluxo de dados onde os dados são **mesclados** de diferentes fontes. Ele fornece **mapeamento de campos** e **verificação de mesclagem de dados** no **frontend** e na pré-visualização da **resposta HTTP**.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1YRpXJwNSTp_jOPxP-j0M9SvocZw1W6Tt/view?usp=sharing).