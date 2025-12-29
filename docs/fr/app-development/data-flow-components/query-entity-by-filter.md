# Interroger une entité par filtre

![](../../assets/images/app-development/query-entity-by-filter.png)

## Informations générales
L'étape "Interroger une entité par filtre" est utilisée pour rechercher des entrées dans un composant spécifique. Contrairement aux étapes, qui utilisent des filtres ou des identifiants pour rechercher, cette étape est conçue pour rechercher directement des entrées dans un composant.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélectionner l'étape précédente |
| Composant          | -                 | Composant qui est recherché |
| Nom du champ de destination | -         | Nom du champ dans lequel le résultat de la requête sera enregistré |

## Cas
- **Recherche directe dans le composant** : Utilisé pour rechercher directement des entrées dans un composant spécifique.

## Exceptions
- **Dépendance au composant** : L'efficacité de l'étape est directement liée à la structure et au contenu des données dans le composant sélectionné.

## Scénario d'application

Le flux de données démontre divers scénarios d'utilisation de l'interrogation d'entité par filtre pour le filtrage des données. Chaque scénario comprend l'ajout de l'étape Modèle d'Action Get et de l'étape Interroger une entité par filtre, le remplissage des champs et l'application des filtres, ainsi qu'une étape Écrire la réponse pour la sortie des résultats.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1FBXtSNuk7-KmyGofhghsJJiVrV_xebT1/view?usp=sharing)