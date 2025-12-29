# Exécuter le script

![](../../assets/images/app-development/execute-script.png)

## Informations générales
L'étape "Exécuter le script" est conçue pour exécuter des scripts Python en utilisant des bibliothèques Python standard.

Cette étape vous permet d'exécuter des scripts Python de toute complexité tout en travaillant avec le modèle de flux de données actuel. À l'aide du script, vous pouvez modifier le modèle en ajoutant de nouvelles variables ou en changeant les valeurs des variables existantes.

Exemples d'utilisation :
- Pour obtenir la valeur d'une variable à partir de l'étape "modèle d'action de récupération" : `item ['data'] ['Property_name'] `
- Pour créer une nouvelle variable dans le script : `item ['Property_name'] `

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|---------------------|-------------------|----------|
| Nom de l'étape      | -                 | Nom de l'étape |
| Étape source        | -                 | Sélection de l'étape précédente |

## Cas d'utilisation
- **Personnalisation du traitement des données** : Convient pour une logique de traitement des données complexe qui ne peut pas être mise en œuvre avec des outils de flux de données standard.
- **Ajout et modification de données** : Convient pour des scénarios nécessitant l'ajout de nouvelles données ou la modification de données existantes dans le modèle.

## Exceptions
- **Nécessité de compétences en Python** : Nécessite des connaissances en Python et une compréhension de la logique de travail avec le flux de données.
- **Typage des variables** : Un typage strict des variables peut nécessiter une attention supplémentaire lors de l'écriture des scripts. Types pris en charge : `@number`, `@integer`, `@string`, `@uuid`, `@boolean`, `@uri`, `@date`, `@date-time`, `@time`, `@catalog`, `@array`.

## Scénario d'application

Ce composant présente divers scénarios d'utilisation de l'étape Exécuter le script au sein d'un flux de données, y compris la création de nouvelles variables de différents types et la modification des valeurs des champs disponibles dans le modèle de données.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/18fbg2g2rcvXORI7i31zu81NdSKwMqE99/view?usp=sharing)