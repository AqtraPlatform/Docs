# Regrouper par

![](../../assets/images/app-development/group-by.png)

## Informations générales
L'étape "Regrouper par" est utilisée pour collecter et regrouper les données divisées dans les étapes précédentes, par exemple, en utilisant l' "Extraction de collection". La fonction principale de cette étape est de regrouper les données par des clés spécifiques spécifiées par l'utilisateur. L'étape collecte les données divisées et combine uniquement les entrées qui correspondent aux clés spécifiées.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|---------------------|-------------------|----------|
| Nom de l'étape      | -                 | Nom de l'étape |
| Étape source        | -                 | Sélection de l'étape précédente |
| Clés                | -                 | Clés utilisées pour regrouper les données |

## Cas d'utilisation
- **Combinaison de données divisées** : Utilisé pour combiner des données divisées dans les étapes précédentes, telles que l' "Extraction de collection", en utilisant des clés spécifiques.
- **Segmentation et analyse des données** : Convient aux cas où il est nécessaire d'analyser les données selon des catégories ou critères spécifiques.

## Exceptions
- **Dépendance aux clés de regroupement** : L'exactitude et la pertinence des clés sont essentielles pour regrouper correctement les données.
- **Difficulté dans le traitement et l'analyse des données** : Le regroupement peut être difficile si la structure des données est variée ou si les clés n'identifient pas les groupes de manière unique.

## Scénario d'application

Ce composant vérifie la disponibilité des champs dans l'étape Regrouper par. Dans le flux de données, d'abord, une étape de modèle d'action Get et une étape Regrouper par sont ajoutées. Ensuite, sur le frontend, le composant importé est ouvert, et l'onglet "Réseau" dans les outils de développement du navigateur est ouvert. Après cela, le bouton "Regrouper par" est cliqué sur le frontend. Si l'étape fonctionne correctement, une ligne "exécuter" avec un aperçu de la réponse HTTP devrait apparaître dans l'onglet Réseau, contenant des données avec la clé "ETO test123" et leur agrégation.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1fKeJh3a0HHcG7VuFs-Tx5YdS7H6C7mI0/view?usp=sharing).