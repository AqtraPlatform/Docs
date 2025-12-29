# Entrada de atualização diferida

![](../../assets/images/app-development/deferred-update-entry.png)

## Informações gerais
A etapa “Entrada de Atualização Diferida” é usada para organizar a atualização diferida de entradas em um componente específico. Esta etapa permite acumular ações para criar, atualizar ou excluir entradas, que são então executadas após a ativação da etapa “Aplicar Operações de Atualização Diferida”. Dessa forma, múltiplas operações de atualização podem ser coletadas.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionar a etapa anterior |
| Componente            | -                | Componente a ser atualizado |
| Chave do campo do componente | -        | Campo com a chave do componente a ser atualizado |
| Marcar entrada para exclusão | true, false | Marca de exclusão da entrada |
| Campo de nome         | -                | Nome do campo a ser atualizado |
| Mapeamento de campos   | -                | Mapeamento de campos entre o fluxo de dados e o componente |

## Casos
- **Processamento em Lote de Dados**: Usado para coletar múltiplas operações de atualização de dados e, em seguida, executá-las em uma única transação, melhorando o desempenho e reduzindo a carga no sistema.
- **Gerenciamento complexo de dados**: Adequado para cenários que requerem lógica complexa de atualização de dados, incluindo a criação, modificação e exclusão de entradas dentro de um único fluxo de trabalho.

## Exceções
- **Necessidade de Atualizações Subsequentes**: Todas as operações de atualização acumuladas por esta etapa precisam ser ativadas através da etapa “Aplicar Operações de Atualização Diferida” para serem realizadas.

## Cenário de aplicação

O componente com uma definição personalizada configura um fluxo de dados para atualizar registros. Os usuários começam extraindo o modelo de ação usando a etapa "Obter modelo de ação". Em seguida, a etapa "Entrada de atualização diferida" é usada para atualizações diferidas de registros, onde os usuários podem especificar o componente, ID do componente e mapeamentos de campo. A etapa "Aplicar atualização diferida" permite configurar o processamento em lote e parâmetros de execução paralela. Após a conclusão dessas etapas, o componente está pronto para atualizar, criar ou excluir registros, o que ocorre no frontend ao interagir com os elementos da interface correspondentes.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing)