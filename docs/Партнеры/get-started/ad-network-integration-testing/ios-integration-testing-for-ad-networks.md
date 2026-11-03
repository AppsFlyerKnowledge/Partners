---
title: 'iOS: тестирование интеграции для рекламных сетей'
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
  created_at: '2020-12-16T11:39:36Z'
  edited_at: '2026-09-02T00:37:28Z'
  id: 360016588278
  locale: ru
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ru/articles/360016588278
---
> **Кратко:** Протестируйте интеграцию AppsFlyer для iOS с помощью приложения AppsFlyer Partner Integrations, чтобы инициировать обычные постбэки и постбэки Advanced Privacy.

## iOS: тестирование интеграции

Тестирование состоит из следующих элементов:

* Используйте версию приложения Интеграция партнеров от AppsFlyer для iOS, чтобы генерировать тестовые установки и события покупки в приложении. Эти тесты, в свою очередь, запускают постбэки, отправляемые на ваши конечные точки. Вы также можете тестировать события входа и регистрации в приложении.
* После получения постбэков убедитесь, что ваша система может их принять и обработать.

### Область тестирования

Рекламодатели управляют данными, передаваемыми рекламным сетям с помощью настройки Advanced Privacy. Эта настройка вместе с настройкой <Anchor target="_blank" href="/marketers/ru/docs/att-implications-ios-14-and-deprecation-of-lat">ATT</Anchor> пользователя приложения влияет на тип постбэка и данные, передаваемые рекламным сетям, как описано в <Anchor target="_blank" href="/partners/ru/docs/advanced-privacy-guide-postback-macros-for-ad-networks">руководстве по постбэкам Advanced Privacy</Anchor>. В следующей таблице перечислены тестовые сценарии в соответствии с доступными комбинациями настроек.

Для каждого сценария можно тестировать установки и события в приложении. Что касается событий в приложении, вы можете использовать <Anchor target="_blank" href="/partners/ru/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">сопоставление событий в приложении</Anchor>, чтобы сопоставить события рекламодателя с вашими событиями.

#### Комбинации тестовых сценариев

| Пример ситуации | Настройка Advanced Privacy | Настройка ATT в приложении | Тип отправляемого постбэка |
| --- | --- | --- | --- |
| А | Откл. | Разрешить | Regular |
| Б | Включен | Попросить приложение не отслеживать | Продвинутая защита данных |

## Тестирование

Выполните предварительные условия, а затем выполните тестовые процедуры в следующих разделах. Каждый тестовый раздел содержит таблицу, в которой можно записывать результаты тестов.

<div id="prerequisites" />

<Accordion title="Требования">

Перед тем как приступить к выполнению тестовой процедуры, выполните предварительные условия.

