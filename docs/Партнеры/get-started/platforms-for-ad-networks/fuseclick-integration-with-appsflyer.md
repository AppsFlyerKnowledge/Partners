---
title: Интеграция Fuseclick с AppsFlyer
metadata:
  keywords:
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
  created_at: '2016-01-11T14:46:45Z'
  edited_at: '2026-09-02T00:38:54Z'
  id: 207583573
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/207583573
---
> **Краткий обзор:** Рекламные сети, использующие FuseClick, могут воспользоваться решением AppsFlyer для вероятностного моделирования, чтобы получать данные атрибуции об установках и событиях в приложении.

## Базовая ссылка атрибуции

Ниже вы найдете базовую ссылку атрибуции с подробным объяснением каждого параметра:

```http
https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}
```

| Базовый URL-адрес AppsFlyer | Description(Описание) |
| --- | --- |
| https://app.appsflyer.com | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения — динамическое значение, изменяемое для каждого продвигаемого приложения |
| pid | Имя медиа-источника включает **\_int** для идентификации **интегрированной** сети на серверах AppsFlyer |
| c | Название кампании |

**Рекомендуемые параметры ссылки атрибуции:**

| Параметр AppsFlyer | Макросы FuseClick | Описание |
| --- | --- | --- |
| clickid | `{TID}` | Идентификатор запроса каждой пользовательской сессии — **обязательно** |
| af\_siteid | `{SC}` | Идентификатор партнера, продвигающего оффер — **необязательно** |

Полный список параметров AppsFlyer можно посмотреть <Anchor target="_blank" href="/partners/ru/docs/postback-macros-for-ad-networks">здесь</Anchor>

Полный список макросов FuseClick можно посмотреть <Anchor target="_blank" href="https://support.fuseclick.com/documentation/open/iwf/2016/0805/199.html">здесь</Anchor>

Шаблон полной ссылки атрибуции:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={TID}&af_siteid={ADV_SID}
```

### Постбэки по установкам и внутренним событиям приложения

Глобальный постбэк по установке:

```
https://tracking.zadsmobile.com/pb?tid={TID}
```

По запросу в постбэк можно добавить дополнительную информацию об атрибуции, например код страны, Advertising ID, IDFA и другое.

## Завершение регистрации

* Если у вас есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламного партнера <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

<div data-zendesk-anchors="basic-attribution-link=%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT0DX287AWQND2BYFSV50HW=%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 install-and-inapp-event-postbacks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JFT0DX2B6FFE3K7VTXG1YVJ1=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F finalizing-your-registration=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8 01JFT0DX2BD8A19BY9197X11QW=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8" />
