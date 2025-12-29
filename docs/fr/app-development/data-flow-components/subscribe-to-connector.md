# S'abonner au connecteur

![](../../assets/images/app-development/subscribe-to-connector.png)

## Informations générales

L'étape « S'abonner au connecteur » est destinée à s'abonner pour recevoir des messages de divers systèmes de messagerie, tels que RabbitMQ ou Kafka.

## Paramètres

**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur          | Objectif                                                      |
| ------------------ | -------------------------- | ------------------------------------------------------------ |
| Nom de l'étape     | -                          | Nom de l'étape                                             |
| Système            | Sélection multiple de Catalogue | Contient des systèmes d'intégration préconfigurés                   |
| Connecteur         | Sélection multiple de Catalogue | Contient des connecteurs préconfigurés dans le système d'intégration |
| Chemin de requête  | Sélection multiple de Catalogue | Contient le « Point d'accès » à accéder                       |
| Nom de méthode     | Get, Post, Put, Delete     | Type de requête à exécuter                                   |

## Cas d'utilisation

- **Réponse aux événements** : Réception automatique de notifications concernant des événements ou des changements de données provenant de sources externes.
- **Intégration avec des systèmes de messagerie** : Interaction avec diverses plateformes de messagerie pour garantir un flux de données continu.

## Exceptions

- **Fonctionnalité limitée** : L'étape est limitée à l'abonnement aux messages et ne prend pas en charge d'autres types d'interactions avec des systèmes externes.
- **Dépendance aux systèmes externes** : Nécessite une configuration fiable et un support des systèmes de messagerie utilisés.

## Scénario d'application

Le composant est configuré pour **s'abonner à une file d'attente RabbitMQ** et enregistrer les messages reçus dans une **base de données**. Des étapes telles que "**S'abonner au connecteur**", "**Exécuter le script**" pour le traitement des données, et "**Mettre à jour l'entrée**" pour enregistrer les messages sont utilisées dans ce processus.

- La configuration du composant sera disponible ultérieurement.