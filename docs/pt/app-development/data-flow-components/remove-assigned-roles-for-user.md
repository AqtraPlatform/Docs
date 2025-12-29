# Remover funções atribuídas ao usuário

![](../../assets/images/app-development/remove-assigned-roles-for-user.png)

## Informações gerais
A etapa “Remover Funções Atribuídas ao Usuário” é utilizada para redefinir todas as funções atribuídas a um usuário específico. Isso permite que administradores de sistema e gerentes de processo removam funções de usuário, simplificando a gestão de permissões e controles de segurança.

## Parâmetros
**Configurações da Etapa:**

| Campo            | Opções de Valor      | Propósito |
|------------------|--------------------|------------|
| Nome da etapa    | -                  | Nome da etapa |
| Etapa de origem  | -                  | Selecionando a etapa anterior |
| Campo de ID do usuário | Nome de uma variável do tipo informações do usuário | Campo que contém o ID do usuário para redefinição de função |

## Casos
- **Gestão de Acesso e Funções**: Esta etapa é ideal para scripts onde você deseja alterar ou redefinir rapidamente as funções de usuário, como quando as responsabilidades de trabalho mudam ou quando um funcionário sai.
- **Garantindo a Segurança do Sistema**: Usado para prevenir acesso não autorizado a dados sensíveis ou recursos do sistema, removendo funções de usuários que não precisam mais dessas permissões de acesso.

## Exceções
- **Dependência da Precisão da Identificação do Usuário**: A eficácia da etapa depende da identificação precisa do usuário cujas funções você deseja redefinir.
- **Necessidade de Obter o ID do Usuário Primeiro**: A etapa requer que você primeiro obtenha um ID de usuário interno, o que pode ser feito através da etapa “Obter Informações do Usuário” ou outros métodos de autenticação.