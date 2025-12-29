# Visionneuse de PDF

![](../../assets/images/app-development/pdf-viewer.png)

## Informations générales
Le composant Visionneuse de PDF vous permet de visualiser et d'interagir avec des documents PDF directement dans l'interface utilisateur. Ce composant est utile pour afficher des fichiers PDF tels que des rapports, des instructions et d'autres documents.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Liaison | Multisélection de Catalogue | Contient un champ “Fichier” associé du modèle |
|  | Fichier | Bouton | Permet de télécharger un fichier avec une extension .pdf |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | true, false | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les espacements extérieurs sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les espacements intérieurs sur tous les côtés de l'élément |
| Apparence | RayonDeCoin | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | ÉpaisseurDeBordure | - | La propriété vous permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | BrosseDeBordure | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Visualisation de rapports :** Permet aux utilisateurs de visualiser des rapports et de la documentation au format PDF.

## Exceptions
- **Limitations de format :** La Visionneuse de PDF prend en charge les documents PDF standard mais peut ne pas afficher correctement les formats complexes ou les documents protégés.
- **Performance :** L'utilisation de documents PDF volumineux ou d'un grand nombre d'éléments interactifs peut affecter les performances.