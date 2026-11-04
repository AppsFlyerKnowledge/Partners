---
title: Тестирование интеграции Android для рекламных сетей
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
  created_at: '2021-12-06T10:35:58Z'
  edited_at: '2026-09-02T00:37:25Z'
  id: 4412945443857
  locale: ru
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ru/articles/4412945443857
---
> **Кратко:** Проверьте интеграцию AppsFlyer для Android с помощью приложения AppsFlyer Partner Integrations, чтобы запускать постбэки.

<div id="android-integration-testing" />

## Тестирование интеграции Android

Тестирование включает следующие элементы:

* Используйте версию приложения AppsFlyer Partner Integrations для Android, чтобы генерировать тестовые установки и события purchase в приложении. Эти тесты, в свою очередь, запускают постбэки, отправляемые в ваши конечные точки. Вы также можете тестировать события login и registration в приложении.
* После получения постбэков убедитесь, что вы можете их принимать.

**Область тестирования**

В следующей таблице перечислены тестовые сценарии в соответствии с доступными комбинациями настроек.

Для каждого сценария можно тестировать установки и события в приложении. Для событий в приложении можно использовать <Anchor target="_blank" href="/partners/ru/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">сопоставление событий в приложении</Anchor>, чтобы сопоставить события рекламодателя с вашими событиями.

<div id="testing" />

## Тестирование

Выполните предварительные требования, а затем выполните тестовые процедуры в следующих разделах. Каждый раздел тестирования содержит таблицу, которую можно использовать для записи результатов тестирования.

<div id="prerequisites" />

<Accordion title="Требования">

Перед выполнением тестовой процедуры выполните предварительные требования.

| Требования |
| --- |
| <Anchor target="_blank" href="/partners/ru/docs/turn-on-test-app-integration-for-ad-networks">Интегрируйте тестовое приложение Android в свою учетную запись.</Anchor> |
| Убедитесь, что тестовое приложение интегрировано в вашу учетную запись |
| <Anchor target="_blank" href="/partners/ru/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">Сопоставьте события в приложении с названиями ваших событий</Anchor>. Названия событий для сопоставления: `purchase`, `login`, `registration` |
| <Anchor target="_blank" href="/partners/ru/docs/ios-integration-testing-for-ad-networks#attribution-link">Подготовьте ссылку атрибуции</Anchor> |
| Протестируйте атрибуцию установки на устройстве под управлением Android |
| Протестируйте атрибуцию события в приложении на устройстве Android |
| Протестируйте атрибуцию ретаргетинга на устройстве Android |

</Accordion>

<div id="test-install-attribution" />

<Accordion title="Тестирование атрибуции установок">

**Чтобы запускать постбэки:**

1. Отправьте ранее подготовленную ссылку атрибуции на тестовое устройство.
2. Нажмите на ссылку, выполните установку, а затем откройте приложение.  
   Отображается страница **Install Data**.
3. Проверьте атрибуцию по следующим параметрам. Если проверка не пройдена, см. раздел <Anchor target="_blank" href="/partners/ru/docs/ios-integration-testing-for-ad-networks#troubleshooting">Устранение неполадок</Anchor>.

   1. `install_time`: близко к текущему времени. Время указывается по UTC.
   2. `af_status: Non-organic` Если это не так, установка не была атрибутирована.
   3. `media_source`: ваша рекламная сеть
4. Нажмите **In-App Event Tests.**
5. Нажмите **Purchase Event.**  
   Отображается подтверждение события Purchase Event.
6. Проверьте, что:
   1. Вы получили постбэки об установке и покупке.
   2. Название события сопоставлено правильно (если вы настроили сопоставление событий в приложении).
   3. Вы можете принять постбэк.

</Accordion>

<div id="supplementary-information-and-procedures" />

## Дополнительная информация и процедуры

<div id="about-the-partner-integrations-test-app" />

<Accordion title="О тестовом приложении Partner Integrations">

Приложение Partner Integrations доступно в Google Play. Приложение отправляет данные об установке и события в приложении на платформу AppsFlyer.

При первом открытии приложения страница **Install Data** отображает данные конверсии, зарегистрированные на платформе AppsFlyer. Тестовые события в приложении запускаются в пользовательском интерфейсе.

Доступны следующие опции:

* **In-App Event Tests**Отправка событий в приложении `purchase`, `login` и `registration`. При сопоставлении названий событий в приложении с вашими названиями событий постбэки заполняются с использованием ваших названий событий.

</Accordion>

<div id="attribution-link" />

<Accordion title="Ссылка атрибуции">

