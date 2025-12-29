# Interrupteur

![](../../assets/images/app-development/switch.png)

## Informations générales
Le composant “Interrupteur” est un élément d'interface qui permet à l'utilisateur d'activer ou de désactiver une fonction, une option ou un état spécifique. Ce composant est souvent utilisé pour fournir la possibilité de basculer rapidement entre deux états (Vrai/Faux).

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient un champ “Catalogue” lié du modèle |
| Événements | Valeur changée | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | true, false | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les espacements extérieurs sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les espacements intérieurs sur tous les côtés de l'élément |
| Apparence | Rayon de coin | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de bord | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Bordure | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Sélection binaire :** L'interrupteur est utilisé pour des sélections binaires telles que activer/désactiver le son, les notifications et d'autres options.
- **Gestion d'état :** Vous pouvez utiliser l'interrupteur pour gérer l'état d'un élément d'interface particulier.

## Exceptions
- **Statut peu clair :** S'il n'est pas évident ce que signifient les statuts activé et désactivé, les utilisateurs peuvent être confus.