# Enviar notificação com modelo

![](../../assets/images/app-development/send-templated-notification-workflow.png)

## Informações gerais
A etapa “Enviar Notificação com Modelo” dentro do fluxo de trabalho é usada para enviar notificações a usuários ou grupos de usuários utilizando modelos pré-configurados. Isso permite criar mensagens padronizadas, mas personalizadas, o que melhora a comunicação e garante a consistência das mensagens.

## Parâmetros
**Configurações da Etapa:**

| Campo de Configuração | Opções de Valor        | Propósito |
|-----------------------|------------------------|-----------|
| Nome da etapa         | -                      | Nome da etapa |
| Tipo de notificação   | Smtp, Mail, SignalR    | Tipo de canal de entrega da notificação |
| Campo de informações do usuário | Multiseleção de Catálogo | Campo com informações sobre um usuário ou grupo de usuários |
| Grupo de usuários     | Multiseleção de Catálogo | (Parâmetro desatualizado, não utilizado) |
| Roteamento de usuários | Multiseleção de Catálogo | Configuração do roteamento de notificações |
| Nome do usuário       | Multiseleção de Catálogo | Usuário específico a ser notificado |
| Modelo                | Multiseleção de Catálogo | Escolha de um modelo de notificação |
| Tipo de renderização   | Texto, Html, Docx, Xlsx | Formato de renderização do modelo |

## Casos
- **Notificações Automatizadas**: Usadas para enviar notificações padronizadas, como lembretes, confirmações de ação ou mensagens informativas.
- **Comunicação Eficaz**: Adequadas para criar mensagens profissionalmente elaboradas para comunicações externas ou internas.

## Exceções
- **Requisitos de Personalização de Modelo**: Os modelos de notificação devem ser preparados e configurados com antecedência para garantir que as mensagens sejam relevantes para os propósitos de comunicação.
- **Gerenciar Destinatários de Notificações**: É importante identificar os destinatários das mensagens usando o Campo de informações do usuário e o Nome do usuário para garantir que as notificações cheguem aos destinatários corretos.