---
title: Protect360 для интегрированных партнеров.
metadata:
  keywords:
    - Protect360
    - Ad Networks
    - Partners
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2017-09-19T08:27:29Z'
  edited_at: '2026-08-19T00:36:59Z'
  id: 115004745523
  locale: ru
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/ru/articles/115004745523
---
> **Краткий обзор.** Интегрированные партнеры (рекламные сети и агентства) могут отслеживать мошенничество, связанное с выявлением и блокировкой трафика механизмами ProtectLite и Protect360, а также правилами валидации клиентов, определенными вручную.

<div id="overview" />

## Обзор

AppsFlyer выявляет и блокирует мошенничество следующим образом: 

* <Anchor target="_blank" href="/marketers/ru/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">ProtectLITE</Anchor>: Базовая защита от мошенничества для всех клиентов.
* <Anchor target="_blank" href="/marketers/ru/docs/protect360-anti-fraud-guide">Protect360</Anchor>: Расширенная защита от мошенничества для рекламодателей с премиум-планом подписки.

Рекламодатели должны предоставить:

* <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#permissions-tab">Разрешения</Anchor> рекламным сетям на **доступ к дэшборду Protect360 и отчетам по сырым данным** (включая ProtectLite), а также **доступ к агрегированным данным о внутренних событиях приложения** (для выявления мошенничества в приложениях).
* **Необходимые условия**: Разрешение рекламодателя на доступ к ProtectLite и Protect360.

При наличии нужных разрешений интегрированные партнеры могут:

* Просматривать данные, связанные с трафиком, сгенерированным этим партнером.
* Скачать соответствующие отчеты по <Anchor target="_blank" href="/marketers/ru/docs/protect360-anti-fraud-guide#raw-data">сырым данным</Anchor>.

Рекламным сетям также доступны <Anchor target="_blank" href="/partners/ru/docs/protect360-reports-for-ad-networks">отчеты по сырым данным</Anchor> об ограничении кликов и показов, а также о кликах с неудачными подписями, для которых разрешение рекламодателя не требуется.

<div id="note" />

> 📘 **Примечание**
>
> Для рекламодателей, которые работают с рекламными сетями через агентство, чтобы и рекламная сеть, и агентство имели доступ к данным, рекламодатель должен настроить в AppsFlyer интеграцию с агентством и рекламной сетью и предоставить им обоим доступ к данным.
>
> Если интегрировано и имеет доступ только агентство, у рекламной сети не будет доступа к данным.

<div id="dashboard-view" />

### Представление дэшборда

**Необходимые условия**: Разрешение рекламодателя на доступ к ProtectLite и Protect360. 

Интегрированные партнеры могут просматривать дэшборд и диаграммы; см. следующий скриншот.

Для рекламодателей, которые работают с рекламными сетями через агентство: чтобы доступ к данным имели и рекламная сеть, и агентство, рекламодатель должен настроить в AppsFlyer интеграцию с ними обоими и разрешить им обоим доступ к данным.   

Ограничения:

* Рекламные сети не могут получить доступ к дэшборду аномалий.

<Image align="center" alt="p360_dashboard_1.jpg" src="https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg" />

* Рекламные сети и агентства не имеют доступа к Fraud protection studio или к уровню сырых данных размеченных данных. Однако они могут видеть их в агрегированном виде в дэшборде Protect360 в разделах Tagged attribution и Tagged in-app events. А также выявлять фрод по типу тега (новый релиз и т. д.). Чтобы узнать больше о FPS, смотрите <Anchor target="_blank" href="/marketers/ru/docs/beta-fraud-protection-studio">эту статью</Anchor>.

  <Image align="center" alt="" src="https://files.readme.io/7e8bee04ecaf53148f65ae0aa9b2e3559a550bdbc5a5ebf9047a7e82dc093966-44928678660881.png" width="624px" />

  <Image align="center" alt="" src="https://files.readme.io/fa35e6046d6c06579e602ccc1cb919e5312ec22055b3e29d3ead6b2a7ab5ea82-44928694758161.png" width="624px" />

