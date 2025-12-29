# Enviar notificação com modelo

![](../../assets/images/app-development/send-templated-notification.png)

## Informações gerais
A etapa “Enviar Notificação com Modelo” é projetada para enviar notificações a usuários ou grupos de usuários usando modelos pré-configurados. Esta etapa oferece flexibilidade na escolha do método de entrega e dos destinatários da notificação.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor   | Propósito |
|-----------------------|-------------------|-----------|
| Nome da etapa         | -                 | Nome da etapa |
| Etapa de origem       | -                 | Selecionar a etapa anterior | 
| Tipo de notificação   | Smtp, Mail, SignalR| Tipo de canal de entrega da notificação |
| Campo de informações do usuário | - | Lista de usuários a serem notificados |
| Roteamento do usuário  | - | Roteamento do usuário para entregar a notificação |
| Nome do usuário       | -                 | Usuário específico a ser notificado |
| Modelo                | -                 | Seleção de modelos de notificação pré-configurados |
| Tipo de renderização   | Texto, Html, Docx, Xlsx, Pdf | Tipo de renderização do modelo de notificação  |
| Tema da mensagem      | Texto             | Linha de assunto para notificações por e-mail |

## Casos
- **Notificações Automatizadas**: Usadas para enviar notificações a usuários utilizando modelos predefinidos para garantir mensagens consistentes e precisas.
- **Flexibilidade na Entrega de Mensagens**: Permite escolher entre diferentes canais de entrega (por exemplo, SMTP, Mail, SignalR), o que aumenta a cobertura e a eficiência das comunicações.
- **Personalização de Notificações**: Suporta a personalização de notificações para usuários ou grupos específicos, bem como vários formatos de conteúdo (texto, HTML, Docx, Xlsx).

## Exceções
- **Requisito de um Canal de Entrega Configurado**: Para que as notificações sejam enviadas com sucesso, você deve ter um canal de entrega funcional, como um servidor SMTP para notificações por e-mail.