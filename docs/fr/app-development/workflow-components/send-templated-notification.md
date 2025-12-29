# Envoyer une notification modélisée

![](../../assets/images/app-development/send-templated-notification-workflow.png)

## Informations générales
L'étape "Envoyer une notification modélisée" dans le flux de travail est utilisée pour envoyer des notifications aux utilisateurs ou groupes d'utilisateurs en utilisant des modèles préconfigurés. Cela vous permet de créer des messages standardisés mais personnalisés, ce qui améliore la communication et garantit la cohérence des messages.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur        | Objectif |
|---------------------|--------------------------|----------|
| Nom de l'étape      | -                        | Nom de l'étape |
| Type de notification | Smtp, Mail, SignalR      | Type de canal de livraison de notification |
| Champ d'information utilisateur | Multisélection de Catalogue | Champ contenant des informations sur un utilisateur ou un groupe d'utilisateurs |
| Groupe d'utilisateurs | Multisélection de Catalogue | (Paramètre obsolète, non utilisé) |
| Routage utilisateur  | Multisélection de Catalogue | Configuration du routage des notifications |
| Nom d'utilisateur    | Multisélection de Catalogue | Utilisateur spécifique à notifier |
| Modèle              | Multisélection de Catalogue | Choix d'un modèle de notification |
| Type de rendu       | Texte, Html, Docx, Xlsx   | Format de rendu du modèle |

## Cas d'utilisation
- **Notifications automatisées** : Utilisées pour envoyer des notifications standardisées, telles que des rappels, des confirmations d'action ou des messages d'information.
- **Communication efficace** : Convient pour créer des messages conçus professionnellement pour des communications externes ou internes.

## Exceptions
- **Exigences de personnalisation des modèles** : Les modèles de notification doivent être préparés et configurés à l'avance pour garantir que les messages sont pertinents pour les objectifs de communication.
- **Gérer les destinataires de notification** : Il est important de cibler les destinataires des messages en utilisant le champ d'information utilisateur et le nom d'utilisateur pour s'assurer que les notifications atteignent les bons destinataires.