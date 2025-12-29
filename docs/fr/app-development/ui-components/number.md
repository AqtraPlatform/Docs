# Nombre

![](../../assets/images/app-development/number.png)

## Informations générales
Le composant “Nombre” est une interface pour entrer des valeurs numériques. Ce composant permet aux utilisateurs d'entrer des nombres et peut être utilisé à diverses fins telles que l'entrée de nombres, de quantités ou d'autres données numériques.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient le champ “Integer” et “Number” associé du modèle |
| Événements | Sur changement de valeur | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | true, false | La propriété détermine combien un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les espacements extérieurs sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les espacements intérieurs sur tous les côtés de l'élément |
| Apparence | Rayon de coin | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de bord | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Bordure | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Entrée de valeurs numériques :** Les utilisateurs peuvent entrer des nombres dans le composant Nombre, tels que des quantités de produits ou des paramètres numériques.
- **Limite de plage :** Les valeurs minimales et maximales permettent de limiter les nombres que vous entrez à une plage spécifique.
- **Changer le nombre à l'aide des flèches :** Les utilisateurs peuvent augmenter ou diminuer un nombre à l'aide des flèches haut et bas.

## Exceptions
- **Saisie de données non numériques :** Seules des données numériques peuvent être saisies.