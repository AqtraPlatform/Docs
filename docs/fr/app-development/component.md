# Composant

Les composants sont les éléments clés de la plateforme, fournissant la base pour la création d'applications. Ce sont des unités encapsulées de fonctionnalité qui peuvent inclure des données, une interface utilisateur, une logique métier et une automatisation des processus.

## Types de Composants

1. **Composant Unique** :

   - Contient le modèle d'objet de base pour le stockage des données.
   - Inclut un modèle d'interface utilisateur avec des formulaires et des contrôles.
   - Dispose d'un modèle d'automatisation avec des flux de données et des workflows.
   - Prend en charge les scripts Python pour une personnalisation supplémentaire du comportement.
   - Il a des options de sécurité uniques.

2. **Multi-Composant** :
   - Combine plusieurs composants pour créer des applications complexes.
   - Il est utilisé pour construire une interface utilisateur unique, par exemple, dans des applications mobiles.

## Création d'un Nouveau Composant

1. Ouvrez Studio ('https://<your-hosting-name>/studio').
2. Allez dans le menu Applications/Composants.
3. Cliquez sur le bouton Ajouter pour créer un nouveau composant ou un multi-composant.

## Paramètres de Base du Composant

| Paramètre         | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| `Title`           | Le nom du composant qui est affiché aux utilisateurs.                |
| `Proxy Mode`      | Détermine si le composant agira en tant que proxy.                   |
| `Restrict Access` | Restreint l'accès au composant.                                     |
| `Maker`           | Identifie le créateur ou le propriétaire du composant.                |
| `Cron`            | Configuration de l'heure de début d'un composant à l'aide de Cron.   |
| `Run as User`     | Spécifie l'utilisateur au nom duquel il sera exécuté.                |
| `Access Mode`     | Définit le mode d'accès au composant.                               |
| `Description`     | Une description détaillée du composant, de son objectif et de ses fonctions. |
| `Domains`         | Les domaines ou catégories auxquels le composant appartient.          |

## Modèle d'Objet de Composant dans la Plateforme

Chaque composant de la plateforme inclut automatiquement les champs suivants :

- 'Id' : Un identifiant unique du composant.
- 'creatorSubject' : Le sujet qui a créé l'objet.
- 'updateSubject' : Le sujet qui a mis à jour l'objet.
- 'createdDate' : Date à laquelle l'objet a été créé.
- 'updateDate' : Date à laquelle l'objet a été mis à jour pour la dernière fois.

Les composants peuvent inclure des éléments supplémentaires, qui peuvent appartenir à l'un des onze types : 'string', 'datetime', 'catalog', 'number', 'integer', 'array', 'file', 'boolean', 'time', 'date', 'uri'. Chacun de ces éléments a ses propres paramètres.

Paramètres globaux pour tous les types :

- 'Name' : Nom système de la propriété.
- 'Title' : Nom de la propriété à afficher dans l'interface.
- 'Required' : Spécifie si le champ est requis.
- 'Primary Key' : Détermine si un champ est un identifiant unique.
- 'Query' : Détermine si le champ peut être utilisé dans des requêtes.
- 'Virtual property' : Exclut un champ des processus de synchronisation.

## Constructeur d'Interface

La plateforme offre un outil puissant pour personnaliser l'interface utilisateur de chaque composant – le Constructeur d'Interface. C'est un éditeur visuel qui vous permet de créer et de personnaliser des interfaces utilisateur multi-composants en utilisant des fonctionnalités de glisser-déposer. Le Constructeur d'Interface est un espace de travail dans la section Définition de l'Interface de Création de Composant.

Dans cette section, vous pouvez :

- Créer une interface d'application multi-écrans à l'aide d'un éditeur intuitif de glisser-déposer.
- Ajouter des éléments d'interface utilisateur à partir des catégories de Base, Avancé et Mise en Page.
- Configurer le modèle d'objet pour le Workflow et le Dataflow de l'application.
- Personnaliser les styles CSS pour tous les éléments d'interface utilisateur.

Après avoir ajouté des éléments d'interface utilisateur à la mise en page de votre application, vous pouvez effectuer les opérations suivantes :

