# Condition If

![](../../assets/images/app-development/if-condition.png)

## Informations générales

L'étape "Condition If" dans le flux de travail est utilisée pour vérifier la valeur d'un champ par rapport à la condition spécifiée. Cette étape vous permet de mettre en œuvre un branchement conditionnel dans un processus où l'exécution de certaines actions ou le passage à un script alternatif dépend du résultat d'une vérification de condition. Un script alternatif doit contenir l'étape "Fin".

## Paramètres

**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur           | Objectif                                 |
| ------------------ | --------------------------- | ---------------------------------------- |
| Nom de l'étape     | -                           | Nom de l'étape "Condition If"           |
| Champ de condition  | Multisélection de Catalogue | Champ de validation de condition         |
| Opérateur          | Égal, Pas égal, Supérieur, Inférieur | Type d'opérateur pour vérifier la condition |
| Comparer avec null | vrai, faux                 | Vérification de la comparaison avec null |
| Valeur             | -                           | Valeur à comparer avec le champ         |

## Cas

- **Exécution conditionnelle des actions** : Utilisé pour activer différentes parties du flux de travail en fonction des valeurs de certains champs, par exemple, pour démarrer différents processus en fonction de l'état de la demande.
- **Branchement logique dans les processus** : Convient pour créer des chaînes logiques complexes où différentes étapes d'exécution dépendent de la satisfaction de conditions spécifiques.

## Exceptions

- **Précision de la définition de la condition** : Il est important de définir avec précision les conditions et de configurer correctement les champs pour les valider afin d'éviter un branchement incorrect ou des erreurs dans la logique du flux de travail.
- **Gestion des différents scripts** : Vous devez planifier clairement comment les différents scripts seront gérés en fonction du résultat de la vérification de la condition, en particulier dans les flux de travail à plusieurs étapes ou complexes.