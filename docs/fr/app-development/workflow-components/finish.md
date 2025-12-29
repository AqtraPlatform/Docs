# Fin

![](../../assets/images/app-development/finish.png)

## Informations générales
L'étape “Fin” dans un flux de travail est conçue pour compléter l'exécution du Workflow actuel. Cette étape est généralement utilisée pour spécifier explicitement le point de complétion d'un flux de travail, en particulier dans les scripts alternatifs définis dans le bloc Conditions.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Objectif |
|--------------------|----------|
| Nom de l'étape     | Nom de l'étape “Fin” |

## Cas d'utilisation
- **Achèvement contrôlé du flux de travail** : Utilisé pour spécifier explicitement le point de complétion d'un flux de travail, ce qui est particulièrement important dans les processus complexes comportant de nombreuses conditions et branches.
- **Chemins d'exécution alternatifs** : Convient aux scripts où un flux de travail doit se terminer sous certaines conditions qui diffèrent du flux principal d'exécution.

## Exceptions
- **Besoin d'une configuration appropriée** : Il est important de s'assurer que l'étape “Fin” est correctement intégrée dans la logique du flux de travail afin qu'elle n'interrompe pas le processus prématurément ou ne saute pas des étapes importantes.