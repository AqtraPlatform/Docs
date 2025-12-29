# Obtenir un Modèle Vide

![](../../assets/images/app-development/get-empty-model.png)

## Informations générales
L'étape "Obtenir un Modèle Vide" est utilisée dans les scripts de flux de données qui ne nécessitent pas de récupération de modèle de données à l'entrée. Elle est souvent utilisée lorsque le flux de données est appelé pour exécuter des opérations régulières, telles que la génération de rapports, en particulier s'ils sont planifiés (par exemple, par cron).

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre     | Options de valeur | Objectif |
|------------------------|-------------------|----------|
| Nom de l'étape         | -                 | Nom de l'étape |
| Valider les valeurs d'entrée | true, false   | Indique que les valeurs d'entrée doivent être vérifiées pour leur exactitude avant le traitement |

## Cas d'utilisation
- **Opérations Régulières** : Idéal pour les flux de données planifiés pour s'exécuter régulièrement sans besoin de données d'entrée.
- **État Initial du Flux de Données** : Utilisé pour initialiser le flux de données sans données préétablies, permettant aux développeurs de créer et de peupler le modèle de données eux-mêmes à l'aide d'étapes ultérieures.

## Exceptions
- **Pas de Données d'Entrée** : Lors de l'utilisation de cette étape, les données d'entrée ne sont pas fournies dans le flux de données. Cela signifie que le développeur doit initialiser et peupler le modèle de données dans les étapes suivantes.

## Scénario d'application

Ce composant est une interface pour ajouter un nouveau nom via un **champ de saisie** sur le front end, puis mettre à jour le modèle de données et afficher le résultat dans un **datagrid**. Le flux de données dans le composant permet d'ajouter un nouveau nom au modèle et de mettre à jour l'enregistrement dans le **datagrid**.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1G3v4cZiteFdONpIjxPAf78a8gBTrh0w_/view?usp=sharing)