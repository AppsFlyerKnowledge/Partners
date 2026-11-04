---
title: Интеграция Offerslook с AppsFlyer для рекламных сетей
metadata:
  keywords:
    - Offerslook
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
  created_at: '2016-05-31T08:47:36Z'
  edited_at: '2026-09-02T00:39:00Z'
  id: 209074606
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/209074606
---
> **Кратко:** Узнайте, как рекламные сети, использующие Offerslook, могут интегрироваться с AppsFlyer и получать данные атрибуции установок.

Чтобы начать интеграцию, отправьте в AppsFlyer:

1. Ваша ссылка атрибуции

   ```http
   https://networkname.offerstrack.net/index.php?offer_id={offer_id}&aff_id={aff_id}
   ```
2. Ваш постбэк (для установок)  

   ```http
   https://networkname.offerstrack.net/advBack.php?click_id={click_id}&adv_id={adv_id}
   ```

<div id="creating-your-attribution-link" />

## Создание ссылки атрибуции

Ссылка атрибуции состоит из базовой ссылки атрибуции AppsFlyer, приведенной ниже, и дополнительных макросов, добавленных рекламной сетью.

Ниже приведена базовая ссылка атрибуции AppsFlyer с подробным объяснением каждого макроса:

| Базовый URL-адрес AppsFlyer | Description(Описание) | Offerslook |
| --- | --- | --- |
| http://app.appsflyer.com | Конечная точка AppsFlyer |  |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения — динамическое значение, изменяемое для каждого продвигаемого приложения |  |
| pid= | Название медиаисточника с добавлением \_int для идентификации интегрированных сетей |  |
| c= | Доступно только в <Anchor target="_blank" href="/marketers/ru/docs/about-data-locker-advanced-reports">расширенных отчётах</Anchor>. | `{offer_id}` |

Ниже приведен пример ссылки атрибуции после добавления дополнительных макросов Offerslook:

```http
  https://app.appsflyer.com/com.
  
  appsflyer?pid=mediaName_int&
  
  clickid={click_id}&af_siteid={
  
  aff_id}&advertising_id={ga_id}
  
  &idfa={idfa}
```

Полный список параметров AppsFlyer доступен <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">здесь</Anchor>.

Доступные макросы в ссылках атрибуции AppsFlyer

В сгенерированной ссылке можно использовать следующие макросы:

| **Название макроса** | **Description(Описание)** | **Offerslook** |
| --- | --- | --- |
| pid | Название медиаисточника — предоставляется AppsFlyer и не должно изменяться |  |
| c | Доступно только в <Anchor target="_blank" href="/marketers/ru/docs/about-data-locker-advanced-reports">расширенных отчётах</Anchor>. |  |
| clickid | Уникальный идентификатор кликов для рекламной сети | `{click_id}` |
| af\_siteid | Идентификатор паблишера в рекламной сети | `{aff_id}` |

<div id="new-macros" />

#### Новые макросы

Новый набор макросов добавляет ряд дополнительных параметров в понятном, стандартизированном и структурированном виде. Мы настоятельно рекомендуем использовать эти макросы, прежде чем возвращаться к макросам af\_sub1–5.

| **Название макроса** | **Description(Описание)** | **Offerslook** |
| --- | --- | --- |
| af\_c\_id | ID кампании — предоставляется производителем рекламы. | `{adv_sub1}<br /><br />{adv_sub2}<br /><br />{adv_sub3}` |
| af\_adset | Название адсета — предоставляется рекламодателем. Адсет — это промежуточный уровень в иерархии между **кампанией** и **рекламным объявлением**. |  |
| af\_adset\_id | идентификатор группы объявлений (adset); |  |
| af\_ad | Название рекламного объявления |  |
| af\_ad\_id | Идентификатор |  |
| af\_ad\_type | Тип рекламы — любое описание формата рекламы (например, «видео» или «баннер», «средний размер» или «большой размер») |  |
| af\_channel | Канал, через который распространяется реклама (например, YouTube или Google Search) |  |
| af\_keywords | Список ключевых слов для SMS кампаний. |  |
| af\_cost\_model | Модель затрат — в настоящее время поддерживается CPI, и это модель по умолчанию. Значения CPC и CPA также допустимы. | `{pricing_type}` |
| af\_cost\_currency | Код валюты (например, USD). | `{currency}` |
| af\_cost\_value | Значение стоимости | `{revenue}` |

**Макросы для Android**

| **Название макроса** | **Description(Описание)** | **Offerslook** |
| --- | --- | --- |
| android\_id | Устройство Android\_id — требуется поддержка рекламной сети | `{android_id}` |
| sha1\_android\_id | Устройство Android\_id, хешированный с помощью SHA1 — требуется поддержка рекламной сети |  |
| рекламный\_идентификатор | Рекламный идентификатор Google — требуется поддержка рекламной сети | `{ga_id}` |
| sha1\_advertising\_id | Рекламный идентификатор Google, хешированный с помощью SHA1 — требуется поддержка рекламной сети |  |
| af\_r | Только вне магазина — целевой URL-адрес перенаправления. |  |
| sha1\_el | Используется для атрибуции с компьютера на мобильное устройство — адрес электронной почты, хэшированный с помощью SHA1; требуется поддержка рекламной сети |  |

**Макросы, специфичные для iOS**

| **Название макроса** | **Description(Описание)** | **Offerslook** |
| --- | --- | --- |
| IDFA | ID производителя рекламы Apple — указывается в верхнем регистре, требуется поддержка рекламной сети. | `{idfa}` |
| sha1\_idfa | ID производителя рекламы Apple, хешированный с SHA1 — требуется поддержка рекламной сети. |  |
| mac | Mac-адрес устройства — требуется поддержка рекламной сети. | `{mac}` |
| sha1\_mac | Mac-адрес устройства, хешированный с SHA1 — требуется поддержка рекламной сети. |  |

<div id="creating-your-install-postbacks" />

## Создание постбэков об установке

Ниже приведено пошаговое описание того, как создать постбэки об установке на платформе Offerslook:

1. Создайте или выберите оффер, использующий протокол Postback w/Transaction ID
2. В разделе сведений на странице предложения нажмите ссылку «отслеживание»
3. Скопируйте URL-адрес постбэка, указанный в поле «URL-адрес постбэка»
4. Удалите параметр offer\_id и его значение из URL-адреса постбэка, чтобы преобразовать определенный постбэк в глобальный постбэк

Глобальный постбэк по установке:

`http://{networkname}.offerstrack.net/advBack.php?click_id={click_id}&adv_id={adv_id}`

`networkname` — это доменное имя, предоставленное Offerslook.

**Завершение регистрации**

* Если у вас есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламного партнера <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

<div data-zendesk-anchors="creating-your-attribution-link=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT1JFND230EFDBRTWNKXKSH=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 new-macros=%D0%BD%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B 01JFT1JFP8T3HF5GQBR19YHQW5=%D0%BD%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B creating-your-install-postbacks=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%BE%D0%B1-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 01JFT1JFP9BMZM99TKDR58FNZP=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%BE%D0%B1-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5" />
