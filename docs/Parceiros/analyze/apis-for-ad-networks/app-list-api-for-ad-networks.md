---
title: API de lista de aplicativos para ad networks
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
  edited_at: '2026-08-18T00:37:58Z'
  id: 360011700857
  locale: pt
  section: APIs for ad networks
  section_id: 6551618728209
  url: https://support.appsflyer.com/hc/pt/articles/360011700857
---
> **Em resumo:** As ad networks podem recuperar metadados dos aplicativos associados à conta de parceiro integrada.

## API para obter a lista de aplicativos

As seções a seguir incluem as informações necessárias para usar a API.

<div id="get-app-list-basics" />

<Accordion title="Get app list basics">

<table><thead><tr><th>Categoria</th><th>Item</th><th><span>A descrição</span></th></tr></thead><tbody><tr><td rowspan="3">Solicitação</td><td>Método HTTP</td><td><code>BAIXAR</code></td></tr><tr><td>Caminho</td><td><span>https://hq1.appsflyer.com/api/mng/apps</span></td></tr><tr><td>Cabeçalho de autorização </td><td><ul><li>O cabeçalho de autorização obrigatório contém um token Bearer. </li><li>O administrador obtém o token no dashboard da seguinte forma: <a href="/marketers/pt/docs/managing-appsflyer-tokens" target="_blank">O administrador acessa a lista suspensa de e-mail &gt; tokens de API para obter o token V2.0</a> </li></ul></td></tr><tr><td rowspan="3"> Tempo de</td><td>Resultados</td><td>Retorno em JSON</td></tr><tr><td>Limite de solicitação</td><td><ul><li>20 solicitações/minuto</li><li>100 solicitações/dia</li></ul></td></tr><tr><td>Limite de registros</td><td>1,000 registros/solicitação. Se for necessário retornar mais de 1,000 registros, use solicitações de paginação subsequentes, descritas neste artigo.</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="Solicitação de API">

A solicitação da API consiste no método, no caminho, no parâmetro obrigatório capabilities e nos parâmetros opcionais de paginação. O token está contido no cabeçalho de autorização.

**Mensuração**

```http
GET https://hq1.appsflyer.com/api/mng/apps?capabilities={capabilities} 
```

#### Parâmetros obrigatórios para obter a lista de aplicativos

<Table>
  <thead>
    <tr>
      <th>
        Parâmetro de consulta
      </th>
      <th>
        A descrição
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        capacidades
      </td>
      <td>
        Para obter a lista e o número de aplicativos para os quais você tem permissões/recursos de integração, defina o parâmetro capabilities como uma das opções listadas.

        | Opção | Tipo de valor esperado | A descrição |
        | --- | --- | --- |
        | `protect_360` | Permissão de relatório | Obter <Anchor target="_blank" href="/partners/pt/docs/protect360-for-integrated-partners">relatórios de dados brutos do Protect360 para ad networks</Anchor> |
        | `cost` | integração | O aplicativo está habilitado para obter dados de custo <Anchor target="_blank" href="/partners/pt/docs/incost-api-for-ad-networks">pela API InCost</Anchor> |

        **Exemplo**: lista de aplicativos para os quais você tem permissão da API de relatórios de dados brutos do Protect360:`capabilities=protect_360`
      </td>
    </tr>
  </tbody>
</Table>

#### **Mecanismo de paginação**

Um mecanismo de paginação, sempre operacional, é implementado.

**Princípios de paginação:**

* Retorna até 1.000 registros por solicitação (página).
* Os JSONs de resposta contêm as seguintes chaves relacionadas à paginação:
  * **meta.total\_items**: O número de registros a serem retornados por todas as páginas combinadas. Isso representa o número de aplicativos para os quais você recebeu as capacidades consultadas.
  * Os links de paginação (mostrados no JSON a seguir) têm as seguintes chaves:
    * **links.prev**: Se houve uma solicitação anterior: a solicitação usada para gerar a página anterior.
    * **links.self**: A solicitação atual: a solicitação usada para gerar o JSON atual (página)
    * **links.next**: A solicitação necessária para obter a próxima página. Se não houver a próxima chave, esta é a última página.

**Use um dos seguintes métodos de controle de paginação:**

* [Melhores práticas] Use os links no JSON: se a chave links.next existir, use-a para criar uma solicitação para obter a próxima página. Continue fazendo isso até receber um JSON sem uma chave links.next.
* Implemente programaticamente os parâmetros limit e offset em conjunto com a chave total\_items.

**Exemplo de JSON de links de paginação**

* O exemplo a seguir contém o resultado da primeira solicitação, consistindo na resposta à segunda solicitação, que contém dois registros na seção de dados (não exibida).
* O número total de registros a serem retornados é 6.
* A chave **links.next** contém a solicitação que retorna a próxima página — registros 5 e 6.

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

#### Parâmetros do mecanismo de paginação (opcional)

