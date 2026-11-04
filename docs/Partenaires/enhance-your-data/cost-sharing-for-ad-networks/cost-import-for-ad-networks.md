---
title: Importation des coûts pour les réseaux publicitaires
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Gray
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2019-10-20T06:03:13Z'
  edited_at: '2024-05-22T09:13:32Z'
  id: 360002868097
  locale: fr
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/fr/articles/360002868097
---
> **En bref :** Découvrez comment les réseaux publicitaires peuvent signaler les coûts de campagne de l'annonceur directement à AppsFlyer via des fichiers CSV.

<div id="cost-import-for-ad-networks" />

## Importation des coûts pour les réseaux publicitaires

![AdspendIngestion.jpg](https://files.readme.io/e870005c5f20531a2d06cc78b47a82a8a1f730f2c04728f5d0a5674c1c70129a-24507313816337.jpg)

<div id="overview" />

#### Introduction

* Préparez un fichier CSV contenant les détails des dépenses publicitaires comme suit :
  * Date de la dépense
  * ID d'application (plusieurs applications autorisées par fichier si les applications appartiennent au même propriétaire)
  * Source multimédia (une source par fichier autorisée)
  * Nom de la campagne
  * Montant dépensé
  * [Optionnel] Géolocalisation
  * [Optionnel] Devise (USD par défaut)
* Envoyez le fichier à AppsFlyer par e-mail/téléchargement de fichier à l'aide du compte de réseau publicitaire dans AppsFlyer.   
  **Remarque :**
  * Avant de soumettre des fichiers pour la première fois, l'annonceur doit vous accorder, à vous, la régie publicitaire, l'autorisation d'importation des coûts. Cela doit être fait une fois pour chaque application. C’est un processus très rapide.
  * Une fois qu'un fichier est téléchargé, il ne peut plus être annulé.
* Surveillez et vérifiez qu'aucune erreur n'a été trouvée dans le fichier.

<div id="submitting-ad-spend-files-for-ad-networks" />

### Envoi de fichiers de dépenses publicitaires pour les réseaux publicitaires

* Utilisez la méthode de téléchargement ou la méthode par e-mail pour ingérer les fichiers de dépenses publicitaires.
* [Bonne pratique] Utilisez d’abord la méthode de téléchargement car elle est plus facile pour résoudre les problèmes de formatage du CSV.

<div id="submission-by-file-upload" />

#### Envoi par téléchargement (upload) du fichier

**Pour soumettre des fichiers d'importation de coûts par téléchargement :**

1. [Pour chaque application avec laquelle vous travaillez, vous devez effectuer cette action une seule fois] <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#granting-an-ad-network-ingestion-permission">Demandez à l'annonceur de vous accorder la permission d'importer les coûts</Anchor>.
2. <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#csv-file-format-and-schema">Préparez le fichier CSV en utilisant ce format et ce schéma spécifiques</Anchor>.
3. Cliquez ici pour <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">vous connecter à votre compte de réseau publicitaire AppsFlyer.</Anchor>
4. <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#uploading-ad-spend-files">Téléchargez et ingérez le fichier</Anchor>.
5. Dans le tableau de bord AppsFlyer, surveillez l'ingestion :

   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#status-indicators">Statut</Anchor>
   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#row-matching-and-the-unmatched-report">Lignes comparées</Anchor>
   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#ad-spend-ingestion-actions">Actions d'importation de coûts</Anchor>
6. Procédures supplémentaires :
   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#overwrite-correct-previously-ingested-ad-spend">Écraser l'ingestion précédente</Anchor>
   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#ad-spend-ingestion-actions">Revenir (annuler)</Anchor>

<div id="submission-by-email" />

#### Envoi par email

**Pour soumettre des fichiers d'importations de coûts par email :**

1. [Pour chaque application avec laquelle vous travaillez, vous devez effectuer cette action une seule fois] <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#granting-an-ad-network-ingestion-permission">Demandez à l'annonceur de vous accorder la permission d'importer les coûts</Anchor>.
2. <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#csv-file-format-and-schema">Préparez le fichier CSV en utilisant ce format et ce schéma spécifiques</Anchor>.
3. Si vous n'avez pas de token d'importation de coûts (vous en aurez besoin lorsque vous enverrez le fichier par e-mail):
   * Cliquez ici pour <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">vous connecter à votre compte de réseau publicitaire AppsFlyer</Anchor>.
   * Afficher le token de dépense publicitaire (Ad Spend) Remarque : Le même token est utilisé pour tous les annonceurs.
4. Soumettre le dossier par<Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#sending-ad-spend-files-by-email">Email</Anchor>
5. AppsFlyer envoie par e-mail un rapport de statut ; il indique si l'ingestion a réussi ou si des problèmes ont été détectés. **Remarque** : Si le courrier de statut n'a pas été reçu, voyez <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#after-emailing-the-ad-spend-files-no-status-email-is-received">ici.</Anchor>
6. Dans le tableau de bord AppsFlyer, surveillez l'ingestion :

   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#status-indicators">Statut</Anchor>
   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#row-matching-and-the-unmatched-report">Lignes comparées</Anchor>
   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#ad-spend-ingestion-actions">Actions d'importation de coûts</Anchor>
7. Procédures supplémentaires :
   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#overwrite-correct-previously-ingested-ad-spend">Écraser l'ingestion précédente</Anchor>
   * <Anchor target="_blank" href="/marketers/fr/docs/import-cost-data#ad-spend-ingestion-actions">Revenir (annuler)</Anchor>

<div data-zendesk-anchors="ad-spend-ingestion-for-ad-networks=importation-des-co%C3%BBts-pour-les-r%C3%A9seaux-publicitaires h_01HX94WSX07YEG40X66TMRFJGA=importation-des-co%C3%BBts-pour-les-r%C3%A9seaux-publicitaires overview=introduction h_01HX94WSX0HR2KTGRT7MQ481Y6=introduction submitting-ad-spend-files-for-ad-networks=envoi-de-fichiers-de-d%C3%A9penses-publicitaires-pour-les-r%C3%A9seaux-publicitaires h_01HX94WSX0G429FTHKYCG07BB9=envoi-de-fichiers-de-d%C3%A9penses-publicitaires-pour-les-r%C3%A9seaux-publicitaires submission-by-file-upload=envoi-par-t%C3%A9l%C3%A9chargement-upload-du-fichier h_01HX94WSX0ENTJEDMXWRHDCP0D=envoi-par-t%C3%A9l%C3%A9chargement-upload-du-fichier submission-by-email=envoi-par-email h_01HX94WSX0HVTMFQQ0NMW0VSKP=envoi-par-email" />
