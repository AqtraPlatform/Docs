# Grille de données

![](../../assets/images/app-development/data-grid.png)

## Informations générales
La Grille de données est un composant UI puissant conçu pour afficher et interagir avec de grandes quantités de données sous forme tabulaire. Ce composant est idéal pour présenter des données sous forme de lignes et de colonnes, ainsi que pour fournir des fonctionnalités de tri et de filtrage.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre      | Options de valeur        | Objectif                          |
|----------------------|-------------------------|--------------------------|-------------------------------------|
| (Paramètres globaux) | Nom                     | -                        | Nom du composant UI dans le système   |
|                      | Colonnes                | -                        | Définir les colonnes et leurs propriétés   |
|                      | Composant               | Multisélection de Catalogue | Contient une liste de tous les Composants |
|                      | Filtres statiques       | Bouton                  | Utilisé pour spécifier des filtres statiques |
|                      | Filtres dynamiques      | Bouton                  | La propriété est utilisée pour spécifier des filtres dynamiques |
|                      | Taille de page          | -                        | Taille de la page                     |
|                      | Rechargement manuel     | -                        | Rechargement manuel des données          |
|                      | Mode de sélection       | aucun, unique, multiple, case à cocher | Mode de sélection d'éléments          |
|                      | ID d'automatisation     | -                        | ID pour l'automatisation     |
| Événements           | Lors du chargement de la source de données | - | Événement de chargement de la source de données |
|                      | Lors des lignes sélectionnées | -             | Événement de sélection de lignes |
|                      | Lors du chargement      | -      | Événement de chargement du composant |
|                      | Lors du changement de table | -        | Événement de changement de table |
|                      | Lors du changement d'en-tête | -      | Événement de changement d'en-tête |
|                      | Lors du changement de ligne | -         | Événement de changement de ligne |
|                      | Lors du changement de cellule | -         | Événement de changement de cellule |

**Propriétés CSS :**

| Groupe de paramètres | Champ de paramètre      | Options de valeur        | Objectif                          |
|----------------------|-------------------------|--------------------------|-------------------------------------|
| Mise en page         | Largeur                 | -                        | Largeur du composant                   |
|                      | Hauteur                 | -                        | Hauteur du composant                   |
|                      | Marge                   | -                        | Rembourrage extérieur                      |
|                      | Rembourrage             | -                        | Rembourrage intérieur                   |
|                      | Visible                 | -                        | Visibilité du composant                |
|                      | Caché                  | -                        | Cacher un composant                  |
| Apparence            | Rayon de coin           | -                        | Rayon des coins                   |
|                      | Épaisseur de bordure    | -                        | Épaisseur de la bordure                       |
| Brosse               | Arrière-plan            | -                        | Couleur de fond                           |
|                      | Brosse de bordure       | -                        | Couleur de la bordure                          |

**Modèle de configuration de DataGrid**

Les paramètres suivants sont utilisés pour modifier les colonnes du composant UI DataGrid : 

| Champ de paramètre   | Options de valeur                           | Objectif                                              |
|----------------------|--------------------------------------------|------------------------------------------------------|
| Valeur de traduction  | -                                          | En-tête de colonne                                   |
| Afficher l'en-tête    | vrai, faux                                | Cette propriété vous permet de personnaliser l'affichage de l'en-tête de la colonne |
| Triable              | vrai, faux                                | La propriété vous permet de configurer la capacité de trier le tableau par la colonne sélectionnée |
| Filtrable            | vrai, faux                                | Cette propriété vous permet de configurer la capacité de filtrer le tableau par la colonne sélectionnée |
| Visible              | vrai, faux                                | La propriété détermine la visibilité de la colonne                   |
| Texte brut           | vrai, faux                                | Propriété pour afficher une colonne en texte brut    |
| Largeur              | -                                          | Largeur de la colonne dans le tableau                                |
| Format d'affichage    | -                                          | Format d'affichage des données de la colonne                       |
| Icône                | Disponible uniquement pour Éditer l'enregistrement, Ouvrir l'application | Une propriété qui contient une sélection d'icônes disponibles         |
| Type de commande      | Ouvrir l'application, Éditer l'enregistrement | La propriété vous permet de sélectionner l'action qui sera effectuée en cliquant sur la colonne |
| Ajouter un champ      | Bouton                                     | La propriété vous permet d'ajouter des champs pour la sortie dans la colonne   |

## Cas d'utilisation
- **Affichage des données** : Idéal pour afficher des données sous une forme tabulaire facile à comprendre.
- **Panneaux administratifs** : Largement utilisé dans les interfaces de gestion pour visualiser et modifier des données.
- **Applications d'analyse** : Permet d'analyser et de trier de grandes quantités d'informations.

## Exceptions
- **Visualisation limitée** : La Grille de données n'est pas adaptée aux visualisations de données complexes telles que les graphiques ou les tableaux.
- **Traitement des données** : Le composant est conçu pour afficher des données, et non pour traiter ou calculer des données.