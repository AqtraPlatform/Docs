# Sélectionner plusieurs

![](../../assets/images/app-development/select-many.png)

## Informations générales
L'étape "Sélectionner plusieurs" est utilisée pour convertir un champ de type tableau en une liste plate. Contrairement à l'étape "Extraire la collection", "Sélectionner plusieurs" préserve les données du modèle de l'étape précédente et ajoute des valeurs "parent" avec un préfixe `$parent` pour chaque élément du tableau. Cela permet non seulement d'étendre le tableau, mais aussi de préserver le contexte de l'entrée parent.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Chemin du modèle   | -                 | Chemin vers un champ de tableau dans le modèle de données |

## Cas d'utilisation
- **Expansion et préservation du contexte** : Utilisé pour convertir des tableaux de données en une liste plate tout en préservant la relation avec les données parent.
- **Traitement de structures hiérarchiques** : Adapté pour des scripts où vous devez traiter des données provenant de tableaux sans perdre la connexion avec les éléments de données "parent".

## Exceptions
- **Traitement de grands tableaux** : Le traitement de grands tableaux peut être plus intensif en ressources en raison de la nécessité de préserver le contexte des données parent.

## Scénario d'application

Ce composant est un outil pour créer et gérer des flux de données au sein de l'application. L'étape 'Sélectionner plusieurs' dans ce composant est utilisée pour choisir plusieurs éléments à partir d'un tableau de données obtenu à l'étape précédente du flux de données. Le composant permet aux utilisateurs de définir des conditions de sélection et de traitement des données selon leurs besoins.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1T9k35m8cg56vmM68LCT0brMeYQ2JIJ6U/view?usp=sharing).