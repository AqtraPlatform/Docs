# Case à cocher

![](../../assets/images/app-development/checkbox.png)

## Informations générales
Une “Case à cocher” est un élément d'interface qui permet aux utilisateurs de sélectionner ou de désélectionner un paramètre ou une option spécifique. Ce composant est largement utilisé pour créer des listes de paramètres, gérer des paramètres ou sélectionner plusieurs options à la fois.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient un champ “Boolean” lié du modèle |
| Événements | Valeur modifiée | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |

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
- **Sélection d'options** : Les utilisateurs peuvent sélectionner ou désélectionner certains paramètres ou options.
- **Gestion des paramètres** : La case à cocher est utilisée pour activer ou désactiver certains paramètres ou fonctionnalités.
- **Sélection multiple** : Dans le groupe de cases à cocher, les utilisateurs peuvent sélectionner plusieurs options en même temps.

## Exceptions
- **Interface peu intuitive :** Avec un grand nombre de cases à cocher sur une page ou dans des formulaires complexes, les utilisateurs peuvent avoir des difficultés à choisir des options.
- **Formulations peu claires :** Si les formulations des cases à cocher ne sont pas informatives ou claires, les utilisateurs peuvent ne pas comprendre ce qu'ils choisissent.