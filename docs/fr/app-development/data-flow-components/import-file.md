# Fichier d'importation

![](../../assets/images/app-development/import-file.png)

## Informations générales
L'étape "Fichier d'importation" est utilisée pour importer des données à partir de fichiers .csv, Excel ou JSON. Les données sont importées ligne par ligne, en se mappant au format décrit dans "Mapping des champs". Pour importer un fichier, vous devez charger le fichier dans le champ de type Fichier et spécifier ce champ dans le paramètre "Champ d'informations sur le fichier".

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre    | Options de valeur | Objectif |
|-----------------------|-------------------|----------|
| Nom de l'étape        | -                 | Nom de l'étape |
| Étape source          | -                 | Sélection de l'étape précédente |
| Champ d'informations sur le fichier | -                 | Champ contenant le fichier à importer |
| Type de fichier d'entrée | .csv, .xlsx, .json| Format de fichier pour l'importation |
| Séparateur de colonnes | ;                 | Séparateur de colonnes pour le fichier CSV |
| Premières lignes à ignorer | 0             | Nombre de premières lignes à ignorer dans le fichier |
| Mapping des champs    | -                 | Mapping des champs de composant aux colonnes du fichier |

## Cas d'utilisation
- **Importer des données tabulaires** : Utilisé pour charger des données à partir de fichiers CSV ou Excel, en personnalisant le mapping entre les colonnes du fichier et les champs de composant.
- **Importer des données structurées** : Adapté pour importer des fichiers JSON contenant des données structurées.

## Exceptions
- **Mapping des champs incorrect** : Des erreurs dans le paramètre "Mapping des champs" peuvent entraîner une importation de données incorrecte.
- **Ignorer les lignes non informatives** : Vous devez spécifier exactement le nombre de lignes à ignorer avant de commencer à importer des données.

## Scénario d'application

Ce composant est une interface pour télécharger des fichiers aux formats **CSV** et **XLSX**. Il comprend des champs pour trois champs de modèle de données **CSV** et trois champs de modèle de données **XLSX**, ainsi qu'un champ pour le téléchargement de fichiers. Deux flux de données sont utilisés pour l'importation de fichiers, l'exécution de scripts et le stockage de données.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/10P0-XqSZOKV7wZzg8uH6NR1VnxZ0-8RB/view?usp=sharing)