# Modèles de jointure

![](../../assets/images/app-development/join-models.png)

## Informations générales
L'étape "Modèles de jointure" est conçue pour fusionner des données provenant de deux sources différentes. Elle ajoute des données de la source de l'"Étape droite" aux données de la source de l'"Étape gauche" si des entrées correspondantes sont trouvées dans les deux sources.

L'étape crée un nouveau modèle de données en fusionnant les flux de données définis dans les paramètres de l'"Étape gauche" et de l'"Étape droite". L'étape attend que les deux flux aient terminé le traitement, puis trie et fusionne les données.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape gauche       | -                 | Source de données pour le côté gauche des flux fusionnés |
| Étape droite       | -                 | Source de données pour le côté droit des flux fusionnés |
| Clé gauche         | -                 | Clé pour fusionner les données de la source gauche |
| Clé droite         | -                 | Clé pour fusionner les données de la source droite |
| Mappage            | -                 | Mappage des champs entre les sources gauche et droite |

## Cas d'utilisation
- **Fusion des flux de données** : Utilisé pour fusionner deux flux de données différents en un seul modèle, vous permettant d'analyser et de traiter les données fusionnées.
- **Enrichissement des données** : Utilisé pour ajouter des informations supplémentaires d'un ensemble de données à un autre, améliorant ainsi la complétude des informations.

## Exceptions
- **Besoin d'une clé de fusion exacte** : Des erreurs dans la définition de la "Clé gauche" et de la "Clé droite" peuvent entraîner une fusion de données incorrecte ou inefficace.

## Scénario d'application

Ce composant permet de **tester** et de **vérifier** la fonctionnalité d'un flux de données où les données sont **fusionnées** à partir de différentes sources. Il fournit un **mappage des champs** et une **vérification de la fusion des données** sur le **frontend** et dans l'aperçu de la réponse **HTTP**.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1YRpXJwNSTp_jOPxP-j0M9SvocZw1W6Tt/view?usp=sharing).