---
title: API InCost pour les réseaux publicitaires
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Marketers
    - ROI360
    - Ad Networks
  created_at: '2020-04-26T19:13:47Z'
  edited_at: '2024-10-28T15:16:50Z'
  id: 360007714957
  locale: fr
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/fr/articles/360007714957
---
> **En bref :** l’API InCost, partie intégrante de ROI360 AppsFlyer, permet aux réseaux publicitaires d'envoyer à AppsFlyer de manière programmée des données de coûts publicitaires. Cela permet aux annonceurs de connaître les données de coûts globales et de comprendre l'importance effective de votre réseau.

## À propos de l’API InCost

L'API InCost est la meilleure solution pour permettre aux réseaux publicitaires d’envoyer des données de coûts à AppsFlyer. Les partenaires du réseau publicitaire envoient des données de coûts publicitaires détaillées à AppsFlyer via l'API. AppsFlyer ingère et traite les données et les met à la disposition des annonceurs et des partenaires dans des tableaux de bord et rapports.

#### Les points forts

* Aidez vos clients à connaître l'impact effectif de votre réseau avec à de simples rapports de coûts. Sans les données de coûts, un élément crucial des mesures manque à vos clients, ils ne peuvent donc pas mesurer avec précision le ROAS. Ils risquent donc d'investir par erreur dans d'autres sources média, ce qui aura un effet négatif sur vos résultats.
* Donnez des preuves de votre ROI avec une solution qui garantit une mesure des coûts précise, complète et en temps réel.
* API inCost est rapide et simple à déployer, et ses résultats sont quasi immédiats. Vous disposez également d'un contrôle total sur comment et quand vous envoyez les données, avec la possibilité d'envoyer les données de coûts datant de 90 jours.
* L'API InCost prend en charge tous les modèles de tarification des campagnes, et pas seulement le CPI (qui est le seul modèle disponible lors de l'envoi du coût par clic).
* Démarquez-vous dans le marketplace des partenaires AppsFlyer avec un badge "Coût" qui indique que vous proposez cette fonctionnalité.

## Mise en œuvre de l'API InCost

**Conditions à remplir** : pour que l'API InCost soit éligible, votre réseau publicitaire doit remplir ces conditions :

* 90 % des campagnes contiennent l'ID de campagne dans l'attribution.
* Possibilité d'envoyer des données au moins 6 fois par jour pour une meilleure actualisation des données. La fréquence est définie par le réseau publicitaire.
* Si le réseau publicitaire met à jour les données rétroactivement : possibilité d'envoyer les données des 7 derniers jours à chaque fois, afin de permettre l’intégrité des données.

**Mettre en œuvre l'API InCost et envoyer les données de coûts à AppsFlyer**

* Suivez les étapes indiquées dans le tableau.

