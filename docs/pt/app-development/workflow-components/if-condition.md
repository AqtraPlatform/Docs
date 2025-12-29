# Condição If

![](../../assets/images/app-development/if-condition.png)

## Informações gerais

A etapa “Condição If” dentro do fluxo de trabalho é usada para verificar o valor de um campo em relação à condição especificada. Esta etapa permite implementar ramificações condicionais em um processo onde a realização de certas ações ou a movimentação para um script alternativo depende do resultado de uma verificação de condição. Um script alternativo deve conter a etapa “Finalizar”.

## Parâmetros

**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor              | Propósito                                |
| --------------------- | ---------------------------- | ---------------------------------------- |
| Nome da etapa         | -                            | Nome da etapa “Condição If”             |
| Campo de condição     | Multiseleção de Catálogo     | Campo de validação da condição           |
| Operador              | Igual, Diferente, Maior, Menor | Tipo de operador para verificar a condição |
| Comparar com nulo     | verdadeiro, falso            | Verificação de comparação com nulo      |
| Valor                 | -                            | Valor para comparar com o campo         |

## Casos

- **Execução Condicional de Ações**: Usado para ativar diferentes partes do fluxo de trabalho com base nos valores de certos campos, por exemplo, para iniciar diferentes processos com base no status da solicitação.
- **Ramificação Lógica em Processos**: Adequado para criar cadeias lógicas complexas onde diferentes etapas de execução dependem da satisfação de condições específicas.

## Exceções

- **Precisão na Definição de Condições**: É importante definir com precisão as condições e configurar corretamente os campos para validá-las, a fim de evitar ramificações incorretas ou erros na lógica do fluxo de trabalho.
- **Tratamento de Diferentes Scripts**: É necessário planejar claramente como diferentes scripts serão tratados dependendo do resultado da verificação da condição, especialmente em fluxos de trabalho complexos ou com várias etapas.