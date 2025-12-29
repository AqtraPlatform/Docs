# Entrée de requête proxy

![](../../assets/images/app-development/proxy-query-entry.png)

## Informations générales
L'étape « Entrée de requête proxy » est utilisée pour générer un modèle de requête proxy en utilisant un filtre (**Query**) pour récupérer une ou plusieurs entrées. Cette étape fonctionne en conjonction avec le paramètre « Mode proxy » dans la section « Paramètres ». Pour que le modèle de données du composant fonctionne correctement, les propriétés avec le drapeau **Query** doivent être définies.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre     | Options de valeur | Objectif |
|------------------------|-------------------|----------|
| Nom de l'étape         | -                 | Nom de l'étape |
| Filtre de requête      | -                 | Filtre pour définir une entrée spécifique pour une requête |
| Paramètres de mode proxy| -                 | Référence aux paramètres de mode proxy définis dans « Paramètres » |

## Cas d'utilisation
- **Requêtes filtrées dans le proxy** : Utilisé dans le flux de données d'entrée pour les composants marqués comme proxy afin d'exécuter des requêtes avec filtrage des données.
- **Récupération de données spécifiques** : Récupère une entrée spécifique basée sur certains critères de filtre.

## Exceptions
- **Dépendance de configuration du composant** : Nécessite certaines propriétés avec le drapeau **Query** dans le modèle de données du composant.
- **Utilisation limitée** : L'étape est conçue pour récupérer des données basées sur des filtres et n'est pas adaptée aux requêtes générales sans spécification.