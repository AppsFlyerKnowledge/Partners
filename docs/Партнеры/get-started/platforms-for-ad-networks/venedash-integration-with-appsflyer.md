---
title: интеграция venedash с AppsFlyer
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
  created_at: '2020-04-24T21:20:47Z'
  edited_at: '2026-09-12T00:38:21Z'
  id: 360007705617
  locale: ru
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ru/articles/360007705617
---
> **Краткий обзор:** Отправляйте данные атрибуции из AppsFlyer в venedash. AppsFlyer может отправлять в venedash данные об установках и событиях в приложении.

<div id="venedash-integration-setup" />

## настройка интеграции с venedash

* Если у вас уже есть интеграция с AppsFlyer, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.
* Если у вас нет интеграции с AppsFlyer, заполните заявку на регистрацию рекламного партнера <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">здесь</Anchor>.

**Чтобы включить интеграцию с AppsFlyer:**

1. В **AppsFlyer** перейдите в **Collaborate** > **Partner Integrations > Active Integrations** и выберите Venedash из списка партнеров.
2. На вкладке **Интеграция** включите **Активировать партнера**.
3. Перейдите на вкладку **Ссылка атрибуции** и сгенерируйте ссылку атрибуции со следующими обязательными параметрами:

   

| Параметр AppsFlyer | параметр venedash | Описание |
| --- | --- | --- |
| &clickid= | `{#ydrid#}` | Request ID каждой пользовательской сессии |
| &af\_siteid= | `{#ydr_pid#}` | Идентификатор ID партнера, который продвигает оффер |
| &advertising\_id | `{#android_adv#}` | Идентификатор устройства Android |
| &idfa= | `{#iosidfa#}` | Идентификатор устройства iOS |

   Обратите внимание: параметр pid заполняет команда AppsFlyer.  
   Название группы объявлений

   ```http
   https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#ydrid#&af_siteid=#ydr_pid#&advertising_id=advertising_id&idfa=#iosidfa#">https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#ydrid#&af_siteid=#ydr_pid#&advertising_id=advertising_id&idfa=#iosidfa#
   ```

   <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">Узнать больше</Anchor> о параметрах ссылки атрибуции.
4. В Venedash создайте оффер и вставьте ссылку атрибуции AppsFlyer в поле URL-адрес назначения.

   <Image align="center" alt="venedash-destination_url-en_us.png" src="https://files.readme.io/2a284eab8d25f57f1bfa2981e2d86bf16bce16b64b61858fdb819d5ac14eac20-360016242798.png" />

<div data-zendesk-anchors="venedash-integration-setup=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-%D1%81-venedash h_01HKW87R2DGCXHZSVSV9D9203Z=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-%D1%81-venedash" />
