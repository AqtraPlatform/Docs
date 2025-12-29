# Mot de passe

![](../../assets/images/app-development/password.png)

## Informations générales
Le mot de passe est un composant d'interface utilisateur de base conçu pour entrer des mots de passe de manière sécurisée. Ce composant est utilisé pour créer des champs de saisie de mot de passe, garantissant la confidentialité et la protection des données saisies.

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
|  | Nom | - | Nom du composant UI dans le système |
| Commun | Désactivé | true, false | La propriété permet de désactiver un élément sur le formulaire |
|  | Requis | true, false | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire |
|  | Afficher le clair | true, false | Affiche l'icône de réinitialisation de la valeur du champ |
|  | Autocomplétion |  | Champ pour définir la valeur de l'attribut HTML d'autocomplétion. En règle générale, utilisez username pour le champ de saisie du nom, et password, new-password ou current-password pour les champs de saisie correspondants pour différents types de mots de passe. Fonctionne en conjonction avec le paramètre Provide Root Form pour le contrôle de l'interface utilisateur de la page. |
|  | Étiquette | - | Contient la table des matières du conteneur de texte |
|  | Liaison | Multisélection de Catalogue | Contient un champ “String” lié du modèle |
| Événements | Sur changement de valeur | - | Permet d'exécuter le script spécifié après avoir changé la valeur du champ |
|  | Sur key down |  | Permet d'exécuter le script spécifié après être passé à l'élément suivant de la page (onglet) |
|  | Sur key up |  | Permet d'exécuter le script spécifié après être revenu à l'élément précédent de la page (onglet) |
|  | Sur focus |  | Permet d'exécuter un script au moment où un élément est mis au point |
| Index d'onglet |  | Entier positif commençant à zéro | Définit l'ordre dans lequel les champs actifs (éditables) sont basculés via le clavier (par exemple, en utilisant la touche Tab) |
| ID d'automatisation |  |  | ID de contrôle pour les tests automatisés et pour le transfert des paramètres CSS |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif |
| --- | --- | --- | --- |
| Mise en page | Largeur | - | Largeur du composant |
|  | Hauteur | - | Hauteur du composant |
|  | Croissance | true, false | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|  | Marge | - | La propriété définit les marges extérieures sur les quatre côtés de l'élément |
|  | Rembourrage | - | La propriété définit les rembourrages intérieurs sur tous les côtés de l'élément |
| Apparence | Rayon de coin | - | La propriété est utilisée pour arrondir les coins d'un élément |
|  | Épaisseur de bordure | - | La propriété permet de définir les limites de l'élément |
| Brosse | Arrière-plan | - | La propriété définit la couleur de fond de l'élément |
|  | Brosse de bordure | - | La propriété définit la couleur de la bordure de l'élément |

## Cas d'utilisation
- **Formulaires d'authentification** : Utilisé dans les formulaires de connexion et d'inscription pour entrer des mots de passe de manière sécurisée.
- **Formulaires interactifs** : Activation de formulaires interactifs nécessitant la saisie de données confidentielles.

## Exceptions
- **Limitations de formatage** : Ne prend pas en charge des formats de texte complexes tels que les hyperliens ou les images intégrées.