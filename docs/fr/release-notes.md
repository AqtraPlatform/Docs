# Descriptions des versions

!!! note "La plateforme Aqtra évolue constamment !"
De nouvelles versions sont normalement publiées une fois par mois pour :

    - Cluster Kubernetes
    - Mini-image Docker

<br>

## Version 0.13.x

> **Fonctionnalités ajoutées**

- **Nouveau module de composant** : Au sein du composant, le module **Web parts** a été ajouté, qui se compose de deux blocs : “Styles” et “JavaScript”. Ce module est similaire au module “Component Script”, mais au lieu d'interagir avec Python, vous pouvez décrire des styles CSS dans le bloc “Styles” et interagir en JavaScript dans le bloc “JavaScript” ;
- **Configuration des modules globaux dans le domaine de l'application** : La configuration des modules CSS et JavaScript globaux a été ajoutée dans les **Paramètres principaux** du **domaine de l'application**. Plus de détails **ici** ;
- **Nouveaux outils dans le menu de maintenance** : Un paramètre a été ajouté pour la section **Stockage de fichiers**. Plus de détails **ici** ;
- **Nouveaux paramètres de modèle d'objet pour les données de type fichier** : Vous pouvez désormais définir une validation par type de fichier et une limite de taille de fichier en octets ;
- **Support XSRF/CSRF** : Le composant de téléchargement de fichiers élimine désormais le transfert de données binaires via JS et ajoute l'envoi XSRF. Les demandes de téléchargement de fichiers sont désormais ciblées et l'accès direct au stockage de fichiers est exclu. Des améliorations ont également été apportées au lieu de travail pour recevoir un jeton XSRF lors du chargement d'une page, et le contrôleur OData a été amélioré pour charger des fichiers. L'envoi de demandes depuis le lieu de travail pour télécharger des fichiers est désormais également ciblé, et l'accès direct au stockage de fichiers est impossible.
  <br>

> **Design mis à jour**

- **Section Export/Import** : Le design de la section d'exportation/importation du menu **Applications** a été mis à jour.
  <br>

## Version 0.12.x

> **Fonctionnalités ajoutées**

- **Envoyer une notification** : Un nouveau pas dans le flux de données “Envoyer une notification” a été ajouté. Ce pas vous permet d'envoyer des notifications simples à l'utilisateur, ce qui améliore la manière dont vous interagissez avec l'utilisateur via le système de notification. Plus de détails ici : **Envoyer une notification**
- **Grille de pivot** : Un nouvel élément d'interface utilisateur “Grille de pivot” a été ajouté pour l'analyse et la visualisation des données. Plus de détails ici : **Grille de pivot**
- **Modifications de la **Vue de liste** :
  - Capacité d'étendre le composant horizontalement ou verticalement.
  - La possibilité d'activer le glisser-déposer a été ajoutée pour tous les groupes d'un composant ou par choix.
  - La fonction d'activation a été ajoutée aux événements après utilisation du glisser-déposer.
- **Modifications de la **Grille de données** :
  - Le mécanisme de sélection multiple a été modifié. Dans les paramètres de la grille de données, il y a maintenant une option “Mode de sélection” avec un choix : `None`, `Single`, `Multiple`, `Checkbox`.
  - Nouveaux événements : `On Table Changed`, `On Header Changed`, `On Row Changed`, `On Cell Changed`.
  - Capacité de sélectionner le nombre de lignes dans le paginator à l'avant.
- **Modifications dans **Vue de graphique** :
  - Le paramètre de schéma de couleurs a été supprimé.
  - Les paramètres Min/Max ont été ajoutés.
- **Intégration du client SIP** :
  - Capacité de passer des appels depuis le lieu de travail grâce à l'intégration du client SIP. Plus de détails **ici**.
