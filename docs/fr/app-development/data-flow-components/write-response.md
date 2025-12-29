# Écrire une réponse

![](../../assets/images/app-development/write-response.png)

## Informations générales
L'étape "Écrire une réponse" joue un rôle clé dans Dataflow, car elle est conçue pour renvoyer le résultat final à l'appelant. Cette étape est généralement la dernière étape de tout Dataflow, résumant et renvoyant les données reçues à la source demandeuse.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |

## Cas d'utilisation
- **Retourner les résultats du Dataflow** : Utilisé pour envoyer les résultats du processus de données Dataflow à l'appelant, ce qui peut être critique dans l'analyse de données et la gestion des erreurs.
- **Transformation des données avant la réponse** : Peut être combiné avec l'étape "Transformer le modèle" pour transformer ou filtrer les données avant qu'elles ne soient envoyées, vous permettant d'optimiser et de personnaliser le contenu de la réponse pour répondre aux exigences de l'appelant.

## Scénario d'application

Le composant contient des définitions de données personnalisées (définitions) et offre la possibilité de créer et de gérer des données à l'aide de flux de données. Il implémente des étapes pour récupérer des modèles de données (modèle d'action Get) et écrire des réponses (écrire une réponse), permettant aux utilisateurs d'interagir avec les données via l'interface utilisateur et d'interagir avec celles-ci sur le frontend de l'application.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1qNTgk1uYrMO3uUkDRmTO3i4En5mbG22i/view?usp=sharing).