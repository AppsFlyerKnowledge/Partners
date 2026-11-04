---
title: Сигналы о доходе от рекламы для рекламных сетей UA
metadata:
  keywords:
    - Ad Network
    - Partner
    - ad revenue
    - Data Locker
    - Ad Networks
    - Partners
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-michael-talapov
    - ROI360
    - Ad Networks
  created_at: '2021-06-21T13:39:13Z'
  edited_at: '2026-08-18T00:38:26Z'
  id: 4402898251409
  locale: ru
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ru/articles/4402898251409
---
> **Краткий обзор:** Рекламные сети, отвечающие за привлечение пользователей, могут получать данные о доходах от рекламы и использовать их для оптимизации кампаний по привлечению пользователей своих клиентов.

Рекламные сети могут получать через Data Locker отчеты с ценной информацией о доходах от рекламы в отношении пользователей. Эти пользователи могут быть привлечены в результате кампаний, которые проводятся через них, или происходить из другого медиа-источника.

Затем рекламные сети могут использовать эти данные для алгоритмов таргетинга и оптимизации кампаний, а также для повышения эффективности кампаний ROAS на основе полного обзора доходов, полученных от привлечения пользователей.

<div id="set-the-ad-revenue-report-in-data-locker" />

## Настройка отчета по доходу от рекламы в Data Locker

Чтобы получить доступ к отчету по доходам от рекламы в Data Locker, необходимо выполнить следующие действия:

