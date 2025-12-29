# Entrada de consulta proxy

![](../../assets/images/app-development/proxy-query-entry.png)

## Informações gerais
A etapa “Entrada de Consulta Proxy” é usada para gerar um modelo de consulta proxy usando um filtro (**Consulta**) para recuperar uma ou várias entradas. Esta etapa funciona em conjunto com a configuração “Modo Proxy” na seção “Configurações”. Para que o modelo de dados do componente funcione corretamente, propriedades com a flag **Consulta** devem ser definidas.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração  | Opções de Valor | Propósito |
|-----------------------|-------------------|------------|
| Nome da etapa         | -                 | Nome da etapa |
| Filtro de Consulta     | -                 | Filtro para definir uma entrada específica para uma consulta |
| Configurações do modo proxy | -                 | Referência às configurações do modo proxy definidas em “Configurações” |

## Casos
- **Consultas Filtradas em Proxy**: Usado no fluxo de dados de entrada para componentes marcados como proxy para executar consultas com filtragem de dados.
- **Recuperação de Dados Específicos**: Recupera uma entrada específica com base em certos critérios de filtro.

## Exceções
- **Dependência de Configuração do Componente**: Requer certas propriedades com a flag **Consulta** no modelo de dados do componente.
- **Uso Limitado**: A etapa é projetada para recuperar dados com base em filtros e não é adequada para consultas gerais sem especificação.