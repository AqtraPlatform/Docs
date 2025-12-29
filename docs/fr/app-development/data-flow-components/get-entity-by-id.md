# Obtenir une entité par ID

![](../../assets/images/app-development/get-entity-by-id.png)

## Informations générales
L'étape "Obtenir une entité par ID" est utilisée pour obtenir un élément de composant par son identifiant unique (ID). Cette étape est généralement utilisée en combinaison avec d'autres étapes, telles que "Recherche" ou "Mettre à jour l'entrée", qui renvoient un ID approprié pour cette étape.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Champ Src          | -                 | Champ contenant l'ID à rechercher |
| Nom du champ Dst   | -                 | Champ où le résultat sera enregistré |
| Composant          | -                 | Composant qui est recherché |

## Cas
- **Recherche de données par ID** : Utilisé pour récupérer avec précision une entrée spécifique en utilisant l'ID du composant.

## Exceptions
- **Dépendance à l'exactitude de l'ID** : L'ID exact doit être spécifié et disponible dans les données source pour que la requête soit réussie.
- **Gestion des incohérences** : S'il n'y a pas d'entrée avec l'ID spécifié, l'étape peut renvoyer un résultat vide.

## Scénario d'application

Ce composant permet d'ajouter un champ de type catalogue et de créer un flux de données pour récupérer une entité par son identifiant. Le champ de type catalogue est placé sur la page pour sélectionner la valeur correspondante dans le catalogue. Le flux de données comprend une étape 'Obtenir le modèle d'action' pour l'initialisation, une étape 'Obtenir une entité par ID' pour récupérer l'entité par identifiant en utilisant la valeur sélectionnée dans le catalogue, et une étape 'Écrire la réponse' pour afficher le résultat.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1eCxoYHKg0Zl8APxnUMRA9qmpqNkrtfuW/view?usp=sharing).