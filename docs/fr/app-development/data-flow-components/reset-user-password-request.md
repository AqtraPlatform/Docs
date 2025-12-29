# Demande de réinitialisation du mot de passe utilisateur

![](../../assets/images/app-development/reset-user-password-request.png)

## Informations générales
L'étape « Demande de réinitialisation du mot de passe utilisateur » est conçue pour générer un nouveau mot de passe pour l'utilisateur. L'étape fonctionne en conjonction avec la « Notification modélisée » pour s'assurer que les utilisateurs reçoivent un nouveau mot de passe. L'étape ne fonctionne que si vous avez un domaine d'application avec une URI publique configurée.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Champ d'informations utilisateur | -     | Un champ contenant des informations sur l'utilisateur |
| Nom d'utilisateur   | -                 | Nom d'utilisateur pour lequel le mot de passe est réinitialisé |
| Client pour la demande | -             | Client ou application qui initie la demande d'authentification |

## Cas
- **Récupération d'accès utilisateur** : Utilisé dans des scripts où un utilisateur a oublié son mot de passe et doit le réinitialiser pour retrouver l'accès au système.

## Exceptions
- **Exigence d'un domaine d'application avec une URI publique** : L'étape nécessite un domaine d'application configuré avec une URI publique pour fonctionner correctement.
- **Dépendance à la méthode de notification de l'utilisateur** : L'efficacité de l'étape dépend de la fiabilité et de la disponibilité de la méthode de notification de l'utilisateur, comme l'email, utilisée pour envoyer un nouveau mot de passe.