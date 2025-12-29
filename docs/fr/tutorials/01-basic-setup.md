# Tutoriel №1

<br>

## Création de votre première application — Inventaire des factures

<br>

**Description de l'application : Inventaire des factures**

Nous allons créer une application simple qui vous permet d'ajouter, de visualiser et de modifier des factures.

Chaque facture contiendra les données suivantes (voir le tableau ci-dessous).

| Brève description    | Description détaillée                                         |
| -------------------- | ------------------------------------------------------------ |
| Numéro de facture     | Numéro attribué à la facture par le fournisseur.              |
| Titre de la facture   | Description de l'élément de la facture.                      |
| Montant total de la facture | Nombre indiquant le montant d'argent facturé dans la facture. |
| Date d'échéance de la facture | Date à laquelle la facture doit être payée.                    |

<br>

De plus, nous suivrons le statut de la facture comme suit (voir le tableau ci-dessous).

| ID  | Titre lisible       | Description                                                                          |
| --- | -------------------- | ------------------------------------------------------------------------------------ |
| 0   | En cours d'examen   | Assigné immédiatement lors de la création de la facture.                            |
| 1   | Accepté pour paiement | Assigné après l'examen de la facture et l'approbation pour le paiement.            |
| 2   | Rejeté              | Assigné après la fin de l'examen, mais la facture n'est pas acceptée pour paiement. |
| 3   | Payé                | Assigné après que la facture a été payée.                                          |
| 4   | En retard           | Indique que la facture est impayée et que la date d'échéance est passée.           |

<br>

La version de base de l'application aura 2 écrans principaux.

- Une liste de toutes les factures dans le système, qui peut être filtrée et/ou triée en utilisant tous les champs de facture décrits ci-dessus. Nous l'appellerons « Toutes les factures ».
- Un écran pour ajouter une nouvelle facture ou modifier une facture existante. Nous l'appellerons « Modifier/Voir la facture ».

Après la création, l'application ressemblera à la capture d'écran ci-dessous.

<br>

![Tutoriel 1](../assets/images/tutorials/tut1.png)

<br>

## Ouverture de Studio

La création d'une application sur la plateforme commence par l'ouverture de Studio et l'ajout d'un composant.

Vous pouvez ouvrir Studio en utilisant le lien https://<your_hosting_name>/studio/.

Par exemple, si le nom de domaine où vous avez déployé votre instance de la plateforme est [my.platform.io](http://my.platform.io/), vous pouvez accéder à Studio en utilisant l'URL suivante : “[https://my.platform.io/studio/”](https://my.platform.io/studio/%E2%80%9D).

Après vous être connecté à Studio, vous verrez l'écran suivant avec un menu à gauche listant Accueil, Applications et Accès. Sélectionnez Applications→Composants.

<br>

![Tutoriel 2](../assets/images/tutorials/tut2.png)

<br>

Vous verrez une liste de tous les composants existants. Cliquez sur le bouton « Ajouter » et sélectionnez l'option « Composant », comme indiqué ci-dessous.

<br>

![Tutoriel 3](../assets/images/tutorials/tut3.png)

<br>

Félicitations, vous avez maintenant votre premier composant ! Nommez-le « Inventaire des factures » et définissez quelques paramètres importants.

Pour nommer votre composant, cliquez sur le bouton « Paramètres » puis saisissez « Inventaire des factures » dans le champ « Nom ».

Puisque notre application ne sera accessible qu'aux personnes disposant des identifiants de connexion appropriés, nous devons nous assurer que le champ « Mode d'accès » est défini sur « Privé ».

## Configuration des champs de données requis

Cliquez sur Enregistrer pour vous assurer que votre composant est enregistré. Un message d'erreur s'affichera car nous n'avons pas encore de données dans notre composant. Ajoutons quelques données.
Allez à l'onglet "Définition" et cliquez sur le signe "+" à côté de "Inventaire des factures". La plateforme ajoutera automatiquement plusieurs champs système que vous voyez dans la capture d'écran, ainsi que votre premier champ de données — Property_1.

<br>

![Tutoriel 4](../assets/images/tutorials/tut4.png)

<br>

Cliquez sur l'icône de modification (crayon) sur Property_1. Vous verrez un nouveau panneau s'ouvrir à droite. C'est ici que vous définissez comment vos champs de données doivent être interprétés par le système.
Name — c'est le nom interne du système pour votre champ de données (propriété). Il ne doit contenir que des lettres anglaises, sans espaces. Vous utiliserez ce nom plus tard, par exemple, dans des scripts Python pour ajouter une logique avancée à l'application.

_Note : à partir de la version 0.4.x, il existe également une propriété système “name” qui est automatiquement ajoutée lorsque la première propriété est créée et est utilisée lorsque vous devez montrer aux utilisateurs des valeurs pour les utilisateurs lors de l'utilisation des propriétés de type Catalog (lien vers un autre composant ; utilisé pour les relations 1:1 et M:1) ou Array (lien vers un tableau d'autres composants ; utilisé pour les relations 1:M et M:M). Contrairement au nom interne du système qui est présent pour chaque propriété au sein du composant, le nom du champ système est unique pour l'ensemble du composant._

