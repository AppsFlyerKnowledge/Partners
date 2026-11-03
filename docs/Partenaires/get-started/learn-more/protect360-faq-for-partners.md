---
title: Protect360 - FAQ à l’attention des partenaires
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2023-06-12T12:43:34Z'
  edited_at: '2024-10-23T12:46:49Z'
  id: 16091549732497
  locale: fr
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/fr/articles/16091549732497
---
> **En bref :** Trouvez les réponses aux questions que les partenaires posent le plus par rapport à Protect360.

## Anomalies au niveau des clics/impressions

<div id="why-are-impressionsclicks-being-capped" />

<Accordion title="Pourquoi les impressions/clics sont-ils plafonnés ?">

Le système Protect360 AppsFlyer prend en compte plusieurs paramètres lorsqu'il définit le plafonnement des engagements publicitaires, ce qui inclut entre autres : le volume des impressions/clics, le CVR, le taux d'anomalies détectées, les fluctuations normales de l'activité, ainsi que les standards que ce soit en termes d’activité ou de géo. L'algorithme est dynamique et mis à jour toutes les heures, afin de tenir compte de l'évolution des tendances.

Une fois le mécanisme de plafonnement déclenché, Protect360 bloque les impressions ou les clics du réseau publicitaire pour le cycle de 24 heures en cours pour l'application concernée. Cela signifie que les impressions/clics qui se produisent une fois le plafond atteint ne sont pas enregistrés par AppsFlyer, et ils ne sont pas pris en compte pour l'attribution.

Un réseau peut éviter de dépasser ce plafond en arrêtant les campagnes et les éditeurs dont le nombre d'engagements publicitaires est anormalement élevé et qu’il n’impacte pas les résultats.

Nous vous recommandons de parcourir ces articles :  
<Anchor target="_blank" href="/partners/fr/docs/protect360-for-integrated-partners#impression-capping">Plafonnement des impressions et des clics</Anchor>  
<Anchor target="_blank" href="/partners/fr/docs/protect360-for-integrated-partners#faq">FAQ sur le plafonnement</Anchor>

</Accordion>

<div id="i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client" />

<Accordion title="Pourquoi ai-je un problème de plafonnement des clics avec une app, alors que je ne travaille pas avec le client ?">

Ce scénario indique probablement que votre PID a été manipulé par un tiers afin de contourner vos propres résultats de mesure. A titre préventif, AppsFlyer propose une solution de "signature des clics" pour vérifier que chaque clic portant votre PID est bien issu de vous.

Vous pouvez transmettre l'article "<Anchor target="_blank" href="/partners/fr/docs/click-signing-for-ad-networks">Signature des clics pour les réseaux publicitaires</Anchor>" à votre équipe afin d'explorer les possibilités de mise en œuvre. En attendant, indiquez au chatbot de votre tableau de bord d'ouvrir un dossier, et notre équipe vous guidera à travers les étapes.

</Accordion>

<div id="the-number-of-capped-clicks-is-very-small-why-does-such-a-small-amount-trigger-click-capping" />

<Accordion title="Le nombre de clics plafonnés est très faible. Pourquoi un nombre aussi bas déclenche-t-il le plafonnement des clics ?">

Le nombre de "clics plafonnés" affiché sur le tableau de bord Protect360 n'est pas l'élément qui déclenche le plafonnement. Il indique plutôt le nombre de clics qui vont être ignorés pour l'attribution dans le cycle du plafonnement.

De même, les clics (et les performances liées) examinés par le mécanisme de plafonnement représentent ce qui s'est passé avant le déclenchement du mécanisme.

Nous vous recommandons de lire ces articles sur le <Anchor target="_blank" href="/partners/fr/docs/protect360-for-integrated-partners#impression-capping">plafonnement des impressions et des clics</Anchor>.

</Accordion>

<div id="the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate" />

<Accordion title="Pourquoi les installations sont-elles bloquées en raison d’un click flooding, alors que le taux de conversion est élevé ?">

