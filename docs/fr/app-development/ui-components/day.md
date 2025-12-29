# Jour

![](../../assets/images/app-development/day.png)

## Informations générales
Le composant Jour est un élément d'interface utilisateur conçu pour afficher ou sélectionner des jours individuels. Cet élément est couramment utilisé dans les calendriers ou les capteurs de date, permettant à l'utilisateur de sélectionner des jours spécifiques pour accomplir des tâches ou définir des rappels.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Format | - | La propriété permet de [configurer](https://docs.microsoft.com/ru-ru/dotnet/standard/base-types/custom-date-and-time-format-strings) l'affichage de la date et de l'heure |
|  | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient un champ "Date" associé du modèle |
| Événements | Sur changement de valeur | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |

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
|  | Brosse de bord | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Sélecteur de date** : Utilisé pour sélectionner des jours spécifiques dans des interfaces où une sélection de date précise est requise.
- **Affichage d'événements** : Peut être utilisé pour afficher des événements ou des rappels programmés pour des jours spécifiques.

## Exceptions
- **Fonctionnalité limitée** : Le composant Jour est limité à l'affichage et à la sélection de jours, et n'est pas adapté pour afficher des intervalles de temps plus larges.