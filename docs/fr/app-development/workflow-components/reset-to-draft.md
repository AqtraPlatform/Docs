# Réinitialiser au brouillon

![](../../assets/images/app-development/reset-to-draft.png)

## Informations générales
L'étape « Réinitialiser au brouillon » dans le flux de travail est utilisée pour ramener le script à l'état « non en cours d'exécution ». Cette étape est utile dans les situations où vous devez pouvoir modifier ou examiner une demande ou un processus pendant qu'il est en cours d'approbation ou d'exécution.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Objectif |
|--------------------|----------|
| Nom de l'étape     | Nom de l'étape « Réinitialiser au brouillon » |

## Cas d'utilisation
- **Modification pendant le processus d'approbation** : Utilisé pour offrir la possibilité d'apporter des modifications à une demande ou un processus qui est déjà en phase d'approbation ou de mise en œuvre, ce qui peut être nécessaire pour corriger ou clarifier les informations.
- **Gestion de processus flexible** : Convient aux scripts où vous avez besoin de la capacité de revenir à un processus à son état initial pour éviter des erreurs ou une exécution incorrecte.

## Exceptions
- **Surveiller le processus de retour en arrière** : Vous devez vous assurer que le processus de retour en arrière ne compromet pas l'intégrité des données et la logique du flux de travail.