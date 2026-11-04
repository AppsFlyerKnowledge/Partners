---
title: Guia de integração da SKAN para ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - SKAD
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2020-08-03T08:56:14Z'
  edited_at: '2026-08-19T00:37:21Z'
  id: 360011502657
  locale: pt
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/pt/articles/360011502657
---
> **Em resumo**: as ad networks se integram às SKAdNetworks (SKAN) da AppsFlyer, permitindo que otimizem campanhas e recebam atribuição pelo tráfego que geram.

<div id="appsflyer-offering-for-ad-networks" />

## Oferta da AppsFlyer para ad networks

**Learn more about the AppsFlyer SKAN solution for advertisers:**

<Anchor target="_blank" href="/marketers/pt/docs/skadnetwork-skan-solution-guide">SKAN solution guide |</Anchor> <Anchor target="_blank" href="/marketers/pt/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">SKAN dashboard</Anchor>

* **Receba atribuição por conversões de campanha:**
  * A integração com a AppsFlyer garante que a ad network receba atribuição por todas as instalações, eventos in-app e receita resultantes das campanhas executadas em nome dos anunciantes.
  * Sem a integração implementada, as instalações, os eventos in-app e a receita são atribuídos como orgânicos, e não à ad network.
* **Otimização de campanhas:**
  * O valor de conversão no postback é codificado.
  * A AppsFlyer permite que ad networks traduzam o valor de conversão de cada postback, garantindo que possam otimizar suas campanhas com base no valor decodificado por aplicativo.
* **Não há necessidade de integração direta com cada anunciante:** os postbacks da SKAN são enviados apenas para a ad network, e os anunciantes podem consumir os dados usando qualquer uma das opções a seguir:
  * Integração individual com cada ad network. Uma solução que não é escalável nem para ad networks nem para anunciantes.
  * Uma única integração com a AppsFlyer. Escalável tanto para o anunciante quanto para a ad network.
* **Aumente sua visibilidade na AppsFlyer:**
  * Ad networks com integração SKAN são certificadas e identificadas como tal no dashboard da AppsFlyer.
  * Isso assegura aos anunciantes que eles estão trabalhando com ad networks que podem ser mensuradas de forma determinística por meio deste modelo de atribuição.

<div id="skan-data-flow" />

## Fluxo de dados da SKAN