* Рекламные сети должны <Anchor target="_blank" href="/partners/ru/docs/data-locker-for-partners#set-up-data-locker">подключены к Data Locker для партнеров</Anchor>.
* Рекламные сети должны [настроить параметры вывода отчетов](#configure-the-report-output-settings) и [активировать отчет по доходам от рекламы](#enable-the-ad-revenue-report).
* Рекламодатели должны разрешить рекламным сетям просматривать отчет. <Anchor target="_blank" href="/marketers/ru/docs/share-ad-revenue-data-with-partners#ua-signals-for-ad-networks">Инструкции для рекламодателей</Anchor>

<div id="configure-the-report-output-settings" />

<Accordion title="Настройка параметров вывода отчета">

Чтобы настроить вывод отчета, выполните следующие действия:

1. **В AppsFlyer перейдите в разделОтчет** > Data Locker.
2. В области **Настройки вывода отчета** включите переключатель **Отправлять отчеты**.
3. Настройте свойства вывода отчетов.
   * Формат отчета (Parqet/CSV).
   * Метод сжатия отчета (Snappy/GZIPO/Без сжатия).
   * Максимальное количество строк в файле.
4. Просмотрите ожидаемый путь вывода файлов отчетов. Путь задается в соответствии с вашими настройками подключения. Подробнее о том, как настроить подключение читайте в разделе <Anchor target="_blank" href="/partners/ru/docs/data-locker-for-partners#set-up-data-locker">Настройка Data Locker</Anchor>.

</Accordion>

<div id="enable-the-ad-revenue-report" />

<Accordion title="Активация отчета по доходам от рекламы">

1. В разделе **Содержимое Data Locker** выберите типа отчета **Доход от рекламы [ежедневно]** .
2. Нажмите **Сохранить подключение**.
3. Убедитесь, что рекламодатель разрешил рекламной сети просматривать отчет.
4. Инструкции приведены в разделе <Anchor target="_blank" href="/marketers/ru/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">Предоставление рекламным сетям разрешения на получение данных о доходе от рекламы.</Anchor>

</Accordion>

<div id="report-specification" />

## Спецификация отчета

<div id="report-considerations" />

<Accordion title="Структура и формат отчета">

* Формат: Данные поступают в формате CSV в корзину S3 партнера по привлечению пользователей.
* Уровень: Содержит параметры и метрики на уровне устройства.
* Обогащение данных: Включает данные по доходу от рекламы от партнеров-посредников, а также добавляет данные по атрибуции, релевантные для рекламной сети UA (которые очищаются от всех параметров, не имеющих отношения к рекламной сети UA).
* Обновление данных: <Anchor target="_blank" href="/marketers/ru/docs/about-data-freshness-and-timezone-support#ad-revenue">Ежедневно, то есть данные за день 0 поступают в день 1</Anchor>. Данные записываются ежедневно в 21:00 <Anchor target="_blank" href="/marketers/ru/docs/about-data-freshness-and-timezone-support#daily">по UTC</Anchor> до h=23 вашей корзины Data Locker.
* Включенные приложения: В одном отчете содержатся данные по всем приложениям, для которых рекламодатели предоставили разрешение.
* Отчеты содержат данные обо всех типах конверсий: установки, повторные атрибуции, повторные вовлечения и переустановки.
* Валюта: В долларах США. Доход от события рассчитывается в долларах США в день, когда произошло событие.
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSoV1U_pMUoTFhIpyYQmUI1zQWArY19c8gMmsfpRiAaGXVZEG4WqgSC26u5-fv32j8ZQN4uxtNgVkYs/pub?output=csv">Посмотреть пример отчета</Anchor>

</Accordion>

<div id="report-structure" />

<Accordion title="Поля отчета">

| **Поле** | **Примечания** |
| --- | --- |
| Версия | Временная метка Unix в секундах. Пример: 1661315124 |
| app\_id (идентификатор приложения) | Идентификатор приложения на платформе AppsFlyer |
| время\_установки | <ul><li>Временная метка установки: ГГГГ-ММ-ДД ЧЧ:ММ:СС<br />Пример: 2020-08-16 11:22:33</li><li>Для устройств iOS 14+ и пользователей, не давших согласия, или если у рекламодателя включена функция расширенной конфиденциальности, время установки округляется до ближайшего часа.</li></ul> |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Заполняются только в том случае, если UA атрибутировано партнеру, получающему данные. |
| idfa, idfv, advertising\_id | <ul><li>Один и тот же идентификатор устройства, например IDFA, IDFV или advertiser\_id, может отображаться в нескольких строках при наличии нескольких событий монетизации доходов от рекламы.</li><li>Для устройств iOS 14+ и пользователей, не давших согласия на сбор данных, а также если рекламодатель включил функцию Расширенная конфиденциальность, этот параметр не отображается.</li></ul> |
| platform | Платформа устройства: iOS, Android или Windows Mobile |
| Страна | Код страны согласно <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor> Пример: US, CN. |
| original\_url | <ul><li>Для устройств iOS 14+ и пользователей, не давших согласия на сбор данных, а также если рекламодатель включил функцию Расширенная конфиденциальность, этот параметр не отображается.</li><li>Заполняются только в том случае, если UA атрибутировано партнеру, получающему данные.</li></ul> |
| рекламный\_блок |  |
| placement |  |
| mediation\_network |  |
| тип\_взаимодействия |  |

Метрики:

| **Поле** | **Примечания** |
| --- | --- |
| impressions (показы) | Количество показов рекламы пользователю |
| revenue\_usd | Ежедневный доход (в долларах США) по идентификатору устройства. **Примечание**: Если сумма дохода небольшая, она представлена в экспоненциальном формате. Например: 8.00E-05 |

</Accordion>

<div data-zendesk-anchors="set-the-ad-revenue-report-in-data-locker=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0-%D0%BF%D0%BE-%D0%B4%D0%BE%D1%85%D0%BE%D0%B4%D1%83-%D0%BE%D1%82-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D1%8B-%D0%B2-data-locker h_01H8Y7ABGVR7BNHEYVFKPFM4JN=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0-%D0%BF%D0%BE-%D0%B4%D0%BE%D1%85%D0%BE%D0%B4%D1%83-%D0%BE%D1%82-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D1%8B-%D0%B2-data-locker h_01H8Y7ABGV2T6GBE9BHJQM6FDF=configure-the-report-output-settings h_01H8Y7ABGVW6Y5RY7CVNM3EJZR=enable-the-ad-revenue-report report-specification=%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0 h_01H8Y7ABGVXJ9ZQCJ8BR0DST6W=%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D1%84%D0%B8%D0%BA%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0 h_01H8Y7ABGV0G4GJBRKKGNBSEC5=report-considerations h_01H8Y7ABGV81X0VFWTRMXGHYSA=report-structure" />
