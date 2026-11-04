---
title: Интеграция Everflow с AppsFlyer
metadata:
  keywords:
    - everflow
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2017-11-21T07:36:24Z'
  edited_at: '2026-09-02T00:38:48Z'
  id: 115005709185
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/115005709185
---
> **Кратко:** Everflow — интегрированный партнер AppsFlyer. AppsFlyer отправляет Everflow данные атрибуции по установкам и событиям в приложении.

<div id="initiating-the-integration-with-appsflyer" />

## Настройка интеграции с AppsFlyer

**Чтобы начать интеграцию с AppsFlyer:**

1. Заполните <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">**форму регистрационной информации партнера**</Anchor>.
2. После отправки приведенной выше регистрационной формы вы получите электронное письмо от менеджера по развитию партнерских отношений в течение 24 часов.
3. Ответьте на это электронное письмо, указав имя клиента AppsFlyer, для которого вы проводите онбординг. Отправьте нам следующую информацию с помощью виджета помощника партнера:
   * Название вашей компании
   * Прозрачный логотип
   * Рекомендуемый шаблон ссылки атрибуции Everflow (используйте приведенный ниже шаблон)
   * Для *pid* нужно указать выбранное вами имя, которое будет отображаться в отчетах AppsFlyer.
   * Любые дополнительные значения, которые вы хотите использовать.
   * Ваш идентификатор сети Everflow (nid) и домен постбэка для настройки постбэков по установкам и событиям в приложении

<div id="attribution-url-template" />

### Шаблон URL-адреса атрибуции

```http
https://app.appsflyer.com/{app_id}?pid=mediaName_int&clickid={transaction_id}&af_siteid={affiliate_id}
&af_sub_siteid={affiliate_source_id}&idfa={idfa}&sha1_idfa={idfa_sha1}&advertising_id={google_aid}
&af_cost_value={amount}&af_cost_currency={offer_currency}&af_cost_model=CPI
```

Если у вас уже есть интеграция с AppsFlyer, свяжитесь с нами с помощью виджета помощника партнера

 и добавьте новый постбэк Everflow и шаблон ссылки атрибуции.

<div id="creating-your-attribution-link" />

## Создание ссылки атрибуции

Ссылка атрибуции состоит из базовой ссылки атрибуции AppsFlyer и дополнительных макросов, добавленных рекламной сетью, как описано здесь. 

Ниже приведена базовая ссылка атрибуции AppsFlyer с подробным объяснением каждого макроса:

| Базовый URL-адрес AppsFlyer | Описание |
| --- | --- |
| `https://app.appsflyer.com/{app_id}?` | Конечная точка AppsFlyer<br /><br />app\_id = уникальный идентификатор приложения — представляет собой идентификатор продвигаемого приложения |
| pid= | Имя медиаисточника, объединенное с \_int для идентификации интегрированных сетей. Пример: mediaName\_int |
| c= | Доступно только в <Anchor target="_blank" href="/marketers/ru/docs/about-data-locker-advanced-reports">расширенных отчётах</Anchor>. |

