---
title: ROI360 pour les partenaires UA
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2023-08-12T17:09:08Z'
  edited_at: '2023-09-26T14:07:30Z'
  id: 17735150011921
  locale: fr
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/fr/articles/17735150011921
---
> **En bref** : AppsFlyer fournit aux partenaires UA des données détaillées sur les publicités, achats in-app et abonnements auto-renouvelables via des rapports et postbacks. Les partenaires peuvent utiliser ces informations pour optimiser les campagnes UA.

## Introduction

AppsFlyer reçoit des informations sur les revenus à la fois de ses partenaires et des app stores (Apple App Store et Google Play Store). Une fois reçues, les données sont traitées via différentes étapes : validation, normalisation, attribution et enrichissement avec des propriétés et dimensions supplémentaires.  AppsFlyer peut envoyer les informations au partenaire UA. À l'issue du processus, AppsFlyer transmet les données enrichies et attribuées au partenaire UA. Le partenaire UA peut alors utiliser ces éléments pour optimiser ses campagnes UA et améliorer le service qu'il propose aux annonceurs.

<div id="what-revenue-types-are-reported-to-the-partners" />

<Accordion title="Quels sont les types de revenus transmis aux partenaires ?">

Les applications créent deux types de revenus :

* **Revenus publicitaires :** les revenus publicitaires sont générés chaque fois qu'une publicité s'affiche dans l'application, comme une bannière, publicité interstitielle ou autre format publicitaire. Ils peuvent être calculés quelle que soit la méthode de campagne facturée à un annonceur.
* **Achat in-app et abonnement à renouvellement automatique :** les revenus du store sont générés chaque fois qu'un achat in-app ou une transaction liée à un abonnement a lieu.

</Accordion>

<div id="how-does-appsflyer-provide-revenue-signals-to-ua-partners" />

<Accordion title="Comment AppsFlyer fournit les infos liées aux revenus aux partenaires UA ?">

AppsFlyer fournit à ses partenaires des infos sur les publicités in-app, les achats in-app et les revenus d'abonnement par les moyens suivants :

* **Rapport sur les infos UA des revenus publicitaires (Revenue UA Signals)** : ce rapport contient les événements liés aux revenus publicitaires agrégés au niveau de l'appareil. Le rapport est disponible quotidiennement dans Data Locker, il contient les données de la veille.
* **Postbacks de revenus publicitaires** : chaque fois qu'une impression publicitaire a lieu sur l'appareil d'un client, un postback est envoyé par AppsFlyer au partenaire, avec les détails de l'événement de revenu publicitaire.
* **Postbacks de revenus du store** : chaque fois qu'un achat ou un abonnement a lieu, un postback est envoyé par AppsFlyer au partenaire, avec les détails de l'événement de revenu.

</Accordion>

## Mettre en place ROI360 pour les partenaires

Quelles actions doivent effectuer les partenaires pour recevoir le rapport sur les infos UA et les postbacks de revenus du store ?

<div id="how-to-subscribe-to-the-roi360-ua-signals-report" />

<Accordion title="Abonnement au rapport ROI360 UA Signals">

Pour permettre au partenaire d'obtenir le rapport via Data Locker :

* Le partenaire doit compléter les étapes suivantes dans Data Locker :
  1. Configurer <Anchor target="_blank" href="/partners/fr/docs/data-locker-for-partners#set-up-data-locker">Data Locker</Anchor> dans le compte du partenaire, ce qui inclut la connexion au fournisseur de services sur le cloud, ainsi que le format et le contenu des rapports.
  2. <Anchor target="_blank" href="/partners/fr/docs/ad-revenue-signals-for-ua-ad-networks#enable-the-ad-revenue-report">Activer le rapport ROI360 UA Signals</Anchor>.
* L'annonceur doit <Anchor target="_blank" href="/marketers/fr/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">donner au partenaire l'autorisation de publier le rapport</Anchor>.

</Accordion>

<div id="how-to-receive-roi360-postbacks-from-appsflyer" />

<Accordion title="Recevoir les postbacks ROI360 envoyés par AppsFlyer">

Pour recevoir les postbacks AppsFlyer, les partenaires doivent contacter l'équipe intégration des partenaires AppsFlyer. Par la suite, l'équipe configurera les valeurs de postback du revenu in-app du ROI au sein de la plateforme AppsFlyer.

Pour contacter l'assistance des partenaires AppsFlyer, ouvrez le menu **Assistance** de votre tableau de bord et sélectionnez **Contacter notre équipe**.

[![alt](https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif)](https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif)

</Accordion>

## Rapport ROI360 UA Signals pour les réseaux UA

