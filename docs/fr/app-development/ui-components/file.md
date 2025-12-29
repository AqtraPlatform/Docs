# Fichier

![](../../assets/images/app-development/file.png)

## Informations générales
Le composant “Fichier” permet de charger et d'afficher des fichiers dans l'interface utilisateur. Ce composant est utile pour télécharger et visualiser différents types de fichiers, tels que des images, des documents, des archives, etc.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Taille maximale du fichier en octets | - | La propriété permet de spécifier la taille maximale du fichier téléchargé en octets |
|  | Accepter les fichiers |  | La propriété permet de spécifier les fichiers qui sont disponibles pour le téléchargement |
|  | Lecture seule | true, false | Cette propriété permet de désactiver le téléchargement de fichiers dans les formulaires |
|  | Désactivé | true, false | La propriété permet de désactiver un élément dans le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Valeur | - | - |
|  | Liaison | Choix multiple : Catalogue | Référence au Catalogue de type Fichier |
| Événements | Valeur changée | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | true, false | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les espacements extérieurs sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les espacements intérieurs sur tous les côtés de l'élément |
| Apparence | Rayon des coins | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de la bordure | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Couleur de la bordure | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Téléchargement de documents** : Permet aux utilisateurs de télécharger des documents, des images et d'autres fichiers.
- **Afficher les informations sur le fichier :** Affiche des informations sur le fichier téléchargé, telles que son nom et sa taille.

## Exceptions
- **Performance** : Le téléchargement de fichiers volumineux ou d'un grand nombre de fichiers peut affecter les performances.