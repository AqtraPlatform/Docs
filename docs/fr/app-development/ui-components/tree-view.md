# Vue Arborescente

![](../../assets/images/app-development/tree-view.png)

## Informations générales
La “Vue Arborescente” est un composant d'interface utilisateur pour afficher et personnaliser des données sous une forme hiérarchique, ce qui facilite la navigation et la présentation de structures de données complexes.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant d'interface utilisateur dans le système |
| Commun | Objet de données | Multisélection de Catalogue | Contient une liste de tous les composants |
|  | Regrouper par | Multisélection de Catalogue | Propriété pour regrouper les données par champ sélectionné |
|  | Ajouter champ de tri | Bouton | La propriété est utilisée pour ajouter des champs de tri |
|  | Champs de tri | Multisélection de Catalogue | Permet de sélectionner le champ par lequel trier. |
| Événements | Lors du chargement de la source de données | - | Permet d'exécuter le script spécifié lorsque la source de données est complète |

## Cas d'utilisation
- **Visualisation des hiérarchies** : Idéal pour présenter des données hiérarchiques, telles que la structure organisationnelle ou la classification des produits.

## Exceptions
- **Complexité de personnalisation** : Nécessite une configuration minutieuse pour afficher correctement des structures de données complexes.