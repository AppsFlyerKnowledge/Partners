---
title: Macros de postback pour les réseaux publicitaires
metadata:
  keywords:
    - postbacks
    - Advertisers
    - Ad Networks
    - macros
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2016-01-11T14:41:40Z'
  edited_at: '2022-04-20T07:23:03Z'
  id: 207273946
  locale: fr
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/fr/articles/207273946
---
> **En bref :** en tant qu'ad network, vous pouvez définir le contenu et les points de terminaison des postbacks qui vous sont envoyés dans le cadre de votre intégration avec AppsFlyer. Les postbacks sont liés à l'engagement des utilisateurs d'app, par exemple les installations, les évènements in-app, les réengagements, etc.

Guides du postback des partenaires intégrés :

* <Anchor target="_blank" href="/partners/fr/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Protection de la vie privée avancée</Anchor>
* <Anchor target="_blank" href="/partners/fr/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/partners/fr/docs/rejected-attribution-postbacks-to-integrated-partners">Postbacks d'attribution rejetés</Anchor>

## Les postbacks pour les réseaux publicitaires

* **Configuration du postback :** pour demander des modifications de vos paramètres de postback, contactez [integrations@appsflyer.com](mailto:integrations@appsflyer.com) ou votre responsable du développement partenaire AppsFlyer.
* **Types de postback** : les postbacks sont disponibles pour les événements d'installation et événements in-app, ainsi que pour les installations et événements in-app bloqués en raison soit d'une fraude identifiée par Protect360, soit d'une violation des règles de validation du ciblage.

| Source | Description |
| --- | --- |
| <Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters">Paramètres du lien d'attribution</Anchor> | Paramètres fournis par le partenaire sur les URL de clic et d'impression<br /><br />Exemple : Paramètre de l'ID de clic sur le lien d'attribution - "&click\_id=CLICK\_ID" |
| ID de partenaire dans AppsFlyer | Identifiants uniques fournis à l'annonceur par le partenaire<br /><br />Exemples : ID d'app, ID de compte, ID d'utilisateur, ID de réseau |
| Informations provenant du SDK | Informations extraites de l'appareil par le SDK AppsFlyer<br /><br />Exemple : les identifiants des appareils iOS peuvent être extraits en utilisant "&IDFA=(idfa)" dans le postback |
| Issue de la plate-forme AppsFlyer | Infos issues de la plate-forme AppsFlyer. |
| Protect360 et règles de validation | Informations sur les installations identifiées comme frauduleuses, les installations qui violent les règles de ciblage des campagnes, ainsi que les événements in-app qui en découlent |

## Macros de postback

Lorsque les macros sont intégrées à un postback, elles sont remplacées par les données de l'utilisateur correspondant. Par exemple, pour obtenir l'adresse IP d'un utilisateur qui installe l'application, intégrez `country_code=(ip)` dans la structure du postback. Les macros prises en charge sont répertoriées dans le tableau suivant :

Signification des colonnes du tableau suivant :

* **Source :** origine des données.
  * Lien : liens d'attribution
  * SDK : SDK AppsFlyer intégré dans l'app ou l'API de serveur à serveur
  * AF : après traitement par AppsFlyer
* **Envoyer tout**: si oui, vous pouvez recevoir les données des installations et événements qui ont été attribués à d'autres réseaux ou en organique. (En d'autres termes : qui ne vous est pas attribué).
* **[Base] Macros pour tous les postbacks** : macros relatives à l'installation, à l'événement in-app et aux postbacks d'événement qui ont été rejetés
* **[Facultatif]** concerne les événements in-app et les événements rejetés tels qu'indiqué dans la colonne (rejeté, in-app)

