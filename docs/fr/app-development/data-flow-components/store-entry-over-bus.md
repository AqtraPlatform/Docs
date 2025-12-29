# Entrée de magasin via le bus

![](../../assets/images/app-development/store-entry-over-bus.png)

## Informations générales

L'étape "Entrée de magasin via le bus" est conçue pour stocker le modèle dans les données du composant (champs) via le bus. Cette étape crée toujours une nouvelle instance du composant spécifié et est utilisée pour travailler dynamiquement avec les données dans le système. L'étape est appelée de manière asynchrone.

## Paramètres

**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur      | Objectif                                                                             |
| ------------------ | ---------------------- | ----------------------------------------------------------------------------------- |
| Nom de l'étape     | -                      | Nom de l'étape                                                                      |
| Étape source       | -                      | Sélection de l'étape précédente                                                     |
| Composant          | -                      | Sélection parmi les composants disponibles pour enregistrer l'entrée                |
| Nom                | Chaîne                | Nom système de l'entrée à afficher en utilisant des liens de type Catalogue         |
| Clés               | AJOUTER UNE CLÉ       | Pour les composants avec le drapeau Restreindre l'accès, spécifiant les clés pour mapper les champs |
| Champ clé          | Multisélection de Catalogue | Champs contenant les clés primaires du composant sélectionné                       |
| Mappage des champs | -                      | Configuration dynamique du mappage des modèles de composants au modèle de flux de données |

## Cas d'utilisation

- **Création de nouvelles instances de composants** : Utilisé pour créer automatiquement de nouvelles entrées dans les composants en fonction des données dans le flux de données.

## Exceptions

- **Dépendance à la disponibilité des clés primaires dans le composant** : L'efficacité de l'étape dépend de la disponibilité et de la justesse des clés primaires dans le composant cible, surtout si le composant a le drapeau Restreindre l'accès.
- **Exigence de traitement asynchrone** : L'étape est effectuée de manière asynchrone, ce qui peut affecter la séquence et le temps de traitement du système.

## Scénario d'application

Ce composant permet de récupérer des données de l'intégration sélectionnée et de les stocker dans les champs correspondants des modèles de données créés. Les données récupérées peuvent ensuite être utilisées dans d'autres parties du système pour un traitement ou un affichage ultérieur.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1jFuXBG8v-YuICBozvoCPAm0FfBQhApvG/view?usp=sharing)