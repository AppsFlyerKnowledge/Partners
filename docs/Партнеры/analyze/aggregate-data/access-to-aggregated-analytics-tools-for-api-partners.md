---
title: Доступ к инструментам агрегированной аналитики для API-партнеров
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Premium API
    - Marketers
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketers
    - Marketing Analytics
    - Ad Networks
  created_at: '2020-02-17T10:50:10Z'
  edited_at: '2026-10-19T14:33:29Z'
  id: 360005854857
  locale: ru
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/ru/articles/360005854857
---
> **At a glance:** API-партнеры могут использовать свой токен API для доступа к данным рекламодателей с разрешения рекламодателя, что позволяет им извлекать из платформы метрики эффективности.

<div id="api-token-permissions" />

## Разрешения токена API

<Image alt="api-access-permissions.jpg" src="https://files.readme.io/7961394cb39cf1e6f85d77cd732183edea5fb1408c220ca05b23ae7bbb50138e-23701010316689.jpg" width="439px" />

Рекламодатели могут предоставлять следующие разрешения на уровне приложения:

| Тип разрешения | Инструмент отчетности | Характеристики и ограничения |
| --- | --- | --- |
| Отчетность по агрегированной аналитике | <Anchor target="_blank" href="/marketers/ru/docs/cohort-analytics-via-data-locker">Когортные аналитические данные через Data Locker</Anchor> | Данные кампаний X Ads недоступны для API-партнеров из-за ограничений со стороны X Ads. |
| Отчетность SKAN | <ul><li><Anchor target="_blank" href="/marketers/ru/docs/skan-aggregated-performance-report-api">Отчетность по эффективности SKAN</Anchor></li><li><Anchor target="_blank" href="/marketers/ru/docs/skan-aggregated-postback-arrival-date-api">Агрегированная отчетность о постбэках SKAN</Anchor></li></ul> | -- |


<div id="considerations" />

### Соображения

* **С точки зрения рекламодателя**
  * Рекламодатели могут предоставлять API-партнерам разрешения, перечисленные в приведенной выше таблице.
* **С точки зрения партнера**
  * Извлечение данных через API. **Примечание**: безопасность обеспечивается с помощью аутентификационного <Anchor target="_blank" href="/marketers/ru/docs/managing-appsflyer-tokens">токена</Anchor>, доступного в дэшборде AppsFlyer. Один и тот же токен действителен для всех приложений и рекламодателей.
  * Получение данных через Data Locker
  * Рекламодатели могут отзывать разрешения на доступ к данным своих приложений. Это не повлияет на учетные данные вашего партнера.

<Accordion title="Предоставление доступа партнеру">

> 🚧 **Important**
>
> **предупреждение**
>
> * Этот тип разрешения дает партнеру доступ к данным, включая трафик, привлеченный другими партнерами, и органические данные.
> * Не делитесь своим токеном с партнерами.

**Чтобы предоставить партнеру доступ к API:**

1. В AppsFlyer в боковом меню выберите **Collaborate** > **Integrated partners**.
2. Найдите партнера и выберите его.
3. Нажмите **Настроить интеграцию**. Вы будете перенаправлены на страницу настройки интеграции.
4. На вкладке **Доступ к API** включите одно или несколько разрешений. Выберите один из вариантов:
   * **Отчетность по агрегированной аналитике**
   * **Отчетность SKAdNetwork** (для приложений iOS, не относится к Data Locker)
5. Нажмите **Сохранить доступ к API**.
6. Сообщите партнеру, что вы включили необходимый доступ к API.

</Accordion>

<div data-zendesk-anchors="api-access-permissions=%D1%80%D0%B0%D0%B7%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%B0-api h_01HGG3N6KVF9MCQRW8594YG0HV=%D1%80%D0%B0%D0%B7%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D1%8F-%D1%82%D0%BE%D0%BA%D0%B5%D0%BD%D0%B0-api considerations=%D1%81%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01HT2J7ZFVDA812R35948XXEM1=%D1%81%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01KZXND2TWVKK51RH3JWNMFENK=%D1%81%D0%BE%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F" />