| Macro de postback (nom) | Source | Envoyer tout | Description | [Par défaut] Macros pour tous les postbacks | Événements in-app et rejetés [optionnel] |
| --- | --- | --- | --- | --- | --- |
| advertising\_id | SDK | Oui | ID d'appareil réinitialisable par l'utilisateur, également nommé GAID. Également disponible sous la forme : (sha1-advertiserId) | Oui |  |
| app\_name | SDK | Oui | Nom de l'app défini par l'annonceur | Oui |  |
| appsflyer\_id | SDK | Oui | Identifiant unique AppsFlyer enregistré lors de la conversion | Oui |  |
| attributed\_touch\_type | SDK | Non | Valeurs possibles  click, impression, TV, préinstallé | Oui |  |
| blocked\_reason | AF | Non | Fraude/motif des règles de validation | Non | Rejeté |
| blocked\_reason\_value | AF | Non | Fraude/valeur du motif des règles de validation (ex : ID de site) | Non | Rejeté |
| blocked\_sub\_reason | AF | Non | Fraude/sous-motif des règles de validation | Non | Rejeté |
| bundle\_id | SDK | Oui | iOS : identification visant à faire correspondre une app ou un groupe d'apps dans iOS (cf ID de groupe des développeurs Apple) Android : le nom de l'app | Oui |  |
| country\_code | AF | Oui | Code pays utilisant ISO 3166 (alpha-2) Exemple : US, CN. | Oui |  |
| event\_name | SDK | Oui | Nom attribué à un événement | Non | Achat |
| event\_revenue\_USD | AF | Oui | Valeur de l'événement en USD | Non | Achat |
| event\_revenue | SDK | Oui | Valeur de l'événement raporté par le SDK à l'aide de event\_revenue\_currency, ou la devise que vous avez sélectionnée. | Non | Achat |
| {"event_revenue"}  <br />{"_currency"} | SDK | Oui | Le code de devise du revenu d'évènement rapporté dans l'événement, ou la devise que vous avez sélectionnée. | Non | Achat |
| event\_time | SDK | Oui | Heure de l'évènement | Non | Achat |
| event\_value | SDK | Oui | L'événement in-app comporte des attributs dotés de valeurs, lesquelles peuvent être entièrement envoyées entièrement au postback au format JSON. URL encodée à partir de la macro (encodage). | Non | Achat |
| idfa | SDK | Oui | ID publicitaire réinitialisable par l'utilisateur qui est présent sur les appareils iOS. Également disponible sous : (sha1-idfa) | Oui |  |
| idfv | SDK | Oui | Identifiant unique par utilisateur et par vendeur présent sur les appareils IOS | Oui |  |
| install\_time | SDK | Oui | Horodateur de l'installation | Oui |  |
| install\_unix\_ts | SDK | Oui | Installer l'horodateur au format unix | Oui |  |
| is\_attributed | AF | Oui | Un drapeau marquant si l'installation ou l'événement est attribué à cette source média | Oui |  |
| is\_lat | SDK | Oui | Suivi publicitaire limité (LAT) : le lancement du LAT iOS 14 a été rendu obsolète par Apple. Définissez le statut de confidentialité des utilisateurs à l'aide de ATT. Dans ce cas, ne prenez pas en compte is\_lat. Versions antérieures à IOS 14, si défini sur «true», l'IDFA n'est pas disponible et est réglé sur 0. Lorsque «true», l'utilisateur a choisi de refuser les publicités basées sur les intérêts. Ceci n'empêche pas la collecte de GAID. | Oui |  |
| is\_primary\_attribution | AF | Oui | Si défini sur «false», voir is\_retargeting. | Non | Achat |
| is\_retargeting | Lien | Non | Utilisable associé à is\_primary\_attribution. En savoir plus sur la <Anchor target="_blank" href="/marketers/fr/docs/resolve-retargeting-double-attribution">double attribution des événements de retargeting.</Anchor><br /><br />Si «true» (1), l'événement est rapporté dans le cadre d'une campagne de retargeting, la source média étant la source média de retargeting.<br /><br />Si «false» (0) et is\_primary\_attribution est «false», l'événement fait partie d'une campagne de retargeting mais la source média de référence est la source média d'attribution de l'utilisateur | Non |  |
| langue | SDK | Oui | Langue (locale) signalée par l'appareil et définie par l'OS de l'appareil. | Oui |  |
| OAID | SDK | Oui | ID réinitialisable par l'utilisateur présents sur certains appareils Android, remplace généralement le GAID | Oui |  |
| partner\_event\_id | AF | Oui | Nom/ID de l'événement correspondant sur la plate-forme du partenaire | Non | Achat |
| platform | SDK | Oui | Plate-forme de l'appareil : iOS, Android ou Windows Mobile | Oui |  |
| retargeting\_  <br />conversion\_type | AF | Non | Indicateur précisant s'il s'agit d'une réattribution ou d'un réengagement | Retargeting uniquement |  |
| app\_version | SDK | Oui | Nom de la version de l'app défini par le développeur dans le code de l'app | Oui |  |
| app\_id | SDK | Oui | L'ID de l'app tel que rapporté par l'app. | Oui |  |
| att-0-1 | SDK | Oui | Valeurs possibles :<ul><li>1 : statut ATT autorisé ou af\_authorized.</li><li>0 : tout autre statut ATT.</li></ul> | Oui |  |
| att-status | SDK | Oui | Le <Anchor target="_blank" href="/marketers/fr/docs/att-implications-ios-14-and-deprecation-of-lat#valeurs-att">statut ATT</Anchor> rapporté par iOS. Comme autorisé, not\_determined.<br /><br />Dans certains cas, il n'y a pas de valeur et "" est renvoyé. | Oui |  |
| af\_ad | Lien | Non | Nom de la publicité (<Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters#niveaux-de-granularité-des-données">voir plus</Anchor>) - fourni par l'annonceur/l'éditeur | Oui | Oui |
| af\_ad\_id | Lien | Non | Fourni par l'annonceur/l'éditeur | Oui | Oui |
| af\_adset | Lien | Non | <ul><li>Fourni par l'annonceur/l'éditeur</li><li>Adset représente un niveau intermédiaire dans la hiérarchie entre campagne et publicité. <Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters#niveaux-de-granularité-des-données">En savoir plus</Anchor></li></ul> | Oui | Oui |
| af\_adset\_id | Lien | Non | Fourni par l'annonceur/l'éditeur | Oui | Oui |
| C | Lien | Non | Fourni par l'annonceur/l'éditeur. Les noms de campagne comportant plus de 100 caractères sont affichés dans le tableau de bord comme "c\_name\_exceeded\_max\_length" | Oui | Oui |
| af\_c\_id | Lien | Non | Fourni par l'annonceur/l'éditeur | Oui | Oui |
| af\_siteid | Lien | Non | <ul><li>L'ID unique qui définit l'éditeur qui affiche la publicité. <Anchor target="_blank" href="/marketers/fr/docs/about-link-structure-and-parameters#site-id-parameter">En savoir plus</Anchor></li></ul> | Oui | Oui |
| af\_subsite\_id | Lien | Non | <ul><li>ID du sous-réseau/de l'éditeur.</li><li>Si en plus de l'éditeur principal (ID de site) il existe un sous-éditeur, ou bien si vous souhaitez inclure des infos supplémentaires, comme le type de publicité ou l'emplacement dans l'app (bannière, interstitiel, vidéo, etc.), veuillez utiliser af\_sub\_siteid. Exemple : af\_sub\_siteid =ABCD\_4567</li></ul> | Oui | Oui |
| af\_ad\_type | Lien | Non | Utiliser la convention de dénomination suivante :<ul><li>**text :** une unité publicitaire qui ne contient que du texte, par exemple un résultat de recherche</li><li>**banner :** un format de base qui apparaît en haut ou en bas de l'écran de l'appareil</li><li>**interstitial :** une annonce pleine page qui apparaît pendant les pauses faites durant l'expérience</li><li>**video:** une vidéo standard, qui est non-rewarded (sans récompense)</li><li>**rewarded\_video :** un bloc de publicités qui offre des récompenses in-app aux utilisateurs qui décident de regarder une vidéo</li><li>**playable :** un bloc de publicités contenant un aperçu interactif de l'expérience de l'app</li><li>**sponsor\_contenu :** un lien inclus dans un extrait de contenu sponsorisé, comme un article publicitaire</li><li>**audio :** une publicité audio</li></ul> | Oui | Oui |
| imei | SDK | Oui | A unique number used to identify mobile phones | Oui |  |

### Macros d'évènements in-app uniquement

Les exemples suivant concernent les postbacks d'événement in-app qui sont disponibles pour les partenaires.

> 📄 **Exemple**
>
> Le modèle de postback d'événement "&event=(event)&json=(encode)" a été traduit dans le postback suivant pour un événement af\_purchase spécifique :
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> La valeur JSON décodée de ce postback est
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

#### **Valeurs chiffrées**

Les postbacks peuvent contenir des caractères spéciaux, c'est à dire non alphanumériques. Pour transférer ces valeurs via postback sans les altérer, AppsFlyer encode les valeurs qui ne sont pas alphanumériques.

Pour décoder ou encoder un postback, utilisez un <Anchor target="_blank" href="https://www.urldecoder.org/">service d'encodage web.</Anchor>

### Exemple de postbacks

### Exemples de postbacks d'installations

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)
&advertising_id=(advertiser_id)&android_id=(android_id)
&install_time=(install_unix_ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?&site_id=(publisher_id)&
device_ip=(ip)&;idfa=(idfa)&install_time=(install_unix_ts)
```

</Tab>
</Tabs>

### Exemples de postbacks d'événements in-app

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)&
device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android_id)&
install_time=(install_unix_ts)&event_name=(event_name)&currency=(currency)&
json=(event_value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?clickid=(clickid)&site_id=(publisher_id)&
device_ip=(ip)&idfa=(idfa)&install_time=(install_unix_ts)
&event_name=(event_name)&currency=(currency)&json=(event_value)
```

</Tab>
</Tabs>

### Exemple de postback d'événement in-app

Paramètres d'événements :

* Nom de l'événement : af\_revenue
* Revenu de l'événement : 120.00
* Devise de l'événement : USD
* Valeur de l'événement : `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

Postback :

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```