---
title: Макросы постбэков для партнеров по аналитике
metadata:
  keywords:
    - Advertisers
    - Ad Networks
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
  created_at: '2021-01-04T04:44:40Z'
  edited_at: '2026-09-02T00:37:03Z'
  id: 360016751637
  locale: ru
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ru/articles/360016751637
---
> **At a glance:** Используйте макросы в постбэках, отправляемых партнерам по аналитике, чтобы получать релевантные данные атрибуции.

## Постбэки для партнеров по аналитике

Партнеры по аналитике могут определять содержимое постбэков и конечные точки, на которые AppsFlyer отправляет эти постбэки, в рамках своей интеграции с AppsFlyer. В постбэках содержится информация об интеракциях пользователей приложения, например, об установках, событиях в приложении, повторных вовлечениях и т. п.

* **Настройка постбэков:** Чтобы запросить изменения в настройках постбэков, используйте <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощника партнера</Anchor>, чтобы открыть тикет, или обратитесь к менеджеру AppsFlyer по развитию партнеров.
* **Типы постбэков**: постбэки доступны для установок и событий в приложении.

## Макросы в постбэках

При включении в постбэк макросы заменяются соответствующими пользовательскими данными. Например, для получения IP-адресов пользователей, устанавливающих приложение, нужно добавить в структуру постбэка макрос country\_code=(ip). Поддерживаемые макросы перечислены в следующей таблице:

* Источник: откуда пришли данные:
  * SDK: SDK AppsFlyer, встроенный в приложение или межсерверный API.
  * AF: После обработки AppsFlyer.
* **[Base]** **Макросы для всех постбэков**: макросы, относящиеся к установкам и событиям в приложении.
* **[Необязательно]** для событий в приложении, как указано в столбце.

#### Макросы — установки и события в приложении

