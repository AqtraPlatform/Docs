# Mettre à jour le champ du modèle

![](../../assets/images/app-development/update-model-field.png)

## Informations générales
L'étape "Mettre à jour le champ du modèle" dans le flux de travail est utilisée pour mettre à jour un champ spécifique dans le modèle. Cette étape vous permet de modifier les valeurs des champs individuels dans le modèle de données, ce qui est particulièrement utile pour la gestion dynamique des données pendant l'exécution du flux de travail.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Objectif |
|--------------------|----------|
| Nom de l'étape     | Nom de l'étape "Mettre à jour le champ du modèle" |
| Champ du modèle    | Champ du modèle que vous souhaitez mettre à jour |
| Valeur             | Valeur à laquelle le champ sera mis à jour |
| Champ source       | Champ source dont la valeur sera utilisée pour la mise à jour |

## Cas d'utilisation
- **Mise à jour dynamique des données** : Utilisé pour changer les valeurs dans le modèle en fonction des données générées pendant le flux de travail, comme la mise à jour du statut d'une tâche ou le changement des options de configuration.

## Exceptions
- **Précision et pertinence des données** : Assurez-vous que les données mises à jour sont précises et à jour pour éviter des conséquences indésirables.
- **Compréhension de l'impact des changements** : Il est important de comprendre l'impact de la mise à jour d'un champ sur l'ensemble du modèle et de la logique du flux de travail, en particulier dans les systèmes complexes avec des dépendances interconnectées.