# Numéro de téléphone

![](../../assets/images/app-development/phone-number.png)

## Informations générales

Le Numéro de téléphone est un composant UI conçu pour entrer et afficher des numéros de téléphone. Ce composant facilite l'entrée des numéros de téléphone, garantissant un formatage correct et une validation des données saisies.

## Paramètres

**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre | Options de valeur          | Objectif                                                                               |
| -------------------- | ------------------ | -------------------------- | ------------------------------------------------------------------------------------- |
|                      | Nom                | -                          | Nom du composant UI dans le système                                                  |
| Commun               | Désactivé          | true, false                | La propriété vous permet de désactiver un élément sur le formulaire                   |
|                      | Requis             | true, false                | La propriété rend l'élément obligatoire à remplir avant de soumettre le formulaire    |
|                      | Étiquette          | -                          | Contient la table des matières du conteneur de texte                                 |
|                      | Liaison            | Multiselect de Catalog     | Contient un champ “String” lié du modèle                                             |
| Événements           | Sur changement de valeur | -                      | Vous permet d'exécuter le script spécifié après avoir changé la valeur du champ      |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre | Options de valeur | Objectif                                                                                                                   |
| -------------------- | ------------------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Mise en page         | Largeur            | -                 | Largeur du composant                                                                                                       |
|                      | Hauteur            | -                 | Hauteur du composant                                                                                                       |
|                      | Croissance         | true, false       | La propriété détermine dans quelle mesure un élément va croître par rapport aux autres éléments flex dans le même conteneur |
|                      | Marge              | -                 | La propriété définit les marges extérieures sur les quatre côtés de l'élément                                            |
|                      | Rembourrage        | -                 | La propriété définit les rembourrages intérieurs sur tous les côtés de l'élément                                          |
| Apparence            | Rayon de coin      | -                 | La propriété est utilisée pour arrondir les coins d'un élément                                                             |
|                      | Épaisseur de bord  | -                 | La propriété vous permet de définir les limites de l'élément                                                                |
| Brosse               | Arrière-plan       | -                 | La propriété définit la couleur de fond de l'élément                                                                        |
|                      | Brosse de bord     | -                 | La propriété définit la couleur de la bordure de l'élément                                                                  |

## Cas d'utilisation

- **Validation du format du numéro :** Utilisé pour valider le numéro de téléphone saisi afin de s'assurer qu'il suit un format national ou international spécifique.

## Exceptions

- **Options de formatage limitées :** La fonctionnalité peut ne pas prendre en charge tous les formats de numéro de téléphone possibles, en particulier les variantes non standard ou régionales.
- **Sensibilité aux erreurs de saisie :** Une saisie utilisateur invalide peut entraîner des erreurs dans le traitement du numéro de téléphone.