---
title: Bien démarrer — Intégration des agences
metadata:
  keywords:
    - Agency Account
    - Agency
    - permissions
    - Advertisers
    - Agencies
    - Partners
    - Marketers
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Marketers
    - Platform essentials
    - Agencies
  created_at: '2019-09-02T12:50:49Z'
  edited_at: '2023-11-24T14:12:13Z'
  id: 360002381617
  locale: fr
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/fr/articles/360002381617
---
> **En bref :** commencez à mesurer les campagnes de vos clients en créant un compte d'agence.

<Embed title="Bien démarrer — Intégration des agences" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/54qzpj1lm7" providerUrl="https://fast.wistia.com" />

<div id="appsflyer-attribution-model" />

## Modèle d'attribution AppsFlyer

Avant de continuer, vous devez comprendre comment fonctionne l'attribution d'AppsFlyer. Cette section explique ce qui se passe entre le premier clic ou la première impression et l'attribution d'une installation ou d'un événement — et ensuite.

<Image align="center" alt="ua-agency-flow.png" src="https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png" />

1. Un marketeur ou une agence au nom du marketeur, configure une campagne avec un certain ad network à l'aide des liens d'attribution AppsFlyer.
2. Un utilisateur clique sur l'une de ses annonces – par exemple une bannière ou un lien vers une offre.
3. Le lien d'attribution AppsFlyer associé à la publicité est ensuite peuplé d'informations recueillies pendant le clic. Nous stockons les informations que nous recueillons à partir du lien d'attribution dans notre base de données.
4. L'utilisateur est redirigé vers l'App Store.
5. L'utilisateur installe l'app et l'ouvre pour la première fois. Le SDK AppsFlyer dans l'app appelle nos serveurs avec les informations relatives à l'appareil sur lequel l'app est installée.
6. Nous faisons correspondre ces données à notre base de données de clics en utilisant nos <Anchor target="_blank" href="/marketers/fr/docs/appsflyer-attribution-model">méthodes d'attribution.</Anchor>
7. Si nous identifions une correspondance, nous attribuons l'installation au clic. Dans le cas contraire, nous attribuons l'installation à un téléchargement organique.
8. Une fois l'installation attribuée, nous l'affichons sur les tableaux de bord et les rapports du marketeur et de l'agence (<Anchor target="_blank" href="/partners/fr/docs/about-agency-accounts#ad-networks-auto-reporting">sauf Meta ads et X Ads</Anchor>).
9. Nous envoyons ensuite un postback avec les détails de conversion au réseau publicitaire, qui peut utiliser ces informations pour une meilleure optimisation.

<div id="agency-role-in-mobile-attribution-chain" />

## Rôle de l'agence dans la chaîne d'attribution mobile

Le marketeur qui possède l'app y intègre le SDK AppsFlyer afin de mesurer son action marketing.

Certains propriétaires d'app choisissent d'engager des agences de marketing pour mener des campagnes publicitaires en leur nom. Pour ce faire, l'agence doit disposer d'un compte AppsFlyer, et les marketeurs doivent autoriser l'agence <Anchor target="_blank" href="/marketers/fr/docs/set-up-an-integrated-partner#autorisations-pour-lagence">à accéder à leurs apps</Anchor>.

L'agence n'est pas techniquement propriétaire des apps, elle se contente de les promouvoir sur les canaux de marketing avec lesquels elle travaille, sans implication technique, comme l'intégration SDK. En fonction de l'ensemble des autorisations données par un marketeur, une agence peut contrôler diverses fonctions.

Lorsqu'une installation est attribuée à une publicité placée par une agence, elle s'affiche sur le tableau de bord de cette dernière. Le propriétaire de l'app la verra également et saura qu'elle est attribuée à l'agence.

Remarque : si votre organisation est propriétaire de l'app, ou si elle est chargée de son développement et de sa commercialisation, vous devez ouvrir un compte de marketeur.

<div id="pricing" />

## Tarification

