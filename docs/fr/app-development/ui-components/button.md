# Bouton

![](../../assets/images/app-development/button.png)

## Informations générales
Un Bouton est le principal composant de l'interface utilisateur utilisé pour exécuter des commandes ou initier des actions dans une application. Il peut être configuré pour exécuter des processus, confirmer des actions utilisateur ou servir d'outil de navigation.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre | Options de valeur       | Objectif |
|----------------------|--------------------|-------------------------|----------|
| (Paramètres globaux) | Nom                | -                       | Nom du composant UI dans le système |
| Commun               | Icône              | -                       | Chargement de l'icône (.svg) |
|                      | Désactivé          | true, false             | Désactivation d'un élément |
|                      | Étiquette          | -                       | Texte du bouton |
| Texte                | Taille de police    | -                       | Taille de la police |
|                      | Couleur            | -                       | Couleur du texte (CSS) |
|                      | Gras               | true, false             | Police en gras |
|                      | Italique           | true, false             | Police en italique |
|                      | Alignement du texte| Gauche, Droite, Centre, Justifier | Alignement du texte |
| Actions              | Type de commande   | Diverses commandes      | Action par clic sur le bouton |
|                      | Restreindre l'accès| true, false             | Limitation d'accès |

**Propriétés CSS :**

| Groupe de paramètres | Champ de paramètre | Options de valeur       | Objectif |
|----------------------|--------------------|-------------------------|----------|
| Mise en page         | Largeur            | -                       | Largeur du composant |
|                      | Hauteur            | -                       | Hauteur du composant |
|                      | Élargir            | true, false             | Étirement du composant |
|                      | Marge              | -                       | Rembourrage extérieur |
|                      | Rembourrage        | -                       | Rembourrage intérieur |
| Apparence            | Rayon de coin      | -                       | Rayon des coins |
|                      | Épaisseur de bord  | -                       | Épaisseur de la bordure |
| Brosse               | Arrière-plan       | -                       | Couleur de fond |
|                      | Brosse de bordure  | -                       | Couleur de la bordure |

## Cas d'utilisation
- **Soumission de formulaire** : Utilisation d'un bouton pour soumettre des données de formulaire au serveur ou pour initier le traitement des données de formulaire dans l'application.
- **Navigation** : Attribution d'un bouton pour naviguer entre différents écrans ou sections de l'application.
- **Éléments interactifs** : Création de boutons pour contrôler des éléments interactifs, tels que le changement de contenu sur une page.

## Exceptions
- **Limitations sur le nombre d'actions** : Une seule action peut être assignée à un bouton (exécuter un flux de données, exécuter un script, etc.).