| Требования |
| --- |
| <Anchor target="_blank" href="/partners/ru/docs/getting-started-onboarding-guide-for-ad-networks#часть-1-интеграция-и-тестирование">Завершите стандартную интеграцию с AppsFlyer.</Anchor> При необходимости свяжитесь с AppsFlyer с помощью <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджета помощника для партнеров</Anchor>. |
| <Anchor target="_blank" href="/partners/ru/docs/self-serve-integration-management-for-ad-networks#постбэки-для-расширенной-конфиденциальности-и-постбэки-skan">Завершите интеграцию Расширенная конфиденциальность с AppsFlyer.</Anchor> При необходимости свяжитесь с AppsFlyer с помощью <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджета помощника партнера</Anchor>. |
| <Anchor target="_blank" href="/partners/ru/docs/turn-on-test-app-integration-for-ad-networks">Интегрируйте тестовое iOS-приложение в свою учетную запись.</Anchor> |
| [Убедитесь, что тестовое приложение интегрировано в вашу учетную запись](/docs/ios-integration-testing-for-ad-networks#test-app-integrated-in-your-account) |
| <Anchor target="_blank" href="/partners/ru/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">Сопоставьте события в приложении с названиями своих событий</Anchor>. Названия событий для сопоставления: `purchase`, `login`, `registration` |
| [Подготовьте ссылку атрибуции](/docs/ios-integration-testing-for-ad-networks#attribution-link) |
| Проведите тест на устройстве под управлением iOS 14.5+ |

</Accordion>

<div id="test-advanced-privacy-off" />

<Accordion title="Тест — расширенные настройки конфиденциальности: выкл">

**Чтобы активировать постбэки:**

1. На дэшборде AppsFlyer установите для параметра [Enable Advanced Privacy](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy) значение off.
2. На устройстве:
   1. Проверьте, что тестовое приложение не установлено. При необходимости удалите его.
   2. В настройках конфиденциальности убедитесь, что параметр **Allow Apps to Request to Track** is on.  

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. Отправьте ссылку атрибуции на тестовое устройство.
4. Откройте ссылку атрибуции в браузере устройства.  
   Вы будете перенаправлены в магазин приложений.
5. Скачайте и откройте приложение.  
   Появится диалоговое окно согласия ATT.

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. Нажмите **Allow**.  
   Откроется страница **Install Data**.

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. Нажмите **ATT Status**.  
   Отобразится статус **Авторизовано**.
8. Проверьте атрибуцию, используя следующие параметры. Если валидация не пройдена, см. раздел [Устранение неполадок](/docs/ios-integration-testing-for-ad-networks#troubleshooting).

   1. `install_time`: близко к текущему времени. Время указано в UTC.
   2. `af_status: Non-organic` Если это не так, установка не была атрибутирована.
   3. `media_source`: ваша рекламная сеть
9. Нажмите **Тесты in-app событий.**

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. Нажмите **Событие покупки.**  
    Появится подтверждение события покупки.
11. Проверьте, что:
    1. Вы получили постбэки об установке и покупке.
    2. Имя события сопоставлено правильно (если вы настроили события в приложении).
    3. Вы можете принять постбэк.

#### Расширенные настройки конфиденциальности отключены — результаты теста

| постбэк | Время запуска события | Ожидаемый тип постбэка | Фактически полученный постбэк (успешно/неуспешно) | Валидация постбэка (успешно/неуспешно) |
| --- | --- | --- | --- | --- |
| установка |  | Regular |  |  |
| In-app событие: Purchase |  | Regular |  |  |

</Accordion>

<div id="test-advanced-privacy-on" />

<Accordion title="Тест — расширенные настройки конфиденциальности включены">

**Чтобы инициировать постбэки:**

1. На дэшборде AppsFlyer включите параметр [Enable Advanced Privacy](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy).
2. На устройстве:
   1. Убедитесь, что тестовое приложение не установлено. Удалите это при необходимости.
   2. В настройках конфиденциальности проверьте, что параметр **Allow Apps to Request to Track** включен.

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. Отправьте ссылку атрибуции на тестовое устройство.
4. Откройте ссылку атрибуции в браузере на устройстве.  
   Вы будете перенаправлены в магазин приложений.
5. Скачайте и откройте приложение.  
   Появится диалоговое окно согласия ATT.

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. Нажмите **Попросить приложение не отслеживать.** Отображается страница **Install Data**.

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. Нажмите **ATT Status**.  
   Отобразится статус **Denied**.
8. Проверьте атрибуцию по перечисленным параметрам. Если валидация не пройдена, см. раздел [Troubleshooting](/docs/ios-integration-testing-for-ad-networks#troubleshooting).

   1. `install_time`: близко к текущему времени. Время указывается по UTC.
   2. `af_status: Non-organic` Если это не так, установка не атрибутирована.
   3. `media_source`: ваша рекламная сеть
9. Нажмите **In-App Event Tests.**

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. Нажмите **Purchase Event.**
11. Проверьте, что:
    1. Вы получили постбэки об установке и покупке.
    2. Название события сопоставлено правильно (если вы сопоставили события в приложении).
    3. Вы можете принять постбэк.

#### Расширенная конфиденциальность включена — результаты теста

| постбэк | Время запуска события | Ожидаемый тип постбэка | Полученный постбэк (успешно/неуспешно) | Валидация постбэка (успешно/неуспешно) |
| --- | --- | --- | --- | --- |
| установка |  | Продвинутая защита данных |  |  |
| Событие в приложении: Покупка |  | Продвинутая защита данных |  |  |

</Accordion>

## Дополнительная информация и процедуры

<div id="about-the-partner-integrations-test-app" />

<Accordion title="О тестовом приложении Partner Integrations">

Приложение Partner Integrations доступно в App Store. Приложение отправляет на платформу AppsFlyer установки и события в приложении.

При первом открытии приложения появляется диалоговое окно iOS **запросить отслеживание**, после чего отображается страница **Данные установки** с данными конверсии, записанными на платформе AppsFlyer. Тестовые события в приложении запускаются в пользовательском интерфейсе.

[<Image alt="PartnerIntegrationУстановкаData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)

Доступны следующие функции:

* **Тестирование событий в приложении**Отправить событие `покупки`, `входа` и `регистрации` в приложении. Если сопоставить названия событий в приложении с вашими названиями событий, постбэки будут заполняться вашими названиями событий.
* **Статус ATT**Возвращает текущий статус ATT, указанный iOS: **Authorized** или **Denied**. Статус ATT зависит от согласия пользователя на отслеживание в диалоговом окне согласия ATT и от настройки устройства **Разрешить приложениям запрашивать отслеживание**.

</Accordion>

<div id="attribution-link" />

<Accordion title="Ссылка атрибуции">

Подготовьте ссылку атрибуции в дэшборде AppsFlyer одним из следующих способов:

* Сгенерируйте ссылку на дэшборде AppsFlyer.
* Отредактируйте пример ссылки ниже.

**Чтобы сгенерировать ссылку в дэшборде:**

1. В AppsFlyer перейдите в **Мои приложения**.
2. Выберите **id1543229303**.
3. В боковом меню выберите **Сотрудничество** > **Активные интеграции** > выберите свою рекламную сеть > вкладку **Ссылка атрибуции**.
4. На вкладке «Ссылка атрибуции» задайте указанные параметры. При необходимости можно добавить дополнительные параметры. 

| Параметр | Пример значения | Замечание |
| --- | --- | --- |
| кампания; | c-test-2020-12-20 | Задайте значение, которое можно идентифицировать в ваших постбэках |

5. Скопируйте полученную ссылку для дальнейшего использования.

**Пример ссылки атрибуции:**

```http
https://app.appsflyer.com/id1543229303?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="set-advanced-privacy" />

<Accordion title="Настройте расширенную конфиденциальность">

<Image alt="AdvancedPrivacyOff.png" src="https://files.readme.io/ef845ea74cbaa0d3214e61c6e2229fd4b9026d0e221b19fecb9e3486e9b795eb-360014980157.png" width="357px" />

**Чтобы изменить настройку Enable Advanced Privacy:**

1. В AppsFlyer перейдите в **Мои приложения**.
2. Выберите приложение id1543229303.
3. В боковом меню выберите **Сотрудничество** > **Активные интеграции** > выберите свою рекламную сеть > вкладку **Интеграция**.
4. Установите для **Enable Advanced Privacy** подходящее значение для каждого тестового сценария.
5. Нажмите кнопку **Save Integration** (Сохранить интеграцию).

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="Тестовое приложение, интегрированное в ваш аккаунт">

**Чтобы убедиться, что тестовое приложение доступно в вашей учетной записи:**

1. В AppsFlyer перейдите в **Мои приложения**.
2. Убедитесь, что приложение **Partner Integrations id1543229303** отображается в разделе Available Apps. В противном случае обратитесь к своему менеджеру по развитию партнеров.

</Accordion>

<div id="troubleshooting" />

<Accordion title="Устранение неполадок">

| Симптом | Причина/корректирующее действие |
| --- | --- |
| Время установки не соответствует текущему времени | Приложение не было удалено перед установкой.<br /><br />Удалите приложение и повторите процедуру. |
| Медиаисточник не совпадает с вашим медиаисточником | Убедитесь, что в ссылке атрибуции указано правильное значение **pid**. Убедитесь, что вы используете правильную ссылку атрибуции |
| af\_status — органический | Убедитесь, что версия iOS на устройстве соответствует указанной в предварительных требованиях.<br /><br />Проверьте формат ссылки атрибуции, особенно значение **pid**. |

</Accordion>

<div data-zendesk-anchors="ios-integration-testing=ios-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 h_01HJR5YDW9ENA1B1AC1DQVX8SF=ios-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 testing-scope=%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F h_01HJR5YDW92MXP9DDBX9C1928V=%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F test-scenario-combinations=%D0%BA%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8-%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D1%85-%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B5%D0%B2 h_01HJR5YDW9Q7B10MXB1V4AKH2D=%D0%BA%D0%BE%D0%BC%D0%B1%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8-%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D1%85-%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B5%D0%B2 testing=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5 h_01HJR5YDW9AGY148E1ZD97JFRB=%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5 h_01HJR5YDW9SGN9KH63CPZ54RM5=prerequisites test%E2%80%94advanced-privacy-off=test-advanced-privacy-off h_01HJR5YDWA20EQT5RE1EJ7QK2X=test-advanced-privacy-off advanced-privacy-off%E2%80%94test-results=%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BE%D1%82%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D1%8B--%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B-%D1%82%D0%B5%D1%81%D1%82%D0%B0 h_01HJR5YDWAEAR22NPXF8ZD5QX6=%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BE%D1%82%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D1%8B--%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B-%D1%82%D0%B5%D1%81%D1%82%D0%B0 test%E2%80%94advanced-privacy-on=test-advanced-privacy-on h_01HJR5YDWAY6B55BFQ1B0WJEHR=test-advanced-privacy-on advanced-privacy-on%E2%80%94test-results=%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B0--%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B-%D1%82%D0%B5%D1%81%D1%82%D0%B0 h_01HJR5YDWAK3DZ1Q0W3TSR7ZKZ=%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%B0%D1%8F-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B0--%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B-%D1%82%D0%B5%D1%81%D1%82%D0%B0 supplementary-information-and-procedures=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%B8-%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D1%8B h_01HJR5YDWA74Q46F6XKY5J375C=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%B8-%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D1%8B h_01HJR5YDWASJWC1NGNABWR1VW5=about-the-partner-integrations-test-app h_01HJR5YDWA0WXWN5B5VNPK40FY=attribution-link h_01HJR5YDWA73BQB478D6N0R8GP=set-advanced-privacy h_01HJR5YDWAGZ5XMQJG1KX3J6CP=test-app-integrated-in-your-account h_01HJR5YDWAXRD7DVHTZPJCFM56=troubleshooting" />
