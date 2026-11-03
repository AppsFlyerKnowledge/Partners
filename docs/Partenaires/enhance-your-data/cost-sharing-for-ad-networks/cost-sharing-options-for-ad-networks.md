---
title: Options de partage des coûts pour les réseaux publicitaires
metadata:
  keywords:
    - clicks
    - Partner
    - cost
    - Ad Networks
    - Partners
    - ad spend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2020-09-07T13:50:24Z'
  edited_at: '2024-05-26T06:55:49Z'
  id: 360012893658
  locale: fr
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/fr/articles/360012893658
---
> **En bref :** Comparer les méthodes de partage des coûts disponibles pour les partenaires du réseau publicitaire AppsFlyer.

## Partage des coûts avec AppsFlyer et les annonceurs

Les annonceurs utilisent AppsFlyer comme source de référence pour le retour sur investissement (ROI), la facturation et pour prendre des décisions concernant l'allocation du budget marketing. Pour que les réseaux soient visibles, il est indispensable de partager les données relatives aux coûts avec AppsFlyer. Les réseaux sans données sur les coûts apparaissent au bas de la liste du tableau de bord d'AppsFlyer.

Les réseaux publicitaires partagent les coûts avec AppsFlyer en utilisant l'un des moyens suivants : 

* **API InCost**: Envoi de données à AppsFlyer
* **Coût API**: AppsFlyer collecte des données
* **Importation des coûts**: Les fichiers de données de coûts sont téléchargés/envoyés à AppsFlyer
* **Coût par clic :** Les réseaux publicitaires déclarent le coût chaque fois qu'un lien d'attribution est cliqué

### Badge de coût pour les réseaux publicitaires

![CostBadge.jpg](https://files.readme.io/6b660b68b932802f7982a3beb3a155ecc350de1b4cb3baede6e84ef0d704388c-360011247338.jpg)

* Un badge de coût s'affiche dans la <Anchor target="_blank" href="/marketers/fr/docs/partner-integrations#page-partenaire">page de profil du partenaire</Anchor>, mettant en évidence les partenaires utilisant l'API InCost ou Cost.
* Le badge certifie que le partenaire en question sait maîtriser ses coûts.
* Des analyses internes et des enquêtes approfondies auprès des utilisateurs montrent que les annonceurs sont toujours à la recherche de nouveaux partenaires. Ceux qui ont le badge «maîtrise des coûts» sont plus susceptibles de se démarquer, car les annonceurs veulent comprendre leurs performances marketing notamment par l’analyse du retour sur investissement.

### Options de reporting des coûts disponibles pour les réseaux publicitaires

| Option | Se qualifier pour un badge de maîtrise des coûts | Caractéristiques des options |
| --- | --- | --- |
| <Anchor target="_blank" href="/partners/fr/docs/incost-api-for-ad-networks">API InCost</Anchor> | ✓ | Le réseau publicitaire a la pleine responsabilité de décider quand mettre en place le reporting InCost.<br /><br />InCost présente les caractéristiques suivantes :<ul><li>Prise en charge de tous les modèles de coûts</li><li>Précision et fiabilité</li><li>De manière entièrement automatisée</li><li>Contrôles des partenaires des réseaux publicitaires :<ul><li>Schéma de téléchargement des données</li><li>À quelle fréquence télécharger (taux de fraîcheur des données)</li></ul></li><li>Dans le dashboard d'AppsFlyer, l'annonceur autorise le partenaire à télécharger les données relatives aux coûts.</li></ul>**Limitation**:<br /><br />Les comptes d'agence AppsFlyer ne sont pas pris en charge. |
| Coût API | ✓ | <ul><li>Prise en charge de tous les modèles de coûts</li><li>Précision</li><li>Le partenaire conserve un certain contrôle sur ses données relatives aux coûts dans AppsFlyer</li><li>Prise en charge des coûts pour les comptes d'agence dans AppsFlyer</li><li>Les annonceurs fournissent leurs identifiants en tant que partenaires dans le tableau de bord d'AppsFlyer.</li><li>Taux de rafraîchissement des données : 6 fois par jour, toutes les quatre heures</li></ul>**Limitation**:<br /><br />L'intégration est soumise au système de priorité d'AppsFlyer. |
| <Anchor target="_blank" href="/partners/fr/docs/cost-import-for-ad-networks">Importation des coûts</Anchor><br /><br />(téléchargement de fichiers) | Non | <ul><li>Le partenaire du réseau publicitaire :<ul><li>a la possibilité de charger manuellement des données s'il ne dispose pas des ressources techniques nécessaires à l'automatisation ;</li><li>contrôle le moment où les données sont téléchargées ;</li><li>conserve un certain contrôle sur ses données de coûts dans AppsFlyer</li><li>L'intégration se fait par application. Dans le dashboard d'AppsFlyer, l'annonceur autorise le partenaire à télécharger les données relatives aux coûts.</li><li>La correspondance avec les données d'attribution est basée sur le nom de la campagne (et non sur l'identifiant de la campagne).</li></ul></li></ul>**Limitation**:<ul><li>Les comptes d'agence AppsFlyer ne sont pas pris en charge</li><li>Risque d'échec si le téléchargement est automatisé via e-mail</li></ul> |
| <Anchor target="_blank" href="/partners/fr/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Coût par clic</Anchor><br /><br />(sur la ligne d'attributionk) | Non | <ul><li>Solution rapide pour les campagnes CPI</li><li>Presque en temps réel</li><li>Le coût par clic (CPC) peut être moins précis si l'annonceur utilise SKAdNetwork.</li></ul>**Les limites** :<ul><li>Limité au modèle de coût du CPI</li><li>Si des données erronées sont envoyées sur le lien, elles ne peuvent pas être modifiées rétroactivement.</li><li>Le reciblage n'est pas pris en charge</li><li>Les coûts rapportés par clic sont affichés dans le tableau de bord de SKAdNework quand ils sont disponibles.</li></ul> |

<div data-zendesk-anchors="sharing-cost-with-appsflyer-and-advertisers=partage-des-co%C3%BBts-avec-appsflyer-et-les-annonceurs h_01HN0A1ER3MNZM508ZCG9KP26P=partage-des-co%C3%BBts-avec-appsflyer-et-les-annonceurs cost-badge-for-ad-networks=badge-de-co%C3%BBt-pour-les-r%C3%A9seaux-publicitaires h_01HN0A1ER4K1V4479W5SXCEC30=badge-de-co%C3%BBt-pour-les-r%C3%A9seaux-publicitaires reporting-cost-options-available-to-ad-networks=options-de-reporting-des-co%C3%BBts-disponibles-pour-les-r%C3%A9seaux-publicitaires h_01HN0A1ER4Y128ZHJERXS6A8ET=options-de-reporting-des-co%C3%BBts-disponibles-pour-les-r%C3%A9seaux-publicitaires" />
