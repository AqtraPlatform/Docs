# Menu de maintenance

<br>

Le menu “Maintenance” est un outil puissant pour gérer les données et maintenir le système, en particulier après des mises à jour majeures, des migrations de données ou des modifications de base de données.
<br>

## Description générale

- **Objectif** : Gérer les données PostgreSQL via ODATA, supprimer les données supprimées, analyser et gérer les journaux système.
- **Fonctionnalités** : L'outil est principalement utilisé après les mises à jour de version de la plateforme, les importations de composants ou les changements massifs de données.
  <br>

## Onglets du menu de maintenance

<br>

### Journaux système

<br>

! [Journaux système] (system-logs.png)
<br>

- **Fonctionnalité** : Voir les journaux système actuels et ajuster les niveaux de journalisation (Trace, Debug, Information, Avertissement, Critique, Erreur, Aucun).
  <br>

### Maintenance du système

<br>

! [Maintenance du système] (system-maintenance.png)
<br>

1. **Reconstruire les références de base de données** : Vérifier et reconstruire les références croisées entre les composants ou au sein des composants (flux de données/processus).
2. **Reconstruire les règles RLS** : Reconstruire les règles de sécurité au niveau des lignes pour personnaliser l'accès aux données.
3. **Reconstruire le cache** : Reconstruire le cache interne de la plateforme, résoudre les problèmes liés aux mises à jour.
4. **Analyse marquée pour suppression** : Voir et gérer les enregistrements marqués pour suppression en utilisant le drapeau ‘Marquer l'entrée pour suppression’ dans l'étape ‘Mettre à jour l'entrée’. Après avoir cliqué sur le bouton “Analyse marquée pour suppression”, toutes les entrées marquées sont affichées. Les entrées sont sélectionnées et supprimées via “Supprimer les éléments sélectionnés”. Le système empêchera la suppression des entrées s'il y a des entrées non étiquetées associées.
5. **Réinitialiser la publication actuelle** : Réinitialise le processus de publication s'il échoue.
   <br>

### Stockage de fichiers

Cette section ajoute la possibilité de configurer les paramètres suivants pour le stockage de fichiers :

| Types de fichiers acceptables | Limite de taille de fichier en octets |
| ----------------------------- | ------------------------------------- |
| .\* (tous les types de fichiers)  | taille sélectionnée                   |

<br>

Vous pouvez spécifier des types de filtres, en les séparant par des virgules. Cela peut être des extensions de fichiers, telles que .jpg, .json, .docx, ou des types Mime, par exemple, image/_, application/_

Vous pouvez également combiner des filtres, par exemple, `image/*`, `.docx`.
L'utilisation du filtre `*/*` vous permet de télécharger n'importe quel fichier.
<br>

![Maintenance du stockage de fichiers](../assets/images/user-interface/file-storage-maintenance.png)