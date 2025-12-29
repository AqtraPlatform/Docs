# Tutoriel №2 
<br>

## Création d'une application simple pour un concessionnaire automobile
<br>

**Description de l'application :**

Nous allons créer une application composée de plusieurs composants qui permet de suivre les voitures disponibles à la vente, d'assigner un responsable pour la signature des contrats et de permettre aux responsables de conclure la vente.

**Nous allons créer les composants suivants :**

<br>

### Composant "Spécialistes des transactions"

Le premier composant sera un formulaire simple pour ajouter de nouveaux responsables et consistera en une seule propriété personnalisée :

<br>

![Tutoriel 2.2](../assets/images/tutorials/tut2.1.png)

<br>

Ensuite, nous passons à la configuration de notre espace de travail, en ajoutant un élément de panneau où nous allons effectuer notre travail.

Puis, dans les paramètres du panneau sous le groupe de paramètres "Disposition", changez l'orientation du panneau en vertical et commencez à ajouter les éléments suivants : nous aurons besoin du manager_name que nous avons créé et d'un bouton. Cela devrait ressembler à ceci :

<br>

![Tutoriel 2.2](../assets/images/tutorials/tut2.2.png)

<br>

Ensuite, créez un flux de données, nommez-le "Ajouter un responsable" et ajoutez les étapes suivantes : `get action model`, `update entry`, `write response`. Cela devrait ressembler à ceci :

<br>

![Tutoriel 2.3](../assets/images/tutorials/tut2.3.png)

<br>

Configurez l'étape `Update entry` comme suit :

<br>

![Tutoriel 2.4](../assets/images/tutorials/tut2.4.png)

<br>

**N'oubliez pas** de définir le `source step` pour l'étape `update entry` !

Après avoir configuré le flux de données, liez-le au bouton comme suit : allez dans les paramètres du bouton, cliquez sur le groupe de paramètres "actions", définissez le "type de commande" sur "exécuter le flux de données" et sélectionnez le flux de données que nous avons créé "Ajouter un responsable".

