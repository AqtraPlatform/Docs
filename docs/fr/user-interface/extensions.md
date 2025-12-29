# Menu des extensions
<br>

Le menu se compose de 2 blocs :
- **Modèles**
- **Paramètres SMTP**
<br>

## Modèles

Les modèles sont utilisés pour l'envoi de courriels et les notifications utilisateur et ne peuvent être utilisés que dans l'étape « Envoyer une notification modélisée ». Les modèles sont configurés dans la section « Application/Modèles ».
<br>

### Ajout/Suppression de modèles

- Pour **ajouter un nouveau modèle**, cliquez sur le bouton « AJOUTER ».
- Pour **supprimer un modèle**, cliquez sur la croix dans la liste commune de tous les modèles.
<br>

### Configuration du modèle de composant de modèle

Lors de l'ajout ou de la modification d'un modèle, vous devez définir une structure de modèle d'objet qui interagira avec Dataflow et/ou Workflow. Cela se fait en définissant un ensemble de propriétés pour chacun d'eux, similaire à la configuration de tout composant.
<br>

### Personnalisation de la mise en page et du contenu du modèle

La plateforme utilise « DevExpress Report Designer » pour créer des modèles. Ces modèles peuvent être utilisés pour envoyer des notifications ou créer des documents.

- Après avoir créé un nouveau modèle, la fenêtre d'édition s'ouvre. C'est ici que vous pouvez ajouter et personnaliser des éléments visuels à votre modèle, et faire des liens vers les propriétés de votre modèle.
<br>

## Paramètres SMTP

Le service de messagerie est utilisé pour envoyer des notifications via SMTP.

Recommandations pour l'utilisation d'un serveur SMTP :

- **Pendant le développement** : Il est recommandé d'utiliser un serveur SMTP d'entreprise ou des services shareware tels que [sendinblue.com](http://www.sendinblue.com/). Évitez d'utiliser un serveur personnel pour ne pas tomber dans les spams.
- **Pour un usage industriel** : Il est préférable d'utiliser un service SMTP commercial d'entreprise ou payant.

Configurez les paramètres suivants pour le service de messagerie :

| Champ de paramètre | Options de valeur | Objectif |
| ------------------- | ----------------- | --------- |
| `Sender`       | -                 | Nom de l'expéditeur par défaut, par exemple `sender@company.com` |
| `User name`    | -                 | Identifiant pour le serveur SMTP, généralement au format `user@company.com`. |
| `Password`     | -                 | Mot de passe du serveur SMTP |
| `Host`         | -                 | Adresse du serveur SMTP, par exemple `http://smtp-relay.sendinblue.com/` |
| `Port`         | -                 | Le port pour le serveur SMTP dépend du fournisseur, par exemple 587 pour sendinblue.com |
| `Enable SSL`   | `true`, `false`   | Utilisation de SSL pour chiffrer les données. « True » est généralement utilisé pour les serveurs SMTP modernes. |

<br>

### Exemple d'utilisation d'un modèle et de SMTP

1. Créez et personnalisez un modèle.
2. Configurez SMTP pour envoyer des e-mails.
3. Dans votre flux de travail, ajoutez l'étape « Envoyer une notification modélisée ».
4. Sélectionnez le type de notification SMTP et définissez les paramètres pour l'envoi d'e-mails.
5. Choisissez votre modèle et définissez le type de rendu en HTML.

Après avoir complété ces étapes, votre flux de travail enverra un e-mail en utilisant le modèle personnalisé.