# Enviar notificação

![](../../assets/images/app-development/send-notification-workflow.png)

## Informações gerais
A etapa “Enviar Notificação” dentro do fluxo de trabalho é usada para enviar notificações simples a um usuário ou grupo de usuários usando um ícone de sino. Isso permite que você se comunique de forma eficaz com os usuários do sistema, transmitindo informações ou notificações importantes.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor       | Propósito |
|-----------------------|-----------------------|-----------|
| Nome da etapa         | -                     | Nome da etapa |
| Tipo de notificação   | Smtp, Mail, SignalR   | Tipo de canal de entrega da notificação |
| Campo de informações do usuário | Multiseleção de Catálogo | Campo contendo usuário ou lista de usuários |
| Nome do usuário       | Multiseleção de Catálogo | Usuário específico a ser notificado |
| Mensagem              | -                     | Texto da notificação |

## Casos
- **Informações do Usuário**: Usado para informar os usuários sobre eventos importantes, mudanças no sistema, alarmes ou outras mensagens que precisam de atenção.
- **Notificações Personalizadas**: Permite que notificações sejam enviadas a usuários ou grupos específicos, tornando a comunicação mais direcionada e eficaz.

## Exceções
- **Necessidade de Informações de Usuário Atualizadas**: A entrega eficaz de notificações requer informações de usuário atualizadas, incluindo detalhes de contato do usuário.
- **Selecionando o Canal de Entrega Correto**: Você deve escolher cuidadosamente o tipo de canal de entrega (Smtp, Mail, SignalR) dependendo das preferências dos usuários e das capacidades técnicas do sistema.