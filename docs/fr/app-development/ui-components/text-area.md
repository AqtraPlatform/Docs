# Zone de texte

![](../../assets/images/app-development/text-area.png)

## Informations générales
La zone de texte est un composant d'interface utilisateur de base conçu pour saisir et afficher du texte sur plusieurs lignes. Elle est idéale pour taper de grandes quantités de texte, telles que des commentaires ou des descriptions, et offre suffisamment d'espace pour une saisie facile.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre | Options de valeur         | Objectif |
|----------------------|--------------------|---------------------------|----------|
| (Paramètres globaux) | Nom                | -                         | Nom du composant UI dans le système |
| Commun               | Désactivé          | true, false               | Désactivation d'un élément |
|                      | Taille automatique  | true, false               | Contrôle automatique des dimensions |
|                      | Requis             | true, false               | Champ obligatoire à remplir |
|                      | Étiquette          | -                         | Description du champ de saisie |
|                      | Liaison           | Multisélection de Catalogue | Liaison de données |
| Événements           | Sur changement de valeur | -                     | Événement de changement de valeur |
| Index de tabulation  | -                  | Entier                   | Ordre de changement de champ |

**Propriétés CSS :**

| Groupe de paramètres | Champ de paramètre | Options de valeur         | Objectif |
|----------------------|--------------------|---------------------------|----------|
| Mise en page         | Largeur            | -                         | Largeur du composant |
|                      | Hauteur            | -                         | Hauteur du composant |
|                      | Croissance         | true, false               | Étirement du composant |
|                      | Marge              | -                         | Rembourrage extérieur |
|                      | Rembourrage        | -                         | Rembourrage intérieur |
| Apparence            | Rayon des coins    | -                         | Rayon des coins |
|                      | Épaisseur de bord  | -                         | Épaisseur de la bordure |
| Brosse               | Arrière-plan       | -                         | Couleur de fond |
|                      | Brosse de bordure  | -                         | Couleur de la bordure |

## Cas d'utilisation
- **Saisie multi-lignes** : Idéal pour les formulaires nécessitant de grandes quantités de texte.
- **Commentaires et descriptions** : Utilisé pour écrire des commentaires, des descriptions ou tout autre script où une saisie multi-lignes est requise.

## Exceptions
- **Formatage limité** : Comme la plupart des champs de saisie de texte, la zone de texte limite l'utilisation de formatages complexes, tels que les hyperliens ou les images intégrées.