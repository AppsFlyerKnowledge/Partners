---
title: Postbacks d'attribution rejetés aux partenaires intégrés
metadata:
  keywords:
    - fraud
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
  created_at: '2017-09-19T07:03:47Z'
  edited_at: '2024-09-23T13:08:58Z'
  id: 115004744123
  locale: fr
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/fr/articles/115004744123
---
> **En bref :** Les partenaires intégrés reçoivent des postbacks pour les installations et les événements in-app rejetés en raison de fraudes ou de non-conformité aux règles de validation.

## Postbacks d'attribution rejetés liés à la fraude et aux règles de validation

**Terminologie** :

* **Événements de fraude :** installations et événements in-app bloqués par Protect360
* **Événements non conformes :** installations et événements in-app qui ne respectent pas les règles de validation
* **Événements rejetés :** Événements de fraude et événements non conformes aux règles de validation
* **Installation avec attribution corrigée :** Une installation détournée, identifiée puis bloquée, dont l'attribution est ensuite corrigée et attribuée à la véritable source média.

**Postbacks**

* Les partenaires intégrés reçoivent en temps réel les postbacks des événements rejetés.
* Il n'y a pas de postbacks d'événements frauduleux pour les événements in-app des installations avec attribution corrigée.
* Les postbacks des événements rejetés sont envoyés au point de terminaison spécifié par le partenaire pour les postbacks d'installation et d'événement rejetés, avec les paramètres supplémentaires suivants :  
  * Raison du blocage
  * Sous-raison du rejet
  * Est rejeté
  * Valeur de la raison de rejet (lorsqu'elle est disponible). Par exemple : `reject_reason=site_blacklist&reject_reason_value="1123456"&is_rejected=1`

Le tableau suivant répertorie la raison du rejet, la valeur de la raison du rejet et une explication de cette raison :

| Raison du rejet | Valeur de la raison du rejet | L'utilisateur peut configurer | Explication |
| --- | --- | --- | --- |
| ctit\_anomalies | Le temps mesuré entre le clic et l'installation, en secondes | **x** | Les anomalies CTIT sont des clics attribués qui ont été bloqués en raison d'un temps entre clic et installation jugé déraisonnable. |
| validation\_installation\_store | N/A | **x** | Installations dont la validation par l'App Store a échoué |
| site\_blacklist | ID du site | **x** | Installations provenant d'ID de sites bloqués par AppsFlyer en raison d'une forte densité d'activités frauduleuses. Déterminé par nos algorithmes internes. |
| bots | N/A | **x** | Tentatives d'installation bloquées par des bots |
| click\_flood | ID du site ou vide | **x** | Installations provenant de clusters bloqués par AppsFlyer en raison d'un grand nombre d'installations avec un CTIT élevé et un faible taux de conversion. |
| anomalies\_comportementales | N/A | **x** | Les anomalies comportementales sont des fraudes à l'installation bloquées en raison d'un comportement post-installation incohérent et anormal. |
| hijacking\_installation | N/A | **x** | Le détournement d'installation est attribué à des clics bloqués en fonction d'un délai de clic et d'installation déraisonnable, basé sur l'API côté serveur de Google Play. |
| validation\_bots | Noms des règles ou vide | ✓ | Règle définie par le client. |
| validation\_hijacking | Noms des règles | ✓ | Règle définie par le client. |
| ai\_layer | N/A | **x** | Les modèles d'IA sont utilisés pour analyser de grandes quantités de données, améliorant ainsi les capacités de détection pour identifier les activités frauduleuses sur les appareils et les installations. |

#### Raisons du rejet pour les événements in-app

| Raison du rejet | Valeur de la raison du rejet | Explication |
| --- | --- | --- |
| Hérite de l'installation | Hérite de l'installation | Installation initiale identifiée comme fausse en raison du niveau <Anchor target="_blank" href="/marketers/fr/docs/protect360-raw-data-reports#motifs-de-blocage">d'installation</Anchor>  ou <Anchor target="_blank" href="/marketers/fr/docs/protect360-raw-data-reports#motifs-de-blocage"> de la</Anchor> liste de refus. |
| inapps\_bots | paramètres\_appareil\_faux | L'algorithme AppsFlyer détecte la fraude |
| validation\_inapps | nom\_événement\_invalide | Basé sur une règle de validation demandée ou définie manuellement |
| validation\_inapps | valeur\_événement\_invalide | Basé sur une règle de validation demandée ou définie manuellement |
| validation\_inapps | Nom(s) de la règle | Basé sur des règles définies manuellement |

> 🚧 **Important !**
>
> * Pour distinguer les postbacks d'événements légitimes et les postbacks rejetés, vous devez configurer les <Anchor target="_blank" href="/partners/fr/docs/postback-macros-for-ad-networks#macros%E2%80%94installs-inapp-events-and-rejected-events">macros des postbacks rejetés</Anchor>.
> * Pour activer les postbacks rejetés pour la confidentialité avancée, vous devez d'abord ajouter les paramètres suivants au <Anchor target="_blank" href="/partners/fr/docs/self-serve-integration-management-for-ad-networks#postback-par-défaut">postback par défaut</Anchor> :
>   * `is-rejected`
>   * `blocked-reason`
>   * `blocked-sub-reason`
>   * `blocked-reason-value`
> * Lorsque les paramètres ci-dessus sont ajoutés au postback par défaut et au postback de confidentialité avancée, les postbacks d'installation/d'événement in-app rejetés sont activés.

<div data-zendesk-anchors="rejected-attribution-postbacks-relating-to-fraud-and-validation-rules=postbacks-dattribution-rejet%C3%A9s-li%C3%A9s-%C3%A0-la-fraude-et-aux-r%C3%A8gles-de-validation h_01J5597AMDVWR2KTANSF7Y7T4P=postbacks-dattribution-rejet%C3%A9s-li%C3%A9s-%C3%A0-la-fraude-et-aux-r%C3%A8gles-de-validation reject-reasons-for-inapp-events=raisons-du-rejet-pour-les-%C3%A9v%C3%A9nements-in-app h_01J5597AMDHT5GJQN7QJZKV41F=raisons-du-rejet-pour-les-%C3%A9v%C3%A9nements-in-app h_01J5597AMD29TAZSKZS9WTFSM5=important-" />
