# Obtenir des valeurs du connecteur

![](../../assets/images/app-development/get-values-from-connector.png)

## Informations générales
L'étape "Obtenir des valeurs du connecteur" vous permet de récupérer des données via une requête vers des systèmes externes en utilisant les connecteurs configurés. L'étape peut être appelée par un calendrier ou au nom de l'utilisateur.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre    | Options de valeur          | Objectif |
|-----------------------|---------------------------|----------|
| Nom de l'étape        | -                         | Nom de l'étape |
| Système               | Multisélection de Catalogue| Contient des systèmes d'intégration préconfigurés |
| Connecteur            | Multisélection de Catalogue| Contient des connecteurs préconfigurés dans le système d'intégration |
| Chemin de requête     | Multisélection de Catalogue| Contient l'"EndPoint" à accéder |
| Nom de méthode        | Get, Post, Put, Delete    | Type de requête à exécuter |
| Mappage des paramètres | -                         | Une entité dynamique qui vous permet de filtrer une requête via une API sélectionnée |

## Cas d'utilisation
- **Mise à jour programmée des données** : L'étape est utilisée pour mettre à jour automatiquement les données dans le flux de données d'entrée sur une base programmée via cron, garantissant l'obtention d'informations opportunes et à jour.
- **Personnalisation de requête individuelle** : L'étape est configurée pour envoyer des requêtes spécifiques à différents systèmes externes, permettant une intégration flexible et un traitement des données provenant de plusieurs sources.
- **Optimisation du flux de données** : L'étape est utilisée de manière efficace pour extraire des données des systèmes externes, minimisant le besoin de traitement manuel et améliorant les performances du flux de données.

## Exceptions
- **Méthodes de requête** : Bien que diverses méthodes de requête (Get, Post, Put, Delete) soient prises en charge, une personnalisation soigneuse est requise au cas par cas, en tenant compte des caractéristiques spécifiques du système externe et du type de données.
- **Automatisation avec limitations** : La capacité d'appeler automatiquement une étape programmée offre de la commodité, mais nécessite un ajustement des paramètres et une vérification de l'accessibilité des systèmes externes.

## Scénario d'application

Ce composant gère les données de caractère. Nous créons cinq modèles de données pour leurs attributs : character_id, character_name, character_species, character_status et gender. Ensuite, nous sélectionnons une intégration, par exemple, Rick and Morty, et ajoutons les étapes suivantes : Obtenir des valeurs du connecteur, Extraire la collection, Stocker l'entrée sur le bus et Écrire la réponse.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1zWIWzpqccbocpDCfVUNIkGW2grrWJ5Yn/view?usp=sharing)