Cliquez sur "Enregistrer", "Prêt à publier". Publiez le composant, puis ajoutez-le au lieu de travail en utilisant le "menu de navigation" du domaine où vous déployez votre application (dans notre cas, il s'agit du domaine "digital-workplace").

<br>

![Tutoriel 2.5](../assets/images/tutorials/tut2.5.png)

<br>

Cliquez sur "AJOUTER UN ÉLÉMENT DE MENU" et ajoutez notre composant :
<br>

![Tutoriel 2.6](../assets/images/tutorials/tut2.6.png)

<br>

Allez dans le `workplace` et ajoutez quelques responsables pour travailler avec eux par la suite.

<br>

### Composant "Flotte de voitures"

<br>

Avec ce composant, nous allons configurer l'affichage de toutes les voitures et des informations générales les concernant, ajouter un formulaire pour créer des enregistrements de nouvelles voitures, un formulaire pour assigner un responsable de transaction à une voiture, et un formulaire pour confirmer que la vente est conclue avec l'archivage ultérieur de l'enregistrement de la voiture.

Dans ce composant, nous allons créer un certain nombre de propriétés personnalisées :

- `car_vin` : type de propriété - `string`, titre - `VIN`, paramètres - `required`, `primary key`, `query` ;
- `car_brand` : type de propriété - `string`, titre - `Car Brand`, paramètres - `required`, `query` ;
- `car_model` : type de propriété - `string`, titre - `Car Model`, paramètres - `required`, `query` ;
- `year_of_manufacture` : type de propriété - `integer`, titre - `Year of manufacture`, paramètres - `required`, `query` ;
- `color` : type de propriété - `string`, titre - `Color`, paramètres - `required`, `query` ;
- `price` : type de propriété - `number`, titre - `Price of the car`, paramètres - `required`, `query` ;
- `is_manager_exists` : type de propriété - `boolean`, titre - `Is manager exists`, paramètres - `query` ;
- `choosen_manager` : type de propriété - `catalog`, composant - `Transaction Specialists` titre - `Chosen Manager`, paramètres - `query` ;
- `is_archieved` : type de propriété - `string`, paramètres - `query`.

Le composant sera composé des parties suivantes (pages) :

<br>

1. **Page principale**

Pour ajouter une page, vous devez trouver le groupe `Layout` dans le `Toolbox` et faire glisser l'élément `Page` dans l'espace de travail.
Cette page présentera une grille de données avec toutes les voitures disponibles à la vente et des informations générales à leur sujet pour les responsables des ventes. De plus, nous ajouterons un bouton à la page qui redirigera vers un formulaire pour ajouter des voitures à la liste, mais nous l'ajouterons plus tard.

Ajoutez un panneau à l'espace de travail, changez le paramètre d'orientation en vertical, puis ajoutez deux autres panneaux. Dans le panneau inférieur, placez l'élément de la grille de données, et dans le panneau supérieur, ajoutez deux autres panneaux. Dans le panneau de gauche, placez une étiquette et écrivez "Flotte de voitures" dans ses paramètres de "valeur de traduction". Dans le panneau de droite, ajoutez un bouton et écrivez "Ajouter une nouvelle voiture" dans sa "valeur de traduction". Plus tard, nous changerons le paramètre "Actions", mais pour l'instant, vous pouvez changer la taille du bouton dans les paramètres de "Mise en page".

<br>

![Tutoriel 2.7](../assets/images/tutorials/tuto2.7.png)

<br>

Vous pouvez essayer d'autres paramètres.

Ensuite, procédez à la configuration du `data grid` : cliquez sur l'icône d'engrenage et sélectionnez le composant pour la grille de données "Flotte de voitures". Ensuite, à côté des colonnes, cliquez sur `+`, cela ajoutera une colonne à notre grille de données, faites cela 5 fois.

Cliquez sur la première colonne, puis "Ajouter un champ" et sélectionnez la propriété `car_brand`. La configuration ultérieure devrait ressembler à ceci :

<br>

![Tutoriel 2.8](../assets/images/tutorials/tut2.8.png)

<br>

Vous devez configurer les colonnes suivantes de manière similaire dans cet ordre : 2ème colonne - `car_model`, 3ème colonne - `year_of_manufacture`, 4ème colonne - `color`, 5ème colonne - `price`.

De plus, dans les paramètres de la grille de données, définissez `Static filters`. Puisque nous allons afficher des voitures qui n'ont pas encore été assignées à un responsable, définissez le paramètre suivant :

<br>

![Tutoriel 2.12](../assets/images/tutorials/tut2.12.png)

<br>

Le résultat final dans notre espace de travail devrait ressembler à ceci :

<br>

![Tutoriel 2.9](../assets/images/tutorials/tut2.9.png)

<br>

2. **Ajouter une nouvelle voiture**

Cette page sera accessible par l'utilisateur en cliquant sur le bouton "Ajouter une nouvelle voiture" de notre page précédente. Commençons à configurer notre espace de travail.

Ajoutez un panneau à la page. Dans ses paramètres, changez l'orientation de la page en verticale. Ensuite, ajoutez deux autres panneaux. Dans le premier panneau, changez également l'orientation en verticale et transférez nos propriétés pour ressembler à ceci :

<br>

![Tutoriel 2.10](../assets/images/tutorials/tut2.10.png)

<br>

Dans le panneau inférieur, ajoutez deux boutons, définissez leur espacement comme sur le bouton "Ajouter une nouvelle voiture" et nommez-les en conséquence : "Ajouter une nouvelle voiture" et "Retour à toutes les voitures".

Dans les paramètres du bouton "Retour à toutes les voitures", définissez les "Actions" sur "Ouvrir la page" "Page principale". En cliquant sur ce bouton, l'utilisateur sera redirigé vers la page avec la grille de données. Pour le bouton "Ajouter une nouvelle voiture", créez un flux de données, que nous lierons plus tard.

Le flux de données se composera des étapes suivantes : `get action model`, `execute script`, `update entry`, `write response`. Configurons-les.

Dans l'étape `execute script`, créez des variables qui seront utilisées pour les propriétés `is_manager_exists` et `is_archieved` :

```
item["_is_manager_exists@boolean"] = False
item["_is_archieved@boolean"] = False
```

Ensuite, configurez l'étape `Update entry` :

<br>

![Tutoriel 2.13](../assets/images/tutorials/tut2.13.png)

<br>

Ensuite, nous devons mapper nos champs. **N'oubliez pas** que les champs dans les paramètres d'étape sont mappés avec le préfixe data.`property_name`. Pour les propriétés `is_archieved` et `is_manager_exists`, utilisez les valeurs de variable définies dans l'étape de script d'exécution, laissez le champ `chosen_manager` vide :

<br>

![Tutoriel 2.14](../assets/images/tutorials/tut2.14.png)

<br>

**Définissez toujours l'étape source pour chaque étape sauf la première. Cela ne sera pas mentionné plus loin dans la description du tutoriel.**

Maintenant que notre flux de données est complet, nous pouvons le lier au bouton "Ajouter une nouvelle voiture" et enregistrer notre composant. Le résultat final de notre page est montré ci-dessous :

<br>

![Tutoriel 2.15](../assets/images/tutorials/tut2.15.png)

<br>

3. **Nommer un responsable**

Cette page sera appelée comme une fenêtre modale en cliquant sur une entrée particulière dans la grille de données. Elle est conçue pour une fonction unique - assigner un responsable à une voiture particulière. Passons à la configuration de l'espace de travail.
La page elle-même ressemblera à la page "Ajouter une nouvelle voiture", la seule différence étant que nous ajouterons la propriété `chosen_manager` à l'espace de travail, qui sera la seule propriété disponible pour modification. Cela permet au responsable de sélectionner un collègue à qui il transférera la voiture et l'accord. De plus, ajoutez deux boutons, l'un pour fermer la fenêtre modale appelé "Retour à toutes les voitures", et l'autre appelé "Désigner un responsable" qui sera lié à un flux de données que nous créerons plus tard.

**N'oubliez pas d'activer le paramètre Désactivé dans les paramètres de la TextBox pour chaque propriété sauf `chosen_manager`.**

<br>

![Tutoriel 2.16](../assets/images/tutorials/tut2.16.png)

<br>

Le résultat final sur cette page devrait ressembler à celui montré ci-dessous :

<br>

![Tutoriel 2.17](../assets/images/tutorials/tut2.17.png)

<br>

**Passons à la configuration du flux de données**.

Nous devons ajouter les étapes suivantes : `get action model`, `execute script`, `lookup reference`, `update entry`, `write response`.

Dans l'étape `execute script`, nous créerons une variable qui changera la propriété `is_manager_exists` en True, provoquant la disparition de l'entrée nouvellement créée du tableau de données sur la page principale, où nous avons défini des filtres statiques.

```
item["_is_manager_exists@boolean"] = True
```

Ensuite, nous utilisons l'étape `Lookup reference`. Je vous recommande de lire à propos de cette étape dans la section Flux de données de notre documentation technique. L'étape doit être configurée comme indiqué ci-dessous.

<br>

![Tutoriel 2.18](../assets/images/tutorials/tut2.18.png)

<br>

Ensuite, nous configurons l'étape `Update entry`, dans le champ clé du composant spécifiez le nom du champ de l'étape `Lookup reference` :

<br>

![Tutoriel 2.19](../assets/images/tutorials/tut2.19.png)

<br>

Dans 'Mapping des champs', laissez les champs vides sauf pour `chosen_manager` et `is_manager_exists`, ce sont les champs que nous voulons modifier dans l'enregistrement trouvé en utilisant l'étape `Lookup reference`.

<br>

![Tutoriel 2.20](../assets/images/tutorials/tut2.20.png)

<br>

Dans l'étape `write response`, nous devons définir l'étape source.

Attribuez ce flux de données pour être exécuté lorsque le bouton "Désigner un responsable" est pressé. Ensuite, enregistrez le composant.

<br>

**Procédez au script du composant pour construire la fenêtre modale**.

Pour créer une fenêtre modale, vous pouvez utiliser le script ci-dessous. Pour travailler avec le **script du composant**, je vous recommande vivement de lire la section de documentation `Using Python` :

```
def show_model_info(model):
    context.Logger.Error("updated")

def open_custom_modal(sender, model):
    # Creating a modal window template using the GUID of a specific component
    dialog_builder = context.PlatformServices.DialogBuilder('component guid')
    # Setting the title for the modal window and selecting a specific page from the component's settings
    # Also setting the component instance ID to 1, so the first saved instance of component data will be used
    dialog_builder.WithEntryId(int(model[0].Id)).WithTitle("Appoint a manager").WithPageId('page id')
    # Setting the size of the modal window
    dialog_builder.WithVSize("650px").WithHSize("820px")
    dialog_builder.OnComplete(lambda model: show_model_info(model))
    dialog_builder.OnCancel(update_cars_success)
    # Opening the created modal window
    dialog_builder.OpenDialog()
    
def get_datagrid_cars(sender, *args):
    global datagrid_cars
    datagrid_cars = sender
    
def update_cars_success():
    datagrid_cars.Refresh()
```

Les fonctions `get_datagrid_cars` et `update_cars_success` sont utilisées pour mettre à jour automatiquement le tableau de données après une action. Si vous ne les utilisez pas, le tableau de données ne se mettra à jour qu'après avoir rafraîchi la page dans le navigateur. Après avoir copié, vous devez enregistrer le composant et revenir à l'espace de travail sur la "page principale".

Vous devez aller dans les paramètres du tableau de données dans le groupe de paramètres `Events`, et attribuer l'exécution des fonctions à certaines actions sur le tableau de données.

<br>

![Tutoriel 2.21](../assets/images/tutorials/tut2.21.png)

<br>

Enregistrez le composant, puis passez à la configuration de la page suivante.

4. **Entrer dans un contrat**

Cette page est un formulaire qui permet au responsable d'archiver un accord de voiture particulier en changeant le champ `is_archieved` en `True`.

La page est une copie de la page `Appoint a manager`, la seule différence étant que tous les champs ont le paramètre `Disabled` -> `True`. En bas, nous ajouterons deux boutons, dont l'un lancera le flux de données, et l'autre redirigera l'utilisateur vers la page du composant que nous n'avons pas encore créée.

La page elle-même devrait ressembler à ceci :

<br>

![Tutoriel 2.22](../assets/images/tutorials/tut2.22.png)

<br>

Passons à la création et à la configuration du flux de données. Nous aurons besoin de 5 étapes : `get action model`, `execute script`, `update entry`, `form action`, `write response`.

Dans l'étape `execute script`, nous créerons une variable qui définira la valeur `True` dans la propriété `is_archieved`.

```
item["_is_archieved@boolean"] = True
```

La configuration de l'étape `update entry` devrait ressembler à ceci :

<br>

![Tutoriel 2.23](../assets/images/tutorials/tut2.23.png)

<br>
Dans le champ clé du composant, nous fournirons une référence à l'enregistrement que nous souhaitons modifier, puis procéderons à "Mapping des champs". Ici, nous laissons tous les champs vides sauf pour `is_archieved`. Ici, nous mettons la variable que nous avons définie à l'étape `execute script`.

Ensuite, c'est l'étape `Form action`, à laquelle nous reviendrons après avoir créé le composant final. Pour l'instant, enregistrez le composant pour éviter de perdre votre travail.

### Composant "Grille des gestionnaires"

Ce composant consistera en une seule page et nous ne créerons pas de propriétés personnalisées pour cela. Ce composant ne sera utilisé que par les gestionnaires qui y ont accès, leur permettant de voir toutes les voitures qui ont été déplacées à l'étape de l'accord et assignées à un gestionnaire particulier.

Créez une grille de données, liez-la au composant `Car fleet`, et ajoutez une colonne pour chacune de ses propriétés. Le résultat devrait ressembler à ceci :

<br>

![Tutoriel 2.24](../assets/images/tutorials/tut2.24.png)

<br>

Ensuite, allez dans le groupe de paramètres `Actions`, définissez le type de commande sur `Open application`, le composant sur `Car fleet`, la page du composant sur `Enter into a contract`, une page que nous avons créée comme dernière page du composant `Car fleet`.

Ensuite, cliquez sur le bouton `Action parameters` et mappez Id -> Id comme indiqué ci-dessous.

<br>

![Tutoriel 2.25](../assets/images/tutorials/tut2.25.png)

<br>

Enregistrez le composant et allez dans ses paramètres. En plus de nommer et de sélectionner le domaine requis, nous devons cocher la case `Restrict access` afin de pouvoir définir des autorisations de sécurité spéciales pour ce composant.

Enregistrez à nouveau, marquez le composant comme prêt à être publié, et ajoutez-le à `Navigation menu` du domaine que nous utilisons.

<br>

**Retournez au composant `Car fleet` sur la page `Enter into a contract`**

Il reste un bouton inutilisé, `Back to all contracts`, définissons son `Command type` dans le groupe de paramètres `Actions` sur `Navigation back`.

Ensuite, nous devons revenir au flux de données "L'accord est conclu" et terminer la configuration de l'étape `Form action`. La configuration finale de l'étape devrait ressembler à ceci :

<br>

![Tutoriel 2.26](../assets/images/tutorials/tut2.26.png)

<br>

**N'oubliez pas de sélectionner le `source step` dans l'étape `update entry`**.

Enregistrez, publiez le composant, ajoutez-le au lieu de travail en utilisant `Navigation menu` et assurez-vous que tous les composants sont en place.

<br>

### Définir l'accès au composant `Managers grid`

Vous devez aller dans le menu "Accès" dans la section "Permissions" et cliquer sur le bouton "Ajouter" dans le coin supérieur droit.

Une fenêtre de paramètres de permission s'ouvrira sur votre écran, où vous devez spécifier le domaine et donner un nom à la permission. Pour accorder l'accès à manipuler le composant `Managers grid`, allez dans `Permissions`, entrez dans la section `Components`, trouvez notre composant `Managers grid`, et sélectionnez des droits d'accès complets pour celui-ci. Cliquez sur le bouton "Enregistrer" et passez à la section suivante "Rôles".

Ici, vous devez également cliquer sur le bouton "AJOUTER", sélectionner le domaine requis, le nommer, et sélectionner la "Permission" que vous avez créée précédemment. Ensuite, passez à la section `Users`.

Dans la section `Users`, tous les utilisateurs enregistrés dans votre système sont listés. Cliquez sur l'utilisateur auquel vous souhaitez accorder des droits d'utilisation de ce composant, dans "Sélectionner des contextes" choisissez "Plateforme" -> "Système" et dans "Sélectionner des rôles" trouvez le rôle que vous avez créé précédemment, puis cliquez sur la case à cocher et cliquez sur "Enregistrer".

<br>

### Conclusion

Vous avez créé une petite application simple dans laquelle vous avez travaillé avec plusieurs composants et appris à les lier ensemble. Vous avez appris à créer des fenêtres modales et commencé à explorer l'interaction entre les langages de programmation et les outils de notre plateforme.

Essayez de créer plusieurs gestionnaires, d'ajouter de nouvelles voitures à vendre, d'assigner des gestionnaires à celles-ci, et d'essayer de conclure des accords.
Bien sûr, cette application est un test ; elle peut être améliorée et rendue plus complexe indéfiniment. Après l'avoir créée, vous pouvez utiliser d'autres outils par vous-même, construire une logique différente et personnaliser le design à votre goût. La plateforme vous fournit des outils flexibles qui rendent le développement plus passionnant et plus facile !

Les descriptions des outils utilisés dans le tutoriel peuvent être trouvées dans la section "Développement d'Application".