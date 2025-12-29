# Tutoriel №3

<br>

## Utilisation de Python

### Introduction

<br>

La plateforme offre la possibilité d'utiliser Python à diverses fins en tant que langage de script/programming pratique et largement connu.

Les scripts Python pris en charge par la plateforme doivent utiliser la version 3.0 de Python, comme décrit ici : https://docs.python.org/3/. Le guide complet pour les développeurs peut être trouvé dans la section "Utilisation de Python".

La version de Python utilisée par la plateforme est appelée Iron Python, qui fournit une interface pour le code C#. Elle fournit deux bibliothèques importantes qui doivent être importées au début du script — `clr` et `system`. Ces bibliothèques donnent accès aux entités de la plateforme qui peuvent être interrogées et contrôlées depuis le script.
<br>

### Façons d'utiliser des scripts Python sur la plateforme

<br>

Il existe plusieurs façons d'utiliser Python sur la plateforme :

- Elle permet de contrôler les formulaires d'application conçus et exécutés à l'aide de la plateforme, ainsi que de fournir des indices personnalisés qui peuvent être déclenchés en réponse à un événement, tel qu'un client appuyant sur un bouton.
  <br>

- Appeler une fonction à l'intérieur d'un "script de composant", par exemple, lorsqu'un bouton est pressé :

  - Pour ce faire, vous devez définir une fonction à l'intérieur du script de composant, puis aller à un élément de contrôle UI tel qu'un bouton, aller à la section "Actions" et définir le paramètre "Type de commande" sur "Exécuter le script". Ensuite, vous devez entrer le nom et les paramètres d'appel (le cas échéant) de votre script dans les champs fournis.
    <br>

- Utiliser une fonction à l'intérieur d'un script de composant pour les événements de changement de valeur :
  - Pour ce faire, vous devez définir une fonction à l'intérieur du script de composant, puis aller à un élément de contrôle UI tel qu'une zone de texte, etc., puis aller à la section "Événements" et entrer le nom de votre script dans le champ "Lors du changement de valeur".
  - Notez que cette fonction ne sera appelée que si les données dans le champ ont changé et que le focus de l'élément de contrôle UI dans le formulaire quitte cet élément de contrôle UI.

<br>

