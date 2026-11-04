---
title: Тест интеграции кампании маркетолога с рекламной сетью
metadata:
  keywords:
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
  created_at: '2021-12-08T04:41:04Z'
  edited_at: '2026-09-02T00:37:31Z'
  id: 4413093220113
  locale: ru
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ru/articles/4413093220113
---
> **Кратко**: протестируйте интеграцию с рекламной сетью с помощью приложений маркетолога.

<div id="prerequisites" />

## Требования

Прежде чем начать тестировать интеграцию маркетолога с вашей рекламной сетью, убедитесь, что выполнены следующие требования:

* Добавьте устройства в список разрешённых: попросите маркетолога <Anchor target="_blank" href="/marketers/ru/docs/registering-test-devices">добавить в список разрешённых</Anchor> все устройства, которые вы используете для тестирования
* Приложение должно включать SDK AppsFlyer
* Если приложение недоступно в Google Play или iOS App Store, попросите маркетолога предоставить вам приложение
* Независимо от того, опубликовано приложение или нет, оно должно <Anchor target="_blank" href="/marketers/ru/docs/adding-an-app-to-appsflyer">находиться в аккаунте AppsFlyer маркетолога</Anchor>

<div id="getting-started" />

## Начало работы

Откройте свой дэшборд AppsFlyer. На экране **Поиск приложения** введите идентификатор приложения маркетолога:

<div id="example" />

> 📄 **Например**
>
> Android — **com.example.app**
>
> iOS — **id1234123412**

Когда в поле ввода появится зелёная галочка, нажмите синюю стрелку. При клике по стрелке открывается дэшборд приложения.

