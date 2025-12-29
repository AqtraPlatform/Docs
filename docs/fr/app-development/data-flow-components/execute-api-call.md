# Exécuter l'appel API

![](../../assets/images/app-development/execute-api-call.png)

## Informations générales
L'étape "Exécuter l'appel API" est utilisée pour interagir avec des systèmes externes via l'API. Cette étape peut être configurée pour divers types de requêtes, y compris la réception de données (GET), l'envoi de données (POST/PUT) ou la suppression de données (DELETE) dans un système externe. Selon le contexte d'utilisation, cette étape peut être l'une des premières étapes dans Dataflow pour obtenir des données ou l'une des dernières étapes pour mettre à jour des données dans des systèmes externes.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Champ de stockage du résultat | -       | Un champ pour stocker l'ID d'une entrée créée ou traitée |
| Système            | -                 | Choix d'un système d'intégration |
| Connecteur         | -                 | Sélection d'un connecteur dans le système d'intégration |
| Chemin de requête  | -                 | EndPoint pour la requête |
| Nom de méthode     | Get, Post, Put, Delete | Type de requête à compléter |
| Mappage des paramètres | -             | Configuration dynamique pour le filtrage des requêtes |

## Cas d'utilisation
- **Obtenir des données de sources externes** : Il est utilisé pour télécharger des données à partir de systèmes externes, ce qui peut être particulièrement utile lors de l'intégration avec des services ou des bases de données externes.
- **Envoyer ou mettre à jour des données** : Convient pour envoyer des données à des systèmes externes ou mettre à jour des données existantes, par exemple, lors de la synchronisation des modifications apportées à Dataflow.
- **Supprimer des données** : Il peut être utilisé pour supprimer des données de systèmes externes, ce qui aide à maintenir la pertinence et l'intégrité des données dans les systèmes intégrés.

## Exceptions
- **Besoin de traitement asynchrone** : L'étape est effectuée de manière asynchrone, ce qui nécessite de prendre en compte le temps de réponse des systèmes externes et l'impact potentiel sur la séquence de traitement des données.
- **Exigence de configuration du connecteur** : L'efficacité de l'étape dépend de la configuration correcte des systèmes d'intégration et des connecteurs, ainsi que de l'exactitude de la détermination de l'EndPoint et des paramètres de requête.

## Scénario d'application

Le composant crée une intégration simple pour récupérer des données, telles que la météo, via une API. Dans le flux de données, des étapes sont utilisées pour configurer la requête API, y compris l'exécution d'un script pour créer des variables API, l'appel de l'API et la sauvegarde des résultats. Ensuite, l'intégration est sélectionnée et configurée dans le système, et les résultats sont affichés sur le frontend à l'aide d'un formulaire lié à l'exécution du script. La fonction dans le composant traite les données récupérées pour l'affichage utilisateur.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/119_NZiqzENXCaqdmiZ7qj4ZmeHcje7je/view?usp=sharing).