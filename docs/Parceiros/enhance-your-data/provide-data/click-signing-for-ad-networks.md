---
title: Assinatura de cliques para ad networks
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
  edited_at: '2026-08-19T00:37:29Z'
  id: 360017831497
  locale: pt
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/pt/articles/360017831497
---
> **Em resumo:** Adicione validação de assinatura aos cliques para evitar responsabilidades por fraude e para que cliques fraudulentos não sejam atribuídos à sua ad network.

## Sobre assinatura de cliques

Com o mínimo de tecnologia, golpistas podem enviar cliques em nome de uma ad network e criar milhares, ou até milhões, de cliques falsos que são enviados para a AppsFlyer. Às vezes, as próprias ad networks não estão cientes do problema.

Para que uma ad network garanta que os cliques atribuídos a ela pela AppsFlyer realmente se originaram da ad network, e não de um golpista que cria cliques falsos, as ad networks devem assinar seus cliques com assinaturas <Anchor target="_blank" href="https://en.wikipedia.org/wiki/HMAC">HMAC-SHA256</Anchor>.

A assinatura de cliques também evita que o tráfego da ad network seja bloqueado devido a um flooding de cliques. Ou seja, se uma ad network atingir o limite de bloqueio de cliques devido a um nível extremo de flooding de cliques, a AppsFlyer para de registrar e atribuir seus cliques pelo resto do dia.

As assinaturas permitem que a AppsFlyer valide os cliques e verifique se as informações do clique não foram manipuladas por fraudadores.

* Os cliques validados são registados e atribuídos à rede de publicidade.
* Os cliques invalidados são rejeitados e:
  * Estão disponíveis nos relatórios do Protect360 para ad networks (não anunciantes). <Anchor target="_blank" href="/partners/pt/docs/protect360-reports-for-ad-networks#failed-click-signatures">Saiba mais</Anchor>
  * Não afetam a taxa de conversão ou o limite de bloqueio de cliques da ad network

## Integração de assinatura de cliques

### Fluxo

O gráfico a seguir descreve o fluxo do desenvolvimento inicial e testes básicos para os testes de produção e, finalmente, para a produção.

![Click_signing_integration_flow.png](https://files.readme.io/3bc0103090535c22db027fb09f72ad89d88210bba8f2b6f43d1166c2911d71cd-360017572558.png)

### Procedimento

**Pré-requisito:** <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">token da API V2.0</Anchor> do administrador para autorizar a API de assinatura de clique.

**Para assinar seus cliques**:

1. Gere uma chave secreta com a API Gerar chave secreta.  
   Melhores práticas: gere e use uma nova chave secreta a cada 24 horas, com expiração de 36 horas.
2. Desenvolva código em seus servidores que chame a API Gerar chave secreta, pegue a chave secreta e gere uma assinatura HMAC-SHA256. Veja o exemplo de código.  
   Você pode usar as outras APIs conforme descrito na tabela a seguir.
3. O código adiciona o seguinte aos seus URLs de clique:
   * Um parâmetro **expires** que contém um carimbo de data/hora Unix (em UTC) após o qual a ad network não reivindica o clique.
   * A assinatura HMAC-SHA256.  
     Exemplo:

     ```http
     https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_siteid=12345&expires=1597657118&signature_v2=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk
     ```

> 📘 **Observação:**
>
> Certifique-se de que qualquer codificação de URL de caracteres especiais ou espaços no seu link ocorra antes que a assinatura de clique seja gerada. Gerar a assinatura primeiro resulta em falha na verificação.

## Criando uma assinatura de clique

Para criar uma assinatura de clique você deve:

1. Crie um JSON usando a lista de atributos e as regras JSON abaixo
2. Crie a assinatura deste JSON usando HMAC56

### Lista de atributos

A lista de atributos a seguir é compatível com assinatura de clique e engajamento.

| Pedido | Parâmetro | Obrigatoriedade | Notas |
| --- | --- | --- | --- |
| 1 | link\_domain | Yes | O domínio do URL do clique Por exemplo:<ul><li>app.appsflyer.com</li><li>myapp.onelink.me</li><li>click.mycustomdomain.com</li></ul> |
| 2 | link\_path | Yes | O caminho da URL de clique, sem incluir uma barra invertida inicial.  <br />**app-id** para links de plataforma única ou **template-id** para OneLink |
| 3 | pid | Yes |  |
| 4 | af\_prt | Sem |  |
| 5 | af\_siteid | Yes |  |
| 6 | clickid | Yes | Um identificador único e exclusivo do clique |
| 7 | expires | Yes | expiração do clique |
| 8 | af\_engagement\_type | Sem |  |
| 9 | af\_click\_lookback | Sem |  |
| 10 | af\_viewthrough\_lookback | Sem |  |
| 11 | {"af_reengagement"} {"_window"} | Sem |  |
| 12 | is\_retargeting | Sem |  |
| 13 | af\_ip | Sem |  |
| 14 | advertising\_id | Sem |  |
| 15 | OAID | Sem |  |
| 16 | fire\_advertising\_id | Sem |  |
| 17 | idfa | Sem |  |
| 18 | idfv | Sem |  |

### Regras de atributos e JSON

#### Ordem e aparência dos atributos

* Os parâmetros compatíveis no URL de engajamento com um valor devem estar no JSON
* Os atributos devem ser listados no JSON na ordem listada na tabela acima

#### Atributos vazios

* Os atributos listados no JSON não podem ser valores vazios ou conter apenas espaços

#### Estrutura de dados JSON

* A estrutura de dados JSON deve ser uma matriz de atributos
  * Cada atributo estará no formato ["key", "value"]  
    Exemplo:   
    `[["key-1","value-1"],["key-2","value-2"]...["key-n","value-n"]]`

#### Valor do atributo escapando

* Os valores no JSON devem ser escritos em **strings em minúsculas**, conforme definido no <Anchor target="_blank" href="https://www.w3docs.com/snippets/java/how-should-i-escape-strings-in-json.html">padrão JSON</Anchor>.

#### Espaços no JSON

* O JSON deve ser compactado. Não deve conter espaços em branco, parágrafos ou caracteres em quebra de linha entre os valores.

#### Algoritmo de assinatura

* Use HmacSHA256 com a chave secreta para criar a assinatura para o JSON
* Codifique a assinatura com Base64 **sem** preenchimento
* Adicione a assinatura ao URL do clique com um parâmetro signature\_v2

```json
//generate a signature from the click url and encode it with base64 without padding String generatedSignature = Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(jsonString.getBytes()));
```

### Exemplo de assinatura

<div id="building-a-signature-example" />

<Accordion title="Criando um exemplo de assinatura">

Exemplo de URL de clique do OneLink (multiplataforma):

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&clickid=sdkfjasksjskdfj9845weh&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615
```

Exemplo de objeto json para assinatura (antes de remover espaços em branco):

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

Exemplo de objeto json para assinatura (após remover espaços em branco)

```json
[["link_domain","yourbrand.onelink.me"],["link_path","qswl"],["pid","mediasource_int"],["template-id","qswl"],["af_siteid","my_site"],["clickid","12345"],["expires","1689695615"]]
```

URL do clique final com a assinatura:

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615  
&signature_v2=WIfCmfLAPSsVrBTqCqfihMeLCnbE4dIAlhHF84WsiWA
```

</Accordion>

### Exemplos de código

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
		return nil, errors. New("falha ao carregar " + path)
	}
	var params []Param
	_ = json. Unmarshal(byteValue, &params)
	return params, nil
}

