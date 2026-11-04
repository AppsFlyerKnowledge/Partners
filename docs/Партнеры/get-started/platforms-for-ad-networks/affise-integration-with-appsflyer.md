---
title: Интеграция Affise с AppsFlyer
metadata:
  keywords:
    - Integration
    - affise
    - Advertisers
    - Ad Networks
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
  created_at: '2016-04-19T12:08:58Z'
  edited_at: '2026-10-19T14:36:26Z'
  id: 208537116
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/208537116
---
> **Краткий обзор:** Рекламные сети, использующие Affise, могут использовать решение AppsFlyer для вероятностного моделирования, чтобы получать данные атрибуции об установках и событиях в приложении.

Чтобы начать интеграцию, вы должны отправить в AppsFlyer ссылку атрибуции и постбэк для отчетности.

<div id="base-attribution-link" />

## Базовая ссылка атрибуции

Ниже вы найдете базовую ссылку атрибуции с подробным объяснением каждого параметра:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}&af_c_id={offerid}
```

**Обязательные параметры ссылки атрибуции**

| Параметр AppsFlyer | Макросы Affise | Описание |
| --- | --- | --- |
| clickid | `{clickid}` | Идентификатор запроса для каждой пользовательской сессии |
| af\_siteid | `{pid}` | Идентификатор партнера, продвигающего оффер |
| af\_c\_id | `{offer_id}` | Идентификатор оффера |

Полный список параметров AppsFlyer можно посмотреть <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">здесь</Anchor>.

<div id="complete-attribution-link-template" />

## Шаблон полной ссылки атрибуции

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={pid}
```

<div id="install-and-in-app-event-postbacks" />

## Постбэки по установкам и внутренним событиям приложения

Ниже приведены примеры постбэков по установкам и событиям в приложении:

<div id="global-install-postback-ios" />

### Глобальный постбэк по установке iOS

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}
```

<div id="global-install-postback-android" />

### Глобальный постбэк по установке Android

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}
```

<div id="global-in-app-event-postback-ios" />

### Глобальный постбэк по событию в приложении iOS

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&ios_idfa={idfa}&goal={event-name}
```

<div id="global-in-app-event-postback-android" />

### Глобальный постбэк по событию в приложении Android

```http
https://domain.com/postback?clickid={clickid}&action_id={eventtime}&android_id={android_id}&goal={event-name}
```

Domain.com — это имя идентификатора сети (домена), предоставленное Affise.

e= задается как **Event Name** в дэшборде AppsFlyer для каждого приложения рекламодателем — это фактическое название события в приложении из приложения.

По запросу в постбэк может быть добавлена дополнительная информация об атрибуции, например код страны, рекламный идентификатор, IDFA и т. д.

<div id="finalizing-your-registration" />

## Завершаем вашу регистрацию

* Если у вас есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощника для партнеров</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламного партнера <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

<div data-zendesk-anchors="base-attribution-link=%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT0RZG0F67JFBC7W5KK54BM=%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 complete-attribution-link-template=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT0RZG2QTT3Z9S6SVNV5VE7=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 install-and-inapp-event-postbacks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JFT0RZG3C7MBBYFKA6W813PF=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F global-install-postback-ios=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5-ios 01JFT0RZG3HM9P81XYGKHZXHFK=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5-ios global-install-postback-android=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5-android 01JFT0RZG4JCDP8D4CWQW02AY7=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5-android global-inapp-event-postback-ios=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8-ios 01JFT0RZG40N0VNNVMDBFYNT9E=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8-ios global-inapp-event-postback-android=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8-android 01JFT0RZG4PA9WTP212AX52QWZ=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8-android finalizing-your-registration=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B0%D0%B5%D0%BC-%D0%B2%D0%B0%D1%88%D1%83-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8E 01JFT0RZG52JW6C5GR0KA4CZF6=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B0%D0%B5%D0%BC-%D0%B2%D0%B0%D1%88%D1%83-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D1%8E" />
