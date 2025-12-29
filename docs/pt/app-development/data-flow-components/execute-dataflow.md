# Executar dataflow

![](../../assets/images/app-development/execute-dataflow.png)

## Informações gerais
A etapa Executar Dataflow é usada para chamar o Dataflow de qualquer componente publicado. Esta etapa permite que você execute um Dataflow adicional no contexto do processo atual de processamento de dados.

Quando usada com um campo de array obtido de uma fonte externa ou de um campo de array (propriedade), a etapa analisa esse array e inicia o processamento paralelo de cada registro ou objeto contido no array.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Componente            | -                | O componente do qual o Dataflow é chamado |
| Dataflow              | -                | Nome do Dataflow a ser executado |
| Campo de armazenamento de resultado | - | Campo para salvar o resultado da execução do Dataflow |

## Casos
- **Atualizando dados de outros dataflows**: A etapa “Executar Dataflow” é ideal para situações em que você deseja atualizar campos no modelo atual com dados coletados ou processados em outros dataflows. Isso possibilita a integração e sincronização eficaz de dados entre diferentes processos e componentes.
- **Chamada de Dataflow externo**: Usado para integrar e lançar Dataflows adicionais como parte do processo atual de processamento de dados.

## Exceções
- **Dependência da correção de outros dataflows**: A eficácia da etapa “Executar Dataflow” depende diretamente da precisão e confiabilidade dos dados obtidos de outros dataflows. Todos os dataflows relacionados devem ser cuidadosamente configurados e testados para garantir que os dados atualizados estejam corretos e atualizados.

## Cenário de aplicação

Este componente cria um dataflow para realizar operações nos dados do componente atual. Inclui etapas do modelo de ação Get para recuperar o modelo do dataflow e etapas de executar dataflow para executar o dataflow com parâmetros apropriados, como selecionar o componente atual, escolher o dataflow a ser executado, configurar campos de resultado e exibir definições do componente de dados. Este componente permite operações de dados no componente diretamente da interface da aplicação.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1ekmRNTRgO30koKm04pyhEZsXG9W5T-O-/view?usp=sharing).