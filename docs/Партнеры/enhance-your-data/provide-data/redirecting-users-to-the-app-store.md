---
title: Перенаправление пользователей в магазин приложений
metadata:
  keywords:
    - clicks
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2018-04-30T08:08:25Z'
  edited_at: '2026-08-18T00:39:34Z'
  id: 360000807629
  locale: ru
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ru/articles/360000807629
---
> **Краткий обзор:** Узнайте о вариантах перенаправления пользователей в магазин приложений после показа рекламы и о том, как отправлять данные о вовлечении в AppsFlyer.

<div id="overview" />

## Обзор

AppsFlyer получает данные о вовлечении (кликах и показах) для атрибуции несколькими способами:

* Пользователь **нажимает** на рекламу и [перенаправляется в AppsFlyer](#пользователи-перенаправляются-через-appsflyer), а затем в магазин приложений.
* Пользователь **нажимает на рекламу или просматривает** ее и [перенаправляется непосредственно в магазин приложений](#пользователи-направленные-непосредственно-рекламной-сетью), а **ссылка атрибуции отправляется AppsFlyer с устройства**.

В обоих случаях используется обычная <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">структура и параметры ссылок атрибуции</Anchor>.

<div id="note" />

> 📘 **Примечание:**
>
> Для SRN данные принимаются через специализированные API

<div id="users-redirected-via-appsflyer" />

## Пользователи перенаправляются через AppsFlyer

При нажатии на рекламу пользователь перенаправляется в AppsFlyer, который затем перенаправляет его в магазин приложений следующим образом:

1. Пользователь перенаправляется на AppsFlyer
2. AppsFlyer регистрирует клик
3. AppsFlyer перенаправляет пользователя в магазин приложений
4. Пользователь устанавливает приложение
5. AppsFlyer атрибутирует установку

<div id="users-sent-directly-by-the-ad-network" />

## Пользователи, направленные непосредственно рекламной сетью

При нажатии на рекламу рекламная сеть перенаправляет пользователя в магазин приложений, сводя к минимуму количество перенаправлений:

1. Пользователь направляется в магазин приложений
2. Рекламная сеть передает AppsFlyer данные о вовлечении с устройства
3. Пользователь устанавливает приложение
4. AppsFlyer атрибутирует установку

<div id="sending-engagement-data-to-appsflyer" />

### Отправка данных о вовлечении в AppsFlyer

Направление пользователя непосредственно в магазин приложений улучшает пользовательский опыт за счет сокращения количества перенаправлений. Это также обеспечивает точную атрибуцию установок и высококачественный трафик.

Рекламные сети могут сообщать AppsFlyer о кликах и показах только **непосредственно с устройства пользователя**.

<div id="timing-of-sending-redirects" />

#### Синхронизация отправки перенаправлений

Чтобы предотвратить потерю атрибуций и доходов рекламной сети, клики и показы должны отправляться в AppsFlyer в режиме реального времени:

* **URL-адреса показов** должны быть переданы после показа рекламы
* **URL-адреса кликов** должны быть переданы, как только пользователь нажимает на рекламу

<div data-zendesk-anchors="overview=%D0%BE%D0%B1%D0%B7%D0%BE%D1%80 h_01HDY3CARC0A9504XGMJHYHGY4=%D0%BE%D0%B1%D0%B7%D0%BE%D1%80 h_01HDY3CARCZK06C5XHEQFQYA8W=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 redirect-users-via-appsflyer=%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8-%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%82%D1%81%D1%8F-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-appsflyer 01HDYFGYW3FDR64C54KKPXRHDF=%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8-%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D1%8F%D1%8E%D1%82%D1%81%D1%8F-%D1%87%D0%B5%D1%80%D0%B5%D0%B7-appsflyer send-users-directly-by-the-ad-network=%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8-%D0%BD%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BD%D0%B5%D0%BF%D0%BE%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D0%BE%D0%B9-%D1%81%D0%B5%D1%82%D1%8C%D1%8E 01HDYFH8ZCSP2SN4ZYQQVG7EED=%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8-%D0%BD%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D0%BD%D0%B5%D0%BF%D0%BE%D1%81%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D0%BE%D0%B9-%D1%81%D0%B5%D1%82%D1%8C%D1%8E send-engagement-data-to-appsflyer=%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BE-%D0%B2%D0%BE%D0%B2%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B8-%D0%B2-appsflyer h_01HDYGSEFHVF8ZD43XCVNGYT9N=%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BE-%D0%B2%D0%BE%D0%B2%D0%BB%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B8-%D0%B2-appsflyer timing-of-sending-redirects=%D1%81%D0%B8%D0%BD%D1%85%D1%80%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B8-%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B9 h_01HDXXDDXDEP43YHE3GF81BSKV=%D1%81%D0%B8%D0%BD%D1%85%D1%80%D0%BE%D0%BD%D0%B8%D0%B7%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B8-%D0%BF%D0%B5%D1%80%D0%B5%D0%BD%D0%B0%D0%BF%D1%80%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B9" />
