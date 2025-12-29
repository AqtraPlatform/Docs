# Distinct

![](../../assets/images/app-development/distinct.png)

## Informations générales
L'étape Distinct est utilisée pour éliminer les entrées dupliquées du flux de données, ne laissant que des valeurs uniques. Ce processus aide à optimiser le traitement des données en éliminant les doublons et en réduisant la quantité de données analysées.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif                           |
|--------------------|-------------------|------------------------------------|
| Nom de l'étape     | -                 | Nom de l'étape dans le flux de données        |
| Étape source       | -                 | Sélection de l'étape précédente |
| Clés               | -                 | Clés pour vérifier l'unicité      |

## Cas d'utilisation
- **Nettoyage des données** : Suppression des entrées dupliquées pour simplifier l'analyse.
- **Préparation à l'agrégation** : Pré-nettoyage des données avant d'effectuer des opérations d'agrégation.

## Exceptions
- **Sélection des clés** : Une sélection incorrecte des clés peut entraîner la perte de données importantes.
- **Perte d'informations** : Risque de perdre une partie des données si l'étape est configurée incorrectement.

## Scénario d'application

Ce composant vérifie la disponibilité des champs dans l'étape Distinct. Le bouton "Distinct" est cliqué sur le frontend. Si l'étape fonctionne correctement, une ligne "execute" avec un aperçu de la réponse HTTP devrait apparaître dans l'onglet Réseau, contenant des données pour trois enregistrements.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1dA9EzzJOn9sWBYhdvL__AcI1kJ5qNNLd/view?usp=sharing).