# Barre de progression

![](../../assets/images/app-development/progress-bar.png)

## Informations générales
Ce composant UI est utilisé pour afficher et configurer la barre de progression.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif  |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Afficher la valeur | true, false | La propriété est utilisée pour afficher les valeurs de la barre de progression |
|  | Déterminé | true, false | La propriété permet de rendre la barre de progression une animation |
|  | Inverser | true, false | La propriété permet d'inverser la barre de progression |
|  | Format | - | La propriété permet de spécifier le format de sortie des données |
|  | Valeur | - | La propriété permet de définir une valeur |
|  | Liaison | Multisélection de Catalogue | Contient le champ “Integer” associé du modèle |
|  | Valeur minimale | - | La propriété permet de spécifier une valeur minimale |
|  | Liaison | Multisélection de Catalogue | Contient le champ “Integer” associé du modèle pour la valeur minimale  |
|  | Valeur maximale | - | La propriété permet de spécifier une valeur maximale |
|  | Liaison | Multisélection de Catalogue | Contient le champ “Integer” associé du modèle pour la valeur maximale  |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croître | true, false | La propriété détermine combien un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les espacements extérieurs sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les espacements intérieurs sur tous les côtés de l'élément |
| Apparence | Rayon des coins | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de la bordure | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Bordure | - | La propriété définit la couleur de la bordure de l'élément |
|  | Progression | - | La propriété définit la couleur de la barre de l'élément |

## Cas d'utilisation
- Affichage de la progression des tâches, des téléchargements ou d'autres processus.

## Exceptions
- Limité à l'utilisation pour la présentation de la progression et non adapté à d'autres types de visualisations.