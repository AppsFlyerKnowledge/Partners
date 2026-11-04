---
title: Macros de postback para ad networks
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
  edited_at: '2026-08-19T00:37:37Z'
  id: 207273946
  locale: pt
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/pt/articles/207273946
---
> **Resumo:** Como uma ad network, você pode definir o conteúdo e os endpoints dos postbacks enviados a você como parte da sua integração com a AppsFlyer. Postbacks dizem respeito ao engajamento do usuário do aplicativo, como instalações, eventos in-app, reengajamentos e assim por diante.

Guias relacionados a postbacks para parceiros integrados:

* <Anchor target="_blank" href="/partners/pt/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Privacidade avançada</Anchor>
* <Anchor target="_blank" href="/partners/pt/docs/skan-integration-guide-for-ad-networks">Proteção contra fraudes</Anchor>
* <Anchor target="_blank" href="/partners/pt/docs/rejected-attribution-postbacks-to-integrated-partners">Postbacks de atribuição rejeitados</Anchor>

<div id="postbacks-for-ad-networks" />

## Postbacks para ad networks

* **Configuração do postback:** para solicitar alterações em suas configurações de postback, use o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor> ou entre em contato com seu partner development manager da AppsFlyer.
* **Tipo de postback**: os postbacks estão disponíveis para eventos de instalação e eventos in-app e para instalações e eventos in-app bloqueados por conta de fraudes identificadas pelo Protect360 ou que violam as Regras de Validação de Direcionamento.

<div id="postback-data-sources" />

### Fontes de dados de postback

| Fonte | Descrição |
| --- | --- |
| <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">Parâmetros do link de atribuição</Anchor> | Parâmetros oferecidos pelo parceiro em URLs de clique e de impressão<br /><br />Exemplo: parâmetro do click ID no link de atribuição - "&click\_id=CLICK\_ID" |
| IDs de parceiros na AppsFlyer | IDs exclusivos oferecidos ao anunciante pelo parceiro<br /><br />Exemplos: App ID, Account ID, User ID, Network ID. |
| Informações derivadas do SDK | Informações extraídas do dispositivo pelo SDK da AppsFlyer.<br /><br />Exemplo: device IDs do iOS podem ser extraídas usando "&IDFA=(idfa)" no postback |
| Derivada da plataforma AppsFlyer | Informações derivadas da plataforma AppsFlyer. |
| Protect360 e regras de validação | Informações sobre instalações identificadas como fraudes e instalações que violam regras de segmentação de campanhas e seus eventos in-app associados. |

<div id="postback-macros" />

## Macros de postback

Quando incluídas em um postback, as macros são substituídas por dados relevantes ao usuário. Por exemplo, para obter o endereço de IP do usuário que instala o aplicativo, inclua `country_code=(ip)` na estrutura de postback. As macros compatíveis estão listadas na tabela a seguir:

As colunas na tabela abaixo têm o seguinte significado:

* **Fonte:** de onde os dados vêm.
  * Link: links de atribuição
  * SDK: SDK da AppsFlyer incorporado no aplicativo ou na S2S API
  * AF: após o processamento pela AppsFlyer.
* **Enviar tudo**: se sim, você pode receber os dados de instalações e eventos atribuídos a outras networks ou orgânicos. (ou seja, não atribuídos a você).
* **[Base] Macros para todos os postbacks**: macros relevantes para postbacks de instalação, eventos no aplicativo e eventos rejeitados
* **[Opcional]** para eventos in-app e eventos rejeitados conforme indicado na coluna (rejeitado, in-app)

<div id="macrosinstalls-in-app-events-and-rejected-events" />

### Macros—instalações, eventos in-app e eventos rejeitados

