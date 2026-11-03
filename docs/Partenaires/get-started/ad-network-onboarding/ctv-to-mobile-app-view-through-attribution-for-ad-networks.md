---
title: >-
  Attribution des publicités CTV aux applications mobiles pour les réseaux
  publicitaires
metadata:
  keywords:
    - Attribution
    - Ad Networks
    - Partners
    - CTV
    - CTV Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roi-tamir
    - CTV Attribution
    - Ad Networks
  created_at: '2022-08-21T06:49:24Z'
  edited_at: '2024-09-23T12:40:51Z'
  id: 8528418936977
  locale: fr
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/fr/articles/8528418936977
---
> **En bref :** Attribuez les installations d'applications mobiles aux publicités visionnées sur des appareils CTV.

## Attribution des publicités CTV aux applications mobiles pour les réseaux publicitaires

Avec les URLs d'impression multiplateformes d'AppsFlyer, vous pouvez attribuer les installations d'applications mobiles aux publicités affichées sur CTV. Plusieurs installations au sein d’un même foyer peuvent être attribuées à la même impression publicitaire sur CTV.

![50310_CTV_flow_chart__2_.jpg](https://files.readme.io/401bcb083e1cc618794cb302668f7271cf825a5a6045ff10055e0164baf423a1-19774176963473.jpg)

L'attribution des publicités CTV aux applications mobiles utilise une <Anchor target="_blank" href="/marketers/fr/docs/set-up-cross-platform-links-for-multi-device-campaigns#setup">URL d'impression OneLink</Anchor> basée sur un modèle OneLink multiplateforme (avec un ID de modèle) créé par les annonceurs. Cela permet aux annonceurs de regrouper plusieurs applications de différentes plates-formes (par exemple, applications Android et iOS) à l'aide d'une seule URL.

Lorsque les utilisateurs voient la publicité sur CTV, vous envoyez l'URL d'impression à AppsFlyer en temps réel.

Exemple d'URL :

```http
https://impressions.onelink.me/{template_id}?pid=__media_source__&af_xplatform=true&af_xplatform_vt_lookback=24h&af_siteid=__CSITE__&c=__CAMPAIGN_NAME__&af_channel=__PLACEMENT__&af_c_id=__CAMPAIGN_ID__&af_adset=__AID_NAME__&af_adset_id=__AID__&af_ad=__CID_NAME__&af_ad_id=__CID__&af_source_platform=__source_platform__&af_source_device_category=__device_category__&af_ad_type=__CTYPE__&af_ip=__IP__&af_ua=__UA__&redirect=false
```

Les postbacks vous sont envoyés après chaque conversion.

<div id="setup" />

<Accordion title="Configuration">

**Pour configurer l'attribution des publicités CTV aux applications mobiles avec un annonceur** :

1. Assurez-vous d'être un <Anchor target="_blank" href="/partners/fr/docs/getting-started-onboarding-guide-for-ad-networks">partenaire intégré AppsFlyer</Anchor>, que vos postbacks soient correctement configurés, et que vous ayez [testé l'intégration de vos publicités CTV aux applications mobiles](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#test-partner-integration) avec AppsFlyer.
2. Assurez-vous que l'URL contient les [paramètres obligatoires](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#parameters), ainsi que tous les autres paramètres souhaités.
3. Envoyez à AppsFlyer l'adresse IP de l'utilisateur et le user agent. Ces informations sont nécessaires pour l'attribution des publicités CTV aux applications mobiles. Ces informations peuvent être envoyées soit :
   1. Comme les paramètres `af_ip` et `af_ua` sur l'URL d'impression.
   2. Comme les paramètres  et   dans les en-têtes de la requête.

</Accordion>

<div id="test-partner-integration" />

<Accordion title="Intégration des partenaires de test">

**Pour tester l'attribution des publicités CTV aux applications mobiles** :

1. Utilisez les applications de test suivantes : com.appsflyer.android.deviceid et id1192323960
2. Contactez l'équipe des Solutions Partenaires d'AppsFlyer pour recevoir une URL de test. Pour ce faire, connectez-vous à votre [tableau de bord partenaire](https://hq1.appsflyer.com/auth/login), et dans le menu supérieur, cliquez sur **Aide** > **Contacter notre équipe**.
   * Exemple d'URL : `https://impressions.onelink.me/dfHa?pid=partner_int&c=test_1&af_xplatform=true&af_xplatform_vt_lookback=24h&af_ip=MACRO&af_ua=MACRO&redirect=false`
3. Confirmez que votre identifiant de partenaire dans le paramètre `pid` est correct.
4. Saisissez votre adresse IP pour le paramètre `af_ip`.
5. Saisissez votre user agent pour le paramètre `af_ua`.
6. Saisissez l'URL dans un navigateur sur ordinateur.
7. Sur votre appareil mobile, accédez à l'App Store, téléchargez, installez et lancez l'application.
8. Une nouvelle installation devrait apparaître dans AppsFlyer et vous devriez recevoir un postback correspondant. Si vous ne voyez pas l'installation ou ne recevez pas le postback, contactez l'équipe des solutions partenaires.

</Accordion>

<div id="parameters" />

<Accordion title="Paramètres">

Les paramètres suivants sont utilisés pour fournir des données d'attribution et de mesure aux annonceurs.

| Paramètre | Obligatoire | Description |
| --- | --- | --- |
| ID\_template | ✓ | L'ID du <Anchor target="_blank" href="/marketers/fr/docs/create-a-onelink-template">template OneLink</Anchor>. Le template contient les paramètres de prédiction de base pour les applications des annonceurs et constitue la base pour la création d'autres liens. |
| pid | ✓ | L'identifiant du partenaire, attribué par AppsFlyer à la source média (réseau publicitaire) qui place l'annonce. |
| af\_xplatform | ✓ | <ul><li>Défini par l'annonceur pour indiquer si le lien prend en charge l'attribution multiplateforme.</li><li>Valeurs : vraifaux</li></ul> |
| af\_xplatform\_vt\_lookback | - | Fenêtre configurable qui indique le nombre d'heures suivant l'impression pendant lesquelles l'installation de l'application peut être attribuée à l'impression. Valeurs de paramètre disponibles : 1h - 72h (heures). La valeur par défaut est de 24h. |
| af\_ip | ✓ | <ul><li>L'adresse IP de l'appareil CTV qui affiche la publicité.</li><li>Si l'adresse IP n'est pas envoyée dans l'URL, elle doit être envoyée dans les en-têtes de la requête afin qu'AppsFlyer puisse effectuer l'attribution CTV-à-application mobile.</li></ul> |
| af\_ua | ✓ | <ul><li>L'agent utilisateur de l'appareil CTV qui affiche la publicité.</li><li>Si l'agent utilisateur n'est pas envoyé dans l'URL, il doit être envoyé dans les en-têtes de la requête afin qu'AppsFlyer puisse effectuer l'attribution CTV-à-application mobile.</li></ul> |
| af\_source\_platform | - | <ul><li>Une liste de valeurs pour représenter le système d'exploitation où l'impression se produit.</li><li>Valeurs :<ul><li>android</li><li>ios</li><li>tizen</li><li>webos</li><li>smartcast</li><li>roku</li><li>windowsphone</li><li>vidaa</li><li>PlayStation</li><li>smartcast</li><li>site web</li></ul></li></ul> |
| catégorie d'appareil source af | - | <ul><li>Une liste de valeurs pour représenter le type d'appareil où l'impression se produit.<ul><li>tv</li><li>téléphone mobile</li><li>ordinateur de bureau</li><li>tablette</li><li>décodeur</li><li>console de jeux</li><li>catégorie de périphérique inconnue</li><li>lecteur multimédia</li></ul></li></ul> |

D'autres paramètres pouvant être ajoutés à l'URL sont disponibles dans l'article <Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters">Structure et paramètres des liens d'attribution</Anchor>.

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Caractéristiques et limites">

| Caractéristique | Remarques |
| --- | --- |
| Fenêtre d'attribution | Entre 1 et 72 heures, selon le paramètre de fenêtre rétrospective . |
| Reciblage | <ul><li>Réattribution : Prise en charge pour l'interopérabilité entre plateformes et mobiles. Pas pour les autres plateformes.</li><li>Réengagement : Non pris en charge</li></ul> |
| Méthode d'attribution | Attribution par vue à l'aide d'un modèle probabiliste (adresse IP) |
| Attribution domestique | Soutenu. Cela signifie que plusieurs installations au sein d'un même foyer peuvent être attribuées à la même impression publicitaire CTV. |
| Intégration des partenaires de test | Non disponible pour les réseaux publicitaires signalés pour des taux élevés de fraude entre applications mobiles ou affiliés à des sources médiatiques signalées. |

</Accordion>

<div data-zendesk-anchors="ctvtomobile-app-attribution-for-ad-networks=attribution-des-publicit%C3%A9s-ctv-aux-applications-mobiles-pour-les-r%C3%A9seaux-publicitaires h_01HE2X91GTDTPKKFBRRYYFMHDW=attribution-des-publicit%C3%A9s-ctv-aux-applications-mobiles-pour-les-r%C3%A9seaux-publicitaires h_01HE2X91GT6406JZNK2RCQKPVM=setup h_01HE2X91GT1B9SG9J4C3SNAPWD=test-partner-integration h_01HE2X91GTA96HJJNG3HRV18DF=parameters h_01HE2X91GVK9P44J1MA0M44KE1=traits-and-limitations" />