func computeHmac256(message, secret string) (res string, errResult error) {
	defer func() {
		if r := recover(); r != nil {
			errResult = r.(error)
			fmt. err: %+v", errResult)
			res = ""
			return
		}
	}()

	key := []byte(secret)
	h := hmac. New(sha256. New, key)
	h. Write([]byte(message))
	return base64.URLEncoding. WithPadding(base64. NoPadding). EncodeToString(h. Sum(nil)), nil
}

// esta função aceita uma URL de clique, um ttl para o clique em segundos e a lista de parâmetros com suporte
// a função:
// 1. adiciona a expiração ao clique com base no ttl fornecido
// 2. cria um json para a assinatura
// 3. cria uma assinatura HMAC256
// 4. adiciona a assinatura à URL de clique
func signURLV2(originalURL string, secret string, clickTtlSeconds int64, supportedParams []Param) (signedURL string, err error) {

	// adiciona uma expiração ao clique
	expires := time. Now().UTC(). Unix() + clickTtlSeconds
	urlWithExpired := fmt. Sprintf("%s%s%d", originalURL, "&expires=", expires)

	// analisa a URL
	parsedURL, err := url. Parse(urlWithExpired)
	if err != nil {
		return "", errors. New("falha ao analisar a URL")
	}

	// cria um json a partir da URL
	jsonStr, err := buildJSONFromURLV2(parsedURL, supportedParams)
	if err != nil {
		return "", err
	}

	// cria uma assinatura
	signatureV2, err := computeHmac256(jsonStr, secret)
	if err != nil {
		fmt. Println("Falha ao calcular computeHMAC256 para a URL %s. err: %+v", jsonStr, err)
		return "", errors. New("falha ao calcular computeHMAC256 para a url")
	}

	//add the signature to the url
	signedURL = fmt. err: %+v", jsonStr, err)
		return "", errors.New("falha ao calcular computeHMAC256 para a url")
	}

	//add the signature to the url
	signedURL = fmt.Sprintf("%s%s%s", urlWithExpired, "&signature_v2=", signatureV2)

	return signedURL, nil

}

// this function builds a json from a given click url.
// Ela retorna uma representação em string do json pronta para ser assinada.
func buildJSONFromURLV2(parsedURL *url.URL, supportedParams []Param) (string, error) {
	// inicia um json vazio na estrutura [[key-1,val-1],[key-2,val-2]...[key-n,val-n]]
	var jsonData [][2]string

	// adiciona o domínio do host da URL ao json
	domain := parsedURL. Host
	param := [2]string{"link_domain", domain}
	jsonData = append(jsonData, param)

	// adiciona o caminho (ID do aplicativo ou ID do modelo) ao json
	path := parsedURL. Path
	if len(path) > 1 {
		param := [2]string{"link_path", path[1:]}
		jsonData = append(jsonData, param)
	}

	// percorre a lista ordenada de parâmetros com suporte e os adiciona ao json
	for i := 0; i <len(supportedParams); i++ {name := supportedParams[i]. Name val := parsedURL. Query(). Get(name) if len(val) > 0 {
			param := [2]string{name, val}
			jsonData = append(jsonData, param)
		} else if supportedParams[i]. Mandatory {
			return "", errors. New("parâmetro obrigatório ausente: " + name)
		}
	}

	// gera a representação em string do objeto json
	jsonObj, _ := json. Marshal(jsonData)
	return strings. ToLower(string(jsonObj)), nil
}

