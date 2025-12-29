# Temps

![](../../assets/images/app-development/time.png)

## Informations générales
Le temps est un composant UI conçu pour entrer et afficher l'heure. Cet élément est généralement utilisé pour définir l'heure des événements ou des tâches, et pour afficher l'heure dans les interfaces d'application.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient un champ "Temps" lié du modèle |
| Événements | Sur changement de valeur | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |

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
- **Réglage de l'heure** : Utilisé pour définir une heure spécifique dans les planificateurs et les calendriers.
- **Saisie de l'heure** : Fournit une interface pour que l'utilisateur entre l'heure à diverses fins.

## Exceptions
- **Formatage de l'heure** : Vous devez être conscient des restrictions de format d'heure définies dans les paramètres du composant.
- **Heure uniquement** : Le composant Temps est limité à l'affichage et à la saisie uniquement de l'heure, sans dates.