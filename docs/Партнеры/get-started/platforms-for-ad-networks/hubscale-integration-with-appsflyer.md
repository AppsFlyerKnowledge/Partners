---
title: Интеграция Hubscale с AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Hubscale
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
  created_at: '2017-12-19T12:25:07Z'
  edited_at: '2026-10-19T14:36:44Z'
  id: 115005874869
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/115005874869
---
> **Краткий обзор:** Узнайте, как рекламные сети, использующие Hubscale, могут интегрироваться с AppsFlyer.

**Чтобы инициировать интеграцию, вам нужно отправить AppsFlyer**:

1. Ваша ссылка для атрибуции
2. Ваш постбэк (для установок и событий в приложении)

<div id="creating-the-attribution-link" />

## Создание ссылки атрибуции

ссылка атрибуции состоит из базовой ссылки атрибуции AppsFlyer, приведенной ниже, и дополнительных макросов, добавленных рекламной сетью.

Ниже приведена базовая ссылка атрибуции AppsFlyer с подробным объяснением каждого макроса:

| Базовый URL-адрес AppsFlyer | Description(Описание) |
| --- | --- |
| https://app.appsflyer.com | Конечная точка AppsFlyer |
| app\_id (идентификатор приложения) | Уникальный идентификатор приложения — динамическое значение, изменяемое для каждого продвигаемого приложения |
| pid | Имя медиаисточника с добавлением \_int для идентификации интегрированных сетей |
| c | Название кампании |

Ниже показано, как должна выглядеть полная ссылка атрибуции после добавления дополнительных макросов Hubscale:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={affiliate_id}&af_sub5={offer_id}af_ad_id=
{offer_file_id}&advertising_id={google_aid}&idfa={ios_ifa}" target="
_blank" rel="nofollow noopener noreferrer" data-is-link="https://
app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={transaction_id}
&af_siteid={affiliate_id}&af_sub5={offer_id}af_ad_id={offer_file_id}
&advertising_id={google_aid}&idfa={ios_ifa}">
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id=
{google_id}&idfa={ios_ifa}
```

<Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">Полный список параметров AppsFlyer</Anchor>

<div id="global-postbacks-for-installs-and-in-app-events" />

## Глобальные постбэки для установок и событий в приложении:

В Hubscale есть глобальные постбэки для установок и событий в приложении:

Для установок:

```http
https://companyname.156th.com/conv?transaction_id={publisher_ref_id}&ios_ifa={ios_ifa}
&google_id={google_aid}&app_version={app_version}&language={language}&ext_country_code={country_code}
&ext_city={city}&user_agent={user_agent}&user_ip={device_ip}&adv_revenue={revenue_usd}
```

Для событий после установки, Hubscale может регистрировать до девяти событий после установки для одного и того же идентификатора ID транзакции. Ниже показано, как создать девять глобальных постбэков в виде шаблонов:

<Table>
  <thead>
    <tr>
      <th>
        Номер события
      </th>
      <th>
        Шаблон URL-адреса
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Событие 2 (событие 1 — это установка)
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=2
        ```
      </td>
    </tr>
    <tr>
      <td>
        Событие 3
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=3
        ```
      </td>
    </tr>
    <tr>
      <td>
        Событие 4
      </td>
      <td>
        ...
      </td>
    </tr>
    <tr>
      <td>
        ...
      </td>
      <td>
        ...
      </td>
    </tr>
    <tr>
      <td>
        Событие 10
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=10
        ```
      </td>
    </tr>
  </tbody>
</Table>

Тег события — это значение, которое рекламодатель вводит при сопоставлении событий.

<Image align="center" alt="In-App_Events.png" src="https://files.readme.io/5fa9ea3c2428e0dce7ce6a8062ebdf9aca5b2f873cc4e3d76d815d83b3a72b64-360002301369.png" />

Если имя партнера, использующего Hubscale, — PARTNER, то домен обычно будет таким: partner.156th.com.

Общая ссылка атрибуции:

```http
https://app.appsflyer.com/com.appsflyer?pid=partnername_int&clickid={transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id={google_id}&idfa={ios_ifa}
```

<div id="finalizing-your-registration" />

## Завершение регистрации

* Если у вас есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламного партнера <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

<div id="mapping-of-appsflyer-parameters-and-hubscale-macros" />

## Сопоставление параметров AppsFlyer и макросов Hubscale

| Параметры AppsFlyer | Макросы Hubscale | Обзор |
| --- | --- | --- |
| pid | pub\_id | Название медиаисточника — для интегрированных партнеров  <br />и не должно изменяться. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#partner-id-pid-parameter">Подробнее</Anchor>. |
| c | campaign\_name | Имя кампании — предоставляется рекламодателем. |
| clickid | идентификатор\_транзакции | Уникальный идентификатор кликов для рекламной сети |
| af\_siteid | pub\_id | ID издателя в рекламной сети |
| af\_sub\_siteid | sub\_pub\_id | ID рекламной субсети или издателя. |
| af\_c\_id | campaign\_id (идентификатор кампании) | ID кампании — предоставляется производителем рекламы. |
| af\_adset |  | Название группы объявлений — предоставляется рекламодателем. Адсет  <br />— это промежуточный уровень в иерархии между  <br />кампанией и рекламным объявлением. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#уровни-детализации-данных">Подробнее</Anchor> |
| af\_ad | adv\_name | Название рекламного объявления (<Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#уровни-детализации-данных">см. подробнее</Anchor>) |
| af\_ad\_id | adv\_id | Идентификатор |
| af\_cost\_model | adv\_payout\_model | Модель стоимости — CPI в настоящее время является единственной поддерживаемой  <br />моделью |
| af\_cost\_currency | adv\_payout\_currency | Код валюты (например, USD). |
| af\_cost\_value | adv\_payout\_amount | Значение стоимости |

<div data-zendesk-anchors="creating-the-attribution-link=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01JFT1EB6KZE1D6C9HMXQ5A841=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 global-postbacks-for-installs-and-inapp-events=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 01JFT1EB6PH56T619J1197TAK2=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 finalizing-your-registration=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8 01JFT1EB70G5V9EBMD4XMAR3GF=%D0%B7%D0%B0%D0%B2%D0%B5%D1%80%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%B3%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%86%D0%B8%D0%B8 mapping-of-appsflyer-parameters-and-hubscale-macros=%D1%81%D0%BE%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2-appsflyer-%D0%B8-%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D0%B2-hubscale 01JFT1EB71F36JD4QNB8KHKZRX=%D1%81%D0%BE%D0%BF%D0%BE%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D0%BE%D0%B2-appsflyer-%D0%B8-%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D0%B2-hubscale" />
