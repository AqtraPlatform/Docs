# Exporter vers un fichier

![](../../assets/images/app-development/export-to-file.png)

## Informations générales
L'étape "Exporter vers un fichier" est utilisée pour exporter des données du modèle Dataflow interne vers un fichier structuré. Cette étape prend en charge la création de fichiers aux formats CSV, Excel et JSON, vous permettant de transférer et de distribuer efficacement les données traitées.

## Paramètres
**Paramètres de l'étape :**

| Champ de paramètre       | Options de valeur | Objectif |
|--------------------------|-------------------|----------|
| Nom de l'étape           | -                 | Nom de l'étape |
| Étape source             | -                 | Sélection à partir des étapes précédentes pour la source de données |
| Type de fichier de sortie | Csv, Excel, JSON  | Format du fichier d'exportation |
| Nom de fichier           | -                 | Nom du fichier d'exportation |
| Séparateur de colonnes   | ; (par défaut)    | Séparateur de fichier CSV (par défaut ";") |
| Nom de la feuille (Si le type de fichier d'entrée = Excel) | - | Nom de la feuille dans le fichier Excel |
| Mappage des champs       | -                 | Mappage des champs du modèle Dataflow et de la structure du fichier |

## Cas d'utilisation
- **Distribution de données** : Idéal pour créer des rapports, distribuer des informations aux clients ou partenaires, et transférer des données entre différents systèmes ou départements.
- **Archivage de données** : Peut être utilisé pour stocker des informations importantes dans un format structuré et facilement accessible.
- **Intégration avec d'autres systèmes** : Permet de préparer des données pour une intégration ou un traitement ultérieur par d'autres systèmes qui prennent en charge les formats CSV, Excel ou JSON.

## Exceptions
- **Compatibilité des formats de fichier** : Il est important d'affiner les paramètres d'exportation pour garantir que les fichiers générés sont compatibles avec les attentes et les exigences des utilisateurs finaux ou des systèmes.
- **Optimisation des performances pour de grands volumes de données** : Lors de l'exportation de grands volumes de données, il est nécessaire de prendre en compte les performances et les éventuelles restrictions de taille de fichier (par défaut 1 Mo).

## Scénario d'application

Le composant créé sert d'outil pour exporter des données du système. Il comprend plusieurs étapes telles que la récupération du modèle de données, le filtrage et l'exportation vers un fichier Excel. L'utilisateur peut personnaliser le filtrage des données avant l'exportation et télécharger les résultats dans un format pratique à l'aide du bouton sur l'interface utilisateur.

- Vous pouvez télécharger la configuration du composant [ici](https://drive.google.com/file/d/1haTgN7Qyu6rD3GSYcDKPEMu3V_KcOdVt/view?usp=sharing).