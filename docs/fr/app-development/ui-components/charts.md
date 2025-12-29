# Graphiques

![](../../assets/images/app-development/charts.png)

## Informations générales
“Vue de graphique” est un composant d'interface utilisateur conçu pour afficher et personnaliser la présentation graphique des données.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre | Options de valeur                          | Objectif                                      |
|----------------------|--------------------|--------------------------------------------|-------------------------------------------------|
| (Paramètres globaux) | Composant          | -                                          | Sélection d'un composant à afficher dans le graphique     |
|                      | Type de graphique   | barre, barre horizontale, camembert, donut, ligne      | Type de graphique                                     |
|                      | Champ d'étiquette   | -                                          | Champ pour les étiquettes sur le graphique                      |
|                      | Source de données   | -                                          | Source de données pour le graphique                    |
|                      | Afficher la légende | vrai, faux                                | Affichage de la légende sur le graphique                 |
|                      | Valeur max de l'axe Y | -                                          | Valeur maximale sur l'axe Y                 |
|                      | Valeur min de l'axe Y | -                                          | Valeur minimale sur l'axe Y                  |
|                      | Valeur max de l'axe X | -                                          | Valeur maximale sur l'axe X                 |
|                      | Valeur min de l'axe X | -                                          | Valeur minimale sur l'axe X                  |
|                      | ID d'automatisation | -                                          | ID pour l'automatisation                |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | vrai, faux | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les espacements extérieurs sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les espacements intérieurs sur tous les côtés de l'élément |
|  | Visible | vrai, faux | Visibilité du composant    |
|                      | Caché | vrai, faux | Masquage d'un composant      |
| Apparence | Rayon de coin | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de bord | - | La propriété vous permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Brosse de bord | - | La propriété définit la couleur de la bordure de l'élément |

**Paramètres de la source de données :**

| Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- |
| Titre | - | Titre de la source de données |
| Valeur | Choix multiple
Catalogue | La propriété vous permet de sélectionner une valeur de source de données parmi les champs Entier et Nombre |
| OK | Bouton | Application de la personnalisation |
| Annuler | Bouton | Annulation de la personnalisation |

## Cas d'utilisation
- **Visualisation des données** : Utilisé pour créer des graphiques et des diagrammes, permettant de présenter les données de manière efficace.
- **Tableaux de bord analytiques** : Convient aux tableaux de bord analytiques qui nécessitent une présentation visuelle des statistiques et des métriques.

## Exceptions
- **Utilisation spécialisée** : Limité à la création de graphiques et n'est pas adapté à d'autres types de visualisations.