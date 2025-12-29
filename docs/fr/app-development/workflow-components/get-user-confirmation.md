# Obtenir la confirmation de l'utilisateur

![](../../assets/images/app-development/get-user-confirmation.png)

## Informations générales
L'étape "Obtenir la confirmation de l'utilisateur" dans le flux de travail est utilisée pour demander une confirmation ou effectuer une action de l'utilisateur. L'étape envoie une notification à l'utilisateur avec une demande d'effectuer une action spécifique sur l'objet, où l'objet est l'état du modèle actuel.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre   | Options de valeur     | Objectif |
|----------------------|-----------------------|----------|
| Nom de l'étape       | -                     | Nom de l'étape "Obtenir la confirmation de l'utilisateur" |
| Champ de confirmation | -                     | Champ avec les options à demander à l'utilisateur |
| Champ d'informations utilisateur | Multisélection de Catalogue | Champ contenant des informations sur un utilisateur ou un groupe d'utilisateurs |
| Routage utilisateur   | Multisélection de Catalogue | Objet qui constitue un contexte de sécurité |

## Cas
- **Demande de confirmation de l'utilisateur** : Idéal pour les scripts qui nécessitent une confirmation ou un choix d'action de l'utilisateur, comme confirmer une transaction, accepter le traitement des données ou choisir une option de réponse.
- **Participation interactive de l'utilisateur au processus** : Convient à un flux de travail, où il est important de prendre en compte les décisions ou choix de l'utilisateur pour continuer ou modifier le processus.

## Exceptions
- **Assurer que la demande est claire** : Il est important de formuler clairement la demande de confirmation afin que l'utilisateur comprenne quelle action est attendue de sa part.
- **Gestion des réponses des utilisateurs** : Les réponses des utilisateurs doivent être traitées de manière adéquate et prises en compte, en particulier dans les situations où elles déterminent le cours des actions ultérieures dans le flux de travail.
- **Prendre en compte le contexte de sécurité et les autorisations** : Lors de l'utilisation du paramètre de routage utilisateur, il est important de considérer le contexte de sécurité et les autorisations correspondantes de l'utilisateur.