| Étape n° | Action |
| --- | --- |
| 1 | Postuler à InCost :<ol><li>Dans AppsFlyer, dans le menu du haut, sélectionnez **Assistance** > **Contacter notre équipe.**<br />Le widget de l'assistant des partenaires s'ouvre.</li><li>Sélectionnez **Activer la mesure des coûts** et soumettez vos informations.<br />Une fois soumis, un ticket s'ouvre pour qu’un agent AppsFlyer dédié aux partenaires vous contacte.</li></ol> |
| 2 | Assurez-vous que les hiérarchies de campagne (ID de campagne et, éventuellement, l’ID d'adset et l’ID publicitaire) sont incluses dans vos liens d'attribution pour plus de 90 % de votre trafic. |
| 3 | Obtenez le <Anchor target="_blank" href="/marketers/fr/docs/managing-appsflyer-tokens">jeton d’API</Anchor> AppsFlyer dans le tableau de bord AppsFlyer. |
| 4 | Transmettez le jeton d’API à votre développeur pour qu'il l'utilise dans l'en-tête d'autorisation API, et demandez-lui de suivre <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-overview">ses instructions</Anchor> pour mettre en œuvre les trois méthodes d’API :<ol><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/app-list-ad-nets-api-get">Obtenir la liste des apps</Anchor>.</li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-uploader-post">Importer InCost</Anchor> : indiquez au développeur quels champs doivent être utilisés pour renseigner le JSON :<ul><li>Les champs obligatoires doivent être remplis. En d'autres termes : n'envoyez pas de champs vides.</li><li>La source média est limitée aux sources média associées à (enregistrées dans) votre compte de réseau publicitaire. La liste peut être obtenue auprès de votre responsable du développement des partenaires.</li><li>Tenez compte du <Anchor target="_blank" href="/marketers/fr/docs/about-data-freshness-and-timezone-support#fuseau-horaire-spécifique-à-lapp">fuseau horaire de l</Anchor>'app (tel qu'il est indiqué via l'API Get app permission list) pour que les dates des données de coûts s’alignent sur celles de l'application.</li><li>Si certains champs ne font pas partie de la hiérarchie du reporting des coûts de votre campagne, ne les ajoutez pas. Par exemple, l'ID d'adset, le nom d'actif, l'ID publicitaires, le nom de la publicité.</li></ul></li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-jobstatus-get">Obtenir le statut de l'opération</Anchor>.</li></ol> |
| 6 | Dans le fil du ticket (cf l'étape 1), informez AppsFlyer que l'implémentation de l'API est terminée, puis attendez la confirmation que votre intégration est opérationnelle. |
| 7 | Vérifiez que vos annonceurs ont activé les <Anchor target="_blank" href="/marketers/fr/docs/set-up-an-integrated-partner#cost-tab">données de coûts</Anchor> dans l'onglet coût de leur page partenaire intégrée à AppsFlyer. Ils commenceront alors à recevoir des données de coûts. |

### Champs pour InCost Upload JSON

<table><thead><tr><th><p>Champ</p></th><th><p>Obligatoire</p></th><th><p>Remarques</p></th></tr></thead><tbody><tr><td><p>date</p></td><td><p><span>Oui</span></p></td><td><ul><li><span>Date de la dépense</span></li><li><span>Format : <code>YYYY-MM-DD</code></span></li><li><span>Exemple : <code>2019-12-30</code></span></li></ul></td></tr><tr><td>app_id</td><td><p>Oui</p></td><td><ul><li>L'ID de l'application tel qu'il apparaît dans la plateforme AppsFlyer</li><li><span>Format : chaîne de 250 caractères maxi</span></li><li> <span>Exemple : </span><span>Android :<code>com.app.name</code>, </span>iOS : <code>id123456789</code> </li></ul></td></tr><tr><td><p><span>media_source</span></p></td><td><p><span>Oui</span></p></td><td><ul><li><span>Nom du réseau (ID), affichant la publicité associée à votre compte de partenaire de réseau publicitaire dans AppsFlyer</span></li><li><span>Format : chaîne de 50 caractères</span></li><li><span>Exemple : <code>network_int</code></span></li></ul></td></tr><tr><td><p><span>af_prt</span></p></td><td><p><span>Non\*</span></p></td><td><ul><li><span>Obligatoire pour les données d'attribution et de coûts des agences.</span></li><li><span><span>Nom de l'agence tel qu'il apparaît dans le lien d'attribution, et tel qu’il est associé au compte de l'agence dans AppsFlyer.</span></span></li><li><span>Format : chaîne de 50 caractères</span></li><li><span><span>Exemple : <code>agencya</code></span></span></li></ul></td></tr><tr><td><p><span>campaign_id</span></p></td><td><p><span>Oui</span></p></td><td><ul><li><span>Doit être identique au paramètre <code>af_c_id</code> envoyé dans le lien d'attribution.</span></li><li><span>Chaîne vide non autorisée</span></li><li><span>Format : chaîne de 24 caractères</span></li><li> <span>Exemple : <code>123abc</code></span><span></span> </li></ul></td></tr><tr><td><p><span>campaign_name</span></p></td><td><p><span>Oui</span></p></td><td><ul><li><span>Format : chaîne de 100 caractères</span></li><li><span>Exemple : <code>my_campaign123</code></span></li></ul></td></tr><tr><td><p><span>adset_id</span></p></td><td>Non\*</td><td><ul><li><span>Obligatoire si vous envoyez <code>adset_name</code> </span></li><li><span>Doit être identique au paramètre <code>af_adset_id</code> envoyé dans le lien d'attribution.</span></li><li><span>Si votre système de déclaration des coûts ne prend pas en charge <code>adset_id</code>, vous ne devez jamais l'envoyer.</span></li><li><span>Format : chaîne de 24 caractères</span></li><li><span>Exemple : <code>123A</code></span></li></ul></td></tr><tr><td><p><span>adset_name</span></p></td><td><p><span>Non</span></p></td><td><ul><li><span>Si vous envoyez ce champ, vous devez également envoyer <code>adset_id</code></span></li><li><span>Format : chaîne de 100 caractères</span></li><li><span>Exemple : <code>my_adset_name</code></span></li></ul></td></tr><tr><td><p><span>ad_id</span></p></td><td><p>Non\*</p></td><td><ul><li>Obligatoire si vous envoyez <span><code>ad_name</code></span>.</li><li><span>Ce champ doit être identique au paramètre <code>af_ad_id</code> envoyé dans le lien d'attribution </span></li><li><span>Si votre système de déclaration des coûts ne prend pas en charge <code>adset_id</code>, vous ne devez jamais l'envoyer.</span></li><li><span>Format : chaîne de 24 caractères</span></li><li>Exemple : <code>123AB</code> </li></ul></td></tr><tr><td><p><span>site_id</span></p></td><td><p>Non</p></td><td><ul><li>L'ID unique qui définit l'éditeur qui affiche la publicité.</li><li>Format : chaîne de 24 caractères.</li></ul></td></tr><tr><td><p><span>ad_name</span></p></td><td><p><span>Non</span></p></td><td><ul><li><span>Si vous envoyez ce champ, vous devez également envoyer <code>ad_id</code></span></li><li><span>Format : chaîne de 100 caractères</span></li><li>Exemple : <code>Ad-name</code> </li></ul></td></tr><tr><td><p><span>geo</span></p></td><td><p><span>Non</span></p></td><td><ul><li><span>Le pays que vous avez enregistré comme étant associé au coût</span></li><li><span>Dans la mesure du possible, il s'agit du pays où la publicité a été diffusée.</span></li><li><span>Format : <span>code pays à 2 caractères ISO 3166</span></span></li><li><span>Exemple : <code>US, CN, ZA</code></span></li></ul></td></tr><tr><td>currency</td><td><p><span>Oui</span></p></td><td><ul><li><span>Type de devise dépensé</span></li><li><span>Format : <span>Code devise à 3 caractères ISO 4217</span></span></li><li> <span>Exemple :</span> <span><code>USD, EUR, ZAR</code></span> </li></ul></td></tr><tr><td>spend</td><td>Oui</td><td><ul><li>Montant des dépenses dans la devise indiquée </li><li><span>Jusqu'à 5 chiffres après la virgule</span></li><li><span>La valeur 0 (zéro) est autorisée</span></li><li><span>Les valeurs négatives (-) ne sont PAS autorisées</span></li><li><span>N’envoyez pas les séparateurs (virgule)</span></li><li>N'envoyez pas les valeurs entre guillemets. </li><li>Format : nombre décimal</li><li>Exemple de valeurs : <code>1</code> <code>1.2</code> <code>1234.20</code>  </li></ul></td></tr><tr><td>channel</td><td>Non</td><td><ul><li> <span>Doit être identique au paramètre </span> <span><code>af_channel</code></span> envoyé dans le lien d'attribution</li><li>Format : chaîne de 20 caractères</li><li>Exemple : <code>my_channel</code> </li></ul></td></tr><tr><td>keywords</td><td>Non</td><td><ul><li>Format : chaîne de 100 caractères</li><li>Exemple : <code>abc app</code> </li></ul></td></tr><tr><td colspan="3"><p>\* Voir la colonne Remarques, car dans certains cas précis ce champ doit être envoyé.</p></td></tr></tbody></table>

<div data-zendesk-anchors="incost-api=%C3%A0-propos-de-lapi-incost h_01HE0WCBD9GD66KB1QGQ9MEXBJ=%C3%A0-propos-de-lapi-incost benefits=les-points-forts h_01HKVW85AYFG91PGYE5BDQVJNR=les-points-forts implementing-incost-api=mise-en-%C5%93uvre-de-lapi-incost h_01HKVWSWTWETTES5ZTNZ05X9VA=mise-en-%C5%93uvre-de-lapi-incost fields-for-incost-upload-json=champs-pour-incost-upload-json h_01HM8VCV81GQ6XQ4NA1EDCZ4K7=champs-pour-incost-upload-json" />
