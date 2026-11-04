---
title: Интеграция Trackier с AppsFlyer
metadata:
  keywords:
    - AdNetwork Integration
    - ad networks
    - Advertisers
    - ad network
    - Partners
    - trackier
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
  created_at: '2020-02-24T13:25:45Z'
  edited_at: '2026-09-02T00:39:07Z'
  id: 360006111917
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/360006111917
---
> **Кратко:** рекламные сети, использующие Trackier, могут получать от AppsFlyer данные атрибуции об установках и событиях в приложении.

Чтобы начать интеграцию, предоставьте AppsFlyer URL-адрес ссылки атрибуции и URL-адрес постбэка. Эти URL-адреса нужны для отчетности. В этой статье объясняется, как создать эти URL-адреса.

<div id="attribution-link-url" />

## URL-адрес ссылки атрибуции

В этом разделе приведены базовая ссылка атрибуции и описания связанных параметров.

<div id="base-attribution-link-url" />

### Базовый URL-адрес ссылки атрибуции

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={click_id}&af_siteid={publishedr_id}
&af_c_id={camp_id}
```

| Базовый URL-адрес AppsFlyer | Определение | Description(Описание) |
| --- | --- | --- |
| https://app.appsflyer.com | Базовый URL-адрес | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Идентификатор приложения | Динамическое значение, различающееся для каждого приложения |
| pid= | Название медиаисточника | **\_int** обозначает **интегрированную** сеть |
| c= | Доступно только в <Anchor target="_blank" href="/marketers/ru/docs/about-data-locker-advanced-reports">расширенных отчётах</Anchor>. | Имя, заданное рекламодателем |

<div id="attribution-link-parameters" />

### Параметры ссылки атрибуции

<div id="note" />

> 📘 **Примечание**
>
> Ссылки атрибуции в следующей таблице **обязательны**.
>
> См. полные списки параметров для:
>
> * <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">AppsFlyer:</Anchor>
> * <Anchor target="_blank" href="https://trackier.com/support/kb/tracking-macros/">Trackier</Anchor>

| Параметр AppsFlyer | Макрос Trackier | Description(Описание) |
| --- | --- | --- |
| &clickid= | `{click_id}` | Запрашивает идентификатор для каждой сессии пользователя |
| &af\_siteid= | `{publisher_id}` | Идентификатор партнера, продвигающего предложение |
| &af\_c\_id= | `{camp_id}` | Тип конверсии, который был зафиксирован в системе AppsFlyer из-за действий пользователя, связанных с [conversion\_name](#attribution::942d31ab). |

<div id="postback-urls-for-install-and-in-app-events" />

## URL-адреса постбэков для установок и событий в приложении

В этом разделе приведены примеры URL-адресов постбэка и параметров для установки и событий в приложении.

<div id="ios-postback-urls" />

### URL-адреса постбэка **iOS**

<div id="global-install-postback" />

#### Глобальный постбэк по установке

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&idfa={idfa}
```

<div id="global-in-app-event-postback" />

#### Глобальные постбэки от событий внутри приложения

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&idfa={idfa}&goal_value={event-name}
```

<div id="android-postback-urls" />

### URL-адреса постбэка **Android**

<div id="global-install-postback-1" />

#### Глобальный постбэк по установке

```http
https://yourdomain.com/acquisition?click_id={clickid}&security_token=xxxxxxxxxxxxxxx&gaid={android_id}
```

<div id="global-in-app-event-postback-1" />

#### Глобальные постбэки от событий внутри приложения

```http
https://yourdomain.com/acquisition?click_id={click_id}&security_token=xxxxxxxxxxxxxxx&gaid={android_id}&goal_value={event-name}
```

<div id="postback-parameters" />

### Параметры постбэка

| Базовый URL-адрес AppsFlyer | Description(Описание) |
| --- | --- |
| yourdomain.com | <ul><li>Название сети (домен) и идентификатор ID</li><li>Предоставляется Trackier</li></ul> |
| название события | <ul><li>"event\_name"</li><li>Определяется рекламодателем</li></ul> |
| security\_token | Предоставляется Trackier |
| Код страны, рекламный идентификатор, IDFA и т. д. | [Необязательно] Информация об атрибуции, которую можно добавить в постбэк |

<div id="finalizing-your-registration" />

## Завершение регистрации

Уже интегрированы с AppsFlyer? Отправьте нам URL-адреса через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.

Еще не интегрированы с AppsFlyer? Заполните <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">заявку на регистрацию партнеров по рекламе</Anchor>.

<div data-zendesk-anchors="attribution-link-url=url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT1SETSSMD0Z0EEQZCYPDB6=url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 base-attribution-link-url=%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9-url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT1SETTCEC1CAGT89SGNZNX=%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D1%8B%D0%B9-url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 attribution-link-parameters=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT1SEVJTM09KHEKS51KQB7F=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT1SEVJR7TW06CAZWGMBZEB=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 postback-urls-for-install-and-inapp-events=url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 01JFT1SEWCM9DFRANRJRDSG5DC=url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 ios-postback-urls=url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-ios 01JFT1SEWCSS585NF8P0T251PZ=url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-ios global-install-postback=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 01JFT1SEWD3A0JP6MRM1QXKX53=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 global-inapp-event-postback=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BE%D1%82-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JFT1SEWDT1CWHHTVWVACDT0B=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BE%D1%82-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F android-postback-urls=url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-android 01JFT1SEWD0HA5WKC83V8HYAA2=url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-android global-install-postback::1726dfc2=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5-1 01JFT1SEWDY7882HGY032SPGP7=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5-1 global-inapp-event-postback::ab23c9cb=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BE%D1%82-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-1 01JFT1SEWDYKTWDE536A4ZY34G=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BE%D1%82-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-1 postback-parameters=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0 01JFT1SEWEZQF38K9V9M6TNP3N=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0 finalizing-your-registration=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8 01JFT1SEWTPX9BH7N1FPN4NJJW=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8" />
