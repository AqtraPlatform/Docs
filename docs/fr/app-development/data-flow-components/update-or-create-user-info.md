# Mettre à jour ou créer des informations utilisateur

![](../../assets/images/app-development/update-or-create-user-info.png)

## Informations générales
L'étape « Mettre à jour ou créer des informations utilisateur » est utilisée pour mettre à jour les informations d'un utilisateur existant ou créer un nouvel utilisateur. Cette étape fonctionne exclusivement avec le composant « Informations utilisateur ». Lorsque les informations de l'utilisateur sont mises à jour, si le mot de passe n'est pas spécifié, il restera inchangé.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur  | Objectif |
|---------------------|--------------------|------------|
| Nom de l'étape      | -                  | Nom de l'étape |
| Étape source        | -                  | Sélection de l'étape précédente |
| Champ d'informations utilisateur | -                  | Un champ contenant des informations sur l'utilisateur |
| Nom d'utilisateur    | -                  | Nom de l'utilisateur |
| Mot de passe utilisateur | -                  | Mot de passe de l'utilisateur (obligatoire) |
| Utilisateur désactivé | true, false       | Statut d'activité de l'utilisateur |
| Mettre à jour les champs | name, email, lastName, userName, firstName, middleName | Champs pour mettre à jour ou créer des informations utilisateur |

## Cas d'utilisation
- **Mise à jour des informations utilisateur** : Utilisé pour modifier les données concernant les utilisateurs existants, y compris leurs informations de contact, nom d'utilisateur et autres informations personnelles.
- **Création de nouveaux utilisateurs** : Adapté pour ajouter de nouveaux utilisateurs au système, vous permettant d'élargir rapidement et efficacement la base de données des utilisateurs.

## Exceptions
- **Besoin de précision des données** : L'étape nécessite une saisie de données précise et à jour, en particulier lors de la création de nouveaux utilisateurs.
- **Gestion des mots de passe** : Lorsque les informations de l'utilisateur sont mises à jour, si le mot de passe n'est pas spécifié, il restera inchangé. Lors de la création d'un utilisateur, la spécification d'un mot de passe est obligatoire.

## Scénario d'application

Le composant est conçu pour gérer les informations utilisateur. Il implique la récupération des informations utilisateur, la mise à jour de leurs données et la création d'un nouvel enregistrement utilisateur avec des paramètres spécifiés.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1zrn1vRmP3BtXAp-FBsoc5OHj96JuGKvF/view?usp=sharing)