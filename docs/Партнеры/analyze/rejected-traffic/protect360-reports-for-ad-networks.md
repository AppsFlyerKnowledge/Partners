---
title: Отчеты Protect360 для рекламных сетей
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2022-02-08T14:53:48Z'
  edited_at: '2026-09-02T00:36:13Z'
  id: 4420246395793
  locale: ru
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/ru/articles/4420246395793
---
> **Кратко:** Рекламные сети, отвечающие за привлечение пользователей и ретаргетинг, могут получать данные о заблокированных кликах и показах.

## Отчеты Protect360 для рекламных сетей

**Отказ от ответственности**: В этой статье представлена информация об отчетах Protect360, доступных только рекламным сетям. Чтобы узнать о данных, которые также доступны рекламодателям, см. <Anchor target="_blank" href="/partners/ru/docs/protect360-for-integrated-partners">Protect360 для интегрированных партнеров</Anchor>.

Рекламные сети могут получать отчеты через <Anchor target="_blank" href="/partners/ru/docs/data-locker-for-partners">Data Locker for Partners</Anchor> с ценной информацией о кликах и показах, которые блокируются по одной из следующих причин:

* Заблокированные клики и показы, возникающие, когда рекламные сети превышают лимит фрода. Отчет включает общее количество блокировок, а также блокировки из-за ограничения кликов и показов. <Anchor target="_blank" href="/partners/ru/docs/protect360-for-integrated-partners#ограничение-показов">Узнать больше об ограничении</Anchor>
* Недействительные сигнатуры кликов, которые возникают, когда клик с параметром PID сети и сигнатурой клика для валидации кликов не удается валидировать. <Anchor target="_blank" href="/partners/ru/docs/click-signing-for-ad-networks">Узнайте больше о подписи кликов</Anchor>

Затем рекламные сети могут загружать эти данные на уровне сети с межклиентской видимостью своих заблокированных кликов и показов и использовать их для защиты от фрода.

### Рекомендации по отчету

* Данные поступают в формате CSV в бакет партнера по UA/ретаргетингу.
* Содержит измерения и метрики, относящиеся к рекламной сети (то есть очищенные от всех измерений, не относящихся к рекламной сети).
* Доступно через <Anchor target="_blank" href="/partners/ru/docs/data-locker-for-partners">Data Locker for Partners</Anchor>.
* Актуальность данных: <Anchor target="_blank" href="/marketers/ru/docs/about-data-freshness-and-timezone-support#ad-revenue">Ежедневно, то есть данные за день 0 поступают в день 1</Anchor>. Данные записываются ежедневно в 07:00 <Anchor target="_blank" href="/marketers/ru/docs/about-data-freshness-and-timezone-support#daily">по времени UTC</Anchor> в h=23 вашего бакета Data Locker.
* Включенные приложения: один отчет содержит данные по всем приложениям.

## Типы отчетов

<div id="blocked-clicks-and-impressions" />

<Accordion title="Заблокированные клики и показы">

Этот отчет содержит агрегированные данные о кликах и показах, которые блокируются из-за ограничения или по любой другой причине.  

#### Структура отчета: Поля/измерения

| **Поле** | **Специфика** |
| --- | --- |
| app\_id (идентификатор приложения) | Идентификатор приложения на платформе AppsFlyer. |
| site\_id (идентификатор сайта) | Идентификатор ID, который определяет паблишера, показывающего рекламу. |
| дата | Заблокированная дата |
| agency (агентство) | <ul><li>Агентство, которое привело трафик через эту рекламную сеть.</li><li>Возвращается как null, если агентство не задействовано.</li></ul> |

#### Структура отчета: метрики

| **Поле** | **Специфика** |
| --- | --- |
| number\_of\_blocked\_clicks | Общее число заблокированных кликов сети |
| number\_of\_blocked\_impressions | Общее число заблокированных показов сети |
| number\_of\_capped\_clicks | Количество ограниченных кликов сети (из общего числа заблокированных кликов) |
| number\_of\_capped\_impressions | Количество ограниченных показов сети (из общего числа заблокированных показов) |

</Accordion>

<div id="failed-click-signatures" />

<Accordion title="Подписи неудачных кликов">

Этот отчет содержит данные на уровне пользователя о сбоях валидации сигнатур кликов. То есть, когда рекламные сети используют <Anchor target="_blank" href="/partners/ru/docs/click-signing-for-ad-networks">метод подписи кликов AppsFlyer</Anchor>, отчет содержит клики по URL-адресам с PID сети, у которых нет подтвержденных подписей кликов: либо подпись недействительна или срок ее действия истек, либо клик вообще не подписан. Сбои подписи кликов могут возникать из-за технических ошибок при реализации подписей кликов рекламной сетью или когда клики отправляет от имени сети (с ее PID) другая сторона.

#### Структура отчета: поля/измерения

| **Поле** | **Специфика** |
| --- | --- |
| время\_события |  |
| original\_url |  |
| failed\_signing\_reason | Например:<ul><li>Недопустимая подпись</li><li>Отсутствующая подпись</li><li>Просроченная подпись</li><li>Истек срок действия секретного ключа</li></ul> |
| is\_blocking\_enabled | Относится к режиму конфигурации <Anchor target="_blank" href="/partners/ru/docs/click-signing-for-ad-networks">API подписи кликов</Anchor>:<ul><li>TRUE — если включено.</li><li>FALSE — только для отчета.</li><li>Не включено в отчет, если отключено.</li></ul> |

</Accordion>

<div data-zendesk-anchors="protect360-reports-for-ad-networks=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%8B-protect360-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 report-considerations=%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D0%B0%D1%86%D0%B8%D0%B8-%D0%BF%D0%BE-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%83 report-types=%D1%82%D0%B8%D0%BF%D1%8B-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BE%D0%B2 report-structure-fieldsdimensions=%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0-%D0%BF%D0%BE%D0%BB%D1%8F%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F report-structure-metrics=%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0-%D0%BC%D0%B5%D1%82%D1%80%D0%B8%D0%BA%D0%B8 report-structure-fieldsdimensions::44afb679=%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0-%D0%BF%D0%BE%D0%BB%D1%8F%D0%B8%D0%B7%D0%BC%D0%B5%D1%80%D0%B5%D0%BD%D0%B8%D1%8F-1" />
