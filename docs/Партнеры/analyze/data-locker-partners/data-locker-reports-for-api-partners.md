---
title: Отчеты Data Locker для маркетинговых партнеров
metadata:
  keywords:
    - Advertisers
    - Partners
    - marketing partners
    - Marketers
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Marketers
    - Data Locker
  created_at: '2023-01-08T11:32:00Z'
  edited_at: '2026-09-02T00:36:00Z'
  id: 12000718524561
  locale: ru
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ru/articles/12000718524561
---
> **Краткий обзор**. Отчеты, упомянутые в этой статье, доступны вам (маркетинговым партнерам) в Data Locker. Чтобы мы могли предоставлять вам данные, рекламодатель (владелец приложения) должен предоставить вам доступ к данным, как описано в этой статье.

<div id="data-locker-reports-for-api-partners" />

## Отчеты Data Locker для маркетинговых партнеров

Чтобы получить отчет, вы как маркетинговый партнер должны:

* Проверить, что рекламодатель предоставил вам разрешение на <Anchor target="_blank" href="/partners/ru/docs/access-to-aggregated-analytics-tools-for-api-partners#grant-permission-to-a-partner">доступ к агрегированной отчетности и аналитике</Anchor>.
* <Anchor target="_blank" href="/partners/ru/docs/data-locker-for-partners#set-up-data-locker">Настроить Data Locker</Anchor>. **Примечание**. Пропустите шаги 3-4.

Маркетинговым партнерам доступны следующие отчеты:

* <Anchor target="_blank" href="/marketers/ru/docs/cohort-analytics-via-data-locker">Объединенные когорты</Anchor> (ежедневно)
* <Anchor target="_blank" href="/marketers/ru/docs/cohort-analytics-via-data-locker">Привлечение пользователей по когортам</Anchor> (ежедневно)
* <Anchor target="_blank" href="/marketers/ru/docs/cohort-analytics-via-data-locker">Когорты: ретаргетинг</Anchor>
* [Бета-версия] Также доступны отчеты по версиям и с улучшенной актуальностью данных.

Отчеты передаются в папку h=23.

<div id="specifications-and-limitations" />

<Accordion title="Спецификации и ограничения">

| Специфика | Примечания |
| --- | --- |
| Прозрачность агентства | Не поддерживается |
| Часовой пояс приложения | Доступно в расширенных агрегированных (версионных) отчетах |
| Валюта приложения | Да |
| органические данные | Доступно |
| Неорганические данные | Доступно |
| Данные о затратах | Не доступно |
| Актуальность данных | <ul><li>Для ежедневных когортных отчетов:<ul><li>Отчеты обычно доступны к 10:00 UTC в папке h=23 за предыдущий день. Например, отчет для данных, созданных в понедельник, находится в папке понедельника h=23.</li><li>Исключение: события, связанные с доходами от рекламы, имеют актуальность данных за день 0+3. То есть события, связанные с доходами от рекламы, в отчете за понедельник произошли в субботу.</li></ul></li><li>[Бета-версия] Отчеты по версиям обычно доступны с 06:00 UTC.</li></ul> |

Специфика

</Accordion>

<div id="see-also" />

> 📄 **См. также**
>
> * <Anchor target="_blank" href="/partners/ru/docs/access-to-aggregated-analytics-tools-for-api-partners">Инструменты агрегированной аналитики для маркетинговых партнеров</Anchor>

<div data-zendesk-anchors="data-locker-reports-for-marketing-partners=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%8B-data-locker-%D0%B4%D0%BB%D1%8F-%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D1%8B%D1%85-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D0%BE%D0%B2 h_01HBZZ5BFJC82MW9JQ9MEX991S=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%8B-data-locker-%D0%B4%D0%BB%D1%8F-%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%B8%D0%BD%D0%B3%D0%BE%D0%B2%D1%8B%D1%85-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D0%BE%D0%B2 h_01HBZZ5BFJYFH54X70RJ63CJCV=specifications-and-limitations h_01HE7RFGCZ65YJRX1VCND691CX=%D1%81%D0%BC-%D1%82%D0%B0%D0%BA%D0%B6%D0%B5" />
