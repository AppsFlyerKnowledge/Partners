---
title: Интеграция TUNE (ранее HasOffers) с AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Tune
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
  created_at: '2015-12-22T14:55:13Z'
  edited_at: '2026-09-02T00:39:09Z'
  id: 207034806
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/207034806
---
> **Кратко:** Узнайте, как рекламные сети, которые используют TUNE (ранее HasOffers) для управления партнерскими маркетинговыми кампаниями, могут интегрироваться с AppsFlyer и получать данные атрибуции об установках и событиях в приложении.

**Чтобы начать интеграцию, подготовьте и отправьте в AppsFlyer следующую информацию:**

1. Ваша [ссылка атрибуции](/docs/tune-formerly-hasoffers-integration-with-appsflyer#создать-ссылку-атрибуции)
2. Ваши [постбэки](/docs/tune-formerly-hasoffers-integration-with-appsflyer#создайте-постбэки-по-установкам-и-событиям-в-приложении) (для установок и событий в приложении)

<div id="create-attribution-link" />

## Создать ссылку атрибуции

Ссылка атрибуции состоит из базовой ссылки атрибуции AppsFlyer и дополнительных макросов, добавленных рекламной сетью.

Ниже приведена базовая ссылка атрибуции AppsFlyer с подробным объяснением каждого макроса:

| Базовый URL-адрес AppsFlyer | Description(Описание) |
| --- | --- |
| https://app.appsflyer.com | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения — динамическое значение, которое меняется для каждого продвигаемого приложения |
| pid= | Название медиаисточника, объединенное с `_int`, для идентификации интегрированных сетей |
| c= | Доступно только в <Anchor target="_blank" href="/marketers/ru/docs/about-data-locker-advanced-reports">расширенных отчётах</Anchor>. |

<div id="example-attribution-link-after-adding-tune-macros" />

### Пример ссылки атрибуции после добавления макросов TUNE

```
 
```

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={affiliate_id}&af_c_id={offer_id}&af_ad_id={offer_file_id}&idfa=
{ios_ifa}&advertiser_id={google_aid}&af_sub5={offer_id}
```

* В предыдущую ссылку был добавлен параметр `af_sub5={offer_id}` для целей отчетности TUNE.

Подробнее о [макросах TUNE](https://help.tune.com/hasoffers/parameters-macros-in-hasoffers/).

<div id="create-install-and-in-app-event-postbacks" />

## Создайте постбэки по установкам и событиям в приложении

Пошаговые инструкции по созданию постбэков для установок и событий в приложении:

1. Создайте или выберите оффер, в котором используется протокол Postback w/Transaction ID.
2. В разделе сведений на странице оффера нажмите ссылку **Tracking**.
3. Скопируйте URL-адрес из поля **Postback URL**.
4. Удалите параметр `offer_id` и его значение из URL-адреса постбэка, чтобы преобразовать его из специального постбэка в глобальный постбэк.

Узнайте больше о [глобальных URL-адресах постбэков TUNE](http://help.tune.com/hasoffers/global-postback-urls/).

<div id="sample-postbacks" />

### Примеры постбэков

<div id="global-install-postback" />

#### Глобальный постбэк по установке:

```
 
```

```http
https://NETWORK_ID.go2cloud.org/aff_lsr?offer_id={af_c_id}&transaction_id={clickid}
```

<div id="in-app-event-postback" />

#### Постбэк по внутреннему событию:

```
 
```

```http
https://NETWORK_ID.go2cloud.org/aff_goal?a=lsr&goal_id={goal_id}&transaction_id={clickid}
```

В приведенных выше URL-адресах постбэка:

* NETWORK\_ID = доменное имя (ID сети), предоставленное TUNE
  * Чтобы обеспечить корректную атрибуцию, в качестве NETWORK\_ID всегда следует использовать фирменное доменное имя, предоставленное TUNE, а не пользовательский домен отслеживания, используемый для конкретного оффера (если применимо).
* goal\_id = тег события в дэшборде AppsFlyer для каждого из ваших приложений. Это фактическое название события в приложении.

Узнать больше о <Anchor target="_blank" href="/partners/ru/docs/dynamic-event-mapping-for-in-app-events">динамическом сопоставлении событий для событий в приложении</Anchor>.

<div id="finalizing-your-registration" />

## Завершение регистрации

* Если у вас есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламного партнера <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

<div data-zendesk-anchors="create-attribution-link=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 h_01ET22GJ5N67DKECBQ41QEPEAT=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D1%82%D1%8C-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D1%83-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 example-attribution-link-after-adding-tune-macros=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D0%B2-tune 01JFT1MXJJF3C17B3Y9Q8604BM=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D0%B2-tune create-install-and-inapp-event-postbacks=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%B9%D1%82%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 h_01ET22H0A0MQ3HH30AJ1TMFNTQ=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%B9%D1%82%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 sample-postbacks=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 01JFT1MXJNSTV7YRVX3BPZ50CY=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 global-install-postback=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 01JFT1MXJNJBY1P51JQ3ES7QYS=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 inapp-event-postback=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B5%D0%BC%D1%83-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E 01JFT1MXJNMF0FWJ2RFER3E316=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B5%D0%BC%D1%83-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E finalizing-your-registration=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8 01JFT1MXJQAXV53RKACW0VAS6E=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8" />
