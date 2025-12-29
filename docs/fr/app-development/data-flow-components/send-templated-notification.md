# Envoyer une notification modélisée

![](../../assets/images/app-development/send-templated-notification.png)

## Informations générales
L'étape "Envoyer une notification modélisée" est conçue pour envoyer des notifications aux utilisateurs ou à des groupes d'utilisateurs en utilisant des modèles préconfigurés. Cette étape offre une flexibilité dans le choix de la méthode de livraison et des destinataires de la notification.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur   | Objectif |
|---------------------|---------------------|------------|
| Nom de l'étape      | -                   | Nom de l'étape |
| Étape source        | -                   | Sélection de l'étape précédente | 
| Type de notification | Smtp, Mail, SignalR | Type de canal de livraison de notification |
| Champ d'information utilisateur | - | Liste des utilisateurs à notifier |
| Routage utilisateur  | - | Routage de l'utilisateur pour livrer la notification |
| Nom d'utilisateur    | - | Utilisateur spécifique à notifier |
| Modèle              | - | Sélection parmi les modèles de notification préconfigurés |
| Type de rendu       | Texte, Html, Docx, Xlsx, Pdf | Type de rendu du modèle de notification  |
| Thème du message    | Texte                 | Ligne d'objet pour les notifications par email |

## Cas d'utilisation
- **Notifications automatisées** : Utilisées pour envoyer des notifications aux utilisateurs en utilisant des modèles prédéfinis afin d'assurer des messages cohérents et précis.
- **Flexibilité de la livraison des messages** : Permet de choisir entre différents canaux de livraison (par exemple, SMTP, Mail, SignalR), ce qui augmente la couverture et l'efficacité des communications.
- **Personnalisation des notifications** : Prend en charge la personnalisation des notifications pour des utilisateurs ou groupes spécifiques, ainsi que divers formats de contenu (texte, HTML, Docx, Xlsx).

## Exceptions
- **Exigence d'un canal de livraison configuré** : Pour que les notifications soient envoyées avec succès, vous devez disposer d'un canal de livraison fonctionnel, tel qu'un serveur SMTP pour les notifications par email.