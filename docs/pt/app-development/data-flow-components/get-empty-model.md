# Obter Modelo Vazio

![](../../assets/images/app-development/get-empty-model.png)

## Informações gerais
A etapa “Obter Modelo Vazio” é utilizada em scripts de fluxo de dados que não requerem a recuperação do modelo de dados na entrada. É frequentemente usada quando o fluxo de dados é chamado para executar operações regulares, como a geração de relatórios, especialmente se forem agendadas (por exemplo, por cron).

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração  | Opções de Valor | Propósito |
|-----------------------|-------------------|------------|
| Nome da etapa         | -                 | Nome da etapa |
| Validar valores de entrada | true, false       | Indica que os valores de entrada devem ser verificados quanto à correção antes do processamento |

## Casos
- **Operações Regulares**: Ideal para fluxos de dados agendados para serem executados regularmente sem a necessidade de dados de entrada.
- **Estado Inicial do Fluxo de Dados**: Usado para inicializar o fluxo de dados sem dados pré-definidos, permitindo que os desenvolvedores criem e populam o modelo de dados por conta própria usando etapas subsequentes.

## Exceções
- **Sem Dados de Entrada**: Ao usar esta etapa, os dados de entrada não são fornecidos no fluxo de dados. Isso significa que o desenvolvedor deve inicializar e preencher o modelo de dados nas etapas subsequentes.

## Cenário de Aplicação

Este componente é uma interface para adicionar um novo nome através de um **campo de entrada** na interface, atualizando então o modelo de dados e exibindo o resultado em um **datagrid**. O fluxo de dados no componente permite adicionar um novo nome ao modelo e atualizar o registro no **datagrid**.

- Você pode baixar a configuração do componente [aqui](https://drive.google.com/file/d/1G3v4cZiteFdONpIjxPAf78a8gBTrh0w_/view?usp=sharing)