# Source de filtre

![](../../assets/images/app-development/filter-source.png)

## Informations générales
L'étape "Source de filtre" est utilisée pour filtrer le flux de données dans le flux de données. Elle vous permet de ramifier les flux de données en fonction de la valeur du champ sélectionné et de l'opérateur de test spécifié, tel que égal, différent, supérieur et inférieur.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre  | Options de valeur   | Objectif |
|---------------------|---------------------|----------|
| Nom de l'étape      | -                   | Nom de l'étape |
| Étape source        | -                   | Sélection de l'étape précédente |
| Champ Src           | -                   | Champ à filtrer |
| Opérateur           | égal, différent, supérieur, inférieur | Opérateur pour comparer les valeurs des champs |
| Comparer avec null  | vrai, faux          | Indique s'il faut comparer avec null |
| Valeur de filtre    | -                   | Valeur à filtrer |

## Cas d'utilisation
- **Ramification du flux de données** : Utilisé pour diviser un flux de données en fonction de conditions spécifiques définies dans le filtre.
- **Segmentation des données** : Convient aux situations où vous devez traiter différents segments de données différemment en fonction de critères spécifiés.

## Exceptions
- **Précision des paramètres de filtre** : Un filtre mal configuré peut entraîner la perte de données importantes ou l'inclusion de données inutiles dans le traitement.
- **Dépendance au champ sélectionné** : L'efficacité du filtrage dépend du choix correct du champ et de l'opérateur de comparaison approprié.

## Scénario d'application

Ce composant est une interface avec trois boutons : `ExecuteFilterSource`, `ExecuteFilterSourceNotEqual`, et `ExecuteFilterSourceGreat`, chacun déclenchant un flux de données en fonction de l'entrée dans le champ `First`. Différents scénarios de test incluent la vérification des conditions d'égalité, d'inégalité et de supérieur/inferieur à la valeur spécifiée.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1OO5SymRdhmv3oED2EPG4twG5mypsqqs9/view?usp=sharing).