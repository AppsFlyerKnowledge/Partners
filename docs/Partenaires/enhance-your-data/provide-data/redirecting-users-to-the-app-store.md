---
title: Redirection des utilisateurs vers l'app store
metadata:
  keywords:
    - clicks
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2018-04-30T08:08:25Z'
  edited_at: '2024-08-15T14:34:34Z'
  id: 360000807629
  locale: fr
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/fr/articles/360000807629
---
> **En bref :** Découvrez les options permettant de rediriger les utilisateurs vers l'app store après la diffusion d'une publicité, et comment envoyer les données d'engagement à AppsFlyer.

<div id="overview" />

## Présentation

AppsFlyer reçoit des données d'engagement (clics et impressions) pour l'attribution de plusieurs façons :

* L'utilisateur **clique sur** l'annonce et est [redirigé vers AppsFlyer](#utilisateurs-redirigés-via-appsflyer), puis vers l’app store.
* L'utilisateur **clique sur l'** annonce **ou la consulte** et est [directement redirigé vers l’app store](#utilisateurs-envoyés-directement-par-le-réseau-publicitaire), tandis que **le lien d'attribution est envoyé à AppsFlyer à partir de l'appareil.**

Dans les deux cas, la <Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters">structure et les paramètres habituels des liens d'attribution</Anchor> sont utilisés.

<div id="note" />

> 📘 **Remarque**
>
> Pour les SRN, les données sont reçues via des API spécialisées.

<div id="users-redirected-via-appsflyer" />

## Utilisateurs redirigés via AppsFlyer

Lorsqu'il clique sur une publicité, l'utilisateur est dirigé vers AppsFlyer, qui le redirige ensuite vers l’app store selon le flux suivant :

1. L'utilisateur est redirigé vers AppsFlyer
2. AppsFlyer enregistre le clic
3. AppsFlyer redirige l'utilisateur vers l'app store
4. L'utilisateur installe l'app
5. AppsFlyer attribue l'installation

<div id="users-sent-directly-by-the-ad-network" />

## Utilisateurs envoyés directement par le réseau publicitaire

Lorsqu'il clique sur une publicité, l'utilisateur est dirigé vers l’app store par le réseau publicitaire, ce qui minimise le nombre de redirections :

1. L'utilisateur est dirigé vers l’app store
2. Le réseau publicitaire transmet les données d'engagement à AppsFlyer à partir de l'appareil.
3. L'utilisateur installe l'app
4. AppsFlyer attribue l'installation

<div id="sending-engagement-data-to-appsflyer" />

### Envoi des données d'engagement à AppsFlyer

Le fait d'envoyer l'utilisateur directement vers l’app store améliore son expérience grâce au nombre réduit de redirections. Cela garantit également une attribution précise des installations et permet un trafic de haute qualité.

Les réseaux publicitaires ne peuvent rapporter à AppsFlyer que les clics et les impressions **provenant directement de l'appareil de l'utilisateur**.

<div id="timing-of-sending-redirects" />

#### Timing de l'envoi des redirections

Pour éviter la perte d'attributions et de revenus pour le réseau publicitaire, les clics et les impressions doivent être envoyés à AppsFlyer en temps réel :

* Les **URL d'impression** doivent être signalées dès qu'une publicité est diffusée.
* Les **URL de clic** doivent être signalées dès qu'un utilisateur clique sur l'annonce.

<div data-zendesk-anchors="overview=pr%C3%A9sentation h_01HDY3CARC0A9504XGMJHYHGY4=pr%C3%A9sentation h_01HDY3CARCZK06C5XHEQFQYA8W=remarque redirect-users-via-appsflyer=utilisateurs-redirig%C3%A9s-via-appsflyer 01HDYFGYW3FDR64C54KKPXRHDF=utilisateurs-redirig%C3%A9s-via-appsflyer send-users-directly-by-the-ad-network=utilisateurs-envoy%C3%A9s-directement-par-le-r%C3%A9seau-publicitaire 01HDYFH8ZCSP2SN4ZYQQVG7EED=utilisateurs-envoy%C3%A9s-directement-par-le-r%C3%A9seau-publicitaire send-engagement-data-to-appsflyer=envoi-des-donn%C3%A9es-dengagement-%C3%A0-appsflyer h_01HDYGSEFHVF8ZD43XCVNGYT9N=envoi-des-donn%C3%A9es-dengagement-%C3%A0-appsflyer timing-of-sending-redirects=timing-de-lenvoi-des-redirections h_01HDXXDDXDEP43YHE3GF81BSKV=timing-de-lenvoi-des-redirections" />