- En s'abonnant aux changements de données en utilisant la méthode `context.DataModel.Model.Subscribe()` :
  - La façon la plus simple de le faire est de définir une fonction pour intercepter tous les changements (par exemple, `def check_all_changes()`) dans votre script de composant, puis de s'y abonner.
  - Votre fonction sera appelée chaque fois qu'il y a un changement dans les données actuelles de l'élément de contrôle UI, au moment où cet élément de contrôle UI perd le focus (par exemple, lorsque l'utilisateur passe à un autre élément de contrôle UI ou à une autre application).

<br>

- Dans le cadre d'une action DataFlow, exécutez un script pour définir la logique de prise de décision, transformer des données et définir des variables internes qui seront utilisées dans le cadre des scripts DataFlow. Vous pouvez voir des exemples d'utilisation de scripts Python pour DataFlow dans la section "Utilisation de Python".

<br>

### Utilisation de Python pour accéder aux composants de la plateforme

<br>

Pour accéder aux composants de la plateforme, vous devez d'abord importer les bibliothèques clr d'IronPython, comme indiqué ci-dessous.

```
#Add IronPython library that imports system CRL (.NET) names into Python
import clr
```

Après l'importation, plusieurs objets peuvent être accessibles depuis le script Python via la variable système `context`.

<br>

### Utilisation de context.Model & context.DataModel

<br>

`context.Model` & `context.DataModel` fournissent un accès à divers champs de données du modèle de la plateforme.

Pour context.Model, les champs de données incluent à la fois les champs de composant par défaut fournis par la plateforme et les champs personnalisés ajoutés par le développeur de composants.

Pour context.DataModel, seuls les champs personnalisés ajoutés par les développeurs de composants sont disponibles.

Il est recommandé d'utiliser context.DataModel pour accéder à tous les champs personnalisés, et context.Model ne doit être utilisé que pour accéder aux champs internes du composant par défaut.

Si nous écrivons un script de composant qui accède à ce modèle, les variables de modèle système suivantes seront disponibles dans notre script via context.Model :
- `Id` - identifiant interne, généré automatiquement par la plateforme pour chaque composant. Si Id == 0, cela signifie que les données du composant n'ont pas encore été enregistrées, indiquant que nous sommes en mode saisie de données pour cette instance particulière des données du composant, comme l'ajout d'une nouvelle facture dans notre Tutoriel #1.
- `createDate` - date définie en interne lorsque l'instance de données de ce composant a été créée pour la première fois
- `name` (String) - nom convivial pour le système qui sera pris par défaut pour afficher des liens à travers des champs de type Catalogue
- `updateDate` - date définie en interne de la dernière mise à jour de l'instance de données de ce composant.
- `CreatorSubject` - données qui montrent quel utilisateur a ajouté l'instance de données de ce composant particulier.
- `changeAuthor` - données qui montrent quel utilisateur a mis à jour pour la dernière fois ce composant particulier

De plus, les attributs spécifiques au composant suivants seront disponibles pour notre composant du Tutoriel #1 via context.DataModel (recommandé) ou context.Model :

- `InvoiceName` - nom unique pour notre nouvelle facture
- `InvoiceState` - statut actuel de notre nouvelle facture
- `InvoiceNumber` - identifiant numérique unique pour notre facture
- `InvoiceDueDate` - date d'échéance de notre facture
- `InvoiceTotalValue` - valeur totale de notre facture

Écrivons maintenant un script d'exemple qui pré-remplira certains champs pour une nouvelle facture.

<br>

```python
#Start of the script
#Add IronPython library that imports system CRL (.NET) names into Python
import clr

#Get Component’s DataModel reference
datamodel = context.DataModel.Model
# context.Model.Id shows internal Id for the component data instance
if (context.Model.Id == 0):
# If context.Model.Id is 0, then the instance has not yet been created,
# That means we are creating a new invoice
# We will then set some fields with default values
# Since this is a new Invoice,
# We’ll set it’s status to Under Review and provide default number and name
datamodel.InvoiceNumber = 11111
datamodel.InvoiceName = 'PLEASE_SET_A_UNIQUE_NAME'
datamodel.InvoiceState = 0
#End of the script
```

<br>

Maintenant, si nous ouvrons l'application du Tutoriel #1 et cliquons sur le bouton "Ajouter" pour ajouter une nouvelle facture, l'écran ressemblera à ceci :

<br>

![Tutoriel 3.1](../assets/images/tutorials/tut3.1.png)

<br>

### Utilisation de context.Properties

<br>

`context.Properties` permet d'accéder à tous les éléments du composant et peut être utilisé, par exemple, pour utiliser les fonctions des éléments de contrôle de l'interface utilisateur du formulaire pour gérer un élément de contrôle de l'interface utilisateur spécifique.

Pour accéder à un élément de contrôle de l'interface utilisateur, utilisez `context.Properties` comme suit :

```
context.Properties.<Internal_UI_Control_Name>.<UIControlProperty> = <Value>
```

Ici, `<Internal_UI_Control_Name>` doit être remplacé par le nom de votre élément de contrôle de l'interface utilisateur que vous avez configuré lors de la conception. Par exemple, dans le cas du Tutoriel #1, nous avons défini le nom interne pour l'élément de contrôle de l'interface utilisateur InvoiceState comme indiqué ci-dessous :

<br>

![Tutoriel 3.2](../assets/images/tutorials/tut3.2.png)

<br>

Nous pouvons maintenant utiliser ce nom interne pour définir la logique suivante :

1. Lors de la création d'une nouvelle facture, le statut est défini sur "En cours de révision".
2. Changer le champ de statut est interdit, ce qui signifie que ce champ doit être désactivé mais visible.

La façon de procéder est d'utiliser la propriété `Disable` de notre élément de contrôle de l'interface utilisateur pour la définir sur `True`. Cela fera apparaître le champ mais il ne peut pas être modifié par l'utilisateur créant la nouvelle facture. Cela se fait en ajoutant une ligne de code comme indiqué ci-dessous :

```
context.Properties.UI_InvoiceStatus.Disabled = True
```

Ajouter cela à notre script de composant entraînera les changements suivants dans notre formulaire d'ajout de nouvelle facture.

<br>

![Tutoriel 3.3](../assets/images/tutorials/tut3.3.png)

<br>

Comme vous pouvez le voir, le champ "Statut de la facture" est maintenant désactivé.

Un autre champ fréquemment utilisé `context.Properties` pour gérer les éléments de contrôle de l'interface utilisateur est `Visible`. S'il est défini sur `False`, cet élément de contrôle de l'interface utilisateur spécifique n'apparaîtra pas dans le formulaire. Il peut ensuite être réactivé en le définissant sur `True`. Cela peut être fait pour tout élément de contrôle de l'interface utilisateur, y compris les panneaux contenant plusieurs éléments de contrôle de l'interface utilisateur différents.

Un exemple de la façon dont cela peut être utilisé dans le contexte de notre Tutoriel #1 pour cacher initialement le champ "Statut de la facture" est montré ci-dessous.

<br>

```python
if (context.Model.Id == 0):
    context.Properties.UI_InvoiceStatus.Visible = False
if (context.Model.Id > 0):
    context.Properties.UI_InvoiceStatus.Visible = True
```

<br>

Il y a aussi le champ `Hidden`, qui cache/affiche les éléments de l'interface utilisateur, similaire au champ `Visible`.

Un autre champ fréquemment utilisé `context.Properties` est `Required`. S'il est défini sur `True`, l'élément de contrôle de l'interface utilisateur spécifique devient obligatoire (ne peut pas être vide), et s'il est défini sur `False`, il devient optionnel. Notez que cela ne change que l'état de l'élément de contrôle de l'interface utilisateur pour la propriété personnalisée dans l'instance actuelle du formulaire, pas la propriété personnalisée elle-même, le modèle de formulaire, ou les éléments de contrôle de l'interface utilisateur pour cette propriété personnalisée dans d'autres formulaires.

<br>
### Utilisation de context.Form

<br>

`context.Form` peut être utilisé pour accéder aux données du formulaire (par exemple, à des fins de validation lors du traitement du formulaire, avant que les données du formulaire ne soient enregistrées dans le stockage interne) ou pour gérer la représentation visuelle du formulaire, par exemple en définissant un message d'erreur.

Pour ce faire, utilisez `context.Form.Get(<CustomFieldName>)` pour obtenir un objet représentant un champ spécifique. Ensuite, vous pouvez utiliser les fonctions suivantes avec cet objet.

- `context.Form.Get(<CustomFieldName>).SetValue(<Value>)` — définit la valeur d'un contrôle UI spécifique dans le formulaire actuel.
- `context.Form.Get(<CustomFieldName>).AddError(<StringValue>)` — définit un message d'erreur affiché sous un contrôle UI spécifique dans le formulaire actuel.
- `context.Form.Get(<CustomFieldName>).ClearError()` — efface le message d'erreur affiché sous un contrôle UI spécifique dans le formulaire actuel.

L'extension de script suivante montre comment vérifier la situation où l'utilisateur n'a pas changé le nom de facture par défaut que nous avons défini ci-dessus dans les exemples pour le Tutoriel #1.

<br>

```python
if datamodel.InvoiceName == 'PLEASE_SET_A_UNIQUE_NAME':
    context.Form.Get("InvoiceName").AddError("Please set a unique invoice name")
else:
    context.Form.Get("InvoiceName").ClearError()
```

<br>

Le résultat ressemblera à la capture d'écran suivante si le nom par défaut n'a pas été changé :

<br>

![Tutoriel 3.4](../assets/images/tutorials/tut3.4.png)

<br>

### Utilisation de context.Commands

<br>

`context.Commands` peut être utilisé pour gérer l'interface utilisateur du composant actuellement exécuté, changer le contenu du formulaire actuel, ouvrir différentes pages, ouvrir de nouveaux composants, revenir à la page précédente, ou même lancer de nouveaux Workflows, Dataflows ou Scripts.

Ces commandes sont généralement utilisées dans des scripts appelés par l'action ExecuteScript à l'aide de boutons, et dans des cas similaires. Par exemple, dans notre Tutoriel #1, le bouton Retour à toutes les factures peut utiliser le script suivant pour revenir à la page précédente :

<br>

```python
def navigate_back():
    context.Commands.NavigationBack()
```

<br>

Ce script doit faire partie du script du composant et être configuré pour le bouton Retour à toutes les factures, dans la section `Actions` -> `Command Type` : `Execute Script` -> `Method Name` : `navigate back`.

<br>

Autres fonctions disponibles de context.Commands :

- `context.Commands.AddItem(GUID)` - ajouter un élément de contrôle UI à la page en utilisant le GUID.
- `context.Commands.ChangePageAsync(GUID)` - ouvrir une page en utilisant son GUID
- `context.Commands.ChangePageByName(«PageName»)` - changer la page du composant actuel en une nouvelle page en utilisant le nom interne
- `context.Commands.OpenComponent(GUID ComponentID, GUID PageID)` - ouvrir un nouveau composant et une page spécifique dans le composant
- `context.Commands.EditItem(GUID UI_ControlID, EntityId)` - déplacer le focus de l'UI vers un élément de contrôle UI spécifique et des données spécifiques (en utilisant son identifiant interne)
- `context.Commands.ExecuteWorkflow(GUID WorkflowID)` - exécuter un workflow en utilisant son identifiant. De plus, vous pouvez définir WaitComplete sur true ou false si nécessaire.
- `context.Commands.ExecuteDataflow(GUID dataflow identifier, ContextID)` - exécuter un dataflow en utilisant son GUID et le contexte de données spécifié.
- `context.Commands.ExecuteScript(String ScriptName, StringParams Script)` - exécuter un script (fonction) à partir du Script du Composant avec certains paramètres.