# Préparer les clés externes

![](../../assets/images/app-development/prepare-external-keys.png)

## Informations générales
L'étape « Préparer les clés externes » est utilisée pour convertir les identifiants internes du composant en clés de système externe. Cette étape est largement utilisée pour préparer et envoyer des données à des systèmes externes, y compris l'intégration avec LDAP. Elle facilite le processus de transfert des informations utilisateur vers un système externe, y compris le contexte pertinent.

Au cours de cette étape, les ID internes du composant sont remplacés par les clés primaires spécifiées pour ce composant, ce qui garantit le bon mappage des données entre les systèmes internes et externes.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Source de données pour la conversion de clés |

## Cas d'utilisation
- **Intégration avec des systèmes externes** : Utilisé pour adapter les données internes pour leur intégration appropriée et leur envoi à des systèmes externes tels que LDAP.
- **Préparer les données pour l'exportation** : Convient aux scripts où les ID internes doivent être transformés pour répondre aux normes et exigences des systèmes externes.

## Exceptions
- **Exigence de pertinence et d'exactitude des données** : L'efficacité de l'étape dépend de l'exactitude et de la pertinence des données internes et de leur conformité à la structure du système externe.
- **Gestion du mappage des données** : Vous devez vous assurer que tous les ID internes sont correctement mappés aux clés primaires du système externe pour éviter les erreurs d'intégration.