---
title: Углубленное руководство по типам вовлеченности для рекламных сетей
metadata:
  keywords:
    - Advertisers
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2024-10-15T10:54:29Z'
  edited_at: '2026-08-19T00:37:45Z'
  id: 29221265052433
  locale: ru
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ru/articles/29221265052433
---
> **Краткий обзор:** Узнайте, как создавать ссылки атрибуции обогащенных типов вовлеченности (EET), чтобы отразить полный спектр вовлеченности пользователей и достичь точной и эффективной оптимизации кампаний.

Обогащенные типы вовлечения отражают весь спектр вовлечения и намерений пользователей при просмотре или взаимодействии с рекламой, от моментального воздействия до прямой реакции. В этой статье подробно описывается, как партнёры должны сообщать о типах взаимодействия в атрибуционных ссылках AppsFlyer в зависимости от того, как пользователи взаимодействуют с их рекламой.

<div id="disclaimer" />

> ❗️ **Дисклеймер**
>
> Эта статья сосредоточена на аспектах EET, имеющих отношение к партнерам. Чтобы узнать, что такое EET, и получить полную информацию о нем, смотрите статью <Anchor target="_blank" href="/marketers/ru/docs/about-enriched-engagement-types#which-ad-networks-report-enriched-engagement-types">о Расширенных типах вовлеченности.</Anchor>

<div id="which-networks-can-report-eet-to-appsflyer" />

## Какие сети могут сообщать EET в AppsFlyer?

Поддержка новых типов вовлечения будет доступна сетям, которые соответствуют критериям Premier, Advance или Engage партнерской программы AppsFlyer. Эти уровни относятся к сетям, которые имеют значительный опыт предоставления большого количества трафика неизменно высокого качества для наших общих клиентов, передают данные о взаимодействии прозрачным и надежным способом и интегрированы с полным спектром услуг AppsFlyer.

<div id="note" />

> 📘 **Примечание:**
>
> Чтобы начать отчет о вовлеченных просмотрах и кликах, рекламные сети должны связаться со службой поддержки AppsFlyer.

Смотрите список сетей, имеющих право сообщать о ЕЭТ

<div id="warning" />

> ❗️ **Предупреждение**
>
> Клики и показы из неразрешенных сетей, включающие параметр af\_engagement\_type, будут отклонены и не будут использоваться для атрибуции.

<div id="engaged-click-or-engaged-view-attribution-flow" />

<Accordion title="Атрибуция вовлеченного клика или вовлеченного просмотра">

Следующие шаги описывают процесс от первоначального отображения рекламы до окончательной атрибуции события установки, через либо вовлеченный клик, либо вовлеченный просмотр:

1. Рекламная сеть отображает рекламу.
2. Рекламная сеть отправляет показ в AppsFlyer с указанным`af_ad_tran_id`
3. Пользователь взаимодействует с рекламой.
4. Рекламная сеть отправляет клик или показ с параметрами `af_engagement_type``af_ad_tran_id``af_ad_format``af_ad_type`и, при необходимости, с параметрами`viewability` .
5. AppsFlyer сопоставляет событие установки с вовлеченным кликом или вовлеченным просмотром.
6. AppsFlyer приписывает событие установки рекламной сети.

</Accordion>

<div id="parameters-for-reporting-engagement-types-in-attribution-links" />

<Accordion title="Параметры для отчетности о типах вовлеченности в атрибуционных ссылках">

Сети могут сообщать о типах вовлеченности, включая следующие параметры в ссылки атрибуции