| Макрос в постбэке (название) | Информация на дэшборде | Description(Описание) | [Основа] Макросы для всех постбэков | [Необязательно] События в приложении |
| --- | --- | --- | --- | --- |
| рекламный\_идентификатор | SDK (пакет средств разработки ПО) | Идентификатор устройства, который пользователь может сбросить, он же GAID. Другой вариант: (sha1-advertiserId) | Да |  |
| имя\_события | SDK (пакет средств разработки ПО) | Имя, присвоенное событию |  | Да |
| event\_revenue\_USD | AF | Значение стоимости события в USD. |  | Да |
| event\_revenue | SDK (пакет средств разработки ПО) | Значение события, определенное SDK с помощью event\_revenue\_currency или выбранной вами валюты. |  | Да |
| event\_currency | SDK (пакет средств разработки ПО) | Код валюты дохода от события, переданный в событии, или код выбранной вами валюты. |  | Да |
| время\_события | SDK (пакет средств разработки ПО) | Event Time (Время события) |  | Да |
| event\_value | SDK (пакет средств разработки ПО) | Внутреннее событие приложения содержит атрибуты со значениями, которые можно целиком включать в постбэки в формате JSON и кодировать как URL-адрес, используя макрос (encode). и кодировать как URL-адрес, используя макрос (encode). |  | Да |
| partner\_event\_id | AF | Имя/идентификатор соответствующего события на платформе партнера. |  | Да |
| имя\_приложения | SDK (пакет средств разработки ПО) | Имя приложения, заданное рекламодателем | Да |  |
| appsflyer\_id | SDK (пакет средств разработки ПО) | Уникальный идентификатор AppsFlyer, зафиксированный при конверсии. | Да |  |
| attributed\_touch\_type (атрибутированный тип взаимодействия) | AF | Флаг для указания, что атрибуция осуществлялась по просмотру (1 = показ, 0 = клик) | Да |  |
| код\_страны | AF | Код страны согласно ISO 3166 (alpha-2) Пример: США, Китай. | Да |  |
| IDFA | SDK (пакет средств разработки ПО) | Идентификатор рекламного объявления, который может быть сброшен пользователем, на устройствах iOS. Также доступен как (sha1-idfa) | Да |  |
| IDFV | SDK (пакет средств разработки ПО) | Уникальный идентификатор для каждого пользователя и поставщика на устройствах iOS | Да |  |
| время\_установки | SDK (пакет средств разработки ПО) | Метка времени установки | Да |  |
| install\_unix\_ts | SDK (пакет средств разработки ПО) | Метка времени установки в формате unix | Да |  |
| is\_lat | SDK (пакет средств разработки ПО) | Ограничение отслеживания рекламы (LAT): iOS: Начиная с iOS 14 LAT устарело в Apple. Определите статус конфиденциальности пользователя с помощью ATT. В этом случае игнорируйте is\_lat. До версии iOS 14, если установлено значение true, то IDFA не доступен и отображается 0. Android: Если true, пользователь отказался от рекламы на основе интересов. Это не мешает сбору GAID. | Да |  |
| язык | SDK (пакет средств разработки ПО) | Язык (местный), сообщается устройством, устанавливается ОС устройства. | Да |  |
| app\_id (идентификатор приложения) | SDK (пакет средств разработки ПО) | Уникальный идентификатор приложения в AppsFlyer | Да |  |
| app-version-name | SDK (пакет средств разработки ПО) | Версия приложения, установленная разработчиком приложения в коде приложения | Да |  |
| attributed\_touch time | AF | Время взаимодействия, которому AppsFlyer присвоил атрибуцию. | Да |  |
| тип\_устройства | SDK (пакет средств разработки ПО) | Доступно только в <Anchor target="_blank" href="/marketers/ru/docs/about-data-locker-advanced-reports">расширенных отчётах</Anchor>. Пример: SM-GM284 или iPhone7 | Да |  |
| ip | AF | IP-адрес устройства пользователя, сообщающего о событии | Да |  |
| Местоположение устройства | AF | Тип метода атрибуции. Например, srn, id\_matching, probabilistic | Да |  |
| os\_version | SDK (пакет средств разработки ПО) | Версия операционной системы устройства | Да |  |
| user\_agent | SDK (пакет средств разработки ПО) | Агент пользователя URL-адреса | Да |  |
| Информация об устройстве | SDK (пакет средств разработки ПО) | Если true, подключение было по Wi-Fi в момент конверсии | Да |  |
| oaid | SDK (пакет средств разработки ПО) | Сбросный идентификатор на некоторых устройствах Android, обычно альтернатива GAID | Да |  |
| platform | SDK (пакет средств разработки ПО) | Платформа устройства: iOS, Android или Windows Mobile | Да |  |
| тип\_конверсии\_ретаргетинга | SDK (пакет средств разработки ПО) | Флаг для указания, является ли событие реатрибуцией или повторным вовлечением | Да |  |
| pid | AF | Рекламная сеть, которой атрибутируется установка или событие в приложении | Да |  |
| af\_ad | Атрибуция PBA | Название рекламы (<Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#уровни-детализации-данных">см. подробнее</Anchor>), предоставленное рекламодателем/издателем | Да | Да |
| af\_ad\_id | Атрибуция PBA | Предоставляется рекламодателем или издателем | Да | Да |
| af\_adset | Атрибуция PBA | <ul><li>Предоставляется рекламодателем/издателем.</li><li>Адсет — это промежуточный уровень в иерархии между кампанией и рекламным объявлением. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#уровни-детализации-данных">Подробнее</Anchor></li></ul> | Да | Да |
| af\_adset\_id | Атрибуция PBA | Предоставляется рекламодателем или издателем | Да | Да |
| c | Атрибуция PBA | Предоставляется рекламодателем/издателем. Имя кампании, превышающее 100 символов, отображается на панели управления как "c\_name\_exceeded\_max\_length". | Да | Да |
| af\_c\_id | Атрибуция PBA | Предоставляется рекламодателем или издателем | Да | Да |
| af\_siteid | Атрибуция PBA | <ul><li>Уникальный идентификатор, определяющий издателя, показывающего рекламу. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#site-id-parameter">Узнать больше</Anchor></li></ul> | Да | Да |
| af\_subsite\_id | Атрибуция PBA | <ul><li>ID подсети/издателя.</li><li>Если в дополнение к основному издателю (ID сайта) существует субиздатель, или вы хотите включить дополнительную информацию, такую как тип/размещение рекламы в приложении, например баннер, межстраничная реклама, видео и т.д., используйте af\_sub\_siteid. Например: af\_sub\_siteid =ABCD\_4567</li></ul> | Да | Да |
| af\_ad\_type | Атрибуция PBA | Используйте следующее соглашение об именовании:<ul><li>**text:** рекламный блок, содержащий только текст, например результат поиска</li><li>**banner:** базовый формат, который отображается в верхней или нижней части экрана устройства</li><li>**interstitial:** полностраничное объявление, которое появляется во время перерывов в текущем опыте</li><li>**video:** стандартное видео без вознаграждения</li><li>**rewarded\_video:** рекламный блок, предлагающий награды в приложении в обмен на просмотр видео</li><li>**playable:** рекламный блок, содержащий интерактивный предварительный просмотр работы приложения</li><li>**sponsored\_content:** ссылка, включенная в спонсируемый контент, например в рекламную статью</li><li>**аудио:** аудиореклама</li></ul> | Да | Да |

## Макросы, применимые только для внутренних событий приложения

Приведенные ниже примеры относятся к постбэкам по внутренним событиям, доступным партнерам.

> 📘 **Note**
>
> **Например**
>
> Шаблон постбэка события `&event=(event)&json=(encode)` был преобразован в следующий постбэк для конкретного события af\_purchase:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> Декодированное значение JSON этого постбэка: `{"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

### Кодирование значений

В некоторых случаях в постбэки, кроме букв и цифр, могут включаться нестандартные символы. Чтобы правильно передать эти значения через постбэки, AppsFlyer выполняет URL-кодирование не буквенно-цифровых значений.  
Чтобы декодировать или закодировать постбэк, используйте [веб-службу кодирования](https://www.urldecoder.org/).

## Примеры постбэков

### Типовые примеры постбэков для установок

<Tabs>
<Tab title="Android iOS">

```http
http://YourCompanyDomain.com?pid=(media_source)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)
```

</Tab>

<Tab title="adjusted.png">

```http
http://YourCompanyDomain.com?pid=(media source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)
```

</Tab>
</Tabs>

### Типовые примеры постбэков для внутренних событий приложения

<Tabs>
<Tab title="Android iOS">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>

<Tab title="/marketers/ru/docs/set-up-multi-store-android-attribution">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>
</Tabs>

## Пример постбэка по внутреннему событию

**Параметры события:**

* Имя события: af\_revenue
* Доход от события 120,00
* Валюта события: USD
* Значение события: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

**Постбэк:**

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&android_id=9aaeecc4455xxxxx&install_time=1451923560&event_name=af_purchase&currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-analytics-partners=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D0%BE%D0%B2-%D0%BF%D0%BE-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B5 01JH2HWTN05T8S3P4W6CKVA7K4=%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B8-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D0%BE%D0%B2-%D0%BF%D0%BE-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B5 postback-macros=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D0%B2-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0%D1%85 01JH2HWTN52E8CVVGTQWK3QXW6=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D0%B2-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0%D1%85 macros%E2%80%94installs-and-inapp-events=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B--%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8-%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 01JH2HWTN7XY6B55TED4NT2KRR=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B--%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BA%D0%B8-%D0%B8-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8F-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 inapp-event-only-macros=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8%D0%BC%D1%8B%D0%B5-%D1%82%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JH2HWTVN8880HZSF6V6XZ7EF=%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81%D1%8B-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B8%D0%BC%D1%8B%D0%B5-%D1%82%D0%BE%D0%BB%D1%8C%D0%BA%D0%BE-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F encoded-values=%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9 01JH2HWTVNARNYV0M9AKHQ0NDA=%D0%BA%D0%BE%D0%B4%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9 sample-postbacks=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 01JH2HWTVNQT0NPJ7SG9424MTQ=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 general-install-postback-examples=%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA 01JH2HWTVN4DDQ6F70WP3XE19D=%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA general-inapp-event-postback-examples=%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F 01JH2HWTVN2MH2SB6W34DH2MF7=%D1%82%D0%B8%D0%BF%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B8%D1%85-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F inapp-event-postback-example=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%BF%D0%BE-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B5%D0%BC%D1%83-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E 01JH2HWTVP50J5WV11DZR3RSTM=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%BF%D0%BE-%D0%B2%D0%BD%D1%83%D1%82%D1%80%D0%B5%D0%BD%D0%BD%D0%B5%D0%BC%D1%83-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D1%8E" />
