# Vue en liste

![](../../assets/images/app-development/list-view.png)

## Informations générales
La "Vue en liste" est un composant d'interface utilisateur utilisé pour afficher et configurer la présentation des données sous forme de "cartes".

## Paramètres
**Propriétés du composant**

| Groupe de paramètres | Champ de paramètre   | Options de valeur          | Objectif                         |
|----------------------|----------------------|----------------------------|----------------------------------|
|                      | Nom                  | -                          | Nom du composant UI dans le système |
| Commun               | Composant            | Multisélection de Catalogue| Contient une liste de tous les Composants |
|                      | Nombre de colonnes   | -                          | Nombre de colonnes de conteneur  |
|                      | Nombre de lignes     | -                          | Nombre de lignes de conteneur     |
|                      | Espace entre colonnes| -                          | Espacement entre les colonnes     |
|                      | Espace entre lignes   | -                          | Espacement entre les lignes       |
|                      | Taille de page       | -                          | Taille du conteneur              |
|                      | Rechargement manuel   | true, false                | Capacité à recharger manuellement les données |
|                      | Masquer le sélecteur de page | true, false          | Masquer le sélecteur de page     |
|                      | Activer le glisser-déposer | true, false            | Activer la fonctionnalité de glisser-déposer |
|                      | Groupe de glisser-déposer | -                      | Groupe de glisser-déposer (le cas échéant) |
|                      | ID d'automatisation   | -                          | ID pour l'automatisation         |
| Événements           | À la charge de la source de données | -                | Événement de chargement de la source de données |
|                      | À la charge          | -                          | Événement de chargement du composant |
|                      | À la dépose          | -                          | Événement de glisser-déposer     |

**Propriétés CSS**

| Groupe de paramètres | Champ de paramètre   | Options de valeur          | Objectif                         |
|----------------------|----------------------|----------------------------|----------------------------------|
| Mise en page         | Largeur              | -                          | Largeur du composant             |
|                      | Hauteur              | -                          | Hauteur du composant             |
|                      | Marge                | -                          | Rembourrage extérieur du composant |
|                      | Rembourrage          | -                          | Rembourrage intérieur du composant |
|                      | Visible              | true, false                | Visibilité du composant          |
|                      | Caché                | true, false                | Camouflage du composant          |
|                      | Orientation          | Horizontal, Vertical       | Orientation du composant         |
| Apparence            | Rayon de coin        | -                          | Rayon d'arrondi des coins        |
|                      | Épaisseur de bord    | -                          | Épaisseur de la bordure du composant |
|                      | Opacité              | -                          | Transparence du composant        |
| Brosse               | Arrière-plan         | -                          | Couleur de fond du composant     |
|                      | Brosse de bord       | -                          | Couleur de la bordure du composant |

## Utilisation de la fonctionnalité de glisser-déposer
Tout d'abord, dans le groupe de paramètres "Commun", vous devez sélectionner l'option suivante :

![](../../assets/images/app-development/enable-drag-and-drop.png)

Après avoir enregistré et publié, le glisser-déposer sera déjà disponible pour cette vue en liste sur le lieu de travail. Pour le bon fonctionnement ultérieur, vous devez accéder au script du composant et préparer la fonction pour gérer l'événement de glisser-déposer (à la dépose).

Voici un exemple de la fonction appliquée à un tableau kanban qui se compose d'une vue en liste principale et d'une vue en liste imbriquée. La principale remplit la fonction des étapes de l'entonnoir de vente et est en position horizontale, tandis que l'imbriquée contient les affaires elles-mêmes et est en position verticale. La fonction prend l'ID de l'objet en cours de glissement (dans ce cas, l'affaire) et l'étape à laquelle l'affaire est transférée, puis appelle le flux de données et, si cela réussit, met à jour la vue en liste, déplaçant l'affaire vers une nouvelle étape :

```python
def OnMove(dstList, srcList, dataObject, oldIdx, newIdx):
    context.Logger.Info("Callback on move")
    # The new Busy(boolean) method puts the UIElement into a loading status,
    # showing or hiding the loader
    srcList.Busy(True)
    dstList.Busy(True)
    
    # The new GetDynamicFilterValue(string) method computes the value of a Dynamic filter.
    # If there are two filters on one field, the first in the list is computed
    stage = dstList.GetDynamicFilterValue("data.Stage")
    
    # Creating a model to call the data-flow
    flowModel = {"Stage": stage, "OrderId": dataObject.Id}
    # Calling the data-flow with a new overload for onComplete and onError
    context.ExecuteDataflow("783cf3e3-d8f8-4551-8447-13be4f738e41", flowModel, 
    lambda res: OnDataflowComplete(res, dstList, srcList), 
    lambda ex: OnDataflowError(ex, dstList, srcList))

def OnDataflowComplete(dataResult, dstList, srcList):
    # The new Busy(boolean) method puts the UIElement into a loading status,
    # showing or hiding the loader
    srcList.Busy(False)
    dstList.Busy(False)
    # Refreshing the lists
    srcList.Refresh()
    dstList.Refresh()

def OnDataflowError(exception, dstList, srcList):
    # The new Error(boolean, string) method puts the UIElement into an error status,
    # displaying the error message
    srcList.Error(True, "An error occurred")
    dstList.Error(True)
    context.Logger.Error(exception, "An error occurred during the data-flow call")
```

## Cas
- **Affichage des données** : Efficace pour présenter des données sous forme de cartes ou de listes.
- **Interface utilisateur** : Convient aux interfaces qui nécessitent une représentation de l'information sous forme de cartes ou de listes.

## Exceptions
- **Flexibilité limitée** : Pas adapté pour afficher des données au-delà du format carte ou liste, car il se spécialise dans une représentation visuelle spécifique.
- **Limitations visuelles** : Le style et le design peuvent être limités par les paramètres CSS, ce qui peut ne pas répondre à toutes les exigences de conception.