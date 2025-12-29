# Envoyer une notification

![](../../assets/images/app-development/send-notification.png)

## Informations générales
L'étape "Envoyer une notification" est conçue pour envoyer des notifications personnalisées aux utilisateurs ou à des groupes d'utilisateurs. Cette étape offre un haut degré de flexibilité, vous permettant de définir directement le texte et le sujet de chaque notification, ce qui la rend idéale pour les situations nécessitant des messages personnalisés.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Source des données pour l'envoi de la notification |
| Champ d'informations utilisateur | -   | Champ contenant des informations sur les destinataires de la notification |
| Nom d'utilisateur   | -                 | Nom de l'utilisateur à qui la notification sera envoyée |
| Champ du corps du message | -         | Champ pour le corps du message |
| Thème du message   | Texte             | Sujet de la notification |
| Corps du message    | Texte             | Texte personnalisable de la notification |
| Type de notification | Smtp, Mail, SignalR | Type de notification |

## Cas d'utilisation
- **Notifications personnalisées** : Utilisées pour créer des messages uniques pour chaque utilisateur ou situation, garantissant une pertinence et un engagement maximum des destinataires.
- **Communication flexible** : Convient aux scripts où des messages spéciaux sont nécessaires, tels que des offres spéciales, des rappels individuels ou des bulletins d'information personnalisés.

## Exceptions
- **Exigence de détail du message** : Une attention particulière aux détails et à la précision doit être portée lors de la formulation du texte de chaque notification.
- **Nécessité d'une gestion soigneuse des notifications** : Étant donné que chaque message est personnalisable individuellement, il est important de gérer soigneusement le processus de création et d'envoi des notifications pour éviter les erreurs et les incohérences.