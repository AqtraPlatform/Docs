# Enregistrer le contexte pour le modèle

![](../../assets/images/app-development/register-context-for-model.png)

## Informations générales
L'étape « Enregistrer le contexte pour le modèle » est utilisée dans le cadre de l'intégration LDAP pour enregistrer le contexte de sécurité des utilisateurs enregistrés dans un système externe. Cette étape garantit que les données concernant les utilisateurs et leurs rôles sont synchronisées entre le système externe et le système actuel, en utilisant des clés pour identifier et enregistrer le contexte.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Composant          | -                 | Composant pour lequel le contexte est enregistré |
| Champ de nom       | -                 | Champ qui indique le nom ou l'identifiant de l'entité |
| Clés               | -                 | Clés utilisées pour identifier de manière unique une entité |

## Cas
- **Intégration LDAP** : Utilisé pour synchroniser et enregistrer les données des utilisateurs à partir de LDAP dans le système actuel.
- **Gestion des rôles et des accès** : Convient aux scripts qui nécessitent une correspondance précise et un suivi des rôles des utilisateurs enregistrés dans des systèmes externes.

## Exceptions
- **Exigences de précision des clés** : Les clés doivent être correctement appariées pour identifier et enregistrer correctement les utilisateurs dans le système.
- **Gestion des changements dans les systèmes externes** : Les changements de rôles ou de statuts des utilisateurs dans un système externe nécessitent une mise à jour appropriée dans le système actuel, ce qui peut représenter un défi face à des données en évolution dynamique.