---
title: Интеграция FOCUUS с AppsFlyer
metadata:
  keywords:
    - Focuus
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
  created_at: '2016-10-02T05:18:19Z'
  edited_at: '2026-09-02T00:38:51Z'
  id: 213374546
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/213374546
---
> **Краткий обзор:** Рекламные сети, использующие FOCUUS, могут использовать решение AppsFlyer для вероятностного моделирования, чтобы получать данные атрибуции об установках и событиях в приложении.

## Создание собственной ссылки атрибуции

Ссылка атрибуции состоит из приведенной ниже базовой ссылки атрибуции AppsFlyer и дополнительных макросов, добавленных рекламной сетью.

Ниже приведена базовая ссылка атрибуции AppsFlyer с подробным объяснением каждого макроса:

| Базовый URL-адрес AppsFlyer | Description(Описание) |
| --- | --- |
| https://app.appsflyer.com | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения |
| pid | Имя медиа-источника включает \_int для идентификации интегрированной сети на серверах AppsFlyer |
| c | Доступно только в <Anchor target="_blank" href="/marketers/ru/docs/about-data-locker-advanced-reports">расширенных отчётах</Anchor>. |

### Рекомендуемые параметры ссылки атрибуции

| Параметр AppsFlyer | Макросы FOCUUS | Description(Описание) |
| --- | --- | --- |
| **clickid** | **`{tid}`** | **Идентификатор запроса каждой пользовательской сессии** — **Обязательно** |
| af\_siteid | `{publisher_id}` | Идентификатор партнера, продвигающего оффер, — необязательно |

Полный список параметров AppsFlyer можно посмотреть по <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#параметры-ссылки-атрибуции">ссылке</Anchor>.

FOCUUS поддерживает неограниченное количество макросов, и вы можете называть их как угодно; <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#параметры-ссылки-атрибуции">нажмите</Anchor> <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827379-traffic-source-template-tokens-macros">здесь</Anchor>.

### Шаблон полной ссылки атрибуции

`https://app.appsflyer.com/com.appsflyer?pid={traffic_source}&clickid={tid}&af_siteid={publisher_id}`

Эта ссылка атрибуции устанавливается в поле <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827784-adding-a-new-link">назначение</Anchor> вашей кампании FOCUUS.

## Постбэки по установкам и внутренним событиям приложения

Чтобы создать постбэки для установки и событий в приложении в **FOCUUS**

1. Создайте <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827775-events">новое событие</Anchor> (установка и любые другие события в приложении).
2. <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827766-s2s-integration">Сгенерируйте пиксель</Anchor> (постбэк) для внедрения.
3. Скопируйте URL-адрес постбэка, который отображается в поле <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827766-s2s-integration">Server2Server Pixel</Anchor>.
4. Замените TRANSACTION\_ID на макрос AppsFlyer — «**clickid**»  
   `https://pixel.focuusing.com/event.php?type=imp&tid={clickid}`

**Необязательные параметры постбэка**

| Макросы FOCUUS | Description(Описание) | Например |
| --- | --- | --- |
| event\_value | Значение выплаты для каждого типа события | `https://pixel.focuusing.com/event.php?type=cpi&tid={Your_TRANSACTION_ID}&eid=49816&event_value={25}` |

**Название события (установка, регистрация и т. д.) по умолчанию отображается в сгенерированном пикселе. например:**

* `https://traffic.focuusing.com/install?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/conversion?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/ftd?tid={TRANSACTION_ID}`

<div data-zendesk-anchors="creating-your-attribution-link=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT11W3GWZ3QFYPHEZTS7EX7=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 recommended-attribution-link-parameters=%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D1%83%D0%B5%D0%BC%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT11W3QWT08KMGEPGK7MV5R=%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D1%83%D0%B5%D0%BC%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 complete-attribution-link-template=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT11W3Y7HRB7FYS1K173G2W=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D0%BF%D0%BE%D0%BB%D0%BD%D0%BE%D0%B9-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 install-and-inapp-event-postbacks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JFT11W3YMN4RBW0WFTQ9EADK=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%BC-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F" />
