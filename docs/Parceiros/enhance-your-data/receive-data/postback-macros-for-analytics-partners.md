---
title: Macros de postback para Parceiros de análise
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
  edited_at: '2026-08-19T00:37:40Z'
  id: 360016751637
  locale: pt
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/pt/articles/360016751637
---
> **At a glance:** **Em resumo:** use macros como parte dos postbacks enviados aos Parceiros de análise para obter dados de atribuição relevantes.

## Postbacks para Parceiros de análise

Os Parceiros de análise podem definir o conteúdo e os endpoints dos postbacks enviados a eles como parte da integração com a AppsFlyer. Postbacks dizem respeito ao engajamento do usuário do aplicativo, como instalações, eventos in-app, reengajamentos e assim por diante.

* **Configuração do postback:** Para solicitar alterações nas suas configurações de postback, use o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget de assistente de parceiro</Anchor> para abrir um ticket ou entre em contato com seu gerente de desenvolvimento de parceiros da AppsFlyer.
* **Tipos de postback**: há postbacks disponíveis para instalação e eventos in-app.

## Macros de postback

Quando incluídas em um postback, as macros são substituídas por dados relevantes ao usuário. Por exemplo, para obter o endereço de IP do usuário que instala o aplicativo, inclua country\_code=(ip) na estrutura de postback. As macros compatíveis estão listadas na tabela a seguir:

* Fonte: de onde os dados vêm:
  * SDK: SDK da AppsFlyer incorporado no aplicativo ou na S2S API
  * AF: após o processamento pela AppsFlyer.
* **[Base]** **Macros para todos os postbacks**: macros relevantes para instalação e eventos in-app.
* **[Opcional]** para eventos in-app, conforme indicado na coluna.

#### Macros — instalações e eventos in-app

