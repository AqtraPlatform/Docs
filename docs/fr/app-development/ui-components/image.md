# Image

![](../../assets/images/app-development/image.png)

## Informations générales
Le composant Image est utilisé pour afficher des images dans l'interface utilisateur. Ce composant est un élément clé pour la visualisation et peut être utilisé pour afficher des photos, des illustrations et d'autres éléments graphiques.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Liaison | Multisélection de Catalogue | Contient un champ “Fichier” associé du modèle |
|  | Fichier | Bouton | Permet de télécharger un fichier avec les extensions .png, .jpg et .svg |
| | Afficher l'image de remplacement | Vrai, Faux | Affichage de l'image de remplacement |
| | Pas d'image de remplacement | Choisir un fichier sur le disque, choisir un fichier dans le stockage | Image de remplacement si aucune image n'est chargée | 

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croître | vrai, faux | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les marges extérieures sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les rembourrages intérieurs sur tous les côtés de l'élément |
| Apparence | Rayon des coins | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de la bordure | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Brosse de bordure | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Affichage de photos :** Utilisé pour afficher des photos personnalisées, des images de produits et d'autres objets.
- **Illustrations et graphiques :** Applicable pour afficher des illustrations, des éléments graphiques et des logos.

## Exceptions
- **Performance :** L'utilisation d'images grandes ou multiples sur une page peut affecter la performance.