- **Copier :** Copie l'élément actuel dans le presse-papiers.
- **Coller :** Colle l'élément copié à un nouvel emplacement.
- **Déplacer :** Change la position de l'élément.
- **Propriétés :** Ouvre le panneau des propriétés pour configurer l'élément.
- **Aperçu :** Affiche la mise en page dans un format proche de l'application de l'utilisateur.
- **Aperçu du balisage :** Affiche le balisage web textuel de la page.
- **Supprimer :** Supprime l'élément sélectionné.
- **Champ de données :** Vous permet de lier un élément à un champ de données (lien de base de données).

## Module des parties Web : “Styles” et “JavaScript”

Le bloc “Styles” est conçu pour décrire les styles CSS qui sont appliqués au composant, tandis que le bloc “JavaScript” vous permet d'établir une interaction avec l'interface utilisateur et de fournir des fonctionnalités supplémentaires en utilisant le langage JavaScript.

De cette manière, le module des parties Web permet aux développeurs de créer des composants plus complexes et interactifs en utilisant différents langages de programmation pour décrire les styles et la fonctionnalité.<br>

### Utilisation de "JavaScript"

Exemple d'utilisation de JavaScript pour implémenter une fonctionnalité de création de boutons, dont la pression prend une capture d'écran :

1. Pour appeler des fonctions JavaScript depuis le bloc 'Web parts', il est nécessaire d'utiliser la méthode context.InvokeInterop(methodName, objects) dans le script Componen :

````python
def capturePage1():
    context.InvokeInterop("callScreenshot")

2. Next, we move to the 'JavaScript' section of the 'Web parts' block and prepare function:
```javascript
// Création d'un élément <script> pour charger la bibliothèque html2canvas
var script = document.createElement('script');
script.src = "https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js";
document.head.appendChild(script);

// Fonction pour créer et télécharger une capture d'écran de la page
function takeScreenshot() {
    // Capturing a screenshot of the entire body using html2canvas
    html2canvas(document.body).then(canvas => {
        // Creating a link for downloading the screenshot
        var link = document.createElement('a');
        link.href = canvas.toDataURL("image/png");
        link.download = "screenshot.png";
        // Adding the link to the HTML document and simulating a click to download the screenshot
        document.body.appendChild(link);
        link.click();
        // Removing the link from the document after the screenshot has been downloaded
        document.body.removeChild(link);
    });
}

// Méthode pour appeler la fonction takeScreenshot
this.callScreenshot = () => {
    takeScreenshot();
}

Ce code crée un élément script qui charge la bibliothèque html2canvas depuis un réseau de distribution de contenu (CDN). Après le chargement de la bibliothèque, une fonction takeScreenshot() est définie, qui capture une capture d'écran de la page actuelle en utilisant html2canvas.

Après avoir créé la capture d'écran, le code crée un élément <a> pour rendre possible le téléchargement, définit son href sur l'URL de l'image au format PNG et l'attribut de téléchargement sur screenshot.png. Ensuite, il ajoute ce lien au corps du document, simule un clic sur ce lien pour télécharger la capture d'écran, et enfin supprime le lien du document.

### Utilisation de "Styles"

Exemple de code CSS qui définit la couleur de fond de votre espace de travail entier

```css
body {
    background-color: violet; /* Purple background color */
}
```

## Construction de flux de données et de workflows {: #dataflow-workflow }

Le modèle d'objet de chaque composant contient des données qui sont utilisées à la fois dans le composant lui-même et dans les processus de son intégration avec d'autres éléments du système. Ces données servent de base à la configuration et à l'exécution des flux de données et des workflows.

Pour commencer à construire un flux de données ou un workflow, vous devez faire glisser l'un des éléments depuis les "Flux" vers la zone de construction de l'interface, après quoi vous pourrez personnaliser l'éditeur visuel du flux de données et du workflow.

En savoir plus sur [les composants de flux de données](data-flow-components/index.md) et [les composants de workflow](workflow-components/index.md)

## Publication d'un composant et transfert vers l'interface Web {: #publication }

- Après avoir terminé la configuration du composant, vous devez le publier dans le cadre d'une nouvelle publication.
- La gestion des publications est décrite dans [Publication d'applications](publishing-applications.md).
- Ensuite, vous devez revenir au menu 'Accueil' et aller au 'menu de navigation' du 'domaine d'application' souhaité, cliquer sur 'Ajouter un élément de menu', sélectionner le composant souhaité, remplir les paramètres et cliquer sur 'Enregistrer'.

![Menu de navigation](../assets/images/app-development/navigation-menu.png)