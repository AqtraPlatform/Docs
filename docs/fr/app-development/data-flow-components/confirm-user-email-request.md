# Confirmation de la demande d'email utilisateur

![](../../assets/images/app-development/confirm-user-email-request.png)

## Informations générales
L'étape "Confirmation de la demande d'email utilisateur" est utilisée pour activer l'utilisateur qui a été initialement créé avec le drapeau "Désactivé". Ce processus implique de vérifier l'utilisateur par email en utilisant l'étape "Envoyer une notification modélisée". L'étape nécessite un domaine d'application avec une URI publique et un serveur SMTP configuré pour envoyer des notifications par email.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Champ d'information utilisateur | -     | Un champ qui contient des informations sur l'utilisateur |
| Nom d'utilisateur   | -                 | Nom de l'utilisateur dont la confirmation doit être obtenue |
| Client pour la demande | -             | Le client ou l'application qui initie la demande de confirmation |

## Cas d'utilisation
- **Activation de nouveaux utilisateurs** : Cette étape est utilisée pour activer les utilisateurs qui ont été enregistrés comme désactivés en vérifiant leur email. Cela fournit une couche supplémentaire de vérification et de sécurité.
- **Gestion des accès utilisateur** : Convient aux systèmes qui nécessitent une vérification de l'email de l'utilisateur avant que l'accès complet aux fonctionnalités du système puisse être accordé.

## Exceptions
- **Exigence d'un serveur SMTP configuré** : Un serveur SMTP configuré est requis pour que les notifications par email de confirmation soient envoyées avec succès.
- **Dépendance au domaine d'application et à l'URI publique** : Cette étape nécessite un domaine d'application avec une URI publique pour garantir que l'opération est correcte et que le processus de vérification est disponible pour l'utilisateur.