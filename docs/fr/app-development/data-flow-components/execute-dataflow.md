# Exécuter le flux de données

![](../../assets/images/app-development/execute-dataflow.png)

## Informations générales
L'étape Exécuter le flux de données est utilisée pour appeler le flux de données depuis n'importe quel composant publié. Cette étape vous permet d'exécuter un flux de données supplémentaire dans le contexte du processus de traitement des données actuel.

Lorsqu'elle est utilisée avec un champ de tableau obtenu à partir d'une source externe ou d'un champ de tableau (propriété), l'étape analyse ce tableau et commence le traitement parallèle de chaque enregistrement ou objet contenu dans le tableau.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre  | Options de valeur | Objectif |
|---------------------|-------------------|----------|
| Nom de l'étape      | -                 | Nom de l'étape |
| Étape source        | -                 | Sélection de l'étape précédente |
| Composant           | -                 | Le composant à partir duquel le flux de données est appelé |
| Flux de données     | -                 | Nom du flux de données à exécuter |
| Champ de stockage des résultats | -       | Champ pour enregistrer le résultat de l'exécution du flux de données |

## Cas d'utilisation
- **Mise à jour des données provenant d'autres flux de données** : L'étape « Exécuter le flux de données » est idéale pour les situations où vous souhaitez mettre à jour des champs dans le modèle actuel avec des données collectées ou traitées dans d'autres flux de données. Cela permet d'intégrer et de synchroniser efficacement les données entre différents processus et composants.
- **Appel de flux de données externe** : Utilisé pour intégrer et lancer des flux de données supplémentaires dans le cadre du processus de traitement des données actuel.

## Exceptions
- **Dépendance à l'exactitude des autres flux de données** : L'efficacité de l'étape « Exécuter le flux de données » dépend directement de l'exactitude et de la fiabilité des données obtenues à partir d'autres flux de données. Tous les flux de données associés doivent être soigneusement configurés et testés pour garantir que les données mises à jour sont correctes et à jour.

## Scénario d'application

Ce composant crée un flux de données pour effectuer des opérations sur les données du composant actuel. Il comprend des étapes de modèle d'action Get pour récupérer le modèle de flux de données et des étapes d'exécution de flux de données pour exécuter le flux de données avec des paramètres appropriés tels que la sélection du composant actuel, le choix du flux de données à exécuter, la configuration des champs de résultats et l'affichage des définitions du composant de données. Ce composant permet des opérations sur les données du composant directement depuis l'interface de l'application.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1ekmRNTRgO30koKm04pyhEZsXG9W5T-O-/view?usp=sharing).