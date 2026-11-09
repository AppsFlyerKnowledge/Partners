---
title: Импорт данных о затратах для рекламных сетей
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Gray
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2019-10-20T06:03:13Z'
  edited_at: '2026-08-18T00:39:02Z'
  id: 360002868097
  locale: ru
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ru/articles/360002868097
---
> **Краткий обзор:** Узнайте, как рекламные сети могут сообщать о расходах рекламодателя на кампанию непосредственно в AppsFlyer через файлы CSV.

<div id="cost-import-for-ad-networks" />

## Импорт данных о затратах для рекламных сетей

<Image align="center" alt="AdspendIngestion.jpg" src="https://files.readme.io/e870005c5f20531a2d06cc78b47a82a8a1f730f2c04728f5d0a5674c1c70129a-24507313816337.jpg" />

<div id="overview" />

#### Обзор

* Подготовьте CSV-файл, содержащий подробную информацию о расходах на рекламу, следующим образом:
  * Дата расходов
  * Идентификатор приложения (в одном файле разрешено несколько приложений, если приложения принадлежат одному владельцу)
  * Медиа-источник (допускается один на каждый файл)
  * Название кампании
  * Сумма расходов
  * [Необязательно] Гео
  * [Необязательно] Валюта (по умолчанию доллар США)
* Отправьте файл в AppsFlyer по электронной почте или загрузите файл, используя аккаунт рекламной сети в AppsFlyer.   
  **Примечание.**
  * Прежде чем вы отправите файлы в первый раз, рекламодатель должен предоставить вам, рекламной сети, разрешение на импорт данных о затратах. Это необходимо сделать один раз для каждого приложения, и это очень короткий процесс.
  * После загрузки файла его невозможно вернуть.
* Отслеживайте файл и проверяйте, чтобы в файле не было ошибок.

<div id="submitting-ad-spend-files-for-ad-networks" />

### Отправка файлов о рекламных расходах для рекламных сетей

* Для импорта файлов о расходах на рекламу используйте метод загрузки или электронную почту.
* [Рекомендации] Сначала используйте метод загрузки, поскольку так проще решить проблемы с форматированием CSV.
* Рекламные сети не могут импортировать данные о затратах агентств – это могут делать только рекламодатели.

<div id="submission-by-file-upload" />

#### Отправка путем загрузки файла

**Чтобы отправить файлы с данными о затратах путем загрузки:**

1. [Для каждого приложения, с которым вы работаете, это необходимо сделать один раз] <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-permissions-for-ad-networks">Попросите рекламодателя предоставить вам разрешение на импорт данных о затратах</Anchor>.
2. <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#prepare-csv-file-with-cost-data">Подготовьте файл CSV, используя этот формат и схему</Anchor>.
3. Нажмите здесь, чтобы <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">войти в свой аккаунт рекламной сети в AppsFlyer.</Anchor>
4. <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#upload-file">Загрузите и импортируйте файл</Anchor>.
5. Отслеживайте импорт на дэшборде AppsFlyer:

   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">Статус</Anchor>
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#matched-rows">Сопоставленные строки</Anchor>
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">Действия с импортом данных о затратах</Anchor>
6. Дополнительные процедуры:
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">Перезаписать предыдущий импорт</Anchor>
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">Вернуть (отменить)</Anchor>

<div id="submission-by-email" />

#### Отправка по электронной почте

**Чтобы отправить файлы с данными о затратах по электронной почте:**

1. [Для каждого приложения, с которым вы работаете, это необходимо сделать один раз] <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-permissions-for-ad-networks">Попросите рекламодателя предоставить вам разрешение на импорт данных о затратах</Anchor>.
2. <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#prepare-csv-file-with-cost-data">Подготовьте файл CSV, используя этот формат и схему</Anchor>.
3. Если у вас нет токена для импорта данных о затратах (он понадобится вам при отправке файла по электронной почте):
   * Нажмите здесь, чтобы <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">войти в свой аккаунт рекламной сети в AppsFlyer</Anchor>.
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#token-for-email-import">Получите токен расходов на рекламу.</Anchor> Примечание. Для всех рекламодателей используется один и тот же токен.
4. Отправьте файл по <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#email-file">электронной почте</Anchor>
5. AppsFlyer отправляет отчет о статусе, в котором отмечается, успешно ли прошел импорт или были обнаружены проблемы. **Примечание**: Если письмо о статусе не получено, обратитесь к <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">дэшборду импорта данных о затратах</Anchor>.
6. Отслеживайте импорт на дэшборде AppsFlyer:

   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">Статус</Anchor>
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#matched-rows">Сопоставленные строки</Anchor>
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">Действия с импортом данных о затратах</Anchor>
7. Дополнительные процедуры:
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">Перезаписать предыдущий импорт</Anchor>
   * <Anchor target="_blank" href="/marketers/ru/docs/import-cost-data#cost-import-dashboard">Вернуть (отменить)</Anchor>

<div data-zendesk-anchors="ad-spend-ingestion-for-ad-networks=%D0%B8%D0%BC%D0%BF%D0%BE%D1%80%D1%82-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BE-%D0%B7%D0%B0%D1%82%D1%80%D0%B0%D1%82%D0%B0%D1%85-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 h_01HX94WSX07YEG40X66TMRFJGA=%D0%B8%D0%BC%D0%BF%D0%BE%D1%80%D1%82-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BE-%D0%B7%D0%B0%D1%82%D1%80%D0%B0%D1%82%D0%B0%D1%85-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 overview=%D0%BE%D0%B1%D0%B7%D0%BE%D1%80 h_01HX94WSX0HR2KTGRT7MQ481Y6=%D0%BE%D0%B1%D0%B7%D0%BE%D1%80 submitting-ad-spend-files-for-ad-networks=%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2-%D0%BE-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%80%D0%B0%D1%81%D1%85%D0%BE%D0%B4%D0%B0%D1%85-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 h_01HX94WSX0G429FTHKYCG07BB9=%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D1%84%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2-%D0%BE-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%80%D0%B0%D1%81%D1%85%D0%BE%D0%B4%D0%B0%D1%85-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 submission-by-file-upload=%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D1%83%D1%82%D0%B5%D0%BC-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0 h_01HX94WSX0ENTJEDMXWRHDCP0D=%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D1%83%D1%82%D0%B5%D0%BC-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8-%D1%84%D0%B0%D0%B9%D0%BB%D0%B0 submission-by-email=%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE-%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BF%D0%BE%D1%87%D1%82%D0%B5 h_01HX94WSX0HVTMFQQ0NMW0VSKP=%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B0-%D0%BF%D0%BE-%D1%8D%D0%BB%D0%B5%D0%BA%D1%82%D1%80%D0%BE%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BF%D0%BE%D1%87%D1%82%D0%B5" />