[![partner-app-search.png](https://files.readme.io/9fb3454de2eb7ea1cc7015151d75a9ae0835a60134b244227bf4da7f614a2a37-21414453165457.png)](https://files.readme.io/9fb3454de2eb7ea1cc7015151d75a9ae0835a60134b244227bf4da7f614a2a37-21414453165457.png)

<div id="testing-live-apps" />

## Тестирование опубликованных приложений

В дэшборде AppsFlyer для вашего приложения в боковом меню выберите **Активные интеграции**. Выберите свою рекламную сеть и нажмите **Ссылка атрибуции**.

<div id="important" />

> 🚧 **Двоеточие (:)**
>
> Если параметры в разделе **Ссылка атрибуции** неактивны, попросите маркетолога <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#permissions-tab">включить разрешения для рекламной сети</Anchor>. Требуются следующие разрешения: **Разрешить настраивать интеграцию** и **Разрешить настраивать постбэки событий в приложении**.
>
> Либо попросите маркетолога предоставить вам ссылку атрибуции.

<div id="installing-the-app-through-the-attribution-link" />

<Accordion title="Установка приложения по ссылке атрибуции">

Теперь вы можете создать ссылку атрибуции, чтобы протестировать атрибуцию установок.

Добавьте в ссылку атрибуции параметры в соответствии с вашими требованиями и данными, которые вы хотите записывать.

[![partner-configure-attribution-link.png](https://files.readme.io/9402ab5b3d1750ffd3ae8a2867c751545bdfd5b79202e09c8c90b9bc0bbbef95-21414453180817.png)](https://files.readme.io/9402ab5b3d1750ffd3ae8a2867c751545bdfd5b79202e09c8c90b9bc0bbbef95-21414453180817.png)

<div id="tip" />

> 👍 **Совет.**
>
> Подробнее о параметрах, которые можно добавить в ссылку атрибуции, см. в статье <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">Структура и параметры ссылки атрибуции AppsFlyer</Anchor>.

</Accordion>

<div id="testing-install-attribution" />

<Accordion title="Тестирование атрибуции установок.">

Отправьте ссылку атрибуции на тестовое устройство. Откройте ссылку в браузере, установите приложение и запустите его.

Запуск приложения крайне важен для процесса атрибуции. Если приложение не запущено, атрибуция не фиксируется.

После этого вы можете [просмотреть установку на своем дэшборде](/docs/test-marketer-campaign-integration-with-the-ad-network#просмотр-установок-на-дэшборде).

</Accordion>

<div id="testing-apps-in-development" />

## Тестирование приложений в разработке

Вы можете протестировать интеграцию кампании маркетолога с вашей рекламной сетью, даже если приложение еще не опубликовано. Однако вам нужно попросить маркетолога предоставить вам приложение (файл .apk или .ipa), чтобы вы могли установить его на свои тестовые устройства.

<div id="generate-an-attribution-link" />

<Accordion title="Создание ссылки атрибуции">

Создайте ссылку атрибуции. Вы можете использовать [те же инструкции, что приведены выше](/docs/test-marketer-campaign-integration-with-the-ad-network#installing-the-app-through-the-attribution-link). Отправьте ссылку атрибуции на тестовое устройство и перейдите по ней в браузере устройства.

На экране появится такое окно:

[![app-not-available.png](https://files.readme.io/fda6290e4f0f995dbf04966c0a36b24fb246c4665ec367907178ed1d04edcf0c-21414453195921.png)](https://files.readme.io/fda6290e4f0f995dbf04966c0a36b24fb246c4665ec367907178ed1d04edcf0c-21414453195921.png)

Это ожидаемый результат. Поскольку приложение неактивно, ссылка атрибуции не ведет ни в один магазин приложений. Однако ссылка атрибуции по-прежнему действительна для целей атрибуции. Ссылка атрибуции и ее параметры записываются на серверах AppsFlyer, а эти данные используются для атрибуции.

</Accordion>

<div id="installing-the-app" />

<Accordion title="Установка приложения">

Установите приложение на тестовое устройство с помощью файла, который предоставит маркетолог, а затем запустите приложение. Удалите приложение и повторите процесс (чтобы сгенерировать несколько установок). После этого вы можете [просмотреть установки на своем дэшборде](/docs/test-marketer-campaign-integration-with-the-ad-network#просмотр-установок-на-дэшборде).

</Accordion>

<div id="testing-in-app-events" />

## Тестирование внутренних событий приложения.

<div id="note" />

> 📘 **Примечание**
>
> Вы можете тестировать постбэки событий в приложении как для опубликованных приложений, так и для приложений в разработке.

Прежде чем тестировать постбэки по событиям в приложении, свяжитесь с маркетологом, чтобы узнать, какие типы событий в приложении он регистрирует и как их можно вызвать из приложения.

<div id="mapping-events" />

<Accordion title="Сопоставление событий">

Если маркетолог включил разрешение <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">**Configure in-app event postbacks**</Anchor> в настройках интеграции для вашей рекламной сети, вы можете сопоставить события AppsFlyer с событиями, которые вы регистрируете на своих серверах.

В дэшборде AppsFlyer для вашего приложения в боковом меню выберите **Активные интеграции** и выберите нужную рекламную сеть. На вкладке **Integration** прокрутите вниз до раздела **In-app event settings**. Выберите событие в приложении и сопоставьте его с соответствующим событием:

[![partner-in-app-events-postbacks-mapping.png](https://files.readme.io/2fe64793de5946d457a8fcb567db761c539755bdbe4cf910953b178eca84d841-21414453211793.png)](https://files.readme.io/2fe64793de5946d457a8fcb567db761c539755bdbe4cf910953b178eca84d841-21414453211793.png)

</Accordion>

<div id="triggering-inapp-events" />

<Accordion title="Запуск событий в приложении">

Когда вы определите, какие события в приложении регистрирует маркетолог, и настроите сопоставление событий, запустите несколько событий в установленном приложении.

<div id="note-1" />

> 📘 **Примечание**
>
> Рекламные сети не имеют доступа к дэшборду событий и могут видеть события в приложении на обзорном дэшборде только после того, как рекламодатель включит **Доступ к агрегированным данным по событиям в приложении** <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#permissions-tab">разрешение для рекламной сети</Anchor>. Однако вы можете экспортировать данные, связанные с событиями в приложении, из [отчета «Постбэки по событиям в приложении»](/docs/test-marketer-campaign-integration-with-the-ad-network#проверка-данных-постбэка).

В отчете по постбэкам событий в приложении можно найти такие данные, как URL-адрес постбэка и сопоставленные параметры. Используйте данные из отчёта и сравните их с данными на ваших серверах (полученными через постбек), чтобы убедиться, что данные из постбеков точны и правильно записаны вашими серверами.

После экспорта отчета «Постбэки по событиям в приложении» вы можете проверить в нем следующее:

1. Событие атрибутировано вам как рекламной сети в поле **медиаисточник**
2. Название события указано правильно в поле **Event name**
3. Постбэк, если он включен, содержит название и значение события в поле **URL-адрес постбэка**
4. События в приложении корректно сопоставлены в поле **URL-адрес постбэка**

</Accordion>

<div id="viewing-installs-in-the-dashboard" />

## Просмотр установок на дэшборде

После установки и запуска приложения результаты можно увидеть на вашем дэшборде.

<div id="important-1" />

> 🚧 **Двоеточие (:)**
>
> Чтобы сгенерировать несколько установок, [устройство должно быть в списке разрешенных](/docs/test-marketer-campaign-integration-with-the-ad-network#требования).

Откройте дэшборд AppsFlyer и в боковом меню выберите **Анализ** > **Обзор**.

Отфильтруйте по своей рекламной сети. Вы можете увидеть количество кликов и установок, атрибутированных вашей рекламной сети.

Данные, связанные с кликами и установками, отображаются в верхней части экрана **Overview**. Экран **Overview** также включает разделы **Breakdown by campaign** и **Aggregated performance report**. Проверьте, что кампании, отображающиеся в этих разделах, соответствуют параметру кампании в ссылке атрибуции.

<div id="verifying-postback-data" />

## Проверка данных постбэка

Каждая установка, атрибутированная вашей рекламной сети, генерирует постбэк установки. Если постбэки событий в приложении включены, события из приложения, установка которого атрибутирована вашей рекламной сети, также генерируют постбэки.

Откройте <Anchor target="_blank" href="/marketers/ru/docs/raw-data-export-page">страницу экспорта сырых данных</Anchor> и создайте 2 отчета по постбэкам:

1. **Установок**
2. **События в приложении**

Оба отчета содержат столбец **Postback URL**. В этом столбце перечислены URL-адреса постбэков для установок или событий в приложении (в зависимости от типа отчета).

Проверьте данные в этом столбце и убедитесь в следующем:

* URL-адрес конечной точки указан верно
* Параметры, добавленные к URL-адресу, соответствуют параметрам, добавленным к ссылке атрибуции AppsFlyer
* Для постбэков in-app событий события сопоставлены правильно, например:  
  Для постбэков in-app событий события сопоставлены правильно, например:  
  `sdk_event=af_purchase&mapped-event=purchase`  
  `sdk_event=af_login&mapped-event=login`
* Столбец **Postback Error Message** пуст

<div data-zendesk-anchors="prerequisites=%D1%82%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F h_01HKA1DE8VKXM92D7S5BANFZJ4=%D1%82%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F getting-started=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B h_01HKA1DE8V9A9AJWYQR9VJQ0H8=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B h_01HKA1DE8VA7HAM8BT3KZ8HYGP=%D0%BD%D0%B0%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80 testing-live-apps=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BE%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 h_01HKA1DE8V0J2Y8DQ60J9S5DAK=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BE%D0%BF%D1%83%D0%B1%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 h_01HKA1DE8VDQGKYSYFDF5K2HSX=%D0%B4%D0%B2%D0%BE%D0%B5%D1%82%D0%BE%D1%87%D0%B8%D0%B5- h_01HKA1DE8VEEH8YE1QT28QVFZQ=installing-the-app-through-the-attribution-link h_01HKA1DE8VV0K8J2AG7W0FDDWY=%D1%81%D0%BE%D0%B2%D0%B5%D1%82 h_01HKA1DE8VEH7S0JAJTJ91KE7X=testing-install-attribution testing-apps-in-development=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B5 h_01HKA1DE8VK9RQGQ8BCG157H1Y=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-%D1%80%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B5 h_01HKA1DE8VSPE0FFM65AFQRJ8S=generate-an-attribution-link h_01HKA1DE8V68Z5CM4EF7YBPHPS=installing-the-app testing-inapp-events=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01HKA1DE8VVJXK11BM77D3YWA5=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01HKA1DE8W2VT648E022BHJP0K=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 h_01HKA1DE8WQVGPSTG2SQCM2BQW=mapping-events h_01HKA1DE8WRZPCX3GGV01ZK10K=triggering-inapp-events h_01HKA1DE8W8XXM4BK7843TAEJQ=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5-1 viewing-installs-in-the-dashboard=%D0%BF%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%BD%D0%B0-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B5 h_01HKA1DE8WY7VCST4XDN1HWGC7=%D0%BF%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%BD%D0%B0-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B5 h_01HKA1DE8WYRTTNC2Q0VGKMM82=%D0%B4%D0%B2%D0%BE%D0%B5%D1%82%D0%BE%D1%87%D0%B8%D0%B5--1 verifying-postback-data=%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0 h_01HKA1DE8WEQY58XAPS9MBNGKE=%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0" />
