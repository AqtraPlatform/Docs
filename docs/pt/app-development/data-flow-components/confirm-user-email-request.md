# Confirmação de solicitação de e-mail do usuário

![](../../assets/images/app-development/confirm-user-email-request.png)

## Informações gerais
A etapa “Confirmação de Solicitação de E-mail do Usuário” é usada para habilitar o usuário que foi originalmente criado com a flag “Desativado”. Este processo envolve a verificação do usuário via e-mail usando a etapa “Enviar Notificação Modelada”. A etapa requer um domínio de aplicativo com uma URI pública e um servidor SMTP configurado para enviar notificações por e-mail.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Selecionando a etapa anterior |
| Campo de informações do usuário | -      | Um campo que contém informações sobre o usuário |
| Nome do usuário       | -                | Nome do usuário cuja confirmação deve ser obtida |
| Cliente para solicitação | -            | O cliente ou aplicativo que inicia a solicitação de confirmação |

## Casos
- **Habilitação de Novos Usuários**: Esta etapa é usada para habilitar usuários que foram registrados como desativados, verificando seu e-mail. Isso fornece uma camada adicional de verificação e segurança.
- **Gerenciamento de Acesso do Usuário**: Adequado para sistemas que exigem verificação de e-mail do usuário antes que o acesso total à funcionalidade do sistema possa ser concedido.

## Exceções
- **Requisito de um servidor SMTP configurado**: Um servidor SMTP configurado é necessário para que as notificações de e-mail de confirmação sejam enviadas com sucesso.
- **Dependência do domínio do aplicativo e URI pública**: Esta etapa requer um domínio de aplicativo com uma URI pública para garantir que a operação esteja correta e que o processo de verificação esteja disponível para o usuário.