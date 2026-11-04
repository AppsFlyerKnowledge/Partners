---
title: Использование макросов в постбэках для рекламных сетей
metadata:
  keywords:
    - postbacks
    - Advertisers
    - Ad Networks
    - macros
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2016-01-11T14:41:40Z'
  edited_at: '2026-08-18T00:39:37Z'
  id: 207273946
  locale: ru
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ru/articles/207273946
---
> **Краткий обзор:** Как рекламная сеть при интеграции с AppsFlyer вы можете определять контент постбэков и конечные точки, на которые AppsFlyer отправляет эти постбэки. В постбэках содержится информация об интеракциях пользователей приложения, например, об установках, событиях в приложении, повторных вовлечениях и т. п.

Руководства по постбэкам для интегрированных партнеров:

* <Anchor target="_blank" href="/partners/ru/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Расширенные настройки конфиденциальности</Anchor>
* <Anchor target="_blank" href="/partners/ru/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/partners/ru/docs/rejected-attribution-postbacks-to-integrated-partners">Отклоненные постбэки по атрибуции</Anchor>

<div id="postbacks-for-ad-networks" />

## Постбэки для рекламных сетей

* **Настройка постбэков:** чтобы запросить изменения в настройках постбэков, используйте <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor> или обратитесь к менеджеру AppsFlyer по работе с партнерами.
* **Типы постбэков**: доступны постбэки по установкам и внутренним событиям, а также по установкам и внутренним событиям, заблокированным как мошеннические в Protect360 или из-за нарушения правил проверки таргетинга.

<div id="postback-data-sources" />

### Источники данных постбэков

| Источник | Описание |
| --- | --- |
| <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters">Параметры ссылки атрибуции</Anchor> | Параметры, предоставляемые партнером вместе с URL-адресами для учета кликов и показов объявления<br /><br />Пример: параметр click ID в ссылке атрибуции — "&click\_id=CLICK\_ID" |
| Идентификаторы партнеров в AppsFlyer | Уникальные идентификаторы, предоставляемые рекламодателю партнером<br /><br />Например, ID приложения, ID аккаунта, ID пользователя, ID сети. |
| Информация, полученная из SDK | Информация, полученная от устройства с помощью SDK AppsFlyer.<br /><br />Например: используя макрос «&IDFA=(idfa)» в постбэке, можно получить идентификаторы устройств iOS |
| Получено платформой AppsFlyer | Информация, полученная платформой AppsFlyer. |
| Protect360 и правила проверки | Информация об установках, которые признаны мошенническими, и об установках, нарушающих правила таргетинга кампании, а также связанные с ними события в приложении. |

<div id="postback-macros" />

## Макросы в постбэках

При включении в постбэк макросы заменяются соответствующими пользовательскими данными. Например, для получения IP-адресов пользователей, устанавливающих приложение, нужно добавить в структуру постбэка макрос `country_code=(ip)`. Поддерживаемые макросы перечислены в следующей таблице:

Столбцы в таблице ниже имеют следующее значение:

* **Источник:** откуда пришли данные.
  * Link: Ссылки атрибуции:
  * SDK: SDK AppsFlyer, встроенный в приложение или межсерверный API.
  * AF: После обработки AppsFlyer.
* **Отправлять все**: Если этот столбец содержит значение «Да», вы можете получать данные об установках и событиях, атрибутированных другим сетям или органических. (То есть атрибутированных не вам.)
* **[Основа] Макросы для всех постбэков**: макросы, относящиеся к постбэкам об установках, внутренних событиях и отклоненных событиях.
* **[Дополнительно]** для внутренних событий и отклоненных событий, как указано в столбце (отклонено, внутренние)

<div id="macrosinstalls-in-app-events-and-rejected-events" />

### Макросы: установки, внутренние события приложения и отклоненные события

