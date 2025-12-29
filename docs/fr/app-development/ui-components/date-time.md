# Date / Heure

![](../../assets/images/app-development/date-time.png)

## Informations générales
Date/Heure est un composant UI pour entrer et afficher la date et l'heure. Il est conçu pour fournir une interface conviviale pour sélectionner la date/l'heure, ainsi que pour afficher ces données dans un format spécifique.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre | Options de valeur       | Objectif                 |
|----------------------|--------------------|--------------------------|--------------------------|
| (Paramètres globaux) | Nom                | -                        | Nom du composant UI dans le système |
| Date Heure           | Format             | Date, Heure, Date & Heure | Format d'affichage       |
|                      | Valeur par défaut  | -                        | Valeur par défaut        |
|                      | Date min           | -                        | Date minimale            |
|                      | Date max           | -                        | Date maximale            |
| Commun               | Liaison            | -                        | Liaison aux données      |
|                      | Requis             | true, false              | Requis à remplir         |

**Propriétés CSS :**

| Groupe de paramètres | Champ de paramètre | Options de valeur       | Objectif                 |
|----------------------|--------------------|--------------------------|--------------------------|
| Mise en page         | Largeur            | -                        | Largeur du composant     |
|                      | Hauteur            | -                        | Hauteur du composant     |
|                      | Marge              | -                        | Rembourrage extérieur     |
|                      | Rembourrage        | -                        | Rembourrage intérieur     |
| Apparence            | Rayon de coin      | -                        | Rayon des coins          |
|                      | Épaisseur de bord  | -                        | Épaisseur de bord        |
| Brosse               | Arrière-plan       | -                        | Couleur de fond          |
|                      | Brosse de bord     | -                        | Couleur de bord          |

## Cas d'utilisation
- **Sélection de date d'événement** : Utilisé pour sélectionner une date dans le calendrier ou pour définir l'heure de l'événement.
- **Filtrer par date** : Peut être utilisé dans des filtres pour filtrer des données par date/heure.
- **Afficher des intervalles de temps** : Convient pour des tâches impliquant l'affichage d'intervalles de temps, comme dans les planificateurs de tâches.

## Exceptions
- **Formatage** : Date/Heure n'est pas destiné à une saisie de texte libre, mais est utilisé strictement pour travailler avec des dates et des heures.