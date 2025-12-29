# Action de formulaire

![](../../assets/images/app-development/form-action.png)

## Informations générales
L'étape "Action de formulaire" est utilisée pour effectuer diverses actions dans l'interface utilisateur (UI) à l'avant de l'application, telles que l'ouverture de pages, l'exécution de scripts, l'ouverture de fenêtres modales, etc. L'étape est le lien entre la logique du serveur et l'interface utilisateur, vous permettant de contrôler dynamiquement le comportement de l'UI.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur | Objectif |
|--------------------|-------------------|----------|
| Nom de l'étape     | -                 | Nom de l'étape |
| Étape source       | Multisélection de Catalogue | Sélection des étapes précédentes |
| Action de formulaire| Exécuter le script, Ouvrir la page, Ouvrir le composant, Ouvrir la barre latérale, Ouvrir la modale, Ouvrir le fichier dans un nouvel onglet | Type de commande UI |
| Nom de la méthode  | (Si 'Exécuter le script' est sélectionné) | Nom de la fonction de script à exécuter |
| Ouvrir la page     | (Si 'Ouvrir la page' est sélectionné) | Liste des pages à ouvrir |
| Champ d'information de fichier | (Si 'Ouvrir le fichier' dans un nouvel onglet est sélectionné) | Champ d'information de fichier à ouvrir |
| Ouvrir la barre latérale | Paramètres pour la barre latérale | Configuration pour ouvrir la barre latérale |
| Ouvrir la modale   | Paramètres pour les fenêtres modales | Configuration pour ouvrir une fenêtre modale |

## Cas d'utilisation
- **Gestion dynamique des éléments UI** : Utiliser "Ouvrir la barre latérale" ou "Ouvrir la modale" vous permet d'afficher dynamiquement des barres latérales ou des modales avec des informations supplémentaires, des formulaires ou d'autres contenus, ce qui augmente l'interactivité et l'utilisabilité de l'interface.
- **Mise à jour de la grille de données** : Dans un script où l'utilisateur charge de nouvelles données, vous pouvez ajouter une fonction de rafraîchissement au formulaire et la grille de données sera mise à jour sans rafraîchir la page.

## Exceptions
- **Étape d'écriture de réponse requise** : Après avoir effectué des actions telles que l'ouverture d'une page ou d'un fichier, vous devez ajouter une étape "Écrire la réponse" pour compléter correctement le flux de données.
- **Dépendance aux étapes précédentes** : Lors de l'utilisation de certaines actions, telles que "Ouvrir le fichier dans un nouvel onglet", vous devez avoir un fichier approprié préparé par les étapes précédentes.

## Scénario d'application

Ce composant utilise diverses méthodes dans l'étape Action de formulaire pour interagir avec l'interface utilisateur à l'avant. Les utilisateurs peuvent effectuer différentes actions telles qu'exécuter un script (Exécuter le script), ouvrir une page (Ouvrir la page) ou un composant (Ouvrir le composant), télécharger un fichier (Télécharger le fichier) et ouvrir un fichier dans un nouvel onglet (Ouvrir le fichier dans un nouvel onglet). Après que ces actions ont été exécutées, les données sont traitées et renvoyées à l'avant à l'aide de l'étape Écrire la réponse.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1AgjjrOW-z2LPMj7sFWg_PKjHjFfVtxub/view?usp=sharing)