Подготовьте ссылку атрибуции в дэшборде AppsFlyer, используя один из следующих способов:

* Сгенерируйте ссылку в дэшборде AppsFlyer.
* Измените пример ссылки ниже.

**Чтобы сгенерировать ссылку в дэшборде:**

1. В AppsFlyer в верхнем меню выберите вкладку **Мои приложения**.
2. Выберите **adNetworkTest**.
3. В AppsFlyer в боковом меню выберите **Сотрудничество** > **Активные интеграции** > выберите свою рекламную сеть > вкладку **Ссылка атрибуции**.
4. На вкладке Attribution link задайте перечисленные параметры. При необходимости можно добавить дополнительные параметры. Ссылка на ссылку атрибуции 

| Параметр | Пример значения | Замечание |
| --- | --- | --- |
| <span id="campaign"></span>кампания; | c-test-2020-12-20 | Задайте значение, которое можно идентифицировать в ваших постбэках |
| <span id="pid"></span>pid | pitestap |  |

5. Скопируйте полученную ссылку для дальнейшего использования.

**Пример ссылки атрибуции:**

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="Тестовое приложение, интегрированное в вашу учетную запись">

**Чтобы убедиться, что тестовое приложение доступно в вашей учетной записи:**

1. В AppsFlyer в верхнем меню перейдите в раздел **Мои приложения**.
2. Убедитесь, что приложение **Интеграция партнеров adNewtorkTest** отображается в разделе Доступные приложения. Если это не так, обратитесь к своему Partner Development Manager.

</Accordion>

<div id="troubleshooting" />

<Accordion title="Устранение неполадок">

| Симптом | Причина/корректирующее действие |
| --- | --- |
| Время установки не совпадает с текущим временем | Приложение не было удалено перед установкой.<br /><br />Удалите приложение и повторите процедуру. |
| Медиаисточник не совпадает с вашим медиаисточником | Убедитесь, что в ссылке атрибуции задано правильное значение **pid**. Убедитесь, что вы используете правильную ссылку атрибуции |
| af\_status — органический | Проверьте формат ссылки атрибуции, особенно значение **pid**. |

</Accordion>

<div id="test-retargeting-attribution" />

<Accordion title="Тест атрибуции ретаргетинга">

Вы также можете протестировать атрибуцию ретаргетинга. Процесс почти такой же, за исключением одного параметра, который нужно добавить в ссылку атрибуции.

Создайте новую ссылку атрибуции и добавьте в нее параметр `is_retargeting=true`.

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_click_lookback=7d
          &clickid={clickid}&is_retargeting=true
