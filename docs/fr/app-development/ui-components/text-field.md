# Champ de texte

![](../../assets/images/app-development/text-field.png)

## Informations générales
Le “Champ de texte” est un composant d'interface utilisateur conçu pour afficher et configurer l'entrée et la sortie de texte.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant d'interface utilisateur dans le système |
| Commun | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient un champ “String” lié du modèle |
| Événements | Sur changement de valeur | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |
| Index de tabulation |  | Entier positif commençant à zéro | Définit l'ordre dans lequel les champs actifs (éditables) sont basculés via le clavier (par exemple, en utilisant la touche Tab) |

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
|  | Bordure de brosse | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Formulaires de saisie de données** : Utilisé pour collecter des informations textuelles auprès des utilisateurs.
- **Paramètres d'interface** : Fournit une interface utilisateur pour entrer ou modifier du texte.

## Exceptions
- **Fonctionnalité limitée** : Convient uniquement pour l'entrée de texte.