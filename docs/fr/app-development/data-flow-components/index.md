# Flux de données

## Qu'est-ce que le flux de données ? {: #dataflow }

Le flux de données, ou data flow, dans la plateforme est un composant clé qui permet aux utilisateurs de traiter et de transformer des données au sein d'une application. C'est un outil puissant pour intégrer des données, traiter des événements et automatiser des processus métier.

Le flux de données est construit sur la plateforme à l'aide d'un 'éditeur visuel' du flux de données :

L'éditeur visuel de flux de données est un concepteur intuitif pour créer et gérer des flux de données. Cet outil permet aux utilisateurs de créer séquentiellement un ensemble d'Étapes et de Phases pour mettre en œuvre des scripts de traitement de données complexes.

- **Ajouter une Phase** : Cela se fait en appuyant sur l'icône "+" dans le panneau de contrôle du flux de données. Vous pouvez ajouter un nombre illimité de phases en fonction des besoins de votre script.
- **Supprimer une Phase** : Pour supprimer une phase, utilisez le bouton "X" sur le bloc de phase sélectionné.
- **Modifier une Phase** : Vous ne pouvez modifier que le nom de la phase sélectionnée.
- **Ajouter une Étape** : Une nouvelle étape est ajoutée en appuyant sur le bouton "AJOUTER ÉTAPE" à la phase appropriée. Les utilisateurs peuvent choisir des types d'étapes parmi les groupes d'activités proposés.
- **Supprimer une Étape** : Pour supprimer une étape, cliquez sur l'icône "X" sur le bloc d'étape sélectionné.

## Groupe d'Entrée

Composants pour récupérer et importer des données :

- [Étapes d'Entrée](input-steps.md) - Vue d'ensemble des étapes d'entrée
- [Obtenir des Valeurs du Connecteur](get-values-from-connector.md) - Récupérer des données des connecteurs
- [S'abonner au Connecteur](subscribe-to-connector.md) - S'abonner aux mises à jour de données
- [Obtenir le Modèle d'Action](get-action-model.md) - Récupérer le modèle d'action
- [Obtenir le Modèle de Workflow](get-workflow-model.md) - Récupérer le modèle de workflow
- [Obtenir le Modèle Vide](get-empty-model.md) - Créer un modèle de données vide
- [Proxy Obtenir Entrée](proxy-get-entry.md) - Récupération d'entrée par proxy
- [Proxy Requête Entrée](proxy-query-entry.md) - Exécution de requête par proxy
- [Obtenir le Modèle Brut](get-raw-model.md) - Récupérer le modèle de données brut
- [Importer Fichier](import-file.md) - Importer des données à partir de fichiers

## Groupe de Transformation de Modèle

Composants pour la transformation et le traitement des données :

- [Étapes de Transformation de Modèle](model-transformation-steps.md) - Vue d'ensemble des étapes de transformation
- [Transformer le Modèle](transform-model.md) - Transformer des modèles de données
- [Joindre des Modèles](join-modes.md) - Joindre plusieurs modèles de données
- [Extraire des Collections](extract-collections.md) - Extraire des données de collection
- [Filtrer la Source](filter-source.md) - Filtrer les sources de données
- [Recherche de Référence](lookup-reference.md) - Recherche de référence
- [Exécuter le Script](execute-script.md) - Exécuter des scripts personnalisés
- [Requête Entité par Filtre](query-entity-by-filter.md) - Requêtes basées sur des filtres
- [Sélectionner Plusieurs](select-many.md) - Sélection multiple
- [Obtenir l'Entité par ID](get-entity-by-id.md) - Récupérer par identifiant
- [Charger des Catalogues par Clé](load-catalogs-by-key.md) - Charger des données de catalogue
- [Distinct](distinct.md) - Obtenir des valeurs distinctes
- [Grouper par](group-by.md) - Grouper des données
- [Calculer Tableau](calculate-array.md) - Calculs de tableau
- [Mathématiques Simples](simple-math.md) - Opérations mathématiques
- [Exécuter le Flux de Données](execute-dataflow.md) - Exécuter un flux de données imbriqué
- [Obtenir les Infos du Fichier](get-file-info.md) - Récupérer des informations sur le fichier

## Groupe de Contextes Utilisateur

Composants pour la gestion des utilisateurs et l'authentification :

- [Étapes de Contextes Utilisateur](user-contexts-steps.md) - Vue d'ensemble des étapes de contexte utilisateur
- [Enregistrer le Contexte pour le Modèle](register-context-for-model.md) - Enregistrer le contexte du modèle
- [Enregistrer Utilisateur Externe](register-external-user.md) - Enregistrement d'utilisateur externe
- [Préparer Clés Externes](prepare-external-keys.md) - Préparer des clés d'authentification
- [Attribuer Rôle de Contexte pour le Modèle](assign-context-role-for-model.md) - Attribuer des rôles
- [Obtenir Code à Usage Unique pour l'Utilisateur](get-one-time-code-for-user.md) - Générer un OTP
- [Confirmer le Code à Usage Unique pour l'Utilisateur](confirm-one-time-code-for-user.md) - Vérifier l'OTP
- [Mettre à Jour ou Créer les Infos de l'Utilisateur](update-or-create-user-info.md) - Gestion des informations utilisateur
- [Obtenir les Infos de l'Utilisateur](get-user-info.md) - Récupérer les données utilisateur
- [Connexion avec Mot de Passe](login-with-password.md) - Authentification par mot de passe
- [Demande de Réinitialisation du Mot de Passe de l'Utilisateur](reset-user-password-request.md) - Réinitialisation du mot de passe
- [Confirmer la Demande d'Email de l'Utilisateur](confirm-user-email-request.md) - Vérification de l'email
- [Envoyer Notification Modèle](send-templated-notification.md) - Notifications basées sur des modèles
- [Envoyer Notification](send-notification.md) - Envoyer des notifications
- [Supprimer les Rôles Attribués pour l'Utilisateur](remove-assigned-roles-for-user.md) - Supprimer les rôles utilisateur

## Groupe de Sortie

Composants pour la sortie de données et les actions :

- [Étapes de Sortie](output-steps.md) - Vue d'ensemble des étapes de sortie
- [Stocker l'Entrée via le Bus](store-entry-over-bus.md) - Stocker des données via le bus de messages
- [Mettre à Jour l'Entrée](update-entry.md) - Mettre à jour les entrées de données
- [Mise à Jour Différée de l'Entrée](deferred-update-entry.md) - Mises à jour différées
- [Appliquer les Opérations de Mise à Jour Différée](apply-deferred-update-operations.md) - Appliquer des opérations différées
- [Exécuter Appel API](execute-api-call.md) - Appels API externes
- [Écrire la Réponse](write-response.md) - Écrire les données de réponse
- [Action de Formulaire](form-action.md) - Actions de soumission de formulaire
- [Exécuter le Workflow](execute-workflow.md) - Exécuter le workflow
- [Exporter vers Fichier](export-to-file.md) - Exporter des données vers des fichiers
- [Rendre le Modèle](render-template.md) - Rendu de modèle