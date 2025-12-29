# Bouton radio

![](../../assets/images/app-development/radio-button.png)

## Informations générales
Le composant “Bouton Radio” est un élément d'interface qui permet à l'utilisateur de sélectionner l'une des options fournies. Ce composant est utilisé pour implémenter la sélection d'un seul élément parmi plusieurs options mutuellement exclusives.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multiselect de Catalog | Contient un champ “Catalog” lié du modèle |
| Événements | Sur changement de valeur | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |
|  | Sur focus |  | Permet d'exécuter le script spécifié lorsqu'il est en focus |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | true, false | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les marges extérieures sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les rembourrages intérieurs sur tous les côtés de l'élément |
| Apparence | Rayon de coin | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de bord | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Bordure | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Sélection d'une seule option :** Les utilisateurs ne peuvent sélectionner qu'une seule option dans la liste.
- **Options mutuellement exclusives :** Le composant Bouton Radio est utilisé pour créer un ensemble d'options mutuellement exclusives dont une seule peut être sélectionnée.

## Exceptions
- **Informations insuffisantes :** Si les étiquettes des boutons radio ne sont pas suffisamment informatives, les utilisateurs peuvent avoir des difficultés à sélectionner des options.
- **Choix difficile :** Avec un grand nombre de boutons radio ou une organisation peu claire, le choix peut être difficile pour les utilisateurs.