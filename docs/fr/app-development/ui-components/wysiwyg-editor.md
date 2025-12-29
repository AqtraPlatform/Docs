# Éditeur WYSIWYG

![](../../assets/images/app-development/wysiwyg-editor.png)

## Informations générales
L'éditeur WYSIWYG est un composant d'interface utilisateur conçu pour saisir et modifier du texte enrichi au format WYSIWYG. Il offre des fonctionnalités similaires à des éditeurs comme Wordpad, permettant aux utilisateurs de formater facilement le texte et d'insérer divers éléments multimédias.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre | Options de valeur          | Objectif |
|----------------------|--------------------|----------------------------|----------|
| (Paramètres globaux) | Nom                | -                          | Nom du composant UI dans le système |
| Commun               | Désactivé          | true, false                | Désactivation d'un élément |
|                      | Requis             | true, false                | Champ requis à remplir |
|                      | Plugins            | -                          | Activation des plugins |
|                      | Étiquette          | -                          | Description du champ |
|                      | Liaison           | Multisélection de Catalogue | Liaison de données |
| Événements           | Sur changement de valeur | -                      | Événement de changement de valeur |
|                      | Sur touche enfoncée | -                         | Événement de pression de touche |
|                      | Sur touche relâchée | -                         | Événement de relâchement de touche |
|                      | Sur focus          | -                          | Événement lors de la mise au point sur un élément |
| Index de tabulation  | -                  | Entier                    | Ordre de changement de champ |

**Propriétés CSS :**

| Groupe de paramètres | Champ de paramètre | Options de valeur          | Objectif |
|----------------------|--------------------|----------------------------|----------|
| Mise en page         | Largeur            | -                          | Largeur du composant |
|                      | Hauteur            | -                          | Hauteur du composant |
|                      | Croissance         | true, false                | Étirement du composant |
|                      | Marge              | -                          | Rembourrage extérieur |
|                      | Rembourrage        | -                          | Rembourrage intérieur |
| Apparence            | Rayon de coin      | -                          | Rayon des coins |
|                      | Épaisseur de bord  | -                          | Épaisseur de la bordure |
| Brosse               | Arrière-plan       | -                          | Couleur de fond |
|                      | Brosse de bordure  | -                          | Couleur de la bordure |

## Cas d'utilisation
- **Mise en forme du texte** : Utilisé pour créer des documents et du contenu richement formatés.
- **Édition de contenu** : Utilisé dans les systèmes de gestion de contenu pour faciliter l'édition d'articles, de blogs et d'autres contenus textuels.

## Exceptions
- **Complexité de l'interface** : Peut être difficile à utiliser pour les utilisateurs sans expérience avec des éditeurs similaires.
- **Limitations techniques** : Selon l'implémentation, peut ne pas prendre en charge toutes les fonctionnalités des éditeurs de texte avancés.