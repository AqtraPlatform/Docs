# Proxy get entry

![](../../assets/images/app-development/proxy-get-entry.png)

## Informações gerais
A etapa “Proxy Get Entry” é usada para gerar um modelo de uma solicitação proxy a fim de obter uma única entrada. Esta etapa está intimamente relacionada à configuração “Proxy mode”, que pode ser encontrada na seção “Settings”.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração  | Opções de Valor | Propósito |
|-----------------------|-------------------|------------|
| Nome da etapa         | -                 | Nome da etapa |
| Validar valores de entrada | true, false       | Indica que os valores de entrada devem ser verificados quanto à correção antes do processamento |

## Casos
- **Recuperação de Entrada Única**: Usado para gerar e enviar solicitações para uma entrada específica via um servidor proxy.
- **Integração com sistemas externos**: Fornece comunicação com sistemas e serviços externos para obter dados usando proxy de consulta.

## Exceções
- **Dependência das Configurações de Proxy**: O funcionamento correto da etapa depende da configuração correta do “Proxy mode” na seção “Settings”.
- **Funcionalidade Limitada**: A etapa é especializada na recuperação de registros únicos e não é projetada para lidar com múltiplas consultas ou dados.