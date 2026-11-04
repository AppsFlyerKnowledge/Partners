---
title: Firma de clics para redes de publicidad
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
  edited_at: '2026-08-12T12:28:21Z'
  id: 360017831497
  locale: es
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/es/articles/360017831497
---
> **De un vistazo:** Agrega la validación de firma a los clics para evitar responsabilidades por fraude y para que los clics fraudulentos no se atribuyan a tu red de publicidad.

<div id="about-click-signing" />

## Acerca de la firma de clics

Con un mínimo de tecnología, los estafadores pueden enviar clics en nombre de una red de publicidad y crear miles, o incluso millones, de clics falsos que se envían a AppsFlyer. A veces, las propias redes de publicidad no son conscientes del problema.

Para que una red de publicidad se asegure de que los clics que AppsFlyer le atribuye proceden realmente de la red de publicidad y no de un estafador que crea clics falsos, las redes de publicidad deben firmar sus clics con firmas <Anchor target="_blank" href="https://en.wikipedia.org/wiki/HMAC">HMAC-SHA256</Anchor>.

La firma de clics también evita que el tráfico de la red de publicidad se bloquee debido a inundaciones de clics. Esto significa que si una red publicidad alcanza el umbral de bloqueo de clics debido a un nivel extremo de inundación de clics, AppsFlyer deja de registrar y atribuir sus clics durante el resto del día .

Las firmas permiten que AppsFlyer valide los clics y asegurarse de que la información de clics no haya sido manipulada por estafadores.

* Los clics validados se registran y se atribuyen a la red de publicidad
* Los clics invalidados se rechazan y:
  * Están disponibles en los reportes de Protect360 para las redes de publicidad (no para los anunciantes). <Anchor target="_blank" href="/partners/es/docs/protect360-reports-for-ad-networks#failed-click-signatures">Saber más</Anchor>
  * No afectan la tasa de conversión ni el umbral de bloqueo de clics de la red de publicidad

<div id="click-signature-integration" />

## Integración de la firma clic

<div id="flow" />

### Flujo

El siguiente gráfico describe el flujo desde el desarrollo inicial y las pruebas básicas hasta las pruebas de producción y, por último, hasta la producción.

![Click_signing_integration_flow.png](https://files.readme.io/3bc0103090535c22db027fb09f72ad89d88210bba8f2b6f43d1166c2911d71cd-360017572558.png)

<div id="procedure" />

### Procedimiento

curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/report?start-date=2021-01-07T07&end-date=2021-01-17T12' \ -H 'Authorization: Bearer `{API V2.0 token available to the admin in the dashboard.}`' \

**Para firmar tus clics**:

1. Genera una clave secreta con la API Generar clave secreta.  
   ¡Práctica recomendada!/span> Genera y utiliza una nueva clave secreta cada 24 horas, con una caducidad de 36 horas.
2. Desarrolla el código en tus servidores que llame a la API Generar clave secreta, tome la clave secreta y genere una firma HMAC-SHA256. Ver ejemplo de código.  
    Ver ejemplo de código.  
   Puedes usar las otras API como se describe en la siguiente tabla.
3. El código añade lo siguiente a las URL de tus clics:
   * Un parámetro de **caducidad** que contiene una marca de tiempo Unix (en UTC) después de la cual la red de publicidad no reclama el clic.
   * La firma HMAC-SHA256.  
     Ejemplo:

     ```http
     https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_siteid=12345&expires=1597657118&signature_v2=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk
     ```

<div id="note" />

> 📘 **Nota**
>
> Asegúrate de que cualquier codificación URL de caracteres especiales o espacios en tu enlace se produce antes de que se genere la firma de clic. Generar primero la firma provoca un fallo en la verificación.

<div id="creating-a-click-signature" />

## Crear una firma de clic

Para crear una firma de clic debes:

1. Construir un JSON utilizando la lista de atributos y reglas JSON que se indican a continuación
2. Crear la firma a partir de este JSON utilizando HMAC56

<div id="list-of-attributes" />

### Lista de atributos

La siguiente lista de atributos es compatible con la firma por clic y engagement.

| Orden | Parámetro | Obligatorio | Notas |
| --- | --- | --- | --- |
| 1 | link\_domain | Sí | El dominio de la URL de clic Por ejemplo:<ul><li>app.appsflyer.com</li><li>myapp.onelink.me</li><li>click.mycustomdomain.com</li></ul> |
| 2 | link\_path | Sí | La ruta de la URL del clic sin incluir una barra invertida inicial.  <br />**app-id** para enlaces de plataforma única o **template-id** para OneLink |
| 3 | PID | Sí |  |
| 4 | af\_prt | No |  |
| 5 | af\_siteid | Sí |  |
| 6 | clickid | Sí | Un identificador único de un solo uso del clic |
| 7 | desactivado | Sí | pulsa en caducidad |
| 8 | af\_engagement\_type | No |  |
| 9 | af\_click\_lookback | No |  |
| 10 | af\_viewthrough\_lookback | No |  |
| 11 | af\_ventana\_de\_reengagement | No |  |
| 12 | es\_retargeting | No |  |
| 13 | af\_ip | No |  |
| 14 | advertising\_id | No |  |
| 15 | oaid | No |  |
| 16 | fire\_advertising\_id | No |  |
| 17 | idfa | No |  |
| 18 | idfv | No |  |

<div id="attribute-and-json-rules" />

### Reglas de atributos y JSON

<div id="order-and-appearance-of-attributes" />

#### Orden y apariencia de los atributos

* Los parámetros admitidos en la URL de engagement con un valor deben estar en el JSON
* Los atributos deben figurar en el JSON en el orden indicado en la tabla anterior

<div id="empty-attributes" />

#### Atributos vacíos

* Los atributos listados en el JSON no pueden ser valores vacíos o contener sólo espacios

<div id="json-data-structure" />

#### Estructura de datos JSON

* La estructura de datos JSON debe ser una matriz de atributos
  * Cada atributo tendrá el formato ["key", "value"].  
     Ejemplo:   
    `[["key-1","value-1"],["key-2","value-2"]...["key-n","value-n"]]`

<div id="attribute-value-escaping" />

#### Escape de valores de atributos

* Los valores del JSON deben escribirse en **minúsculas**, tal y como se define en el <Anchor target="_blank" href="https://www.w3docs.com/snippets/java/how-should-i-escape-strings-in-json.html">estándar JSON</Anchor>.

<div id="json-spaces" />

#### Espacios JSON

* El JSON debe estar compactado. No debe contener espacios en blanco, tabuladores ni caracteres de nueva línea entre los valores.

<div id="signature-algorithm" />

#### Algoritmo de firma

* Utiliza HmacSHA256 con la clave secreta para crear la firma para el JSON
* Codificar la firma con Base64 **sin** relleno
* Añadir la firma a la URL de clic con un parámetro signature\_v2

```json
//genera una firma a partir de la URL de clic y la codifica con base64 sin relleno String generatedSignature = Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(jsonString.getBytes()));
```

<div id="signature-example" />

### Ejemplo de firma

<div id="building-a-signature-example" />

<Accordion title="Construir un ejemplo de firma">

Ejemplo de URL de clic en OneLink (multiplataforma):

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&clickid=sdkfjasksjskdfj9845weh&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615
```

Ejemplo de objeto json para la firma (antes de eliminar los espacios en blanco):

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

Ejemplo de objeto json para la firma (tras eliminar los espacios en blanco)

```json
[["link_domain","yourbrand.onelink.me"],["link_path","qswl"],["pid","mediasource_int"],["template-id","qswl"],["af_siteid","my_site"],["clickid","12345"],["expires","1689695615"]]
```

URL del clic final con la firma:

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615  
&signature_v2=WIfCmfLAPSsVrBTqCqfihMeLCnbE4dIAlhHF84WsiWA
```

</Accordion>

<div id="code-examples" />

### Ejemplos de código

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
	jsonFile, _ := os. Open(path)
	defer jsonFile. Close()
	byteValue, err := io. ReadAll(jsonFile)
	if err != nil {
		return nil, errors. New("failed loading " + path)
	}
	var params []Param
	_ = json. Unmarshal(byteValue, &params)
	return params, nil
}

func computeHmac256(message, secret string) (res string, errResult error) {
	defer func() {
		if r := recover(); r != nil {
			errResult = r.(error)
			fmt. Println("failed to invoke ComputeHmac256. err: %+v", errResult)
			res = ""
			return
		}
	}()

	key := []byte(secret)
	h := hmac. New(sha256.New, key)
	h. Write([]byte(message))
	return base64.URLEncoding.WithPadding(base64.NoPadding).EncodeToString(h.Sum(nil)), nil
}

// this function accepts a click url, a ttl for the click in seconds, and the list of supported params
// the function:
// 1. añade la caducidad al clic en función del ttl proporcionado
// 2. crea un json para la firma
// 3. crea una firma HMAC256
// 4. adds the signature to the click url
func signURLV2(originalURL string, secret string, clickTtlSeconds int64, supportedParams []Param) (signedURL string, err error) {

	//add an expiration to the click
	expires := time. Now().UTC().Unix() + clickTtlSeconds
	urlWithExpired := fmt. Sprintf("%s%s%d", originalURL, "&expires=", expires)

	//parse the url
	parsedURL, err := url. Parse(urlWithExpired)
	if err != nil {
		return "", errors. New("failed parsing URL")
	}

	//build a json from the url
	jsonStr, err := buildJSONFromURLV2(parsedURL, supportedParams)
	if err != nil {
		return "", err
	}

	//create a signature
	signatureV2, err := computeHmac256(jsonStr, secret)
	if err != nil {
		fmt. Println("Failed to computeHMAC256 for url %s. err: %+v", jsonStr, err)
		return "", errors. New("fail to computeHMAC256 for url")
	}

	//add the signature to the url
	signedURL = fmt. Sprintf("%s%s%s", urlWithExpired, "&signature_v2=", signatureV2)

	return signedURL, nil

}

// this function builds a json from a given click url.
// Devuelve una representación en cadena del json lista para firmarse.
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
			return "", errors. New("missing mandatory param: " + name)
		}
	}

	//generate string representation of the json object
	jsonObj, _ := json. Marshal(jsonData)
	return strings. ToLower(string(jsonObj)), nil
}

func main() {

	supportedParams, err := LoadSupportedParams()
	if err != nil {
		fmt. Println("Error: ", err)
		os. Exit(1)
	}

	var secretKey = "tqJU4Qd/eFTEWfqW7KCG9asDO0bmZoFzv8GY3VPSPAM="
	var clickTtlSeconds int64 = 60
	var originalUrl = "https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012&clickid=1234&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign"

	fmt.
```

</Accordion>

<div id="click-signature-apis" />

## API de firma por clic

AppsFlyer proporciona API que permiten a las redes de publicidad gestionar y probar el proceso de firma de clics. Consulta la lista de API en la tabla siguiente y las secciones que siguen con la información necesaria para utilizar la API. 

<div id="click-signature-apis-1" />

#### API de firma por clic

| Método API | Observaciones |
| --- | --- |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-post">Generar clave secreta</Anchor> | Generar las claves secretas que se utilizarán en la firma. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-delete">Revocar la clave secreta</Anchor> | Anular las claves secretas comprometidas. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-test-post">Prueba</Anchor> | Enviar clics individuales para probar la firma. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-update-put">Configurar modo</Anchor> | Configurar el modo de firma de clic:<ul><li>**Requisito previo:** <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">Token de la API V2.0</Anchor> del administrador para autorizar la API de firma de clics.</li><li>**sólo reporte** (modo de prueba): AppsFlyer valida las firmas de los clics, pero no bloquea los clics con firmas no válidas. La red de publicidad puede utilizar la **API de reportes** para obtener estadísticas sobre clics acertados/fallidos. Utilízalo para probar la firma de clics sin afectar a la producción ni al tráfico real.</li><li>**habilitado:** AppsFlyer bloquea los clics con firmas no válidas o ausentes.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-circuit-breaker-put">Configurar disyuntor</Anchor> | Configura el modo del disyuntor que protege la red de publicidad de tener demasiados clics bloqueados:<ul><li>habilitada<br />**Nota:** establece el modo "activado sólo después de ejecutar el modo de sólo reportes durante unas horas y comprueba tus reportes para asegurarte de que la configuración es correcta y de que todos los clics han pasado la validación de firmas.<ul><li>La API de modo de configuración cambia a sólo reporte.</li><li>Y se envía una alerta por correo electrónico a la red de publicidad para verificar que la API de firma de clics está correctamente configurada.</li></ul></li><li>**desactivado**: Protect360 sigue bloqueando todos los clics marcados como no válidos, incluso cuando el porcentaje de bloqueo es inusualmente alto.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-get">Obtener configuración</Anchor> | Obtén el modo y los ID de las claves secretas activas. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-report-get">Reporte</Anchor> | Obtén las estadísticas sobre clics correctos y fallidos cuando el sistema esté en modo de **sólo reporte** o **activado**. Utilízalo para probar la firma de clics sin afectar a la producción ni al tráfico real. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-add">Excluir aplicación</Anchor> | Configura los ID de aplicación que se excluirán de la firma por clic. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-delete">Eliminar la aplicación excluida</Anchor> | Configura los ID de aplicación para que se incluyan en la firma por clic después de haber sido excluidos. |

<div id="legacy-versions" />

## Versiones heredadas

Estas versiones no deben utilizarse y se enumeran únicamente a título de referencia

<div id="v1-legacy" />

<Accordion title="V1: heredado">

<div id="generate-secret-key-method" />

### Método de generación de clave secreta

<div id="generate-secret-key-basics" />

<Accordion title="Generar clave secreta básica">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Ruta</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>"}</code></span></td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td>La clave secreta se devuelve en un JSON</td></tr><tr><td> </td><td>Límite de solicitud</td><td>Máximo de 2 claves secretas activas a la vez</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="Solicitud API">

**Método**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>
```

<div id="parameters" />

#### Parámetros

| Parámetro | Descripción |
| --- | --- |
| ttlHours | <ul><li>Tiempo de vida para la clave secreta, en horas, de 1-1440 horas.</li><li>El valor predeterminado es de 36 horas.</li></ul> |

</Accordion>

<div id="json-response" />

<Accordion title="Respuesta JSON">

| **Clave** | **Descripción** |
| --- | --- |
| secret-key-id | Un ID para la clave secreta |
| Clave secreta | La clave secreta para la firma clic |
| caducidad | Tiempo en milisegundos |

</Accordion>

<div id="generate-secret-key-curl-example-and-response" />

<Accordion title="Generar clave secreta curl ejemplo y respuesta">

**Solicitud de curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=36' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Respuesta JSON**

```json
{
	"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
	"secret-key": "zGW6Rhrmb8+vuhHtL/Kp6rW5Ci9PNsjH1J5MGO9SIeg=",
	"expiration": 1610533263
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="revoke-secret-key-method" />

### Método de revocación de la clave secreta

<div id="revoke-secrete-key-basics" />

<Accordion title="Revocar clave secreta básica">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>ELIMINAR</code></td></tr><tr><td>Ruta</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>"}</code></span></td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td>Vacío</td></tr></tbody></table>

</Accordion>

<Accordion title="Solicitud API">

**Método**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>
```

<div id="parameters-1" />

#### Parámetros

| Parámetro | Descripción |
| --- | --- |
| secret-id | ID de la clave secreta que se va a revocar |

</Accordion>

<div id="generate-secret-key-curl-example-and-response::5a4174fc" />

<Accordion title="Generar clave secreta curl ejemplo y respuesta">

**Solicitud de curl**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/secret/59ad6547-affc-45eb-a6c9-9805f88ee755' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7dc4ee64" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes-1" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="test-method" />

### Método de prueba

<div id="test-basics" />

<Accordion title="Conceptos básicos">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Ruta</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/test</span></td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td>Devuelve en un JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="Solicitud API">

**Método**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/test
```

<div id="parameters-2" />

#### Parámetros

| Parámetro | Descripción |
| --- | --- |
| URL | La URL del clic (incluida la firma) que se va a probar |

</Accordion>

<div id="json-response::cd966b82" />

<Accordion title="Respuesta JSON">

| **Clave** | **Descripción** |
| --- | --- |
| test-status | Aprobado o fallido |
| mensaje | Motivo del fallo de la prueba. Por ejemplo,<ul><li>Ausencia de firma</li><li>Firma inválida</li><li>Caducado</li></ul> |

</Accordion>

<div id="test-curl-example-and-response" />

<Accordion title="Ejemplo de curl de prueba y respuesta">

**Solicitud de curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/test' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "url": "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345&expires=1597657118&signature=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk"
}'
```

**Respuesta JSON**

```json
{
	"test-status":"Passed / Failed",
	"message": "Firma no válida"
}
```

</Accordion>

<div id="http-response-codes::22d1011c" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes-2" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="configure-mode-method" />

### Configurar método de modo

<div id="configure-mode-basics" />

<Accordion title="Configuración básica del modo">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Ruta</td><td> https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>mode/&lt;mode&gt;</span></strong> </td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td>Devuelve en un JSON</td></tr></tbody></table>

</Accordion>

<div id="api-request::b2432cce" />

<Accordion title="Solicitud API">

**Método**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/mode/<mode>
```

<div id="parameters-3" />

#### Parámetros

| Parámetro | Descripción |
| --- | --- |
| Modo | Opciones:<ul><li>**activado** (por defecto): establece el modo "activado sólo después de ejecutar el modo de sólo reportes durante unas horas y comprueba tus reportes para asegurarte de que la configuración es correcta y de que todos los clics han pasado la validación de firmas.</li><li>deshabilitada</li><li>sólo reporte</li></ul> |

</Accordion>

<div id="configure-mode-curl-example" />

<Accordion title="Ejemplo de configuración del modo curl">

**Solicitud de curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/mode/report-only' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::b3328f8b" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes-3" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 400 | Solicitud incorrecta | Modo no válido |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="configure-circuit-breaker-method" />

### Configurar el método del disyuntor

<div id="configure-circuit-breaker-basics" />

<Accordion title="Configuración básica de disyuntores">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Ruta</td><td><span>https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker</span></td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td><span>Estado HTTP</span></td></tr></tbody></table>

</Accordion>

<div id="api-request::1ede8b9c" />

<div id="api-request::ef73eae0" />

<Accordion title="Solicitud API">

**Método**

```http
POST https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker
```

<div id="request-body-json" />

#### Cuerpo de la solicitud JSON

| Parámetro | Descripción |
| --- | --- |
| Estado | <ul><li>habilitada</li><li>deshabilitada</li></ul> |

</Accordion>

<div id="configure-circuit-breaker-curl-example-and-response" />

<Accordion title="Configurar disyuntor curl ejemplo y respuesta">

**Solicitud de curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
--data-raw '{
"status":"enabled"
}'
```

</Accordion>

<div id="http-response-codes::d35e3a62" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes-4" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 400 | Solicitud incorrecta | Estado no válido |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="get-configuration-method" />

### Obtener método de configuración

<div id="get-configuration-basics" />

<Accordion title="Obtener la configuración básica">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>GET</code></td></tr><tr><td>Ruta</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config</span></td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td>Devuelve en un JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="Solicitud API">

**Método**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/config
```

</Accordion>

<div id="json-response::fee92c" />

<Accordion title="Respuesta JSON">

| **Clave** | **Descripción** |
| --- | --- |
| Modo | Uno de:<ul><li>habilitada</li><li>deshabilitada</li><li>sólo reporte</li></ul> |
| circuit-breaker-config | Un objeto JSON que contiene el **estado**, uno de:<ul><li>habilitada</li><li>**desactivado** (por defecto):</li></ul> |
| active-key-ids | Una matriz JSON que contiene las claves activas:<ul><li>**secret-key-id**: ID generado aleatoriamente de la clave secreta</li><li>**caducidad**: tiempo en milisegundos de la clave secreta</li></ul> |
| excluded-app-ids | Una matriz JSON con ID de aplicaciones excluidas |

</Accordion>

<div id="get-configuration-curl-example-and-response" />

<Accordion title="Obtener configuración curl ejemplo y respuesta">

**Solicitud de curl**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/config' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Respuesta JSON**

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

<div id="http-response-codes::90a409c" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes-5" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="report-method" />

### Método de reporte

<div id="report-basics" />

<Accordion title="Informe básico">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>GET</code></td></tr><tr><td>Ruta</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/report</span></td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td>Devuelve en un CSV</td></tr></tbody></table>

</Accordion>

<div id="api-request::a2a93b39" />

<div id="api-request::b28cedb0" />

<Accordion title="Solicitud API">

**Método**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/report
```

<div id="parameters-4" />

#### Parámetros

<table><thead><tr><th>Parámetro</th><th>Descripción</th></tr></thead><tbody><tr><td>start_date</td><td>Fecha y hora de inicio del reporte. Formato: aaaa-mm-dd</td></tr><tr><td>Fecha de finalización</td><td><span>Fecha y hora de finalización del reporte. Formato: aaaa-mm-dd</span></td></tr><tr><td colspan="2"><span>La API requiere <strong>tanto</strong> start-date como end-date o <strong>ninguna</strong> de las dos. Si no se indican las fechas de inicio y fin, el reporte mostrará los resultados de las últimas 24 horas.</span></td></tr></tbody></table>

</Accordion>

<div id="csv-response" />

<Accordion title="Respuesta CSV">

| **Columna** | **Descripción** |
| --- | --- |
| intervalo de tiempo | Fecha y hora de los clics. Formato aaaa-mm-dd |
| Total de clics | Número total de clics durante el periodo del reporte |
| clics válidos | Número de clics válidos durante el periodo del reporte |
| missing\_signature | Número de clics sin firma durante el periodo del reporte |
| clics caducados | Número de clics caducados durante el periodo del reporte |
| invalid\_signature | Número de clics con firma no validada durante el periodo del reporte |
| sin secretos activos | Número de clics rechazados porque no hay claves secretas activas en el sistema (normalmente cuando el sistema está en modo de sólo reporte). |

</Accordion>

<div id="test-curl-example-and-response::66e922" />

<Accordion title="Ejemplo de curl de prueba y respuesta">

**Solicitud de curl**

```json
Asegúrate de que tienes una clave secreta válida comprobando la configuración de firma de clics mediante el método obtener configuración.
```

**Respuesta CSV**

| **intervalo de tiempo** | **Total de clics** | **clics válidos** | **missing\_signature** | **clics caducados** | **invalid\_signature** | **sin firmas activas** |
| --- | --- | --- | --- | --- | --- | --- |
| 2021-01-17T07 | 928082156 | 928082156 | 0 | 0 | 0 | 0 |
| 2021-01-17T08 | 923796132 | 923796132 | 0 | 0 | 0 | 0 |
| 2021-01-17T09 | 917541373 | 917541373 | 0 | 0 | 0 | 0 |
| 2021-01-17T10 | 909977064 | 909977064 | 0 | 0 | 0 | 0 |
| 2021-01-17T11 | 965104299 | 965104299 | 0 | 0 | 0 | 0 |
| 2021-01-17T12 | 975134824 | 975134824 | 0 | 0 | 0 | 0 |

</Accordion>

<div id="http-response-codes::8454f45d" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes-6" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="exclude-app-method" />

### Excluir método de aplicación

<div id="exclude-app-method-basics" />

<Accordion title="Conceptos básicos del método de exclusión de aplicaciones">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Ruta</td><td> https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>excluded-app/&lt;app-id&gt;</span></strong> </td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td>Vacío</td></tr></tbody></table>

</Accordion>

<div id="api-request::1054abca" />

<Accordion title="Solicitud API">

**Método**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-5" />

#### Parámetros

| Parámetro | Descripción |
| --- | --- |
| app-id | ID de aplicación que debe excluirse de la validación de firma de clics |

</Accordion>

<div id="exclude-app-curl-example" />

<Accordion title="Ejemplo de exclusión de aplicación curl">

**Solicitud de curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7991b66" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes-7" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="remove-excluded-app-method" />

### Eliminar el método de aplicaciones excluidas

<div id="remove-excluded-app-method-basics" />

<Accordion title="Eliminar método básico para aplicaciones excluidas">

<table><thead><tr><th>Categoría</th><th>Elemento</th><th><span>Descripción</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitud</td><td>Método HTTP</td><td><code>ELIMINAR</code></td></tr><tr><td>Ruta</td><td> https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>excluded-app/&lt;app-id&gt;</span></strong> </td></tr><tr><td>Encabezado de autorización </td><td><ul><li>El encabezado de autorización obligatorio contiene un token de portador. </li><li>El administrador obtiene el token en el panel de control de la siguiente manera:  <a href="/marketers/es/docs/managing-appsflyer-tokens" target="_blank">El administrador va a la lista desplegable de correo electrónico &gt; tokens de API para obtener el token V2.0</a>  </li></ul></td></tr><tr><td>Respuesta</td><td>Resultados</td><td>Vacío</td></tr></tbody></table>

</Accordion>

<div id="api-request::3f5b6d35" />

<div id="api-request::9504d16f" />

<Accordion title="Solicitud API">

**Método**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-6" />

#### Parámetros

| Parámetro | Descripción |
| --- | --- |
| app-id | ID de aplicación que debe eliminarse de la lista de aplicaciones excluidas de la validación de firma por clic |

</Accordion>

<div id="remove-excluded-app-curl-example" />

<Accordion title="Ejemplo de eliminación de curl de aplicación excluida">

**Solicitud de curl**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::b5e059da" />

<Accordion title="Códigos de respuesta HTTP">

<div id="response-codes-8" />

#### Códigos de respuesta

| Código | Mensaje | Observaciones |
| --- | --- | --- |
| 200 | Correcto |  |
| 401 | No autorizado | Encabezado de autorización no válido o ausente |

</Accordion>

<div id="code-sample" />

<Accordion title="Ejemplo de código">

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

//añade la caducidad a la URL del clic
long expiration = System.currentTimeMillis() + (60000L * ttlMinutes);
clickUrl += "&expires="+expiration;

//crea un objeto SecretKey a partir de la cadena de clave proporcionada
SecretKeySpec signingKey = new SecretKeySpec(secretKey.getBytes(), "HmacSHA256");
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(signingKey);

//genera una firma a partir de la URL del clic y la codifica en base64 sin relleno
String generatedSignature =     
Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(clickUrl.getBytes()));

//añade la firma a la URL del clic
String signedClickUrl = clickUrl + "&signature=" + generatedSignature;
```

</Accordion>

</Accordion>

<div id="additional-information" />

## Información adicional

<div id="troubleshooting" />

<Accordion title="Resolución de problemas">

AppsFlyer detiene la validación de firmas de clics y vuelve al modo de sólo reporte cuandomás del 90% de los clics en una hora no superan la validación de firmas.

Esto sirve para proteger a tu empresa de un posible problema técnico y te permite encontrar la causa de la anomalía:

* Las redes de publicidad pueden tener un máximo de dos claves secretas activas simultáneamente.
* Si observas que los clics se bloquean incorrectamente:
  1. Si compruebas que la firma funciona como se espera y los clics se bloquean correctamente, desactiva el [disyuntor mediante el método de configuración del disyuntor.](/docs/click-signing-for-ad-networks#configurar-el-método-del-disyuntor)
  2. Utiliza el [reporte de firma de clics](/docs/click-signing-for-ad-networks#método-de-reporte) para obtener más información sobre los clics bloqueados e investigar las fuentes (agencia/app-iDs) y los motivos de los clics no válidos.
* Si encuentras un problema con una aplicación específica debido a una integración no estándar, excluye esta aplicación de la validación de firma de clics utilizando la API de [excluir aplicación API.](/docs/click-signing-for-ad-networks#excluir-método-de-aplicación)
* Si encuentras un problema con tu configuración:
  1. Continúa funcionando en modo sólo reporte.
  2. Arregla el proceso de firma de clics por tu parte.
  3. Comprueba los resultados en el [reporte de firma de clics](/docs/click-signing-for-ad-networks#método-de-reporte) yvuelve a activar la validación de firma de clics cuando veas que los clics se están validando como se esperaba.

</Accordion>

<div id="faq" />

<Accordion title="Preguntas frecuentes">

| **Pregunta: ¿Cómo podemos probar la firma clic sin afectar a la producción?**<br /><br />**Respuesta**: Hay dos formas de probar la firma por clic:<ol><li>Utiliza la [API de prueba](/docs/click-signing-for-ad-networks#método-de-prueba). Este método es útil durante la fase de desarrollo, para probar las firmas de clics individuales.</li><li>Utiliza el modo de sólo reporte. El modo de sólo reporte verifica las firmas de los clics de producción y te muestra lo que se bloquearía, pero no bloquea los clics no válidos. Por lo tanto, puedes probar que la firma de clics funciona sin afectar al tráfico real.</li></ol> |
| --- |
| **Pregunta: ¿Cuál es la diferencia entre un token de API y una clave secreta?**<br /><br />**Respuesta**: **Token de API**: se utiliza para autorizar y ejecutar la API de firma de clics. Sólo hay uno por red de publicidad. El <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">token API V2.0 token de AppsFlyer</Anchor> debe obtenerse del administrador.<br /><br />**Clave secreta**: Se utiliza para generar la firma. Utiliza el [método de generación de claves secretas](/docs/click-signing-for-ad-networks#método-de-generación-de-clave-secreta) para crear claves secretas. La red de publicidad se encarga de generar nuevas claves secretas. Consulta la [sección de rasgos](/docs/click-signing-for-ad-networks#traits) para más información. |
| **Pregunta: ¿Podemos aplicar la firma por clic sólo a determinadas campañas?**<br /><br />**Respuesta**: No. La firma de clics se aplica a todos los clics procedentes de una red de publicidad. Puedes excluir determinadas aplicaciones de la firma de clics, pero no puedes excluir sólo determinadas campañas. |

</Accordion>

<div id="traits" />

<Accordion title="Características">

| Caducado | Descripción |
| --- | --- |
| Haz clic en la firma | La firma debe producirse en los servidores de la red de publicidad. |
| Clave secreta | <ul><li>curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \ -H 'Authorization: Bearer `{API V2.0 token available to the admin in the dashboard.}' --data-raw '{ "status":"enabled" }`'</li><li>Cada clave secreta tiene una caducidad.</li><li>Los clics firmados con claves secretas caducadas son rechazados.</li></ul> |
| Reporte de API | Las estadísticas actualizadas de la validez de los clics se agregan cada hora. |

</Accordion>

<div data-zendesk-anchors="about-click-signing=acerca-de-la-firma-de-clics h_01HNWC70BPGDJAG3X8M5Z2RHQ4=acerca-de-la-firma-de-clics click-signature-integration=integraci%C3%B3n-de-la-firma-clic h_01HNWC70BPFYMZ56GTPV3W6DXA=integraci%C3%B3n-de-la-firma-clic flow=flujo h_01HNWC70BPMXTKF9NZBYGCB874=flujo procedure=procedimiento h_01HNWC70BPHCAGD1ECA56CC1Q6=procedimiento h_01HNWC70BPAR4QNTNSFE1JZM2J=nota list-of-attributes=crear-una-firma-de-clic h_01HP4A42YYFFF6M4VEH84KRTTK=crear-una-firma-de-clic h_01HNWD3XYWFRY262HZZVAVWACR=lista-de-atributos attribute-rules=reglas-de-atributos-y-json h_01HNWE3A19RM7757B707TWZ6G0=reglas-de-atributos-y-json order-and-appearance-of-attributes=orden-y-apariencia-de-los-atributos h_01HNWE3A1920YQGZX2VG4X3M4B=orden-y-apariencia-de-los-atributos empty-attributes=atributos-vac%C3%ADos h_01HNYRZ1DPDDQ5H8RFYKAQWVKP=atributos-vac%C3%ADos json-data-structure=estructura-de-datos-json h_01HNYS6R7F0MNPBN08TXKQS5DV=estructura-de-datos-json attribute-value-escaping=escape-de-valores-de-atributos h_01HNYSEBGD1DBSV2MHS7DZ75HS=escape-de-valores-de-atributos json-spaces=espacios-json h_01HNYSY42HS1RXFG7T7QS9B0TK=espacios-json signature-algorithm=algoritmo-de-firma h_01HNYSJDFWAM9RREYH4M8DZQJA=algoritmo-de-firma signature-example=ejemplo-de-firma h_01HP3YAN03BWVA30JP1JAFZYAG=ejemplo-de-firma h_01HP3Y2Z65BN0SZ56XSHD52MSY=building-a-signature-example code-example=ejemplos-de-c%C3%B3digo h_01HNYT8Z33M69JAS72MQ03YX0M=ejemplos-de-c%C3%B3digo h_01HP3XVEJTBBVKZYEBZT62PR20=signingsupportedparamsjson h_01HP3XVEJTWWJVDBK5PGQH7DJY=signatureexamplego click-signature-apis=api-de-firma-por-clic h_01HNWC70BPNEVT00S040TQ9KVD=api-de-firma-por-clic click-signature-apis::58bf03c7=api-de-firma-por-clic-1 h_01HNWC70BPR8XXC3TQCAZSGFZS=api-de-firma-por-clic-1 legacy-versions=versiones-heredadas h_01HNZ3YMFRWFDY751EBA58V6Q0=versiones-heredadas h_01HNWCYB2YXCVGCP38GRBAJYQ4=v1-legacy generate-secret-key-method=m%C3%A9todo-de-generaci%C3%B3n-de-clave-secreta h_01HNWC70BPBPSX1WKJJC2W6H69=m%C3%A9todo-de-generaci%C3%B3n-de-clave-secreta h_01HNWC70BPPBK2S38KA6RQSTCN=generate-secret-key-basics h_01HNWC70BP40D5XN8DZQHSDZ5K=api-request parameters=par%C3%A1metros h_01HNWC70BPS83JD78JWQYK1NX9=par%C3%A1metros h_01HNWC70BPQC37602GV8GQPSEQ=json-response h_01HNWC70BP7V8KRW4861PXC2PX=generate-secret-key-curl-example-and-response h_01HNWC70BPKTPZEKFD37B6YQMH=http-response-codes response-codes=c%C3%B3digos-de-respuesta h_01HNWC70BPMQ8Q94JD5CBT5RHZ=c%C3%B3digos-de-respuesta revoke-secret-key-method=m%C3%A9todo-de-revocaci%C3%B3n-de-la-clave-secreta h_01HNWC70BP8V05Q04J6EVGAS9T=m%C3%A9todo-de-revocaci%C3%B3n-de-la-clave-secreta h_01HNWC70BP69ZJERY1Z03A5V4C=revoke-secrete-key-basics h_01HNWC70BPN01BNKKC7T9QMF44=api-request::3f5b6d35 parameters::f8e4d5cf=par%C3%A1metros-1 h_01HNWC70BPQ5S06E210RTE7E6R=par%C3%A1metros-1 h_01HNWC70BPBQA0ME8D6TZEM2EB=generate-secret-key-curl-example-and-response::5a4174fc h_01HNWC70BP9AV6PPEZNPQWJN85=http-response-codes::7dc4ee64 response-codes::d802debd=c%C3%B3digos-de-respuesta-1 h_01HNWC70BPN18MB98KWND886QN=c%C3%B3digos-de-respuesta-1 test-method=m%C3%A9todo-de-prueba h_01HNWC70BPKEVRDMT8N4HMC98W=m%C3%A9todo-de-prueba h_01HNWC70BPX4TH2MNE4GJBGHRG=test-basics h_01HNWC70BP5X2MZ3AC8BF69XYK=api-request::b2432cce parameters::7d3f0c33=par%C3%A1metros-2 h_01HNWC70BPKQFVEGWR9QT566YX=par%C3%A1metros-2 h_01HNWC70BPM50T2JEGJF41GGX4=json-response::cd966b82 h_01HNWC70BPSQYQ5R7PJE4CAKYG=test-curl-example-and-response h_01HNWC70BP8SSK2E5DFAD2Q6NP=http-response-codes::22d1011c response-codes::a79c47f4=c%C3%B3digos-de-respuesta-2 h_01HNWC70BPC43F5H85F56DDSQR=c%C3%B3digos-de-respuesta-2 configure-mode-method=configurar-m%C3%A9todo-de-modo h_01HNWC70BP6NPF7NSF0MGA4BJ3=configurar-m%C3%A9todo-de-modo h_01HNWC70BPKNAVCD57D2E7FX8F=configure-mode-basics h_01HNWC70BQFCJCHHVQHKWB57GF=api-request::1ede8b9c parameters::2fff2a1b=par%C3%A1metros-3 h_01HNWC70BQSQ7YWZVQB9A4DZQW=par%C3%A1metros-3 h_01HNWC70BQF0J2TZF181BW0MKT=configure-mode-curl-example h_01HNWC70BQ9HNQV7HA45ZXA2Z3=http-response-codes::b3328f8b response-codes::fe5a5b10=c%C3%B3digos-de-respuesta-3 h_01HNWC70BQZ657X25N8JGM57A1=c%C3%B3digos-de-respuesta-3 configure-circuit-breaker-method=configurar-el-m%C3%A9todo-del-disyuntor h_01HNWC70BQVSFS7G330NF4XHEP=configurar-el-m%C3%A9todo-del-disyuntor h_01HNWC70BQ097J2VXW0XKSH3M9=configure-circuit-breaker-basics h_01HNWC70BQJWZYZEDJJ5J7JX6X=api-request::ef73eae0 request-body-json=cuerpo-de-la-solicitud-json h_01HNWC70BQ6R955776Y6H4EZRG=cuerpo-de-la-solicitud-json h_01HNWC70BQRZEZ4PTV59FGYS4Z=configure-circuit-breaker-curl-example-and-response h_01HNWC70BQPP5X9JH1HJ1K58H4=http-response-codes::d35e3a62 response-codes::b056f2a3=c%C3%B3digos-de-respuesta-4 h_01HNWC70BQWQ5KWZX8BM0A7BC5=c%C3%B3digos-de-respuesta-4 get-configuration-method=obtener-m%C3%A9todo-de-configuraci%C3%B3n h_01HNWC70BQZY6TYSQBWZ17S0W5=obtener-m%C3%A9todo-de-configuraci%C3%B3n h_01HNWC70BQY6CPZA5A56J3TET0=get-configuration-basics h_01HNWC70BQ444XNRRCZZH2GFJH=api-request::a2a93b39 h_01HNWC70BQJ8J2WGXE2QF144FK=json-response::fee92c h_01HNWC70BQ701HZR6PYC0CW88T=get-configuration-curl-example-and-response h_01HNWC70BQ8R5GR906Y9W79E81=http-response-codes::90a409c response-codes::ebf1292a=c%C3%B3digos-de-respuesta-7 h_01HNWC70BQDGVBZ94F0N49FF40=c%C3%B3digos-de-respuesta-7 report-method=m%C3%A9todo-de-reporte h_01HNWC70BQTBMNKHV4RH4ZQ0AE=m%C3%A9todo-de-reporte h_01HNWC70BQ4K7T3FXZWV5KW3FM=report-basics h_01HNWC70BQMBD2WNVQH69FMSPR=api-request::b28cedb0 parameters::e6795217=par%C3%A1metros-4 h_01HNWC70BQ0FDT4T2RAJEPAHNC=par%C3%A1metros-4 h_01HNWC70BQRZTXMKD30V7QQPE4=csv-response h_01HNWC70BQV61TVE65TQ3WWGCP=test-curl-example-and-response::66e922 h_01HNWC70BQQ3MP256QK0JT2K78=http-response-codes::8454f45d response-codes::a8a9822d=c%C3%B3digos-de-respuesta-8 h_01HNWC70BQTPPWA4SNG25E8FFB=c%C3%B3digos-de-respuesta-8 exclude-app-method=excluir-m%C3%A9todo-de-aplicaci%C3%B3n h_01HNWC70BQ9SK2XCBGGHXVMRDV=excluir-m%C3%A9todo-de-aplicaci%C3%B3n h_01HNWC70BQ8GGRTQ1RW1KCY0SQ=exclude-app-method-basics h_01HNWC70BQ4D62SZCHKGEP6RMJ=api-request::1054abca parameters::f5e3c6ce=par%C3%A1metros-5 h_01HNWC70BREG4XQJV3X9518FC5=par%C3%A1metros-5 h_01HNWC70BR2PVDHTG64WZ36KPV=exclude-app-curl-example h_01HNWC70BR7XCTW6N69GEB4ARF=http-response-codes::7991b66 response-codes::addfcfd8=c%C3%B3digos-de-respuesta-8 h_01HNWC70BRN8BHWF6WGY2RH45X=c%C3%B3digos-de-respuesta-8 remove-excluded-app-method=eliminar-el-m%C3%A9todo-de-aplicaciones-excluidas h_01HNWC70BR18P0H96VN64RS05G=eliminar-el-m%C3%A9todo-de-aplicaciones-excluidas h_01HNWC70BRAWBGC5EE0Q8XBTW1=remove-excluded-app-method-basics h_01HNWC70BRD885KN6YDXQ9GXS2=api-request::9504d16f parameters::34936c8f=par%C3%A1metros-6 h_01HNWC70BR4ADH7T3AFG58FZH6=par%C3%A1metros-6 h_01HNWC70BRK7DM7MW150AFVKG2=remove-excluded-app-curl-example h_01HNWC70BRMFN4RM65YV2NWR29=http-response-codes::b5e059da response-codes::e8de940a=c%C3%B3digos-de-respuesta-8 h_01HNWC70BRHA8AA7ZV1R4EBYJH=c%C3%B3digos-de-respuesta-8 h_01HNWC70BRTZZWME7QCP8HV9AY=code-sample additional-information=informaci%C3%B3n-adicional h_01HNWC70BRN0NGTQVWED6VG81Y=informaci%C3%B3n-adicional h_01HNWC70BRS884G8RCMAPFPV1N=troubleshooting h_01HNWC70BRP3BVJSHSD1CPCB9S=faq h_01HNWC70BRDN37MBTEKT0DH8CT=traits" />
