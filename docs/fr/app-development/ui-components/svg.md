# SVG

![](../../assets/images/app-development/svg.png)

## Informations générales
SVG (Scalable Vector Graphics) est un composant pour intégrer des graphiques vectoriels dans les interfaces utilisateur. Il permet d'afficher des images, ce qui le rend idéal pour les icônes, les diagrammes et les illustrations complexes.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Liaison | Multisélection de Catalogue | Contient un champ “Fichier” associé du modèle |
|  | Fichier | Bouton | Permet de télécharger un fichier avec une extension .svg |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | true, false | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les espacements extérieurs sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les espacements intérieurs sur tous les côtés de l'élément |
| Apparence | RayonDesCoins | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | ÉpaisseurDeBordure | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | BordureBrosse | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Icônes et Illustrations** : Utilisé pour ajouter des éléments graphiques clairs et évolutifs.

## Exceptions
- **Performance** : Des images SVG complexes ou volumineuses peuvent affecter les performances des pages web.