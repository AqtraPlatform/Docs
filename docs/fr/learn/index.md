# Introduction

> Un point d'entrée structuré pour les nouveaux utilisateurs d'Aqtra. Ton technique. Cette page relie la documentation, les tutoriels, les vidéos (avec transcriptions) et un exemple exécutable pour former une feuille de route d'apprentissage progressive.

---

## Qu'est-ce qu'Aqtra ?

Aqtra est une **plateforme low-code** pour la création d'applications métier principalement via une interface utilisateur visuelle, avec un **scripting Python** optionnel pour une logique avancée. Ce modèle hybride accélère la livraison pour les débutants et permet aux développeurs d'étendre et de personnaliser si nécessaire.

**Vous apprendrez à :**

- Installer et exécuter Aqtra (cloud ou local via Docker).
- Construire une première fonctionnalité de bout en bout (modèle de données → composant UI → flux de données → publication).
- Utiliser des scripts Python lorsque cela est approprié.
- Intégrer des services externes et des API.

> **Public cible :** développeurs citoyens, développeurs front‑/back‑end juniors, analystes, architectes, chefs d'équipe.

**Appels à l'action principaux :**

- **Commencer en 60 minutes →** Guide de la première fonctionnalité (voir [4) Première victoire](#4-first-win-in-60-minutes))
- **Documentation →** [https://docs.aqtra.io/](https://docs.aqtra.io/fr/)
- **Piste vidéo →** [https://www.youtube.com/@Aqtra.Academy](https://www.youtube.com/@Aqtra.Academy)

**Liens rapides (cartes) :**

- **Installer** → [5) Installer & Accéder](#5-install--access) (Cloud / Docker)
- **Construire votre premier écran (Facture)** → [4) Première victoire](#4-first-win-in-60-minutes)
- **Notions de base sur DataFlow** → [2) Chemin d'apprentissage étape par étape](#2-stepbystep-learning-path-single-track)
- **Publier sur le web** → [2) Chemin d'apprentissage étape par étape](#2-stepbystep-learning-path-single-track)

**Sur cette page**

- [1) Méthodologie — comment utiliser ce guide](#1-methodology--how-to-use-this-guide)
- [2) Chemin d'apprentissage étape par étape](#2-stepbystep-learning-path-single-track)
- [3) Liens croisés vers les tutoriels et la documentation](#tutorials-documentation-cross-links)
- [4) Première victoire en ~60 minutes](#4-first-win-in-60-minutes)
- [5) Installer & Accéder](#5-install--access)
- [6) Concepts de base (Glossaire Aqtra)](#6-core-concepts-aqtra-glossary)
- [7) Piste vidéo](#7-video-track-with-transcripts--timecodes)
- [8) Bibliothèque d'étapes DataFlow](#8-dataflow-step-library-quick-reference)
- [9) FAQ](#9-faq-short-practical)

---

## 1) Méthodologie — comment utiliser ce guide {: #1-methodology--how-to-use-this-guide }

- **Progression à voie unique** : un chemin unifié pour tous les rôles, concepts nouveaux minimaux par étape.
- **Liens de première mention** : chaque concept/élément UI est lié une fois à sa première apparition ; les étapes suivantes supposent cela.
- **Profondeur juste à temps** : chaque étape fait référence à des documents ciblés et à une courte vidéo avec des horodatages cliquables.
- **Résultats visibles** : chaque étape se termine par un résultat concret et testable dans Workplace.
- **Mentalité axée sur les erreurs** : l'étape 10 enseigne le débogage systématique/l'analyse des journaux.
- **Évaluation** : le **Capstone** (Étape 11) valide CRUD, intégration, modélisation, navigation et rôles/permissions.

### Portée & prérequis

- Accès à **Aqtra Studio/Workplace** (locataire cloud) _ou_ une configuration **Docker** locale (≥ 4 vCPU / 8 Go de RAM).
- Navigateur moderne et capacité à afficher l'onglet **Réseau** des outils de développement.
- (Optionnel) Familiarité de base avec JSON et les API HTTP pour l'étape 6.

### Résultats d'apprentissage (par étape)

- **Étape 1** : vous pouvez accéder à Studio/Workplace.
- **Étape 2** : vous pouvez modéliser une entité (Facture) et la rendre visible dans un Composant dans Workplace.
- **Étape 3** : vous pouvez construire un DataFlow et le lier à un Bouton.
- **Étape 4** : vous pouvez compléter CRUD et validation de base.
- **Étape 5** : vous pouvez ajouter une logique Python dans un flux.
- **Étape 6** : vous pouvez appeler une API HTTP externe et mapper les résultats.
- **Étape 7** : vous pouvez composer une page MultiComponent avec un contexte de données.
- **Étape 8** : vous pouvez naviguer entre les pages avec des paramètres d'action.
- **Étape 9** : vous pouvez rendre et télécharger un document à partir d'un modèle.
- **Étape 10** : vous pouvez diagnostiquer des erreurs en utilisant des journaux/outils de développement et republier.
- **Étape 11** : vous pouvez livrer une petite fonctionnalité avec des rôles/permissions et une intégration.

### Boucle de rétroaction

- Après **Première victoire** et **Capstone**, capturez les retours : ce qui était flou, où des erreurs sont apparues, et quels liens/vidéos ont été les plus utiles ; intégrez cela dans la documentation.

### Grille d'évaluation (Capstone)

- [ ] CRUD fonctionne avec validation et messages utilisateur clairs.
- [ ] Appel API externe mappé ; échecs gérés (timeouts/4xx/5xx).
- [ ] Modèle de document rendu ; fichier téléchargeable.
- [ ] La navigation via des paramètres d'action ouvre le bon enregistrement/page.
- [ ] Au moins **2 rôles** configurés avec des accès différents.
- [ ] Tous les composants **Publiés** sans avertissements bloquants.

---

## 2) Chemin d'apprentissage étape par étape (voie unique)

Un chemin unifié pour tous les rôles. Suivez les étapes dans l'ordre ; chaque étape renvoie à des documents et (optionnellement) à une courte vidéo.

**Étape 1 — Accéder à Aqtra (cloud ou Docker)**
Obtenez une instance en cours d'exécution (voir Section 4). Vérifiez que vous pouvez ouvrir **Studio** et **Workplace**.

**Étape 2 — Premier squelette d'application**
Créez un **DataModel** minimal (par exemple, `Invoice(number, title, totalAmount, dueDate)`) et un **Composant** pour l'afficher/modifier. Publiez et ajoutez à la navigation pour qu'il apparaisse dans Workplace.

**Docs** : Composant → [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/fr/app-development/component.html) ; Catalogue UI → [https://docs.aqtra.io/app-development/ui-components/index.html](https://docs.aqtra.io/fr/app-development/ui-components/index.html)
**Vidéo** : Tutoriel #1 → [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ) ; Tutoriel #2 → [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)

**Étape 3 — Notions de base sur DataFlow**
Ajoutez un **DataFlow** avec des étapes : `Get Action Model → Update Entry → Write Response`. Liez-le à un **Bouton** et testez la création/mise à jour.

**Docs** : Vue d'ensemble de Dataflow → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/fr/app-development/data-flow-components/index.html) ; Mettre à jour l'entrée → [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/fr/app-development/data-flow-components/update-entry.html) ; Exécuter le dataflow → [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-dataflow.html)
**Vidéo** : Tutoriel #3 — ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))

**Étape 4 — Achèvement de CRUD**
Ajoutez des vues liste/détail, terminez les flux de création/mise à jour/suppression et les validations.

**Docs** : Grille de données → [https://docs.aqtra.io/app-development/ui-components/data-grid.html](https://docs.aqtra.io/fr/app-development/ui-components/data-grid.html)
**Vidéo** : Tutoriel #4 — supprimer via Mettre à jour l'entrée ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)); Tutoriel #5 — filtres dynamiques ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180))

**Étape 5 — Scripting Python pour la logique métier**
Insérez une étape **Script Python** pour calculer des champs dérivés et valider les entrées.

**Docs** : Exécuter le script → [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-script.html)
**Vidéo** : Tutoriel #6 — Exécuter le script ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370))

**Étape 6 — Intégrations externes**
Appelez une API HTTP externe depuis un script Python ; mappez la réponse à votre DataModel.

**Docs** : Exécuter l'appel API → [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-api-call.html)
**Vidéo** : (Optionnel) Tutoriel #10 — diagnostiquer les incompatibilités de charge/type ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! astuce "Dépannage"
_ **Timeout/5xx** : vérifiez l'URL/méthode/headers ; ajoutez une nouvelle tentative/un temps d'attente ; enregistrez le corps de la réponse.
_ **401/403** : fournissez/rafraîchissez le jeton d'authentification (stockez les secrets en toute sécurité).
_ **406/422 (incompatibilité de type)** : corrigez le mappage des champs et les types ; transformez dans **Exécuter le script** (par exemple, chaîne → nombre/date) avant `Update Entry`.
_ Utilisez `context.Logger` pour enregistrer les ID de corrélation et les extraits de charge utile.

**Étape 7 — Pages MultiComponent**
Composez une page à partir de plusieurs composants (filtres + grille + formulaire). Configurez le **contexte de données** et le câblage.

**Docs** : Vue liste → [https://docs.aqtra.io/app-development/ui-components/list-view.html](https://docs.aqtra.io/fr/app-development/ui-components/list-view.html) ; Contrôle d'onglets → [https://docs.aqtra.io/app-development/ui-components/tab-control.html](https://docs.aqtra.io/fr/app-development/ui-components/tab-control.html) ; Graphiques → [https://docs.aqtra.io/app-development/ui-components/charts.html](https://docs.aqtra.io/fr/app-development/ui-components/charts.html)
**Vidéo** : Tutoriel #6 — boîte de dialogue modale + grille de rafraîchissement automatique ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)); Tutoriel #7 — Vue liste ([00:59](https://youtu.be/PtAJwn07sWI?t=59)–[03:00](https://youtu.be/PtAJwn07sWI?t=180))

> **Astuce de conception (optionnelle)** : regroupez les entrées connexes en panneaux, maintenez un rythme vertical cohérent (multiples de 8 à 12 px), évitez d'utiliser excessivement des graphiques—ajoutez-les uniquement lorsqu'ils clarifient les tendances.

**Étape 8 — Navigation & câblage inter-pages**
Ajoutez des éléments de menu et ouvrez des pages avec des **paramètres d'action** (transmettez l'enregistrement `id` de la grille au formulaire).

**Docs** : Actions de bouton → [https://docs.aqtra.io/app-development/ui-components/button.html](https://docs.aqtra.io/fr/app-development/ui-components/button.html)
**Vidéo** : Tutoriel #12 — ouvrir la page + mappage des paramètres ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)); Tutoriel #5 — Ouvrir l'application depuis la grille ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))

**Étape 9 — Modèles & génération de documents (PDF)**
Rendez et téléchargez un document à partir d'un modèle via DataFlow.

**Docs** : Composants Dataflow (Rendre le modèle) → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/fr/app-development/data-flow-components/index.html)
**Vidéo** : Tutoriel #12 — rendu de modèle + téléchargement ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165) ; [05:20](https://youtu.be/k36-qpZa9bU?t=320)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

**Étape 10 — Gestion des erreurs & débogage**
Utilisez l'onglet Réseau et les journaux de Studio pour diagnostiquer les 4xx/5xx ; corrigez les types ; republiez.

**Docs** : Publication d'applications → [https://docs.aqtra.io/app-development/publishing-applications.html](https://docs.aqtra.io/fr/app-development/publishing-applications.html)
**Vidéo** : Tutoriel #10 — trouver et corriger les erreurs ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))

!!! astuce "Dépannage"

- Suivez la séquence : **Compiler → Enregistrer → Prêt à publier → Publier** ; vérifiez que le composant est répertorié comme _Publiée_.
- Utilisez les outils de développement du navigateur **Réseau** pour comparer la demande/réponse au schéma attendu ; corrigez le mappage/types.
  _ Si le comportement diffère entre les pages, vérifiez que **tous les composants dépendants** ont été republiés ensemble.
  _ Sur les configurations Docker, inspectez les journaux des conteneurs pour les traces de pile et les conflits de ports.

**Étape 11 — Capstone**
Étendez votre application en une petite fonctionnalité (par exemple, Mini-CRM) : rôles/permissions, tableau de bord MultiComponent, une intégration, un modèle de document. Documentez les critères d'acceptation et réalisez une courte vidéo de démonstration.

[Retour en haut](#getting-started)

---

## 3) Liens croisés vers les tutoriels et la documentation {: #tutorials-documentation-cross-links }

**Installer / Plateforme**

- Paramètres de base, authentification, journaux, métriques → [https://docs.aqtra.io/install1/basic-settings.html](https://docs.aqtra.io/fr/install1/basic-settings.html)

**Construction de base**

- Composant (création, paramètres de base) → [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/fr/app-development/component.html)
- Catalogue des composants UI (première mention) → [https://docs.aqtra.io/app-development/ui-components/index.html](https://docs.aqtra.io/fr/app-development/ui-components/index.html)
- Grille de données (première mention) → [https://docs.aqtra.io/app-development/ui-components/data-grid.html](https://docs.aqtra.io/fr/app-development/ui-components/data-grid.html)
- Vue liste / Contrôle d'onglets / Graphiques (première mention) → [https://docs.aqtra.io/app-development/ui-components/list-view.html](https://docs.aqtra.io/fr/app-development/ui-components/list-view.html), [https://docs.aqtra.io/app-development/ui-components/tab-control.html](https://docs.aqtra.io/fr/app-development/ui-components/tab-control.html), [https://docs.aqtra.io/app-development/ui-components/charts.html](https://docs.aqtra.io/fr/app-development/ui-components/charts.html)

**Flux / Logique**

- Vue d'ensemble de Dataflow → [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/fr/app-development/data-flow-components/index.html)
- Mettre à jour l'entrée (CRUD) → [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/fr/app-development/data-flow-components/update-entry.html)
- Exécuter le dataflow → [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-dataflow.html)
- Exécuter le script (Python) → [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-script.html)
- Exécuter l'appel API → [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-api-call.html)

**Publication**

- Publication d'applications → [https://docs.aqtra.io/app-development/publishing-applications.html](https://docs.aqtra.io/fr/app-development/publishing-applications.html)

**Tutoriels (docs)**

- Tutoriel #1 → [https://docs.aqtra.io/tutorials/tutorial1.html](https://docs.aqtra.io/fr/tutorials/tutorial1.html)
- Tutoriel #2 → [https://docs.aqtra.io/tutorials/tutorial2.html](https://docs.aqtra.io/fr/tutorials/tutorial2.html)
- Tutoriel #3 → [https://docs.aqtra.io/tutorials/tutorial3.html](https://docs.aqtra.io/fr/tutorials/tutorial3.html)

**Index vidéo (horodatages cliquables)**

- T#3 — Notions de base sur DataFlow ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450)).
- T#4 — Supprimer via Mettre à jour l'entrée ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380)).
- T#5 — Filtres de la grille de données ; Ouvrir l'application ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680)).
- T#6 — Exécuter le script ; boîte de dialogue modale ; grille de rafraîchissement automatique ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020)).
- T#10 — Déboguer 500→406 ; corriger les types ; republier ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300)).
- T#12 — Rendre le modèle ; Télécharger ; Ouvrir la page + mappage ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420)).

---

## 4) Première victoire en ~60 minutes

> Construisez la mini-fonctionnalité **Inventaire de Factures** de bout en bout.

1. **Accédez à Aqtra** (cloud ou Docker) et ouvrez **Studio**.
2. **Créez le DataModel** `Invoice(number, title, totalAmount, dueDate)`.
3. **Ajoutez un Composant** pour créer/lister des factures (première utilisation de la Grille de données).
4. **Câblez un DataFlow** — `Get Action Model → Update Entry → Write Response` (exécution optionnelle du **Script** pour valider totalAmount).
5. **Publiez** et vérifiez dans **Workplace** : créez deux factures, modifiez-en une.

**Docs** : Tutoriels → Construisez votre première application — [https://docs.aqtra.io/tutorials/index.html](https://docs.aqtra.io/fr/tutorials/index.html)

---

## 5) Installer & Accéder {: #5-install--access }

Choisissez l'une des options suivantes. Gardez les identifiants et les clés de licence en sécurité.

### Option 1 — Cloud (Hébergé)

- Obtenez l'accès via un partenaire d'hébergement ou achetez directement.
- Tarification & acquisition : [https://aqtra.io/#price](https://aqtra.io/#price).
- Recevez une URL d'organisation/locataire et des identifiants.
- Configurez SSO (optionnel), utilisateurs et rôles.

### Option 2 — Local (Docker)

**Prérequis** : Docker Engine/Compose à jour ; hôte Linux/Windows/macOS avec **4 vCPU / 8 Go de RAM** minimum.

**Liste de contrôle**

- [ ] Installez Docker/Compose et vérifiez que `docker ps` fonctionne.
- [ ] Préparez `docker-compose.yml` et `.env` avec les secrets requis.
- [ ] Démarrez la DB → `docker compose up -d db` et attendez qu'elle soit prête.
- [ ] Démarrez l'application → `docker compose up -d app`.
- [ ] Accédez à **Workplace** à `http://<host>:8080/` et à **Studio** à `http://<host>:8080/studio/`.

**Docs** : Paramètres de base (architecture, ports, authentification, journaux, métriques) → [https://docs.aqtra.io/install1/basic-settings.html](https://docs.aqtra.io/fr/install1/basic-settings.html)

[Retour en haut](#getting-started)

---

## 6) Concepts de base (Glossaire Aqtra)

Définitions courtes et exploitables.

- **Composant** — un bloc de construction UI qui rend des données et des actions pour les utilisateurs (formulaire, liste, détail, etc.). [https://docs.aqtra.io/app-development/component.html](https://docs.aqtra.io/fr/app-development/component.html)
- **DataFlow** — un flux d'opérations dirigé (par exemple, valider → transformer → persister → notifier) qui s'exécute sur des événements utilisateur ou système. Étapes typiques : **Obtenir le modèle d'action**, **Mettre à jour l'entrée**, **Écrire la réponse**, **Exécuter le script**, **Exécuter l'appel API**. [https://docs.aqtra.io/app-development/data-flow-components/index.html](https://docs.aqtra.io/fr/app-development/data-flow-components/index.html)
- **DataModel** — la définition structurée des entités/attributs que l'application persiste et manipule.
- **MultiComponent** — une vue composite assemblant plusieurs Composants (par exemple, liste + détails + filtres) en une page cohérente ; les éléments utilisent le **contexte de données** pour se lier à un composant source.
- **Script Python** — étape de logique personnalisée intégrée dans un flux pour transformer des données, appeler des services ou mettre en œuvre des règles. [https://docs.aqtra.io/app-development/data-flow-components/execute-script.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-script.html)

---

## 7) Piste vidéo (avec transcriptions & horodatages) {: #7-video-track-with-transcripts--timecodes }

Liste vidéo centralisée avec des liens profonds et des horodatages. Utilisez-les pour sauter directement aux moments de démonstration pertinents.

- **Tutoriel #1** — [https://youtu.be/GaUr5ET4dfQ](https://youtu.be/GaUr5ET4dfQ)
- **Tutoriel #2** — [https://youtu.be/UEG2pmct74s](https://youtu.be/UEG2pmct74s)
- **Tutoriel #3** — Notions de base sur DataFlow ([05:16](https://youtu.be/UEG2pmct74s?t=316)–[07:30](https://youtu.be/UEG2pmct74s?t=450))
- **Tutoriel #4** — Supprimer via Mettre à jour l'entrée ([05:18](https://youtu.be/oLoYMSAlLVo?t=318)–[06:20](https://youtu.be/oLoYMSAlLVo?t=380))
- **Tutoriel #5** — Filtres de la grille de données ; Ouvrir l'application ([00:13](https://youtu.be/YuU_YomoNaw?t=13)–[03:00](https://youtu.be/YuU_YomoNaw?t=180)), ([10:53](https://youtu.be/YuU_YomoNaw?t=653)–[11:20](https://youtu.be/YuU_YomoNaw?t=680))
- **Tutoriel #6** — Exécuter le script ; boîte de dialogue modale ; grille de rafraîchissement automatique ([04:10](https://youtu.be/bOR2nOk_S0c?t=250)–[06:10](https://youtu.be/bOR2nOk_S0c?t=370)), ([10:45](https://youtu.be/bOR2nOk_S0c?t=645)–[17:00](https://youtu.be/bOR2nOk_S0c?t=1020))
- **Tutoriel #7** — [https://youtu.be/PtAJwn07sWI](https://youtu.be/PtAJwn07sWI)
- **Tutoriel #8** — [https://youtu.be/YfqfdJpDm-k](https://youtu.be/YfqfdJpDm-k)
- **Tutoriel #9/10** — Débogage & diagnostics ([01:46](https://youtu.be/qJcpIQQEqbo?t=106)–[05:00](https://youtu.be/qJcpIQQEqbo?t=300))
- **Tutoriel #11** — [https://youtu.be/d-FD1ARn0h0](https://youtu.be/d-FD1ARn0h0)
- **Tutoriel #12** — Rendre le modèle ; Télécharger ; Ouvrir la page + mappage ([01:37](https://youtu.be/k36-qpZa9bU?t=97)–[02:45](https://youtu.be/k36-qpZa9bU?t=165)), ([06:18](https://youtu.be/k36-qpZa9bU?t=378)–[07:00](https://youtu.be/k36-qpZa9bU?t=420))

!!! note "Restez à jour"
Abonnez-vous à **Aqtra Academy** sur YouTube et vérifiez régulièrement la racine de la documentation pour des mises à jour. De nouveaux épisodes seront liés ici à leur arrivée.

[Retour en haut](#getting-started)

---

## 8) Bibliothèque d'étapes DataFlow (référence rapide)

Quelques étapes utiles que vous utiliserez probablement au-delà de CRUD :

- **Mettre à jour l'entrée** — [https://docs.aqtra.io/app-development/data-flow-components/update-entry.html](https://docs.aqtra.io/fr/app-development/data-flow-components/update-entry.html)
- **Exécuter le dataflow** — appeler un autre dataflow et fusionner les résultats.
  [https://docs.aqtra.io/app-development/data-flow-components/execute-dataflow.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-dataflow.html)
- **Exécuter l'appel API** — configurer et exécuter une requête HTTP, lier les résultats.
  [https://docs.aqtra.io/app-development/data-flow-components/execute-api-call.html](https://docs.aqtra.io/fr/app-development/data-flow-components/execute-api-call.html)
- **Obtenir l'entité par id** — récupérer l'entité par identifiant via le champ catalogue.
  [https://docs.aqtra.io/app-development/data-flow-components/get-entity-by-id.html](https://docs.aqtra.io/fr/app-development/data-flow-components/get-entity-by-id.html)
- **Mettre à jour le champ du modèle** — définir/dériver un champ unique au sein du modèle.
  [https://docs.aqtra.io/workflow-components/update-model-field.html](https://docs.aqtra.io/fr/workflow-components/update-model-field.html)
- **Mathématiques simples** — additionner/soustraire/multiplier et écrire dans un champ cible.
  [https://docs.aqtra.io/app-development/data-flow-components/simple-math.html](https://docs.aqtra.io/fr/app-development/data-flow-components/simple-math.html)
- **Stocker l'entrée sur le bus** — créer/stocker une instance de composant de manière asynchrone.
  [https://docs.aqtra.io/app-development/data-flow-components/store-entry-over-bus.html](https://docs.aqtra.io/fr/app-development/data-flow-components/store-entry-over-bus.html)
- **S'abonner au connecteur** — par exemple, abonnement RabbitMQ → traitement → sauvegarde.
  [https://docs.aqtra.io/app-development/data-flow-components/subscribe-to-connector.html](https://docs.aqtra.io/fr/app-development/data-flow-components/subscribe-to-connector.html)

[Retour en haut](#getting-started)

---

## 9) FAQ (courte, pratique)

**Q : Cloud vs local ?**
R : Cloud pour un onboarding rapide/accès en équipe ; Docker local pour hors ligne/PoCs/environnements restreints.

**Q : Docker ne démarre pas ou est lent.**
R : Assurez-vous d'avoir 4 vCPU/8 Go de RAM+, libérez les ports cibles et vérifiez les journaux des conteneurs. Redémarrez Docker et réessayez de composer.

**Q : Où mettre la logique personnalisée ?**
R : Ajoutez une étape **Script Python** à l'intérieur d'un **DataFlow** pour valider, transformer ou appeler des API externes.

**Q : Comment appeler des services externes ?**
R : Utilisez `http.client` depuis un script Python ; mappez la réponse à votre DataModel.

**Q : Principaux blocs de construction ?**
R : **DataModel**, **Composant**, **DataFlow**, **MultiComponent**, **Script Python**.

**Q : Erreurs et exceptions ?**
R : Utilisez l'inspecteur de réseau et les journaux de Studio ; corrigez les incompatibilités de type, republiez et retestez. Voir la vidéo dans la Section 8.

**Q : Comment acheter ou obtenir un essai ?**
R : Voir la tarification : [https://aqtra.io/#price](https://aqtra.io/#price). Achetez via un fournisseur ou directement ; pour les déploiements hébergés, suivez l'intégration des partenaires.

---

## 10) Quelles sont les prochaines étapes

- Modèles et meilleures pratiques (naming, versioning, testing flows).
- Intégrations avancées (SSO, bases de données, files d'attente de messages).
- Flux de travail d'équipe (revues de code pour les scripts, promotion d'environnement).
- Liens vers la communauté et le support (Slack/Telegram/Forum) — _ajouter lorsque disponible_.