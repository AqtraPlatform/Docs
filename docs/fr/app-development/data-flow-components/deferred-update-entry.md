# Entrée de mise à jour différée

![](../../assets/images/app-development/deferred-update-entry.png)

## Informations générales
L'étape "Entrée de mise à jour différée" est utilisée pour organiser la mise à jour différée des entrées dans un composant spécifique. Cette étape vous permet d'accumuler des actions pour créer, mettre à jour ou supprimer des entrées, qui sont ensuite exécutées après que l'étape "Appliquer les opérations de mise à jour différées" soit activée. De cette manière, plusieurs opérations de mise à jour peuvent être collectées.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre      | Options de valeur | Objectif |
|-------------------------|-------------------|----------|
| Nom de l'étape          | -                 | Nom de l'étape |
| Étape source            | -                 | Sélection de l'étape précédente |
| Composant               | -                 | Composant à mettre à jour |
| Clé de champ de composant | -               | Champ avec la clé de composant à mettre à jour |
| Marquer l'entrée pour suppression | true, false | Marque de suppression de l'entrée |
| Champ de nom            | -                 | Nom du champ à mettre à jour |
| Mappage des champs      | -                 | Mappage des champs entre le flux de données et le composant |

## Cas d'utilisation
- **Traitement par lots de données** : Utilisé pour collecter plusieurs opérations de mise à jour de données et les exécuter ensuite dans une seule transaction, améliorant ainsi les performances et réduisant la charge sur le système.
- **Gestion complexe des données** : Adapté aux scénarios nécessitant une logique de mise à jour de données complexe, y compris la création, la modification et la suppression d'entrées dans un seul flux de travail.

## Exceptions
- **Besoin de mises à jour ultérieures** : Toutes les opérations de mise à jour accumulées par cette étape doivent être activées via l'étape "Appliquer les opérations de mise à jour différées" afin de les exécuter.

## Scénario d'application

Le composant avec une définition personnalisée configure un flux de données pour la mise à jour des enregistrements. Les utilisateurs commencent par extraire le modèle d'action en utilisant l'étape "Obtenir le modèle d'action". Ensuite, l'étape "Entrée de mise à jour différée" est utilisée pour les mises à jour différées des enregistrements, où les utilisateurs peuvent spécifier le composant, l'ID du composant et les mappages de champs. L'étape "Appliquer la mise à jour différée" permet de configurer le traitement par lots et les paramètres d'exécution parallèle. Après avoir complété ces étapes, le composant est prêt pour mettre à jour, créer ou supprimer des enregistrements, ce qui se produit sur le frontend lors de l'interaction avec les éléments d'interface correspondants.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing)