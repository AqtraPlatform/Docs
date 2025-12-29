# Supprimer les rôles assignés pour l'utilisateur

![](../../assets/images/app-development/remove-assigned-roles-for-user.png)

## Informations générales
L'étape « Supprimer les rôles assignés pour l'utilisateur » est utilisée pour réinitialiser tous les rôles assignés à un utilisateur particulier. Cela permet aux administrateurs système et aux gestionnaires de processus de supprimer les rôles des utilisateurs, simplifiant ainsi la gestion des autorisations et des contrôles de sécurité.

## Paramètres
**Paramètres de l'étape :**

| Champ             | Options de valeur  | Objectif |
|------------------|--------------------|------------|
| Nom de l'étape   | -                  | Nom de l'étape |
| Étape source     | -                  | Sélection de l'étape précédente |
| Champ d'identifiant utilisateur | Nom d'une variable de type informations utilisateur | Champ contenant l'ID utilisateur pour la réinitialisation des rôles |

## Cas d'utilisation
- **Gestion des accès et des rôles** : Cette étape est idéale pour les scripts où vous souhaitez rapidement changer ou réinitialiser les rôles des utilisateurs, par exemple lorsque les responsabilités professionnelles changent ou lorsqu'un employé quitte l'entreprise.
- **Assurer la sécurité du système** : Utilisé pour prévenir l'accès non autorisé aux données sensibles ou aux fonctionnalités du système en supprimant les rôles des utilisateurs qui n'ont plus besoin de telles autorisations d'accès.

## Exceptions
- **Dépendance à l'exactitude de l'identification de l'utilisateur** : L'efficacité de l'étape dépend de l'identification précise de l'utilisateur dont vous souhaitez réinitialiser les rôles.
- **Besoin d'obtenir d'abord l'ID utilisateur** : L'étape nécessite d'abord d'obtenir un ID utilisateur interne, ce qui peut être fait via l'étape « Obtenir des informations utilisateur » ou d'autres méthodes d'authentification.