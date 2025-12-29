# Registrar usuário externo

![](../../assets/images/app-development/register-external-user.png)

## Informações gerais
A etapa “Registrar Usuário Externo” é destinada ao registro de usuários individuais ou grupos de usuários. Esta etapa é projetada no contexto da integração LDAP e é utilizada para integração com sistemas externos, facilitando o processo de troca de usuários desses sistemas e, em seguida, fazendo o login deles no sistema atual.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Nome do usuário       | -                | Nome de registro ou ID do usuário |
| Campo chave           | -                | Campo contendo informações chave para identificar o usuário |
| Provedor de autenticação | -              | Provedor de autenticação utilizado para registrar o usuário |

## Casos
- **Integração de Usuários de Sistemas Externos**: Usado para trocar e registrar usuários de LDAP ou outros sistemas externos, garantindo sua correta integração no sistema atual.
- **Automação do Processo de Registro**: Adequado para scripts onde é necessário automatizar o processo de registro de um grande número de usuários, minimizando o trabalho manual e possíveis erros.

## Exceções
- **Dependência da Precisão dos Dados de Entrada**: A eficácia da etapa depende da precisão e completude dos dados recebidos do sistema externo.