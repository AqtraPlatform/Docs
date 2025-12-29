# Enregistrer un utilisateur externe

![](../../assets/images/app-development/register-external-user.png)

## Informations générales
L'étape "Enregistrer un utilisateur externe" est destinée à l'enregistrement d'utilisateurs individuels ou de groupes d'utilisateurs. Cette étape est conçue dans le contexte de l'intégration LDAP et est utilisée pour l'intégration avec des systèmes externes, facilitant le processus de remplacement des utilisateurs de ces systèmes et leur connexion au système actuel.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | -                 | Sélection de l'étape précédente |
| Nom d'utilisateur   | -                 | Nom d'enregistrement ou ID utilisateur |
| Champ clé          | -                 | Champ contenant des informations clés pour identifier l'utilisateur |
| Fournisseur d'authentification | -       | Fournisseur d'authentification utilisé pour enregistrer l'utilisateur |

## Cas
- **Intégration des utilisateurs à partir de systèmes externes** : Utilisé pour remplacer et enregistrer des utilisateurs provenant de LDAP ou d'autres systèmes externes, garantissant leur intégration correcte dans le système actuel.
- **Automatisation du processus d'enregistrement** : Convient aux scripts où il est nécessaire d'automatiser le processus d'enregistrement d'un grand nombre d'utilisateurs, minimisant le travail manuel et les erreurs possibles.

## Exceptions
- **Dépendance à l'exactitude des données d'entrée** : L'efficacité de l'étape dépend de l'exactitude et de l'exhaustivité des données reçues du système externe.