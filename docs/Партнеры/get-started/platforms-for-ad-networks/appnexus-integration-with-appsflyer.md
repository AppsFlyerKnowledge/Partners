---
title: Интеграция AppNexus с AppsFlyer
metadata:
  keywords:
    - Integration
    - AppNexus
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
  created_at: '2016-01-11T14:45:34Z'
  edited_at: '2026-10-19T14:36:28Z'
  id: 207583523
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/207583523
---
> **Краткий обзор:** Рекламные сети, использующие Affise, могут воспользоваться решением AppsFlyer для вероятностного моделирования, чтобы получать данные атрибуции об установках и событиях в приложении.

## Начало интеграции

Чтобы начать интеграцию, вы должны отправить в AppsFlyer ссылку атрибуции и постбэк для отчетности.

Ниже вы найдете базовую ссылку атрибуции с подробным объяснением каждого параметра:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| Базовый URL-адрес AppsFlyer | Description(Описание) |
| --- | --- |
| https://app.appsflyer.com | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения — динамическое значение, изменяемое для каждого продвигаемого приложения |
| pid | Имя медиа-источника включает **\_int** для идентификации **интегрированной** сети на серверах AppsFlyer |
| c | Название кампании |

**Макросы рекламного идентификатора AppNexus**

| Операционная система | Макрос |
| --- | --- |
| Android; | &advertising\_id=$`{DEVICE_AAID}` |
| https://support.appsflyer.com/hc/article_attachments/360016192917 | idfa=$`{DEVICE_APPLE_IDA}` |

**Рекомендуемые параметры ссылки атрибуции**

| Параметр AppsFlyer | Макросы AppNexus | Description(Описание) |
| --- | --- | --- |
| clickid | $`{SSP_DATA}` | Идентификатор запроса для каждой пользовательской сессии — **обязательно** |
| af\_siteid | $`{PUBLISHER_ID}` | Идентификатор партнера, продвигающего оффер — **необязательно** |

Полный список параметров AppsFlyer можно посмотреть <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">здесь</Anchor>.

Полный список макросов AppNexus можно посмотреть <Anchor target="_blank" href="https://wiki.appnexus.com/display/sdk/Welcome">здесь</Anchor>.

### Шаблон полной ссылки атрибуции:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=${SSP_DATA}&af_siteid=${PUBLISHER_ID}
```

### Постбэки по установкам и внутренним событиям приложения

Глобальный постбэк по установке:

```http
https://sspx-router.adnxs.net/sspx?id={ID}&sspdata={clickid}
```

`{ID}` — идентификатор сети, предоставленный AppNexus и добавляемый в дэшборде AppsFlyer для каждого приложения.

### Дэшборд установок AppsFlyer

[![appnexus-pixelid.png](https://files.readme.io/0f14632fc7421fbbb26f90c13cc37afad58e4e217f4bcebd931cddb7576c5113-360018728918.png)](https://support.appsflyer.com/hc/article_attachments/49929594144273)

По запросу в постбэк можно добавить дополнительную информацию об атрибуции, например код страны, рекламный идентификатор, IDFA и т. д.

## Завершение регистрации

* Если у вас есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламного партнера <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

<div data-zendesk-anchors="starting-the-integration=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 01JFT0Z4H4N0SFK6CAKQGW41Q4=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 complete-attribution-link-template=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT0Z4H7MA1B9FMNWKESF170=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 install-and-inapp-event-postbacks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JFT0Z4H7TZPQCFGZCASNWHD7=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F appsflyer-install-dashboard=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-appsflyer 01JFT0Z4H89BP3YWFRSJ69RK6D=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-appsflyer finalizing-your-registration=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8 01JFT0Z4H9TF582WHB69MT9VP2=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8" />
