# Obtenir le modèle de workflow

![](../../assets/images/app-development/get-workflow-model.png)

## Informations générales
L'étape "Obtenir le modèle de workflow" est utilisée exclusivement dans les flux de données qui sont appelés depuis un workflow. Elle vous permet d'obtenir le modèle et les données du workflow appelant dans le flux de données actuel.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre     | Options de valeur | Objectif |
|------------------------|-------------------|----------|
| Nom de l'étape         | -                 | Nom de l'étape |
| Valider les valeurs d'entrée | true, false       | Indique que les valeurs d'entrée doivent être vérifiées pour leur exactitude avant le traitement |

## Cas d'utilisation
- **Intégration des flux de données et des workflows** : Permet d'intégrer le flux de données avec le workflow en fournissant un accès au modèle et aux données du workflow appelant.

## Exceptions
- **Utilisation limitée** : L'étape n'est pas destinée à être utilisée dans un flux de données d'entrée.

## Scénario d'application

Le composant vous permet de créer un flux de données pour mettre à jour un enregistrement dans le composant de données source. Il comprend des étapes telles que Obtenir le modèle de workflow pour obtenir le modèle de workflow, Mettre à jour l'entrée pour mettre à jour l'enregistrement avec les paramètres appropriés, et Écrire la réponse pour afficher le résultat. Ce composant peut être utilisé pour mettre à jour des données dans le composant source en utilisant des workflows et des éléments d'interface utilisateur.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1F2ZFQlyMf6ZaxABcoOWib4T8AD8w-75Q/view?usp=sharing)