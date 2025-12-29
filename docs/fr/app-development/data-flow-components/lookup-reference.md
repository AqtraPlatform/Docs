# Référence de recherche

![](../../assets/images/app-development/lookup-reference.png)

## Informations générales
L'étape "Référence de recherche" est utilisée pour rechercher des références aux instances de composants par des clés externes. Ce processus nécessite qu'au moins une propriété avec le drapeau "Clé primaire" soit configurée dans le composant à rechercher.

La recherche est effectuée par cette propriété, et le résultat de la recherche sous la forme d'Id (entier) de l'enregistrement trouvé sera enregistré dans la variable spécifiée dans le "Nom du champ". Si aucune instance d'un composant avec une telle clé n'est trouvée, la variable sera nulle.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Composant          | -                 | Composant qui est recherché |
| Nom du champ       | -                 | Nom du champ où le résultat de la recherche sera enregistré |

## Cas d'utilisation
- **Recherche de clé primaire** : Utilisé pour déterminer la disponibilité et identifier les instances de composants par des identifiants uniques.
- **Liaison de données de composants** : Convient aux scripts où vous souhaitez lier des données de différents composants en fonction de clés uniques.

## Exceptions
- **Exigence de clé primaire** : Le composant doit avoir une clé primaire configurée pour garantir une recherche réussie.
- **Gestion des enregistrements manquants** : S'il n'y a pas d'instance avec la clé spécifiée, la valeur de la variable sera nulle, ce qui peut nécessiter un traitement supplémentaire.

## Scénario d'application

Ce composant utilise l'étape de Référence de recherche pour trouver l'ID d'enregistrement dans la table "Tâche de tri" en fonction du numéro de tri saisi. Après avoir saisi le numéro de tri et exécuté le flux de données, l'ID d'enregistrement correspondant est affiché sur le frontend.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1LZzqHGc7I5IdAVLmK6H1_ItODiiruSAJ/view?usp=sharing)