Title — c'est ainsi que votre champ de données sera nommé dans l'interface utilisateur. Ici, vous pouvez utiliser tous les caractères dont vous avez besoin.

Pour les champs de données qui doivent toujours être non vides, assurez-vous que la case “Required” est cochée.

Le type de propriété vous permet de sélectionner l'un des types de champs de données disponibles.

Pour commencer, nous allons ajouter le champ de données Nom de la Facture, et définir le type de propriété sur String. Étant donné que les noms de factures proviennent théoriquement de fournisseurs externes, ils peuvent se répéter, donc nous ne définissons pas le drapeau de clé primaire ici.

<br>

![Tutorial 5](../assets/images/tutorials/tut5.png)

<br>

Une fois que nous avons terminé de configurer notre premier champ, cliquons sur Enregistrer.

Maintenant, ajoutons les autres champs dont nous aurons besoin dans notre application : numéro de facture, date d'échéance de la facture, montant total de la facture et statut de la facture.

**Numéro de Facture** est le numéro de compte interne de chaque facture unique, qui correspond généralement au nom de la facture, mais nous veillerons à ce qu'il ait au moins 2 caractères en définissant la valeur de longueur minimale à 2, comme indiqué ci-dessous. Il doit également être unique pour distinguer les différentes factures, même si elles ont les mêmes noms, donc nous définissons le drapeau de clé primaire. Cela indique à la plateforme qu'il ne peut pas y avoir plus d'une propriété Numéro de Facture avec la même valeur. Si une tentative est faite pour créer une valeur dupliquée, le système renverra une erreur.

<br>

![Tutorial 6](../assets/images/tutorials/tut6.png)

<br>

Pour la date d'échéance de la facture attendue, définissez le type de propriété sur DateTime.

<br>

![Tutorial 7](../assets/images/tutorials/tut7.png)

<br>

Le montant total de la facture doit être défini comme un nombre. Nous allons également définir le champ de valeur minimale à 0 pour garantir qu'il n'y a pas de factures négatives (cela pourrait être différent dans une application financière réelle où des valeurs négatives sont utilisées, par exemple, pour représenter des crédits de fournisseurs).

<br>

![Tutorial 8](../assets/images/tutorials/tut8.png)

<br>

Enfin, nous allons ajouter le champ “Statut de la Facture”. Comme indiqué dans la description de l'application, ce sera un ensemble de statuts qui devrait ressembler à ceci :

0|En Révision  
1|Accepté pour Paiement  
2|Rejeté  
3|Payé  
4|En Retard  

Pour cela, nous devons définir le type de propriété sur Integer (à partir de la version 0.5.24 et supérieure) et cocher la case Enum. Ensuite, nous devons ajouter tous les statuts disponibles au format <Number>|<Name>, comme indiqué ci-dessous.

<br>

![Tutorial 9](../assets/images/tutorials/tut9.png)

<br>

Cliquez sur “Enregistrer”. Vous devriez voir le modèle de données entièrement configuré, comme indiqué ci-dessous.

<br>

![Tutorial 10](../assets/images/tutorials/tut10.png)

<br>

## Configuration de l'Interface pour Notre Application

Maintenant, nous devons configurer l'interface utilisateur pour notre application. Comme décrit ci-dessus, nous aurons besoin de 2 écrans :

1. Un écran pour ajouter une nouvelle facture ou modifier une facture existante. Nous l'appellerons “Ajouter/Voir Facture”.
2. Une liste de toutes les factures dans le système, qui peut être filtrée et/ou triée en utilisant tous les champs de facture décrits ci-dessus. Nous l'appellerons “Toutes les Factures”.

## Configuration de la Page Ajouter/Voir Facture

Nous avons déjà une page par défaut ajoutée automatiquement appelée “Page Principale” ci-dessus.

