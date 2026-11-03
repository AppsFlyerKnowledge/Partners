---
title: Интеграция партнеров Meta по управлению кампаниями с AppsFlyer
metadata:
  keywords:
    - Callbacks
    - Integration
    - Facebook
    - Partner
    - In-App
    - partner account
    - User Level
    - Data policy
    - FMP
    - Partners
    - Developers
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
  created_at: '2015-03-29T12:38:26Z'
  edited_at: '2026-09-02T00:38:36Z'
  id: 207034146
  locale: ru
  section: Marketing partner onboarding
  section_id: 6551118224657
  url: https://support.appsflyer.com/hc/ru/articles/207034146
---
> **Краткий обзор:** Узнайте, какие типы данных партнеры Meta по управлению кампаниями могут получать от AppsFlyer.

## Постбэки установок

При конверсии AppsFlyer может возвращать следующие параметры:

| Имя параметра | Принятое обозначение параметра |
| --- | --- |
| Название кампании | `{campaign_name}` |
| Строка | `{campaign_id}` |
| Название набора рекламы | `{adset_name}` |
| Идентификатор ID набора рекламы | `{adset_id}` |
| Название группы объявлений | `{adgroup_name}` |
| Идентификатор группы объявлений | `{adgroup_id}` |
| Время события — с округлением в большую сторону | `{timestamp}` |
| Уникальный идентификатор ID пользователя AppsFlyer | `{sha1-appsflyer-device-id}` |
| Хешированный MD5 идентификатора устройства | `{md5IDFA\md4GAID}` |
| Если атрибуция получена по просмотру | `{is-impression}` |
| Канал (Instagram, Meta Audience Network, Facebook, Messenger) | `{af_channel}` |
| Гео/страна | `{user_country}` |

> 📄 **Пример**
>
> http://mcmp_postbackURL.........&mcmp_ADset_name =`{adset_name}`

## https://files.readme.io/8d5c3b6d1dd7542860d58b2cff8581a8eb72880764b730a4c87b8161eb04edab-360001712765.png

При событиях в приложении AppsFlyer может возвращать следующие параметры (в дополнение к указанным выше):

| Имя параметра | Принятое обозначение параметра |
| --- | --- |
| Имя события* | `{event_name}` |
| Значение события | `{event_value}` |

> 📄 **Пример**
>
> `http://FMP_postbackURL.........&eventname={event_name}`

* Партнер Meta по управлению кампаниями может выбрать, получать ли название события в приложении в том виде, в котором рекламодатель настроил его в SDK AppsFlyer, или предоставить рекламодателю возможность заполнять произвольное текстовое поле для каждого события.

## Политика в отношении данных уровня пользователя

* AppsFlyer не может передавать IDFA или Android Advertising ID.

* AppsFlyer передает временные метки установок/событий, округленные до ближайшего часа в большую сторону.

Например: если установка произошла в 4.32 pm и 42 секунды, мы можем передать 5 pm в качестве временной метки

* AppsFlyer может использовать случайный идентификатор, созданный им самим, чтобы привязывать его к событиям. Этот идентификатор не должен формироваться на основе IDFA/Android ID и должен быть уникальным для рекламы Meta. Тот же случайный идентификатор можно передавать дальше для постбэков событий в приложении.

> 📘 **Примечание:**
>
> Согласно условиям Meta, отправка постбэков доступна только для компаний, получивших следующий значок: Ad Technology

> 📄 **Пример**
>
> ![](https://files.readme.io/6832879dafaadb91a795988abdc5e51203c9c1775054e35829cfe60cb2175a66-360001440909.png)
>
> Полный список партнеров Meta по управлению кампаниями доступен <Anchor target="_blank" href="https://www.facebook.com/business/partner-directory/search?programBadges=ADTECH_FB.ADTECH_IG&solution_type=campaign_management">здесь</Anchor>.

<div data-zendesk-anchors="install-postbacks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA inapp-event-postbacks=httpssupportappsflyercomhcarticle_attachments360001712765 userlevel-data-policy=%D0%BF%D0%BE%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B0-%D0%B2-%D0%BE%D1%82%D0%BD%D0%BE%D1%88%D0%B5%D0%BD%D0%B8%D0%B8-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8F-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F" />