func main() {

	supportedParams, err := LoadSupportedParams()
	if err != nil {
		fmt. Println("Erro: ", err)
		os. Exit(1)
	}

	var secretKey = "tqJU4Qd/eFTEWfqW7KCG9asDO0bmZoFzv8GY3VPSPAM="
	var clickTtlSeconds int64 = 60
	var originalUrl = "https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012&clickid=1234&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign"

	fmt.
```

</Accordion>

## APIs de assinatura de clique

A AppsFlyer fornece APIs que permitem que as ad networks gerenciem e testem o processo de assinatura de cliques. Veja a lista de APIs na tabela abaixo e as seções a seguir com informações necessárias para usar a API. 

#### APIs de assinatura de clique

| Método API | Observações |
| --- | --- |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-post">Gerar chave secreta</Anchor> | Gerar chaves secretas para serem usadas na assinatura. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-delete">Revogar chave secreta</Anchor> | Cancelar chaves secretas comprometidas. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-test-post">Testar</Anchor> | Enviar cliques únicos para testar a assinatura. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-update-put">Modo de configuração</Anchor> | Configurar modo de assinatura de clique:<ul><li>**desabilitado** (padrão): Nenhuma validação de assinatura de clique é feita.</li><li>**report-only** (modo de teste): A AppsFlyer valida assinaturas de cliques, mas não bloqueia cliques com assinaturas inválidas. A ad network pode usar a **Report API** para obter estatísticas sobre cliques bem-sucedidos/com falha. Use isso para testar a assinatura de cliques sem afetar a produção e o tráfego real.</li><li>**habilitado:** A AppsFlyer bloqueia cliques com assinaturas inválidas ou ausentes.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-circuit-breaker-put">Configurar interruptor</Anchor> | Configure o modo do interruptor que evita que a ad network tenha muitos cliques bloqueados:<ul><li>**habilitado** (padrão): Se o sistema Protect360 detectar que muitos cliques estão marcados como inválidos, para evitar que a ad network tenha cliques potencialmente bloqueados incorretamente:<ul><li>Configure o modo da API para somente relatório.</li><li>Um alerta por e-mail é enviado para ad network para verificar se a API de assinatura de cliques está configurada corretamente.</li></ul></li><li>**desabilitado**: O Protect360 continua bloqueando todos os cliques marcados como inválidos, mesmo quando a porcentagem de bloqueio é anormalmente alta.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-get">Obter configuração</Anchor> | Obtenha o modo e os IDs das chaves secretas ativas. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-report-get">Relatório</Anchor> | Obtenha estatísticas dos últimos 3 dias sobre cliques bem-sucedidos e com falha quando o sistema estiver no modo **report-only** ou **enabled**. Use isso para testar a assinatura de cliques sem afetar a produção e o tráfego real. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-add">Excluir aplicativo</Anchor> | Configure IDs de aplicativos para serem excluídos da assinatura de cliques. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-delete">Remover aplicativo excluído</Anchor> | Configure IDs de aplicativo a serem incluídos na assinatura de cliques após terem sido excluídos. |

## Versões legadas

Essas versões não devem ser usadas e são listadas apenas para referência

<div id="v1-legacy" />

<Accordion title="V1 - legado">

### Método de geração de chave secreta

<div id="generate-secret-key-basics" />

<Accordion title="Gerar noções básicas de chave secreta">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>Visão geral</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Caminho</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>"}</code></span></td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.</a>  </li></ul></td></tr><tr><td>Mensuração</td><td>Resultados</td><td>Retornos de chaves secretas em um JSON</td></tr><tr><td> </td><td>Limite de solicitação</td><td>Máximo de 2 chaves secretas ativas por vez</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="Solicitação de API">

**Mensuração**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>
```

#### Parâmetros

| Parâmetro | Visão geral |
| --- | --- |
| ttlHours | <ul><li>Tempo de vida para a chave secreta, em horas, de 1 a 1440.</li><li>O padrão é de 36 horas.</li></ul> |

</Accordion>

<div id="json-response" />

<Accordion title="Resposta JSON">

| **Chave** | **Visão geral** |
| --- | --- |
| secret-key-id | Um ID para a chave secreta |
| secret key | A chave secreta para a assinatura do clique |
| expiration | Hora Epoch em milissegundos |

</Accordion>

<div id="generate-secret-key-curl-example-and-response" />

<Accordion title="Gerar exemplo de curl de chave secreta e resposta">

**Solicitação Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=36' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Resposta JSON**

```json
{
	"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
	"secret-key": "zGW6Rhrmb8+vuhHtL/Kp6rW5Ci9PNsjH1J5MGO9SIeg=",
	"expiration": 1610533263
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

### Método de revogação de chave secreta

<div id="revoke-secrete-key-basics" />

<Accordion title="Noções básicas sobre revogação de chave secreta">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>DELETE</code></td></tr><tr><td>Caminho</td><td><span><code>{"https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>"}</code></span></td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.</a>  </li></ul></td></tr><tr><td>resposta</td><td>Resultados</td><td>Vazio</td></tr></tbody></table>

</Accordion>

<Accordion title="Solicitação de API">

**Mensuração**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>
```

#### Parâmetros

| Parâmetro | A descrição |
| --- | --- |
| secret-id | O ID da chave secreta a ser revogada |

</Accordion>

<div id="generate-secret-key-curl-example-and-response::5a4174fc" />

<Accordion title="Gerar exemplo de curl de chave secreta e resposta">

**Solicitação Curl**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/secret/59ad6547-affc-45eb-a6c9-9805f88ee755' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7dc4ee64" />

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

### Método de teste

<div id="test-basics" />

<Accordion title="Noções básicas de teste">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Caminho</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/test</span></td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.</a>  </li></ul></td></tr><tr><td>Mensuração</td><td>Resultados</td><td>Retorna em um JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="Solicitação de API">

**Mensuração**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/test
```

#### Parâmetros

| Parâmetro | A descrição |
| --- | --- |
| url | O URL do clique (incluindo assinatura) para testar |

</Accordion>

<div id="json-response::cd966b82" />

<Accordion title="Resposta JSON">

| **Chave** | **A descrição** |
| --- | --- |
| test-status | Aprovado ou Falhou |
| Mensagem | Motivo da falha no teste. Exemplo:<ul><li>Assinatura faltando</li><li>Assinatura inválida</li><li>Expirou</li></ul> |

</Accordion>

<div id="test-curl-example-and-response" />

<Accordion title="Exemplo e resposta do teste curl">

**Solicitação Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/test' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "url": "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345&expires=1597657118&signature=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk"
}'
```

**Resposta JSON**

```json
{
	"test-status":"Passed / Failed",
	"message": "Invalid signature"
}
```

</Accordion>

<div id="http-response-codes::22d1011c" />

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

### Método de modo de configuração

<div id="configure-mode-basics" />

<Accordion title="Noções básicas do modo de configuração">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Caminho</td><td> <span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>mode/&lt;mode&gt;</strong></span></span> </td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.</a>  </li></ul></td></tr><tr><td>Mensuração</td><td>Resultados</td><td>Retorna em um JSON</td></tr></tbody></table>

</Accordion>

<div id="api-request::b2432cce" />

<Accordion title="Solicitação de API">

**Mensuração**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/mode/<mode>
```

#### Parâmetros

| Parâmetro | A descrição |
| --- | --- |
| mode | Opções de upgrade:<ul><li>habilitado<br />**Atenção!** Defina o modo como "ativado" somente depois de executar o modo somente relatório por algumas horas e verifique seus relatórios para garantir que a configuração esteja correta e que todos os cliques passaram pela validação de assinatura.</li><li>desativado</li><li>somente relatório</li></ul> |

</Accordion>

<div id="configure-mode-curl-example" />

<Accordion title="Exemplo de configuração de modo curl">

**Solicitação Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/mode/report-only' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::b3328f8b" />

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Erro na solicitação | Modo inválido |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

### Configurar método de interruptor

<div id="configure-circuit-breaker-basics" />

<Accordion title="Configurar noções básicas de interruptor">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Caminho</td><td><span>https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker</span></td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.</a>  </li></ul></td></tr><tr><td>Mensuração</td><td>Resultados</td><td><span>Estado HTTP</span></td></tr></tbody></table>

</Accordion>

<div id="api-request::1ede8b9c" />

<div id="api-request::ef73eae0" />

<Accordion title="Solicitação de API">

**Mensuração**

```http
POST https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker
```

#### Corpo da solicitação JSON

| Parâmetro | A descrição |
| --- | --- |
| estado | <ul><li>ativado</li><li>desativado</li></ul> |

</Accordion>

<div id="configure-circuit-breaker-curl-example-and-response" />

<Accordion title="Exemplo de configuração de interruptor curl e resposta">

**Solicitação Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
--data-raw '{
"status":"enabled"
}'
--data-raw '{
"status":"enabled"
}'
```

</Accordion>

<div id="http-response-codes::d35e3a62" />

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Erro na solicitação | Status inválido |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

### Obter método de configuração

<div id="get-configuration-basics" />

<Accordion title="Obter noções básicas de configuração">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>BAIXAR</code></td></tr><tr><td>Caminho</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/config</span></td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.</a>  </li></ul></td></tr><tr><td>Mensuração</td><td>Resultados</td><td>Retorna em um JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="Solicitação de API">

**Mensuração**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/config
```

</Accordion>

<div id="json-response::fee92c" />

<Accordion title="Resposta JSON">

| **Chave** | **A descrição** |
| --- | --- |
| mode | Um de:<ul><li>ativado</li><li>desativado</li><li>somente relatório</li></ul> |
| configuração do disjuntor | Um objeto JSON contendo **status**, um dos seguintes:<ul><li>ativado</li><li>desabilitado</li></ul> |
| active-key-ids | Um array JSON contendo chaves ativas:<ul><li>**secret-key-id**: ID gerado aleatoriamente da chave secreta</li><li>**expiration**: Tempo epoch em milissegundos da chave secreta</li></ul> |
| excluded-app-ids | Uma matriz JSON com app-ids excluídos |

</Accordion>

<div id="get-configuration-curl-example-and-response" />

<Accordion title="Obter exemplo de configuração curl e resposta">

**Solicitação Curl**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/config' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Resposta JSON**

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

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

### Método de relatório

<div id="report-basics" />

<Accordion title="Noções básicas de relatórios">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>BAIXAR</code></td></tr><tr><td>Caminho</td><td><span>https://hq1.appsflyer.com/api/p360-click-signing/report</span></td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; Tokens de API para obter o token V2.0</a>  </li></ul></td></tr><tr><td>Mensuração</td><td>Resultados</td><td>Retorna em um CSV</td></tr></tbody></table>

</Accordion>

<div id="api-request::a2a93b39" />

<div id="api-request::b28cedb0" />

<Accordion title="Solicitação de API">

**Mensuração**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/report
```

#### Parâmetros

<table><thead><tr><th>Parâmetro</th><th>A descrição</th></tr></thead><tbody><tr><td>start_date</td><td>Data e hora de início do relatório. Formato: aaaa-mm-ddThh</td></tr><tr><td>end-date</td><td><span>Data e hora de término do relatório. Formato: aaaa-mm-ddThh</span></td></tr><tr><td colspan="2"><span>A API requer <strong>ambas</strong> as datas, start-date e end-date, ou <strong>nenhuma</strong> delas. Se a data de início/término não for fornecida, o relatório mostrará os resultados das últimas 24 horas.</span></td></tr></tbody></table>

</Accordion>

<div id="csv-response" />

<Accordion title="Resposta CSV">

| **Nome da** | **A descrição** |
| --- | --- |
| Tempo de | Data e hora dos cliques. Formato aaaa-mm-ddThh |
| total\_cliques | Número total de cliques durante o período do relatório |
| cliques\_válidos | Número de cliques válidos durante o período do relatório |
| assinatura\_ausente | Número de cliques sem assinaturas durante o período do relatório |
| cliques\_expirados | Número de cliques expirados durante o período do relatório |
| assinatura\_inválida | Número de cliques com assinatura inválida durante o período do relatório |
| sem\_segredos\_ativos | Número de cliques rejeitados porque não há chaves secretas ativas no sistema (geralmente quando o sistema está no modo somente relatório) |

</Accordion>

<div id="test-curl-example-and-response::66e922" />

<Accordion title="Exemplo e resposta do teste curl">

**Solicitação Curl**

```json
O administrador obtém o token no dashboard da seguinte forma:  O administrador acessa a lista suspensa de e-mail > tokens de API para obter o token V2.
```

**Resposta CSV**

| **Tempo de** | **total\_cliques** | **cliques\_válidos** | **assinatura\_ausente** | **cliques\_expirados** | **assinatura\_inválida** | **no\_active\_signatures** |
| --- | --- | --- | --- | --- | --- | --- |
| 2021-01-17T07 | 928082156 | 928082156 | 0 | 0 | 0 | 0 |
| 2021-01-17T08 | 923796132 | 923796132 | 0 | 0 | 0 | 0 |
| 2021-01-17T09 | 917541373 | 917541373 | 0 | 0 | 0 | 0 |
| 2021-01-17T10 | 909977064 | 909977064 | 0 | 0 | 0 | 0 |
| 2021-01-17T11 | 965104299 | 965104299 | 0 | 0 | 0 | 0 |
| 2021-01-17T12 | 975134824 | 975134824 | 0 | 0 | 0 | 0 |

</Accordion>

<div id="http-response-codes::8454f45d" />

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

### Excluir método de aplicativo

<div id="exclude-app-method-basics" />

<Accordion title="Excluir noções básicas do aplicativo">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>POST</code></td></tr><tr><td>Caminho</td><td> <span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>excluded-app/&lt;app-id&gt;</strong></span></span> </td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.0</a>  </li></ul></td></tr><tr><td>Mensuração</td><td>Resultados</td><td>Vazio</td></tr></tbody></table>

</Accordion>

<div id="api-request::1054abca" />

<Accordion title="Solicitação de API">

**Mensuração**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

#### Parâmetros

| Parâmetro | A descrição |
| --- | --- |
| app-id | ID do aplicativo a ser excluído da validação de assinatura de clique |

</Accordion>

<div id="exclude-app-curl-example" />

<Accordion title="Exemplo de curl de exclusão de aplicativo">

**Solicitação Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7991b66" />

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

### Remover método de aplicativo excluído

<div id="remove-excluded-app-method-basics" />

<Accordion title="Remover noções básicas sobre o método do aplicativo">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>DELETE</code></td></tr><tr><td>Caminho</td><td> <span>https://hq1.appsflyer.com/api/p360-click-signing/config/</span><span><span><strong>excluded-app/&lt;app-id&gt;</strong></span></span> </td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma:  <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.0</a>  </li></ul></td></tr><tr><td>resposta</td><td>Resultados</td><td>Vazio</td></tr></tbody></table>

</Accordion>

<div id="api-request::3f5b6d35" />

<div id="api-request::9504d16f" />

<Accordion title="Solicitação de API">

**Mensuração**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

#### Parâmetros

| Parâmetro | A descrição |
| --- | --- |
| app-id | ID do aplicativo a ser removido da lista de aplicativos excluídos da validação de assinatura de clique |

</Accordion>

<div id="remove-excluded-app-curl-example" />

<Accordion title="Exemplo de curl para remover aplicativo excluído">

**Solicitação Curl**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::b5e059da" />

<Accordion title="Códigos de resposta HTTP">

#### Códigos de resposta

| Código | Mensagem | Considerações |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Não autorizado | Cabeçalho de autorização inválido ou ausente |

</Accordion>

<div id="code-sample" />

<Accordion title="Amostra de código">

```java
package sign;

import javax.crypto. Mac;
import javax.crypto.spec. SecretKeySpec;
import java.security. InvalidKeyException;
import java.security. NoSuchAlgorithmException;
import java.util. Base64;

.
.
.

String clickUrl = "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345"; String secretKey = "secret_key"; 
int ttlMinutes = 5;

//add expiration to the click URL
long expiration = System.currentTimeMillis() + (60000L * ttlMinutes);
clickUrl += "&expires="+expiration;

//create a SecretKey object from the given key string SecretKeySpec signingKey = new SecretKeySpec(secretKey.getBytes(), "HmacSHA256"); Mac mac = Mac.getInstance("HmacSHA256");
mac.init(signingKey);

//generate a signature from the click url and encode it with base64 without padding String generatedSignature = Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(clickUrl.getBytes()));

//add the signature to the click URL String signedClickUrl = clickUrl + "&signature=" + generatedSignature;
```

</Accordion>

</Accordion>

## Informações adicionais

<div id="troubleshooting" />

<Accordion title="Solução de problemas">

A AppsFlyer interrompe a validação da assinatura de clique e retorna ao modo somente relatório quando mais de 90% dos cliques em uma hora falham na validação da assinatura.

Isso protege sua empresa de um possível problema técnico e permite que você encontre a causa da anomalia:

* Se você perceber que a assinatura está funcionando conforme o esperado e os cliques estão sendo bloqueados corretamente, desative o disjuntor usando o [método de configuração do disjuntor.](/docs/click-signing-for-ad-networks#configurar-método-de-interruptor)
* Se você perceber que os cliques estão sendo bloqueados incorretamente:
  1. Certifique-se de que você tem uma chave secreta válida verificando a configuração de assinatura de cliques usando o [método de obter configuração.](/docs/click-signing-for-ad-networks#obter-método-de-configuração)
  2. Use o [relatório de assinatura de cliques](/docs/click-signing-for-ad-networks#método-de-relatório) para obter mais informações sobre os cliques bloqueados e investigar as fontes (IDs de agência/aplicativo) e os motivos dos cliques inválidos.
* Se você encontrar um problema com um aplicativo específico devido a uma integração fora do padrão, exclua esse aplicativo da validação de assinatura de cliques usando a [API de exclusão de aplicativo.](/docs/click-signing-for-ad-networks#excluir-método-de-aplicativo)
* Se você encontrar um problema com sua configuração:
  1. Continue executando no modo somente relatório.
  2. Corrija o seu processo de assinatura de cliques.
  3. Verifique os resultados no [relatório de assinatura de cliques](/docs/click-signing-for-ad-networks#método-de-relatório) e reative a validação de assinatura de cliques quando observar que os cliques estão sendo validados conforme o esperado.

</Accordion>

<div id="faq" />

<Accordion title="Perguntas frequentes">

| **P: Como podemos testar a assinatura de cliques sem afetar a produção?**<br /><br />**R**: Há duas maneiras de testar a assinatura de cliques:<ol><li>Use a [API de teste](/docs/click-signing-for-ad-networks#método-de-teste). Este método é útil durante a fase de desenvolvimento, para testar as assinaturas de cliques únicos.</li><li>Use o modo somente relatório. O modo somente relatório verifica as assinaturas nos cliques de produção e mostra o que seria bloqueado, mas não bloqueia cliques inválidos. Portanto, você pode testar se a assinatura de cliques funciona sem impactar o tráfego real.</li></ol> |
| --- |
| **P: Qual é a diferença entre um token de API e uma chave secreta?**<br /><br />**R**: **Token de API**: é usado para autorizar e executar a API de assinatura de cliques. Há apenas um por ad network. O <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">token da API V2.0 do AppsFlyer</Anchor> deve ser obtido com o administrador<br /><br />**Chave secreta**: é usada para gerar a assinatura. Use o [método de geração de chave secreta](/docs/click-signing-for-ad-networks#método-de-geração-de-chave-secreta) para criar chaves secretas. A ad network é responsável por gerar novas chaves secretas. Veja a [seção de traits](/docs/click-signing-for-ad-networks#traits) para mais informações. |
| **P: Podemos aplicar a assinatura de cliques apenas a determinadas campanhas?**<br /><br />**R**: Não. A assinatura de cliques é aplicada a todos os cliques de uma ad network. Você pode excluir determinados aplicativos da assinatura de cliques, mas não pode excluir apenas determinadas campanhas. |

</Accordion>

<div id="traits" />

<Accordion title="Características">

| Caraterística | A descrição |
| --- | --- |
| Assinatura de cliques | A assinatura deve ocorrer nos servidores da ad network. |
| Chave secreta | <ul><li>As ad networks podem ter no máximo duas chaves secretas ativas simultaneamente.</li><li>Cada chave secreta tem uma data de validade.</li><li>Cliques assinados com chaves secretas expiradas são rejeitados.</li></ul> |
| API de relatórios | Estatísticas atualizadas de validade de cliques são agregadas de hora em hora. |

</Accordion>

<div data-zendesk-anchors="about-click-signing=sobre-assinatura-de-cliques h_01HNWC70BPGDJAG3X8M5Z2RHQ4=sobre-assinatura-de-cliques click-signature-integration=integra%C3%A7%C3%A3o-de-assinatura-de-cliques h_01HNWC70BPFYMZ56GTPV3W6DXA=integra%C3%A7%C3%A3o-de-assinatura-de-cliques flow=fluxo h_01HNWC70BPMXTKF9NZBYGCB874=fluxo procedure=procedimento h_01HNWC70BPHCAGD1ECA56CC1Q6=procedimento h_01HNWC70BPAR4QNTNSFE1JZM2J=observa%C3%A7%C3%A3o list-of-attributes=criando-uma-assinatura-de-clique h_01HP4A42YYFFF6M4VEH84KRTTK=criando-uma-assinatura-de-clique h_01HNWD3XYWFRY262HZZVAVWACR=lista-de-atributos attribute-rules=regras-de-atributos-e-json h_01HNWE3A19RM7757B707TWZ6G0=regras-de-atributos-e-json order-and-appearance-of-attributes=ordem-e-apar%C3%AAncia-dos-atributos h_01HNWE3A1920YQGZX2VG4X3M4B=ordem-e-apar%C3%AAncia-dos-atributos empty-attributes=atributos-vazios h_01HNYRZ1DPDDQ5H8RFYKAQWVKP=atributos-vazios json-data-structure=estrutura-de-dados-json h_01HNYS6R7F0MNPBN08TXKQS5DV=estrutura-de-dados-json attribute-value-escaping=valor-do-atributo-escapando h_01HNYSEBGD1DBSV2MHS7DZ75HS=valor-do-atributo-escapando json-spaces=espa%C3%A7os-no-json h_01HNYSY42HS1RXFG7T7QS9B0TK=espa%C3%A7os-no-json signature-algorithm=algoritmo-de-assinatura h_01HNYSJDFWAM9RREYH4M8DZQJA=algoritmo-de-assinatura signature-example=exemplo-de-assinatura h_01HP3YAN03BWVA30JP1JAFZYAG=exemplo-de-assinatura h_01HP3Y2Z65BN0SZ56XSHD52MSY=building-a-signature-example code-example=exemplos-de-c%C3%B3digo h_01HNYT8Z33M69JAS72MQ03YX0M=exemplos-de-c%C3%B3digo h_01HP3XVEJTBBVKZYEBZT62PR20=signingsupportedparamsjson h_01HP3XVEJTWWJVDBK5PGQH7DJY=signatureexamplego click-signature-apis=apis-de-assinatura-de-clique h_01HNWC70BPNEVT00S040TQ9KVD=apis-de-assinatura-de-clique click-signature-apis::58bf03c7=apis-de-assinatura-de-clique-1 h_01HNWC70BPR8XXC3TQCAZSGFZS=apis-de-assinatura-de-clique-1 legacy-versions=vers%C3%B5es-legadas h_01HNZ3YMFRWFDY751EBA58V6Q0=vers%C3%B5es-legadas h_01HNWCYB2YXCVGCP38GRBAJYQ4=v1-legacy generate-secret-key-method=m%C3%A9todo-de-gera%C3%A7%C3%A3o-de-chave-secreta h_01HNWC70BPBPSX1WKJJC2W6H69=m%C3%A9todo-de-gera%C3%A7%C3%A3o-de-chave-secreta h_01HNWC70BPPBK2S38KA6RQSTCN=generate-secret-key-basics h_01HNWC70BP40D5XN8DZQHSDZ5K=api-request parameters=par%C3%A2metros h_01HNWC70BPS83JD78JWQYK1NX9=par%C3%A2metros h_01HNWC70BPQC37602GV8GQPSEQ=json-response h_01HNWC70BP7V8KRW4861PXC2PX=generate-secret-key-curl-example-and-response h_01HNWC70BPKTPZEKFD37B6YQMH=http-response-codes response-codes=c%C3%B3digos-de-resposta h_01HNWC70BPMQ8Q94JD5CBT5RHZ=c%C3%B3digos-de-resposta revoke-secret-key-method=m%C3%A9todo-de-revoga%C3%A7%C3%A3o-de-chave-secreta h_01HNWC70BP8V05Q04J6EVGAS9T=m%C3%A9todo-de-revoga%C3%A7%C3%A3o-de-chave-secreta h_01HNWC70BP69ZJERY1Z03A5V4C=revoke-secrete-key-basics h_01HNWC70BPN01BNKKC7T9QMF44=api-request::3f5b6d35 parameters::f8e4d5cf=par%C3%A2metros-1 h_01HNWC70BPQ5S06E210RTE7E6R=par%C3%A2metros-1 h_01HNWC70BPBQA0ME8D6TZEM2EB=generate-secret-key-curl-example-and-response::5a4174fc h_01HNWC70BP9AV6PPEZNPQWJN85=http-response-codes::7dc4ee64 response-codes::d802debd=c%C3%B3digos-de-resposta-1 h_01HNWC70BPN18MB98KWND886QN=c%C3%B3digos-de-resposta-1 test-method=m%C3%A9todo-de-teste h_01HNWC70BPKEVRDMT8N4HMC98W=m%C3%A9todo-de-teste h_01HNWC70BPX4TH2MNE4GJBGHRG=test-basics h_01HNWC70BP5X2MZ3AC8BF69XYK=api-request::b2432cce parameters::7d3f0c33=par%C3%A2metros-2 h_01HNWC70BPKQFVEGWR9QT566YX=par%C3%A2metros-2 h_01HNWC70BPM50T2JEGJF41GGX4=json-response::cd966b82 h_01HNWC70BPSQYQ5R7PJE4CAKYG=test-curl-example-and-response h_01HNWC70BP8SSK2E5DFAD2Q6NP=http-response-codes::22d1011c response-codes::a79c47f4=c%C3%B3digos-de-resposta-2 h_01HNWC70BPC43F5H85F56DDSQR=c%C3%B3digos-de-resposta-2 configure-mode-method=m%C3%A9todo-de-modo-de-configura%C3%A7%C3%A3o h_01HNWC70BP6NPF7NSF0MGA4BJ3=m%C3%A9todo-de-modo-de-configura%C3%A7%C3%A3o h_01HNWC70BPKNAVCD57D2E7FX8F=configure-mode-basics h_01HNWC70BQFCJCHHVQHKWB57GF=api-request::1ede8b9c parameters::2fff2a1b=par%C3%A2metros-3 h_01HNWC70BQSQ7YWZVQB9A4DZQW=par%C3%A2metros-3 h_01HNWC70BQF0J2TZF181BW0MKT=configure-mode-curl-example h_01HNWC70BQ9HNQV7HA45ZXA2Z3=http-response-codes::b3328f8b response-codes::fe5a5b10=c%C3%B3digos-de-resposta-3 h_01HNWC70BQZ657X25N8JGM57A1=c%C3%B3digos-de-resposta-3 configure-circuit-breaker-method=configurar-m%C3%A9todo-de-interruptor h_01HNWC70BQVSFS7G330NF4XHEP=configurar-m%C3%A9todo-de-interruptor h_01HNWC70BQ097J2VXW0XKSH3M9=configure-circuit-breaker-basics h_01HNWC70BQJWZYZEDJJ5J7JX6X=api-request::ef73eae0 request-body-json=corpo-da-solicita%C3%A7%C3%A3o-json h_01HNWC70BQ6R955776Y6H4EZRG=corpo-da-solicita%C3%A7%C3%A3o-json h_01HNWC70BQRZEZ4PTV59FGYS4Z=configure-circuit-breaker-curl-example-and-response h_01HNWC70BQPP5X9JH1HJ1K58H4=http-response-codes::d35e3a62 response-codes::b056f2a3=c%C3%B3digos-de-resposta-4 h_01HNWC70BQWQ5KWZX8BM0A7BC5=c%C3%B3digos-de-resposta-4 get-configuration-method=obter-m%C3%A9todo-de-configura%C3%A7%C3%A3o h_01HNWC70BQZY6TYSQBWZ17S0W5=obter-m%C3%A9todo-de-configura%C3%A7%C3%A3o h_01HNWC70BQY6CPZA5A56J3TET0=get-configuration-basics h_01HNWC70BQ444XNRRCZZH2GFJH=api-request::a2a93b39 h_01HNWC70BQJ8J2WGXE2QF144FK=json-response::fee92c h_01HNWC70BQ701HZR6PYC0CW88T=get-configuration-curl-example-and-response h_01HNWC70BQ8R5GR906Y9W79E81=http-response-codes::90a409c response-codes::ebf1292a=c%C3%B3digos-de-resposta-7 h_01HNWC70BQDGVBZ94F0N49FF40=c%C3%B3digos-de-resposta-7 report-method=m%C3%A9todo-de-relat%C3%B3rio h_01HNWC70BQTBMNKHV4RH4ZQ0AE=m%C3%A9todo-de-relat%C3%B3rio h_01HNWC70BQ4K7T3FXZWV5KW3FM=report-basics h_01HNWC70BQMBD2WNVQH69FMSPR=api-request::b28cedb0 parameters::e6795217=par%C3%A2metros-4 h_01HNWC70BQ0FDT4T2RAJEPAHNC=par%C3%A2metros-4 h_01HNWC70BQRZTXMKD30V7QQPE4=csv-response h_01HNWC70BQV61TVE65TQ3WWGCP=test-curl-example-and-response::66e922 h_01HNWC70BQQ3MP256QK0JT2K78=http-response-codes::8454f45d response-codes::a8a9822d=c%C3%B3digos-de-resposta-8 h_01HNWC70BQTPPWA4SNG25E8FFB=c%C3%B3digos-de-resposta-8 exclude-app-method=excluir-m%C3%A9todo-de-aplicativo h_01HNWC70BQ9SK2XCBGGHXVMRDV=excluir-m%C3%A9todo-de-aplicativo h_01HNWC70BQ8GGRTQ1RW1KCY0SQ=exclude-app-method-basics h_01HNWC70BQ4D62SZCHKGEP6RMJ=api-request::1054abca parameters::f5e3c6ce=par%C3%A2metros-5 h_01HNWC70BREG4XQJV3X9518FC5=par%C3%A2metros-5 h_01HNWC70BR2PVDHTG64WZ36KPV=exclude-app-curl-example h_01HNWC70BR7XCTW6N69GEB4ARF=http-response-codes::7991b66 response-codes::addfcfd8=c%C3%B3digos-de-resposta-8 h_01HNWC70BRN8BHWF6WGY2RH45X=c%C3%B3digos-de-resposta-8 remove-excluded-app-method=remover-m%C3%A9todo-de-aplicativo-exclu%C3%ADdo h_01HNWC70BR18P0H96VN64RS05G=remover-m%C3%A9todo-de-aplicativo-exclu%C3%ADdo h_01HNWC70BRAWBGC5EE0Q8XBTW1=remove-excluded-app-method-basics h_01HNWC70BRD885KN6YDXQ9GXS2=api-request::9504d16f parameters::34936c8f=par%C3%A2metros-6 h_01HNWC70BR4ADH7T3AFG58FZH6=par%C3%A2metros-6 h_01HNWC70BRK7DM7MW150AFVKG2=remove-excluded-app-curl-example h_01HNWC70BRMFN4RM65YV2NWR29=http-response-codes::b5e059da response-codes::e8de940a=c%C3%B3digos-de-resposta-8 h_01HNWC70BRHA8AA7ZV1R4EBYJH=c%C3%B3digos-de-resposta-8 h_01HNWC70BRTZZWME7QCP8HV9AY=code-sample additional-information=informa%C3%A7%C3%B5es-adicionais h_01HNWC70BRN0NGTQVWED6VG81Y=informa%C3%A7%C3%B5es-adicionais h_01HNWC70BRS884G8RCMAPFPV1N=troubleshooting h_01HNWC70BRP3BVJSHSD1CPCB9S=faq h_01HNWC70BRDN37MBTEKT0DH8CT=traits" />
