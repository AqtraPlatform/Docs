# Menu d'accueil

<br>

La page fournit des informations sur votre licence et les domaines d'application qui ont été déployés. Vous aurez accès aux fonctionnalités et informations suivantes :

- **Type de plan** : Cela affiche le type de votre plan actuel et la date d'expiration ou de renouvellement de votre abonnement.
- **Domaines d'application** : Cette section vous permet de créer des composants d'application, de connecter des utilisateurs via des URL spécifiques et de naviguer vers la section "Menu de navigation".
- **Statistiques d'utilisation** : Affiche des informations sur le nombre actuel d'applications par rapport à la limite totale, ainsi que le nombre actuel et total d'utilisateurs, de flux de travail et de flux de données.
  <br>

![Tableau de bord principal](../assets/images/user-interface/main-dashboard.png)
<br>

## En savoir plus sur la configuration des domaines d'application

Les domaines d'application sont des espaces externes avec une URL spécifique (HTTP/HTTPS://<votre-nom-de-domaine>) où vous pouvez déployer vos composants.

**Par défaut, une application est disponible** nommée ‘digital-workplace’. Vous pouvez ajouter d'autres applications en utilisant le bouton ‘Ajouter une application’ dans le coin supérieur droit de la barre d'outils. Chaque application que vous ajoutez apparaît dans la liste des applications sous la description de votre plan.

Dans le domaine d'application, les paramètres suivants peuvent être définis dans les ‘paramètres principaux’ :

| Groupe de paramètres | Champ de paramètre     | Options de valeur                                 | Objectif                                               |
| -------------------- | ---------------------- | ------------------------------------------------- | ----------------------------------------------------- |
| Paramètres principaux | Titre                  | -                                                 | Titre de l'onglet du navigateur                        |
|                      | Masquer la barre supérieure | vrai, faux                                      | Masquer le menu supérieur pour le lieu de travail     |
|                      | Menu statique          | vrai, faux                                        | Affichage constant des menus ou affichage au survol de la souris |
|                      | Masquer les fil d'Ariane | vrai, faux                                      | Affichage/masquage de la navigation hiérarchique      |
|                      | Masquer la connexion utilisateur | vrai, faux                                   | Affichage/masquage de la connexion utilisateur         |
|                      | Masquer la sélection de langue | vrai, faux                                    | Affichage/masquage de la sélection de localisation     |
|                      | Choisir un logo        | Logo, Petit logo, favicon, "Pas d'image" placeholder | Choisir un logo pour WorkPlace (différents types)     |
|                      | Stockage de session utilisateur | local/session                               | Sauvegarde des paramètres d'autorisation dans une session ou localement |
|                      | Fournisseur Idp par défaut | Multisélection de Catalogue                     | Choisir une méthode d'autorisation                    |
|                      | Langue par défaut      | Multisélection de Catalogue                       | Localisation par défaut                                |
|                      | Application d'infos utilisateur par défaut | Multisélection de Catalogue              | Application principale pour gérer les données utilisateur |
|                      | Composant par défaut    | Multisélection de Catalogue                       | Composant par défaut                                   |
|                      | Page par défaut        | -                                                 | Page de composant par défaut                           |
|                      | Composant de connexion  | Multisélection de Catalogue                       | Composant du formulaire d'autorisation                 |
|                      | Activer SIP            | Vrai, Faux                                       | Intégration de construction avec SIP                   |

<br>
Dans ce groupe, vous pouvez définir les paramètres des modules globaux via JavaScript et CSS, ce qui vous permet de transformer la plateforme en un système de gestion de contenu (CMS), ainsi que de télécharger et d'utiliser n'importe quelle bibliothèque tierce.

Exemple JS pour JavaScript global :

```javascript
loadScript([
  'https://code.jquery.com/jquery-3.7.1.min.js?integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=&crossorigin="anonymous"',
])
  .then((res) => {
    return loadScript([
      'https://code.jquery.com/ui/1.13.2/jquery-ui.min.js?integrity="sha256-lSjKY0/srUM9BE3dPm+c4fBo1dky2v27Gdjm2uoZaL0="&crossorigin="anonymous"',
    ]);
  })
  .subcribe({
    complete: () => {
      console.log("Load scripts complete");
    },
    error: (err) => {
      console.log("Load scripts err:" + err);
    },
  });
```

<br>

De plus, il existe un groupe de paramètres de « paramètres de style » :

| Groupe de paramètres | Champ de paramètre        | Objectif              |
| -------------------- | ------------------------ | --------------------- |
| Police principale     | Police                   | Police principale de l'application |
| Schéma de couleurs    | Thème par défaut         | Schéma de couleurs par défaut |
|                      | Couleur claire principale | Couleur claire principale     |
|                      | Couleur principale       | Couleur principale           |
|                      | Couleur sombre principale | Couleur sombre principale      |
|                      | Couleur plus sombre      | Couleur plus sombre    |
|                      | Couleur de texte principale | Couleur de texte par défaut   |

<br>

Groupe de paramètres « Modifier le manifeste » :

| Champ de paramètre         | Objectif                         |
| -------------------------- | -------------------------------- |
| Nom                        | Nom de l'application dans le manifeste |
| Nom court                  | Nom court de l'application           |
| Choisir une icône (192x192) | Choisir une icône d'application de 192x192px   |
| Choisir une icône (512x512) | Choisir une icône d'application de 512x512px   |

<br>

## Intégration SIP

Si l'option « Activer SIP » dans les « Paramètres principaux » est activée, plusieurs paramètres subséquents sont nécessaires pour que les appels depuis le lieu de travail fonctionnent correctement.

**Du côté du studio :**

| Champ de paramètre        | Objectif                                                               |
| ------------------------- | --------------------------------------------------------------------- |
| Serveur SIP WebSocket     | Adresse du serveur SIP WebSocket (par exemple, 'wss://test-pbx.aqtra.ru:8089/ws') |
| Domaine SIP               | Domaine SIP (realm)                                                   |

<br>

**Du côté du lieu de travail :**

| Champ de paramètre        | Objectif                                                               |
| ------------------------- | --------------------------------------------------------------------- |
| Nom d'utilisateur SIP     | Nom de l'utilisateur SIP                                              |
| Mot de passe utilisateur SIP | Mot de passe de l'utilisateur SIP                                      |
| Serveur SIP WebSocket     | Adresse du serveur SIP WebSocket (par exemple, 'wss://test-pbx.aqtra.ru:8089/ws') |
| Domaine SIP               | Domaine SIP (realm)                                                   |

<br>

Si tous les paramètres sont correctement configurés, vous pourrez passer des appels depuis le lieu de travail. Vous pouvez lire sur le travail avec SIP dans le script du composant ici : [Utiliser Python](../app-development/using-python.md).