<div id="raw-data-reports" />

### Отчеты по сырым данным

**В: Это мешает нам масштабировать кампании, и мы не хотим, чтобы эти показы/клики блокировались.**   


Отчеты Protect360 по сырым данным показывают выявленное и заблокированное мошенничество с помощью ProtectLite, Protect360 и правил валидации.

Отчеты доступны через:

* Экспорт данных: В AppsFlyer в боковом меню выберите **Отчеты** > **Экспорт сырых данных**.
* API: См. следующий раздел [API отчетности для рекламных сетей](/docs/protect360-for-integrated-partners#api-отчетности-по-protect360-для-рекламных-сетей).

Узнайте больше об отчетах <Anchor target="_blank" href="/marketers/ru/docs/protect360-raw-data-reports">Protect360 по сырым данным</Anchor>.

<div id="protect360-ad-network-reporting-api" />

## API отчетности по Protect360 для рекламных сетей

* Отчеты по сырым данным, перечисленные в этом разделе, доступны рекламным сетям через API.
* Эквивалентные отчеты доступны на дэшборде на странице Экспорт данных.
* Если у рекламодателя нет подписки Protect360, доступен только отчет об установках.

**Необходимые условия**

* Чтобы получить доступ к данным рекламодателя с помощью API, рекламодатель предоставляет рекламной сети <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#permissions-tab">разрешение</Anchor> на доступ к дэшборду Protect360 и к данным по API. Рекламным сетям, имеющим доступ к дэшборду, разрешено использовать API. От рекламодателя не требуется никаких действий.
* Чтобы получить список приложений, для которых у вас есть разрешения Protect360, используйте API <Anchor target="_blank" href="/partners/ru/docs/app-list-api-for-ad-networks">для получения списка приложений</Anchor>.
* Администратору необходимо получить <Anchor target="_blank" href="/marketers/ru/docs/managing-appsflyer-tokens">токен аутентификации AppsFlyer V2.0</Anchor>, доступный на дэшборде.

<div id="protect360-api-reports" />

#### Отчеты Protect360 по API

| Отчет | Актуальность данных | Описание |
| --- | --- | --- |
| Пост-атрибуционное мошенничество с событиями внутри приложения | Ежедневно 10:00 UTC | <ul><li>События в приложении, выполненные в результате установок, идентифицированных как мошеннические.</li><li>Любое другое событие в приложении, которое оценивается как мошенническое независимо от установки.</li></ul>Отчет можно дополнительно отфильтровать по типу внутреннего события, как описано в таблице параметров ниже.<br /><br />Тема отчета: `fraud-post-inapps` |
| Установки после атрибуции | Ежедневно 10:00 UTC | <ul><li>Установки, идентифицированные как мошеннические после атрибуции.</li><li>Отчет можно дополнительно отфильтровать по дате обнаружения, как описано в следующем разделе.</li></ul>Тема отчета: обнаружение |
| Установки | В реальном времени | Блокированные установки с причиной блокировки<br /><br />Тема отчета: отчет о заблокированных установках |
| Внутреннее событие приложения | В реальном времени | События в приложении, выполняемые заблокированными пользователями<br /><br />Тема отчета: `blocked_in-app_events_report` |
| клики; | В реальном времени | Клики, выполненные заблокированными пользователями<br /><br />Тема отчета: `blocked_clicks_report` |

<div id="procedure-for-ad-networks-to-get-protect360-reports-by-download" />

#### **Процедура получения отчетов Protect360 рекламными сетями путем загрузки**

**Чтобы получить отчет по API:**

1. Определите необходимый отчет из предыдущего списка.
2. Используйте соответствующий пример curl (в следующем разделе) для подготовки скрипта.
3. Обязательно замените следующие заполнители своими данными:
   1. Идентификатор приложения
   2. С даты
   3. До даты
   4. Токен предъявителя (<Anchor target="_blank" href="/marketers/ru/docs/managing-appsflyer-tokens">токен аутентификации AppsFlyer V2.0</Anchor>)
4. Некоторые вызовы имеют [дополнительные параметры](/docs/protect360-for-integrated-partners#api-parameters), как описано в этой статье.

<div id="curl-examples" />

### Пример curl

<div id="installs-blocked_installs_report" />

<Accordion title="Установки (blocked_installs_report)">

Замените заполнители app\_id, from, to и token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_installs_report/app/{app_id}?from={2020-07-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \ \
```

</Accordion>

<div id="postattribution-installs-detection" />

<Accordion title="Установки после атрибуции (обнаружение)">

Замените заполнители app\_id, from, to и token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/detection/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additonal-fields=fraud_reason,fraud_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \ \
```

</Accordion>

<div id="inapp-event-blocked_in_app_events_report" />

<Accordion title="Внутренние события (blocked_in_app_events_report)">

Замените заполнители app\_id, from, to и token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_in_app_events_report/app/?from=YYYY-MM-DD&to=YYYY-MM-DD&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \ \
```

</Accordion>

<div id="postattribution-inapp-events-fraud-fraud_post_inapps" />

<Accordion title="Мошенничество с событиями в приложении после атрибуции (fraud_post_inapps)">

Замените заполнители app\_id, from, to и token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/fraud-post-inapps/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,fraud_reason,fraud_sub_reason,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \ \
```

</Accordion>

<div id="clicks-blockedclicks_report" />

<Accordion title="Клики (blocked-clicks_report)">

Замените заполнители app\_id, from, to и token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_clicks_report/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \ \
```

</Accordion>

<div id="protect360-ad-network-api-reference-guide" />

### Справочное руководство по API Protect360 для рекламных сетей

<div id="api-basics" />

<Accordion title="Основы API">

Основы API Protect360 для рекламных сетей:

| Путь | `https://hq1.appsflyer.com/api/adnets-data/v1/export/report_topic/app/app_id` |
| --- | --- |
| Метод | УСТАНОВИТЬ |
| Параметры пути (обязательные) | <ul><li>`app_id`:<ul><li>Идентификатор приложения, указан на дэшборде AppsFlyer. Вставьте его точно так, как он показан на дэшборде.</li><li>Обязательно добавьте к приложениям iOS префикс **id**.</li></ul></li><li>`report_topic`:</li></ul> |
| Принятые типы контента | `application/json` |
| Авторизация | <ul><li>Токен предъявителя в заголовке запроса.</li><li>![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png)Попросите администратора получить токен V2.0 со страницы <Anchor target="_blank" href="/marketers/ru/docs/managing-appsflyer-tokens">токенов</Anchor>. Длина токена составляет около 700 символов.</li></ul> |
| Ограничение предоставления данных | <Anchor target="_blank" href="/marketers/ru/docs/report-generation-quotas-rate-limitations">Ограничение предоставления данных</Anchor> |
| Ограничение диапазона дат | <ul><li>Самая ранняя дата: 90 дней до текущих данных</li><li>31 день из предыдущих 90 дней</li></ul> |
| Ограничения строк | 200 тыс. строк |
| Характеристики отчета | <ul><li>Часовой пояс: UTC</li><li>Валюта: USD</li></ul> |

</Accordion>

<div id="api-parameters" />

<Accordion title="Параметры API">

Параметры API Protect360:

| Параметр | Описание | Формат | Обязательно |
| --- | --- | --- | --- |
| app\_id (идентификатор приложения) | Идентификатор приложения в том виде, в каком он отображается в AppsFlyer | строка | Да |
| from (от) | Начало диапазона дат:<ul><li>Для установок это дата установки.</li><li>Для внутренних событий приложения это дата события.</li></ul> | YYYY-MM-DD | Да |
| to (по) | Конец диапазона дат:<ul><li>Для установок это дата установки.</li><li>Для внутренних событий приложения это дата события.</li></ul> | YYYY-MM-DD | Да |
| event\_name (название события) | [Опционально для пост-атрибуционного мошенничества с событиями внутри приложения]<br /><br />Отфильтруйте события по типу внутренних событий. Добавьте в отчет только конкретные события. Можно включить одно или несколько событий.<br /><br />Пример использования: `&event_name=af_purchase,af_login` | строка | Нет |
| обнаружить-от | [Опционально для пост-атрибуционных установок]<br /><br />Начало диапазона дат обнаружения мошенничества. (По умолчанию from.) | YYYY-MM-DD | Нет |
| обнаружить-до | [Опционально для пост-атрибуционных установок]<br /><br />Конец диапазона дат обнаружения мошенничества. (По умолчанию to.) | YYYY-MM-DD | Нет |

</Accordion>

<div id="protect360-api-http-return-codes" />

<Accordion title="Коды возврата HTTP для API Protect360">

Коды ошибок и решения:

| Статус | Код | Симптом/сообщение | Решение |
| --- | --- | --- | --- |
| OK | 200 | Пустой файл CSV | `addtional_fields` используется в URI более одного раза |
| OK | 200 | Пустой файл CSV | Убедитесь, что даты начала и окончания имеют формат гггг-мм-дд |
| OK | 200 | Возвращается страница входа в AppsFlyer в формате HTML | В заголовке токена предъявителя нет токена |
| Неверный запрос | 400 | Неверный запрос | <ul><li>Ограничение диапазона дат.<ul><li>Самая ранняя допустимая дата — за 90 дней до текущего дня</li><li>Период не может превышать 60 дней для установок и 90 дней для отчетов по внутренним событиям.</li></ul></li></ul> |
| Не авторизовано | 401 | Не авторизовано | Токен найден, но он недействителен. Убедитесь, что для вашего аккаунта установлен токен версии 2.0. Попросите администратора получить текущий токен с дэшборда. |
| Не найдено | 404 |  | <ul><li>Указана неверная конечная точка</li><li>Убедитесь, что идентификатор приложения правильный.</li><li>Вы не авторизованы для доступа к приложению</li></ul> |

</Accordion>

<div id="impression-capping" />

## Ограничение показов

Если в рекламной сети чрезвычайно высок процент мошеннических показов или кликов, Protect360 блокирует показы или клики рекламной сети в течение 24 часов. Это означает, что любые показы/клики, произошедшие после достижения порогового значения, не регистрируются AppsFlyer и не подлежат атрибуции. Заблокированные показы/клики отображаются на дэшборде Protect360 и в отчетах.

Алгоритм защиты от мошенничества AppsFlyer учитывает различные параметры при обнаружении мошенничества, включая количество показов/кликов, CVR, уровень обнаруженного мошенничества, нормальные колебания активности, отраслевые и географические показатели, а также собственные параметры. Алгоритм динамичен и обновляется ежечасно с учетом меняющихся тенденций.

**Неоднократное срабатывание пороговых значений количества показов или кликов может привести к окончательному удалению партнерской интеграции с платформы AppsFlyer.**

Пороговые значения для ограничения показов:

* Применяются ко всем рекламным сетям одинаково. Это означает, что нет рекламной сети, в которой чрезвычайно высокий уровень мошенничества с показами или кликами не приводил бы к ограничению количества кликов или показов.
* Находятся на уровне приложений/рекламной сети. То есть при анализе мошенничества учитываются все кампании рекламной сети в приложении, а блокировка влияет на отчетность и атрибуцию всех кампаний рекламной сети в приложении (независимо от того, есть ли в аккаунте Protect360).
* Обнуляются после 24-часового цикла, а блокировка действует до конца цикла. Сведения о том, когда начинается и заканчивается цикл, AppsFlyer сохраняет в тайне.
* Невозможно изменить или остановить. Protect360 тщательно настроен и точен в обнаружении мошенничества, и алгоритм нельзя настроить или выключить вручную.
* Этого можно избежать, остановив кампании и издателей с аномальной активностью.

<div id="faq" />

<Accordion title="Вопросы и ответы">

Часто задаваемые вопросы об ограничении показов:

| **В: Каков порог для сети?**<br /><br />**О**: Детали механизма блокировки кликов защищены, чтобы предотвратить попытки обойти ограничения.  Тем не менее, пороговое значение достигается только в том случае, если количество показов/кликов превышает возможное поведение человека. Количество показов, кликов и установок за день даст вам четкое представление о том, есть ли проблема с флудингом из-за одного или нескольких издателей. |
| --- |
| **В: Как разблокировать сеть?**<br /><br />**О**: Сеть может обойти пороговое значение,  остановив кампании и издателей с аномальной активностью. После блокировки сети необходимо дождаться окончания 24-часового цикла, чтобы возобновилась запись кликов. |
| **В: Повлияет ли блокировка на клиентов AppsFlyer без Protect360?**<br /><br />**О**: Да, ограничение будет действовать независимо от того, есть ли у клиента Protect360 или нет. Механизм ограничения защищает всех клиентов от злоупотреблений кликами и показами. |
| **В: Это не мошенничество. Сеть работает с дешевыми источниками, и иногда их качество низкое.**<br /><br />**О**: Низкая эффективность в обычном масштабе, исходящая от неподозрительных источников, не приводит к ограничению количества кликов. Алгоритм определяет эффективность, которая не может быть достигнута человеком. |
| **В: Это мешает нам масштабировать кампании, и мы не хотим, чтобы эти показы/клики блокировались.**<br /><br />**О**: Алгоритм AppsFlyer lky защиты от мошенничества защищает клиентов от экстремальных и явных случаев флудинга. Это не влияет на масштабируемость, так как учитываются показы и клики, не вызванные человеком, где подавляющее большинство блокировок влекут за собой только обязательства. Если у вас есть проблемы, свяжитесь с AppsFlyer для их решения. |
| **В: Это не мошенничество. Возможно, у AppsFlyer есть проблемы с обработкой количества показов/кликов?**<br /><br />**О**: У нас нет проблем с обработкой количества. Мы оказываем поддержку крупнейшим рекламодателям в мире и ежедневно обрабатываем миллиарды данных в реальном времени, включая огромное количество легитимных кликов. В рамках нашего стремления поддерживать масштабный рост с помощью обширных и точных данных мы действуем в интересах наших клиентов и предотвращаем явные случаи клик-флудинга. |
| В: Что делать, если мы ожидаем значительного увеличения трафика и количества показов/кликов (например, за счет новых кампаний)? Что можно сделать, чтобы избежать блокировки?<br /><br />О:**Алгоритм динамичен и обновляется ежечасно с учетом различных тенденций. Он достаточно сложен, чтобы выдерживать резкие скачки и не срабатывает из-за нормальных колебаний активности, включая внезапное и значительное увеличение объема. Тем не менее, партнеры могут использовать свои данные о показах и кликах и отчеты для выявления подозрительных источников и остановки этих кампаний.** |
| В: Как проверить проблемный трафик и повысить эффективность кампании?<br /><br />О:**Партнеры могут использовать свои данные о показах и кликах и отчеты для выявления подозрительных источников и остановки этих кампаний. Партнеры также могут видеть заблокированные показы и клики на дэшбордах Protect360/ProtectLite в специальных столбцах, если они получили от рекламодателя необходимое разрешение на просмотр данных о мошенничестве на дэшборде.** |

</Accordion>

<div id="click-signing" />

### Подпись кликов

Рекламные сети могут добавлять <Anchor target="_blank" href="/partners/ru/docs/click-signing-for-ad-networks">подписи</Anchor> HMAC-SHA256 к своим кликам.

Подписи позволяют AppsFlyer проверять клики и следить за тем, чтобы информация о кликах не была изменена мошенниками.

* Подтвержденные клики регистрируются и атрибутируются к рекламной сети
* Недействительные клики отклоняются и:
  * Обобщаются в отчетах Protect360, доступных рекламной сети (не рекламодателям).
  * Не влияют на коэффициент конверсии или пороговое значение количества кликов в рекламной сети.

<div data-zendesk-anchors="overview=%D0%BE%D0%B1%D0%B7%D0%BE%D1%80 h_01HGSXTKYQB4Q1QQX4ZQS60AAJ=%D0%BE%D0%B1%D0%B7%D0%BE%D1%80 h_01HGSXTKYQN42EEMPSZMWVAMWD=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 dashboard-view=%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B0 h_01HGSXTKYQPQP72R2VJB68ZDRZ=%D0%BF%D1%80%D0%B5%D0%B4%D1%81%D1%82%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4%D0%B0 rawdata-reports=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%8B-%D0%BF%D0%BE-%D1%81%D1%8B%D1%80%D1%8B%D0%BC-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC h_01HGSXTKYQWRZECN905RGSEQ42=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%8B-%D0%BF%D0%BE-%D1%81%D1%8B%D1%80%D1%8B%D0%BC-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC protect360-ad-network-reporting-api=api-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BF%D0%BE-protect360-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 h_01HGSXTKYQ9388SCQTT2MX59Q9=api-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BF%D0%BE-protect360-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 protect360-api-reports=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%8B-protect360-%D0%BF%D0%BE-api h_01HGSXTKYQXZN2DMNZ09HE7355=%D0%BE%D1%82%D1%87%D0%B5%D1%82%D1%8B-protect360-%D0%BF%D0%BE-api procedure-for-ad-networks-to-get-protect360-reports-by-download=%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D0%B0-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BE%D0%B2-protect360-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D0%BC%D0%B8-%D1%81%D0%B5%D1%82%D1%8F%D0%BC%D0%B8-%D0%BF%D1%83%D1%82%D0%B5%D0%BC-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8 h_01HGSXTKYQ913MF0G38B23NYBG=%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D0%B0-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BE%D0%B2-protect360-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D0%BC%D0%B8-%D1%81%D0%B5%D1%82%D1%8F%D0%BC%D0%B8-%D0%BF%D1%83%D1%82%D0%B5%D0%BC-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8 curl-examples=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-curl h_01HGSXTKYQX3VN5NRMNQWW4AE4=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-curl h_01HGSXTKYQQBJTM4ZMMQZ0VZNH=installs-blocked_installs_report h_01HGSXTKYQ5KTCD7K63DSVS6E2=postattribution-installs-detection h_01HGSXTKYQ6MA96W8E6R2SXBS5=inapp-event-blocked_in_app_events_report h_01HGSXTKYQMMC0WNWP56Q9J0ZS=postattribution-inapp-events-fraud-fraud_post_inapps h_01HGSXTKYQEG0JXJHS7QBAEBCA=clicks-blockedclicks_report protect360-ad-network-api-reference-guide=%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%BE%D0%B5-%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-api-protect360-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 h_01HGSXTKYQJRE1Y9C5RSCANWT2=%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%BE%D1%87%D0%BD%D0%BE%D0%B5-%D1%80%D1%83%D0%BA%D0%BE%D0%B2%D0%BE%D0%B4%D1%81%D1%82%D0%B2%D0%BE-%D0%BF%D0%BE-api-protect360-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 h_01HGSXTKYQE24FAPYHHMFP0B3X=api-basics h_01HGSXTKYRFSZRPHNPDHNREDH2=api-parameters h_01HGSXTKYRGSQ230NVN06SP6DG=protect360-api-http-return-codes impression-and-click-capping=%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE%D0%BA%D0%B0%D0%B7%D0%BE%D0%B2 h_01HGSXTKYRN6TP3KDYX5YZJV7N=%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE%D0%BA%D0%B0%D0%B7%D0%BE%D0%B2 h_01HGSXTKYR8BK5A2J6TJECMKZA=faq click-signing=%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%8C-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2 h_01HGSXTKYR915V6E4NWGWR61PG=%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D1%8C-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2" />