Ниже приведена полная ссылка атрибуции после добавления дополнительных макросов Everflow:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={transaction_id}&af_siteid={affiliate_id}
&af_sub_siteid={affiliate_source_id}&idfa={idfa}&sha1_idfa={idfa_sha1}&advertising_id={google_aid}
&af_cost_value={amount}&af_cost_currency={offer_currency}&af_cost_model=CPI
```

<div id="note" />

> 📘 **Примечание:**
>
> * Для моделей стоимости кампании, отличных от CPI, обновите параметр **&af\_cost\_model=**, указав соответствующую модель. Пример:  CPA, CPC
> * Если вы уже являетесь партнером AppsFlyer и сейчас переходите на Everflow с другой платформы, обязательно добавьте `&af_additional_postback=1` в свои ссылки атрибуции.

Чтобы просмотреть полный список параметров AppsFlyer, нажмите<Anchor target="_blank" href="/partners/ru/docs/postback-macros-for-ad-networks">здесь</Anchor>.

Чтобы просмотреть полный список макросов Everflow, нажмите<Anchor target="_blank" href="https://help.everflow.io/support/solutions/articles/22000176119-parameters-and-macros">здесь</Anchor>.

<div id="integrating-your-install-and-in-app-event-postbacks" />

## Интеграция постбэков по установкам и in-app событиям

<div id="note-1" />

> 📘 **Примечание:**
>
> * Ниже приведено объяснение того, как форматировать постбэки по установкам и событиям в приложении для платформы Everflow.
> * В приведенных ниже постбэках необходимо передать AppsFlyer ваш пользовательский домен Everflow вместо  [everflow\_domain\_placeholder].
> * NID — это идентификатор сети, предоставленный Everflow.

<div id="global-install-postback" />

## Глобальный постбэк по установке

```http
https://[everflow_domain_placeholder]/?nid=[everflow_network_placeholder]&transaction_id=$$click(clickid)
```

<div id="global-in-app-event-postback" />

## Глобальные постбэки от событий внутри приложения

```http
https://[everflow_domain_placeholder]/?event_id=[everflow_eventid_placeholder]&nid=[everflow_network_placeholder]&transaction_id=$$click(clickid)
```

**Event\_ID**

Уникальный идентификатор ID in-app события, который Everflow генерирует для каждого события оффера.

**Event\_ID= задается рекламодателем как Event Tag на дэшборде AppsFlyer для каждого приложения**

Это фактическое название события в приложении.

Подробную информацию о динамическом сопоставлении событий для событий в приложении см. <Anchor target="_blank" href="/partners/ru/docs/dynamic-event-mapping-for-in-app-events">здесь</Anchor>

<div id="event-setup-in-everflow" />

## Настройка событий в Everflow

**Чтобы настроить событие в Everflow, выполните следующие шаги**:

1. Чтобы настроить события на уровне оффера, воспользуйтесь инструкцией <Anchor target="_blank" href="https://help.everflow.io/support/solutions/articles/22000176131-add-post-conversion-events-">здесь</Anchor>.
2. После настройки событий запомните, какой идентификатор события к какому относится. В примере ниже идентификатор события ID 275 соответствует Purchase, а идентификатор события ID 276 — Registration
3. Добавьте эти события в ссылку атрибуции AppsFlyer.  
   Для каждого значения "&goalid\_x" должен быть один идентификатор ID события.  
   Замените "x" на другой номер goalid. В этом примере мы использовали &goalid\_1=275 и &goalid\_2=276
4. Добавьте их в ссылку атрибуции AppsFlyer на странице **General** после редактирования оффера. [![](https://files.readme.io/2c8e34fb91800fefac0da3c9285579833cdb17366234529001683ae008fba851-360002535645.png)](https://files.readme.io/2c8e34fb91800fefac0da3c9285579833cdb17366234529001683ae008fba851-360002535645.png)
5. Добавьте &goalid\_1=275&goalid\_2=276 в ссылку атрибуции AppsFlyer и нажмите «Сохранить».  
   После завершения это должно выглядеть так (идентификаторы ваших событий могут отличаться): [![](https://files.readme.io/9c62bc03423febe5e990bb230c5a5c3023dba723b7c8877ead5d3328a24ee3bb-360002539489.png)](https://files.readme.io/9c62bc03423febe5e990bb230c5a5c3023dba723b7c8877ead5d3328a24ee3bb-360002539489.png)
6. Попросите рекламодателя сопоставить эти события в AppsFlyer. Подробнее о динамическом сопоставлении событий для событий в приложении — см. выше.
7. Получите постбек события от Everflow и отправьте его в AppsFlyer, убедитесь, что вы сопоставляете правильные макросы goalid с соответствующими событиями на стороне рекламодателя.

<div data-zendesk-anchors="initiating-the-integration-with-appsflyer=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-%D1%81-appsflyer h_01KPJWT3XQ0WZRT7PD6GVRR6SH=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-%D1%81-appsflyer attribution-url-template=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 h_01KPJWT3XQZKMBEP7S20TNT82Q=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-url-%D0%B0%D0%B4%D1%80%D0%B5%D1%81%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 creating-your-attribution-link=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 h_01KPJWT3XQ4M7Z0G1EDD2BNGXP=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 h_01KPJWT3XQEX5TFPKBW14CZPQ3=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 integrating-your-install-and-inapp-event-postbacks=%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-in-app-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC h_01KPJWT3XQ86V1D429YC6FSP2Z=%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B0%D0%BC-%D0%B8-in-app-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F%D0%BC h_01KPJWT3XQ8E01ZJAZPXSFH55P=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5-1 global-install-postback=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 h_01KPJWT3XQW3TKNPR7Z6K2NCQZ=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA-%D0%BF%D0%BE-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B5 global-inapp-event-postback=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BE%D1%82-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01KPJWT3XQCM2BWTJVDXSVSBQP=%D0%B3%D0%BB%D0%BE%D0%B1%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%BE%D1%82-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F event-setup-in-everflow=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-everflow h_01KPJWT3XQ9K4WPVCSGGGC4Z6S=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-everflow" />