| Макрос в постбэке (название) | Источник | Отправить все | Описание | [Основа] Макросы для всех постбэков | [Дополнительно] Внутренние и отклоненные события |
| --- | --- | --- | --- | --- | --- |
| <span id="advertising_id"></span>рекламный\_идентификатор | SDK (пакет средств разработки ПО) | Да | Сбрасываемый пользователем идентификатор устройства, также известный как GAID. Другой вариант: (sha1-advertiserId) | Да |  |
| <span id="af_ad"></span>af\_ad | Ссылка | Нет | Название рекламы (<Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#уровни-детализации-данных">см. подробнее</Anchor>), предоставленное рекламодателем/издателем | Да | Да |
| <span id="af_ad_id"></span>af\_ad\_id | Ссылка | Нет | Предоставлено рекламодателем/издателем | Да | Да |
| <span id="af_ad_type"></span>af\_ad\_type | Ссылка | Нет | Используйте следующее соглашение об именовании:<ul><li>**текст:** рекламный блок, содержащий только текст, например результат поиска</li><li>**баннер:** базовый формат, который отображается в верхней или нижней части экрана устройства</li><li>**межстраничное объявление:** полностраничное объявление, которое появляется во время перерывов в текущем опыте</li><li>**видео:** стандартное видео, без вознаграждения</li><li>**rewarded\_video:** рекламный блок, предлагающий награды в приложении в обмен на просмотр видео</li><li>**playable:** рекламный блок, содержащий интерактивный предварительный просмотр приложения</li><li>**sponsored\_content:** ссылка, включенная в фрагмент заказного контента, например, в рекламную статью</li><li>**аудио:** аудиореклама</li></ul> | Да | Да |
| <span id="af_adset"></span>af\_adset | Ссылка | Нет | <ul><li>Предоставляется рекламодателем/издателем.</li><li>Адсет — это промежуточный уровень в иерархии между кампанией и рекламным объявлением. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#уровни-детализации-данных">Подробнее</Anchor></li></ul> | Да | Да |
| <span id="af_adset_id"></span>af\_adset\_id | Ссылка | Нет | Предоставлено рекламодателем/издателем | Да | Да |
| <span id="af_c_id"></span>af\_c\_id | Ссылка | Нет | Предоставлено рекламодателем/издателем | Да | Да |
| <span id="af_siteid"></span>af\_siteid | Ссылка | Нет | <ul><li>Уникальный идентификатор, определяющий издателя, показывающего рекламу. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#site-id-parameter">Узнать больше</Anchor></li></ul> | Да | Да |
| <span id="af_subsite_id"></span>af\_subsite\_id | Ссылка | Нет | <ul><li>ID подсети/издателя.</li><li>Если в дополнение к основному издателю (ID сайта) существует субиздатель, или вы хотите включить дополнительную информацию, такую как тип/размещение рекламы в приложении, например баннер, межстраничная реклама, видео и т.д., используйте af\_sub\_siteid. Например: af\_sub\_siteid =ABCD\_4567</li></ul> | Да | Да |
| <span id="af_validated"></span>af\_validated | AF | Да | Показывает, прошла ли покупка успешную валидацию. Возможные значения: true или false. | Да |  |
| <span id="af_validation_type"></span>af\_validation\_type | AF | Да | Указывает тип проведённой валидации. Возможные значения: roi360\_purchase, roi360\_subscription, Basic. | Да |  |
| <span id="app_id"></span>app\_id (идентификатор приложения) | SDK (пакет средств разработки ПО) | Да | Идентификатор приложения, сообщенный приложением | Да |  |
| <span id="app_name"></span>имя\_приложения | SDK (пакет средств разработки ПО) | Да | Имя приложения, заданное рекламодателем | Да |  |
| <span id="app_version"></span>версия\_приложения | SDK (пакет средств разработки ПО) | Да | Имя версии приложения, заданное разработчиком в коде приложения. | Да |  |
| <span id="appsflyer_id"></span>appsflyer\_id | SDK (пакет средств разработки ПО) | Да | Уникальный идентификатор AppsFlyer, зафиксированный при конверсии. | Да |  |
| <span id="att01"></span>att-0-1 | SDK (пакет средств разработки ПО) | Да | Возможные значения:<ul><li>1: Статус ATT authorized или af\_authorized.</li><li>0: Любой другой статус ATT.</li></ul> | Да |  |
| <span id="attstatus"></span>att-status | SDK (пакет средств разработки ПО) | Да | <Anchor target="_blank" href="/marketers/ru/docs/att-implications-ios-14-and-deprecation-of-lat#значения-att">Статус ATT</Anchor> от iOS. Напр., authorized, not\_determined.<br /><br />В некоторых случаях значение отсутствует и возвращается "". | Да |  |
| <span id="attributed_touch_type"></span>attributed\_touch\_type (атрибутированный тип взаимодействия) | SDK (пакет средств разработки ПО) | Нет | Возможные значения: click, impression, TV, pre-install (клик, показ, ТВ, предустановка) | Да |  |
| <span id="blocked_reason"></span>заблокированная\_причина | AF | Нет | Причина блокировки: мошенничество / нарушение правил проверки | Нет | Отклонено |
| <span id="blocked_reason_value"></span>заблокированное\_значение\_причины | AF | Нет | Значение причины блокировки из-за мошенничества / нарушения правил проверки | Нет | Отклонено |
| <span id="blocked_sub_reason"></span>заблокированная\_подпричина | AF | Нет | Частная причина блокировки из-за мошенничества / нарушения правил проверки | Нет | Отклонено |
| <span id="bundle_id"></span>Авторизовано | SDK (пакет средств разработки ПО) | Да | iOS: Идентификация для сопоставления одного Приложения или группы Приложений в iOS (см. идентификатор пакета разработчика Apple) Android: Название приложения | Да |  |
| <span id="c"></span>c | Ссылка | Нет | Предоставляется рекламодателем/издателем. Имя кампании, превышающее 100 символов, отображается на панели управления как "c\_name\_exceeded\_max\_length". | Да | Да |
| <span id="country_code"></span>код\_страны | AF | Да | Код страны согласно ISO 3166 (alpha-2) Пример: США, Китай. | Да |  |
| <span id="event_name"></span>event\_name (название события) | SDK (пакет средств разработки ПО) | Да | Имя, присвоенное событию | Нет | В приложении |
| <span id="event_revenue_currency"></span>event\_revenue | SDK (пакет средств разработки ПО) | Да | Значение события, определенное SDK с помощью event\_revenue\_currency или выбранной вами валюты. | Нет | В приложении |
| {"event_revenue"}  <br />{"_"}валюта | SDK (пакет средств разработки ПО) | Да | Код валюты дохода от события, переданный для события, или выбранной вами валюты. | Нет | В приложении |
| <span id="event_revenue_usd"></span>event\_revenue\_USD | AF | Да | Значение стоимости события в USD. | Нет | В приложении |
| <span id="event_time"></span>время\_события | SDK (пакет средств разработки ПО) | Да | Время события | Нет | В приложении |
| <span id="event_value"></span>event\_value | SDK (пакет средств разработки ПО) | Да | Внутреннее событие приложения содержит атрибуты со значениями, которые можно целиком включать в постбэки в формате JSON и кодировать как URL-адрес, используя макрос (encode). и кодировать как URL-адрес, используя макрос (encode). | Нет | В приложении |
| <span id="idfa"></span>IDFA | SDK (пакет средств разработки ПО) | Да | Идентификатор рекламного объявления, который может быть сброшен пользователем, на устройствах iOS. Также доступен как (sha1-idfa) | Да |  |
| <span id="idfv"></span>IDFV | SDK (пакет средств разработки ПО) | Да | Уникальный идентификатор для каждого пользователя и поставщика на устройствах iOS | Да |  |
| <span id="imei"></span>imei | SDK (пакет средств разработки ПО) | Да | Уникальный номер, используемый для идентификации мобильных телефонов | Да |  |
| <span id="install_time"></span>время\_установки | SDK (пакет средств разработки ПО) | Да | Метка времени установки | Да |  |
| <span id="install_unix_ts"></span>install\_unix\_ts | SDK (пакет средств разработки ПО) | Да | Метка времени установки в формате unix | Да |  |
| <span id="is_attributed"></span>is\_attributed | AF | Да | Флаг для указания, что установка или событие атрибутируются данному медиа-источнику | Да |  |
| <span id="is_contrib"></span>is\_contrib | AF | Да | Показывает, была ли рекламная сеть среди трёх основных сетей, поспособствовавших установке.<ul><li>Если рекламная сеть не получила атрибуцию, но находится в тройке лучших, `is_contrib=1`.</li><li>Если рекламная сеть получила атрибуцию, `is_contrib=0`.</li><li>Если рекламная сеть не входит в тройку лучших, `is_contrib=0`.</li></ul> | Да |  |
| <span id="is_lat"></span>is\_lat | SDK (пакет средств разработки ПО) | Да | Ограничение отслеживания рекламы (LAT): iOS: Начиная с iOS 14 LAT устарело в Apple. Определите статус конфиденциальности пользователя с помощью ATT. В этом случае игнорируйте is\_lat. До iOS 14, если true, IDFA недоступен и установлен в 0. Android: Если true, пользователь отказался от рекламы на основе интересов. Это не мешает сбору GAID. | Да |  |
| <span id="is_organic"></span>is\_organic | AF | Да | Если постбэк установки отправляется для всех медиа-источников, включая органические, то рекламная сеть получит информацию о том, была ли установка органической или неорганической. | Только установки |  |
| <span id="is_primary_attribution"></span>is\_primary\_attribution | AF | Да | Если установлено значение false, см. is\_retargeting. | Нет | В приложении |
| <span id="is-reinstall"></span>is\_reinstall | AF | Нет | Если установлено значение true, событие указывается в отчетности как <Anchor target="_blank" href="/marketers/ru/docs/measure-reinstalls">переустановка</Anchor>. |  |  |
| <span id="is_retargeting"></span>is\_retargeting | Ссылка | Да | Используйте вместе с is\_primary\_attribution. Подробнее о <Anchor target="_blank" href="/marketers/ru/docs/resolve-retargeting-double-attribution">двойной атрибуции событий ретаргетинга.</Anchor><br /><br />Если установлено значение true (1), событие регистрируется как часть кампании ретаргетинга, а медиа-источник является медиа-источником ретаргетинга.<br /><br />Если установлено значение false (0) и для is\_primary\_attribution тоже значение false, то событие является частью кампании ретаргетинга, но медиа-источник будет медиа-источником атрибуции пользователя. | Да |  |
| <span id="language"></span>язык | SDK (пакет средств разработки ПО) | Да | Язык (местный), сообщается устройством, устанавливается ОС устройства. | Да |  |
| <span id="oaid"></span>oaid | SDK (пакет средств разработки ПО) | Да | Сбросный идентификатор на некоторых устройствах Android, обычно альтернатива GAID | Нет |  |
| <span id="partner_event_id"></span>partner\_event\_id | AF | Да | Имя/идентификатор соответствующего события на платформе партнера. | Да | В приложении |
| <span id="platform"></span>platform | SDK (пакет средств разработки ПО) | Нет | Платформа устройства: iOS, Android или Windows Mobile | Постбэк: |  |
| <span id="retargeting-conversion-type"></span>тип\_конверсии\_ретаргетинга | AF | Нет | Флаг для указания, является ли событие реатрибуцией или повторным вовлечением | Только для ретаргетинга |  |

<div id="in-app-event-only-macros" />

### Макросы, применимые только для внутренних событий приложения

Приведенные ниже примеры относятся к постбэкам по внутренним событиям, доступным партнерам.

<div id="example" />

> 📄 **Пример**
>
> Шаблон постбэка события «&event=(event)&json=(encode)» был преобразован в следующий постбэк для конкретного события af\_purchase:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> После преобразования этот постбэк в формате JSON будет содержать следующие параметры:
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

<div id="encoded-values" />

#### **Кодирование значений**

В некоторых случаях в постбэки, кроме букв и цифр, могут включаться нестандартные символы. Чтобы правильно передать такие значения через постбэки, AppsFlyer использует для нестандартных символов URL-кодирование.

Чтобы декодировать и закодировать постбэк, используйте <Anchor target="_blank" href="https://www.urldecoder.org/">веб-службу</Anchor>.

<div id="sample-postbacks" />

## Примеры постбэков

<div id="general-install-postback-examples" />

### Типовые примеры постбэков для установок

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)
&advertising_id=(advertiser_id)&android_id=(android_id)
&install_time=(install_unix_ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?&site_id=(publisher_id)&
device_ip=(ip)&;idfa=(idfa)&install_time=(install_unix_ts)
```

</Tab>
</Tabs>

<div id="general-in-app-event-postback-examples" />

### Типовые примеры постбэков для внутренних событий приложения

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)&
device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android_id)&
install_time=(install_unix_ts)&event_name=(event_name)&currency=(currency)&
json=(event_value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?clickid=(clickid)&site_id=(publisher_id)&
device_ip=(ip)&idfa=(idfa)&install_time=(install_unix_ts)
&event_name=(event_name)&currency=(currency)&json=(event_value)
```

</Tab>
</Tabs>

<div id="in-app-event-postback-example" />

### Пример постбэка по внутреннему событию

Параметры события:

* Имя события: af\_revenue
* Доход от события 120,00
* Валюта события: USD
* Значение события: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

Постбэк:

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-ad-networks=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 01JHFZWJT74GNA6J5MYMQBGDWX=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 postback-data-sources=%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 01JHFZWJT978TTXB7FQ6AVG1ZS=%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B8-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 postback-macros=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D0%B2-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0%D1%85 01JHFZWJTTP66NHZRG0RQAY3W8=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D0%B2-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0%D1%85 macros%E2%80%94installs-inapp-events-and-rejected-events=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%B5-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B8-%D0%BE%D1%82%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F 01JHFZWJTXD2K4RJ8RDWXKSYDD=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D0%B5-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B8-%D0%BE%D1%82%D0%BA%D0%BB%D0%BE%D0%BD%D0%B5%D0%BD%D0%BD%D1%8B%D0%B5-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F inapp-event-only-macros=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8%D0%BC%D1%8B%D0%B5-%D1%82%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JHFZWK3FQ5HCX9NDEKT6SPT1=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8%D0%BC%D1%8B%D0%B5-%D1%82%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JHFZWK3F2E31WE5N1G0T0ZHA=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80 encoded-values=%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9 01JHFZWK3GM9XRS2GC4SNXFVD7=%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9 sample-postbacks=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 01JHFZWK3GJSA8RF4AMKVM4XD4=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 general-install-postback-examples=%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA 01JHFZWK3HD1NFJJW1Y8HGVPX2=%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA general-inapp-event-postback-examples=%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JHFZWK3JW0D1GZ739FV0EZWG=%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F inapp-event-postback-example=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%BF%D0%BE-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B5%D0%BC%D1%83-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E 01JHFZWK3JT8GM7BEM3RXCMXV5=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%BF%D0%BE-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B5%D0%BC%D1%83-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E" />
