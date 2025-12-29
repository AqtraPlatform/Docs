# Proxy get entry

![](../../assets/images/app-development/proxy-get-entry.png)

## Informations générales
L'étape « Proxy Get Entry » est utilisée pour générer un modèle de requête proxy afin d'obtenir une seule entrée. Cette étape est étroitement liée au paramètre « Proxy mode », qui se trouve dans la section « Settings ».

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre     | Options de valeur | Objectif |
|------------------------|-------------------|----------|
| Nom de l'étape         | -                 | Nom de l'étape |
| Valider les valeurs d'entrée | true, false       | Indique que les valeurs d'entrée doivent être vérifiées pour leur exactitude avant le traitement |

## Cas d'utilisation
- **Récupération d'une seule entrée** : Utilisé pour générer et envoyer des requêtes pour une entrée spécifique via un serveur proxy.
- **Intégration avec des systèmes externes** : Fournit une communication avec des systèmes et services externes pour obtenir des données en utilisant le proxy de requête.

## Exceptions
- **Dépendance aux paramètres proxy** : Le bon fonctionnement de l'étape dépend du paramètre « Proxy mode » correctement configuré dans la section « Settings ».
- **Fonctionnalité limitée** : L'étape est spécialisée dans la récupération d'enregistrements uniques et n'est pas conçue pour gérer plusieurs requêtes ou données.