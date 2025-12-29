# Rendre le modèle

![](../../assets/images/app-development/render-template.png)

## Informations générales
L'étape "Rendre le modèle" est utilisée pour créer des documents, en particulier au format PDF, en utilisant des données provenant de Dataflow et des modèles disponibles dans le système. Cette étape permet de convertir des données en documents conçus de manière professionnelle, ce qui est largement utilisé dans la génération de rapports, de contrats, de factures et d'autres documents officiels.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre | Options de valeur  | Objectif |
|---------------------|--------------------|----------|
| Nom de l'étape      | -                  | Nom de l'étape |
| Étape source        | -                  | Sélection à partir des étapes précédentes pour la source de données |
| Modèle              | -                  | Sélection parmi les modèles disponibles pour créer un document |
| Type de rendu       | texte, HTML, Docx, Xlsx, PDF | Format du document à générer |
| Nom de fichier      | -                  | Nom du fichier généré |
| Mappage des champs  | -                  | Mappage des champs entre un modèle et un modèle de données |

## Cas d'utilisation
- **Génération de documents formalisés** : Particulièrement utile pour la génération automatisée de documents officiels tels que des rapports, des factures et des contrats, en appliquant des modèles prédéfinis.
- **Personnalisation du contenu** : Permet de créer des documents personnalisés pour les clients ou les utilisateurs en utilisant des données spécifiques à chaque cas, telles que des offres personnalisées ou des rapports sur mesure.
- **Préparation à la distribution de documents** : Utilisé pour créer des documents qui peuvent ensuite être mis à la disposition des utilisateurs pour téléchargement ou envoyés par e-mail.

## Exceptions
- **Exigence de qualité et d'exactitude des modèles** : La qualité des documents résultants est directement liée à l'exactitude et au professionnalisme des modèles utilisés.
- **Nécessité de suivi pour distribuer des documents** : Une fois qu'un document est généré, une étape de suivi, telle que "Action de formulaire" avec l'option "Télécharger le fichier", est souvent requise pour rendre le document disponible aux utilisateurs.

## Scénario d'application

Ce composant utilise plusieurs étapes pour créer et télécharger un fichier PDF. Tout d'abord, le modèle de données est récupéré, puis le modèle PDF est rendu. L'étape d'action de formulaire est configurée pour télécharger le fichier, en spécifiant le champ de données contenant les informations sur le fichier. Après l'étape Écrire la réponse, le fichier généré est envoyé au frontend pour téléchargement.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1Omst72osc9qf1FtxQcIohdARDzqwDKHT/view?usp=sharing).