# Envoyer une notification

![](../../assets/images/app-development/send-notification-workflow.png)

## Informations générales
L'étape "Envoyer une notification" dans le flux de travail est utilisée pour envoyer des notifications simples à un utilisateur ou à un groupe d'utilisateurs en utilisant une icône de cloche. Cela vous permet de communiquer efficacement avec les utilisateurs du système en transmettant des informations ou des notifications importantes.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur   | Objectif |
|--------------------|---------------------|----------|
| Nom de l'étape     | -                   | Nom de l'étape |
| Type de notification | Smtp, Mail, SignalR | Type de canal de livraison de notification |
| Champ d'informations utilisateur | Multisélection de Catalogue | Champ contenant l'utilisateur ou la liste des utilisateurs |
| Nom d'utilisateur   | Multisélection de Catalogue | Utilisateur spécifique à notifier |
| Message            | -                   | Texte de la notification |

## Cas d'utilisation
- **Informations sur l'utilisateur** : Utilisé pour informer les utilisateurs des événements importants, des changements dans le système, des alarmes ou d'autres messages nécessitant une attention.
- **Notifications personnalisées** : Permet d'envoyer des notifications à des utilisateurs ou groupes spécifiques, rendant la communication plus ciblée et efficace.

## Exceptions
- **Besoin d'informations utilisateur à jour** : Une livraison de notification efficace nécessite des informations utilisateur à jour, y compris les coordonnées de l'utilisateur.
- **Sélection du bon canal de livraison** : Vous devez choisir soigneusement le type de canal de livraison (Smtp, Mail, SignalR) en fonction des préférences des utilisateurs et des capacités techniques du système.