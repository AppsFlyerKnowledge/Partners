---
title: Gestion de l’intégration en libre-service pour les réseaux publicitaires
metadata:
  keywords:
    - postbacks
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
  created_at: '2021-03-15T10:03:41Z'
  edited_at: '2024-07-02T11:02:21Z'
  id: 360018512658
  locale: fr
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/fr/articles/360018512658
---
> **En bref :** Configurez et gérez votre intégration à partir du tableau de bord AppsFlyer.

<Embed title="Gestion de l’intégration en libre-service pour les réseaux publicitaires" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/9kvwrhnzjo" providerUrl="https://fast.wistia.com" />

**Conditions préalables :**

* Vous devez disposer d’identifiants de connexion (nom d’utilisateur et mot de passe) pour AppsFlyer avant de pouvoir gérer les liens d’attribution et les postbacks. Pour <Anchor target="_blank" href="/partners/fr/docs/getting-started-onboarding-guide-for-ad-networks">créer un compte partenaire</Anchor> , demandez à un client AppsFlyer (annonceur) de <Anchor target="_blank" href="/marketers/fr/docs/set-up-an-integrated-partner#inviter-de-nouveaux-partenaires-dans-appsflyer">vous inviter</Anchor>.
* La gestion des liens d’attribution et des postbacks par défaut est uniquement disponible pour les partenaires qui ont rejoint l’entreprise après le 1er février 2022.
* Vérifiez que vos serveurs sont prêts à recevoir des postbacks en respectant les points suivants :
  * Autorisez les <Anchor target="_blank" href="/marketers/fr/docs/appsflyer-server-ip-address-ranges-allowlisting">adresses IP</Anchor> du serveur AppsFlyer dans vos pare-feu et systèmes de sécurité pour garantir la communication avec vos points de terminaison.
  * Versions TLS : TLS 1.1, TLS 1.2+ avec <Anchor target="_blank" href="/marketers/fr/docs/appsflyer-https-ssl-encryption-policy-support#outgoing-messages-appsflyer-as-client">les chiffrements listés.</Anchor>
  * Ports : 80, 443
