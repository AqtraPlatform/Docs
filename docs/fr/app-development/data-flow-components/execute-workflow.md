# Exécuter le flux de travail

![](../../assets/images/app-development/execute-workflow.png)

## Informations générales
L'étape "Exécuter le flux de travail" est utilisée pour activer et exécuter un flux de travail spécifique dans le système.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre      | Options de valeur | Objectif |
|-------------------------|-------------------|----------|
| Nom de l'étape          | -                 | Nom de l'étape |
| Étape source            | -                 | Sélection de l'étape précédente |
| Composant               | -                 | Le composant dans lequel le flux de travail est exécuté |
| Flux de travail         | -                 | Nom du flux de travail à compléter |
| Champ d'entrée du composant | -             | Le champ dans le composant utilisé pour transférer des données au flux de travail |

## Cas d'utilisation
- **Contrôle dynamique du flux de données** : Il peut être utilisé pour lancer des flux de travail spécifiques en fonction des données obtenues des étapes précédentes de Dataflow, ce qui permet de créer des systèmes de gestion des données flexibles et adaptatifs.

## Exceptions
- **Dépendance à l'exactitude des données** : Pour éviter des erreurs dans l'exécution du flux de travail, il est nécessaire de s'assurer que les données envoyées au flux de travail sont précises et complètes.
- **Coordination entre Dataflow et Workflow** : Il est important de configurer soigneusement l'interaction entre Dataflow et Workflow pour garantir un transfert fluide et correct des données et des commandes entre eux.

## Scénario d'application

Le composant créé sert d'interface pour interagir avec le modèle de données contenant un champ "user_name" de type chaîne. Ce composant inclut une fonctionnalité pour mettre à jour le modèle de données en utilisant l'étape Mettre à jour le modèle dans le flux de travail. Pour interagir avec le composant, l'utilisateur peut saisir son nom, cliquer sur un bouton, après quoi les données seront envoyées, et le nom sera affiché dans la grille de données après le rafraîchissement de la page.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing).