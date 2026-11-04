---
title: Подпись кликов для рекламных сетей
metadata:
  keywords:
    - Ad Network
    - Advertisers
    - Protect360
    - Ad Networks
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Ad Networks
    - Data Management
  created_at: '2021-02-22T09:33:52Z'
  edited_at: '2024-08-07T10:25:01Z'
  id: 360017831497
  locale: ru
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ru/articles/360017831497
---
> **Краткий обзор.** Добавьте проверку подписи кликов, чтобы избежать ответственности за мошенничество и чтобы мошеннические клики не атрибутировались к вашей рекламной сети.

<div id="about-click-signing" />

## О подписи кликов

Используя минимальные технологии, мошенники могут отправлять клики от имени рекламной сети и создавать тысячи или даже миллионы фальшивых кликов, которые отправляются в AppsFlyer. Иногда сами рекламные сети не знают об этой проблеме. 

Чтобы рекламная сеть могла убедиться, что клики, атрибутируемые ей AppsFlyer, действительно исходят из рекламной сети, а не от мошенника, создающего фальшивые клики, рекламные сети должны обозначать клики подписями <Anchor target="_blank" href="https://en.wikipedia.org/wiki/HMAC">HMAC-SHA256</Anchor>.

Подпись кликов также предотвращает блокировку трафика рекламной сети вследствие клик-флудинга. Это значит, что если рекламная сеть достигает порога блокировки кликов из-за чрезвычайно высокого уровня клик-флудинга, AppsFlyer перестает записывать и атрибутировать клики до конца дня.

Подписи позволяют AppsFlyer проверять клики и следить за тем, чтобы информация о кликах не была изменена мошенниками.

* Подтвержденные клики регистрируются и атрибутируются к рекламной сети
* Недействительные клики отклоняются и: 
  * Доступны в отчетах Protect360 для рекламных сетей (не для рекламодателей). <Anchor target="_blank" href="/partners/ru/docs/protect360-reports-for-ad-networks#failed-click-signatures">Узнать больше</Anchor>
  * Без влияния на коэффициент конверсии или порог блокировки кликов в рекламной сети

<div id="click-signature-integration" />

## Интеграция подписи кликов

<div id="flow" />

### Сценарий

На схеме ниже показан процесс от первоначальной разработки и базовых тестов до производственных тестов и, наконец, производства. 

![Click_signing_integration_flow.png](https://files.readme.io/3bc0103090535c22db027fb09f72ad89d88210bba8f2b6f43d1166c2911d71cd-360017572558.png)

<div id="procedure" />

### Процедура

**Предварительные условия:** <Anchor target="_blank" href="/marketers/ru/docs/managing-appsflyer-tokens">Токен API V2.0</Anchor> от администратора для авторизации API подписи кликов.

**Чтобы подписать свои клики**:

1. Сгенерируйте секретный ключ с помощью API для генерирования секретных ключей.  
   Практические рекомендации: Создавайте и используйте новый секретный ключ каждые 24 часа со сроком действия 36 часов.
2. Разработайте на своих серверах код, который вызывает API для генерирования секретных ключей, берет секретный ключ и генерирует подпись HMAC-SHA256. См. пример кода.  
   Вы можете использовать другие API согласно таблице ниже.
3. Код добавляет следующее к вашим URL-адресам кликов:
   * Параметр **expires**, содержащий временную метку Unix (в формате UTC), после которой рекламная сеть не претендует на клик
   * Подпись HMAC-SHA256.  
     Пример:

     ```http
     https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_siteid=12345&expires=1597657118&signature_v2=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk
     ```

<div id="note" />

> 📘 **Примечание**
>
> Убедитесь, что URL-адрес содержит специальные символы или пробелы в вашей ссылке до создания подписи клика. Генерирование подписи сначала приводит к ошибке верификации.

<div id="creating-a-click-signature" />

## Создание подписи клика

Чтобы создать подпись клика, необходимо выполнить следующее:

1. Создайте JSON, используя приведенный ниже список атрибутов и правила JSON
2. Создайте подпись из этого JSON с помощью HMAC56

<div id="list-of-attributes" />

### Список атрибутов

Для подписи кликов и вовлечения поддерживается следующий список атрибутов.

| Порядок | Параметр | Обязательно / Нет | Примечания |
| --- | --- | --- | --- |
| 1 | link\_domain | Да | Домен из URL-адреса клика Например:<ul><li>app.appsflyer.com</li><li>myapp.onelink.me</li><li>click.mycustomdomain.com</li></ul> |
| 2 | link\_path | Да | Путь к URL-адресу клика без обратной косой черты впереди.  <br />**app-id** для одноплатформенных ссылок и **template-id** для OneLink |
| 3 | pid | Да |  |
| 4 | af\_prt | Нет |  |
| 5 | af\_siteid | Да |  |
| 6 | clickid | Да | Одноразовый уникальный идентификатор клика |
| 7 | expires | Да | Срок действия клика |
| 8 | af\_engagement\_type | Нет |  |
| 9 | af\_click\_lookback | Нет |  |
| 10 | af\_viewthrough\_lookback | Нет |  |
| 11 | af\_reengagement\_window | Нет |  |
| 12 | is\_retargeting | Нет |  |
| 13 | af\_ip | Нет |  |
| 14 | advertising\_id | Нет |  |
| 15 | oaid | Нет |  |
| 16 | fire\_advertising\_id | Нет |  |
| 17 | idfa | Нет |  |
| 18 | idfv | Нет |  |

<div id="attribute-and-json-rules" />

### Атрибуты и правила JSON

<div id="order-and-appearance-of-attributes" />

#### Порядок и внешний вид атрибутов

* В JSON должны быть поддерживаемые параметры в URL-адресе вовлечения со значением
* Атрибуты должны быть перечислены в JSON в порядке, указанном в таблице выше

<div id="empty-attributes" />

#### Пустые атрибуты

* Атрибуты, перечисленные в JSON, не могут быть пустыми значениями или содержать только пробелы

<div id="json-data-structure" />

#### Структура данных JSON

* Структура данных JSON должна представлять собой массив атрибутов
  * Каждый атрибут будет иметь формат [«ключ», «значение»]  
    Пример:   
    `[["key-1","value-1"],["key-2","value-2"]...["key-n","value-n"]]`

<div id="attribute-value-escaping" />

#### Экранирование значения атрибута

* Значения в JSON должны быть записаны в **строках нижнего регистра**, как определено в <Anchor target="_blank" href="https://www.w3docs.com/snippets/java/how-should-i-escape-strings-in-json.html">стандарте JSON</Anchor>.

<div id="json-spaces" />

#### Пробелы JSON

* JSON необходимо сжать. В нем не должно быть пробелов, табуляций или символов новой строки между значениями.

<div id="signature-algorithm" />

#### Алгоритм подписи

* Используйте HMacSha256 с секретным ключом для создания подписи для JSON
* Закодируйте подпись с помощью Base64 **без** заполнения
* Добавьте подпись к URL-адресу клика с параметром signature\_v2

```json
//generate a signature from the click url and encode it with base64 without padding String generatedSignature = Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(jsonString.getBytes()));
```

<div id="signature-example" />

### Пример подписи

<div id="building-a-signature-example" />

<Accordion title="Создание примера подписи">

Пример URL-адреса для перехода по ссылке OneLink (для нескольких платформ):

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&clickid=sdkfjasksjskdfj9845weh&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615
```

Пример объекта json для подписи (до удаления пробелов):

```json
[
	["link_domain","yourbrand.onelink.me"],
	["link_path","qswl"],
	["pid","mediasource_int"],
	["af_siteid","my_site"],
	["clickid","12345"],
	["expires","1689695615"]
]
```

Пример объекта json для подписи (после удаления пробелов)

```json
[["link_domain","yourbrand.onelink.me"],["link_path","qswl"],["pid","mediasource_int"],["template-id","qswl"],["af_siteid","my_site"],["clickid","12345"],["expires","1689695615"]]
```

URL-адрес последнего клика с подписью:

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615  
&signature_v2=WIfCmfLAPSsVrBTqCqfihMeLCnbE4dIAlhHF84WsiWA
```

</Accordion>

<div id="code-examples" />

### Примеры кода

<div id="signingsupportedparamsjson" />

<Accordion title="signing-supported-params.json">

```json
[
  {"index":1, "name":"pid", "mandatory":true},
  {"index":2, "name":"af_prt", "mandatory":false},
  {"index":3, "name":"af_siteid", "mandatory":true},
  {"index":4, "name":"clickid", "mandatory":true},
  {"index":5, "name":"expires", "mandatory":true},
  {"index":6, "name":"af_engagement_type", "mandatory":false},
  {"index":7, "name":"af_click_lookback", "mandatory":false},
  {"index":8, "name":"af_viewthrough_lookback", "mandatory":false},
  {"index":9, "name":"af_reengagement_window", "mandatory":false},
  {"index":10, "name":"is_retargeting", "mandatory":false},
  {"index":11, "name":"af_ip", "mandatory":false},
  {"index":12, "name":"advertising_id", "mandatory":false},
  {"index":13, "name":"oaid", "mandatory":false},
  {"index":14, "name":"fire_advertising_id", "mandatory":false},
  {"index":15, "name":"idfa", "mandatory":false},
  {"index":16, "name":"idfv", "mandatory":false}
]
```

</Accordion>

<div id="signatureexamplego" />

<Accordion title="signature-example.go">

```json
package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/url"
	"os"
	"strings"
	"time"
)

type Param struct {
	Name      string
	Mandatory bool
}

func LoadSupportedParams() ([]Param, error) {
	path := "./signing-supported-params.json"
	jsonFile, _ := os.Open(path)
	defer jsonFile.Close()
	byteValue, err := io.ReadAll(jsonFile)
	if err != nil {
		return nil, errors.New("failed loading " + path)
	}
	var params []Param
	_ = json.Unmarshal(byteValue, &params)
	return params, nil
}

func computeHmac256(message, secret string) (res string, errResult error) {
	defer func() {
		if r := recover(); r != nil {
			errResult = r.(error)
			fmt.Println("failed to invoke ComputeHmac256. err: %+v", errResult)
			res = ""
			return
		}
	}()

	key := []byte(secret)
	h := hmac.New(sha256.New, key)
	h.Write([]byte(message))
	return base64.URLEncoding.WithPadding(base64.NoPadding).EncodeToString(h.Sum(nil)), nil
}

// this function accepts a click url, a ttl for the click in seconds, and the list of supported params
// the function:
// 1. adds the expiration to the click based on the provided ttl
// 2. builds a json for the signature
// 3. create an HMAC256 signature
// 4. adds the signature to the click url
func signURLV2(originalURL string, secret string, clickTtlSeconds int64, supportedParams []Param) (signedURL string, err error) {

	//add an expiration to the click
	expires := time.Now().UTC().Unix() + clickTtlSeconds
	urlWithExpired := fmt.Sprintf("%s%s%d", originalURL, "&expires=", expires)

	//parse the url
	parsedURL, err := url.Parse(urlWithExpired)
	if err != nil {
		return "", errors.New("failed parsing URL")
	}

	//build a json from the url
	jsonStr, err := buildJSONFromURLV2(parsedURL, supportedParams)
	if err != nil {
		return "", err
	}

	//create a signature
	signatureV2, err := computeHmac256(jsonStr, secret)
	if err != nil {
		fmt.Println("Failed to computeHMAC256 for url %s. err: %+v", jsonStr, err)
		return "", errors.New("fail to computeHMAC256 for url")
	}

	//add the signature to the url
	signedURL = fmt.Sprintf("%s%s%s", urlWithExpired, "&signature_v2=", signatureV2)

	return signedURL, nil

}

// this function builds a json from a given click url.
// It returns a string representation of the json ready to be signed.
func buildJSONFromURLV2(parsedURL *url.URL, supportedParams []Param) (string, error) {
	//initiate an empty json in the structure [[key-1,val-1],[key-2,val-2]...[key-n,val-n]]
	var jsonData [][2]string

	//add the url host domain to the json
	domain := parsedURL.Host
	param := [2]string{"link_domain", domain}
	jsonData = append(jsonData, param)

	//add the path (app-id or template-id) to the json
	path := parsedURL.Path
	if len(path) > 1 {
		param := [2]string{"link_path", path[1:]}
		jsonData = append(jsonData, param)
	}

	//loop over the ordered list of supported parameters and add them to the json
	for i := 0; i <len(supportedParams); i++ {name := supportedParams[i].Name val := parsedURL.Query().Get(name) if len(val) > 0 {
			param := [2]string{name, val}
			jsonData = append(jsonData, param)
		} else if supportedParams[i].Mandatory {
			return "", errors.New("missing mandatory param: " + name)
		}
	}

	//generate string representation of the json object
	jsonObj, _ := json.Marshal(jsonData)
	return strings.ToLower(string(jsonObj)), nil
}

func main() {

	supportedParams, err := LoadSupportedParams()
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}

	var secretKey = "tqJU4Qd/eFTEWfqW7KCG9asDO0bmZoFzv8GY3VPSPAM="
	var clickTtlSeconds int64 = 60
	var originalUrl = "https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012&clickid=1234&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign"

	fmt.Println("Original URL: ", originalUrl)

	signedUrl, err := signURLV2(originalUrl, secretKey, clickTtlSeconds, supportedParams)
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	} else {
		fmt.Println("Signed URL: ", signedUrl)
	}
}
```

</Accordion>

<div id="click-signature-apis" />

## API подписи кликов

AppsFlyer предоставляет API, которые позволяют рекламным сетям управлять процессом подписи кликов и тестировать его. См. список API в таблице ниже и следующие разделы с информацией, необходимой для использования API.

<div id="click-signature-apis-1" />

#### API подписи кликов

| Метод API | Примечания |
| --- | --- |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-post">Генерирование секретного ключа</Anchor> | Сгенерируйте секретные ключи для использования в подписи. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-delete">Отмена секретного ключа</Anchor> | Аннулируйте взломанные секретные ключи. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-test-post">Тест</Anchor> | Отправляйте отдельные клики для тестирования подписи. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-update-put">Настройка режима</Anchor> | Настройте режим подписи кликов:<ul><li>**отключено**  (по умолчанию): проверка подписи клика не выполнена.</li><li>**только отчеты**  (тестовый режим): AppsFlyer проверяет подписи кликов, но не блокирует клики с недействительными подписями. Рекламная сеть может использовать **API отчетов** для получения статистики по успешным/неуспешным кликам. Используйте его для тестирования подписи кликов без ущерба для производства и реального трафика.</li><li>**включено:** AppsFlyer блокирует клики с недействительными или отсутствующими подписями.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-circuit-breaker-put">Настройка автоматического выключателя</Anchor> | Настройте режим автоматического выключателя, который защищает рекламную сеть от слишком большого количества заблокированных кликов:<ul><li>**включено** (по умолчанию): если система Protect360 обнаружит, что слишком большое количество кликов помечено как недействительные, то для защиты рекламной сети от потенциально ошибочной блокировки кликов выполните следующие действия:<ul><li>Настройте режим перехода API в режим «только отчеты».</li><li>Кроме того, в рекламную сеть отправляется электронное сообщение с уведомлением, подтверждающим правильность настройки API подписи кликов.</li></ul></li><li>**выключено**: Protect360 продолжает блокировать все клики, помеченные как недействительные, даже если процент блокировки необычно высок.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-get">Получение конфигурации</Anchor> | Получайте данные о режиме и идентификаторы активных секретных ключей. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-report-get">Отчет</Anchor> | Получайте статистику по успешным и неудачным кликам, когда система работает в режиме **«только отчеты»** или **«включено»**. Используйте данные для тестирования подписи кликов без ущерба для производства и реального трафика. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-add">Исключение приложения</Anchor> | Настройте идентификаторы приложений, подлежащих исключению из подписи кликов. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-delete">Удаление исключенного приложения</Anchor> | Настройте идентификаторы приложений, которые будут включены в подпись кликов после исключения. |

<div id="legacy-versions" />

## Устаревшие версии

Эти версии не следует использовать, они приведены только для справки

<div id="v1-legacy" />

<Accordion title="V1 (устарел)">

<div id="generate-secret-key-method" />

### Метод генерирования секретного ключа

<div id="generate-secret-key-basics" />

<Accordion title="Основные сведения о генерировании секретных ключей">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>POST</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/secret?ttlHours=&lt;ttlHours&gt;</span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td>Секретный ключ возвращается в формате JSON</td></tr><tr><td> </td><td>Лимит запросов</td><td>Максимум 2 активных секретных ключа одновременно</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="Запрос API">

**Метод**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>
```

<div id="parameters" />

#### Параметры

| Параметр | Описание |
| --- | --- |
| ttlHours | <ul><li>Срок действия секретного ключа, в часах, от 1 до 1440 часов.</li><li>По умолчанию — 36 часов.</li></ul> |

</Accordion>

<div id="json-response" />

<Accordion title="Ответ JSON">

| **Ключ** | **Описание** |
| --- | --- |
| secret-key-id | Идентификатор секретного ключа |
| secret key | Секретный ключ для подписи клика |
| expiration | Отсчет времени в миллисекундах |

</Accordion>

<div id="generate-secret-key-curl-example-and-response" />

<Accordion title="Пример генерирования секретного ключа curl и ответ">

**Запрос curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=36' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Ответ JSON**

```json
{
	"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
	"secret-key": "zGW6Rhrmb8+vuhHtL/Kp6rW5Ci9PNsjH1J5MGO9SIeg=",
	"expiration": 1610533263
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="Коды ответа HTTP">

<div id="response-codes" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="revoke-secret-key-method" />

### Метод отмены секретного ключа

<div id="revoke-secrete-key-basics" />

<Accordion title="Основные сведения об отмене секретных ключей">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>DELETE</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer.<span>com/api/p360-</span>click-signing/secret/&lt;secret-id&gt;</span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td>Не указан</td></tr></tbody></table>

</Accordion>

<Accordion title="Запрос API">

**Метод**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>
```

<div id="parameters-1" />

#### Параметры

| Параметр | Описание |
| --- | --- |
| secret-id | Идентификатор секретного ключа, который нужно аннулировать |

</Accordion>

<div id="generate-secret-key-curl-example-and-response::5a4174fc" />

<Accordion title="Пример генерирования секретного ключа curl и ответ">

**Запрос curl**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/secret/59ad6547-affc-45eb-a6c9-9805f88ee755' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7dc4ee64" />

<Accordion title="Коды ответа HTTP">

<div id="response-codes-1" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="test-method" />

### Метод тестирования

<div id="test-basics" />

<Accordion title="Основные сведения о тестировании">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>POST</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/test</span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td>Возвращает в формате JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="Запрос API">

**Метод**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/test
```

<div id="parameters-2" />

#### Параметры

| Параметр | Описание |
| --- | --- |
| url | URL-адрес клика (включая подпись) для тестирования |

</Accordion>

<div id="json-response::cd966b82" />

<Accordion title="Ответ JSON">

| **Ключ** | **Описание** |
| --- | --- |
| test-status | Пройден или не пройден |
| message | Причина, по которой тест не пройден. Например:<ul><li>Отсутствующая подпись</li><li>Недопустимая подпись</li><li>Срок действия истек</li></ul> |

</Accordion>

<div id="test-curl-example-and-response" />

<Accordion title="Пример тестирования curl и ответ">

**Запрос curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/test' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "url": "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345&expires=1597657118&signature=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk"
}'
```

**Ответ JSON**

```json
{
	"test-status":"Passed / Failed",
	"message": "Invalid signature"
}
```

</Accordion>

<div id="http-response-codes::22d1011c" />

<Accordion title="Коды ответа HTTP">

<div id="response-codes-2" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="configure-mode-method" />

### Метод настройки режима

<div id="configure-mode-basics" />

<Accordion title="Основные сведения о настройке режима">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>POST</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>mode/&lt;mode&gt;</span></strong></span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td>Возвращает в формате JSON</td></tr></tbody></table>

</Accordion>

<div id="api-request::b2432cce" />

<Accordion title="Запрос API">

**Метод**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/mode/<mode>
```

<div id="parameters-3" />

#### Параметры

| Параметр | Описание |
| --- | --- |
| mode | Варианты:<ul><li>включена<br />**Внимание!** Установите режим «включено» только после нескольких часов работы в режиме «только отчеты» и проверьте отчеты, чтобы убедиться, что конфигурация верна и все клики прошли проверку подписи.</li><li>выключено</li><li>только отчеты</li></ul> |

</Accordion>

<div id="configure-mode-curl-example" />

<Accordion title="Пример настройки режима curl">

**Запрос curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/mode/report-only' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<Accordion title="Коды ответа HTTP">

<div id="response-codes-3" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | Неверный режим |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="configure-circuit-breaker-method" />

### Метод настройки автоматического выключателя

<div id="configure-circuit-breaker-basics" />

<Accordion title="Основные сведения о настройке автоматического выключателя">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>POST</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker</span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td><span>Статус HTTP</span></td></tr></tbody></table>

</Accordion>

<div id="api-request::1ede8b9c" />

<div id="api-request::ef73eae0" />

<Accordion title="Запрос API">

**Метод**

```http
POST https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker
```

<div id="request-body-json" />

#### Тело запроса JSON

| Параметр | Описание |
| --- | --- |
| status | <ul><li>включена</li><li>выключено</li></ul> |

</Accordion>

<div id="configure-circuit-breaker-curl-example-and-response" />

<Accordion title="Пример настройки автоматического выключателя curl и ответ">

**Запрос curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
--data-raw '{
"status":"enabled"
}'
```

</Accordion>

<div id="http-response-codes::b3328f8b" />

<div id="http-response-codes::d35e3a62" />

<Accordion title="Коды ответа HTTP">

<div id="response-codes-4" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Bad request | Неверный статус |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="get-configuration-method" />

### Получение метода настройки

<div id="get-configuration-basics" />

<Accordion title="Основные сведения о получении конфигурации">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>GET</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config</span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td>Возвращает в формате JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="Запрос API">

**Метод**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/config
```

</Accordion>

<div id="json-response::fee92c" />

<Accordion title="Ответ JSON">

| **Ключ** | **Описание** |
| --- | --- |
| mode | Один из следующих:<ul><li>включено</li><li>выключено</li><li>только отчеты</li></ul> |
| circuit-breaker-config | Объект JSON, содержащий **статус**, один из следующих:<ul><li>включено</li><li>выключено</li></ul> |
| active-key-ids | Массив JSON с активными ключами:<ul><li>**идентификатор секретного ключа**: случайно сгенерированный идентификатор секретного ключа</li><li>**срок действия**: отсчет срока действия секретного ключа в миллисекундах</li></ul> |
| excluded-app-ids | Массив JSON с идентификаторами исключенных приложений |

</Accordion>

<div id="get-configuration-curl-example-and-response" />

<Accordion title="Пример получения конфигурации curl и ответ">

**Запрос curl**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/config' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Ответ JSON**

```json
{
	"mode": "report-only",
	"active-key-ids": [
		{
			"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
			"expiration": 1610533263
		}
	],
	"excluded-app-ids": [
		"app-id-1", 	"app-id-2"
	]

}
```

</Accordion>

<Accordion title="Коды ответа HTTP">

<div id="response-codes-5" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="report-method" />

### Метод отчета

<div id="report-basics" />

<Accordion title="Основные сведения об отчетах">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>GET</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/report</span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td>Возвращает в формате CSV</td></tr></tbody></table>

</Accordion>

<div id="api-request::a2a93b39" />

<div id="api-request::b28cedb0" />

<Accordion title="Запрос API">

**Метод**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/report
```

<div id="parameters-4" />

#### Параметры

<table><tbody><tr><th><p>Параметр</p></th><th>Описание</th></tr><tr><td>start-date</td><td><p>Дата и время начала для отчета. Формат: yyyy-mm-ddThh</p></td></tr><tr><td>end-date</td><td><p><span>Дата и время окончания для отчета. Формат: yyyy-mm-ddThh</span></p></td></tr><tr><td colspan="2"><span>Для API требуются как дата начала, <strong>так</strong> и дата окончания, или <strong>ни одна из них</strong>. Если дата начала/окончания не указана, в отчете отображаются результаты за последние 24 часа.</span></td></tr></tbody></table>

</Accordion>

<div id="csv-response" />

<Accordion title="Ответ в формате CSV">

| **Столбец** | **Описание** |
| --- | --- |
| time | Дата и время кликов. Формат: yyyy-mm-ddThh |
| total\_clicks | Общее количество кликов за отчетный период |
| valid\_clicks | Количество действительных кликов за отчетный период |
| missing\_signature | Количество кликов с отсутствующей подписью за отчетный период |
| expired\_clicks | Количество кликов с истекшим сроком действия за отчетный период |
| invalid\_signature | Количество кликов с недействительной подписью за отчетный период |
| no\_active\_secrets | Количество кликов, отклоненных из-за отсутствия активных секретных ключей в системе (обычно когда система работает в режиме «только отчеты») |

</Accordion>

<div id="test-curl-example-and-response::66e922" />

<Accordion title="Пример тестирования curl и ответ">

**Запрос curl**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/report?start-date=2021-01-07T07&end-date=2021-01-17T12' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
```

**Ответ в формате CSV**

| **time** | **total\_clicks** | **valid\_clicks** | **missing\_signature** | **expired\_clicks** | **invalid\_signature** | **no\_active\_signatures** |
| --- | --- | --- | --- | --- | --- | --- |
| 2021-01-17T07 | 928082156 | 928082156 | 0 | 0 | 0 | 0 |
| 2021-01-17T08 | 923796132 | 923796132 | 0 | 0 | 0 | 0 |
| 2021-01-17T09 | 917541373 | 917541373 | 0 | 0 | 0 | 0 |
| 2021-01-17T10 | 909977064 | 909977064 | 0 | 0 | 0 | 0 |
| 2021-01-17T11 | 965104299 | 965104299 | 0 | 0 | 0 | 0 |
| 2021-01-17T12 | 975134824 | 975134824 | 0 | 0 | 0 | 0 |

</Accordion>

<Accordion title="Коды ответа HTTP">

<div id="response-codes-6" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="exclude-app-method" />

### Метод исключения приложения

<div id="exclude-app-method-basics" />

<Accordion title="Основные сведения о методе исключения приложения">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>POST</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>excluded-app/&lt;app-id&gt;</span></strong></span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td>Не указан</td></tr></tbody></table>

</Accordion>

<div id="api-request::1054abca" />

<Accordion title="Запрос API">

**Метод**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

#### Параметры

| Параметр | Описание |
| --- | --- |
| app-id | Идентификатор приложения, которое должно быть исключено из проверки подписи клика |

</Accordion>

<div id="exclude-app-curl-example" />

<Accordion title="Пример исключения приложения curl">

**Запрос curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::90a409c" />

<Accordion title="Коды ответа HTTP">

<div id="response-codes-7" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="remove-excluded-app-method" />

### Метод удаления исключенного приложения

<div id="remove-excluded-app-method-basics" />

<Accordion title="Основные сведения о методе удаления исключенного приложения">

<table><thead><tr><th>Категория</th><th>Элемент</th><th><p><span>Описание</span></p></th></tr></thead><tbody><tr><td rowspan="3">Запрос</td><td>HTTP-метод</td><td><code>DELETE</code></td></tr><tr><td>Путь</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>excluded-app/&lt;app-id&gt;</span></strong></span></p></td></tr><tr><td>Заголовок авторизации </td><td><ul><li>Обязательный заголовок авторизации содержит токен Bearer. </li><li>Администратор получает токен на дэшборде следующим образом:  <a href="/marketers/ru/docs/managing-appsflyer-tokens" target="_blank">Администратор переходит в выпадающий список электронной почты &gt; Токены API, чтобы получить токен V2.0</a>  </li></ul></td></tr><tr><td>Ответ</td><td>Результаты</td><td>Не указан</td></tr></tbody></table>

</Accordion>

<div id="api-request::3f5b6d35" />

<div id="api-request::9504d16f" />

<Accordion title="Запрос API">

**Метод**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-6" />

<div id="parameters-5" />

#### Параметры

| Параметр | Описание |
| --- | --- |
| app-id | Идентификатор приложения, которое должно быть удалено из списка приложений, исключенных из проверки подписи клика |

</Accordion>

<div id="remove-excluded-app-curl-example" />

<Accordion title="Пример удаления исключенного приложения curl">

**Запрос curl**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::8454f45d" />

<div id="http-response-codes::7991b66" />

<div id="http-response-codes::b5e059da" />

<Accordion title="Коды ответа HTTP">

<div id="response-codes-8" />

#### Коды ответа

| Код | Сообщение | Примечания |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Не авторизовано | Неверный или отсутствующий заголовок авторизации |

</Accordion>

<div id="code-sample" />

<Accordion title="Пример кода">

```java
package sign;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

.
.
.

String clickUrl = "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345";
String secretKey = "secret_key"; 
int ttlMinutes = 5;

//add expiration to the click URL
long expiration = System.currentTimeMillis() + (60000L * ttlMinutes);
clickUrl += "&expires="+expiration;

//create a SecretKey object from the given key string
SecretKeySpec signingKey = new SecretKeySpec(secretKey.getBytes(), "HmacSHA256");
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(signingKey);

//generate a signature from the click url and encode it with base64 without padding
String generatedSignature =     
Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(clickUrl.getBytes()));

//add the signature to the click URL
String signedClickUrl = clickUrl + "&signature=" + generatedSignature;
```

</Accordion>

</Accordion>

<div id="additional-information" />

## Дополнительные сведения

<div id="troubleshooting" />

<Accordion title="Устранение неполадок">

AppsFlyer прекращает проверку подписи кликов и возвращается в режим «только отчеты», когда более 90% кликов за час не проходят проверку подписи.

Это необходимо для защиты вашего бизнеса от потенциальных технических проблем и позволяет найти причину  аномалии:

* Если вы считаете, что подпись работает должным образом, а клики блокируются правильно, отключите автоматический выключатель, используя [метод настройки автоматического выключателя](/docs/click-signing-for-ad-networks#метод-настройки-автоматического-выключателя).
* Если вы считаете, что клики блокируются неправильно:
  1. Убедитесь, что у вас есть действительный секретный ключ, проверив настройку подписи кликов с помощью [метода получения конфигурации.](/docs/click-signing-for-ad-networks#получение-метода-настройки)
  2. Используйте [отчет о подписи кликов](/docs/click-signing-for-ad-networks#метод-отчета), чтобы получить дополнительную информацию о заблокированных кликах и изучить источники (идентификаторы агентств/приложений) и причины недействительных кликов.
* Если вы обнаружили проблему с конкретным приложением из-за нестандартной интеграции, исключите это приложение из проверки подписи кликов с помощью [API исключения приложений.](/docs/click-signing-for-ad-networks#метод-исключения-приложения)
* Если вы обнаружили проблему с конфигурацией, выполните следующие действия:
  1. Продолжите работу в режиме «только отчеты».
  2. Внесите исправления в процесс подписи кликов со своей стороны.
  3. Проверьте результаты в отчете по подписи кликов  [и повторно](/docs/click-signing-for-ad-networks#метод-отчета) включите проверку подписи кликов, когда увидите, что проверка кликов происходит должным образом.

</Accordion>

<div id="faq" />

<Accordion title="Вопросы и ответы">

| **В: Как протестировать подпись кликов без ущерба для производства?**<br /><br />**О**: Есть два способа тестирования подписи кликов:<ol><li>Используйте [API для тестирования](/docs/click-signing-for-ad-networks#метод-тестирования). Этот метод полезен на этапе разработки для тестирования подписей одиночных кликов.</li><li>Используйте режим «только отчеты». Режим «только отчеты» проверяет подписи кликов и показывает, какие клики можно заблокировать, но не блокирует недействительные клики. Таким образом, вы можете проверить, работает ли подпись кликов без ущерба для реального трафика.</li></ol> |
| --- |
| **В: В чем разница между токеном API и секретным ключом?**<br /><br />**О**: **Токен API**: Используется для авторизации и запуска API подписи кликов. В каждой рекламной сети есть только один. <Anchor target="_blank" href="/marketers/ru/docs/managing-appsflyer-tokens">Токен AppsFlyer API V2.0</Anchor> нужно получить у администратора<br /><br />**Секретный ключ**: Используется для генерирования подписи. Используйте [метод генерирования секретного ключа](/docs/click-signing-for-ad-networks#метод-генерирования-секретного-ключа) для создания секретных ключей. Рекламная сеть отвечает за генерирование новых секретных ключей. См. [раздел «Особенности»](/docs/click-signing-for-ad-networks#traits) для получения дополнительной информации. |
| **В: Подпись кликов можно применять только к определенным кампаниям?**<br /><br />**О**: Нет. Подпись кликов применяется ко всем кликам в рекламной сети. Можно исключить определенные приложения из подписи кликов, но нельзя исключать только определенные кампании. |

</Accordion>

<div id="traits" />

<Accordion title="Особенности">

| Специфика | Описание |
| --- | --- |
| Подпись клика | Подпись должна происходить на серверах рекламной сети. |
| Секретный ключ | <ul><li>В рекламных сетях могут быть одновременно активны не более двух секретных ключей.</li><li>Срок действия каждого секретного ключа ограничен.</li><li>Клики, подписанные с использованием секретных ключей с истекшим сроком действия, отклоняются.</li></ul> |
| API отчетов | Обновленная статистика по проверке кликов агрегируется ежечасно. |

</Accordion>

<div data-zendesk-anchors="about-click-signing=%D0%BE-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2 h_01HNWC70BPGDJAG3X8M5Z2RHQ4=%D0%BE-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2 click-signature-integration=%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2 h_01HNWC70BPFYMZ56GTPV3W6DXA=%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2 flow=%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9 h_01HNWC70BPMXTKF9NZBYGCB874=%D1%81%D1%86%D0%B5%D0%BD%D0%B0%D1%80%D0%B8%D0%B9 procedure=%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D0%B0 h_01HNWC70BPHCAGD1ECA56CC1Q6=%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D0%B4%D1%83%D1%80%D0%B0 h_01HNWC70BPAR4QNTNSFE1JZM2J=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 list-of-attributes=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%B0 h_01HP4A42YYFFF6M4VEH84KRTTK=%D1%81%D0%BE%D0%B7%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%B0 h_01HNWD3XYWFRY262HZZVAVWACR=%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%BE%D0%B2 attribute-rules=%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-json h_01HNWE3A19RM7757B707TWZ6G0=%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-json order-and-appearance-of-attributes=%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA-%D0%B8-%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%B9-%D0%B2%D0%B8%D0%B4-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%BE%D0%B2 h_01HNWE3A1920YQGZX2VG4X3M4B=%D0%BF%D0%BE%D1%80%D1%8F%D0%B4%D0%BE%D0%BA-%D0%B8-%D0%B2%D0%BD%D0%B5%D1%88%D0%BD%D0%B8%D0%B9-%D0%B2%D0%B8%D0%B4-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%BE%D0%B2 empty-attributes=%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%B5-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B h_01HNYRZ1DPDDQ5H8RFYKAQWVKP=%D0%BF%D1%83%D1%81%D1%82%D1%8B%D0%B5-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D1%8B json-data-structure=%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-json h_01HNYS6R7F0MNPBN08TXKQS5DV=%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D1%83%D1%80%D0%B0-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-json attribute-value-escaping=%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%B0 h_01HNYSEBGD1DBSV2MHS7DZ75HS=%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%82%D0%B0 json-spaces=%D0%BF%D1%80%D0%BE%D0%B1%D0%B5%D0%BB%D1%8B-json h_01HNYSY42HS1RXFG7T7QS9B0TK=%D0%BF%D1%80%D0%BE%D0%B1%D0%B5%D0%BB%D1%8B-json signature-algorithm=%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8 h_01HNYSJDFWAM9RREYH4M8DZQJA=%D0%B0%D0%BB%D0%B3%D0%BE%D1%80%D0%B8%D1%82%D0%BC-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8 signature-example=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8 h_01HP3YAN03BWVA30JP1JAFZYAG=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8 h_01HP3Y2Z65BN0SZ56XSHD52MSY=building-a-signature-example code-example=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BA%D0%BE%D0%B4%D0%B0 h_01HNYT8Z33M69JAS72MQ03YX0M=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%80%D1%8B-%D0%BA%D0%BE%D0%B4%D0%B0 h_01HP3XVEJTBBVKZYEBZT62PR20=signingsupportedparamsjson h_01HP3XVEJTWWJVDBK5PGQH7DJY=signatureexamplego click-signature-apis=api-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2 h_01HNWC70BPNEVT00S040TQ9KVD=api-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2 click-signature-apis::58bf03c7=api-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2-1 h_01HNWC70BPR8XXC3TQCAZSGFZS=api-%D0%BF%D0%BE%D0%B4%D0%BF%D0%B8%D1%81%D0%B8-%D0%BA%D0%BB%D0%B8%D0%BA%D0%BE%D0%B2-1 legacy-versions=%D1%83%D1%81%D1%82%D0%B0%D1%80%D0%B5%D0%B2%D1%88%D0%B8%D0%B5-%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8 h_01HNZ3YMFRWFDY751EBA58V6Q0=%D1%83%D1%81%D1%82%D0%B0%D1%80%D0%B5%D0%B2%D1%88%D0%B8%D0%B5-%D0%B2%D0%B5%D1%80%D1%81%D0%B8%D0%B8 h_01HNWCYB2YXCVGCP38GRBAJYQ4=v1-legacy generate-secret-key-method=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0 h_01HNWC70BPBPSX1WKJJC2W6H69=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%B3%D0%B5%D0%BD%D0%B5%D1%80%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D1%81%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0 h_01HNWC70BPPBK2S38KA6RQSTCN=generate-secret-key-basics h_01HNWC70BP40D5XN8DZQHSDZ5K=api-request parameters=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B h_01HNWC70BPS83JD78JWQYK1NX9=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B h_01HNWC70BPQC37602GV8GQPSEQ=json-response h_01HNWC70BP7V8KRW4861PXC2PX=generate-secret-key-curl-example-and-response h_01HNWC70BPKTPZEKFD37B6YQMH=http-response-codes response-codes=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0 h_01HNWC70BPMQ8Q94JD5CBT5RHZ=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0 revoke-secret-key-method=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%BE%D1%82%D0%BC%D0%B5%D0%BD%D1%8B-%D1%81%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0 h_01HNWC70BP8V05Q04J6EVGAS9T=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%BE%D1%82%D0%BC%D0%B5%D0%BD%D1%8B-%D1%81%D0%B5%D0%BA%D1%80%D0%B5%D1%82%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BA%D0%BB%D1%8E%D1%87%D0%B0 h_01HNWC70BP69ZJERY1Z03A5V4C=revoke-secrete-key-basics h_01HNWC70BPN01BNKKC7T9QMF44=api-request::3f5b6d35 parameters::f8e4d5cf=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-1 h_01HNWC70BPQ5S06E210RTE7E6R=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-1 h_01HNWC70BPBQA0ME8D6TZEM2EB=generate-secret-key-curl-example-and-response::5a4174fc h_01HNWC70BP9AV6PPEZNPQWJN85=http-response-codes::7dc4ee64 response-codes::d802debd=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-1 h_01HNWC70BPN18MB98KWND886QN=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-1 test-method=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F h_01HNWC70BPKEVRDMT8N4HMC98W=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F h_01HNWC70BPX4TH2MNE4GJBGHRG=test-basics h_01HNWC70BP5X2MZ3AC8BF69XYK=api-request::b2432cce parameters::7d3f0c33=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-2 h_01HNWC70BPKQFVEGWR9QT566YX=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-2 h_01HNWC70BPM50T2JEGJF41GGX4=json-response::cd966b82 h_01HNWC70BPSQYQ5R7PJE4CAKYG=test-curl-example-and-response h_01HNWC70BP8SSK2E5DFAD2Q6NP=http-response-codes::22d1011c response-codes::a79c47f4=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-2 h_01HNWC70BPC43F5H85F56DDSQR=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-2 configure-mode-method=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B0 h_01HNWC70BP6NPF7NSF0MGA4BJ3=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8-%D1%80%D0%B5%D0%B6%D0%B8%D0%BC%D0%B0 h_01HNWC70BPKNAVCD57D2E7FX8F=configure-mode-basics h_01HNWC70BQFCJCHHVQHKWB57GF=api-request::1ede8b9c parameters::2fff2a1b=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-3 h_01HNWC70BQSQ7YWZVQB9A4DZQW=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-3 h_01HNWC70BQF0J2TZF181BW0MKT=configure-mode-curl-example h_01HNWC70BQ9HNQV7HA45ZXA2Z3=http-response-codes::b3328f8b response-codes::fe5a5b10=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-3 h_01HNWC70BQZ657X25N8JGM57A1=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-3 configure-circuit-breaker-method=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8-%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-%D0%B2%D1%8B%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8F h_01HNWC70BQVSFS7G330NF4XHEP=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8-%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%B0%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B3%D0%BE-%D0%B2%D1%8B%D0%BA%D0%BB%D1%8E%D1%87%D0%B0%D1%82%D0%B5%D0%BB%D1%8F h_01HNWC70BQ097J2VXW0XKSH3M9=configure-circuit-breaker-basics h_01HNWC70BQJWZYZEDJJ5J7JX6X=api-request::ef73eae0 request-body-json=%D1%82%D0%B5%D0%BB%D0%BE-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0-json h_01HNWC70BQ6R955776Y6H4EZRG=%D1%82%D0%B5%D0%BB%D0%BE-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D0%B0-json h_01HNWC70BQRZEZ4PTV59FGYS4Z=configure-circuit-breaker-curl-example-and-response h_01HNWC70BQPP5X9JH1HJ1K58H4=http-response-codes::d35e3a62 response-codes::b056f2a3=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-4 h_01HNWC70BQWQ5KWZX8BM0A7BC5=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-4 get-configuration-method=%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%B0-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8 h_01HNWC70BQZY6TYSQBWZ17S0W5=%D0%BF%D0%BE%D0%BB%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BC%D0%B5%D1%82%D0%BE%D0%B4%D0%B0-%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B8 h_01HNWC70BQY6CPZA5A56J3TET0=get-configuration-basics h_01HNWC70BQ444XNRRCZZH2GFJH=api-request::a2a93b39 h_01HNWC70BQJ8J2WGXE2QF144FK=json-response::fee92c h_01HNWC70BQ701HZR6PYC0CW88T=get-configuration-curl-example-and-response h_01HNWC70BQ8R5GR906Y9W79E81=http-response-codes::90a409c response-codes::ebf1292a=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-7 h_01HNWC70BQDGVBZ94F0N49FF40=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-7 report-method=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0 h_01HNWC70BQTBMNKHV4RH4ZQ0AE=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%B0 h_01HNWC70BQ4K7T3FXZWV5KW3FM=report-basics h_01HNWC70BQMBD2WNVQH69FMSPR=api-request::b28cedb0 parameters::e6795217=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-4 h_01HNWC70BQ0FDT4T2RAJEPAHNC=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-4 h_01HNWC70BQRZTXMKD30V7QQPE4=csv-response h_01HNWC70BQV61TVE65TQ3WWGCP=test-curl-example-and-response::66e922 h_01HNWC70BQQ3MP256QK0JT2K78=http-response-codes::8454f45d response-codes::a8a9822d=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-8 h_01HNWC70BQTPPWA4SNG25E8FFB=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-8 exclude-app-method=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01HNWC70BQ9SK2XCBGGHXVMRDV=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%B8%D1%8F-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01HNWC70BQ8GGRTQ1RW1KCY0SQ=exclude-app-method-basics h_01HNWC70BQ4D62SZCHKGEP6RMJ=api-request::1054abca parameters::f5e3c6ce=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-6 h_01HNWC70BREG4XQJV3X9518FC5=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-6 h_01HNWC70BR2PVDHTG64WZ36KPV=exclude-app-curl-example h_01HNWC70BR7XCTW6N69GEB4ARF=http-response-codes::7991b66 response-codes::addfcfd8=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-8 h_01HNWC70BRN8BHWF6WGY2RH45X=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-8 remove-excluded-app-method=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01HNWC70BR18P0H96VN64RS05G=%D0%BC%D0%B5%D1%82%D0%BE%D0%B4-%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F-%D0%B8%D1%81%D0%BA%D0%BB%D1%8E%D1%87%D0%B5%D0%BD%D0%BD%D0%BE%D0%B3%D0%BE-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D1%8F h_01HNWC70BRAWBGC5EE0Q8XBTW1=remove-excluded-app-method-basics h_01HNWC70BRD885KN6YDXQ9GXS2=api-request::9504d16f parameters::34936c8f=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-6 h_01HNWC70BR4ADH7T3AFG58FZH6=%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-6 h_01HNWC70BRK7DM7MW150AFVKG2=remove-excluded-app-curl-example h_01HNWC70BRMFN4RM65YV2NWR29=http-response-codes::b5e059da response-codes::e8de940a=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-8 h_01HNWC70BRHA8AA7ZV1R4EBYJH=%D0%BA%D0%BE%D0%B4%D1%8B-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D0%B0-8 h_01HNWC70BRTZZWME7QCP8HV9AY=code-sample additional-information=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F h_01HNWC70BRN0NGTQVWED6VG81Y=%D0%B4%D0%BE%D0%BF%D0%BE%D0%BB%D0%BD%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D1%81%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D1%8F h_01HNWC70BRS884G8RCMAPFPV1N=troubleshooting h_01HNWC70BRP3BVJSHSD1CPCB9S=faq h_01HNWC70BRDN37MBTEKT0DH8CT=traits" />