Nos algorithmes de click flooding se lancent à différents intervalles au cours de la journée, et chaque fois que le seuil est franchi (sur la base de paramètres et d'un procédé internes), les engagements publicitaires de l'éditeur se retrouvent non éligibles pour l'attribution.

**Remarque :** Certains de nos algorithmes de click flooding fonctionnent pour plusieurs applications, ce qui fait que les anomalies issues de sources frauduleuses identiques sont également reconnues pour d'autres applications promues.

Nous vous recommandons de lire : <Anchor target="_blank" href="https://www.appsflyer.com/glossary/click-flooding/">Qu'est-ce que le click flooding ?</Anchor>

</Accordion>

## Anomalies au niveau des installations / évènements in-app

<div id="why-was-my-test-install-rejected-from-attribution" />

<Accordion title="Pourquoi mon installation de test est-elle rejetée des attributions ?">

La détection anti-fraude AppsFlyer applique différents procédés de protection à de multiples niveaux,comme les installations uniques et les ensembles d'installations. Les ensembles sont examinés sous différentes formes : par éditeur, par source média, par application, etc. L'activité frauduleuse est vérifiée à l'aide de différents algorithmes statistiques et d'algorithmes de machine learning qui considèrent chaque ensemble comme un tout. Ainsi, si un ensemble est jugé frauduleux à cause d’un résultat trop élevé, toutes les installations de cet ensemble sont considérées comme frauduleuses. Une des techniques bien connue des fraudeurs consiste à mélanger quelques installations légitimes à un grand nombre d'activités frauduleuses dans l'espoir que la fraude sera suffisamment "diluée" pour ne pas déclencher de blocage.

Par défaut, toutes les installations entrantes sont considérées comme trafic LIVE - par conséquent, pour vous assurer que votre installation de test n'est pas classée dans les algorithmes Protect360, vous devez suivre les étapes mentionnées dans <Anchor target="_blank" href="/marketers/fr/docs/registering-test-devices">cet article</Anchor> pour enregistrer votre appareil comme appareil de test avant d'effectuer un test.

</Accordion>

<div id="What-detection-methods-are-used-to-detect-install-rejections" />

<Accordion title="Quelles méthodes de détection sont utilisées pour repérer les rejets d'installation ?">

Pour mieux comprendre, veuillez consulter le "sous motif de fraude" associé au rejet. Ces données sont également disponibles dans les rapports Protect360 et dans le tableau de bord Protect360, sous réserve de l'accès accordé par l'annonceur concerné.

Nous vous recommandons de lire cet article sur les <Anchor target="_blank" href="/marketers/fr/docs/protect360-raw-data-reports#motifs-de-blocage">motifs de blocage de Protect360</Anchor>.

</Accordion>

## Affichage et compréhension des données Protect360

<div id="how-do-i-gain-visibility-into-the-protect360-results" />

<Accordion title="Comment puis-je consulter les résultats de Protect360 ?">

Vous pouvez afficher les résultats de nos actions de détection à l'aide du tableau de bord Protect360 et des rapports de données brutes, sous réserve de l'accès accordé par l'annonceur concerné.

Nous vous recommandons de parcourir ces articles :  
<Anchor target="_blank" href="/marketers/fr/docs/protect360-dashboard">Tableau de bord Protect360</Anchor>  
<Anchor target="_blank" href="/marketers/fr/docs/protect360-raw-data-reports#obtenir-des-rapports-de-données-brutes">Données brutes Protect360</Anchor>

</Accordion>

<div id="how-can-i-get-notified-in-realtime-about-blocked-traffic" />

<Accordion title="Comment être notifié en temps réel d'un trafic bloqué ?">

AppsFlyer fournit aux réseaux publicitaires des postbacks d'attribution refusée pour chaque installation que Protect360 rejette de l'attribution.

Vous pouvez activer le "postback de rejet" en ajoutant des paramètres de "postback de rejet" à votre template de postback en passant par la <Anchor target="_blank" href="/partners/fr/docs/self-serve-integration-management-for-ad-networks">gestion de l'intégration.</Anchor>

</Accordion>

<div id="why-do-i-see-spikes-in-postattribution-detections" />

<Accordion title="Pourquoi y a-t-il des pics dans les détections post-attribution ?">

La détection en temps réel avant l'attribution et la détection après l'attribution participent du procédé de détection d'anomalies Protect360 AppsFlyer, qui fonctionne à différents moments.

Par rapport à la détection en temps réel, la détection post-attribution s'appuie davantage sur des pointeurs de données collectés après l'installation. Si des anomalies sont alors détectées, Protect360 enregistre les activités anormales et les affiche dans la catégorie post-attribution.

Compte tenu de ce qui précède, certaines méthodes de détection (timestamp\_anomalies, behavioral\_anomalies, etc.) sont plus susceptibles d'être détectées en post-attribution qu'en temps réel, car les données ne sont pas concluantes pour une installation propre, mais gagnent en importance lorsqu'elles sont analysées dans le cadre de leur distribution.

En savoir plus sur la <Anchor target="_blank" href="/marketers/fr/docs/protect360-anti-fraud-guide#postattribution-detection">détection post-attribution</Anchor>.

</Accordion>

<div data-zendesk-anchors="click-impression-level-anomalies=anomalies-au-niveau-des-clicsimpressions 01H8GKS08Y22PX2SBTW5ME02C4=anomalies-au-niveau-des-clicsimpressions 01H8GKS08YXVK4CPNW9TX9XBYN=why-are-impressionsclicks-being-capped i%E2%80%99m-facing-a-click-capping-issue-with-an-app-but-i%E2%80%99m-not-working-with-this-client=i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client 01H8GKS08Y3G46SFASMJRFETXR=i-m-facing-a-click-capping-issue-with-an-app-but-i-m-not-working-with-this-client 01H8GKS08ZGM2QXBNNQCFRC007=the-number-of-capped-clicks-is-very-small-why-does-such-a-small-amount-trigger-click-capping 01H8GKS08ZGNTMNZ5JH846T9Q9=the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate install-inapp-event-level-anomalies=anomalies-au-niveau-des-installations--%C3%A9v%C3%A8nements-in-app 01H8GKS08ZRA7YT9FWJNBBSV4Q=anomalies-au-niveau-des-installations--%C3%A9v%C3%A8nements-in-app 01H8GKS08Z2M0RTMR4GM1BJE7G=why-was-my-test-install-rejected-from-attribution What-detection-methods-are-used-to-detect-install-rejections%3F=What-detection-methods-are-used-to-detect-install-rejections 01H8H30KARRPAPT9XRREDYKHVT=What-detection-methods-are-used-to-detect-install-rejections protect360-data-visibility-and-understanding=affichage-et-compr%C3%A9hension-des-donn%C3%A9es-protect360 01H8GKS08ZX2W1G0K165H96N4Z=affichage-et-compr%C3%A9hension-des-donn%C3%A9es-protect360 01H8GKS08ZGEEK0HQVCRD546MW=how-do-i-gain-visibility-into-the-protect360-results 01H8GKS08ZC6SB4PT53JG5QKHG=how-can-i-get-notified-in-realtime-about-blocked-traffic 01H8GKS08Z673WG6C6JGW31F42=why-do-i-see-spikes-in-postattribution-detections" />