| Macro do postback (nome) | Fonte: | A descrição | [Base] Macros para todos os postbacks | [Opcional] Eventos in-app |
| --- | --- | --- | --- | --- |
| advertising\_id | SDK | device ID que pode ser resetado pelo usuário, conhecido também como GAID. Também disponível como: (sha1-advertiserId) | Yes |  |
| nome\_do\_evento | SDK | Nome escolhido para um evento |  | Yes |
| event\_revenue\_USD | AF | Valor do evento em USD |  | Yes |
| event\_revenue | SDK | Valor do evento reportado pelo SDK usando event\_revenue\_currency ou a moeda selecionada por você. |  | Yes |
| event\_currency | SDK | O código da moeda da receita do evento reportada no evento, ou a moeda selecionada por você. |  | Yes |
| event\_time | SDK | Data/hora do evento |  | Yes |
| event\_value | SDK | Eventos in-app incluem atributos com valores, que podem ser enviados inteiramente no postback em formato JSON. URL codificada usando a macro (codificada). |  | Yes |
| partner\_event\_id | AF | Nome/ID do evento correspondente na plataforma do parceiro |  | Yes |
| ativado | SDK | Nome do aplicativo definido pelo anunciante | Yes |  |
| appsflyer\_id | SDK | Identificador único da AppsFlyer registrado na conversão | Yes |  |
| tipo\_de\_toque\_atribuído | AF | Um sinalizador que indica se a atribuição ocorreu devido a uma exibição (1 = impressão, 0 = clique) | Yes |  |
| código\_país | AF | Código do país usando ISO 3166 (alfa-2) Exemplo: EUA, CN. | Yes |  |
| idfa | SDK | User advertising ID reconfigurável encontrado em dispositivos iOS. Também disponível como: (sha1-idfa) | Yes |  |
| idfv | SDK | Identificador exclusivo para cada usuário e fornecedor em dispositivos iOS | Yes |  |
| install\_time | SDK | Carimbo de data/hora da instalação | Yes |  |
| install\_unix\_ts | SDK | Timestamp de data/hora de instalação no formato unix | Yes |  |
| is\_lat | SDK | Limit ad tracking (LAT): iOS: A partir do iOS 14, o LAT foi descontinuado pela Apple. Determina o status de privacidade do usuário usando a ATT. Nesse caso, ignore o is\_lat. Antes do iOS 14, se true, o IDFA não estava disponível e era definido como 0. Android: Quando true, o usuário optou por não receber anúncios baseados em interesses. Isso não impede a coleta de GAID. | Yes |  |
| language | SDK | Idioma relatado pelo dispositivo e definido pelo sistema operacional do dispositivo. | Yes |  |
| ativado | SDK | Identificador de aplicativo único na Appsflyer. | Yes |  |
| app-version-name | SDK | Versão do aplicativo definido pelo desenvolvedor do aplicativo no código do aplicativo | Yes |  |
| attributed\_touch time | AF | Horário do toque ao qual a AppsFlyer atribuiu | Yes |  |
| device\_type | SDK | O nome do modelo comercial do dispositivo. Exemplo: SM-GM284 ou iPhone7 | Yes |  |
| ip | AF | IP do dispositivo do usuário que reportou o evento | Yes |  |
| match\_type | AF | Tipo de método de atribuição. Por exemplo, srn, id\_matching, probabilístico | Yes |  |
| os\_version | SDK | Versão do sistema operacional do dispositivo | Yes |  |
| user\_agent | SDK | O agente do usuário da URL | Yes |  |
| wifi | SDK | Se for verdadeiro, a conexão era uma conexão Wi-Fi no momento da conversão | Yes |  |
| OAID | SDK | User ID reconfigurável em alguns dispositivos Android, geralmente como alternativa ao GAID | Yes |  |
| platforma | SDK | Plataforma do dispositivo: iOS, Android ou Windows Mobile | Yes |  |
| retargeting\_conversion\_type | SDK | Uma flag aparecerá se for uma reatribuição ou reengajamento | Yes |  |
| pid | AF | Ad network à qual a instalação ou o evento in-app é atribuído | Yes |  |
| af\_ad | Link | Nome do anúncio (<Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#níveis-de-granularidade-de-dados">ver mais</Anchor>) fornecido pelo anunciante/publisher. | Yes | Yes |
| af\_ad\_id | Link | Fornecido pelo anunciante/editor | Yes | Yes |
| af\_adset | Link | <ul><li>Fornecido pelo anunciante/publisher.</li><li>Adset é um nível intermédio entre Campanha e Anúncio. <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#níveis-de-granularidade-de-dados">Saiba mais</Anchor></li></ul> | Yes | Yes |
| af\_adset\_id | Link | Fornecido pelo anunciante/editor | Yes | Yes |
| C | Link | Fornecido pelo anunciante/publisher. Os nomes de campanhas que excedem 100 caracteres são exibidos no dashboard como 'c\_name\_exceeded\_max\_length' | Yes | Yes |
| af\_c\_id | Link | Fornecido pelo anunciante/editor | Yes | Yes |
| af\_siteid | Link | <ul><li>ID único que identifica o publisher que exibe o anúncio. <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#site-id-parameter">Saiba mais</Anchor></li></ul> | Yes | Yes |
| af\_subsite\_id | Link | <ul><li>Ad sub-network/Publisher ID.</li><li>Se, além do publisher principal (site ID), houver um sub-publisher, ou você desejar incluir informações adicionais, como tipo de anúncio/posicionamento dentro do aplicativo, como banner, intersticial, vídeo etc, use af\_sub\_siteid. Exemplo: af\_sub\_siteid=ABCD\_4567</li></ul> | Yes | Yes |
| af\_ad\_type | Link | Tipo de anúncio Use a seguinte convenção de nomenclatura:<ul><li>**text:** uma unidade de anúncios contendo apenas texto, por exemplo, um resultado de pesquisa</li><li>**banner:** um formato básico que aparece na parte superior ou inferior da tela do dispositivo</li><li>**interstitial:** um anúncio de página inteira que aparece durante pausas na experiência vigente</li><li>**video:** um vídeo padrão, ou seja, não recompensado</li><li>**rewarded\_video:** uma unidade de anúncio que oferece recompensas no aplicativo em troca de assistir a um vídeo</li><li>**playable:** uma unidade de anúncio que contém uma visualização interativa da experiência do aplicativo</li><li>**sponsored\_content:** um link incluído em um pedaço de conteúdo patrocinado, como um artigo publicitário</li><li>**audio:** um anúncio em áudio</li></ul> | Yes | Yes |

## Macros somente para eventos in-app

Os exemplos abaixo dizem respeito dos postbacks de eventos in-app disponíveis para parceiros.

> 📘 **Note**
>
> **Exemplo**
>
> O modelo de postback de evento `&event=(event)&json=(encode)` foi convertido no seguinte postback para um evento af\_purchase específico:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> O valor JSON decodificado desse postback é `{"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

### Valores criptografados

Os postbacks podem conter caracteres irregulares, que não são alfanuméricos. Para transferir esses valores corretamente por meio de postbacks, a AppsFlyer codifica em URL valores não alfanuméricos.  
Para decodificar ou codificar um postback, use [um serviço web de codificação](https://www.urldecoder.org/).

## Postbacks de amostra

### Exemplos gerais de postbacks de instalação

<Tabs>
<Tab title="Android iOS">

```http
http://YourCompanyDomain.com?pid=(media_source)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)
```

</Tab>

<Tab title="Exemplo">

```http
http://YourCompanyDomain.com?pid=(media source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)
```

</Tab>
</Tabs>

### Exemplos gerais de postbacks de eventos in-app

<Tabs>
<Tab title="Android / iOS">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android-id)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>

<Tab title="/marketers/pt/docs/ctv-pc-and-console-platform-attribution-concepts">

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=(ip)&idfa=(idfa)&install_time=(install-unix-ts)&event_name=(event-name)&currency=(currency)&json=(event-value)
```

</Tab>
</Tabs>

## Exemplo de postback de evento in-app

**Parâmetros do evento:**

* Nome do evento: af\_revenue
* Receita do evento US$ 120,00
* moeda usada nos eventos. USD
* Valor do evento: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

**Postback**

```http
http://YourCompanyDomain.com?pid=(media_source)&device_ip=38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&android_id=9aaeecc4455xxxxx&install_time=1451923560&event_name=af_purchase&currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```

<div data-zendesk-anchors="postbacks-for-analytics-partners=postbacks-para-parceiros-de-an%C3%A1lise 01JH2HWTN05T8S3P4W6CKVA7K4=postbacks-para-parceiros-de-an%C3%A1lise postback-macros=macros-de-postback 01JH2HWTN52E8CVVGTQWK3QXW6=macros-de-postback macros%E2%80%94installs-and-inapp-events=macros--instala%C3%A7%C3%B5es-e-eventos-in-app 01JH2HWTN7XY6B55TED4NT2KRR=macros--instala%C3%A7%C3%B5es-e-eventos-in-app inapp-event-only-macros=macros-somente-para-eventos-in-app 01JH2HWTVN8880HZSF6V6XZ7EF=macros-somente-para-eventos-in-app encoded-values=valores-criptografados 01JH2HWTVNARNYV0M9AKHQ0NDA=valores-criptografados sample-postbacks=postbacks-de-amostra 01JH2HWTVNQT0NPJ7SG9424MTQ=postbacks-de-amostra general-install-postback-examples=exemplos-gerais-de-postbacks-de-instala%C3%A7%C3%A3o 01JH2HWTVN4DDQ6F70WP3XE19D=exemplos-gerais-de-postbacks-de-instala%C3%A7%C3%A3o general-inapp-event-postback-examples=exemplos-gerais-de-postbacks-de-eventos-in-app 01JH2HWTVN2MH2SB6W34DH2MF7=exemplos-gerais-de-postbacks-de-eventos-in-app inapp-event-postback-example=exemplo-de-postback-de-evento-in-app 01JH2HWTVP50J5WV11DZR3RSTM=exemplo-de-postback-de-evento-in-app" />
