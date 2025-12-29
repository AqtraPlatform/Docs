# Aplicar operações de atualização diferida

![](../../assets/images/app-development/apply-deferred-update-operations.png)

## Informações gerais
A etapa “Aplicar Operações de Atualização Diferida” é utilizada para a aplicação em massa de atualizações que foram preparadas usando a série de etapas “Entrada de Atualização Diferida”. Esta etapa permite que você execute as operações de atualização acumuladas de maneira eficiente, aplicando todas de uma vez.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Tamanho do lote       | 1000             | Tamanho do lote de dados a ser processado |
| Tempo limite ocioso em ms | -           | Tempo limite ocioso em milissegundos entre os lotes |
| Número paralelo de lotes | 0            | Número de lotes de dados processados em paralelo |

## Casos
- **Aplicação de Atualização em Massa**: Ideal para cenários onde você precisa atualizar dados em massa, como quando sincroniza uma grande quantidade de dados ou quando precisa fazer alterações rapidamente em múltiplos componentes do sistema.
- **Otimização de Desempenho**: Melhora o desempenho para atualizações em massa por meio de processamento paralelo e gerenciamento eficiente de lotes de dados.

## Exceções
- **Gerenciamento da Sequência de Atualização**: É importante garantir que as atualizações sejam sequenciadas corretamente, especialmente se os dados nas diferentes etapas da “Entrada de Atualização Diferida” estiverem inter-relacionados.
- **Configuração dos Parâmetros de Processamento em Lote**: Parâmetros como tamanho do lote e número de lotes paralelos devem ser cuidadosamente configurados para evitar sobrecarregar o sistema e garantir que as atualizações sejam realizadas de forma eficiente.

## Cenário de aplicação

O componente com uma definição personalizada configura um fluxo de dados para atualizar registros. Os usuários começam extraindo o modelo de ação usando a etapa "Obter modelo de ação". Em seguida, a etapa "Entrada de atualização diferida" é utilizada para atualizações diferidas de registros, onde os usuários podem especificar o componente, ID do componente e mapeamentos de campo. A etapa "Aplicar atualização diferida" permite configurar parâmetros de processamento em lote e execução paralela. Após a conclusão dessas etapas, o componente está pronto para atualizar, criar ou excluir registros, o que ocorre na interface do frontend ao interagir com os elementos de interface correspondentes.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing)