# Switch case

![](../../assets/images/app-development/switch-case.png)

## Informations générales
L'étape « Switch Case » dans un flux de travail est utilisée comme un opérateur de commutation inconditionnel qui vous permet de choisir entre différentes options de script. Cette étape est idéale pour contrôler la logique du processus en fonction de certaines conditions, généralement spécifiées par des champs Boolean ou Enum. Lorsqu'elle est utilisée, le script principal est toujours désactivé et le processus passe à l'une des branches alternatives.
![](../../assets/images/app-development/switch-case-example.png)

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre  | Objectif |
|---------------------|----------|
| Nom de l'étape      | Nom de l'étape « Switch Case » |
| Champ source de commutation | Champ basé sur la valeur selon laquelle le script est sélectionné |

## Cas
- **Ramification de la logique de processus** : Utilisé pour créer des chemins conditionnels dans un flux de travail où la prochaine direction est déterminée en fonction d'une certaine condition ou valeur.
- **Gestion de différents scripts d'exécution** : Convient aux scripts où un processus nécessite une exécution différente en fonction de conditions prédéfinies ou de la sélection de l'utilisateur.

## Exceptions
- **Précision des conditions de transition** : Il est nécessaire de définir avec précision les conditions de commutation pour chaque cas afin de garantir que le bon chemin d'exécution est sélectionné.
- **Complexité de la gestion de plusieurs chemins** : Les flux de travail complexes avec de nombreux chemins possibles nécessitent une compréhension claire et une gestion de chacun d'eux pour éviter des erreurs dans la logique du processus.