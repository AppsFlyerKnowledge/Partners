---
title: Интеграция PeerClick с AppsFlyer
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
  created_at: '2024-01-07T08:27:18Z'
  edited_at: '2026-08-18T00:41:41Z'
  id: 21479841979793
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/21479841979793
---
> **Краткий обзор.** Рекламные сети, использующие PeerClick, могут воспользоваться решением AppsFlyer для вероятностного моделирования, чтобы получать данные об атрибуции установок и событий в приложении.

<div id="starting-the-integration" />

## Начало интеграции

Чтобы начать интеграцию, вы должны отправить в AppsFlyer ссылку атрибуции и постбэк для отчетности.

Ниже вы найдете базовую ссылку атрибуции с подробным объяснением каждого параметра:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| Базовый URL-адрес AppsFlyer | Описание |
| --- | --- |
| https://app.appsflyer.com | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения — динамическое значение, изменяемое для каждого продвигаемого приложения |
| pid= | Имя медиа-источника включает **\_int** для идентификации **интегрированной** сети на серверах AppsFlyer |
| c= | Название кампании |

**Рекомендуемые параметры ссылки атрибуции:**

| Параметр AppsFlyer | Макросы Voluum | Описание |
| --- | --- | --- |
| &clickid= | `{clickid}` | Уникальный идентификатор транзакции пользовательской сессии — **обязательно** |
| &af\_siteid= | `{trafficsource.id}` | Идентификатор источника трафика — **необязательно** |

<div id="note" />

> 📘 **Примечание**
>
> * Полный список параметров AppsFlyer можно посмотреть <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">здесь</Anchor>
> * Полный список PeerClick можно посмотреть <Anchor target="_blank" href="https://help-center.peerclick.com/en/">здесь</Anchor>

<div id="complete-attribution-link-template" />

### Шаблон полной ссылки атрибуции

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

<div id="install-and-in-app-event-postbacks" />

### Постбэки по установкам и внутренним событиям приложения

**Глобальный постбэк по установке:**

```http
https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}
```

**Глобальный постбэк по событиям в приложении:**

`https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}&payout={monetary}&txid={event-name}`

* **userid:** Идентификатор пользователя, предоставленный PeerClick
* **txid:** Фактическое название события в приложении, установленное рекламодателем в качестве **Event Tag** (тег события) на дэшборде AppsFlyer для каждого приложения.

<div id="appsflyers-in-app-event-dashboard" />

### Дэшборд AppsFlyer событий в приложении

![Voluum_msc_new_1.png](https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png)  
По запросу в постбэк может быть добавлена дополнительная информация об атрибуции, например код страны, ID рекламы, IDFA и т.д.

<div data-zendesk-anchors="starting-the-integration=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 h_01HKHFT3RFWF5H349GP7MHDAYX=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 h_01HM8M27S5WFJVKBG0JAFW548H=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 complete-attribution-link-template=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 h_01HKHFT3RFDW6GZM3E72SYPJSD=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 install-and-inapp-event-postbacks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01HKHFT3RF1PTSJ4SF9RTQ93N8=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F appsflyers-inapp-event-dashboard=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-appsflyer-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 h_01HKHFT3RFDVPCSKJGZPRFB55V=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-appsflyer-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8" />
