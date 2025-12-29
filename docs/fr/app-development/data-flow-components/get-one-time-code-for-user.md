# Obtenir un code à usage unique pour l'utilisateur

![](../../assets/images/app-development/get-one-time-code-for-user.png)

## Informations générales
L'étape « Obtenir un code à usage unique pour l'utilisateur » est utilisée pour générer et envoyer un code à usage unique pour se connecter dans le cadre de l'authentification à deux facteurs. Cette étape fonctionne en conjonction avec l'étape « Confirmer le code à usage unique pour l'utilisateur » et est généralement appliquée en utilisant la fonctionnalité « Envoyer une notification modélisée ».

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|---------------------|-------------------|----------|
| Nom de l'étape      | -                 | Nom de l'étape |
| Étape source        | -                 | Sélection de l'étape précédente |
| Nom d'utilisateur    | -                 | Nom ou ID de l'utilisateur pour lequel le code est généré |
| Client pour la demande | -               | Client ou application qui initie la demande de confirmation |
| Durée de vie du code | -                 | La durée de vie d'un code |

## Cas d'utilisation
- **Authentification à deux facteurs** : Utilisé pour fournir une couche de sécurité supplémentaire lors de la connexion en générant un code temporaire que l'utilisateur doit confirmer.
- **Sécurité de connexion renforcée** : Adapté aux scénarios où des mesures de sécurité renforcées sont nécessaires pour prévenir l'accès non autorisé au système.

## Exceptions
- **Dépendance à l'exactitude des données utilisateur** : L'exactitude et la pertinence des informations utilisateur sont critiques pour la génération et l'envoi réussis d'un code à usage unique.
- **Gestion de la durée de vie du code** : Vous devez configurer correctement la durée de vie du code pour garantir que votre code est à jour et éviter les problèmes d'accès utilisateur.

## Scénario d'application

Le composant ajoute une nouvelle définition de chaîne ForTestCode. Un flux de données est créé où un code à usage unique pour l'utilisateur est obtenu via le modèle d'action Get et les étapes Get user info. L'étape Exécuter le script est utilisée pour passer ce code dans la variable new_code, qui est ensuite stockée dans la définition ForTestCode du composant et affichée dans une fenêtre modale.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing)