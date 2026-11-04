---
title: API списка приложений для рекламных сетей
metadata:
  keywords:
    - API
    - Ad Networks
    - Partners
    - Developers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-08-06T20:11:15Z'
  edited_at: '2026-09-02T00:35:49Z'
  id: 360011700857
  locale: ru
  section: APIs for ad networks
  section_id: 6551618728209
  url: https://support.appsflyer.com/hc/ru/articles/360011700857
---
> **Кратко:** рекламные сети могут получать метаданные приложений, связанных с их учетной записью интегрированного партнера.

<div id="get-app-list-api" />

## API для получения списка приложений

В следующих разделах содержится информация, необходимая для использования API.

<div id="get-app-list-basics" />

<Accordion title="Основные сведения о получении списка приложений">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><span>Description(Описание)</span></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>УСТАНОВИТЬ</code></td></tr><tr><td>Путь</td><td><span>https://hq1.appsflyer.com/api/mng/apps</span></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен в дэшборде следующим образом: <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в раскрывающийся список электронной почты &gt; API tokens, чтобы получить токен V2</a> </li></ul></td></tr><tr><td rowspan="3"> Ответ</td><td>Результаты</td><td>Возвращает в формате JSON</td></tr><tr><td>Лимит запросов</td><td><ul><li>20 запросов/мин</li><li>100 запросов/день</li></ul></td></tr><tr><td>Лимит записей</td><td>1,000 записей/запрос. Если нужно вернуть более 1,000 записей, используйте последующие запросы пагинации, описанные в этой статье.</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="Запрос API">

API-запрос состоит из метода, пути, обязательного параметра capabilities и необязательных параметров пагинации. Токен содержится в заголовке авторизации.

**Аудитории**

```http
GET https://hq1.appsflyer.com/api/mng/apps?capabilities={capabilities} 
```

<div id="get-app-list-mandatory-parameters" />

#### Обязательные параметры для получения списка приложений

<Table>
  <thead>
    <tr>
      <th>
        Параметры запроса
      </th>
      <th>
        Description(Описание)
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        возможности
      </td>
      <td>
        Чтобы получить список и количество приложений, для которых у вас есть разрешения или возможности интеграции, задайте для параметра capabilities одно из указанных значений.

        | Вариант | Тип | Description(Описание) |
        | --- | --- | --- |
        | `protect_360` | Разрешение на отчеты | Получить <Anchor target="_blank" href="/partners/ru/docs/protect360-for-integrated-partners">отчеты о сырых данных Protect360 для рекламных сетей</Anchor> |
        | `cost` | Интеграция | Приложение включено для получения данных о стоимости <Anchor target="_blank" href="/partners/ru/docs/incost-api-for-ad-networks">через InCost API</Anchor> |

        **Пример**: список приложений, для которых у вас есть разрешение API на отчет о сырых данных Protect360:`capabilities=protect_360`
      </td>
    </tr>
  </tbody>
</Table>

<div id="pagination-mechanism" />

#### **Механизм пагинации**

Реализован механизм пагинации, который всегда активен.

**Принципы пагинации:**

* Возвращает до 1 000 записей за один запрос (страницу).
* Ответы JSON содержат следующие ключи, связанные с пагинацией:
  * **meta.total\_items**: количество записей, возвращаемых всеми страницами в совокупности. Это количество приложений, для которых вам предоставлены запрашиваемые возможности.
  * Ссылки пагинации (показанные в JSON ниже) содержат следующие ключи:
    * **links.prev**: если был предыдущий запрос, то запрос, использованный для формирования предыдущей страницы.
    * **links.self**: текущий запрос — запрос, использованный для формирования текущего JSON (страницы)
    * **links.next**: запрос, необходимый для получения следующей страницы. Если ключ next отсутствует, значит это последняя страница.

**Используйте один из следующих методов контроля пагинации:**

* [Практические рекомендации] Используйте ссылки в JSON: если ключ links.next существует, используйте его для создания запроса на получение следующей страницы. Продолжайте, пока не получите JSON без ключа links.next.
* Программно реализуйте параметры limit и offset вместе с ключом total\_items.

**Пример JSON со ссылками пагинации**

* В следующем примере показан результат первого запроса, состоящий из второго запроса, содержащего две записи в разделе данных (не отображаются).
* Общее количество возвращаемых записей — 6.
* Ключ **links.next** содержит запрос, который возвращает следующую страницу — записи 5 и 6.

```json
{                                                                                         
    "data": {[...]},   
    "meta": {
        "total_items": 6
    },
    "links": {
        "prev": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=0&limit=2",
        "self": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=2&limit=2",
        "next": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=4&limit=2"
    }
}
```

<div id="pagination-mechanism-parameters-optional" />

#### Параметры механизма пагинации (необязательно)

<table><thead><tr><th>Параметр запроса</th><th>Обзор</th></tr></thead><tbody><tr><td>limit</td><td><p>Количество записей, возвращаемых за один вызов</p><ul><li>Максимум: 1 000</li><li>Если вы не передаете <code>limit</code>, он автоматически устанавливается в 1 000.</li><li>Пример: <code>limit=2</code> </li><li>Обязательно: Нет</li></ul></td></tr><tr><td>offset</td><td><p>Первая запись, которую нужно вернуть в вызове. Нумерация записей начинается с 0. </p><ul><li>Если не отправить <code>offset</code>, ему автоматически присваивается значение 0.</li><li>Пример: <code>offset=2</code> </li><li>Обязательно: Нет</li></ul></td></tr><tr><td colspan="2"> </td></tr></tbody></table>

