---
title: Интеграция Voluum с AppsFlyer
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
  created_at: '2016-01-11T14:46:09Z'
  edited_at: '2026-09-02T00:39:14Z'
  id: 207274016
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/207274016
---
> **Краткий обзор:** Рекламные сети, использующие Voluum, могут воспользоваться решением AppsFlyer для вероятностного моделирования, чтобы получать данные атрибуции об установках и событиях в приложении.

## Начало интеграции

Чтобы начать интеграцию, вы должны отправить в AppsFlyer ссылку атрибуции и постбэк для отчетности.

Ниже вы найдете базовую ссылку атрибуции с подробным объяснением каждого параметра:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| Базовый URL-адрес AppsFlyer | Description(Описание) |
| --- | --- |
| https://app.appsflyer.com | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения — динамическое значение, изменяемое для каждого продвигаемого приложения |
| pid= | Имя медиаисточника включает **\_int** для идентификации **интегрированной** сети на серверах AppsFlyer |
| c= | Доступно только в <Anchor target="_blank" href="/marketers/ru/docs/about-data-locker-advanced-reports">расширенных отчётах</Anchor>. |

**Рекомендуемые параметры ссылки атрибуции:**

| Параметр AppsFlyer | Макросы Voluum | Description(Описание) |
| --- | --- | --- |
| &clickid= | `{clickid}` | Уникальный идентификатор транзакции пользовательской сессии — **обязательно** |
| &af\_siteid= | `{trafficsource.id}` | Идентификатор источника трафика — **необязательно** |

** Полный список параметров AppsFlyer можно посмотреть <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">здесь</Anchor>

** Полный список макросов Voluum можно посмотреть <Anchor target="_blank" href="http://feedback.voluum.com/knowledgebase/articles/318681-click-urls">здесь</Anchor>

### Шаблон полной ссылки атрибуции

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

### Постбэки по установкам и внутренним событиям приложения

Глобальный постбэк по установке:

```http
https://{Company-Domain}.voluumtrk.com/postback?cid={clickid}
```

Глобальный постбэк по событиям в приложении:

```http
https://{Company-Domain}.trackvoluum.com/postback?cid={clickid}&payout={monetary}&txid={event-name}
```

** `{Company-Domain}` — идентификатор сети (доменное имя), предоставленный Volumm.  
** txid= Рекламодатель задает его как **Event Tag** на дэшборде AppsFlyer для каждого приложения. Это фактическое название события в приложении.

### Дэшборд AppsFlyer событий в приложении

![Voluum_msc_new_1.png](https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png)  
** По запросу в постбэк может быть добавлена дополнительная информация об атрибуции, например код страны, ID рекламы, IDFA и т.д.

## Завершение регистрации

* Если у вас есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламных партнеров <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

<div data-zendesk-anchors="starting-the-integration=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 01JFT0VZZ5KVMKYRD222JT55NH=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 complete-attribution-link-template=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT0VZZ7B1RRY82B65GWF4P7=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 install-and-inapp-event-postbacks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JFT0VZZ86KYXSVE1QBD2V0HF=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F appsflyers-inapp-event-dashboard=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-appsflyer-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 01JFT0VZZ9A4JWG38KPH0CNQ72=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-appsflyer-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 finalizing-your-registration=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8 01JFT0VZZATFYY75QPCPKZF3S6=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8" />