Dans la version actuelle de la plateforme, la première page du composant est utilisée par défaut comme un formulaire pour visualiser et modifier les données du composant lorsqu'il n'y a pas de formulaire explicite pour visualiser et modifier. Par exemple, dans notre cas, le contrôle UI Data Grid que nous utiliserons pour la page Toutes les Factures ouvrira par défaut la première page de notre composant.
Nous utiliserons également la première page pour le formulaire de visualisation et d'édition de notre facture, et pour cela, nous la renommerons de Page principale à Ajouter/Visualiser les factures. Pour ce faire, cliquez sur Page principale, et changez le nom dans la boîte de dialogue qui s'ouvre (champs Nom et Titre).

Le résultat ressemblera à ce qui est montré ci-dessous.

<br>

![Tutorial 11](../assets/images/tutorials/tut11.png)

<br>

Ensuite, pour créer la vue des données et le formulaire d'édition, faites glisser les champs de données (propriétés) de la gauche vers la zone du milieu dans le même ordre que dans la grille de données montrée ci-dessus.

Les résultats devraient ressembler à ceci.

<br>

![Tutorial 12](../assets/images/tutorials/tut12.png)

<br>

Cliquez sur le bouton Enregistrer. Maintenant, ajoutons une page pour visualiser toutes les factures.

## Configuration de la page Toutes les factures

Pour ce faire, ouvrez les Composants UI dans le panneau de droite, sélectionnez Mise en page, cliquez sur Page, et faites-la glisser dans la zone du milieu juste au-dessus de notre formulaire de visualisation des factures. Une page nommée Nouvelle page 1 devrait être ajoutée automatiquement, comme montré ci-dessous.

<br>

![Tutorial 13](../assets/images/tutorials/tut13.png)

<br>

Allez à la Nouvelle page 1 en cliquant sur le bouton du même nom, et renommez-la en Toutes les factures.

Cliquez sur Enregistrer. Dans la liste des Composants UI à droite, sélectionnez Mise en page, puis sélectionnez Page et faites-la glisser dans la zone du milieu. Ensuite, allez à la section Avancé et faites glisser l'élément DataGrid dans le panneau nouvellement créé. Vous verrez le résultat comme montré ci-dessous.

<br>

![Tutorial 15](../assets/images/tutorials/tut15.png)

<br>

Cliquez sur l'icône Paramètres (engrenage) dans le coin supérieur droit du nouvel élément DataGrid et sélectionnez Commun dans le panneau de droite. Vous verrez la sélection du composant pour afficher des données dans cette grille de données. Sélectionnez Inventaire des factures.

<br>

![Tutorial 16](../assets/images/tutorials/tut16.png)

<br>

Ensuite, sélectionnez l'icône “+” à côté de l'étiquette “Colonnes” 5 fois (puisque nous avons 5 champs de données que nous voulons afficher ici).

<br>

![Tutorial 17](../assets/images/tutorials/tut17.png)

<br>

Maintenant, pour chaque colonne, cliquez sur la zone de la colonne. Une nouvelle boîte de dialogue apparaîtra pour configurer la colonne.

Pour chaque colonne, vous devrez définir l'en-tête avec le nom de la colonne (par exemple, “Numéro de facture,” “Nom de la facture,” etc.).

Vous devez également définir l'option “Afficher l'en-tête” sur “Activé.”

Si les options “Triable” et/ou “Filtrable” sont définies sur “Activé,” vous activerez le tri et le filtrage dynamiques (similaire à ce qui se fait dans Excel, par exemple).

Enfin, vous devez cliquer sur le bouton “Ajouter un champ” et sélectionner le champ de données approprié à afficher dans cette colonne.

L'exemple ci-dessous montre la configuration pour le champ “Numéro de facture.” Les autres colonnes sont configurées de manière similaire.

<br>

![Tutorial 18](../assets/images/tutorials/tut18.png)

<br>

Après avoir configuré toutes les colonnes, allez à Actions sur le formulaire à droite et assurez-vous que l'option “Afficher le bouton d'ajout” est sélectionnée. Cela permettra d'ajouter de nouvelles factures via ce DataGrid.

De plus, définissez le Type de commande sur “Modifier l'enregistrement” afin que nous puissions visualiser/éditer toute facture dans la liste en cliquant dessus.

Voir l'illustration ci-dessous pour les résultats.

<br>

![Tutorial 19](../assets/images/tutorials/tut19.png)

<br>

Cliquez sur le bouton Enregistrer.

## Ajout de boutons d'action et flux de données pour enregistrer les données