</Accordion>

<div id="json-response" />

<Accordion title="Ответ JSON">

| **Ключ** | **Обзор** |
| --- | --- |
| id | ID приложения, например: `id123456789`, `com.myapp.com` |
| type | Всегда возвращает `app` |
| Имя камп. | ID приложения |
| платформа | iOS или Android |
| валюта | Код валюты приложения, заданный рекламодателем |
| time\_zone | Часовой пояс приложения, заданный рекламодателем |
| total\_items | Количество приложений, для которых рекламная сеть поддерживает запрошенную опцию capabilities |
| ссылки | Механизм пагинации (описан в разделе параметров)<ul><li>prev: вызов, использованный для формирования предыдущей страницы</li><li>self: вызов, использованный для формирования текущей страницы</li><li>next: вызов, использованный для формирования следующей страницы</li></ul> |

</Accordion>

<div id="get-app-list-curl-example-and-response" />

<Accordion title="Пример curl-запроса для получения списка приложений и ответа">

**Запрос curl**

Этот пример включает полный вызов, в том числе необязательные параметры пагинации.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&limit=1000&offset=0' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \ \
```

**Ответ JSON**

```json
{
    "data": [
        {
            "id": "com.appsflyer.xpend_qa1",
            "type": "app",
            "attributes": {
                "name": "com.appsflyer.xpend_qa1",
                "platform": "android",
                "currency": "USD",
                "time_zone": "UTC"
            }
        },
        {
            "id": "com.abc.app",
            "type": "app",
            "attributes": {
                "name": "com.abc.app",
                "platform": "android",
                "currency": "USD",
                "time_zone": "UTC",
                "enable_retargetting": true
            }
        },
        {
            "id": "com.xyz.app",
            "type": "app",
            "attributes": {
                "name": "com.xyz.app",
                "platform": "android",
                "currency": "JPY",
                "time_zone": "UTC"
            }
        }
    ],
    "meta": {
        "total_items": 3
    },
    "links": {
        "self": "https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&offset=0&limit=1000"
           }
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="Коды ответа HTTP">

| Код | Сообщение | Примечания/устранение неполадок |
| --- | --- | --- |
| 200 | OK | Возвращаются действительные данные |
| 200 | OK | **Симптом**: данные не возвращаются<br /><br />**Действие**: убедитесь, что токен аутентификации находится в заголовке Bearer. |
| 400 | Неверный запрос | <ul><li>См. сообщение в JSON</li><li>Пустой JSON: указана недопустимая capability</li></ul> |
| 401 | Не авторизовано | **Сообщение**: токен авторизации имеет неверный формат<br /><br />Убедитесь, что у вас правильный токен; токен должен содержать более 700 символов. |
| 404 | Не найдено | <ul><li>Устраните все проблемы, связанные с сетью или брандмауэром.</li><li>Убедитесь, что <Anchor target="_blank" href="/marketers/ru/docs/appsflyer-server-ip-address-ranges-allowlisting">IP-адреса AppsFlyer добавлены в список разрешенных</Anchor></li><li>Убедитесь, что вы используете последний выданный токен.</li><li>Данные не найдены: запрошенный тип разрешения/интеграции (возможностей) допустим, но приложения с таким разрешением не найдены.</li></ul> |
| 429 | Слишком много запросов | Превышено ограничение скорости запросов |

</Accordion>

<div data-zendesk-anchors="get-app-list-api=api-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 h_01KQS54YXJ2XBV5BAT3TGJ9SBT=api-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 h_01KQS54YXJHYS9KC2Y7BEP87MZ=get-app-list-basics h_01KQS54YXJJ9SE7DSRTA2X2A9M=api-request get-app-list-mandatory-parameters=%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 h_01KQS54YXJPDZGJB7K6KH1D2W1=%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%B4%D0%BB%D1%8F-%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D1%81%D0%BF%D0%B8%D1%81%D0%BA%D0%B0-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 pagination-mechanism=%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%B7%D0%BC-%D0%BF%D0%B0%D0%B3%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8 h_01KQS54YXJ9X0XBJQ01K6WK2RB=%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%B7%D0%BC-%D0%BF%D0%B0%D0%B3%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8 pagination-mechanism-parameters-optional=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%B7%D0%BC%D0%B0-%D0%BF%D0%B0%D0%B3%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8-%D0%BD%D0%B5%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE h_01KQS54YXJX943PMF5JWV67THW=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BC%D0%B5%D1%85%D0%B0%D0%BD%D0%B8%D0%B7%D0%BC%D0%B0-%D0%BF%D0%B0%D0%B3%D0%B8%D0%BD%D0%B0%D1%86%D0%B8%D0%B8-%D0%BD%D0%B5%D0%BE%D0%B1%D1%8F%D0%B7%D0%B0%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE h_01KQS54YXJS43JYQQHCWCAED6Q=json-response h_01KQS54YXJJK7Y23TSSF1BB58R=get-app-list-curl-example-and-response h_01KQS54YXJ2638DBZWDSN4J9G4=http-response-codes" />
