# Extraction de collection

![](../../assets/images/app-development/extract-collection.png)

## Informations générales
L'étape "Extraction de collection" est utilisée pour convertir un champ de tableau en une liste plate. Ce champ peut être obtenu soit à partir d'une source externe, soit à partir d'un champ (propriété) d'un composant de tableau.

À cette étape, le tableau est analysé et le traitement de chaque élément du tableau (entrée ou objet) est lancé en tant que flux de données interne séparé. Chaque fil d'exécution est exécuté indépendamment des autres. Les flux de données analysés à l'aide de l'étape "Extraction de collection" peuvent être réassemblés via l'étape "Grouper par".

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Chemin du modèle   | -                 | Chemin vers un champ de tableau dans le modèle de données |

## Cas d'utilisation
- **Traitement de tableau de données** : Utilisé pour extraire et traiter chaque élément du tableau de données de manière indépendante.
- **Division et regroupement ultérieur** : Adapté aux scénarios où vous devez diviser des structures de données complexes en éléments plus simples pour un traitement et une analyse ultérieurs.

## Exceptions
- **Besoin de spécifier la source et le chemin exacts** : Une indication incorrecte de la source ou du chemin vers le champ de tableau peut entraîner des erreurs dans le traitement des données.

## Scénario d'application

Ce composant permet de traiter les données d'entrepôt client en ajoutant de nouveaux enregistrements à l'aide des étapes **extraction de collection** et **exécuter le script**. Après l'exécution du flux de données, chaque enregistrement reçoit des données de champ supplémentaires.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1Q1czyILIGHc7tVwPYpkgHIFfI87p5WvQ/view?usp=sharing).