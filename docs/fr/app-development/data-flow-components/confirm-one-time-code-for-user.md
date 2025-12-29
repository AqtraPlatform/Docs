# Confirmer le code à usage unique pour l'utilisateur

![](../../assets/images/app-development/confirm-one-time-code-for-user.png)

## Informations générales
L'étape "Confirmer le code à usage unique pour l'utilisateur" est utilisée pour confirmer le code à usage unique qui a été généré pour l'utilisateur dans l'étape précédente "Obtenir le code à usage unique pour l'utilisateur". Cette étape est la clé du processus d'authentification à deux facteurs, vous permettant de vérifier la validité du code saisi par l'utilisateur pour accéder au système.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Champ de code utilisateur | -         | Le champ dans lequel l'utilisateur saisit le code reçu pour confirmation |

## Cas d'utilisation
- **Confirmation de l'authentification à deux facteurs** : Appliqué pour compléter le processus d'authentification à deux facteurs en exigeant que les utilisateurs saisissent le code qui leur a été envoyé dans l'étape précédente.
- **Renforcement de la sécurité d'accès** : Utilisé dans des scénarios où un contrôle d'accès système renforcé est nécessaire pour prévenir les connexions non autorisées.

## Exceptions
- **Dépendance à la justesse du code saisi** : L'efficacité de l'étape dépend de l'exactitude de la saisie du code par l'utilisateur.
- **Validité limitée du code** : Si le code expire, il doit être réémis, ce qui peut entraîner des retards dans l'authentification.

## Scénario d'application

Le composant crée un flux de données pour confirmer le code à usage unique de l'utilisateur. L'étape du modèle d'action Get est utilisée pour récupérer les données du modèle. Ensuite, le code de la variable ForTestCode est nettoyé des caractères inutiles et stocké dans la variable _code à l'aide de l'étape Exécuter le script. L'étape Confirmer le code à usage unique pour l'utilisateur est utilisée pour confirmer le code à usage unique en utilisant la valeur _code comme code de l'utilisateur. Enfin, le résultat est transmis par l'étape Écrire la réponse.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1_uPyqNOuOddurvwz-KteaoIIRQjgEzBH/view?usp=sharing)