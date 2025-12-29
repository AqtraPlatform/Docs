# Obtenir des informations sur le fichier

![](../../assets/images/app-development/get-file-info.png)

## Informations générales
L'étape "Obtenir des informations sur le fichier" dans Dataflow est utilisée pour récupérer des informations sur un fichier par son ID. Cette étape donne accès à diverses propriétés du fichier, y compris son nom, son extension (type), sa taille, la date de mise à jour, de création, ainsi que l'auteur du fichier initial et du fichier mis à jour.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Champ Src          | -                 | Champ contenant l'ID du fichier |
| Nom du champ Dst   | -                 | Champ où les informations sur le fichier seront enregistrées |

## Cas d'utilisation
- **Extraction d'informations sur le fichier** : Utilisé pour obtenir des informations détaillées sur un fichier, ce qui peut être utile pour un traitement ou une analyse de données ultérieurs.
- **Préparation des données pour un traitement supplémentaire** : Les informations obtenues sur le fichier peuvent être utilisées dans des étapes ultérieures, telles que "Exécuter un script" ou "Filtrer la source", pour effectuer des opérations spécifiques en fonction des propriétés du fichier.

## Exceptions
- **Dépendance à l'exactitude de la source de données** : L'exactitude des informations obtenues dépend de l'exactitude et de la pertinence des données dans la source.
- **Informations limitées** : L'étape ne fournit que des informations de base sur le fichier et peut ne pas inclure certaines données spécifiques ou supplémentaires.