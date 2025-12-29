# Hyperlien

![](../../assets/images/app-development/hyperlink.png)

## Informations générales
Le hyperlien dans la plateforme est un composant front-end pour créer des hyperliens. Il permet aux utilisateurs de naviguer facilement entre différentes parties de l'application ou vers des ressources externes, garantissant une navigation efficace et intuitive.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Étiquette | - | Contient le nom du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient un champ “Uri” associé du modèle |
|  | Valeur | - | Permet de spécifier une valeur statique pour le champ, utilisée pour spécifier un lien |
| Texte | Taille de police | - | La propriété détermine la taille de la police |
|  | Couleur | - | Un module en CSS qui fonctionne avec les couleurs, les types de couleurs et la transparence. |
|  | Gras | true, false | Propriété qui permet de mettre le texte en gras |
|  | Italique | true, false | Propriété qui permet d'italiser le texte |
|  | Alignement du texte | Gauche, Droite, Centre, Justifier | La propriété est utilisée pour définir l'alignement horizontal du texte |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | true, false | La propriété détermine combien un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les marges extérieures sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les rembourrages intérieurs sur tous les côtés de l'élément |
| Apparence | Rayon de coin | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de bordure | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Bordure de brosse | - | La propriété définit la couleur de la bordure de l'élément |

## Cas 
- **Navigation sur le site** : Utilisé pour créer des liens vers d'autres pages de l'application ou des sites web externes, améliorant l'interface utilisateur.
- **Amélioration de l'expérience utilisateur** : Fournit un accès facile à des ressources et informations importantes, améliorant l'expérience utilisateur avec l'application.

## Exceptions
- **Limitations de fonctionnalité** : Un hyperlien peut avoir une interopérabilité limitée en offrant uniquement une fonctionnalité de clic de base.
- **Dépendance au contexte** : Il est important de considérer le contexte dans lequel les liens sont utilisés pour garantir une navigation efficace et éviter les malentendus.