# Appliquer des opérations de mise à jour différées

![](../../assets/images/app-development/apply-deferred-update-operations.png)

## Informations générales
L'étape "Appliquer des opérations de mise à jour différées" est utilisée pour l'application en masse des mises à jour qui ont été préparées à l'aide de la série d'étapes "Entrée de mise à jour différée". Cette étape vous permet d'effectuer les opérations de mise à jour accumulées de manière efficace en les appliquant toutes en une seule fois.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre       | Options de valeur | Objectif |
|--------------------------|-------------------|----------|
| Nom de l'étape           | -                 | Nom de l'étape |
| Taille du lot            | 1000              | Taille du lot de données à traiter |
| Délai d'inactivité du lot en ms | -         | Délai d'inactivité en millisecondes entre les lots |
| Nombre de lots parallèles | 0                 | Nombre de lots de données traités en parallèle |

## Cas d'utilisation
- **Application de mise à jour en masse** : Idéal pour les scénarios où vous devez mettre à jour des données en masse, comme lorsque vous synchronisez une grande quantité de données ou lorsque vous devez apporter rapidement des modifications à plusieurs composants du système.
- **Optimisation des performances** : Améliore les performances pour les mises à jour en masse grâce au traitement parallèle et à la gestion efficace des lots de données.

## Exceptions
- **Gestion de la séquence de mise à jour** : Il est important de s'assurer que les mises à jour sont séquencées correctement, surtout si les données dans les différentes étapes de l'“Entrée de mise à jour différée” sont interconnectées.
- **Configuration des paramètres de traitement par lots** : Des paramètres tels que la taille des lots et le nombre de lots parallèles doivent être soigneusement configurés pour éviter de surcharger le système et garantir que les mises à jour sont effectuées efficacement.

## Scénario d'application

Le composant avec une définition personnalisée configure un flux de données pour la mise à jour des enregistrements. Les utilisateurs commencent par extraire le modèle d'action à l'aide de l'étape "Obtenir le modèle d'action". Ensuite, l'étape "Entrée de mise à jour différée" est utilisée pour les mises à jour différées des enregistrements, où les utilisateurs peuvent spécifier le composant, l'ID du composant et les mappages de champs. L'étape "Appliquer la mise à jour différée" permet de configurer les paramètres de traitement par lots et d'exécution parallèle. Après avoir complété ces étapes, le composant est prêt pour mettre à jour, créer ou supprimer des enregistrements, ce qui se produit sur le frontend lors de l'interaction avec les éléments d'interface correspondants.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/16uo9P5IWDv-QnT749fYDISyyWEbKrDVR/view?usp=sharing)