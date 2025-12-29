# Enviar notificação

![](../../assets/images/app-development/send-notification.png)

## Informações gerais
A etapa “Enviar Notificação” é projetada para enviar notificações personalizadas a usuários ou grupos de usuários. Esta etapa oferece um alto grau de flexibilidade, permitindo que você defina diretamente o texto e o assunto de cada notificação, tornando-a ideal para situações que exigem mensagens personalizadas.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor | Propósito |
|-----------------------|------------------|-----------|
| Nome da etapa         | -                | Nome da etapa |
| Etapa de origem       | -                | Fonte dos dados para envio da notificação |
| Campo de informações do usuário | -      | Campo que contém informações sobre os destinatários da notificação |
| Nome do usuário       | -                | Nome do usuário para quem a notificação será enviada |
| Campo do corpo da mensagem | -          | Campo para o corpo da mensagem |
| Tema da mensagem      | Texto            | Assunto da notificação |
| Corpo da mensagem     | Texto            | Texto personalizável da notificação |
| Tipo de notificação    | Smtp, Mail, SignalR | Tipo de notificação |

## Casos
- **Notificações Personalizadas**: Usadas para criar mensagens únicas para cada usuário ou situação, garantindo máxima relevância e engajamento dos destinatários.
- **Comunicação Flexível**: Adequada para scripts onde mensagens especiais são necessárias, como ofertas especiais, lembretes individuais ou newsletters personalizadas.

## Exceções
- **Requisito de Detalhe da Mensagem**: Atenção aos detalhes e precisão devem ser observadas ao formular o texto de cada notificação.
- **Necessidade de Gestão Cuidadosa das Notificações**: Como cada mensagem é individualmente personalizável, é importante gerenciar cuidadosamente o processo de criação e envio de notificações para evitar erros e inconsistências.