- **Images de remplacement pour les images manquantes dans les paramètres des domaines d'application et l'élément UI "Image"** : Plus de détails dans [Documentation de l'interface utilisateur](user-interface/index.md) et [Composant Image](app-development/ui-components/image.md).
- **Nouvelles méthodes pour gérer l'état des éléments UI**. Plus de détails dans **documentation**.
- **Téléchargement en masse d'images via http.client et stockage de fichiers dans les scripts de flux de données** : Une fonction pour le téléchargement en masse d'images a été ajoutée. Plus de détails dans **documentation**.
- **Optimisation du mécanisme de publication** : Le mécanisme de publication a été amélioré en utilisant une machine à états, fournissant un processus stable avec la possibilité de revenir en arrière en cas d'erreurs. Plus de détails dans **documentation**.

<br>

## Version 0.10.x

> **Fonctionnalités ajoutées**

- Un nouveau pas de flux de données “Obtenir des informations sur le fichier” a été créé, vous permettant d'obtenir des informations sur un fichier par son identifiant. Plus de détails dans la documentation : **Obtenir des informations sur le fichier**
- Ajout d'un filtre pour le champ “Composant” à l'intérieur du pas de flux de données “Obtenir l'entité par id”. Plus de détails ici : **Obtenir l'entité par id**  
  <br>

> **Mise à jour du design**

- Page principale “Tableau de bord”. Plus de détails ici : **Tableau de bord**
- Le “menu de navigation” a été supprimé du menu “Applications” et se trouve désormais sur la page principale. Plus de détails ici : **Menu de navigation**
- Le design des pas de flux de données a été mis à jour. Plus de détails ici : **Pas de flux de données disponibles**
- Le design du “stockage de fichiers” a été mis à jour. Plus de détails ici : **Stockage de fichiers**
- Le design de la “maintenance du système” a été mis à jour. Plus de détails ici : **Maintenance du système**
  <br>

## Version 0.9.x

> **Fonctionnalités ajoutées**

- Fonctionnalités spécifiques au système (spécifiques à la plateforme)
  - Téléchargement de l'interface utilisateur : optimisation de la compilation des composants UI.
  - Refactoring du **menu de maintenance**. Déplacement des boutons de contrôle vers l'onglet “Maintenance du système”, et affichage des journaux avec leurs paramètres dans l'onglet “Journaux système”.
  - Générateur de stockage de file d'attente de travail dans Redis.
  - IronPython a été mis à jour de la version 2.7.12 à 3.4.1 sur le lieu de travail.
- Fonctionnalités spécifiques à l'utilisateur (spécifiques au studio) - Copier/coller des éléments dans le **constructeur d'interface** sur la page du composant. - Ajout de fichiers à la racine du [stockage de fichiers](user-interface/file-storage.md). - Capacité d'utiliser le modèle de données des composants de référence (Catalogue) dans la barre d'outils des éléments de composant pour : `DataGrid`, `ListView`, `TreeView`.
  <br>

> **Modifications de l'interface**

- Refactoring du menu principal du studio :
  - déplacement des éléments suivants dans le coin supérieur droit de la barre de ruban : interrupteur de localisation et bouton pour se déconnecter du compte actuel (déconnexion),
  - l'élément Profil du menu principal a été supprimé.
- L'icône de l'élément de menu Modules Python a été redessinée.
- Des icônes d'aide en ligne ont été ajoutées dans de nombreuses sections du Studio : pas de flux de données, boutons pour éléments d'interface utilisateur (Toolbox UI), paramètres principaux de l'application, ainsi que dans de nombreux autres emplacements dans le studio pour garantir un accès plus rapide à l'aide en ligne sur le site de documentation.  
  <br>

> **Corrections de bogues clés**

- Correction du fonctionnement du planificateur de tâches `Cron` lors de l'import/export de composants.
- Élimination du duplicata `changeAuthor` du modèle de données du composant.
- Stabilisation de la sélection des étapes de flux de travail.
- Correction de l'élément UI `Number` du panneau des éléments de composant.
- Correction du fonctionnement de l'événement On focus pour certains éléments UI : Jour, Heure, Signature.
  <br>

## Version 0.8.x

> **Fonctionnalités importantes et améliorées ajoutées**

- Dans l'étape Action de formulaire du flux de données, les paramètres Ouvrir la barre latérale et Ouvrir la fenêtre modale ont été ajoutés, ce qui vous permet d'ouvrir respectivement une barre latérale et une fenêtre modale, de la même manière que cela peut être fait via un script Python.
- Transfert des attributs requis pour les paramètres transférés dans l'étape Obtenir le modèle d'action.
- L'étape de flux de données “Supprimer les rôles assignés à l'utilisateur” a été ajoutée, ce qui supprime tous les rôles actuels assignés à l'utilisateur, vous permettant de créer un nouvel ensemble de rôles à partir de zéro.
- Le menu **Modules Python** a été ajouté pour gérer la bibliothèque partagée des modules Python.
- Le paramètre d'arrière-plan pour les contrôles UI a été ajouté, ce qui vous permet de définir une image dans des formats standard (par exemple, png, svg, jpeg, etc.) comme arrière-plan pour tous les contrôles qui ont une section de paramètres de pinceau.
- L'icône de vue du modèle de données sur l'étape de flux de données a été changée en icône d'œil.
- Le paramètre “Ignorer de la synchronisation” a été remplacé par Propriété virtuelle. Les champs marqués “Propriété virtuelle” ne sont pas enregistrés dans la base de données lorsque le composant est enregistré.
- Des paramètres supplémentaires pour l'application Web Power (PWA) dans la section Modifier le manifeste ont été ajoutés.
- Des paramètres supplémentaires pour le domaine d'application ont été ajoutés - afficher les fil d'Ariane, connexion, locale.
  <br>

> **Erreurs importantes corrigées**

- Le fonctionnement des filtres dynamiques pour le contrôle de la grille de données a été corrigé.
- Le champ “Première ligne à ignorer” dans l'étape Importer un fichier n'est pas réinitialisé à 0 après l'enregistrement.
- La couleur par défaut pour le domaine d'application s'applique aux contrôles de type bouton qui n'ont pas de couleur par défaut définie.
- Les autorisations pour un composant multiple ne sont pas définies en mode d'accès restreint.
  <br>

## Version 0.7.0

> **Fonctionnalités importantes et améliorées ajoutées**

- Lors de la sélection d'un composant par défaut pour un domaine d'application dans la section Paramètres principaux, vous pouvez sélectionner la page qui sera ouverte pour ce composant dans le champ Page par défaut. Si aucune page n'est sélectionnée, la première page du composant (page principale) sera ouverte par défaut.
- Un nouveau pas “Exécuter le flux de données” a été ajouté au flux de données, ce qui vous permet de lancer de nouveaux flux de données, y compris des flux de données d'autres composants, au sein du flux de données actuel.
- L'ancien pas de flux de données “Obtenir l'audience” a été supprimé, et le pas “Action de formulaire” a été déplacé dans le groupe “Transformation de modèle”. Le groupe “Autre” a été complètement supprimé.
- La recherche pour configurer le “Mapping de champ” a été ajoutée pour le pas “Appliquer les opérations de mise à jour différées”.
- Pour le contrôle UI **Zone de texte**, une option de redimensionnement automatique a été ajoutée, ce qui vous permet d'agrandir la taille du champ si vous devez entrer une plus grande quantité de texte.
- Le pas de flux de données “Interroger l'entité par filtre” a été optimisé via la création automatique d'index et la normalisation de la base de données.
- Un avis d'expiration imminente de la licence a été ajouté. Le message apparaît 10 jours avant la date d'expiration de la licence actuelle.
- Les API Swagger générées pour le flux de données affichent désormais le nom du flux de données comme nom de l'API.
- La possibilité de demander la géolocalisation de l'utilisateur à partir du script de composant via la fonction context.PlatformServices.GeolocationPosition a été ajoutée.
- La possibilité de définir le paramètre de locale par défaut pour le domaine d'application a été ajoutée dans la section Paramètres principaux.
- La possibilité de définir un favicon pour le domaine d'application a été ajoutée dans les paramètres du menu d'accueil : Domaine : Paramètres principaux.
  <br>

> **Erreurs importantes corrigées**

- Le fonctionnement des filtres dynamiques pour le contrôle de la grille de données a été corrigé.
- Un problème où une erreur se produisait lors du tri des champs récupérés à partir de liens de type Catalogue a été corrigé.
- La stabilité de la grille de données, y compris les erreurs fantômes lors de la navigation dans la grille de données, a été améliorée.
- Un problème avec le formulaire de recherche étant coupé dans la grille de données lors du clic sur un filtre a été corrigé.
- La sortie des valeurs de chaîne pour Enum a été ajoutée.
- Mauvais fonctionnement du système avec la déconnexion à distance a été corrigé.
- Mauvais fonctionnement du minuteur dans l'étape “Appliquer les opérations de mise à jour différées” a été corrigé.
- Pour les contrôles UI de type Étiquette, liés à un champ de type Catalogue, le paramètre Couleur est désormais traité correctement.
  <br>

## Version 0.6.x

> **Fonctionnalités importantes et améliorées ajoutées**

- Fonctionnalités avancées pour gérer le menu principal de l'application - construction de menus hiérarchiques et définition d'icônes de menu.
- Amélioration du travail avec les scripts Python - mise en surbrillance de la syntaxe Python, auto-complétion pour les méthodes système Python, ainsi que l'auto-complétion et les conseils pour les méthodes des bibliothèques intégrées de la plateforme ont été ajoutés (disponibles via Ctrl-Espace sous Win10/11, et Option-Espace sous MacOS).
- La possibilité de construire des fenêtres latérales supplémentaires via le script de composant a été ajoutée.
- La possibilité de construire des fenêtres modales complexes via le script de composant avec transfert de données des fenêtres modales vers le script appelant a été ajoutée.
- L'appel du script de composant a été déplacé vers le menu principal.
- La localisation du studio en russe a été complétée.
- Dans le contrôle DataGrid, il est désormais possible de sélectionner des champs arbitraires d'un composant externe lors de l'affichage des champs de référence de type Catalogue.
- L'import-export inclut désormais l'exportation et l'importation ultérieure des autorisations et des rôles (l'exportation de fichiers créés avec la version 0.6.x vers des versions précédentes fonctionnera, mais n'importera pas les rôles et autorisations inclus).
- L'import-export vérifie désormais les composants liés et avertit l'utilisateur si des composants liés n'ont pas été inclus dans la liste d'exportation.
- Au niveau de la plateforme, la possibilité de marquer des entrées (instances de composant) comme disponibles pour suppression physique a été ajoutée via un drapeau dans l'étape de flux de données “Mettre à jour l'entrée”.
- La possibilité pour l'administrateur du studio d'obtenir une liste d'entrées marquées pour suppression et de supprimer celles qui n'ont pas de liens vers des entrées qui ne sont pas marquées prêtes pour suppression a été ajoutée.
  <br>

## Version 0.5.24

> **Fonctionnalités importantes et améliorées ajoutées**

- Capacités avancées pour des filtres dynamiques et statiques dans des contrôles avancés tels que la Grille de données, la Vue de liste, la Vue en arbre, permettant un filtrage à la volée des données avant affichage à l'utilisateur (des paramètres ont été ajoutés pour les filtres de type contient, etc.).
- Élargissement du concept d'utilisation de Flux de données & Flux de travail - maintenant les deux peuvent être créés et utilisés séparément des contrôles UI tels que des boutons, ce qui permet une structure d'application plus flexible et simplifie le développement.
- De nombreuses nouvelles méthodes disponibles via [Utiliser Python](app-development/using-python.md) dans le script de composant ont été ajoutées, telles que l'appel de fenêtres modales, la vérification de la résolution d'écran et du type d'appareil pour créer une mise en page UI réactive.
- La possibilité de travailler avec des systèmes de files d'attente de messages (par exemple, RabbitMQ) depuis le flux de données avec un nouveau pas [S'abonner au connecteur](app-development/data-flow-components/subscribe-to-connector.md) a été ajoutée.
- La possibilité de traitement par lots des données dans le flux de données via de nouveaux pas [Mise à jour différée de l'entrée](app-development/data-flow-components/deferred-update-entry.md) & [Appliquer les opérations de mise à jour différées](app-development/data-flow-components/apply-deferred-update-operations.md) a été ajoutée.
  <br>

## Version 0.4.4

> **Fonctionnalités importantes et améliorées ajoutées**

- Un nouveau champ de stockage système “Nom” a été ajouté, utilisé pour afficher des éléments des Catalogues.
  - Lors de l'affichage d'un seul élément du Catalogue (par exemple, en utilisant un contrôle UI Sélection qui fait référence au Catalogue), le contenu du champ Nom sera désormais toujours affiché. Si le champ Nom est vide, le nom du Catalogue système/numéro de séquence de l'entrée du Catalogue sera affiché.
- Des paramètres de tri par défaut pour la Grille de données et la Vue de liste ont été ajoutés.
- Un remplacement automatique des caractères spéciaux Unicode dans le script de composant pour la génération de liens a été ajouté.
  <br>

> **Erreurs corrigées**

- Mauvais fonctionnement du paginator concernant le changement de plusieurs tables sur une page a été corrigé.
- Fonction de défilement non fonctionnelle dans certaines parties du Studio a été corrigée.
  <br>

## Version 0.3.223

_Cluster Kubernetes 0.3.223 | Mini-image Docker 0.2.118_

> **Fonctionnalités importantes et améliorées ajoutées**

- Un nouveau pas de flux de données “Envoyer une notification avec modèle” a été ajouté, ce qui vous permet d'envoyer une notification par e-mail en utilisant un modèle spécifié.
- Propriété de transparence pour les composants UI.
- Support pour l'autorisation OAuth2 pour les requêtes HTTP a été ajouté. Vous pouvez désormais configurer la génération automatique de jetons via OAuth pour vous connecter à l'API.
- Le paramètre “Stocker la réponse en tant que fichier” a été ajouté dans le pas “Exécuter l'appel API” pour vous permettre de télécharger un fichier via l'API sur demande.
- Les étapes ne génèrent plus de newsletter, elles génèrent désormais un champ dans le modèle pour une utilisation ultérieure, tel que “Envoyer une notification avec modèle”.
  <br>

> **Erreurs corrigées**

- Erreurs lors du travail avec le type DateTime dans le calendrier ont été corrigées.
- UI dans le Studio et le Lieu de travail a été corrigée.
- L'état Désactivé pour le composant UI RadioButton a été corrigé.
- Erreurs de localisation ont été corrigées.
- La recherche dans le Dropdown est désormais insensible à la casse.
- Problèmes d'opération d'autorisation, y compris des problèmes de déconnexion, ont été corrigés. <br>