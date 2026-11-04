---
title: Включите интеграцию тестового приложения с рекламными сетями
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
  created_at: '2021-05-22T15:56:20Z'
  edited_at: '2026-09-12T00:36:50Z'
  id: 360020713538
  locale: ru
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ru/articles/360020713538
---
> **At a glance:** Рекламные сети, которые тестируют интеграцию, должны включить интеграцию приложения (активацию).

<div id="test-apps-for-ad-networks-ios-and-android" />

## Тестовые приложения для рекламных сетей (iOS и Android)

После настройки интеграции и постбэков рекламные сети должны протестировать интеграцию с помощью тестовых приложений AppsFlyer. Перед тестированием рекламная сеть должна активировать интеграцию приложения и при необходимости включить дополнительные разрешения для рекламной сети. Активация выполняется один раз для каждого приложения.

| Тип тестового приложения | Название приложения или идентификатор |
| --- | --- |
| <Anchor target="_blank" href="/partners/ru/docs/getting-started-onboarding-guide-for-ad-networks#часть-2-тестирование-при-помощи-приложений-рекламодателя">Android;</Anchor> | com.appsflyer.adNetworkTest |
| <Anchor target="_blank" href="/partners/ru/docs/ios-integration-testing-for-ad-networks">https://files.readme.io/f28d0aac1797ee18fdc6083d9ea6d5d2f87d37a894a6c27ab0ea9b6ca51c53a1-49839256665233.png</Anchor> | id1543229303 |
| <Anchor target="_blank" href="/partners/ru/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> | <ul><li>id888707085</li><li>id888707086</li><li>id888707087</li></ul> |

<div id="activation-procedure" />

### Процедура активации

Чтобы активировать интеграцию для определенного тестового приложения, выполните следующую процедуру. Выполните эту процедуру один раз для каждого приложения.

**Чтобы активировать интеграцию и предоставить разрешения для тестового приложения**:

1. В AppsFlyer выберите тестовое приложение из списка в предыдущей таблице.
2. В AppsFlyer в боковом меню выберите **Сотрудничество** > **Интеграции с партнерами** > **Активные интеграции**.
3. Выберите рекламную сеть.
4. **Чтобы активировать интеграцию с приложением**:  
   1. Перейдите на вкладку **Интеграция**.
   2. Установите переключатель **Активировать партнера** в положение «Включено».
   3. Нажмите **Сохранить интеграцию**.
5. **Чтобы предоставить разрешения**:
   1. Перейдите на вкладку **Permissions** (Разрешения).
   2. Включите **Configure integration**.
   3. Включите **Настройку постбэков по событиям в приложении.**
   4. Нажмите **Сохранить разрешения**.

<div data-zendesk-anchors="test-apps-for-ad-networks-ios-and-android=%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9-ios-%D0%B8-android h_01HKA15VM7FM69X0AZ1V2H5XPJ=%D1%82%D0%B5%D1%81%D1%82%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9-ios-%D0%B8-android activation-procedure=%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D0%B0-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D0%B8 h_01HKA15VM7J47374WMRG5132GN=%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D0%B0-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%B0%D1%86%D0%B8%D0%B8" />
