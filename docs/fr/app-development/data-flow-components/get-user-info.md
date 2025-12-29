# Obtenir des informations utilisateur

![](../../assets/images/app-development/get-user-info.png)

## Informations générales
L'étape "Obtenir des informations utilisateur" est utilisée pour obtenir des données sur l'utilisateur de la plateforme, telles que l'email, le prénom et le nom de famille, pour un traitement ultérieur dans le flux de données actuel. Cette étape est requise pour la plupart des opérations utilisateur, sauf pour la création d'un nouvel utilisateur.

**Obtention des informations utilisateur**
1. **Utilisation du drapeau ‘Obtenir des informations utilisateur à partir de la requête’** : L'étape tentera de récupérer des données sur l'utilisateur actuel. Pour que cela fonctionne correctement, il est nécessaire que le flux de données soit appelé au nom d'un utilisateur spécifique (par exemple, à partir d'un formulaire de demande ou via une requête Proxy). S'il est appelé au nom de la plateforme (par exemple, dans le flux de données d'entrée), le résultat sera nul.
2. **Sans le drapeau ‘Obtenir des informations utilisateur à partir de la requête’** : L'utilisateur peut être défini :
   - Via le nom du système, en utilisant un paramètre de chaîne du modèle de flux de données actuel.
   - Via un lien vers le répertoire d'informations utilisateur, par exemple, les champs creatorSubject ou changeAuthor.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre        | Options de valeur | Objectif |
|---------------------------|-------------------|----------|
| Nom de l'étape            | -                 | Nom de l'étape |
| Étape source              | -                 | Sélection de l'étape précédente |
| Obtenir des informations utilisateur à partir de la requête | - | Drapeau pour obtenir des informations sur l'utilisateur actuel |
| Champ d'informations utilisateur | -         | Champ d'identification de l'utilisateur |
| Nom d'utilisateur         | -                 | Nom de l'utilisateur |
| Champ de stockage du résultat | -             | Champ pour enregistrer les informations obtenues sur l'utilisateur |

## Cas d'utilisation
- **Récupération des données utilisateur pour traitement** : Utilisé pour extraire des informations utilisateur pour une utilisation ultérieure dans le flux de données.
- **Envoyer des notifications personnalisées** : Dans les cas où vous devez envoyer des notifications par email personnalisées aux utilisateurs, l'étape "Obtenir des informations utilisateur" est utilisée pour obtenir leurs adresses email. Ces informations sont ensuite transmises à l'étape conçue pour l'envoi de notifications.

## Exceptions
- **Gestion de l'utilisateur non trouvé** : Dans les cas où l'utilisateur ne peut pas être identifié, le résultat sera nul, ce qui nécessite un traitement supplémentaire dans le flux de données.

## Scénario d'application

Le composant "Obtenir des informations utilisateur" est conçu pour récupérer des informations sur un utilisateur. Dans un flux de données, cette étape est utilisée pour interroger les données utilisateur en fonction de critères spécifiés, tels qu'un nom d'utilisateur ou d'autres informations d'identification. Par exemple, dans un flux de données, vous pouvez spécifier le nom d'un utilisateur pour récupérer des informations à son sujet, puis utiliser ces informations pour d'autres actions, telles que les afficher sur un écran ou mettre à jour une base de données.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/16keZXK_MXlWLmcSA4a-nLvhx-GPP3RPy/view?usp=sharing)