* ![AppsFlyerAdmin_us-en.png](https://files.readme.io/047d2ffa8bd5258c09f60c6f560162b285c4e9742d98b1158952a26d988ce763-18271759619089.png) Seuls les utilisateurs administrateurs peuvent accéder à cette section et la gérer.

<div id="accessing-integration-management" />

## Accès à la gestion de l’intégration

1. Connectez-vous à votre compte partenaire AppsFlyer.
2. Cliquez sur le menu déroulant en haut à droite > **Gestion des postbacks**.

<div id="attribution-link" />

## Lien d'attribution

Le lien d’attribution est la partie la plus importante de votre intégration. Les liens d’attribution sont utilisés pour informer AppsFlyer de l’engagement des utilisateurs avec une publicité. Les liens d’attribution sont placés derrière les annonces. Ainsi, lorsqu’un utilisateur clique sur une annonce, il clique sur un lien d’attribution.

La configuration du lien d’attribution est obligatoire.

**Pour configurer le lien d’attribution :**

1. Dans l’onglet **Lien d’attribution**, ajoutez les paramètres à inclure dans votre lien d’attribution :
   * **Nom du paramètre** : Nom de l'écran de paramètres AppsFlyer.
   * **Votre macro** : ajoutez la macro qui remplit les paramètres avec des valeurs.
   * **Inclure** : cochez la case pour inclure le paramètre dans le lien.

   <div id="important" />

   > 🚧 **Important !**
   >
   > * Ajoutez des paramètres liés à la campagne et à la publicité pour fournir des données plus fiables sur les performances de la campagne.
   > * **L’ID du site** est un paramètre obligatoire
   > * Les annonceurs utilisent ce lien comme base pour l’intégration d’une application spécifique et peuvent y ajouter des paramètres supplémentaires.
   > * L’ID d’application, la durée de la fenêtre d’analyse et votre ID de partenaire sont automatiquement ajoutés au lien. Vous n’avez pas besoin de les ajouter à ce modèle.

2. **[Facultatif]** Ajoutez des paramètres personnalisés qui ne sont pas fournis par AppsFlyer.
3. Utilisez l’aperçu du lien pour vérifier que tout est correct.
4. Cliquez sur **Enregistrer**.

<Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters">En savoir plus sur les liens d’attribution et les paramètres disponibles</Anchor>.

En cas de problème, contactez-nous à l’aide du <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget Assistant partenaire</Anchor>.

<div id="default-postback" />

## Postback par défaut

Les postbacks sont des URL contenant des macros remplies par AppsFlyer et envoyées à vos serveurs en temps réel après chaque conversion (soit sur votre réseau, soit sur d’autres réseaux également, selon votre configuration).

**Pour configurer le postback par défaut :**

1. Entrez les **adresses des points de terminaison.** Il s’agit des points de terminaison auxquels les postbacks sont envoyées. Entrez les URL appropriées pour les installations, les événements dans l’application ou les deux. Pour pouvoir activer l’intégration, au moins l’URL de postback d’installation est requise.
2. Ajoutez des paramètres au postback :
   * **Nom du paramètre** : Nom de l'écran de paramètres AppsFlyer.
   * **Votre paramètre de réception** : le paramètre de réception respectif de votre côté.
   * **Valeur du paramètre** (disponible pour certains paramètres) : choisissez le format de la valeur. Par exemple, pour les valeurs booléennes, choisissez de les recevoir comme « true »/« false » ou 1/0.
   * **Installer** : cochez la case pour inclure le paramètre dans le postback d’installation.
   * **Événement in-app** : cochez la case pour inclure le paramètre dans le postback de l’événement in-app.

   <Anchor target="_blank" href="/partners/fr/docs/postback-macros-for-ad-networks">Liste complète des macros de postback</Anchor>

   <div id="important-1" />

   > 🚧 **Important !**
   >
   > * Pour pouvoir faire la distinction entre les postbacks pour les événements légitimes et les postbacks rejetés, configurez les <Anchor target="_blank" href="/partners/fr/docs/postback-macros-for-ad-networks#macros%E2%80%94installs-inapp-events-and-rejected-events">macros de postbacks rejetés</Anchor>.
   > * Pour activer les postbacks d’événements d’installation/dans l’application rejetés, ajoutez les paramètres suivants à votre modèle de postback par défaut :
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`  
   >     **Remarque :** Si le postback de confidentialité avancée est activé, ajoutez également les paramètres ci-dessus au modèle Confidentialité avancée.

3. [Facultatif] **Paramètres personnalisés :** Configurez vos propres paramètres à inclure dans le postback.
4. Utilisez l’aperçu du modèle de postback pour vérifier que tout est correct.
5. Cliquez sur **Enregistrer**.

<Anchor target="_blank" href="/marketers/fr/docs/in-app-event-postback-configuration">Plus d’informations et d’exemples de postbacks.</Anchor>

En cas de problème, utilisez le <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget Assistant partenaire</Anchor>.

<div id="advanced-privacy-and-skan-postbacks" />

## Confidentialité avancée et postbacks SKAN

La confidentialité avancée et les postbacks SKAN ne peuvent être configurées qu’après la création du lien d’attribution et du postback par défaut.

**Pour gérer les postbacks :**

1. Sélectionnez un type de postback :
   * Postback de <Anchor target="_blank" href="/partners/fr/docs/advanced-privacy-guide-postback-macros-for-ad-networks">confidentialité avancée</Anchor>.
   * Postback <Anchor target="_blank" href="/partners/fr/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>.
2. Activez le builder.
3. **[Pour la configuration de postback SKAdNetwork uniquement]** Entrez votre ID SKAdNetwork. Ce champ est obligatoire, la configuration ne peut pas être enregistrée sans un ID valide.
4. Entrez les **adresses des points de terminaison.** Il s’agit des points de terminaison auxquels les postbacks sont envoyées. Entrez les URL appropriées pour les installations, les événements dans l’application ou les deux.
5. Ajouter les paramètres de postback :
   * **Nom du paramètre** : nom de l'écran de paramètres AppsFlyer.
   * **Votre paramètre de réception** : le paramètre de réception respectif de votre côté.
   * **Valeur du paramètre** (disponible pour certains paramètres) : choisissez le format de valeur. Par exemple, pour les valeurs booléennes, choisissez de les recevoir comme « true »/« false » ou 1/0.
   * **Installer** : cochez la case pour inclure le paramètre dans le postback d’installation.
   * Évènement in-app : cochez la case pour inclure le paramètre dans le postback d’événements dans l’application.

   Liste des <Anchor target="_blank" href="/partners/fr/docs/skan-integration-guide-for-ad-networks#receive-data-from-appsflyer">macros de postback SKAdNetwork</Anchor>

   Liste des <Anchor target="_blank" href="/partners/fr/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification">macros de postback Advanced Privacy</Anchor>

   <div id="important-2" />

   > 🚧 **Important !**
   >
   > * Pour activer les postbacks d’événements d’installation/dans l’application rejetés, ajoutez les paramètres suivants à votre modèle de postback par défaut :
   >   * `is-rejected`
   >   * `blocked-reason`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`
   > * Pour activer les postbacks rejetés pour la confidentialité avancée, vous devez d’abord ajouter les paramètres ci-dessus au [postback par défaut](/docs/self-serve-integration-management-for-ad-networks#postback-par-défaut)
   > * Lorsque les paramètres ci-dessus sont ajoutés à la fois au postback par défaut et au postback de confidentialité avancée (si cette option est activée), les postbacks d’événements d’installation/dans l’application rejetés sont activés.

6. [Facultatif] **Paramètres personnalisés :** Configurez vos propres paramètres à inclure dans le postback.
7. Utilisez l’aperçu du modèle de postback pour vérifier que tout est correct.
8. Cliquez sur **Enregistrer**.  
   Notez que lorsque vous enregistrez le postback, les modifications ont lieu immédiatement.

En cas de problème, contactez-nous à l’aide du <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget d’assistant partenaire</Anchor>.

<div data-zendesk-anchors="accessing-integration-management=acc%C3%A8s-%C3%A0-la-gestion-de-lint%C3%A9gration h_01H9FCSTYR157CCJWTYSNE9JQ0=acc%C3%A8s-%C3%A0-la-gestion-de-lint%C3%A9gration attribution-link=lien-dattribution h_01H9FCSTYR6HRSF9F8KCR4B3X7=lien-dattribution h_01H9FCSTYR4Q1985DTHNE1M1CC=important- default-postback=postback-par-d%C3%A9faut h_01H9FCSTYR2WX0M0ZW3B22EKBM=postback-par-d%C3%A9faut h_01H9FCSTYSEP367WAAKCFHZT58=important--1 advanced-privacy-and-skan-postbacks=confidentialit%C3%A9-avanc%C3%A9e-et-postbacks-skan h_01H9FCSTYSRKBMYR2BYNQJJKVM=confidentialit%C3%A9-avanc%C3%A9e-et-postbacks-skan h_01H9FCSTYSEJD59AWCFNXDZMYW=important--2" />
