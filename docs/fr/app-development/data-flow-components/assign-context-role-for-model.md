# Assigner un rôle de contexte pour le modèle

![](../../assets/images/app-development/assign-context-role-for-model.png)

## Informations générales
L'étape "Assigner un rôle de contexte pour le modèle" est utilisée pour lier un utilisateur ou un groupe d'utilisateurs à un rôle et un contexte spécifiques. Ce processus nécessite qu'au moins un rôle soit configuré dans la section "Rôles" du menu "Accès". Cette étape vous permet d'établir des relations entre les utilisateurs et les rôles dans le contexte d'un modèle de données spécifique, fournissant ainsi un contrôle sur l'accès et les permissions des utilisateurs.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Champ UserId       | -                 | Champ d'ID utilisateur |
| Champ ContextId    | -                 | Champ d'ID de contexte |
| Sélectionner les contextes | -         | Sélection des contextes auxquels le rôle sera lié |

## Cas d'utilisation
- **Gestion des accès utilisateurs** : Utilisé pour assigner des rôles aux utilisateurs déterminant leur accès et leurs permissions au sein du système.
- **Gestion dynamique des rôles lors de l'interaction avec l'UI** : Cette étape est efficacement utilisée pour changer ou mettre à jour les rôles des utilisateurs en temps réel en fonction de leurs actions et interactions avec les éléments de l'interface utilisateur. Cela permet d'adapter l'accès et les permissions des utilisateurs en fonction d'actions ou de scénarios spécifiques d'utilisation du système.

## Exceptions
- **Exigence de rôles configurés** : Pour un lien réussi, le système doit avoir les rôles appropriés préconfigurés.
- **Dépendance à l'exactitude des ID** : L'identification précise des ID utilisateurs et des contextes est essentielle pour que l'étape fonctionne correctement.