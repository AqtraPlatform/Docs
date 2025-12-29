# Paramètres de base de la plateforme

<br>

## Architecture de la plateforme

La plateforme est construite sur une architecture de microservices qui offre modularité, évolutivité et flexibilité. Les principales caractéristiques de l'architecture incluent :

- **Architecture de microservices** : Le système est divisé en microservices distincts, chacun effectuant une fonction spécifique et opérant de manière indépendante.
- **Traitement distribué** : Les microservices peuvent être répartis sur différents nœuds, offrant un équilibrage de charge et une résilience accrue du système.
- **Containerisation et orchestration** : L'utilisation de Docker pour containeriser les microservices et de Kubernetes pour les orchestrer facilite le déploiement, l'évolutivité et la gestion de l'application.
- **Modularité et interopérabilité des microservices** : La modularité est atteinte en délimitant clairement les fonctions entre les microservices, et la communication entre eux se fait via des API spécifiques et des protocoles d'interopérabilité.

Le système se compose de onze images de conteneurs Docker :

| Service         | Objectif                                                        |
| --------------- | --------------------------------------------------------------- |
| catalogs        | Stockage et traitement des données utilisateur ; support RLS    |
| data-flow       | Traitement et stockage de scripts de données personnalisés      |
| file-storage    | Stockage de données binaires                                     |
| identity        | Gestion des utilisateurs et authentification                     |
| notification    | Envoi de notifications                                          |
| scheduler       | Planificateur d'événements dans le système ; tous les événements sont appelés via le bus |
| template-service | Travail avec des modèles                                        |
| view-service    | Stockage des métadonnées système ; orchestration des processus de mise à jour des métadonnées |
| workflow        | Scripting via la machine à états                                |
| web-studio      | Partie web de développement d'applications                      |
| web-workplace    | Partie web pour l'exécution d'applications                     |

<br>

## Pile technologique

- **Fondation** : La plateforme est construite sur Net Core 8.0, une plateforme de développement logiciel modulaire et open-source.
- **Langage de développement** : C# est utilisé comme principal langage de programmation.
  <br>

## Infrastructure supplémentaire

- **PostgreSQL** (version ≥13.0) : Système de gestion de base de données objet-relationnelle pour le stockage principal des données.
- **Redis** (version ≥5.0) : Base de données non relationnelle utilisée pour la mise en cache des données.
- **RabbitMQ** (version ≥3.0) : Un courtier de messages logiciel pour la gestion des événements et des files d'attente du système.
  <br>

## Parties Web

- Utilise le framework web front-end **Blazor**, partie de Net Core, pour créer des composants web.
- Les parties web sont exécutées en tant que **WebAssembly** (WASM) côté client.
  <br>

## Exigences d'installation

- **Kubernetes** : Un cluster Kubernetes est requis pour que la version clusterisée du produit fonctionne.
  - **Configuration minimale** :
    - 1 x Master (2 vCPU, 4 Go de RAM, 20 Go SSD) - 3 nœuds avec le rôle Master sont recommandés.
    - 1 x Ingress (4 vCPU, 8 Go de RAM, 20 Go SSD)
    - 3 x Worker (16 vCPU, 32 Go de RAM, 60 Go SSD)
- **Système d'exploitation** : Ubuntu Server 22.04 LTS
  <br>

## Réseautage et ports

- Tout le trafic réseau utilise le protocole **TCP/IP**.
- Par défaut, chaque microservice (sauf web-studio) fournit deux ports :
  - **80** : API publique (HTTP/1.1).
  - **5001** : API privée (HTTP/2).
- **Web-studio** : Fournit uniquement le port 80 pour servir des ressources statiques.
- Tous les microservices, à l'exception de web-studio, doivent avoir accès à PostgreSQL, Redis et RabbitMQ.
  <br>

## Protocoles utilisés

- **HTTP/1.1** : Pour l'API publique.
- **GRPC** : Pour l'API privée.
- **WebSocket** : Pour le service de notification.
- **SIP sur WebSocket** : Optionnel, pour l'intégration avec SIP dans un web-workplace.
- **RTC/RTCP** : Optionnel, pour l'intégration avec SIP dans un web-workplace.
  <br>

## Stockage des données

Chaque microservice gère son propre schéma dans la base de données, sans chevauchement avec les autres.

| Service          | Schéma                    |
| ---------------- | ------------------------- |
| catalogs         | catalogs                  |
| data-flow        | dataflow                  |
| file-storage     | file_storage              |
| identity         | identity                  |
| notification     | notification              |
| scheduler        | scheduler                 |
| template-service | template                  |
| view-service     | view_service, maintenance |
| workflow         | workflow, wfc_persistence |
| web-workplace    | workplace-host            |

<br>

Chaque microservice est responsable de la création et de la migration des métadonnées de ses schémas.

Le service catalogs, qui est responsable du stockage des données utilisateur, crée une partition supplémentaire dans son schéma pour chaque type de données, héritée de la table principale, ainsi que des partitions supplémentaires pour mettre en œuvre RLS si nécessaire. Lorsque ces partitions sont formées, tous les index supplémentaires et les clés externes sont générés.

La composition des index et des clés externes dépend de la configuration de l'application que vous construisez sur la plateforme.
<br>

## Gestion des autorisations et des permissions

- Autorisation locale utilisant des **tokens JWT**.
- Possibilité de connecter des systèmes d'autorisation externes (oAuth, OpenId Connect, autorisation Windows, SAML).
- **RBAC** (Contrôle d'accès basé sur les rôles) pour le contrôle d'accès.
  <br>

## Collecte de métriques et de traces

Tous les services, sauf web-studio, fournissent des métriques au format ‘Prometheus’. Les métriques sont disponibles par le chemin relatif /metrics. Pour vérifier la disponibilité du service, deux chemins sont fournis /hc et /liveness :

- hc - informations détaillées sur tous les contrôles ;
- liveness - une réponse courte sur la disponibilité du service.

Les journaux sont collectés par le système lui-même, tous les journaux sont écrits dans le schéma de maintenance, et la visualisation des journaux est disponible dans le web-studio.
Le niveau de journalisation pour chaque service est configuré séparément via le web-studio, dans la section "Maintenance".
Deux systèmes Zipkin ou Jaeger peuvent être connectés pour collecter des traces. La collecte de traces est configurée au niveau des paramètres du service. Si vous souhaitez exporter des traces vers Jaeger, vous devez avoir au moins la version 1.35.