![5754_Postback_flow_for_SKAD__1_.png](https://files.readme.io/dff0fb00721802f59d199ae6a69f9ea7484bc0ef038c669904aa1a7c2b97dfc8-12574373654161.png)

O fluxo completo de postback da SKAN é o seguinte:

1. **iOS** envia o postback da SKAN para a ad network atribuída.
2. **A ad network** executa uma das seguintes ações:
   * **Enriquecer e encaminhar:** enriquece o postback da SKAN com o ID da campanha/identificador da fonte da ad network, o nome da campanha e o endereço IP do dispositivo iOS.
   * **Redirect:** The network requests the iOS device to redirect the postback directly to AppsFlyer. In this case, campaign data enrichment will be performed via a separate API between AppsFlyer and the ad network.
3. **A AppsFlyer** valida e decodifica o postback. Then, it sends the decoded and enriched postback to the ad network (in parallel to sharing it with the advertiser).

<div id="main-integration-parts" />

## Principais partes da integração

A integração da SKAN entre a AppsFlyer e ad networks consiste nas seguintes partes principais, conforme descrito neste artigo:

* Ad networks enviam dados da SKAN para a AppsFlyer
* As ad networks recebem dados enriquecidos e decodificados da AppsFlyer via postback

<div id="send-data-to-appsflyer" />

## Enviar dados para a AppsFlyer

After the ad network receives the SKAN postback from the device, the ad network forwards it to AppsFlyer using one of the following methods:

* Enriquecer e encaminhar (POST)
* Redirecionar (método de redirecionamento HTTP 307)

Ao receber um postback da SKAN, a AppsFlyer realiza o seguinte:

* Validação do postback: garantir que seja exclusivo.
* Decodificação do valor de conversão: gerar registros de instalação com atribuição e de eventos in-app.
* Enviar postbacks decodificados para a ad network.
* Disponibilizar dados de atribuição para anunciantes por meio de dashboards e relatórios.

<div id="enrich-and-forward" />

<Accordion title="Enriquecer e encaminhar">

Usando esse método, as ad networks encaminham à AppsFlyer cada postback recebido do dispositivo.

**A ad network:**

* Recebe o postback do dispositivo iOS.
* [Obrigatório] Enriquece o postback com:
  * ID da campanha e nome da campanha da ad network.
  * O carimbo de data/hora do postback enviado pelo dispositivo iOS.
* [Opcional] Enriquece o postback com:
  * Endereço IP recebido do dispositivo, exigido principalmente para fins de resolução de geolocalização.
  * ID e nome do conjunto de anúncios
  * ID e nome do anúncio
  * Ad network name
  * Código do país
  * ID do aplicativo de origem
  * de criativos
  * Canal
* Envia o postback para a AppsFlyer
* **Nota!** Before sending the postback to AppsFlyer, validate the Apple <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/verifying_an_install-validation_postback">attribution signature</Anchor> using the content of the outgoing postback to ensure that you didn't inadvertently corrupt the data.

<div id="skan-enriched-postback-protocol" />

#### Protocolo de postback enriquecido da SKAN

| Ponto final | `https://skadpostbacks.appsflyer.com/api/postbacks` |
| --- | --- |
| Método HTTP | POST |
| Tipos de conteúdo aceitos | `application/json` |
| Códigos de retorno | 200 OK: o postback recebido tem um formato válido.<br /><br />400: Solicitação inválida: JSON malformado, JSON vazio, campos obrigatórios ausentes. |

<div id="skan-enriched-postback-json-parameters" />

#### Parâmetros JSON do postback enriquecido do SKAN

| Parâmetro | Formato | A descrição | Fonte: |
| --- | --- | --- | --- |
| version | Sequência de caracteres | Versão do SKAdNetwork<br /><br />Exemplo: `"version":"2.0"` | SKAN postback |
| ad-network-id | Sequência de caracteres | ID da ad network<br /><br />Exemplo: `"ad-network-id":" abc123defg.SKAdnetwork"` | SKAN postback |
| ad-network-name | Sequência de caracteres | <ul><li>Nome da ad network</li><li>Exemplo: `ad_network_name=your_network`</li></ul> | Rede de anúncios |
| ad-network-country-code | Sequência de caracteres | <ul><li>A localização do usuário (geolocalização), conforme determinada pela ad network.</li><li>Populate using <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor> codes.</li><li>Exemplo: CN, ZA</li><li>As ad networks frequentemente determinam a geolocalização de acordo com a região-alvo de uma determinada campanha.</li><li>A AppsFlyer usa o código do país para preencher campos relacionados à geolocalização em relatórios e dashboards.</li></ul> | Rede de anúncios |
| campaign-id | Inteiro | <ul><li>Somente para o SKAN 3 e versões anteriores</li><li>ID da campanha do SKAdNetwork</li><li>Exemplo: `"campaign-id":23`</li></ul> | SKAN postback |
| transaction-id | Sequência de caracteres | ID da transação do postback do SKAdNetwork | SKAN postback |
| app-id | Inteiro | <ul><li>ID do aplicativo de destino, como aparece na AppsFlyer. Sempre tem o prefixo id.</li><li>Exemplo:`app_id=id123456789`</li></ul> | SKAN postback |
| assinatura de atribuição | Sequência de caracteres | Assinatura de atribuição | SKAN postback |
| redownload | Boolean | Quando redownload = true, significa que o usuário fez o download do aplicativo novamente na loja de aplicativos. | SKAN postback |
| source-app-id | Inteiro | <ul><li>ID do aplicativo de fonte (publisher)</li><li>No SKAN 4, disponível apenas no primeiro postback, para o nível 3. Veja a [documentação da Apple](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)</li></ul> | SKAN postback |
| conversion-value | Inteiro | O SDK da AppsFlyer define o valor de conversão de acordo com as configurações do anunciante.<br /><br />**Notas**!<ul><li>iOS devido aos limites de preservação de privacidade do iOS pode não preencher o parâmetro no postback e o valor será nulo.</li><li>Nulo e 0 têm significados diferentes:<ul><li>Nulo: o iOS reteve o valor de conversão</li><li>0: o usuário instalou o aplicativo, mas não realizou nenhuma ação mensurável.</li></ul></li></ul> | SKAN postback |
| ad-network-campaign-id | Sequência de caracteres | Para habilitar uma linguagem comum entre ad networks, anunciantes e a AppsFlyer, você deve fornecer seu campaign-id. | Rede de anúncios |
| ad-network-campaign-name | Sequência de caracteres | Nome da campanha da ad network associado ao ID da campanha da ad network. Esse nome é exibido em dashboards e relatórios. | Rede de anúncios |
| ad-network-adset-id | Sequência de caracteres | ID do conjunto de anúncios da ad network | Rede de anúncios |
| ad-network-adset-name | Sequência de caracteres | Nome do conjunto de anúncios da ad network | Rede de anúncios |
| ad-network-ad-name | Sequência de caracteres | Nome do anúncio da ad network | Rede de anúncios |
| ad-network-ad-id | Sequência de caracteres | ID do anúncio da ad network | Rede de anúncios |
| ip | Sequência de caracteres | <ul><li>O endereço IP do dispositivo que envia o postback.</li><li>Endereços iPv4 e IPv6 suportados.</li><li>Example: `"ip":"198.51.100.1"`</li></ul> | Rede de anúncios |
| timestamp | Sequência de caracteres | <ul><li>Hora em que a ad network recebeu o postback do SKAN. Um timestamp UNIX epoch de 10 dígitos. [Opcional] Timestamp epoch de 13 dígitos permitido.</li><li>Exemplo: 4 de agosto de 2020, 07:25 UTC corresponde a `"timestamp": "1596525944"`</li></ul> | Rede de anúncios |
| fidelity-type | Inteiro | <ul><li>Differentiate between <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/receiving_ad_attributions">ad presentation</Anchor> options that affect attribution. Indicado pelos valores 0 e 1 da seguinte forma:<ul><li>Anúncios visualizados (0)</li><li>Anúncios renderizados pelo StoreKit (1)</li></ul></li><li>Mandatory field starting SKAN V2.2</li></ul> | Postback do SKAN (V2.2+) |
| did-win | Boolean | <ul><li>Used to distinguish between campaigns [contributing or attributed](https://developer.apple.com/documentation/storekit/SKAdnetwork/SKAdnetwork_release_notes/SKAdnetwork_version_3_0_release_notes) with the install.</li><li>Se true, a campanha é atribuída como responsável pela instalação.</li><li>Se falso, a campanha é reconhecida como contribuindo para a instalação</li></ul> | Postback do SKAN (V3.0+) |
| ad-network-source-app-id | Sequência de caracteres | Preencha com o *ID do publisher* que você associa ao aplicativo que publica o anúncio. Normalmente, esse é o ID que você atribuiu ao publisher, e não o ID gerado pela Apple. | Rede de anúncios |
| postback-sequence-index | Inteiro | <ul><li>Somente para SKAN 4+</li><li>O valor representa o número da sequência (janela SKAN): `0`, `1` ou `2`.</li></ul> | Postback do SKAN 4.0 (iOS 16.2) |
| valor de conversão coarse | Sequência de caracteres | <ul><li>Somente para SKAN 4+</li><li>O valor pode ser `low`,`medium` ou`high`.</li><li>Para o primeiro postback, disponível apenas para o nível 1. Para o segundo e o terceiro postbacks, disponível para os níveis 1 a 3. Veja a [documentação da Apple](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)</li></ul> | Postback da SKAN 4.0 (iOS 16.2) |
| source-identifier | Sequência de caracteres | <ul><li>Apenas para SKAN 4+</li><li>Substitui `campaign-id`</li><li>O valor pode ter até 4 dígitos.</li><li>No primeiro postback, até 4 dígitos estão disponíveis para os níveis 2-3, e 2 dígitos estão disponíveis para os níveis 0-1. No segundo e no terceiro postback, 2 dígitos estão disponíveis para os níveis 1-3. Para o nível 0, não há postback. Veja a [documentação da Apple](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)</li></ul> | Postback da SKAN 4.0 (iOS 16.2) |
| source-domain | Sequência de caracteres | <ul><li>Apenas para SKAN 4+</li><li>O valor representa a origem dos anúncios web atribuídos. Exemplo: `example.com`</li><li>Disponível apenas em anúncios web, no primeiro postback, para o nível 3. Veja a [documentação da Apple](https://developer.apple.com/documentation/storekit/skadnetwork/receiving_postbacks_in_multiple_conversion_windows)</li></ul> | Postback da SKAN 4.0 (iOS 16.2) |
| Data Locker - select Creative.jpg | Sequência de caracteres | <ul><li>Relevante apenas para SKAN 4+</li><li>Available when you use additional digits in the source\_identifier for additional campaign granularity.</li></ul> | Rede de anúncios |
| Canal | Sequência de caracteres | <ul><li>Relevante apenas para SKAN 4+</li><li>Available when you use additional digits in the source\_identifier for additional campaign granularity.</li></ul> | Rede de anúncios |

<div id="curl-exampleenriched-skan-3-postback" />

#### **Exemplo de Curl — postback avançado da SKAN 3**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version":"3.0",
      "app-id": 888707086,
      "ip": "192.0.2.0",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "source-app-id": 888707074,
      "ad-network-id": "abcabcabc.skadnetwork",
      "transaction-id": "68eb3d91-15f5-44ee-9267-25c7655c20b6",
      "redownload": false,
      "attribution-signature": "MDYCGQCsQ4y8d4BlYU9b8Qb9BPWPi+ixk/OiRysCGQDZZ8fpJnuqs9my8iSQVbJO/oU1AXUROYU=",
      "timestamp": "1596525944",
      "ad-network-campaign-id": "222222",
      "conversion-value": 63,
      "campaign-id": 99
  }'
```

<div id="curl-exampleenriched-skan-4-postback-with-fine-conversion-values" />

#### **Exemplo de Curl — postback avançado da SKAN 4 com valores de conversão refinados**

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "5239",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e30",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "conversion-value": 63
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIGRmSMrqedNu6uaHyhVcifs118R5z/AB6cvRaKrRRHWRAiEAv96ne3dKQ5kJpbsfk4eYiePmrZUU6sQmo+7zfP/1Bxo="
  }'
```

#### Curl example—enriched SKAN 4 postback with coarse conversion values

```bash
curl --location --request POST 'https://skadpostbacks.appsflyer.com/api/postbacks?app_id=id888707074' \
  --header 'Content-type: application/json' \
  --data-raw '{
      "version": "4.0"
      "ad-network-id": "example123.skadnetwork",
      "ad-network-campaign-name": "skadnetwork_abc_campaign",
      "ad-network-campaign-id": "222222",
      "source-identifer": "39",
      "app-id": 525463029,
      "transaction-id": "6aafb7a5-0170-41b5-bbe4-fe71dedf1e31",
      "redownload": false,
      "source-app-id": 1234567891,
      "fidelity-type": 1, 
      "did-win": true,
      "coarse-conversion-value": "high"
      "postback-sequence-index": 0
      "attribution-signature": "MEUCIQD4rX6eh38qEhuUKHdap345UbmlzA7KEZ1bhWZuYM8MJwIgMnyiiZe6heabDkGwOaKBYrUXQhKtF3P/ERHqkR/XpuA="
  }'
```

</Accordion>

<div id="redirect" />

<Accordion title="Redirecionar">

![Redirect_us-en__2_.png](https://files.readme.io/17d4a668cde784a2f823e702e04fc75a2bbbdb483e44d9d10edfad03d865bbb7-360012352758.png)

Com esse método, a ad network responde ao dispositivo com um comando de redirecionamento HTTP (307), solicitando que o dispositivo envie o postback diretamente para a AppsFlyer.

O método de redirecionamento tem as seguintes vantagens:

* **Increased advertiser trust:** The MMP acts on behalf of an advertiser. By providing AppsFlyer access to the postback firsthand, advertisers are confident that postbacks are not manipulated in transit.
* **No processing required by the ad network:** Ad networks respond with the redirect command (to the device), thus eliminating the need to process postbacks. In comparison, the enrich and forward method requires that ad networks consume the postback, enrich it with additional parameters, and finally forward it to AppsFlyer.

<div id="implementation" />

#### **Implementação**

1. Configure your server to respond with an HTTP 307 response redirecting the postback to *[https://skadnetworkredirect.appsflyer.com/api/redirects](https://SKANredirect.appsflyer.com/api/redirects)*
2. Anexe parâmetros de consulta que contenham detalhes da campanha usando os parâmetros de consulta listados na tabela a seguir. Considere o envio dos detalhes da sua campanha obrigatório. Os detalhes da campanha nos permitem enriquecer os dados do SKAN com custo e outros dados da campanha, além de permitir que os anunciantes otimizem campanhas com eficiência.

**Exemplo de URL de redirecionamento**

```http
https://skadredirect.appsflyer.com/api/redirects?
  &ad-network-campaign-id=243232&ad-network-campaign-name=yarg_campaign_name
  &ad-network-adset-name=dsdsa&creative=examplecreative&channel=channelexample
```

<div id="query-params-for-campaign-details-not-mandatory" />

#### Parâmetros de consulta para detalhes da campanha (não obrigatórios)

| Parâmetro de consulta | Visão geral |
| --- | --- |
| ad-network-name | <ul><li>Nome da ad network</li><li>Example:`ad_network_name=your_network`</li></ul> |
| ad-network-campaign-id | ID da campanha |
| ad-network-campaign-name | Nome da campanha |
| ad-network-adset-id | ID do conjunto de anúncios |
| ad-network-adset-name | Nome do adset |
| ad-network-ad-id | ID do anúncio |
| ad-network-ad-name | Nome do anúncio |
| ad-network-country-code | <ul><li>A localização do usuário (geolocalização) derivada pela ad network.</li><li>Populate using <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor> codes.</li><li>Exemplo: CN, ZA</li><li>As ad networks geralmente derivam a geolocalização de acordo com a região-alvo da campanha.</li><li>A AppsFlyer usa o código do país para preencher campos relacionados à geolocalização em relatórios e dashboards.</li></ul> |
| ad-network-source-app-id | Populate with the *publisher ID* that you associate with the app publishing the ad. Geralmente, este é o ID que você atribuiu ao publisher, e não o ID gerado pela Apple. |
| ip | <ul><li>O endereço IP do dispositivo que está enviando o postback.</li><li>Endereços iPv4 e IPv6 compatíveis.</li><li>Example:`"ip":"198.51.100.1"`</li></ul> |
| timestamp | <ul><li>Hora em que a ad network recebeu o postback do SKAN. Carimbo de data/hora UNIX epoch de 10 dígitos. [Opcional] Carimbo de data/hora epoch de 13 dígitos permitido.</li><li>Example: August 4, 2020, 07:25 UTC translates to`"timestamp": "1596525944"`</li></ul> |
| Data Locker - select Creative.jpg | <ul><li>Relevante apenas para SKAN 4+</li><li>Available when you use additional digits in the source\_identifier for additional campaign granularity.</li></ul> |
| canal | <ul><li>Relevante apenas para SKAN 4+</li><li>Available when you use additional digits in the source\_identifier for additional campaign granularity.</li></ul> |

</Accordion>

<div id="receive-data-from-appsflyer" />

## Receber dados da AppsFlyer

Antes de receber seu primeiro postback, considere o seguinte:

* Ad networks must define the postback end-point and template (reach out to your AppsFlyer Partner Development Manager using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>, to ensure this is in place).
* A AppsFlyer envia postbacks do SKAN usando o mesmo mecanismo dos postbacks existentes enviados a você.

<div id="principles" />

<Accordion title="Princípios">

* Para cada postback enviado da ad network para a AppsFlyer, a AppsFlyer envia:
  * Um postback de instalação. Os redownloads são sinalizados pelo parâmetro redownload.
  * De zero a vários postbacks de eventos in-app. O número exato depende da tradução do valor de conversão. See [simulated postbacks.](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks)
* When you consume postbacks, the same install or event can be attributed by more than one AppsFlyer attribution solution. Use the *attribution\_source* parameter to differentiate between postback types.

</Accordion>

<div id="postback-macros-available-to-ad-network-partners" />

<Accordion title="Macros de postback disponíveis para parceiros de ad network">

<table><thead><tr><th>Macro do postback (nome)</th><th>Descrição</th><th>Formato e exemplo</th><th>Relevante apenas para eventos in-app</th></tr></thead><tbody><tr><td>id_do_site</td><td>O aplicativo que publica o anúncio (ID do aplicativo de origem)</td><td>String: 876534</td><td> </td></tr><tr><td>install_time</td><td>Estimado pela AppsFlyer com base na janela de <em>updateConversion</em>. Fornecido como um timestamp UNIX epoch de 10 dígitos ou como um timestamp legível por humanos</td><td><ul><li>String: 1596119460 </li><li>Corresponde a 30 de julho de 2020, 14:31 UTC.</li></ul></td><td> </td></tr><tr><td>skadnetwork_ad_network_time</td><td>Momento em que o postback foi recebido pela ad network do dispositivo iOS. Conforme relatado pela ad network. Fornecido como um timestamp UNIX epoch de 10 dígitos ou como um timestamp legível por humanos</td><td><ul><li>String: 1596119460 </li><li>Corresponde a 30 de julho de 2020, 14:31 UTC</li></ul></td><td> </td></tr><tr><td> <br/>skadnetwork_received_time</td><td>Hora em que a AppsFlyer recebeu o postback da ad network. Fornecido como um carimbo de data/hora UNIX epoch de 10 dígitos ou como um carimbo de data/hora legível</td><td><ul><li>String: 1596119460 </li><li>Corresponde a 30 de julho de 2020, 14:31 UTC</li></ul></td><td> </td></tr><tr><td>nome_do_evento</td><td><p>Nome do evento </p><ul><li>af_skadnetwork_revenue</li><li>af_login</li><li>af_skadnetwork_revenue</li><li>ou conforme definido pelo anunciante </li></ul></td><td><p>String: af_skadnetwork_revenue, abc123</p></td><td>Sim</td></tr><tr><td>revenue</td><td>Valor da receita usando o código de moeda especificado</td><td>Número: 5, 20, 0,4</td><td>Sim</td></tr><tr><td>símbolos monetários</td><td>Código da moeda, sendo a moeda específica do aplicativo definida pelo anunciante</td><td>Sequência de caracteres: EUR, USD, ZAR</td><td>Sim</td></tr><tr><td>attribution_source</td><td><p>A fonte dos dados de atribuição:</p><p>SKAdNetwork: SKAdNetwork</p></td><td>Sequência de caracteres: SKAdNetwork</td><td> </td></tr><tr><td>ativado</td><td>ID do Aplicativo (aplicativo do anunciante)</td><td>Sequência de caracteres: ID123456790</td><td> </td></tr><tr><td>país</td><td>Geolocalização da instalação (país) determinada pela ad network</td><td>Sequência de caracteres: US, UK, ZA </td><td> </td></tr><tr><td>Twitter</td><td>Nome da campanha preenchido usando <em>ad-network-campaign-name</em> enviado no postback da ad network</td><td>Sequência de caracteres: UA_US_23+</td><td> </td></tr><tr><td>id_da_campanha</td><td>ID da campanha da ad network preenchido usando <em>ad-network-campaign-id</em> enviado no postback da ad network. <strong>Observação</strong>: para o SKAN 4, esse valor é sempre nulo.</td><td>String: 3456745</td><td> </td></tr><tr><td>redownload</td><td><p>Valores possíveis: true, false</p><p>Quando redownload = true, isso significa que o usuário fez o download do aplicativo da loja de aplicativos novamente</p></td><td>Booleano: true, false</td><td> </td></tr><tr><td><p>skadnetwork_ambiguous_event</p><p>(descontinuado no SKAN 4+)</p></td><td><p>Eventos recebidos durante as primeiras 72 horas após um anunciante alterar as configurações de SKAN no dashboard. Devido aos diversos timers usados pela SKAN, a AppsFlyer não consegue mapear o evento com exatidão.</p><ul><li>Indisponível na SKAN 4 e versões mais recentes</li></ul></td><td>Booleano: true, false</td><td> </td></tr><tr><td>skadnetwork_campaign_id</td><td>ID da campanha SKAN conforme fornecido pelo postback SKAN original</td><td>56, 23</td><td> </td></tr><tr><td>af_skadnetwork_nonce</td><td>Um identificador aleatório e único que permite aos parceiros identificar postbacks duplicados.</td><td> </td><td> </td></tr><tr><td>Receita associada ao SKU na moeda fornecida no campo <code>event_revenue_currency</code>.</td><td>Name/ID of the corresponding<span> </span><span>event</span><span> </span>in the ad network platform</td><td> </td><td>Sim</td></tr><tr><td>transaction_id</td><td><p>ID da transação do postback SKAN</p><p><strong>Observação</strong>: o anunciante deve permitir explicitamente que compartilhemos o transaction_id com você. Ask the advertiser to do so in the <a href="/marketers/pt/docs/set-up-an-integrated-partner#integration-tab" target="_blank"><strong>Integration</strong></a> tab.</p></td><td> </td><td> </td></tr><tr><td>ad_network_adset_id</td><td>Adicionado ao postback do iOS pela ad network</td><td>string</td><td> </td></tr><tr><td>ad_network_adset_name</td><td>Adicionado ao postback do iOS pela ad network</td><td>string</td><td> </td></tr><tr><td>ad_network_ad_name</td><td>Adicionado ao postback do iOS pela ad network</td><td>string</td><td> </td></tr><tr><td>ad_network_ad_id</td><td>Adicionado ao postback do iOS pela ad network</td><td>string</td><td> </td></tr><tr><td>SKAN_min_event_counter</td><td>Ver nota (1)</td><td>Inteiro</td><td>Sim</td></tr><tr><td>SKAN_max_event_counter</td><td>Ver nota (1)</td><td>Inteiro</td><td>Sim</td></tr><tr><td>SKAN_min_time_post-install</td><td>Ver nota (2)</td><td>Inteiro</td><td>Sim</td></tr><tr><td>SKAN_tempo_máx_pós-instalação</td><td>Ver nota (2)</td><td>Inteiro</td><td>Sim</td></tr><tr><td>SKAN_receita_mín_do_evento</td><td>Ver nota (3)</td><td>Número real</td><td>Sim</td></tr><tr><td>SKAN_receita_máx_do_evento</td><td>Ver nota (3)</td><td>Número real </td><td>Sim</td></tr><tr><td>fidelity-type</td><td><p>Differentiate between <a href="https://developer.apple.com/documentation/storekit/SKAdnetwork/receiving_ad_attributions" target="_blank">ad presentation</a> options that affect attribution. Indicado pelos valores 0 e 1 da seguinte forma: </p><ul><li>Anúncios visualizados (0)</li><li>Anúncios renderizados pelo StoreKit (1)</li></ul></td><td>Inteiro</td><td> </td></tr><tr><td>skad_af_attribution_flag</td><td>Used to indicate if the user was attributed by AppsFlyer using the <a href="/marketers/pt/docs/single-source-of-truth-ssot-guide-for-ios-attribution#campo-de-sinalização-de-atribuição" target="_blank">Single Source of Truth mechanism</a>. </td><td>Boolean</td><td> </td></tr><tr><td>skad_postback_sequence_index</td><td><ul><li>O valor representa a janela SKAN: <code>0</code>, <code>1</code> ou<code>2</code>.</li><li>Para SKAN 3, o valor é <code>0</code> </li></ul></td><td>Inteiro</td><td> </td></tr><tr><td>skad_coarse_conversion_value</td><td><ul><li>O valor pode ser <code>low</code>,<code>medium</code> ou<code>high</code>.</li><li>Para SKAN 3, o valor é <code>null</code>.</li></ul></td><td>Sequência de caracteres</td><td> </td></tr><tr><td>skad_source_identifier</td><td><ul><li>O valor pode ter até 4 dígitos.</li><li>Para SKAN 3, o valor é <code>null</code>. </li></ul></td><td>Sequência de caracteres</td><td> </td></tr><tr><td>skad_source_domain</td><td><ul><li>O valor representa a origem dos anúncios web atribuídos.</li><li>Para SKAN 3, o valor é <code>null</code>.</li></ul></td><td>Sequência de caracteres</td><td> </td></tr><tr><td>ad_network_creative</td><td><ul><li>O valor é baseado no enriquecimento de dados recebido da ad network.</li><li>Para SKAN 3, o valor é <code>null</code>.</li></ul></td><td>Sequência de caracteres</td><td> </td></tr><tr><td>ad_network_channel</td><td><ul><li>Relevante apenas para SKAN 4+</li><li>Available when you use additional digits in the <span>source_identifier</span> for additional campaign granularity.</li></ul></td><td>Sequência de caracteres</td><td> </td></tr><tr><td colspan="4"><p>Atenção:</p><ol><li> <strong>Ocorrências de evento</strong>: O número de ocorrências de evento é calculado usando a seguinte fórmula:<br/><code>[arredondar para cima (SKAN_min_event_counter+SKAN_max_event_counter) / 2]</code><br/>Observação! O valor deve ser arredondado para cima até o número inteiro mais próximo.</li></ol><ul><li>Exemplo:<ul><li>A. A. A. If min=0 and max=1 the number of events is 1.</li><li>B. B. B. If min=0 and max =10 the number of events is 5.</li></ul></li><li> <strong>Determinar o tempo de instalação</strong>: Para anunciantes que implementam a conversão personalizada, a AppsFlyer calcula o tempo de instalação como o horário de chegada do postback - 48h - média (min_time_post_install + max_time_post_install). As ad networks não precisam usar essas macros.  </li><li> <strong>Determinar a receita</strong>: A AppsFlyer usa esses valores para determinar a receita de um evento calculando a média entre o mínimo e o máximo. As ad networks não precisam usar essas macros. </li></ul></td></tr></tbody></table>

</Accordion>

<div id="skan-postback-examples" />

<Accordion title="Exemplos de postback da SKAN">

**Exemplo de um postback de instalação da SKAN enviado pela AppsFlyer**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)
  &attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

**Exemplo de um postback in-app da SKAN enviado pela AppsFlyer**

```http
http://YourCompanyDomain.com/event?site_id=(publisher-id)&install_time=(timestamp)
  &skan_ad_network_time=(timestamp)
  &skan_af_received_time=(timestamp)&revenue=(value)
  &currency=(code)&event_name=(event-name)&attribution_source=skadnetwork
  &app_id=(id123456789)&country=(ZA)&campaign=(campaign-name)
  &campaign_id=(campaign-id)&SKAN_ambiguous_event=(boolean)  
&redownload=(boolean)  
&af_SKAN_nonce=(uuid)
```

</Accordion>

<div id="integration-testing" />

## Teste a integração

Para validar a integração com a AppsFlyer, use um ou ambos os métodos a seguir.

* Postbacks reais da SKAN: com base no tráfego real da SKAN recebido pela network
* Postbacks simulados: com base nos aplicativos de teste da AppsFlyer

**Para receber postbacks reais da SKAN de dispositivos iOS, a ad network conclui o seguinte:**

* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/registering_an_ad_network">Registrar-se na Apple</Anchor>
* <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/generating_the_signature_to_validate_storekit-rendered_ads">Sign ads with a SKAdNetwork signature</Anchor>.
* Publisher app: <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/configuring_a_source_app">Add the network ID to the info.plist file</Anchor> and <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/SKAdnetwork/generating_the_signature_to_validate_an_installation">call the loadProduct</Anchor> function upon ad impression.
* Advertised app: Use the most recent AppsFlyer <Anchor target="_blank" href="/marketers/pt/docs/sdk-integration-overview">iOS SDK.</Anchor> Versões anteriores à V6.0.3 não são suportadas.

**Para receber postbacks simulados:**

* Contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor> and request integration with simulation apps.
* Specify IDs of the apps from the list in the [following section](/docs/skan-integration-guide-for-ad-networks#simulated-postbacks).

<div id="real-environment" />

<Accordion title="Ambiente real">

Usando este método, a ad network envia à AppsFlyer postbacks reais do SKAN de aplicativos ao vivo.

<div id="testing-integration" />

#### Integração de testes

| Responsabilidade | Action |
| --- | --- |
| Rede de anúncios | Notify AppsFlyer via your partner development manager (or use the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>) as to your SKAN network ID, provided by Apple. |
| Ad network e AppsFlyer | Cheguem a um acordo sobre um cliente mútuo (que tenha integrado o SDK mais recente da AppsFlyer) a ser usado para a verificação da integração de postback. |
| Rede de anúncios | Envie postbacks SKAN do aplicativo para a AppsFlyer usando um dos métodos descritos neste artigo. |
| A AppsFlyer | Envie postbacks decodificados para a ad network de acordo com o mapeamento de valor de conversão definido pelo anunciante. |

<div id="test-criteria" />

#### Critérios de teste

| Responsabilidade | Action |
| --- | --- |
| Rede de anúncios | Notifique a AppsFlyer sobre a quantidade de postbacks SKAN enviados durante um período especificado para o cliente mútuo acordado. |
| A AppsFlyer | Verifique a contagem de postbacks recebidos em comparação com a contagem enviada pela ad network. |
| A AppsFlyer | Compartilhe com a ad network a contagem de postbacks enviados para a ad network de um determinado aplicativo, discriminada por tipo:<ul><li>Postbacks de instalação/re-download</li><li>Postbacks in-app.</li></ul>Note: If you use the same endpoint for probabilistic postbacks, ensure that you filter using *attribution\_source=skadnetwork* to distinguish SKAN Network postbacks from other postbacks. |

</Accordion>

<div id="simulated-postbacks" />

<Accordion title="Postbacks simulados">

* Usando este método, a ad network envia à AppsFlyer postbacks pré-preparados para aplicativos de teste da AppsFlyer, conforme detalhado na tabela abaixo. A AppsFlyer responde à ad network com postbacks decodificados.
* Cada aplicativo de teste tem um mapeamento de valor de conversão diferente, conforme detalhado na tabela.

| ID da aplicação | Modo de conversão | Instruções |
| --- | --- | --- |
| <span id="id888707085"></span>id888707085 | Receita, em unidades de $1<br /><br />Resultados esperados: | <ol><li>Na guia **Integração**, habilite **postbacks de eventos in-app**.</li><li>Select event name *af\_SKAN\_revenue* and map to your event identifier.</li><li>Salvar configuração.</li><li>Em um postback, envie valor de conversão = 7.</li><li>A AppsFlyer responde com:<ul><li>Postback de instalação</li><li>af\_SKAN\_revenue postback com valor de $7</li></ul></li></ol> |
| <span id="id888707086"></span>id888707086 | Conversão, incluindo os eventos in-app:<ul><li>af\_level\_complete</li><li>af\_login</li><li>af\_SKAN\_revenue</li><li>af\_register</li><li>af\_subscription</li><li>af\_custom\_event</li></ul> | <ol><li>Na guia **Integração**, ative os **postbacks de eventos in-app**.</li><li>Selecione cada um dos eventos in-app listados e mapeie-o para o identificador do evento.</li><li>Salvar configuração.</li><li>Em um postback, envie valor de conversão = 63.</li><li>A AppsFlyer responde com:<ul><li>Postback de instalação</li><li>postback af\_level\_complete</li><li>postback af\_login</li><li>postback af\_SKAN\_revenue</li><li>postback af\_register</li><li>postback af\_subscription</li><li>postback af\_custom\_event</li></ul></li></ol> |
| <span id="id888707087"></span>id888707087 | Engagement, measured using af\_SKAN\_revenue event | <ol><li>Na guia **Integração**, ative os **postbacks de eventos in-app**.</li><li>Map the event name *af\_SKAN\_revenue* and to your event identifier.</li><li>**Salvar** configuração.</li><li>Em um postback, envie valor de conversão = 3.</li><li>A AppsFlyer responde com:<ul><li>Postback de instalação</li><li>3 postbacks of af\_SKAN\_revenue event</li></ul></li></ol> |

<div id="integration-steps" />

#### Etapas de integração

| Responsabilidade | Action |
| --- | --- |
| Rede de anúncios | Configure your SKAN network ID (provided by Apple) and SKAN postback template on the <Anchor target="_blank" href="/partners/pt/docs/self-serve-integration-management-for-ad-networks">postback management platform</Anchor>. For queries and assistance, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>. |
| Rede de anúncios | <ol><li><Anchor target="_blank" href="/partners/pt/docs/turn-on-test-app-integration-for-ad-networks">Activate the test apps</Anchor>.</li><li>Para cada aplicativo, conclua a coluna de instruções na tabela anterior.</li><li>Envie postbacks simulados usando os aplicativos de teste listados na tabela anterior. Considerações ao enviar postbacks simulados:<ul><li>Defina o app\_id e o valor de conversão conforme listado na tabela anterior.</li><li>Como as ad networks não podem gerar assinaturas compatíveis com a Apple, os postbacks simulados não precisam incluir os campos de assinatura. A AppsFlyer não irá verificá-los quanto a postbacks simulados.</li><li>As ad networks enviam o postback usando a abordagem POST ou REDIRECT.</li></ul></li></ol> |
| A AppsFlyer | Responde com os postbacks decodificados para o endpoint designado pela ad network durante a integração |

<div id="test-criteria-1" />

#### Critérios de teste

| Responsabilidade | Action |
| --- | --- |
| A AppsFlyer | Processa o postback e envia postbacks para a ad network. |
| Rede de anúncios | <ul><li>A ad network recebe e decodifica os postbacks traduzidos.</li><li>Os postbacks in-app enviados pela AppsFlyer correspondem aos fluxos esperados. For example, conversion value 3 for app ID888707087, the ad network receives 3 postbacks of *af\_SKAN\_revenue* event.</li></ul> |

</Accordion>

<div id="clarifications" />

## Esclarecimentos

Esclarecimentos relacionados a campos obrigatórios, enriquecimento, certificação e muito mais.

<div id="faq" />

<Accordion title="Perguntas frequentes">

| Perguntas e respostas sobre postbacks |
| --- |
| **Os campos de enriquecimento são obrigatórios?**<br /><br />Por enquanto, processaremos o postback mesmo que ele não inclua um ou mais dos seguintes parâmetros de enriquecimento. Considere que essas informações são necessárias pelos seguintes motivos:<ul><li>**ID da campanha da ad network**: Se tivermos integração de custo com você, isso será informado usando o ID da sua campanha.</li><li>**Nome da campanha da ad network**: Muitos anunciantes se baseiam no nome da campanha, e não no número da campanha.</li><li>**Endereço IP**: Necessário para a resolução de geolocalização.</li><li>**Timestamp**: Nos ajuda a atribuir a instalação à data correta.</li></ul> |
| **Podemos enviar apenas o ID da campanha ou o nome da campanha, mas não ambos?**<br /><br />Consulte a resposta anterior. Considere preencher o ID e o nome com o mesmo valor. |
| **We are using *Enrich and Forward.* Can we add key-value pairs that are not in the AppsFlyer specification?**<br /><br />Sim, é possível. Processaremos o postback e desconsideraremos as informações adicionais, desde que a assinatura de atribuição seja válida |
| **Os modelos de postback do SKAN são diferentes dos modelos de postback existentes?**<br /><br />sim, sim, O fluxo e a estrutura são diferentes. |
| **Receberemos um postback do SKAN e um postback de modelagem probabilística/determinística relacionados à mesma instalação, ou seja, um reporte duplicado da mesma instalação?**<br /><br />sim, sim, Em cada caso em que registrarmos uma instalação atribuída a você, independentemente do método, enviaremos um postback.<br /><br />Use *attribution\_source* para diferenciar postbacks do SKAN. |
| **Are we required to process the postback from AppsFlyer?**  <br /> <br /><br />Sem. No. Consider, that best practice is to optimize campaigns according to user-quality reported via the postback. |
| **Devemos chamar os links de atribuição da AppsFlyer ou basta enviar o postback com a carga útil do SKAN e os dados enriquecidos?**<br /><br />Basta nos enviar a carga útil do SKAN e os dados enriquecidos. |
| **O que é necessário para sermos certificados no dashboard da AppsFlyer como parceiro integrado ao SKAN?**<ul><li>Conclua a integração usando um dos métodos listados neste artigo</li><li>Envie-nos postbacks de aplicativos que usam a AppsFlyer como parceira de atribuição</li></ul> |
| **Como o limite de 100 IDs de campanha do SKAN me afeta**?<br /><br />O limite de 1 a 100 está relacionado à forma como você assina e numera suas campanhas na Apple. Isso significa que, a qualquer momento, você pode ter 100 campanhas únicas simultâneas. Permitimos que você enriqueça o postback com o nome e o ID reais da sua campanha. Isso significa que você mapeia o ID da campanha do SKAN para os IDs reais de campanha em uso no momento em que o postback é recebido. Isso significa que o limite de 100 IDs não restringe o número de campanhas que você mensura na AppsFlyer, desde que, é claro, você não tenha mais de 100 campanhas simultâneas para um determinado aplicativo. |

</Accordion>

<div data-zendesk-anchors="appsflyer-offering-for-ad-networks=oferta-da-appsflyer-para-ad-networks h_01HDG8991Y6EWWN9KYBR9FEAJZ=oferta-da-appsflyer-para-ad-networks skan-data-flow=fluxo-de-dados-da-skan h_01HDG8991Y5DW0BVD674RS88F2=fluxo-de-dados-da-skan main-integration-parts=principais-partes-da-integra%C3%A7%C3%A3o h_01HDG8991YDTY85NK7TQ26B2Z1=principais-partes-da-integra%C3%A7%C3%A3o send-data-to-appsflyer=enviar-dados-para-a-appsflyer h_01HDG8991YTFP2HE0Y8P8X0C20=enviar-dados-para-a-appsflyer h_01HDG8991YRW3TWSDARFM58FA8=enrich-and-forward skan-enriched-postback-protocol=protocolo-de-postback-enriquecido-da-skan h_01HDG8991YAKZMSA4MAY0YTFPB=protocolo-de-postback-enriquecido-da-skan skan-enriched-postback-json-parameters=par%C3%A2metros-json-do-postback-enriquecido-do-skan h_01HDG8991YS91CWESZH0M7CA00=par%C3%A2metros-json-do-postback-enriquecido-do-skan curl-example%E2%80%94enriched-skan-3-postback=exemplo-de-curl--postback-avan%C3%A7ado-da-skan-3 h_01HDG8991YFHBQDRG4K0XA3JQ8=exemplo-de-curl--postback-avan%C3%A7ado-da-skan-3 curl-example%E2%80%94enriched-skan-4-postback-with-fine-conversion-values=exemplo-de-curl--postback-avan%C3%A7ado-da-skan-4-com-valores-de-convers%C3%A3o-refinados h_01HDG8991YNVCK92TVNJHGKNG5=exemplo-de-curl--postback-avan%C3%A7ado-da-skan-4-com-valores-de-convers%C3%A3o-refinados curl-example%E2%80%94enriched-skan-4-postback-with-coarse-conversion-values=curl-exampleenriched-skan-4-postback-with-coarse-conversion-values h_01HDG8991YXTS27V0NJ4ZXQ53T=curl-exampleenriched-skan-4-postback-with-coarse-conversion-values h_01HDG8991YGHWJ9R1ZKTCFJZCA=redirect implementation=implementa%C3%A7%C3%A3o h_01HDG8991YBR7VWRH9079GT695=implementa%C3%A7%C3%A3o query-params-for-campaign-details-not-mandatory=par%C3%A2metros-de-consulta-para-detalhes-da-campanha-n%C3%A3o-obrigat%C3%B3rios h_01HDG8991YQB77MMF906PCAWC2=par%C3%A2metros-de-consulta-para-detalhes-da-campanha-n%C3%A3o-obrigat%C3%B3rios receive-data-from-appsflyer=receber-dados-da-appsflyer h_01HDG8991ZNF2PKKJN3FPN6QXA=receber-dados-da-appsflyer h_01HDG8991ZKR35WHWVX0DHC612=principles h_01HDG8991ZG9GMMY57XYZF1Q3S=postback-macros-available-to-ad-network-partners h_01HDG8991ZD6ARRK6Z83NQBGRR=skan-postback-examples integration-testing=teste-a-integra%C3%A7%C3%A3o h_01HDG8991ZS10MJJ3ZN31YDPTK=teste-a-integra%C3%A7%C3%A3o h_01HDG8991ZPR41S5T9HZ9N1ZWF=real-environment testing-integration=integra%C3%A7%C3%A3o-de-testes h_01HDG8991ZJ1KTHX6FE9R0QJNP=integra%C3%A7%C3%A3o-de-testes test-criteria=crit%C3%A9rios-de-teste h_01HDG8991ZP59K8RQQ7G1GGMPG=crit%C3%A9rios-de-teste h_01HDG8991Z7DX65Y3E6RPHB2M3=simulated-postbacks integration-steps=etapas-de-integra%C3%A7%C3%A3o h_01HDG8991ZZPYH7H329EY8TNV9=etapas-de-integra%C3%A7%C3%A3o test-criteria::26c15d59=crit%C3%A9rios-de-teste-1 h_01HDG8991ZR4F21KVYF0MQ9GZA=crit%C3%A9rios-de-teste-1 clarifications=esclarecimentos h_01HDG8991Z8C0K0SMBT9VSX12Y=esclarecimentos h_01HDG8991ZDAGFV8GGC1RH73KQ=faq" />
