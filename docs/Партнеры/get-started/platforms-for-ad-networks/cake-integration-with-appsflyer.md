---
title: Интеграция Cake с AppsFlyer
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
  created_at: '2016-01-11T14:44:55Z'
  edited_at: '2026-09-02T00:38:43Z'
  id: 207273986
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/207273986
---
> **Кратко:** Рекламные сети, использующие CAKE, могут получать от AppsFlyer данные атрибуции об установках и событиях в приложении.

<div id="base-attribution-link" />

## Базовая ссылка атрибуции

Ниже вы найдете базовую ссылку атрибуции с подробным объяснением каждого параметра:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| Базовый URL-адрес AppsFlyer | Description(Описание) |
| --- | --- |
| https://app.appsflyer.com | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения — динамическое значение, изменяемое для каждого продвигаемого приложения |
| pid | Имя медиа-источника включает **\_int** для идентификации **интегрированной** сети на серверах AppsFlyer |
| c | Название кампании |

<div id="recommended-attribution-link-parameters" />

### Рекомендуемые параметры ссылки атрибуции

| Параметр AppsFlyer | Макросы CAKE | Описание |
| --- | --- | --- |
| clickid | #oreqid# | Идентификатор запроса для каждой пользовательской сессии — **обязательно** |
| af\_siteid | #affid# | Идентификатор партнера, продвигающего предложение, — **необязательно** |

Полный список параметров AppsFlyer можно посмотреть <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">здесь</Anchor>

Полный список макросов CAKE можно посмотреть <Anchor target="_blank" href="https://support.getcake.com/support/solutions/articles/5000566463-tokens">здесь</Anchor>.

<div id="complete-attribution-link-template" />

### Шаблон полной ссылки атрибуции

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#oreqid#
```

<div id="install-and-in-app-event-postbacks" />

## Постбэки по установкам и внутренним событиям приложения

<div id="global-install-postback" />

### Глобальный постбэк по установке

```http
https://{company-domain}.com/p.ashx?f=pb&r=(Click-ID)
```

<div id="global-in-app-event-postback" />

### Глобальные постбэки от событий внутри приложения

```http
Идентификатор ID клика
```

`{Company-Domain}` — название идентификатора сети (домена), предоставленное CAKE.  
e= задается рекламодателем как **Метка события** в дэшборде AppsFlyer для каждого Приложения — это фактическое название события в приложении.  
Чтобы посмотреть полную структуру постбэка CAKE, кликните здесь

<div id="appsflyer-in-app-events-dashboard" />

### Дэшборд AppsFlyer с событиями в приложении

![IAEP.png](https://files.readme.io/3ce734c3930649fdb0b119cd6e12e135e6bcba19225862e9e93b93991451fc8b-360002326529.png)

По запросу в постбэк может быть добавлена дополнительная информация об атрибуции, например код страны, рекламный идентификатор, IDFA и т. д.

<div id="finalizing-your-registration" />

## Завершение регистрации

* Если у вас есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет ассистента партнера</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламного партнера <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

<div data-zendesk-anchors="base-attribution-link=%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01EZPMKP0AFM26H2ZG9FY1D2S4=%D0%B1%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D1%8F-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 recommended-attribution-link-parameters=%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D1%83%D0%B5%D0%BC%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01EZPMKP0A7DBV5KAGZ08C3R49=%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D1%83%D0%B5%D0%BC%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 complete-attribution-link-template=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01EZPMKP0AH1MB0XYE3PXQPP0V=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 install-and-inapp-event-postbacks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01EZPMKP0A2D0PB41GD04HX9JX=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F global-install-postback=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 01EZPMKP0AVAJRP8YM48T4GV47=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 global-inapp-event-postback=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BE%D1%82-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01EZPMKP0AM7JD7HWW7BCJDQF3=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BE%D1%82-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F appsflyer-inapp-events-dashboard=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-appsflyer-%D1%81-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC%D0%B8-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 01EZPMKP0AJTYT0G9E8G833KT0=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-appsflyer-%D1%81-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC%D0%B8-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 finalizing-your-registration=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8 h_01HY03H1PMWZX3T12RZFV15CFE=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8" />