Le rapport envoie quotidiennement des données CSV/parquet détaillées sur les revenus au jour x+1 au compartiment S3 du partenaire UA.Chaque enregistrement est une agrégation des événements de revenus publicitaires au niveau de l'appareil.

Le rapport UA Signals ne fournit pas de données en temps réel comme le font les rapports sur les revenus publicitaires. Cependant, il est plus précis et plus complet. En effet, la valeur d'une impression peut varier dans le temps. Cela est particulièrement vrai lorsque les données de revenus au niveau de l'impression concernent une impression publicitaire qui a été vendue via une enchère CPM standard, et non une enchère en temps réel.

<div id="what-are-the-report-data-sources" />

<Accordion title="Quelles sont les sources de données du rapport ?">

Selon le type d'intégration de l'annonceur, les données du rapport peuvent provenir de l'une des sources suivantes :

1. Intégration des <Anchor target="_blank" href="/marketers/fr/docs/integrate-the-roi360-ad-revenue-sdk-api">connecteurs SDK AdRevenue</Anchor> : les clients peuvent partager les données de revenus de niveau impression chargées par le partenaire sur les appareils clients, qui sont ensuite transmises à AppsFlyer en temps quasi réel.
2. Intégrations de niveau appareil basées sur API S2S : les clients peuvent configurer leurs identifiants partenaires dans l'interface utilisateur AppsFlyer (section partenaires intégrés) et permettre à ROI360 ad revenue de collecter les données de revenus publicitaires de niveau appareil en leur nom.
3. Un ensemble des deux (actualisation et précision).

   **Remarque :** le transfert des données entre l'annonceur et AppsFlyer dépend des autorisations de l'annonceur et du fait que l'annonceur est un client avancé de ROI360 ou non.

</Accordion>

<div id="what-data-processing-is-performed-on-the-report-data" />

<Accordion title="Comment sont traitées les données du rapport ?">

AppsFlyer ROI360 Ad Revenue effectue les opérations suivantes :

1. Normalisation des données
2. Attribution de la source média d'installation et enrichissement des données
3. Génération des événements de revenus publicitaires
4. Les événements sont agrégés au niveau de l'appareil

</Accordion>

<div id="how-is-the-report-data-delivered" />

<Accordion title="Comment les données du rapport sont-elles transmises ?">

Les données de niveau appareil sont inscrites quotidiennement dans le rapport de Data Locker.

</Accordion>

<div id="what-is-the-report-data-freshness" />

<Accordion title="Comment sont actualisées les données du rapport ?">

Les données sont inscrites quotidiennement dans le dossier h=23 de votre compartiment Data Locker à 21:00 <Anchor target="_blank" href="/marketers/fr/docs/about-data-freshness-and-timezone-support#daily">UTC</Anchor>.

</Accordion>

<div id="what-are-the-report-fields" />

<Accordion title="Quels champs contient le rapport ?">