<table><thead><tr><th>Parâmetro de consulta</th><th>Visão geral</th></tr></thead><tbody><tr><td>limit</td><td><p>Número de registros retornados por chamada</p><ul><li>Máximo: 1.000</li><li>Se você não enviar<code>limit</code>, ele será definido automaticamente como 1.000.</li><li>Exemplo: <code>limit=2</code> </li><li>Obrigatoriedade: Não</li></ul></td></tr><tr><td>offset</td><td><p>O primeiro registro a ser retornado na chamada. Os números dos registros começam em 0. </p><ul><li>Se você não enviar <code>offset</code>, ele será automaticamente definido como 0.</li><li>Exemplo: <code>offset=2</code> </li><li>Obrigatoriedade: Não</li></ul></td></tr><tr><td colspan="2"> </td></tr></tbody></table>

</Accordion>

<div id="json-response" />

<Accordion title="Resposta JSON">

| **Chave** | **Visão geral** |
| --- | --- |
| id | ID do aplicativo, por exemplo: `id123456789`, `com.myapp.com` |
| Tipo | Sempre retornar `app` |
| coluna | Nome do aplicativo |
| plataforma | as integrações de SDK do iOS e Android |
| símbolos monetários | Código de moeda específico do aplicativo, conforme definido pelo anunciante |
| time\_zone | Fuso horário específico do aplicativo, conforme definido pelo anunciante |
| total\_items | Número de aplicativos para os quais a ad network tem a opção de recursos solicitados |
| links | Mecanismo de paginação (explicado na seção de parâmetros)<ul><li>prev: a chamada usada para gerar a página anterior</li><li>self: a chamada usada para gerar a página atual</li><li>next: a chamada usada para gerar a próxima página</li></ul> |

</Accordion>

<div id="get-app-list-curl-example-and-response" />

<Accordion title="Exemplo de curl e resposta para obter a lista de aplicativos">

**Solicitação Curl**

Este exemplo inclui uma chamada completa, inclusive parâmetros de paginação opcionais.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/mng/apps?capabilities=protect_360&limit=1000&offset=0' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Resposta JSON**

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

<Accordion title="Códigos de resposta HTTP">

| Código | Mensagem | Observações/solução de problemas |
| --- | --- | --- |
| 200 | OK | Dados válidos retornados |
| 200 | OK | **Sintoma**: Nenhum dado é retornado<br /><br />**Ação**: Certifique-se de que o token de autenticação esteja no cabeçalho Bearer. |
| 400 | Pedido incorreto | <ul><li>Veja a mensagem contida no JSON</li><li>JSON vazio: funcionalidade especificada ilegal</li></ul> |
| 401 | Não autorizado | **Mensagem**: O token de autorização está malformado<br /><br />Certifique-se de que você tem o token correto; o token deve ter mais de 700 caracteres. |
| 404 | Não encontrado | <ul><li>Resolva quaisquer problemas relacionados à network ou ao firewall.</li><li>Certifique-se de que os <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-server-ip-address-ranges-allowlisting">endereços IP da AppsFlyer estejam na lista de permissões</Anchor></li><li>Certifique-se de usar o token emitido mais recentemente.</li><li>Nenhum dado encontrado: o tipo de permissão/integração (recursos) solicitado é válido, mas nenhum aplicativo com permissão foi encontrado.</li></ul> |
| 429 | Pedidos em excesso | Limite de taxa de requisições excedido |

</Accordion>

<div data-zendesk-anchors="get-app-list-api=api-para-obter-a-lista-de-aplicativos h_01KQS54YXJ2XBV5BAT3TGJ9SBT=api-para-obter-a-lista-de-aplicativos h_01KQS54YXJHYS9KC2Y7BEP87MZ=get-app-list-basics h_01KQS54YXJJ9SE7DSRTA2X2A9M=api-request get-app-list-mandatory-parameters=par%C3%A2metros-obrigat%C3%B3rios-para-obter-a-lista-de-aplicativos h_01KQS54YXJPDZGJB7K6KH1D2W1=par%C3%A2metros-obrigat%C3%B3rios-para-obter-a-lista-de-aplicativos pagination-mechanism=mecanismo-de-pagina%C3%A7%C3%A3o h_01KQS54YXJ9X0XBJQ01K6WK2RB=mecanismo-de-pagina%C3%A7%C3%A3o pagination-mechanism-parameters-optional=par%C3%A2metros-do-mecanismo-de-pagina%C3%A7%C3%A3o-opcional h_01KQS54YXJX943PMF5JWV67THW=par%C3%A2metros-do-mecanismo-de-pagina%C3%A7%C3%A3o-opcional h_01KQS54YXJS43JYQQHCWCAED6Q=json-response h_01KQS54YXJJK7Y23TSSF1BB58R=get-app-list-curl-example-and-response h_01KQS54YXJ2638DBZWDSN4J9G4=http-response-codes" />
