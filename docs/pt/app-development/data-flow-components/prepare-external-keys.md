# Preparar chaves externas

![](../../assets/images/app-development/prepare-external-keys.png)

## Informações gerais
A etapa “Preparar Chaves Externas” é utilizada para converter os identificadores internos do componente em chaves de sistema externo. Esta etapa é amplamente utilizada para preparar e enviar dados para sistemas externos, incluindo integração com LDAP. Facilita o processo de transferência de informações de usuários para um sistema externo, incluindo o contexto relevante.

No decorrer da etapa, os IDs internos do componente são substituídos pelas chaves primárias que são especificadas para este componente, o que garante o mapeamento correto dos dados entre os sistemas interno e externo.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Fonte de dados para conversão de chaves |

## Casos
- **Integração com Sistemas Externos**: Usado para adaptar dados internos para sua devida integração e envio a sistemas externos, como LDAP.
- **Preparar Dados para Exportação**: Adequado para scripts onde os IDs internos precisam ser transformados para atender aos padrões e requisitos de sistemas externos.

## Exceções
- **Relevância e Exatidão dos Dados**: A eficácia da etapa depende da precisão e relevância dos dados internos e sua conformidade com a estrutura do sistema externo.
- **Gerenciamento de Mapeamento de Dados**: É necessário garantir que todos os IDs internos estejam corretamente mapeados para as chaves primárias do sistema externo para evitar erros de integração.