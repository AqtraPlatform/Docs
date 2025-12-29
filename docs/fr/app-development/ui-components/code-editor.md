# Éditeur de code

![](../../assets/images/app-development/code-editor.png)

## Informations générales
L'Éditeur de code est un composant UI spécialisé conçu pour saisir et afficher du code de programme. Il prend en charge divers langages de programmation tels que JavaScript, Python, etc. et offre des fonctionnalités pour un éditeur de code facile, mais l'élément ne prend pas en charge un compilateur.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre | Options de valeur          | Objectif |
|----------------------|--------------------|----------------------------|----------|
| (Paramètres globaux) | Nom                | -                          | Nom du composant UI dans le système |
| Commun               | Désactivé          | true, false                | Désactivation d'un élément |
|                      | Requis             | true, false                | Champ requis à remplir |
|                      | Thème              | -                          | Style visuel de l'éditeur |
|                      | Mode               | -                          | Langage de programmation |
|                      | Étiquette          | -                          | Description du champ |
|                      | Liaison            | Multisélection de catalogue | Liaison de données |
| Événements           | Sur changement de valeur | -                          | Événement de changement de valeur |
|                      | Sur touche enfoncée | -                          | Événement de pression de touche |
|                      | Sur touche relâchée | -                          | Événement de relâchement de touche |
|                      | Sur focus          | -                          | Événement lors du focus sur un élément |
| Index de tabulation  | -                  | Entier                    | Ordre de changement de champ |

**Propriétés CSS :**

| Groupe de paramètres | Champ de paramètre | Options de valeur          | Objectif |
|----------------------|--------------------|----------------------------|----------|
| Mise en page         | Largeur            | -                          | Largeur du composant |
|                      | Hauteur            | -                          | Hauteur du composant |
|                      | Croître            | true, false                | Étirement du composant |
|                      | Marge              | -                          | Rembourrage extérieur |
|                      | Rembourrage        | -                          | Rembourrage intérieur |
| Apparence            | Rayon de coin      | -                          | Rayon des coins |
|                      | Épaisseur de bord  | -                          | Épaisseur de la bordure |
| Brosse               | Arrière-plan       | -                          | Couleur de fond |
|                      | Brosse de bordure  | -                          | Couleur de la bordure |

## Cas d'utilisation
- **Édition de code** : Utilisé pour saisir et modifier du code de programme dans divers langages de programmation.
- **Formation et démonstration** : Utilisé à des fins éducatives et de démonstration pour montrer des exemples de code.

## Exceptions
- **Limitations de fonctionnalité** : Selon l'implémentation, peut ne pas prendre en charge toutes les fonctionnalités des environnements de développement avancés.