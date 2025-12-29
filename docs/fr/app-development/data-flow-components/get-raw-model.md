# Obtenir le modèle brut

![](../../assets/images/app-development/get-raw-model.png)

## Informations générales
L'étape "Obtenir le modèle brut" est utilisée dans un flux de données, qui nécessite le traitement d'un modèle de données personnalisé qui ne correspond pas au modèle de composant standard, au flux de travail ou à d'autres options standard. Les cas d'utilisation typiques incluent un flux de données appelé depuis un script de composant avec des variables définies dans le script, ainsi que le traitement des données de formulaire dans une structure multi-composants.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre     | Options de valeur | Objectif |
|------------------------|-------------------|----------|
| Nom de l'étape         | -                 | Nom de l'étape |
| Valider les valeurs d'entrée | true, false   | Indique que les valeurs d'entrée doivent être vérifiées pour leur exactitude avant le traitement |

## Cas
- **Intégration avec le script de composant** : Utilisé pour le flux de données appelé depuis le script de composant lorsque des variables ou des données spécifiques sont requises.
- **Traitement des données de formulaire multi-composants** : Convient aux scripts où les flux de données travaillent avec des données obtenues à partir de formulaires dans une structure multi-composants.

## Exceptions
- **Exigence de configuration du modèle** : Vous devez préconfigurer le modèle de données au format JSON.
- **Caractéristiques du format de modèle** : Une configuration incorrecte du modèle peut entraîner un traitement incorrect des données ou des erreurs de flux de données.