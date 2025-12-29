# Flux de travail

## Qu'est-ce qu'un flux de travail ? {: #workflow }

Le flux de travail est un mécanisme de gestion des états et des tâches dans divers scripts de composants sur la plateforme. Il vous permet d'organiser l'exécution séquentielle des tâches, de maintenir les états et de fournir la possibilité de redémarrer en cas d'échec.

### Comment créer un flux de travail ?

1. **Ouvrir la Boîte à outils** : Ouvrez le menu Boîte à outils dans la fenêtre des composants et allez à l'onglet Flux.
2. **Ajouter un Flux de travail** : Cliquez sur l'icône Flux de travail et faites-la glisser dans l'espace de travail. Un nouveau flux de travail apparaîtra à configurer.

En utilisant le constructeur visuel de Flux de travail, vous pouvez configurer un script de flux de travail :

- **Ajouter des Étapes et des Phases** : L'éditeur vous permet d'ajouter des Étapes et des Phases qui forment la logique du flux de travail.
- **Configuration de la Séquence** : Les scripts s'exécutent de haut en bas et de gauche à droite, vous permettant de créer un flux de tâches cohérent.

### Paramètres du Flux de travail

- **Nom du flux de travail** : Le nom utilisé pour identifier le flux de travail dans le composant.
- **Restreindre l'accès** : Lorsqu'il est réglé sur "Oui", crée un contexte de sécurité pour le flux de travail.

### Édition des Phases et Étapes du Flux de travail

- **Ajouter des Phases** : En utilisant le bouton "+", vous pouvez ajouter de nouvelles phases.
- **Supprimer des Phases** : Le bouton "X" vous permet de supprimer des phases inutiles.
- **Modifier des Phases** : Seul le nom de la phase peut être changé.
- **Ajouter et Supprimer des Étapes** : Les étapes peuvent être ajoutées et supprimées au sein des phases, définissant des actions spécifiques du flux de travail.

## Groupe de Notifications

Composants pour l'envoi de notifications et de confirmations :

- [Étapes de Notifications](notifications-steps.md) - Vue d'ensemble des étapes de notification
- [Envoyer une Notification](send-notification.md) - Envoyer des notifications aux utilisateurs
- [Envoyer une Notification Modèle](send-templated-notification.md) - Envoyer des notifications basées sur des modèles
- [Obtenir la Confirmation de l'Utilisateur](get-user-confirmation.md) - Demander la confirmation de l'utilisateur

## Groupe d'Intégrations

Composants pour l'intégration avec d'autres systèmes :

- [Étapes d'Intégrations](integrations-steps.md) - Vue d'ensemble des étapes d'intégration
- [Exécuter le Flux de Données](execute-data-flow.md) - Exécuter le flux de données depuis le flux de travail

## Groupe Commun

Opérations courantes de flux de travail :

- [Étapes Communes](common-steps.md) - Vue d'ensemble des étapes communes
- [Mettre à Jour le Modèle](update-model.md) - Mettre à jour le modèle de données
- [Terminer](finish.md) - Compléter l'exécution du flux de travail
- [Mettre à Jour le Champ du Modèle](update-model-field.md) - Mettre à jour un champ spécifique du modèle
- [Réinitialiser au Brouillon](reset-to-draft.md) - Réinitialiser le flux de travail à l'état de brouillon

## Groupe de Conditions

Logique conditionnelle et ramification :

- [Étapes de Conditions](conditions-steps.md) - Vue d'ensemble des étapes de condition
- [Switch Case](switch-case.md) - Ramification switch-case
- [Condition If](if-condition.md) - Ramification conditionnelle