* `af_engagement_type`: Тип взаимодействия, например, `engaged_click``click_to_app`или`engaged_view`. Посмотрите полный список различных типов взаимодействия и их описаний.
* `af_ad_type`: Тип объявления. Например, `af_ad_type` af\_ad\_type`rewarded_video``interstitial``banner`, banner, или . Посмотрите полный список различных типов объявлений и их описаний.
* `af_ad_format`: Формат рекламы, например, `text``image``video``playable` Посмотрите <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#af_ad_format">полный список различных форматов объявлений и их описаний.</Anchor> См. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#af_ad_format">полный список различных форматов рекламы и их описаний.</Anchor>
* `viewability`(необязательно) Дополнительная информация о взаимодействии, например,`af_video_total_length``af_ad_time_viewed``af_audio_played_length` Посмотрите <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#параметры-видимости">полный список различных вариантов видимости и их описаний.</Anchor> Посмотрите <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#параметры-видимости">полный список различных вариантов видимости и их описаний.</Anchor>
* `af_ad_tran_id`: Идентификатор транзакции, позволяющий AppsFlyer проверить вовлеченный клик или вовлеченный просмотр, сопоставив его с предшествующим показом.
* `is_skoverlay=true`ИЛИ `is_skoverlay=true` Определите вовлеченные просмотры, вызванные [SKOverlay](https://developer.apple.com/documentation/storekit/skoverlay) или установками Android Auto Inline.

**Пример для вовлеченного клика**

```http HTTPS
https://app.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_click&af_ad_type=interstitial&af_ad_format=playable&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0
```

**Пример для вовлеченного просмотра**

```http
https://impression.appsflyer.com/com.greatapp?pid=greatnetwork_int&c=GreatCampaign&af_siteid=A1b1&af_engagement_type=engagegd_view&af_ad_type=interstitial&af_ad_format=video&af_ad_tran_id=50b175dd-d804-4715-b415-0206f6c891e0&af_video_total_length=20&af_video_played_length=15
```

</Accordion>

<div id="user-engagements-to-report-as-engaged-clicks" />

<Accordion title="Вовлеченность пользователей для отчета о вовлеченных кликах">

*Engagedngaged click* - это клик, который удерживает пользователя в том же контексте, взаимодействуя с рекламой, не перенаправляя его в магазин приложений и не запуская приложение.

Ниже приведены примеры взаимодействия пользователей, которые рекламные сети должны сообщать со значением параметра `af_engagement_type=engaged_click`:

* **Реклама-микроверсия** Нажатие для взаимодействия с играбельной рекламой, например, нажатие для игры в мини-игру или интерактивный контент внутри рекламы.
* Социальное взаимодействие Клик, чтобы поставить лайк, прокомментировать или поделиться рекламой в социальных сетях, что способствует дальнейшему взаимодействию и потенциальной виральности.
* **Перенаправление** Нажатие для перехода на целевую страницу или другой внешний сайт/страницу.
* **Динамическое рекламное объявление/каталог или карусель** Нажмите, чтобы провести между продуктами.
* **ДОБАВИТЬ\_В\_СПИСОК\_ЖЕЛАНИЙ** Клик, чтобы добавить рекламируемый продукт в вишлист или список избранного в приложении или на внешнем веб-сайте. Сохранить на потом:
* **Сохранить на потом:** Нажимая для сохранения объявления и его содержимого для будущего использования, тем самым указывая на интерес к повторному просмотру объявления или его дальнейшему изучению.
* Добавить в закладки или в коллекции Нажатие кнопки добавления объявления в закладки или в коллекции в приложении указывает на намерение повторно просмотреть или классифицировать объявление.
* **Включить звук рекламы** Нажмите, чтобы включить звук.

**Когда не следует сообщать о вовлеченных кликах в AppsFlyer?**

Ниже приведены примеры взаимодействия пользователей, которые рекламные сети **не должны сообщать** с параметром.

* **Отказ от рекламы:** Клик по значку «x» или аналогичному значку, чтобы закрыть или отклонить объявление. Свидетельствует о незаинтересованности в дальнейшем взаимодействии.
* **Пропустить рекламу** Клик по указанной кнопке позволяет пропустить рекламу и перейти непосредственно к нужному контенту. Указывает на то, что реклама не интересна и не актуальна для пользователя.
* Пожаловаться на объявление: Клик с целью сообщить, что объявление является оскорбительным, вводящим в заблуждение или неуместным. Свидетельствует о недовольстве содержанием объявления.
* **Отказаться или Отписаться**: Клик, чтобы отписаться и отказаться от получения подобной рекламы в будущем. Говорит о желании прекратить взаимодействие с рекламой или ее категорией.
* **Выйти из рекламы** Нажатие на ссылку или кнопку, которая выходит из текущего рекламного опыта, уводя пользователя за пределы рекламируемого контекста или целевой страницы.
* **Выключить рекламу:** отключение звука в видео.

</Accordion>

<div id="user-engagements-to-report-as-engaged-views" />

<Accordion title="Вовлеченность пользователей для отчета как вовлеченные просмотры">

Сети должны сообщать о взаимодействиях пользователей `af_engagement_type=engaged_view`в следующих случаях:

* Пропускаемая рекламная единица: Пользователи смотрят как минимум 5 секунд после появления опции пропуска в видеорекламе. Если сеть не может измерить количество просмотренных секунд, то:
  * Отправьте `engaged_view` при просмотре на 2/4 (50% просмотренных пикселей), если видео длится более 20 секунд.
  * Отправить `engaged_view`по завершении (100% видео завершено), если видео короче 20 секунд.
  * Значение `af_ad_format` параметра должно быть `video` или `playable`
* **вознагражденное\_видео**: Пользователь смотрит вознагражденное видео полностью. Значение`af_ad_type` параметра должно быть `rewarded_video`
* **Реклама, созданная с помощью StoreKit** Клики по рекламе[`SKOverlay`, отображаемой в StoreKit (или в ),](https://developer.apple.com/documentation/storekit/skoverlay) не фиксируются издателями, [а записываются Apple для атрибуции SKAdNetwork (SKAN). То же самое верно и для встроенных установок Android Auto (автохранилище).](https://developer.apple.com/documentation/storekit/skstoreproductviewcontroller)

  Поскольку у рекламных сетей нет возможности узнать, были ли эти объявления вовлечены, они сообщают о показе или клике каждый раз, когда объявления появляются, даже если вовлечения не произошло.

  `click_to_app`Сети могут сообщать о типе вовлеченности каждый раз, когда реклама появляется, но при этом рискуют получить очень высокий коэффициент кликов. То же самое верно и для Android с автоматическими установками.

  Чтобы смягчить этот риск, мы рекомендуем вместо этого сообщить `engaged_view`о типе вовлеченности. В этом кейсе ссылка атрибуции должна включать `is_skoverlay=true` для iOS или `is_autostore=true` для Android.

**Когда не следует сообщать о вовлеченных просмотрах в AppsFlyer?**

Ниже приведен пример вовлеченности пользователей, который рекламные сети не должны **сообщать со** значением параметра, а скорее с`engaged_view` параметром.

* Пользователь смотрит рекламу, которую нельзя пропустить, и это не вознаграждающее видео, и она не была наложена на `SKOverlay` или `autostore` рекламу.

</Accordion>

<div id="01JCAT81K2EJNH91YS6NJGMXMB-data-title" />

<Accordion title="Сети, имеющие право на отчетность по EET">

Список разрешенных сетей включает партнеров, чьи события типа вовлеченности могут обрабатываться AppsFlyer, за исключением вовлеченных кликов и просмотров. Сети из этого списка, которые хотят, чтобы AppsFlyer обрабатывал их вовлеченные клики и просмотры, должны обратиться в службу поддержки AppsFlyer. Чтобы узнать, какие сети уже обработали свои вовлеченные клики и просмотры через AppsFlyer, смотрите статью <Anchor target="_blank" href="/marketers/ru/docs/about-enriched-engagement-types#какие-сети-могут-отчитываться-о-вовлеченных-просмотрах-и-вовлеченных-кликах">для рекламодателей EET.</Anchor>

<div id="warning-1" />

> ❗️ **Предупреждение**
>
> Клики и показы из неразрешенных сетей, включающие параметр af\_engagement\_type, будут отклонены и не будут использоваться для атрибуции.

| Имя партнера |
| --- |
| AdColony |
| Adaction |
| Adaction3 |
| Adikteev |
| adjoe GmbH |
| Amazon |
| Amazon DSP |
| AppLovin |
| Appier |
| Appnext |
| Apple Search Ads |
| Aura от Unity |
| AWIN |
| Bidease |
| ByteDance Ads Китай |
| Cauly |
| Criteo |
| Digital Turbine |
| Digital Turbine On Device |
| Fluent |
| Glance |
| Google Ads (Adwords) |
| Google Marketing Platform (DV360/CM360) |
| Hotstar |
| Huawei |
| InMobi DSP |
| IronSource |
| Jampp |
| Josh |
| Kakao |
| Kuaishou |
| Liftoff |
| Линейная |
| Meta Ads |
| Mintegral |
| Mistplay |
| Motorola Pre-Install |
| Naver |
| Oppo |
| OPPO Global |
| OPPO Store Traffic (Global) |
| OPPOPAI Pre-Install |
| PayTM |
| Rakuten |
| Reddit |
| Remerge |
| RevX |
| Samsung |
| Smadex |
| Snapchat |
| Stackadapt |
| Tapjoy |
| Tencent AMS |
| TikTok for Business — расширенная SRN |
| TikTok for Business (устарело) |
| The Trade Desk |
| Transsion |
| Treasure Data |
| Truecaller |
| Unity Ads |
| Vivo Preload |
| vivo Global |
| Vungle |
| X Ads (ранее Twitter Ads) |
| Xiaomi Global |
| XiaomiPAI Pre-Install |
| Yahoo Япония |
| Яндекс |
| YouAppi |

</Accordion>

<div data-zendesk-anchors="01JA7WZH43ECDKRC0R0J89ED1E=%D0%B4%D0%B8%D1%81%D0%BA%D0%BB%D0%B5%D0%B9%D0%BC%D0%B5%D1%80 which-networks-can-report-eet-to-appsflyer=%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5-%D1%81%D0%B5%D1%82%D0%B8-%D0%BC%D0%BE%D0%B3%D1%83%D1%82-%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B0%D1%82%D1%8C-eet-%D0%B2-appsflyer h_01JJPVYGWZSFSATZ4TH5VBSVXW=%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5-%D1%81%D0%B5%D1%82%D0%B8-%D0%BC%D0%BE%D0%B3%D1%83%D1%82-%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B0%D1%82%D1%8C-eet-%D0%B2-appsflyer 01JAN5JRM56C6S6EP27WFJ2Y4W=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 h_01J00XFV133YYAB7YPQNXM5R37=%D0%BF%D1%80%D0%B5%D0%B4%D1%83%D0%BF%D1%80%D0%B5%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5 01JA7WZH46RJBG996NG9EZV7T9=engaged-click-or-engaged-view-attribution-flow 01JA7WZH4BZVGS9Z1NNHQC72N6=parameters-for-reporting-engagement-types-in-attribution-links 01JA7WZH4JDJFCVT25WJ4GNE20=user-engagements-to-report-as-engaged-clicks 01JA7WZH4Q32TEWM5EKME142R7=user-engagements-to-report-as-engaged-views 01JCAT81K2EJNH91YS6NJGMXMB%20data-title%3D=01JCAT81K2EJNH91YS6NJGMXMB-data-title allowed-network-list=01JCAT81K2EJNH91YS6NJGMXMB-data-title h_01JJPVYGWZ4T6TPFRWTR2AB027=%D0%BF%D1%80%D0%B5%D0%B4%D1%83%D0%BF%D1%80%D0%B5%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-1" />
