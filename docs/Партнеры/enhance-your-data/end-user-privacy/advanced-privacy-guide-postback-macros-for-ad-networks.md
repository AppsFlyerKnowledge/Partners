---
title: >-
  Руководство по режиму расширенной конфиденциальности и макросы в постбэках для
  рекламных сетей
metadata:
  keywords:
    - Ad Networks
    - Partners
    - ios14
    - SKAD
    - Advanced Privacy
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-07-27T07:09:37Z'
  edited_at: '2026-08-19T00:37:30Z'
  id: 360011316197
  locale: ru
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/ru/articles/360011316197
---
> **Краткий обзор.** Обмен данными с партнерами в режиме расширенной конфиденциальности. Инструкции для рекламных сетей по настройке постбэков в режиме расширенной конфиденциальности. Внимание! Эта статья не относится к постбэкам SKAdNetwork и не предназначена для рекламодателей.

> 📄 **Новости о режиме расширенной конфиденциальности для рекламных сетей**
>
> Описанный в этой статье механизм постбэков в режиме расширенной конфиденциальности работает при соблюдении всех следующих условий:
>
> * Устройство пользователя под управлением iOS 14.5+
> * Режим расширенной конфиденциальности включен

![AdvancedPrivacy.png](https://files.readme.io/2a80740637c1003e03bc169df274bf0fa6240ee850c7fd6e967c4abea234e0d1-360018213598.png)

Основные темы статьи:

* Влияние обмена данными в режиме расширенной конфиденциальности на партнеров.
* Требования к [URL-адресу клика](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements), пригодному для атрибуции.
* Настройка [постбэков](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification) в режиме расширенной конфиденциальности на дэшборде AppsFlyer.
* Разница между [режимом расширенной конфиденциальности и SKAdNetwork.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#ap-vs-skadnetwork)

## Принципы обмена данными в режиме расширенной конфиденциальности для рекламных сетей

Начиная с iOS 14.5+, фреймворк AppsFlyer <Anchor target="_blank" href="/marketers/ru/docs/apply-aggregated-advanced-privacy-framework">Aggregated Advanced Privacy</Anchor> (AAP) дает возможность рекламодателям контролировать доступность данных атрибуции уровня пользователя, предоставляемых через платформу AppsFlyer.

В контексте рекламных сетей, фреймворк AAP реализуется с использованием режима расширенной конфиденциальности (Advanced Privacy, AP). Термины режим расширенной конфиденциальности, Advanced Privacy и AP используются в этой статье как синонимы.

AP не влияет на доступность агрегированных данных для партнеров и рекламных сетей.

**На какие данные влияет AP**

Если AP включен, данные, которые клиенты могут предоставлять через постбэки или другими методами отчетности, предоставляются только в агрегированном виде. Когда режим AP включен, по пользователям iOS 14.5+, не давшим согласие, данные уровня пользователя не предоставляются через постбэки или иные способы получения отчетов, включая отчеты Protect360, связанные с мошенничеством.

В контексте постбэков используются разные типы постбэков в зависимости от того, доступен ли идентификатор рекламодателя, и других факторов.

Текущие настройки режима AP для каждого приложения можно просмотреть на дэшборде AppsFlyer. Перейдите в **Настройки** > **Активные интеграции** > выберите вашу рекламную сеть > **вкладка Интеграция.** По умолчанию режим включен.

![APforPartners2.png](https://files.readme.io/e4fb5617a47635f24dc83881c2be3d18b770200a576cb67bd3312e6fc2c123e1-360018154777.png)

#### Типы шаблонов для отправки постбэков

* **Обычный шаблон:** имеющийся шаблон интеграции с AppsFlyer с макросами user-identifier и attribution-data. Этот шаблон используется для отправки постбэков, содержащих данные атрибуции на уровне пользователя.
* **Шаблон расширенной конфиденциальности (AP)**: шаблон без макросов идентификатора пользователя user-identifier. Этот шаблон используется для отправки постбэков, содержащих агрегированные данные об атрибуции.   
  **Примечание.** Если требуется постбэк AP, а вы не завершили интеграцию AP, постбэк не будет отправлен. Настроить интеграцию AP можно самостоятельно с помощью нашего инструмента для [управления постбэками](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback).

> 📘 **Примечание**
>
> * Если пользователь дал согласие на ATT и в приложении рекламодателя, и в приложении издателя («двойное согласие»), обычные постбэки отправляются как атрибутированным, так и неатрибутированным рекламным сетям.
> * **Исключение.** Для установок, атрибутированных к Apple Search Ads (ASA), ASA отправляет постбэки по установкам в рекламную сеть, даже если для рекламодателя включена функция расширенной конфиденциальности, в следующих случаях:
>   * Не авторизовано
>   * Постбэки по установкам в рекламной сети установлены на **Все медиа-источники и органический трафик**.
>   * Рекламная сеть не поддерживает режим расширенной конфиденциальности.

### Используемый тип постбэка

В следующей таблице описаны типы постбэков в зависимости от доступности идентификатора рекламодателя и статуса расширенной конфиденциальности.

#### Тип постбэка для iOS 14.5+

<table><thead><tr><th rowspan="2">Статус AP</th><th colspan="2">Статус ATT</th><th rowspan="2">Тип шаблона постбэка для атрибутированного партнера\*, поддерживающего AP </th><th rowspan="2">Тип шаблона постбэка для атрибутированного партнера\*, не поддерживающего AP </th><th rowspan="2">Постбэк для неатрибутированного партнера\*</th></tr><tr><th>Приложение издателя</th><th>Приложение рекламодателя</th></tr></thead><tbody><tr><td>Включен</td><td>доступно</td><td>Не авторизовано</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Шаблон AP</a> (агрегированные данные)</td><td>Без постбэка</td><td>Ничего</td></tr><tr><td>Включен</td><td>Не авторизовано</td><td>доступно</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Шаблон AP</a> (агрегированные данные)</td><td>Без постбэка</td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Авторизовано</a></p><p><a href="/marketers/ru/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">Поля атрибуции</a> недоступны.\*</p></td></tr><tr><td>Включен</td><td>доступно</td><td>доступно</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Обычный шаблон</a>. Включает доступные идентификаторы, такие как IDFA, IDFV, CUID, ID клика и поля атрибуции. </td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Обычный шаблон</a>. Включает доступные идентификаторы, такие как IDFA, IDFV, CUID, ID клика и поля атрибуции. </td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Обычный шаблон</a> с доступными идентификаторами. <span><a href="/marketers/ru/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">Поля атрибуции</a> недоступны.\*</span> </td></tr><tr><td>Включен</td><td>Не авторизовано</td><td>Не авторизовано</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#используемый-тип-постбэка"><span>Шаблон AP</span></a> (агрегированные данные)</td><td>Без постбэка</td><td>Ничего</td></tr><tr><td>Откл.</td><td>Не учитывается</td><td>Не учитывается</td><td><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Обычный шаблон.</a></td><td><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Обычный шаблон.</a></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#типы-шаблонов-для-отправки-постбэков">Обычный шаблон</a>.</p><p><a href="/marketers/ru/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">Поля атрибуции</a> недоступны.\*</p></td></tr></tbody></table>

**(\*) Принципы обмена данными с партнерами**

По каждому конкретному событию право на получение постбэка могут иметь сразу несколько партнеров — рекламных сетей. Постбэки отправляются следующим образом:

* Атрибутированный партнер: рекламная сеть, которой засчитано событие
* Неатрибутированный партнер: интегрированный партнер, которому событие не засчитано, когда в разделе **In-app events postback** (Постбэк по внутреннему событию) в качестве **Sending option** (Вариант отправки) задано значение **All media sources including organic** (Все медиа-источники, включая органические). Если для приложения рекламодателя есть согласие на ATT, постбэк содержит идентификаторы пользователей без данных атрибуции. (Этот вариант поддерживается не всеми рекламными сетями.)

  ![InAppEventAll.png](https://files.readme.io/e24037f75b2b82797031eb13d5e063b8c2006812491e69674ff066ac830919f7-35847850644881.png)

### Веб-кампании

AP действует иначе, когда рекламная сеть показывает рекламу в вебе.

Чтобы указать, откуда пришел клик — из веба или из приложения, — в URL-адресе клика передается параметр `af_media_type=web` или `af_media_type=app`.

Если параметр `af_media_type` не передается, значение по умолчанию — `app`.

#### Тип постбэка, используемый для iOS 14.5+, когда режим AP включен

<table><thead><tr><th colspan="2">Статус ATT</th><th rowspan="2">Тип постбэка для атрибутированного партнера\*</th><th rowspan="2">Тип постбэка для неатрибутированного партнера\*</th></tr><tr><th>Приложение издателя</th><th>Приложение рекламодателя</th></tr></thead><tbody><tr><td>Нет</td><td>Авторизовано</td><td>Расширенные настройки конфиденциальности</td><td>Ничего</td></tr><tr><td>Нет</td><td>Авторизовано</td><td>Обычный. Данные уровня пользователя с идентификаторами IDFA, IDFV, CUID, ID клика.</td><td>Обычный. Только идентификаторы уровня пользователя.</td></tr></tbody></table>

## Интеграция

Обновите URL-адреса кликов и завершите интеграцию Advanced Privacy.

<div id="click-url-requirements" />

<Accordion title="Требования к URL-адресу клика">

Во многих случаях, в зависимости от наличия согласия пользователя на ATT, идентификатор IDFA будет недоступен в приложении издателя, приложении рекламодателя или обоих. В таких ситуациях AppsFlyer может выполнять атрибуцию, используя механизм <Anchor target="_blank" href="/marketers/ru/docs/appsflyer-attribution-model#aggregated-advanced-privacy-aap">агрегированной атрибуции, основанной на дифференцированной конфиденциальности (Aggregated Advanced Privacy)</Anchor> и <Anchor target="_blank" href="/marketers/ru/docs/appsflyer-attribution-model#probabilistic-modeling">вероятностное моделирование</Anchor>.

**[Рекомендация]** Чтобы повысить точность атрибуции, отправляйте все указанные параметры.

1. Добавьте следующие параметры к URL-адресу клика:

<table><thead><tr><th>Авторизовано</th><th>Параметр клика</th><th>Например, клик, показ</th></tr></thead><tbody><tr><td>Кампания</td><td>c</td><td>US_20_30</td></tr><tr><td>ID кампании</td><td>af_c_id</td><td>12345</td></tr><tr><td>Блок рекламы</td><td>af_adset</td><td>ADSET_1</td></tr><tr><td>ID блока рекламы</td><td>af_adset_id</td><td>56789</td></tr><tr><td>Реклама </td><td>af_ad</td><td>nazvanie_kreativa</td></tr><tr><td>Идентификатор</td><td>af_ad_id</td><td>34567</td></tr><tr><td>ID сайта</td><td>af_siteid</td><td>abcdefgh12345678</td></tr><tr><td>ID субсайта</td><td>af_sub_siteid</td><td>abcdefgh12345678</td></tr><tr><td>Канал</td><td>af_channel</td><td>nazvanie_kanala</td></tr><tr><td>Тип рекламного объявления</td><td>af_ad_type</td><td>Видео</td></tr><tr><td>Модель устройства iOS\*</td><td>af_model</td><td><p>Модель устройства. Возможные значения:</p><ul><li>iphone (все строчные буквы)</li><li>ipad (все строчные буквы)</li></ul></td></tr><tr><td>Операционная система\*</td><td>af_os</td><td>Версия операционной системы</td></tr><tr><td colspan="3">\*Некоторая информация также может предоставляться через агент пользователя. В этом случае значение, отправленное с использованием определенного идентификатора, имеет приоритет.</td></tr></tbody></table>

   Добавление сведений о кампании к URL-адресу клика

   В следующем примере показано, как добавить сведения о кампании к URL-адресу клика:

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adsetname}&af_adset_id={adset ID}&af_ad={adname}&af_ad_id={ad ID}&af_ad_type={Adtype}&af_siteid={PublisherId}` |
| --- |

2. Добавьте следующие обязательные параметры в URL-адрес клика*:

   > ❗️ **Предупреждение**
   >
   > Если URL-адрес клика не передает обязательные параметры, вам не будет засчитана большая часть принесенных вами установок.


   * IP
   * Агент пользователя

   *Никаких действий не требуется, если клик отправляется с помощью простого реферера HTTP, который перенаправляет в AppsFlyer. 

   Используйте описанный метод извлечения, чтобы добавить параметры к URL-клика при использовании любого из следующих методов:

   * Перенаправление через приложение
   * Межсерверные клики (S2S)

   #### Параметры для атрибуции в режиме расширенной конфиденциальности

   <Table>
     <thead>
       <tr>
         <th>
           Параметр
         </th>
         <th>
           Обязательно
         </th>
         <th>
           Метод извлечения
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           **Язык и локаль устройства**

           af\_lang
         </td>
         <td>
           Нет
         </td>
         <td>
           NSString *language = [[NSLocale preferredLanguages] objectAtIndex:0];

           [Рекомендуется] Укажите язык и локаль; например, en-US.
         </td>
       </tr>
       <tr>
         <td>
           **Агент пользователя**

           af\_ua
         </td>
         <td>
           Да
         </td>
         <td>
           Извлеките user-agent в формате:

           ```
           Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+13_3_1  
           +like+Mac+OS+X%29 AppleWebKit%2F605.1.15+%28KHTML%2C  
           +like+Gecko%29+Mobile%2F15E148
           ```

           * Извлеките **НЕ** *user-agent* CFNetwork, а другой.
           * User-agent должен быть закодирован в URL.
         </td>
       </tr>
       <tr>
         <td>
           **IP-адрес устройства**

           af\_ip
         </td>
         <td>
           Да
         </td>
         <td>
           Лучший вариант: если возможно, укажите IP-адрес устройства в параметре af\_ip.

           Следующий вариант: если возможно, AppsFlyer будет использовать IP-адрес из X-Forwarded-For.
         </td>
       </tr>
     </tbody>
   </Table>

   Добавление параметров к URL-адресу клика

   Чтобы передать эти обязательные параметры в ссылке атрибуции клика, используйте следующую схему:

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset name}&af_adset_id={adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad-type}&af_siteid={PublisherId}&af_ua={USER-AGENT}&af_lang={LANGUAGE}&af_ip={IP}` |
| --- |

   **Пример**

| GET `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset` name\}&af\_adset\_id=`{adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />&af\_ua=Mozilla%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2012\_1\_4%20  <br />like%20Mac%20OS%20X%29%20AppleWebKit%<br /><br />`2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Mobile%2F16D57&af_lang=en-US&af_ip=11.11.1.11` |
| --- |

   *Параметры запроса должны быть закодированы в URL.

   **Передача данных о заголовках URL-адреса клика**

   Чтобы передать поля заголовка URL-адреса клика, используйте следующую схему:

| GET `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset` name\}&af\_adset\_id=`{adset ID}&af_ad={ad name}&af_ad_id={ad ID}  <br />&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />`accept-language: en-US,en;q=0.`<br /><br />`User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X)`<br /><br />`AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148`<br /><br />`X-Forwarded-For: 11.11.1.11, 222.222.2.222` |
| --- |

</Accordion>

<div id="advanced-privacy-postback-specification" />

<Accordion title="Спецификация постбэка в режиме расширенной конфиденциальности">

Чтобы получать постбэки в режиме расширенной конфиденциальности, помимо обычной интеграции постбэков, необходимо настроить интеграцию Advanced Privacy. Вы можете настроить [постбэк в режиме расширенной конфиденциальности](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback) самостоятельно на дэшборде AppsFlyer.

**Различия между обычным шаблоном и шаблоном Advanced Privacy**

* Время постбэка не коррелирует с фактическим временем события.
* Макросы меток времени:
  * Для установок и внутренних событий приложения метки времени округляются в меньшую сторону до часа, в котором они произошли. Например, 22:55:30 указывается в отчете как 22:00:00.
  * Регистрируются по часовому поясу UTC. Пример метки времени: (2020-07-20 20:00:00)
* Следующие параметры недоступны в постбэках в режиме расширенной конфиденциальности: ID клика, ID клиента, AppsFlyer ID, IDFA, IDFV, модель устройства, версия ОС, оператор связи.

**Действия, которые рекламная сеть должна выполнить для интеграции:**

1. [Настроить постбэк в режиме расширенной конфиденциальности на дэшборде AppsFlyer.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback)
2. <Anchor target="_blank" href="/partners/ru/docs/ios-integration-testing-for-ad-networks">Протестировать интеграцию Advanced Privacy.</Anchor>

> 🚧 **Важно!**
>
> * Для того, чтобы иметь возможность различать постбэки для легитимных событий и постбэки с отказом, вы должны настроить макросы для постбэков с отказом.
> * Чтобы активировать постбэки по установкам/событиям с отказом, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.

#### Конечная точка постбэка Advanced Privacy [заполните по мере необходимости]

| Тип постбэка |
| --- |
| Установка |
| Переданный приложением |

#### Доступен макрос атрибуции в режиме расширенной конфиденциальности

<table><thead><tr><th>Макрос в постбэке (название)</th><th>Примечания</th><th>Базовые параметры для всех постбэков</th><th>Дополнительные параметры для внутренних событий приложения </th><th>Дополнительные параметры для отклоненной атрибуции</th></tr></thead><tbody><tr><td>af_ad</td><td>Имя креатива</td><td>Да</td><td> </td><td> </td></tr><tr><td>af_ad_id</td><td>34567</td><td>Да</td><td> </td><td> </td></tr><tr><td>af_ad_type</td><td>Например, баннер, футер, видео</td><td>Да</td><td> </td><td> </td></tr><tr><td>af_adset</td><td>ADSET_1</td><td>Да</td><td> </td><td> </td></tr><tr><td>af_adset_id</td><td>56789</td><td>Да</td><td> </td><td> </td></tr><tr><td>app_id (идентификатор приложения)</td><td>-</td><td>Да</td><td> </td><td> </td></tr><tr><td>Переданный приложением</td><td>-</td><td>Да</td><td> </td><td> </td></tr><tr><td>attributed_touch_hour</td><td><p>Округляется в меньшую сторону до ближайшего часа. </p><p>См. примечание по формату (1)</p></td><td>Да</td><td> </td><td> </td></tr><tr><td>attributed_touch_type (атрибутированный тип взаимодействия)</td><td>Например, клик, показ</td><td>Да</td><td> </td><td> </td></tr><tr><td>заблокированная_причина</td><td>Связано с правилами валидации / Protect360</td><td> </td><td> </td><td>Да</td></tr><tr><td>заблокированное_значение_причины</td><td>Связано с правилами валидации / Protect360</td><td> </td><td> </td><td>Да</td></tr><tr><td>заблокированная_подпричина</td><td>Связано с правилами валидации / Protect360</td><td> </td><td> </td><td>Да</td></tr><tr><td>Авторизовано</td><td>Как задано рекламодателем</td><td>Да</td><td> </td><td> </td></tr><tr><td>c</td><td>Название кампании, например, US_20_30</td><td>Да</td><td> </td><td> </td></tr><tr><td>af_c_id</td><td>Идентификатор кампании, например, 12345</td><td>Да</td><td> </td><td> </td></tr><tr><td>af_channel</td><td>Имя канала</td><td>Да</td><td> </td><td> </td></tr><tr><td>код_страны</td><td>ISO-код страны, зафиксированный при конверсии</td><td>Да</td><td> </td><td> </td></tr><tr><td>event_hour</td><td><p>Округляется в меньшую сторону до ближайшего часа. </p><p>См. примечание по формату (1)</p></td><td>Да</td><td> </td><td> </td></tr><tr><td>имя_события</td><td>Переданный приложением</td><td> </td><td>Да</td><td> </td></tr><tr><td>event_revenue</td><td>Сумма дохода в валюте события</td><td> </td><td>Да</td><td> </td></tr><tr><td>event_revenue_<br/>currency</td><td>Код валюты дохода</td><td> </td><td>Да</td><td> </td></tr><tr><td>event_revenue_usd</td><td>Доход в долларах США</td><td> </td><td>Да</td><td> </td></tr><tr><td>Авторизовано</td><td><p>Округляется в меньшую сторону до ближайшего часа. </p><p>Формат: см. примечание (1)</p></td><td>Да</td><td> </td><td> </td></tr><tr><td>Авторизовано</td><td>Истинно, если данное событие в приложении было впервые инициировано определенным конечным пользователем</td><td> </td><td>Да</td><td> </td></tr><tr><td>is_primary</td><td><p>Используется для удаления дубликатов</p><p>Логическое значение: 0, 1</p></td><td> </td><td>Да</td><td> </td></tr><tr><td>is_retargeting</td><td><p>Используется для удаления дубликатов </p><p>Формат: см. примечание (2)</p></td><td>Да</td><td> </td><td> </td></tr><tr><td>is_reengagement</td><td>Формат: см. примечание (2)</td><td> </td><td>Да</td><td> </td></tr><tr><td>Авторизовано</td><td><p>Используется для удаления дубликатов </p><p>Формат: см. примечание (2)</p></td><td>Да</td><td> </td><td> </td></tr><tr><td>Местоположение устройства</td><td>Примеры: id_matching, probabilistic</td><td>Да</td><td> </td><td> </td></tr><tr><td>Доход, связанный с SKU, в валюте, указанной в поле <code>event_revenue_currency</code>.</td><td>Имя/идентификатор соответствующего события на платформе рекламной сети</td><td> </td><td>Да</td><td> </td></tr><tr><td>platform</td><td>Например, iOS, Android</td><td>Да</td><td> </td><td> </td></tr><tr><td>postback_id</td><td>Уникальный идентификатор постбэка</td><td>Да</td><td> </td><td> </td></tr><tr><td>retargeting_<br/>conversion_type</td><td>Например, повторное вовлечение, реатрибуция</td><td>Да</td><td> </td><td> </td></tr><tr><td>af_siteid</td><td>abcdefgh12345678</td><td>Да</td><td> </td><td> </td></tr><tr><td>af_sub_siteid</td><td>abcdefgh12345678</td><td>Да</td><td> </td><td> </td></tr><tr><td colspan="5"><p>ПРИМЕЧАНИЯ</p><p>(1) Доступные форматы меток времени:</p><ul><li>[По умолчанию] строка: YYYY-MM-DD HH:MM:SS</li><li>Unix-время: 10-значная метка времени Unix </li></ul><p>(2) Доступен логический формат</p><ul><li>[По умолчанию] числовой: 0, 1 </li><li>Строка: <em>false</em>, <em>true</em> </li></ul></td></tr></tbody></table>

</Accordion>

<div id="setting-up-your-advanced-privacy-postback" />

<Accordion title="Настройка постбэка в режиме расширенной конфиденциальности">

Настройте постбэк AP в разделе управления постбэками на дэшборде AppsFlyer.

**Необходимые условия**:

* Чтобы управлять постбэками в режиме расширенной конфиденциальности, у вас должна быть активная интеграция с AppsFlyer. Свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>, <Anchor target="_blank" href="/partners/ru/docs/getting-started-onboarding-guide-for-ad-networks">чтобы создать интеграцию</Anchor>.
* ![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Управление постбэками выполняется администратором аккаунта; у членов команды нет соответствующего доступа.

**Чтобы настроить постбэк:**

1. Щелкните выпадающее меню в правом верхнем углу и выберите **Postback management** (Управление постбэками).
2. Выберите тип постбэка: **Advanced Privacy.**
3. Активируйте конструктор.

   ![postback-management-enter-endpoint_en-us.png](https://files.readme.io/4ea0ffc61d1ecdb11d3c745876c29a942fde4133b8ebb54a1426a73c1dc63b16-360018215218.png)
4. Введите **адрес конечной точки**: URL-адрес конечной точки, на который AppsFlyer будет отправлять постбэки. Введите действительные URL-адреса для установок и/или внутренних событий приложения.
5. Введите параметры, которые требуется включать в постбэки:

   * **Имя параметра**: экранное имя параметра AppsFlyer
   * **Получаемый параметр**: соответствующий параметр, получаемый на вашей стороне
   * **Значение параметра** (доступно для некоторых параметров): выберите формат значения. Например, «истина/ложь» или «1/0» для логических значений.
   * **Установка**: установите флажок, чтобы включить параметр в постбэк установки.
   * **Внутреннее событие**: установите флажок, чтобы включить параметр в постбэк внутреннего события приложения.

   ![postback-management-parameters_en-us.png](https://files.readme.io/818ef31df9c4e349ca26b5421a0ba0582ed5f7f9fae39f1d0e4ec3b7562f4192-360018213698.png)

   Полный список [макросов, поддерживаемых в постбэках в режиме расширенной конфиденциальности](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification).
6. **[Необязательно]** Добавьте свои параметры, которые не предоставляются AppsFlyer:

   ![postback-management-custom-parameters_en-us.png](https://files.readme.io/6bca46e1d39c6822b0e041eb1dcbb1b2d40e42fa062c34877c8cbf0c2d2847d6-16589581250321.png)
7. Откройте превью окончательного шаблона постбэка, чтобы убедиться, что все верно.

   ![postback-management-template_en-us.png](https://files.readme.io/b5e41cad37859365c7818c4561620f8a78250c207d8326dae53ed9b522fe3716-360018213718.png)
8. Нажмите **Сохранить**. Обратите внимание, что при сохранении постбэка изменения сразу вступают в силу.

Если возникнут проблемы, свяжитесь с нами через <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">виджет помощи партнерам</Anchor>.

</Accordion>

## Дополнительные сведения

<div id="ap-for-analytics-partners" />

<Accordion title="AP для партнеров по аналитике">

Партнерам по аналитике постбэки отправляются следующим образом:

* AP выкл.: постбэк с данными уровня пользователя без ограничений.
* AP включен: тип постбэка зависит от источника пользователя и доступности идентификатора рекламодателя, как показано в следующей таблице.

#### Тип постбэка для партнера по аналитике с учетом статуса ATT и источника, из которого пришел пользователь

<table><thead><tr><th rowspan="2">Источник, из которого пришел пользователь</th><th colspan="2">ID рекламы.</th><th rowspan="2">Тип постбэка для партнера по аналитике</th></tr><tr><th>Приложение издателя</th><th> Приложение рекламодателя</th></tr></thead><tbody><tr><td rowspan="3"><p>Неорганические </p></td><td>доступно</td><td>доступно</td><td>Обычный</td></tr><tr><td>Не авторизовано</td><td>доступно</td><td>Ничего</td></tr><tr><td>Любое значение</td><td>Не авторизовано</td><td>Ничего</td></tr><tr><td>Органический или веб</td><td>Нет</td><td>доступно</td><td>Обычный</td></tr><tr><td>Органический или веб</td><td>Нет</td><td>Не авторизовано</td><td>Ничего</td></tr></tbody></table>

</Accordion>

<div id="ap-vs-skadnetwork" />

<Accordion title="AP vs. SKAdNetwork">

<Anchor target="_blank" href="/partners/ru/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> — это технология атрибуции, предоставляемая Apple для устройств iOS. Режим расширенной конфиденциальности (Advanced Privacy) — это часть фреймворка <Anchor target="_blank" href="/marketers/ru/docs/apply-aggregated-advanced-privacy-framework">AppsFlyer Aggregated Advanced Privacy</Anchor> (AAP), которая относится к атрибуции, выполняемой AppsFlyer. AAP дает рекламодателям возможность контролировать доступность данных атрибуции, предоставляемых через платформу AppsFlyer. Как правило, рекламные сети поддерживают интеграцию как с AP, так и со SKAdNetwork.

</Accordion>

<div data-zendesk-anchors="h_01HJR7MWPM9XA4BXHDRD2K6D56=%D0%BD%D0%BE%D0%B2%D0%BE%D1%81%D1%82%D0%B8-%D0%BE-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B5-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 ad-network-advanced-privacy-datasharing-principles=%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B-%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8-%D0%B2-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B5-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 h_01HJR7MWPNYNMKZ3R8C3BB5EVG=%D0%BF%D1%80%D0%B8%D0%BD%D1%86%D0%B8%D0%BF%D1%8B-%D0%BE%D0%B1%D0%BC%D0%B5%D0%BD%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D0%BC%D0%B8-%D0%B2-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B5-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 types-of-templates-for-sending-postbacks=%D1%82%D0%B8%D0%BF%D1%8B-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B8-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 h_01HJR7MWPN92BDJRK734P6YXSK=%D1%82%D0%B8%D0%BF%D1%8B-%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD%D0%BE%D0%B2-%D0%B4%D0%BB%D1%8F-%D0%BE%D1%82%D0%BF%D1%80%D0%B0%D0%B2%D0%BA%D0%B8-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%BE%D0%B2 h_01HJR7MWPN71TP0KWVVBHPC0H2=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 type-of-postback-used=%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D0%BC%D1%8B%D0%B9-%D1%82%D0%B8%D0%BF-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0 h_01HJR7MWPNJEDNDT1ZY7P78HMG=%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D0%BC%D1%8B%D0%B9-%D1%82%D0%B8%D0%BF-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0 postback-type-for-ios-145=%D1%82%D0%B8%D0%BF-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%B4%D0%BB%D1%8F-ios-145 h_01HJR7MWPNESP8BDC4D6Y7SBFZ=%D1%82%D0%B8%D0%BF-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%B4%D0%BB%D1%8F-ios-145 web-campaigns=%D0%B2%D0%B5%D0%B1-%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8 h_01HJR7MWPNXHHCSQ6BGCNRBHZK=%D0%B2%D0%B5%D0%B1-%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8 postback-type-used-for-ios-145-when-ap-is-on=%D1%82%D0%B8%D0%BF-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D0%BC%D1%8B%D0%B9-%D0%B4%D0%BB%D1%8F-ios-145-%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC-ap-%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD h_01HJR7MWPNQCCNGHQY5RQHQ6D1=%D1%82%D0%B8%D0%BF-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%B8%D1%81%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D1%83%D0%B5%D0%BC%D1%8B%D0%B9-%D0%B4%D0%BB%D1%8F-ios-145-%D0%BA%D0%BE%D0%B3%D0%B4%D0%B0-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC-ap-%D0%B2%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD integration=%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F h_01HJR7MWPP7YGRXJQR29F3ERHH=%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F h_01HJR7MWPPAXK18KER56E30G8R=click-url-requirements h_01HJR7MWPPRN8XYVSS7HX7NQB9=%D0%BF%D1%80%D0%B5%D0%B4%D1%83%D0%BF%D1%80%D0%B5%D0%B6%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5 parameters-for-advanced-privacy-attribution=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%B2-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B5-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8 h_01HJR7MWPPK2HET3XYW4WBFAZ1=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%B2-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B5-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8 h_01HJR7MWPQ60F4CESKRRMTQ7HX=advanced-privacy-postback-specification h_01HJR7MWPQ8K06A1YM4KV4RTN8=%D0%B2%D0%B0%D0%B6%D0%BD%D0%BE advanced-privacy-postback-endpoint-%5Bcomplete-as-required%5D=%D0%BA%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F-%D1%82%D0%BE%D1%87%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-advanced-privacy-%D0%B7%D0%B0%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5-%D0%BF%D0%BE-%D0%BC%D0%B5%D1%80%D0%B5-%D0%BD%D0%B5%D0%BE%D0%B1%D1%85%D0%BE%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8 h_01HJR7MWPQX9SXJZMBS6QR07WD=%D0%BA%D0%BE%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F-%D1%82%D0%BE%D1%87%D0%BA%D0%B0-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-advanced-privacy-%D0%B7%D0%B0%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5-%D0%BF%D0%BE-%D0%BC%D0%B5%D1%80%D0%B5-%D0%BD%D0%B5%D0%BE%D0%B1%D1%85%D0%BE%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D0%B8 advanced-privacy-attribution-macros-available=%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B5%D0%BD-%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%B2-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B5-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8 h_01HJR7MWPQKH52XMD6H9TJ0SM3=%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B5%D0%BD-%D0%BC%D0%B0%D0%BA%D1%80%D0%BE%D1%81-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%B2-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B5-%D1%80%D0%B0%D1%81%D1%88%D0%B8%D1%80%D0%B5%D0%BD%D0%BD%D0%BE%D0%B9-%D0%BA%D0%BE%D0%BD%D1%84%D0%B8%D0%B4%D0%B5%D0%BD%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B8 h_01HJR7MWPRC44K908A4EAPN9GV=setting-up-your-advanced-privacy-postback additional-information=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F h_01HJR7MWPRVFR6YN56Y0DGBAXH=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F h_01HJR7MWPR6ACNYVZHK7YPHQGP=ap-for-analytics-partners analytics-partner-postback-type-according-to-att-status-and-user-source=%D1%82%D0%B8%D0%BF-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D0%B0-%D0%BF%D0%BE-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B5-%D1%81-%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BC-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%B0-att-%D0%B8-%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B0-%D0%B8%D0%B7-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%B8%D1%88%D0%B5%D0%BB-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C h_01HJR7MWPRZDJNSZNB981WB5Z1=%D1%82%D0%B8%D0%BF-%D0%BF%D0%BE%D1%81%D1%82%D0%B1%D1%8D%D0%BA%D0%B0-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D0%B0-%D0%BF%D0%BE-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B5-%D1%81-%D1%83%D1%87%D0%B5%D1%82%D0%BE%D0%BC-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%B0-att-%D0%B8-%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA%D0%B0-%D0%B8%D0%B7-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%B8%D1%88%D0%B5%D0%BB-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C h_01HJR7MWPR3YR7E9S49P9ZZ3CT=ap-vs-skadnetwork" />
