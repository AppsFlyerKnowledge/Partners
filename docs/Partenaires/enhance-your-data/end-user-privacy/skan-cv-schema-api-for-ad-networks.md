---
title: API de schéma de la valeur de conversion SKAN pour les réseaux publicitaires
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2023-03-05T14:41:18Z'
  id: 11705009866001
  locale: fr
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/fr/articles/11705009866001
---
> **En bref** : pour afficher le schéma de la valeur de conversion SKAN tel qu'il est mappé par l'annonceur.

<div id="skan-cv-schema-api-for-ad-networks" />

## API de schéma de la valeur de conversion SKAN pour les réseaux publicitaires

L'attribution SKAdNetwork (SKAN) permet aux annonceurs d'évaluer la qualité de l'utilisateur en fixant des valeurs de conversion (CV) basées sur l'activité de ce dernier après l'installation et pendant des périodes spécifiques (fenêtres). <Anchor target="_blank" href="/marketers/fr/docs/skadnetwork-skan-solution-guide">En savoir plus sur SKAN</Anchor>

iOS renvoie la CV via des postbacks envoyés au réseau publicitaire qui place la publicité. À partir d'iOS 15, les annonceurs peuvent également demander à iOS d'envoyer les postbacks directement à AppsFlyer.

Cette API fournit aux réseaux publicitaires la carte *CV-to-attribution-events-and-values*. Elle permet aux réseaux publicitaires de décoder les postbacks qu'ils reçoivent.

L'API renvoie un fichier JSON imbriqué. Chaque app possède un schéma distinct. Les mappages par CV sont contenus dans le tableau conversion\_value\_mapping.

Pour utiliser l'API, demandez à votre développeur de suivre <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">les instructions de la section API de schéma de la valeur de conversion SKAN pour les réseaux publicitaires</Anchor>. Pour obtenir une liste des touches clavier et leur description, cliquez sur 200 dans le simulateur.

**Remarque** :

* La gamme de valeurs de conversion est la suivante :
  * Valeur précise de la fenêtre 1 de SKAN 4 : 0-63.
  * Valeur approximative des fenêtres 1, 2 et 3 de SKAN 4 : faible, moyenne, ou élevée.
  * SKAN 3 et moins : 0-63
* Les annonceurs peuvent modifier le mappage des CV à tout moment.
* Vous (le réseau publicitaire) devez interroger cette API quotidiennement afin de vous assurer que votre schéma est à jour.

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=api-de-sch%C3%A9ma-de-la-valeur-de-conversion-skan-pour-les-r%C3%A9seaux-publicitaires" />
