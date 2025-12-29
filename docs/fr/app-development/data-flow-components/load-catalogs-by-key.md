# Charger des catalogues par clé

![](../../assets/images/app-development/load-catalogs-by-key.png)

## Informations générales
L'étape « Charger des catalogues par clé » fonctionne de manière similaire à l'étape « Obtenir l'entité par ID », mais au lieu de nécessiter un ID de composant spécifique, elle identifie automatiquement tout champ de type Catalogue dans le modèle de données. En fonction du choix de l'utilisateur, l'étape récupère l'entrée complète liée au champ de type Catalogue sélectionné. Ainsi, elle vous permet d'obtenir des informations complètes à partir de tout lien dans les données sans avoir à spécifier un ID spécifique.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |

## Cas d'utilisation
- **Identification automatique et téléchargement des données liées** : Utilisé pour identifier et charger automatiquement les données liées aux champs de Catalogue.
- **Extraction de données flexible** : Convient aux scripts qui nécessitent de la flexibilité dans la sélection et l'extraction de données à partir de divers composants liés.

## Exceptions
- **Charge excessive lors du travail avec un grand nombre de catalogues** : S'il y a un grand nombre de catalogues ouverts, cela peut prendre un temps supplémentaire pour les traiter.
- **Remplacement injustifié de l'étape « Obtenir l'entité par ID » par l'étape « Charger des catalogues par clé » :** Si le nombre de catalogues liés ne dépasse pas quelques-uns, il est préférable d'utiliser l'étape « Obtenir l'entité par ID » pour de meilleures performances.

## Scénario d'application

Ce composant vous permet de créer un flux de données à partir de l'obtention d'un modèle de données vide. Ensuite, il est utilisé pour récupérer l'identifiant d'enregistrement avec des catalogues, après quoi il charge ces catalogues et affiche leurs données sur le frontend.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1_GImBJ3UCDo-T1dL6c85-wWgcUfpJIz3/view?usp=sharing).