Après avoir créé les vues de données et les formulaires d'édition, nous devons ajouter une logique pour enregistrer les données du formulaire dans la base de données et permettre aux utilisateurs de l'activer.

Pour ce faire, nous devons faire deux choses.

1. Ajouter des boutons que nous utiliserons soit pour enregistrer les données du formulaire, soit pour annuler tous les changements et revenir à la liste de toutes les factures.
2. Pour enregistrer les données du formulaire, nous ajouterons un flux de travail simple qui prendra les données du formulaire et les enregistrera dans la base de données.

<br>

## Ajouter des boutons Enregistrer et Retour à toutes les factures

<br>

Cliquez sur “Boîte à outils”, sélectionnez le champ “Bouton” dans la section “De base”, et faites glisser le bouton dans la zone du milieu de l'écran. Définissez le titre du bouton sur Enregistrer. Pour ce faire, allez à la section Commune, et dans le champ Valeur de traduction, écrivez Enregistrer.

Ajoutez un autre bouton et définissez le titre sur “Retour à toutes les factures.” Le résultat devrait ressembler à l'image ci-dessous.

<br>

![Tutorial 20](../assets/images/tutorials/tut20.png)

<br>
Maintenant, nous allons faire en sorte que le bouton “Retour à toutes les factures” change l'interface utilisateur pour l'onglet principal “Toutes les factures”. Pour ce faire, dans le menu Paramètres pour le bouton du bas, sélectionnez “Actions” et définissez le “Type de commande” sur “Ouvrir la page” et la “Page du composant” sur “Toutes les factures.” Cliquez sur Enregistrer.

<br>

![Tutoriel 21](../assets/images/tutorials/tut21.png)

<br>

## Ajout d'un flux de données pour l'enregistrement

Pour que le bouton Enregistrer dans l'application enregistre les données saisies en tant que facture, nous devons ajouter un flux de données.

Cliquez sur “Boîte à outils”, sélectionnez le champ “Flux de données” dans la section “Flux”, et faites-le glisser vers la zone centrale de l'écran. Un nouveau flux de données avec le nom par défaut “Flux de données 1” apparaîtra, accessible via le bouton du même nom dans le menu des paramètres du composant principal, à droite du bouton Flux de données d'entrée. Cliquez sur le bouton Flux de données 1 et renommez votre flux de données en Enregistrer.

Le résultat devrait ressembler à ceci.

<br>

![Tutoriel 22](../assets/images/tutorials/tut22.png)

<br>

Ensuite, cliquez sur le bouton "+ AJOUTER UNE ÉTAPE", puis "Ajouter une étape" et sélectionnez l'étape "Obtenir le modèle d'action". Ajoutez une autre étape et sélectionnez "Mettre à jour l'entrée", puis allez dans les paramètres de cette étape. Vous pouvez en savoir plus sur cette étape dans la section "Flux de données". Configurez l'étape comme indiqué ci-dessous :

<br>

![Tutoriel 23](../assets/images/tutorials/tut23.png)

<br>

![Tutoriel 24](../assets/images/tutorials/tut24.png)

<br>

Ensuite, ajoutez l'étape "Écrire la réponse", spécifiez l'étape source dans ses paramètres, et enregistrez le composant.

Après cela, dans le menu Paramètres pour le bouton Enregistrer, sélectionnez Actions et définissez le Type de commande sur Exécuter le flux de données, et choisissez votre nouvel Enregistrer dans la liste.

Cliquez sur le bouton Enregistrer. Le résultat devrait ressembler à ceci.

<br>

![Tutoriel 25](../assets/images/tutorials/tut25.png)

<br>

Cliquez sur Enregistrer et Prêt à publier. Votre nouveau composant est créé et prêt à être publié.

<br>

## Publication et test de votre application

Vous êtes maintenant prêt à publier et tester votre application.

Pour publier votre application, cliquez sur le bouton Prêt à publier à l'intérieur de votre composant, puis allez à Studio→Applications→Publication. Sélectionnez votre composant Inventaire de factures dans la liste des composants disponibles pour publication, et cliquez sur le bouton Publier.

Vous pouvez ensuite utiliser le bouton Voir l'application à l'intérieur de votre Studio (pas toujours disponible), ou aller à l'URL <your-host-name> pour voir votre application en action.

Remplissez les détails de la facture et cliquez sur Enregistrer. Ensuite, cliquez sur le bouton “Retour à toutes les factures”. Votre première facture sera enregistrée, et vous verrez la liste de toutes les factures disponibles.