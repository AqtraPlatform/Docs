# Modèle de transformation

![](../../assets/images/app-development/transform-model.png)

## Informations générales
L'étape "Modèle de transformation" est utilisée pour mapper et transformer les champs dans le modèle de données. Cela implique de changer les noms des champs et de supprimer les champs inutiles du modèle. L'étape crée une nouvelle copie du modèle de flux de données, vous permettant de modifier sa structure, ce qui est souvent utilisé pour minimiser la réponse en tant que modèle de données. Elle peut également être utilisée pour optimiser le modèle de données après avoir effectué plusieurs opérations de regroupement (Group by).

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Mappage des champs | -                 | Mappage et changement des champs dans le modèle de données |

## Cas d'utilisation
- **Optimisation du modèle de données** : Utilisé pour changer la structure du modèle de données, y compris le renommage ou la suppression de champs.

## Exceptions
- **Importance d'un mappage précis** : Des erreurs dans le paramètre "Mappage des champs" peuvent entraîner des modifications indésirables du modèle de données.
- **Dépendance aux données sources** : L'application correcte de l'étape nécessite une compréhension précise de la structure des données sources.

## Scénario d'application

Ce composant contient un flux de données utilisé pour la transformation des données selon des règles spécifiées. Le flux de données comprend des étapes telles que Extraire la collection et Exécuter le script, qui permettent d'ajouter de nouveaux enregistrements aux tableaux de données des clients.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1buQNdkjcnY8wgIUM9TjjI7KoikEcSmv3/view?usp=sharing)