# Obter modelo bruto

![](../../assets/images/app-development/get-raw-model.png)

## Informações gerais
A etapa “Obter Modelo Bruto” é utilizada em um fluxo de dados, que requer o processamento de um modelo de dados personalizado que não corresponde ao modelo de componente padrão, fluxo de trabalho ou outras opções padrão. Casos de uso típicos incluem fluxos de dados chamados de um Script de Componente com variáveis definidas dentro do script, bem como o processamento de dados de formulários dentro de uma estrutura de múltiplos componentes.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração  | Opções de Valor | Propósito |
|-----------------------|-------------------|------------|
| Nome da etapa         | -                 | Nome da etapa |
| Validar valores de entrada | true, false       | Indica que os valores de entrada devem ser verificados quanto à correção antes do processamento |

## Casos
- **Integração com Script de Componente**: Usado para fluxos de dados chamados de Script de Componente quando variáveis ou dados específicos são necessários.
- **Processamento de Dados de Formulário de Múltiplos Componentes**: Adequado para scripts onde fluxos de dados trabalham com dados obtidos de formulários em uma estrutura de múltiplos componentes.

## Exceções
- **Requisito de Configuração do Modelo**: Você deve pré-configurar o modelo de dados em formato JSON.
- **Características do Formato do Modelo**: Uma configuração inadequada do modelo pode resultar em processamento de dados incorreto ou erros no fluxo de dados.