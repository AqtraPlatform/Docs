# Étiquette

![](../../assets/images/app-development/label.png)

## Informations générales
L'étiquette est un composant d'interface utilisateur de base conçu pour afficher des champs de texte non modifiables sur des captures d'écran. Ce composant est largement utilisé pour ajouter du texte descriptif, des titres ou simplement afficher des informations que l'utilisateur ne peut pas changer.

## Paramètres
**Propriétés du composant :**

| Groupe de paramètres | Champ de paramètre | Options de valeur         | Objectif |
|----------------------|--------------------|---------------------------|----------|
| (Paramètres globaux) | Nom                | -                         | Nom du composant UI dans le système |
| Texte                | Taille de police    | -                         | Taille de la police |
|                      | Couleur            | -                         | Couleur du texte (CSS) |
|                      | Gras               | true, false               | Police en gras |
|                      | Italique           | true, false               | Police en italique |
|                      | Alignement du texte| Gauche, Droite, Centre, Justifier | Alignement du texte |
| Commun               | Liaison           | Multisélection de Catalogue | Liaison aux données |
|                      | Valeur            | -                         | Valeur de champ statique |
|                      | Format            | -                         | Format d'entrée/sortie des données (Pour DataTime) |

**Propriétés CSS :**

| Groupe de paramètres | Champ de paramètre | Options de valeur         | Objectif |
|----------------------|--------------------|---------------------------|----------|
| Mise en page         | Aligner les éléments| Aucun, Centre, Fin, Début, Étendre | Alignement des éléments dans un conteneur flex |
|                      | Largeur            | -                         | Largeur du composant |
|                      | Hauteur            | -                         | Hauteur du composant |
|                      | Élargir            | true, false               | Étirement d'un composant dans un conteneur |
|                      | Marge              | -                         | Rembourrage extérieur |
|                      | Rembourrage        | -                         | Rembourrage intérieur |
| Apparence            | Rayon de coin      | -                         | Rayon des coins |
|                      | Épaisseur de bord  | -                         | Épaisseur de la bordure |
| Brosse               | Arrière-plan       | -                         | Couleur de fond |
|                      | Brosse de bordure  | -                         | Couleur de la bordure |

## Cas d'utilisation
- **Conseils d'information** : Utiliser une étiquette pour fournir des informations complémentaires à côté d'autres éléments de l'interface utilisateur, comme expliquer les fonctions des boutons ou des données d'entrée.
- **Titres de section** : Les étiquettes peuvent servir de titres pour différentes sections de l'interface, délimitant clairement le contenu pour améliorer l'expérience utilisateur.
- **Affichage de statut** : Dans les cas où il est nécessaire d'afficher le statut ou le résultat d'une opération, une étiquette peut être utilisée pour afficher les messages correspondants (par exemple, “Chargement...”, “Terminé avec succès”).

## Exceptions
- **Non-modifiabilité** : L'étiquette n'est pas destinée à l'entrée utilisateur ou à la modification de texte. Essayer de l'utiliser à ces fins entraînera un design d'interface inefficace.
- **Restrictions de format** : Bien que l'étiquette permette un certain niveau de personnalisation du texte, elle ne peut pas contenir d'éléments de texte complexes tels que des hyperliens ou des images en ligne.