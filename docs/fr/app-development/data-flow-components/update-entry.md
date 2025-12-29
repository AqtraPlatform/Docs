# Mise à jour de l'entrée

![](../../assets/images/app-development/update-entry.png)

## Informations générales

L'étape "Mise à jour de l'entrée" est utilisée pour créer, mettre à jour ou supprimer une entrée existante dans le système. Cette étape est exécutée directement, et le système attend qu'elle soit terminée. Si une erreur se produit pendant l'exécution, la poursuite de l'exécution du flux de données sera arrêtée.

## Paramètres

**Paramètres de l'étape :**

| Champ de paramètre      | Options de valeur | Objectif                                        |
| ----------------------- | ----------------- | ----------------------------------------------- |
| Nom de l'étape          | -                 | Nom de l'étape                                 |
| Étape source            | -                 | Sélection de l'étape précédente                 |
| Composant               | -                 | Composant à mettre à jour                      |
| Clé du champ composant  | -                 | Champ avec la clé du composant à mettre à jour |
| Marquer l'entrée pour suppression | true, false   | Marque de suppression de l'entrée              |
| Champ de nom            | -                 | Nom du champ à mettre à jour                   |
| Champ de stockage du résultat | -             | Champ pour enregistrer le résultat de l'opération |
| Mappage des champs      | -                 | Mappage des champs entre le flux de données et le composant |

## Cas d'utilisation

- **Mise à jour des données** : Utilisé pour mettre à jour les informations dans les entrées existantes des composants du système afin de garantir que les données sont précises et à jour.
- **Suppression d'une entrée** : L'étape "Mise à jour de l'entrée" peut être utilisée pour supprimer des entrées existantes dans le système. Cela est particulièrement pertinent dans les scripts où vous devez supprimer des informations obsolètes ou incorrectes pour maintenir la précision et l'actualité des données dans le système. Par exemple, cela peut consister à supprimer le compte d'un utilisateur qui a quitté l'organisation ou à retirer des articles non disponibles de l'inventaire. Il est important de noter que l'étape peut être configurée pour marquer l'entrée pour suppression, ce qui vous permet de gérer le processus de suppression de manière plus flexible.

## Exceptions

- **Dépendance à la présence d'un ID d'instance** : Pour mettre à jour les données avec succès, l'ID d'instance du composant doit d'abord être reçu et transmis.
- **Gestion des erreurs d'exécution** : Toute erreur survenant pendant le processus de mise à jour des données arrêtera le flux de données, ce qui nécessite une surveillance attentive de la gestion des erreurs et des exceptions.

## Scénario d'application

Le composant présente un scénario pour ajouter, modifier et supprimer des enregistrements de composants en utilisant l'étape "Mise à jour de l'entrée".

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1k1oMpI2YSF-P3zgsd2cORfRjFs3l7w0o/view?usp=sharing)