| Macro do postback (nome) | Fonte | Enviar tudo | Descrição | [Base] Macros para todos os postbacks | [Opcional] Eventos in-app e rejeitados |
| --- | --- | --- | --- | --- | --- |
| <span id="advertising_id"></span>advertising\_id | SDK | Sim | device ID que pode ser resetado pelo usuário, conhecido também como GAID. Também disponível como: (sha1-advertiserId) | Sim |  |
| <span id="af_ad"></span>af\_ad | Link | Não | Nome do anúncio (<Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#níveis-de-granularidade-de-dados">ver mais</Anchor>) fornecido pelo anunciante/publisher. | Sim | Sim |
| <span id="af_ad_id"></span>af\_ad\_id | Link | Não | Fornecido pelo anunciante/publisher. | Sim | Sim |
| <span id="af_ad_type"></span>af\_ad\_type | Link | Não | Use a seguinte convenção de nomenclatura:<ul><li>**text:** uma unidade de anúncios contendo apenas texto, por exemplo, um resultado de pesquisa</li><li>**banner:** um formato básico que aparece na parte superior ou inferior da tela do dispositivo</li><li>**interstitial:** um anúncio de página inteira que aparece durante pausas na experiência vigente</li><li>**video:** um vídeo padrão, ou seja, não recompensado</li><li>**rewarded\_video:** uma unidade de anúncio que oferece recompensas no aplicativo em troca de assistir a um vídeo</li><li>**playable:** uma unidade de anúncio que contém uma visualização interativa da experiência do aplicativo</li><li>**sponsored\_content:** um link incluído em um pedaço de conteúdo patrocinado, como um artigo publicitário</li><li>**audio:** um anúncio em áudio</li></ul> | Sim | Sim |
| <span id="af_adset"></span>af\_adset | Link | Não | <ul><li>Fornecido pelo anunciante/publisher.</li><li>Adset é um nível intermédio entre Campanha e Anúncio. <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#níveis-de-granularidade-de-dados">Saiba mais</Anchor></li></ul> | Sim | Sim |
| <span id="af_adset_id"></span>af\_adset\_id | Link | Não | Fornecido pelo anunciante/publisher. | Sim | Sim |
| <span id="af_c_id"></span>af\_c\_id | Link | Não | Fornecido pelo anunciante/publisher. | Sim | Sim |
| <span id="af_siteid"></span>af\_siteid | Link | Não | <ul><li>ID exclusivo que identifica o publisher que exibe o anúncio. <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#site-id-parameter">Saiba mais</Anchor></li></ul> | Sim | Sim |
| <span id="af_subsite_id"></span>af\_subsite\_id | Link | Não | <ul><li>Ad sub-network/Publisher ID.</li><li>Se, além do publisher principal (site ID), houver um sub-publisher, ou você desejar incluir informações adicionais, como tipo de anúncio/posicionamento dentro do aplicativo, como banner, intersticial, vídeo etc, use af\_sub\_siteid. Exemplo: af\_sub\_siteid=ABCD\_4567</li></ul> | Sim | Sim |
| <span id="af_validated"></span>af\_validated | AF | Sim | Indica se a compra foi validada com sucesso. Valores possíveis: true ou false. | Sim |  |
| <span id="af_validation_type"></span>af\_validation\_type | AF | Sim | Indica o tipo de validação realizada. Valores possíveis: roi360\_purchase, roi360\_subscription, ou Basic. | Sim |  |
| <span id="app_id"></span>ativado | SDK | Sim | O ID do aplicativo conforme relatado pelo aplicativo | Sim |  |
| <span id="app_name"></span>ativado | SDK | Sim | Nome do aplicativo definido pelo anunciante | Sim |  |
| <span id="app_version"></span>app\_version | SDK | Sim | Nome da versão do aplicativo definido pelo desenvolvedor no código do aplicativo | Sim |  |
| <span id="appsflyer_id"></span>appsflyer\_id | SDK | Sim | Identificador exclusivo da AppsFlyer registrado na conversão | Sim |  |
| <span id="att01"></span>att-0-1 | SDK | Sim | Valores possíveis:<ul><li>1: o status da ATT é autorizado ou af\_authorized.</li><li>0: qualquer outro status da ATT.</li></ul> | Sim |  |
| <span id="attstatus"></span>att-status | SDK | Sim | O <Anchor target="_blank" href="/marketers/pt/docs/att-implications-ios-14-and-deprecation-of-lat#valores-att">status da ATT</Anchor> relatado pelo iOS. Como authorized, not\_determined.<br /><br />Em alguns casos, não há valor e "" é retornado. | Sim |  |
| <span id="attributed_touch_type"></span>tipo\_de\_toque\_atribuído | SDK | Não | Valores possíveis: clique, impressão, TV, pré-instalação | Sim |  |
| <span id="blocked_reason"></span>blocked\_reason | AF | Não | Fraude/motivo das regras de validação | Não | Rejeitado |
| <span id="blocked_reason_value"></span>blocked\_reason\_value | AF | Não | Valor da fraude ou do motivo das regras de validação (como site ID) | Não | Rejeitado |
| <span id="blocked_sub_reason"></span>blocked\_sub\_reason | AF | Não | Submotivo das regras de fraude e validação | Não | Rejeitado |
| <span id="bundle_id"></span>bundle\_id | SDK | Sim | iOS: identificação para corresponder a um único aplicativo ou a um grupo de aplicativos no iOS (consulte bundle ID de desenvolvedor da Apple) Android: o nome do aplicativo | Sim |  |
| <span id="c"></span>C | Link | Não | Fornecido pelo anunciante/publisher. Os nomes de campanhas que excedem 100 caracteres são exibidos no dashboard como 'c\_name\_exceeded\_max\_length' | Sim | Sim |
| <span id="country_code"></span>código\_país | AF | Sim | Código do país usando ISO 3166 (alfa-2) Exemplo: EUA, CN. | Sim |  |
| <span id="event_name"></span>nome\_do\_evento | SDK | Sim | Nome escolhido para um evento | Não | No aplicativo |
| <span id="event_revenue_currency"></span>event\_revenue | SDK | Sim | Valor do evento reportado pelo SDK usando event\_revenue\_currency ou a moeda selecionada por você. | Não | No aplicativo |
| {"event_revenue"}  <br />{"_moeda"} | SDK | Sim | O código da moeda da receita do evento reportada no evento, ou a moeda selecionada por você | Não | No aplicativo |
| <span id="event_revenue_usd"></span>event\_revenue\_USD | AF | Sim | Valor do evento em USD | Não | No aplicativo |
| <span id="event_time"></span>event\_time | SDK | Sim | Hora do evento | Não | No aplicativo |
| <span id="event_value"></span>event\_value | SDK | Sim | Eventos in-app incluem atributos com valores, que podem ser enviados inteiramente no postback em formato JSON. URL codificada usando a macro (codificada). | Não | No aplicativo |
| <span id="idfa"></span>idfa | SDK | Sim | User advertising ID reconfigurável encontrado em dispositivos iOS. Também disponível como: (sha1-idfa) | Sim |  |
| <span id="idfv"></span>idfv | SDK | Sim | Identificador exclusivo para cada usuário e fornecedor em dispositivos iOS | Sim |  |
| <span id="imei"></span>imei | SDK | Sim | Um número exclusivo usado para identificar telefones celulares | Sim |  |
| <span id="install_time"></span>install\_time | SDK | Sim | Timestamp de data/hora da instalação | Sim |  |
| <span id="install_unix_ts"></span>install\_unix\_ts | SDK | Sim | Timestamp de data/hora de instalação no formato unix | Sim |  |
| <span id="is_attributed"></span>is\_attributed | AF | Sim | Uma flag que indica se a instalação ou evento foi atribuído a essa fonte de mídia | Sim |  |
| <span id="is_contrib"></span>is\_contrib | AF | Sim | Indica se a ad network estava entre os 3 principais contribuintes para uma instalação.<ul><li>Se a ad network não ganhou a atribuição, mas está entre os 3 principais contribuintes, `is_contrib=1`.</li><li>Se a ad network ganhou a atribuição, `is_contrib=0`.</li><li>Se a ad network não está entre os 3 principais contribuintes, `is_contrib=0`.</li></ul> | Sim |  |
| <span id="is_lat"></span>is\_lat | SDK | Sim | Limit ad tracking (LAT): iOS: A partir do iOS 14, o LAT foi descontinuado pela Apple. Determina o status de privacidade do usuário usando a ATT. Nesse caso, ignore o is\_lat. Antes do iOS 14, se true, o IDFA não estava disponível e era definido como 0. Android: Quando true, o usuário optou por não receber anúncios baseados em interesses. Isso não impede a coleta de GAID. | Sim |  |
| <span id="is_organic"></span>is\_organic | AF | Sim | Se um postback de instalação for enviado para todas as fontes de mídia, incluindo orgânicas, a ad network receberá uma indicação se a instalação foi orgânica ou não orgânica. | Somente instalações |  |
| <span id="is_primary_attribution"></span>é\_atribuição\_primária | AF | Sim | Se false, veja is\_retargeting. | Não | No aplicativo |
| <span id="is-reinstall"></span>is\_reinstall | AF | Não | Se for verdadeiro, o evento é reportado como <Anchor target="_blank" href="/marketers/pt/docs/measure-reinstalls">uma reinstalação</Anchor>. |  |  |
| <span id="is_retargeting"></span>is\_retargeting | Link | Sim | Use junto com is\_primary\_attribution. Saiba mais sobre a <Anchor target="_blank" href="/marketers/pt/docs/resolve-retargeting-double-attribution">atribuição duplicada de eventos de retargeting.</Anchor><br /><br />Se true (1), o evento é relatado como parte de uma campanha de retargeting e a fonte de mídia é a fonte de mídia de retargeting.<br /><br />Se false (0) e is\_primary\_attribution for false, o evento fará parte de uma campanha de retargeting, mas a fonte de mídia referenciada é a fonte de mídia de atribuição do usuário | Sim |  |
| <span id="language"></span>language | SDK | Sim | Idioma relatado pelo dispositivo e definido pelo sistema operacional do dispositivo. | Sim |  |
| <span id="oaid"></span>OAID | SDK | Sim | User ID reconfigurável em alguns dispositivos Android, geralmente como alternativa ao GAID | Não |  |
| <span id="partner_event_id"></span>partner\_event\_id | AF | Sim | Nome/ID do evento correspondente na plataforma do parceiro | Sim | No aplicativo |
| <span id="platform"></span>platforma | SDK | Não | Plataforma do dispositivo: iOS, Android ou Windows Mobile | **Enviar tudo**: se sim, você pode receber os dados de instalações e eventos atribuídos a outras redes ou orgânicos (ou seja, não atribuídos a você). |  |
| <span id="retargeting-conversion-type"></span>retargeting\_conversion\_type | AF | Não | Uma flag aparecerá se for uma reatribuição ou reengajamento | Somente retargeting |  |

<div id="in-app-event-only-macros" />

### Macros somente para eventos in-app

Os exemplos abaixo dizem respeito dos postbacks de eventos in-app disponíveis para parceiros.

<div id="example" />

> 📄 **Exemplo**
>
> O modelo de postback de evento "&event=(event)&json=(encode)" foi convertido para o seguinte postback para um evento específico af\_purchase:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> O valor descriptografado de JSON deste postback é
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

<div id="encoded-values" />

#### **Valores criptografados**

Os postbacks podem conter caracteres irregulares, que não são alfanuméricos. Para transferir esses valores corretamente por meio de postbacks, a URL da AppsFlyer criptografa valores não-alfa-numéricos.

Para descriptografar ou criptografar um postback, use um <Anchor target="_blank" href="https://www.urldecoder.org/">serviço web de criptografia.</Anchor>

<div id="sample-postbacks" />

## Postbacks de amostra

<div id="general-install-postback-examples" />

### Exemplos gerais de postbacks de instalação

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

### Exemplos gerais de postbacks de eventos in-app

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

### Exemplo de postback de evento in-app

Parâmetros do evento:

* Nome do evento: af\_revenue
* Receita do evento US$ 120,00
* moeda usada nos eventos. USD
* Valor do evento: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

Postback

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-ad-networks=postbacks-para-ad-networks 01JHFZWJT74GNA6J5MYMQBGDWX=postbacks-para-ad-networks postback-data-sources=fontes-de-dados-de-postback 01JHFZWJT978TTXB7FQ6AVG1ZS=fontes-de-dados-de-postback postback-macros=macros-de-postback 01JHFZWJTTP66NHZRG0RQAY3W8=macros-de-postback macros%E2%80%94installs-inapp-events-and-rejected-events=macrosinstala%C3%A7%C3%B5es-eventos-in-app-e-eventos-rejeitados 01JHFZWJTXD2K4RJ8RDWXKSYDD=macrosinstala%C3%A7%C3%B5es-eventos-in-app-e-eventos-rejeitados inapp-event-only-macros=macros-somente-para-eventos-in-app 01JHFZWK3FQ5HCX9NDEKT6SPT1=macros-somente-para-eventos-in-app 01JHFZWK3F2E31WE5N1G0T0ZHA=exemplo encoded-values=valores-criptografados 01JHFZWK3GM9XRS2GC4SNXFVD7=valores-criptografados sample-postbacks=postbacks-de-amostra 01JHFZWK3GJSA8RF4AMKVM4XD4=postbacks-de-amostra general-install-postback-examples=exemplos-gerais-de-postbacks-de-instala%C3%A7%C3%A3o 01JHFZWK3HD1NFJJW1Y8HGVPX2=exemplos-gerais-de-postbacks-de-instala%C3%A7%C3%A3o general-inapp-event-postback-examples=exemplos-gerais-de-postbacks-de-eventos-in-app 01JHFZWK3JW0D1GZ739FV0EZWG=exemplos-gerais-de-postbacks-de-eventos-in-app inapp-event-postback-example=exemplo-de-postback-de-evento-in-app 01JHFZWK3JT8GM7BEM3RXCMXV5=exemplo-de-postback-de-evento-in-app" />
