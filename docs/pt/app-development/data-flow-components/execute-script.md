# Executar script

![](../../assets/images/app-development/execute-script.png)

## Informações gerais
A etapa “Executar Script” é projetada para executar scripts Python usando bibliotecas padrão do Python.

Esta etapa permite que você execute scripts Python de qualquer complexidade enquanto trabalha com o modelo de fluxo de dados atual. Usando o script, você pode alterar o modelo adicionando novas variáveis ou mudando os valores das existentes.

Exemplos de uso:
- Para obter o valor de uma variável da etapa “modelo de ação de obtenção”: `item ['data'] ['Property_name'] `
- Para criar uma nova variável no script: `item ['Property_name'] `

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |

## Casos
- **Personalização do processamento de dados**: Adequado para lógica de processamento de dados complexa que não pode ser implementada com ferramentas padrão de fluxo de dados.
- **Adição e modificação de dados**: Adequado para cenários que exigem a adição de novos dados ou a modificação de dados existentes no modelo.

## Exceções
- **Necessidade de proficiência em Python**: Requer conhecimento de Python e compreensão da lógica de trabalho com fluxo de dados.
- **Tipagem de variáveis**: A tipagem rigorosa de variáveis pode exigir atenção adicional ao escrever scripts. Tipos suportados: `@number`, `@integer`, `@string`, `@uuid`, `@boolean`, `@uri`, `@date`, `@date-time`, `@time`, `@catalog`, `@array`.

## Cenário de aplicação

Este componente demonstra vários cenários de uso da etapa Executar Script dentro de um fluxo de dados, incluindo a criação de novas variáveis de diferentes tipos e a modificação de valores de campos disponíveis no modelo de dados.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/18fbg2g2rcvXORI7i31zu81NdSKwMqE99/view?usp=sharing)