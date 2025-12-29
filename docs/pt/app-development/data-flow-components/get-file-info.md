# Obter informações do arquivo

![](../../assets/images/app-development/get-file-info.png)

## Informações gerais
A etapa “Obter Informações do Arquivo” no Dataflow é usada para recuperar informações sobre um arquivo pelo seu ID. Esta etapa fornece acesso a várias propriedades do arquivo, incluindo seu nome, extensão (tipo), tamanho, data de atualização, criação e autor do arquivo inicial e atualizado.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Campo de origem       | -                | Campo contendo o ID do arquivo |
| Nome do campo de destino | -             | Campo onde as informações sobre o arquivo serão registradas |

## Casos
- **Extração de Informações do Arquivo**: Usado para obter informações detalhadas sobre um arquivo, o que pode ser útil para processamento ou análise de dados subsequentes.
- **Preparação de Dados para Processamento Adicional**: As informações obtidas sobre o arquivo podem ser usadas em etapas subsequentes, como “Executar Script” ou “Filtrar Fonte”, para realizar operações específicas dependendo das propriedades do arquivo.

## Exceções
- **Dependência da Precisão da Fonte de Dados**: A precisão das informações obtidas depende da precisão e relevância dos dados na fonte.
- **Informações Limitadas**: A etapa fornece apenas informações básicas sobre o arquivo e pode não incluir alguns dados específicos ou adicionais.