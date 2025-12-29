# Sélectionner

![](../../assets/images/app-development/select.png)

## Informations générales
“Sélectionner” est un élément d'interface qui permet à l'utilisateur de choisir une option parmi la liste présentée. Ce composant est largement utilisé pour créer des listes déroulantes avec un choix d'options ou de catégories.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient un champ “Catalogue” lié du modèle |
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
|  | Bordure | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Sélection dans la liste :** Les utilisateurs peuvent sélectionner une option parmi une liste d'options suggérées.

## Exceptions
- **Interface peu intuitive :** Si la liste n'est pas intuitive ou compréhensible pour l'utilisateur, cela peut entraîner des difficultés à sélectionner une option.
- **Vitesse de téléchargement :** Si la liste est trop longue, le chargement des éléments sélectionnés nécessitera une attente supplémentaire.