| **Champ** | **Remarques** |
| --- | --- |
| Version | Horodatage Unix en secondes. Exemple : 1661315124 |
| app\_id | ID de l'app sur la plateforme AppsFlyer |
| install\_time | <ul><li>Horodatage de l'installation : AAAA-MM-JJ HH:MM:SS Exemple : 2020-08-16 11:22:33 - Pour les appareils iOS 14+ et les utilisateurs qui n'ont ps donné leur consentement, ou si l'annonceur a activé la fonction Confidentialité avancée, l'heure de l'installation est arrondie à l'heure la plus proche.</li></ul> |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Uniquement renseigné si l'UA est attribuée au partenaire qui reçoit les données. |
| idfa, idfv, advertising\_id | • Le même ID d'appareil, comme IDFA, IDFV ou advertiser\_id, peut s'afficher sur plusieurs lignes s'il y a plusieurs événements de monétisation des revenus publicitaires. • Pour les appareils iOS 14+ et les utilisateurs non consentants, ou si l'annonceur a activé la fonction Confidentialité avancée, ce message ne s'affiche pas. |
| platform | Plate-forme de l'appareil : iOS, Android ou Windows Mobile |
| country | Code pays utilisant la norme [ISO 3166 (alpha-2)](https://www.iso.org/iso-3166-country-codes.html) Exemple : US, CN. |
| original\_url | • Pour les appareils iOS 14+ et les utilisateurs non consentants, ou si l'annonceur a activé la fonction Confidentialité avancée, ce message ne s'affiche pas.• Renseigné uniquement si l'UA est attribuée au partenaire qui reçoit les données. |
| mediation\_network | Le réseau de médiation associé à l'impression ou aux impressions. <Anchor target="_blank" href="/marketers/fr/docs/roi360-guide-ad-revenue-attribution#closed-beta--ua-signals-for-ad-networks">Voir la liste des réseaux possibles</Anchor> |
| ad\_unit | Disponible au troisième trimestre 2023 : le ad\_unit de monétisation associé à l'impression ou aux impressions |
| placement | Disponible au troisième trimestre 2023 : le placement de monétisation associé à l'impression ou aux impressions |

</Accordion>

<div id="download-the-report-data-sample" />

<Accordion title="Télécharger l'exemple de données de rapport">

[Cliquez pour télécharger le rapport.](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv)

</Accordion>

## Postbacks de revenus publicitaires in-app (IAA)

Les postbacks IAA représentent la deuxième méthode utilisée par AppsFlyer pour envoyer des informations sur les revenus à ses partenaires. Leur principal avantage comparé aux rapports Ad Revenue Signals UA est leur degré d'actualisation, en effet les postbacks offrent un partage des données sur les revenus des AAI en temps quasi réel. Cela contraste avec l'actualisation X+1 (un jour après la date de l'événement) offerte par les rapports ad revenue UA signals.

Cependant, l'actualisation en temps réel est moins précise qu'avec X+1 :

* Les données en temps réel des postbacks IAA sont en moyenne moins précises de ±5 % que les données du rapport X+1 des UA Signals.
* Les données en temps réel des postbacks IAA sont en moyenne moins détaillées de ±7 % comparées aux données du rapport X+1 des UA Signals.

<div id="what-are-the-iaa-postback-data-sources" />

<Accordion title="Quelles sont les sources de données des postback IAA?">

Les données des postbacks IAA proviennent des données de niveau impression que les partenaires chargent sur les appareils des clients. Ces données sont ensuite partagées avec AppsFlyer par le biais du connecteur ROI360 Ad Revenue SDK, qui est installé sur l'appareil par l'annonceur. Le connecteur permet au développeur de l'app de signaler un événement d'impression qui comprend certains paramètres, comme l'ILRD, la devise, la plateforme de médiation et la source de monétisation.

Le transfert des données entre les appareils du client annonceur et AppsFlyer dépend des autorisations de l'annonceur et du fait que l'annonceur est un client avancé de ROI360 ou non.

</Accordion>

<div id="what-processing-is-performed-on-the-iaa-postback-data" />

<Accordion title="Comment sont traitées les données des postbacks IAA ?">

AppsFlyer ROI360 suit les étapes ci-dessous pour chaque donnée reçue au niveau de l'impression :

1. Normalisation des données.
2. Attribution de la source média d'installation et enrichissement des données.
3. Génération d'un événement **af\_ad\_revenue**.

</Accordion>

<div id="how-is-the-postback-data-delivered" />

<Accordion title="Comment les données du postback sont-elles transmises ?">

L'événement est envoyé au partenaire via la configuration de postback définie entre le partenaire et AppsFlyer par le biais d'un paramètre supplémentaire.

</Accordion>

## Postbacks des achats in-app (IAP)

Les postbacks ROI360 des achats in-app offrent différents niveaux d'informations en validant d'abord chaque transaction, en supprimant les doublons, puis en déduisant les frais du store et la taxe commerciale.

<div id="what-are-the-iap-postback-data-sources" />

<Accordion title="Quelles sont les sources de données des postback IAA?">

Les données des postbacks IAP proviennent :

1. Des données de niveau transaction lues par le connecteur ROI360 Purchase SDK à chaque fois qu'un achat in-app ou un abonnement auto-renouvelable se produit sur l'appareil.
2. Toutes les **notifications entrantes du serveur App Store et Google Play (RTDN)** sont traitées par le même processus que celui des achats et revenus d'abonnement d'AppsFlyer.
   * Les notifications concernant les transactions déjà rapportées par le connecteur SDK sont validées et traitées.
   * Les notifications concernant des transactions inconnues ne sont pas indiquées dans AppsFlyer.

   **Remarque :** le transfert des données entre l'annonceur et AppsFlyer dépend des autorisations de l'annonceur et du fait que l'annonceur est un client avancé de ROI360 ou non.

</Accordion>

<div id="what-data-processing-is-performed-on-the-iap-postback-data" />

<Accordion title="Comment sont traitées les données des postbacks IAP ?">

AppsFlyer ROI360 suit les étapes ci-dessous pour chaque donnée reçue au niveau de la transaction :

1. AppsFlyer **valide l'achat ou l'abonnement auprès du store concerné** pour confirmer qu'il n'est pas frauduleux.
   * Lorsque la vérification est validée, AppsFlyer enregistre l'achat ou l'abonnement.
   * Si la vérification échoue, l'événement s'affiche dans le rapport de données brutes des événements in-app bloqués (option disponible pour les abonnés Protect360).
2. AppsFlyer veille à ce que les transactions ne soient pas dupliquées, y compris celles liées au partage familial sur iOS.
3. AppsFlyer calcule les données de revenu net en tenant compte des frais du store et des taxes **(Revenu réel**).
4. AppsFlyer génère un achat en interne ou un événement de cycle de vie pour la transaction validée et traitée.

</Accordion>

<div id="how-is-the-postback-delivered" />

<Accordion title="Comment est transmis le postback ?">

L'événement IAP est envoyé au partenaire via une intégration de postbacks définie entre le partenaire et AppsFlyer.

</Accordion>

<div id="what-are-the-iap-events" />

<Accordion title="Quels sont les événements IAP ?">

Les clients ROI360 peuvent partager les noms d'événements générateurs de revenus suivants :

**Noms d'événement**

| **Nom de l'événement** | **Description** |
| --- | --- |
| af\_purchase | Enregistré lorsqu'un utilisateur effectue un achat |
| af\_purchase\_refund | Enregistré lorsqu'un achat est remboursé |
| af\_ars\_trial\_converted | Enregistré lorsqu'un renouvellement au tarif plein commence, après une période d'essai |
| af\_ars\_subscription\_started | Enregistré lorsqu'un abonnement à tarif réduit ou plein commence |
| af\_ars\_subscription\_resumed | Enregistré lorsqu'un abonnement à tarif plein est relancé après un abandon ou une demande de remboursement d'abonnement |
| af\_ars\_subscription\_refunded | Enregistré lorsqu'un abonné perçoit un remboursement |
| af\_ars\_subscription\_renewed | Enregistré lors d'un renouvellement automatique de l'abonnement |
| af\_ars\_subscription\_xgraded | Enregistré lorsqu'un abonné passe à un abonnement supérieur ou inférieur, ou qu'il change d'abonnement |

</Accordion>

<div data-zendesk-anchors="01H7T1DS6SNC7X8GX4DGXT4GC0=introduction 01H7T1DS6TYHE3A4XWBDNHCFCZ=what-revenue-types-are-reported-to-the-partners 01H7T1DS6T82RWQ4BBWNPQ6BT2=how-does-appsflyer-provide-revenue-signals-to-ua-partners set-up-roi360-for-partners=mettre-en-place-roi360-pour-les-partenaires 01H7T1DS6TDA8CX1ZF3GGE4EHB=mettre-en-place-roi360-pour-les-partenaires 01H7T1DS6T0QFB6K6R78PMVVB2=how-to-subscribe-to-the-roi360-ua-signals-report 01H7T1DS6TBNJBBR6M98RTVMFF=how-to-receive-roi360-postbacks-from-appsflyer roi360-ua-signals-report-for-ua-networks=rapport-roi360-ua-signals-pour-les-r%C3%A9seaux-ua 01H7T1DS6T93844DMZY744ECQE=rapport-roi360-ua-signals-pour-les-r%C3%A9seaux-ua 01H7T1DS6T4AF6GTETE6HZMYF7=what-are-the-report-data-sources 01H7T1DS6TDNTYDY4JF70F40SV=what-data-processing-is-performed-on-the-report-data 01H7T1DS6T94V4674AMNVCD4T6=how-is-the-report-data-delivered 01H7T1DS6T4F0QV5VE8XZVV1RY=what-is-the-report-data-freshness 01H7T1DS6TYER08FGK9GDKHFEG=what-are-the-report-fields 01H7T1DS6TH98NT4KGKPR7DRDM=download-the-report-data-sample inapp-ad-revenue-iaa-postbacks=postbacks-de-revenus-publicitaires-in-app-iaa 01H7T1DS6T0CN30EC97VARN80D=postbacks-de-revenus-publicitaires-in-app-iaa 01H7T1DS6TCA8338NAD9Q8CJWW=what-are-the-iaa-postback-data-sources 01H7T1DS6TQ2G43HSQMH8Y6Q4H=what-processing-is-performed-on-the-iaa-postback-data 01H7T1DS6TQZA3W9KE3783G9G1=how-is-the-postback-data-delivered inapp-purchase-iap-postbacks=postbacks-des-achats-in-app-iap 01H7T1DS6TH8AV2ZTY3M8ZXPYA=postbacks-des-achats-in-app-iap 01H7T1DS6TGF4XEMD4CRBD8QS2=what-are-the-iap-postback-data-sources 01H7T1DS6T9W85F40QQ2497RNW=what-data-processing-is-performed-on-the-iap-postback-data 01H7T1DS6VAPRMCGZ9YCPTA9EQ=how-is-the-postback-delivered 01H7T1DS6VKE2G6XR02VF4TWH4=what-are-the-iap-events" />