L'étendue des fonctionnalités d'un compte d'agence dépend des autorisations accordées par le propriétaire de chaque app. Par conséquent, les comptes d'agence sont **gratuits**, et seuls les propriétaires d'apps sont facturés pour l'attribution. Les propriétaires d'apps et les agences peuvent utiliser les données d'attribution d'AppsFlyer à des fins de rémunération.

<div id="getting-started" />

## Mise en route

Pour configurer un nouveau compte d'agence :

1. Remplissez le <Anchor target="_blank" href="https://www.appsflyer.com/start/agencies/">formulaire d'inscription</Anchor>.
   * Utilisez le domaine de messagerie de votre entreprise pour vous inscrire.
   * Utilisez une adresse e-mail qui n'est pas associée à un compte AppsFlyer existant.
2. Un membre de l'équipe de l'agence AppsFlyer peut vous contacter pour vous fournir les informations supplémentaires nécessaires à l'inscription.
3. Une fois votre compte activé, vous recevez une notification et pouvez commencer à utiliser AppsFlyer.

<div id="adding-team-members" />

## Ajout de membres d'équipe

Lorsque votre compte est opérationnel, l'admin du compte (la personne qui a ouvert le compte) peut ajouter d'autres membres de l'équipe, qui peuvent avoir accès à tout ou une partie des apps gérées par l'agence. Pour en savoir plus sur la façon d'ajouter de nouveaux membres d'équipe, cliquez ici.

<div id="adding-apps-to-your-account" />

## Ajouter des apps à votre compte

Lorsque vous créez votre compte pour la première fois, aucune app ne lui est associée :

<Image align="center" alt="agency-start.png" src="https://files.readme.io/b536dde5f7cc886e7fc6ff22f15c402cea5cf68824fd92f242d13037824072d5-360003986997.png" />

Tout employé ou équipe d'agence nécessite l'autorisation du propriétaire de l'app pour :

* avoir accès au tableau de bord de l'app
* modifier la configuration
* exécuter des campagnes

Les marketeurs peuvent <Anchor target="_blank" href="/marketers/fr/docs/set-up-an-integrated-partner#autorisations-pour-lagence">fournir un accès à n'importe quelle agence</Anchor> directement via la plateforme. Une fois votre compte configuré et votre accès aux apps accordé, vous pouvez commencer à lancer des campagnes à l'aide des fonctionnalités AppsFlyer.

<div id="what-does-it-mean-to-get-permission-from-a-marketer" />

### Que signifie obtenir l'autorisation d'un marketeur ?

Lorsque vous obtenez l'autorisation d'un marketeur :

* L'app apparaît dans votre compte.
* Vous pouvez configurer des intégrations avec les réseaux publicitaires pour l'app (à l'exception de certains réseaux qui exigent une configuration par le propriétaire de l'app).
* Vous pouvez créer des liens d'attribution à utiliser dans vos campagnes.
* Vous pouvez configurer des intégrations de coûts avec des partenaires (qui le permettent).
* Vous pouvez voir les données de l'app.
* Vous pouvez autoriser les réseaux publicitaires et tous leurs membres d'équipe à consulter les infos de base relatives à l'application.  
  Ainsi, lorsqu'une agence et un marketeur collaborent avec un réseau publicitaire, tous deux peuvent modifier l'autorisation qui permet aux membres d'équipe du réseau publicitaire de consulter le tableau de bord de l'app, et chacun d'entre eux peut voir les modifications apportées par l'autre. Si vous voyez des nouveaux membres d'équipe du réseau publicitaire que vous n'avez pas ajoutés, ou s'il manque des membres d'équipe que vous n'avez pas supprimés, il est donc possible que ce soit le marketeur qui l'ait fait.

Les autorisations supplémentaires comprennent l'accès au rapport de cohorte, au tableau de bord Protect360 et aux données organiques agrégées.

<div id="app-list" />

### Liste des apps

Une fois que vous avez obtenu la permission du marketeur, l'app apparaît sur la page de l'app.

