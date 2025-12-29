# Solicitação de redefinição de senha do usuário

![](../../assets/images/app-development/reset-user-password-request.png)

## Informações gerais
A etapa “Solicitação de Redefinição de Senha do Usuário” é projetada para gerar uma nova senha para o usuário. A etapa funciona em conjunto com a “Enviar Notificação Modelada” para garantir que os usuários recebam uma nova senha. A etapa só funciona se você tiver um domínio de aplicativo com uma URI pública configurada.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Campo de informações do usuário | -      | Um campo que contém informações sobre o usuário |
| Nome do usuário       | -                | Nome de usuário para o qual a senha está sendo redefinida |
| Cliente para solicitação | -            | Cliente ou aplicativo que inicia a solicitação de autenticação |

## Casos
- **Recuperação de Acesso do Usuário**: Usado em scripts onde um usuário esqueceu sua senha e precisa redefini-la para re-acessar o sistema.

## Exceções
- **Requisito para um Domínio de Aplicativo com uma URI Pública**: A etapa requer um domínio de aplicativo configurado com uma URI pública para funcionar corretamente.
- **Dependência do Método de Notificação do Usuário**: A eficácia da etapa depende da confiabilidade e disponibilidade do método de notificação do usuário, como e-mail, usado para enviar uma nova senha.