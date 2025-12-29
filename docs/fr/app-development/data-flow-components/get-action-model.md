# Obtenir le modèle d'action

![](../../assets/images/app-development/get-action-model.png)

## Informations générales
L'étape "Obtenir le modèle d'action" est conçue pour extraire un modèle d'action d'une source ou d'un système spécifique. Cette étape peut être utilisée pour obtenir des données sur des actions ou des processus spécifiques qui sont nécessaires pour un traitement ou une analyse ultérieure dans le flux de données.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre    | Options de valeur          | Objectif |
|-----------------------|---------------------------|----------|
| Nom de l'étape        | -                         | Nom de l'étape |
| Valider les valeurs d'entrée | true, false           | Spécifie si les valeurs d'entrée doivent être vérifiées pour leur exactitude avant le traitement |

## Cas d'utilisation
- **Intégration UI** : Souvent utilisée comme étape initiale dans le flux de données, en particulier lorsque le flux de données est activé depuis l'UI, par exemple en appuyant sur un bouton. Permet d'obtenir l'état actuel des données du composant au moment de l'activation.
- **Transfert de données automatique depuis l'UI** : Lorsque le transfert de données est activé depuis des éléments de l'UI tels que des boutons, la plateforme transmet automatiquement les données actuelles du composant, y compris les modifications apportées par l'utilisateur.

## Exceptions
- **Limitations de récupération des données** : L'étape ne récupère que les données des champs (propriétés) du composant. Pour obtenir les variables définies dans le script du composant, vous devez utiliser d'autres étapes, telles que "Obtenir le modèle brut".

## Scénario d'application

Le composant est un système pour ajouter et afficher des données en utilisant divers types de champs. Il inclut la capacité d'ajouter des champs de différents types dans la **définition** et fournit une interface frontale pour saisir des valeurs, ainsi que pour afficher des données dans un **datagrid** avec la possibilité de rafraîchir la page. Ce composant utilise les **étapes de flux de données** suivantes : **Obtenir le modèle d'action**, **Mettre à jour l'entrée**, **Écrire la réponse**.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/15M_FvmlFmkJXunTeeT6jtFolPvE5jCfk/view?usp=sharing)