La page des apps de votre compte répertorie jusqu'à 1000 apps. Si la liste des apps pour lesquelles vous disposez d'autorisations dépasse 1000 apps, certaines d'entre elles ne s'affichent pas dans la liste. Vous pouvez les trouver à l'aide de la recherche.

<Image align="center" alt="agency-apps.png" src="https://files.readme.io/6ec28125c938a5fb90d6a5bfe80ef40225432c222dcd4fafd747eeba529f1c49-360003722277.png" />

<div id="searching-for-apps" />

#### Recherche d'apps

1. Dans votre compte, cliquez sur ***Mes apps***, dans le menu supérieur
2. Dans le champ de recherche, saisissez le terme recherché, par exemple  :
   * Nom de l'app
   * ID d'app
   * E-mail du propriétaire d'app

### Transparence

Alors que le secteur favorise un écosystème plus transparent, AppsFlyer soutient la transparence entre les annonceurs et les agences afin qu'ils bénéficient le plus possible de ses rapports et outils d'analyse. Par défaut, votre trafic est configuré pour être transparent. Cela signifie que vos sources média sont transmises aux annonceurs.

> 📘 **Note**
>
> À partir du 14 août 2023, la [transparence d'agence au niveau de l'app](/docs/getting-started-agency-onboarding#transparence) sera activée par défaut et ce, de manière permanente. Sont concernées par ce changement les agences qui viennent de rejoindre AppsFlyer, et les agences existantes qui ont de nouvelles autorisations d'accès pour les annonceurs. Les agences existantes dont l'option **Autoriser la transparence** est désactivé (version héritée) auront la possibilité de la maintenir désactivée, ou de l'activer. Cependant, une fois activée, la transparence le restera en permanence.

#### Activer Autoriser la transparence

**Uniquement pour les agences en non-transparence en version héritée :**

1. Allez à **Configuration** > **Paramètres d'app**.
2. Désactivez **Autoriser la transparence**.

> 📘 **Note**
>
> * Le paramètre de transparence s'applique au niveau de l'app
> * Seuls les admins de compte d'agence peuvent activer le paramètre de transparence.
> * Si le marketeur désactive les autorisations de l'agence, les données historiques de l'agence (telles que les installations et les coûts) deviennent non transparentes.
> * Les données de Meta Ads, de X Ads et de SKAN restent transparentes, que l’option **Autoriser la transparence** soit activée ou non.
> * Les données des rapports de consommations restent non transparentes, que l’option **[Autoriser la transparence](/docs/getting-started-agency-onboarding#transparence)** soit activée ou non, les rapports affichent donc toujours le nom de l’agence mais pas la source média attribuée.

<div id="agency-dashboard" />

## Tableau de bord d'agence

Cliquez sur une app dans la liste pour accéder à son <Anchor target="_blank" href="/marketers/fr/docs/getting-started-with-appsflyer-dashboards">tableau de bord</Anchor>. Lorsque vous commencez à mener des campagnes, les données agrégées qui vous sont attribuées s'affichent ici.

<Image align="center" alt="agency-dashboard.png" src="https://files.readme.io/5f541770f60ba7d212c9f18e3a14d625758c5d8911997ce4cc39333ee7530244-360003815398.png" />

Le tableau de bord du compte de l'Agence comprend un accès par défaut aux éléments suivants :

* Tableau de bord global de valeur vie client
* Tableau de bord des événements in-app
* Tableau de bord de retargeting

<div id="running-campaigns" />

## Campagnes en cours

<div id="self-reporting-networks-srns" />

### Réseaux auto-reporting (SRN)

Les SRN, également connus sous le nom de réseaux auto-attribués (SAN), sont des réseaux qui n'ont pas besoin pas des liens d'attribution AppsFlyer pour rapporter les clics ou autres données. Ils utilisent plutôt l'intégration directe avec AppsFlyer. Parmi ces réseaux figurent <Anchor target="_blank" href="/marketers/fr/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta ads</Anchor>, <Anchor target="_blank" href="/marketers/fr/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor>, <Anchor target="_blank" href="/marketers/fr/docs/google-ads-adwords-integration-setup-for-agencies">Google Ads</Anchor>, <Anchor target="_blank" href="/marketers/fr/docs/snapchat-advanced-srn-integration-setup">Snapchat</Anchor>, DoubleClick, <Anchor target="_blank" href="/marketers/fr/docs/apple-ads-integration-setup">Apple Ads Search</Anchor>, <Anchor target="_blank" href="/marketers/fr/docs/yahoo-integration-setup">Yahoo</Anchor> et <Anchor target="_blank" href="/marketers/fr/docs/yahoo-japan-search-ads-campaign-configuration#agency-integration">Yahoo! JAPAN</Anchor>.

La plupart de ces réseaux requièrent une configuration spéciale pour les agences. Par exemple, étant donné que l'intégration de Meta ads et X Ads peut uniquement être configurée par un propriétaire d'app, les noms de campagne de l'agence DOIVENT commencer par le nom de l'agence pour s'assurer que les installations sont correctement attribuées à cette dernière.

Cliquez sur les liens ci-dessus pour consulter les guides du réseau et les instructions spécifiques aux paramètres de l'agence.

<div id="sandbox-attribution-agency-campaigns" />

<div id="non-srns" />

### Non SRN

La plupart des réseaux publicitaires ont besoin de liens d'attribution placés derrière une publicité. Pour en savoir plus sur la façon de mener des campagnes avec ces réseaux<Anchor target="_blank" href="/partners/fr/docs/about-agency-accounts#non-srn">, cliquez ici</Anchor>.

### Médias propriétaires : liens personnalisés et OneLink™

Vous pouvez utiliser des <Anchor target="_blank" href="/marketers/fr/docs/create-a-onelink-template">liens personnalisés</Anchor> dans le cadre de campagnes sur des médias autres que des réseaux publicitaires (réseaux sociaux, e-mails, blogs, SMS).

<Anchor target="_blank" href="/marketers/fr/docs/onelink-guide">OneLink™</Anchor> est un type de lien personnalisé qui vous permet d'utiliser le même lien pour plusieurs plateformes ou d'envoyer les utilisateurs vers un contenu spécifique dans l'app.

Remarque : les agences ne peuvent pas créer de templates de liens OneLink ou de plateformes uniques, mais elles peuvent utiliser des templates créés par les marketeurs.

<div id="campaign-naming-1" />

<div id="skadnetwork-agency-campaigns" />

### Campagnes SKAdNetwork des agences

L'infrastructure SKAdNetwork, inhérente à l'iOS d'Apple, permet aux marketeurs de mesurer les performances de leurs campagnes sans IDFA ni ID publicitaire. Même si Apple n'inclut pas les agences dans le processus d'attribution SKAdNetwork et si AppsFlyer ne peut attribuer directement les agences, AppsFlyer peut malgré tout fournir les données d'attribution pour les campagnes d'agence exécutées sous SKAdNetworks.

<div id="campaign-naming" />

#### Nom de la campagne

Pour afficher vos campagnes dans le tableau de bord AppsFlyer SKAdNetwork, les noms des campagnes que vous configurez avec SKAdNetwork doivent inclure votre identifiant de partenaire et avoir la structure suivante :

* votre af\_prt (<Anchor target="_blank" href="/partners/fr/docs/about-agency-accounts#paramètre-af_prt">qu'est-ce que af\_prt et où le trouver</Anchor>),
* tiret du bas,
* le nom réel de votre campagne, conforme à la convention de dénomination de votre agence.

Par exemple, si votre af\_prt est AgencyX, le nom de votre campagne peut ressembler à ceci :

`AgencyX_SummerSale`

> 📘 **Note**
>
> * Les campagnes d'agence dans SKAdNetwork sont toujours transparentes. L'identité du réseau publicitaire qui gère la campagne n'est pas cachée au marketeur. Notez qu'à partir d'iOS 15, le marketeur (le propriétaire de l'app) peut <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/receiving_ad_attributions_and_postbacks">choisir de recevoir directement une copie du postback.</Anchor>
> * <mark>Dans l'onglet Intégration, vous devez demander au marketeur d'activer le paramètre **Activation du partenaire**</mark> de l'ad network. Si ce n'est pas fait, le réseau publicitaire ne recevra pas les postbacks liés aux campagnes SKAN. Important ! Cette opération s'ajoute à l'option Activation du partenaire que vous trouvez dans l'interface utilisateur.

<div id="access-to-skan-conversion-studio" />

#### Accès au SKAN Conversion Studio

Dans <Anchor target="_blank" href="/marketers/fr/docs/skan-conversion-studio#studio-de-conversion-skan--présentation">Conversion Studio</Anchor>, les agences peuvent <Anchor target="_blank" href="/marketers/fr/docs/skan-conversion-studio#view-cv-mapping">consulter et télécharger</Anchor> le mappage des valeurs de conversion SKAN d’un marketeur, mais elles ne peuvent ni configurer ni modifier les paramètres.

<div id="skadnetwork-dashboard" />

#### Tableau de bord SKAdNetwork

<Embed title="Bien démarrer — Intégration des agences" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/jkm7se0jym" providerUrl="https://fast.wistia.com" />

**Pour aller plus loin :**

* <Anchor target="_blank" href="/marketers/fr/docs/about-att-and-skan">Guide de démarrage rapide pour la solution SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/marketers/fr/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">Tableau de bord SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/marketers/fr/docs/skadnetwork-skan-solution-guide">Solution SKAdNetwork</Anchor>

<div id="single-source-of-truth-ssot-for-agencies" />

### SSOT pour les agences

SSOT unifie toutes les méthodes d’attribution en combinant les données d’attribution de différents modèles, et en supprimant les installations en double ainsi que les mesures associées aux coûts et aux revenus. De cette façon, les valeurs eCPI, ROI et ROAS, par exemple, sont calculées correctement.

Les agences peuvent accéder aux données SSOT dans la vue d'ensemble du tableau de bord, mais pas via l'API.

Pour inclure l’indicateur SSOT dans votre vue d'ensemble du tableau de bord, le marketeur doit activer SSOT dans Conversion Studio.

**Pour aller plus loin :**

* <Anchor target="_blank" href="/marketers/fr/docs/single-source-of-truth-ssot-guide-for-ios-attribution">Guide de l'attribution IOS en SSOT (Single Source Of Truth)</Anchor>

<div id="what-else-you-can-do" />

## Que pouvez-vous faire d'autre ?

* Mesurer la rétention des utilisateurs
* Exploiter les événements in-app pour optimiser vos campagnes
* Exécuter des campagnes de <Anchor target="_blank" href="/marketers/fr/docs/retargeting-attribution-guide">retargeting</Anchor>
* Exporter vos <Anchor target="_blank" href="/marketers/fr/docs/manage-data-access-permissions">données</Anchor>
* <Anchor target="_blank" href="/marketers/fr/docs/registering-test-devices">Enregistrer votre appareil de test</Anchor>
* et bien plus encore.

Vous trouverez plus d'informations sur l'utilisation avancée du compte d'agence <Anchor target="_blank" href="/partners/fr/docs/about-agency-accounts#agency-setting-up-campaigns">ici</Anchor>.

Vous êtes tombé sur un terme peu familier ? Retrouvez-le dans notre <Anchor target="_blank" href="/marketers/fr/docs/appsflyer-knowledge-base-glossary">Glossaire</Anchor>.

Vous avez un problème technique urgent ? Faites une recherche dans notre Centre d'assistance : nous avons probablement une réponse pour vous. Si vous ne trouvez pas ce que vous cherchiez, contactez notre équipe de l'assistance en cliquant sur l'angle de votre tableau de bord, en bas à droite.

<div data-zendesk-anchors="appsflyer-attribution-model=mod%C3%A8le-dattribution-appsflyer h_01HFXXKCMW7EREMC7KEYTF3ERH=mod%C3%A8le-dattribution-appsflyer agency-role-in-mobile-attribution-chain=r%C3%B4le-de-lagence-dans-la-cha%C3%AEne-dattribution-mobile h_01HFXXKCMW987FV2PB4EPXH92Z=r%C3%B4le-de-lagence-dans-la-cha%C3%AEne-dattribution-mobile pricing=tarification h_01HFXXKCMWPN6AN98A5RD5YXW7=tarification getting-started=mise-en-route h_01HFXXKCMWRXVBYTW9RYEX7X8F=mise-en-route adding-team-members=ajout-de-membres-d%C3%A9quipe h_01HFXXKCMWB6ZG3PSHDSETC4XC=ajout-de-membres-d%C3%A9quipe adding-apps-to-your-account=ajouter-des-apps-%C3%A0-votre-compte h_01HFXXKCMWBZVTHAEKED1Q27M3=ajouter-des-apps-%C3%A0-votre-compte what-does-it-mean-to-get-permission-from-a-marketer=que-signifie-obtenir-lautorisation-dun-marketeur h_01HFXXKCMWYNNZWTKP9KEQ4VCD=que-signifie-obtenir-lautorisation-dun-marketeur app-list=liste-des-apps h_01HFXXKCMWKW78TMC76F40PY2C=liste-des-apps searching-for-apps=recherche-dapps h_01HFXXKCMW8S93N577393QZTYX=recherche-dapps transparency=transparence h_01HFXXKCMW5YC2APNGHNV6B35C=transparence h_01HFXXKCMW4HKQW7NRA1H5RHE3=note turning-on-allow-transparency=activer-autoriser-la-transparence h_01HFXXKCMW215G5CTB5DBVJSX2=activer-autoriser-la-transparence h_01HFXXKCMWMMKWJYBC3JT0HWWN=note-1 agency-dashboard=tableau-de-bord-dagence h_01HFXXKCMWPZVADY15DKATJ7Z4=tableau-de-bord-dagence running-campaigns=campagnes-en-cours h_01HFXXKCMWFB9RXY7AVBX5CGB9=campagnes-en-cours selfreporting-networks-srns=r%C3%A9seaux-auto-reporting-srn h_01HFXXKCMW1Z7FWHDJ3Y6G0NYD=r%C3%A9seaux-auto-reporting-srn nonsrns=non-srn h_01HFXXKCMWPAMZ373D5AVD5EJF=non-srn owned-media-custom-links-and-onelink%E2%84%A2=m%C3%A9dias-propri%C3%A9taires-liens-personnalis%C3%A9s-et-onelink h_01HFXXKCMWKYR2XMZZ08HNY8WJ=m%C3%A9dias-propri%C3%A9taires-liens-personnalis%C3%A9s-et-onelink skadnetwork-agency-campaigns=campagnes-skadnetwork-des-agences h_01HFXXKCMWZ19E0QR1VE977BTS=campagnes-skadnetwork-des-agences campaign-naming=nom-de-la-campagne h_01HFXXKCMWMW1AHXMS19CYD4VC=nom-de-la-campagne h_01HFXXKCMWEQ41A7TZ2K6DE424=note-2 access-to-skan-conversion-studio=acc%C3%A8s-au-skan-conversion-studio h_01HFXXKCMWX53HMRG2ZTD9FYQE=acc%C3%A8s-au-skan-conversion-studio skadnetwork-dashboard=tableau-de-bord-skadnetwork h_01HFXXKCMW1HHMSS3XAXJKME29=tableau-de-bord-skadnetwork single-source-of-truth-ssot-for-agencies=ssot-pour-les-agences h_01HFXXKCMX1E8GZKHJG7EEJ5Y1=ssot-pour-les-agences what-else-you-can-do=que-pouvez-vous-faire-dautre h_01HFXXKCMXQ2JT63GBMC74PWBA=que-pouvez-vous-faire-dautre" />