```

Установите приложение, используя ссылку ретаргетинга. Процесс такой же, как описано в разделе [тестирование атрибуции установки](/docs/android-integration-testing-for-ad-networks#test-install-attribution).

<div id="viewing-retargeted-installs-in-the-dashboard" />

### Просмотр установок после ретаргетинга в дэшборде

Откройте дэшборд AppsFlyer и кликните **Re-targeting** в меню слева. Данные об установке, выполненной в результате ретаргетинга, появятся на дэшборде в течение 30 минут.

[![com_appsflyer_adNetworkTest-retargeting.png](https://files.readme.io/e46789b004be2f4fc15f095ba11a0f3f5d03abb1240e54e4b534285e3e4efd8d-21266228899601.png)](https://files.readme.io/e46789b004be2f4fc15f095ba11a0f3f5d03abb1240e54e4b534285e3e4efd8d-21266228899601.png)

</Accordion>

<div id="test-viewthrough-attribution" />

<Accordion title="Тест атрибуции по просмотрам">

1. В AppsFlyer перейдите в **My Apps**.
2. Выберите **adNetworkTest**.
3. В AppsFlyer в боковом меню выберите **Collaborate** > **Active Integrations** > выберите свою рекламную сеть > вкладку **Integration**.
4. Убедитесь, что параметр **Enable view-through attribution** включен.
5. Скопируйте ссылку атрибуции показов.

   ```http
   https://impression.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_viewthrough_lookback=24h&advertising_id=YOUR_GAID&af_siteid=YOUR_SITEID
   ```

   Замените параметры следующим образом:

   * YOUR\_PID — ваш идентификатор ID партнера, предоставленный AppsFlyer (заканчивается на *\_int*)
   * YOUR\_CAMPAIGN — любое название кампании
   * YOUR\_GAID — ваш Рекламный идентификатор Google
   * YOUR\_SITEID — любой идентификатор ID сайта

   Примечание: параметры в ссылке — это базовые параметры, используемые здесь для тестирования. Вы можете добавить в ссылку атрибуции по просмотрам другие параметры в соответствии с вашими требованиями.
6. Отправьте ссылку атрибуции по просмотрам на тестовое устройство.
7. Откройте ссылку в браузере и установите приложение из магазина.
8. Запустите приложение.  
   Откроется следующая страница:

   ![vta-testing-postback.png](https://files.readme.io/88b6720928d7540eeb2fe8f42f39ecdccc04655aa49f95d08dba5741d5e39982-4831106525457.png)

   Если вы не видите это сообщение, убедитесь, что ссылка атрибуции по просмотрам сформирована правильно. Удалите приложение и установите его заново, используя ссылку атрибуции по просмотрам на новом тестовом устройстве.

Совет.

Чтобы получить более детальные результаты, повторите процесс установки, используя ссылку атрибуции по просмотрам на новом тестовом устройстве. Удалите приложение, измените параметры в ссылке (название кампании, af\_siteid и advertising\_id), а затем снова установите его, нажав URL-адрес.

<div id="view-installs-in-the-dashboard" />

### Просмотр установок в дэшборде

После установки и запуска приложения результаты можно увидеть на дэшборде AppsFlyer.

Подождите до 30 минут, пока установка не отобразится в дэшборде приложения.

</Accordion>

<div id="raw-data-export" />

<Accordion title="Экспорт сырых данных">

Данные, связанные с приложениями, установка которых атрибутирована вашей рекламной сети, можно экспортировать в формате CSV.

Данные включают следующее:

* Установок
* События в приложении
* Установки из ретаргетинга
* События в приложении для приложений, установленных из ретаргетинговых кампаний

**Чтобы экспортировать сырые данные**:

1. В AppsFlyer перейдите в раздел **Report** > **Raw data export**.
2. Выберите диапазон дат.
3. Выберите отчет.  
   Отчет будет загружен в течение нескольких минут.

</Accordion>

<div id="verify-postback-data" />

<Accordion title="Проверьте данные постбэка">

Каждая установка генерирует постбэк, который отправляется на ваши серверы. Чтобы проверить URL-адрес постбэка, его структуру и параметры, которые к нему добавляются, экспортируйте отчет **Installation postbacks**.

Отчет **Installation postbacks** содержит столбец **Postback URL**. В этом столбце перечислены URL-адреса постбэков, сгенерированные для каждой установки.

Проверьте данные в этом столбце и убедитесь в следующем:

* URL-адрес эндпоинта указан верно
* Параметры, добавленные к URL-адресу, соответствуют параметрам, добавленным к атрибуционной ссылке AppsFlyer
* Столбец **Postback Error Message** пуст

</Accordion>

<div data-zendesk-anchors="android-integration-testing=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-android h_01HJR6V0MYJXD4QSRT95SVXTWH=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-android testing=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5 h_01HJR6V0MYBPC3CSAJTTQSWGAR=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5 h_01HJR6V0MYG42PPWXT7H2AGTAE=prerequisites h_01HJR6V0MYDRZGQQ74TJWDJ2WS=test-install-attribution supplementary-information-and-procedures=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%B8-%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D1%8B h_01HJR6V0MYZ5NG21FEKB4HY6HT=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%B8-%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D1%8B h_01HJR6V0MYTZCS097RQP9HG7GY=about-the-partner-integrations-test-app h_01HJR6V0MYVCNVHNCPZ29KRA4K=attribution-link h_01HJR6V0MY6JZXP2NX9YJ9ZY2T=test-app-integrated-in-your-account h_01HJR6V0MYWK7WAAFHRYPCVM7N=troubleshooting h_01HJR6V0MY2SSP17ZEWRM3NXKE=test-retargeting-attribution viewing-retargeted-installs-in-the-dashboard=%D0%BF%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D1%80%D0%B5%D1%82%D0%B0%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D0%B0-%D0%B2-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B5 h_01HJR6V0MYPC0AZF05YF32Z571=%D0%BF%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%BF%D0%BE%D1%81%D0%BB%D0%B5-%D1%80%D0%B5%D1%82%D0%B0%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D0%B0-%D0%B2-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B5 h_01HJR6V0MY027J9PKXZZ4TCXRX=test-viewthrough-attribution view-installs-in-the-dashboard=%D0%BF%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%B2-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B5 h_01HJR6V0MZ4VA3V8CA3PN5Z31K=%D0%BF%D1%80%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA-%D0%B2-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B5 h_01HJR6V0MZCZ3E8NCR6DG6P6P1=raw-data-export h_01HJR6V0MZAHSXCTEZKTVWM96V=verify-postback-data" />
