# Connexion avec mot de passe

![](../../assets/images/app-development/login-with-password.png)

## Informations générales
L'étape « Connexion avec mot de passe » est utilisée pour créer une session utilisateur basée sur son nom d'utilisateur et son mot de passe. Cette étape permet à l'utilisateur d'être autorisé dans le système en vérifiant les informations d'identification fournies et, si la vérification est réussie, en créant une session utilisateur.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|---------------------|-------------------|----------|
| Nom de l'étape      | -                 | Nom de l'étape |
| Étape source        | -                 | Sélection de l'étape précédente |
| Nom d'utilisateur    | -                 | Nom d'utilisateur pour la connexion |
| Mot de passe utilisateur | -           | Mot de passe de l'utilisateur |
| Client pour la demande | -              | Client ou application qui initie la demande d'authentification |

## Cas d'utilisation
- **Authentification de l'utilisateur** : Étape utilisée dans les processus d'authentification où les utilisateurs saisissent leurs informations d'identification pour accéder au système ou à ses fonctionnalités.
- **Contrôle d'accès** : Convient aux systèmes qui nécessitent que les informations d'identification de l'utilisateur soient vérifiées avant d'accorder l'accès à certaines ressources ou fonctionnalités.

## Exceptions
- **Nécessité de précision des informations d'identification** : L'efficacité de l'étape dépend de la précision des informations d'identification saisies (nom d'utilisateur et mot de passe).
- **Gestion des tentatives de connexion échouées** : Il est important de gérer correctement les tentatives de connexion échouées pour éviter des risques de sécurité potentiels tels que les attaques par force brute. Cela nécessite la mise en œuvre de mécanismes pour limiter le nombre de tentatives de connexion ou bloquer temporairement l'accès après plusieurs tentatives infructueuses.

## Scénario d'application

Le scénario implémente la connexion de l'utilisateur au système en utilisant un nom d'utilisateur et un mot de passe. Après avoir initié le flux de données et saisi le nom d'utilisateur et le mot de passe dans les champs correspondants de l'interface utilisateur, l'étape « Connexion avec mot de passe » authentifie l'utilisateur. Ensuite, en utilisant l'étape « Action de formulaire », le composant sélectionné est ouvert.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1Kb9QNcCHXqetQmXGvBHScQSiRlA-542s/view?usp=sharing)