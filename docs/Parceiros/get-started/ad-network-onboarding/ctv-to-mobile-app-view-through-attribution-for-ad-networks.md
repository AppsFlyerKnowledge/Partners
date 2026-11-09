---
title: Atribuição de view-through no fluxo CTV-to-mobile app para ad networks
metadata:
  keywords:
    - Attribution
    - Ad Networks
    - Partners
    - CTV
    - CTV Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roi-tamir
    - CTV Attribution
    - Ad Networks
  created_at: '2022-08-21T06:49:24Z'
  edited_at: '2026-08-27T00:37:06Z'
  id: 8528418936977
  locale: pt
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/pt/articles/8528418936977
---
> **At a glance:** Atribua instalações de apps mobile a anúncios visualizados em dispositivos de TV conectada (CTV).

<div id="ctv-to-mobile-app-attribution-for-ad-networks" />

## Atribuição de CTV-to-mobile app para ad networks

Com as URLs de impressão cross-platform da AppsFlyer, você pode atribuir instalações de apps mobile a anúncios exibidos em CTV. Múltiplas instalações dentro da mesma residência podem ser atribuídas à mesma impressão de anúncio na CTV.

<Image align="center" alt="Diagrama do fluxo de atribuição de CTV para app mobile" src="https://files.readme.io/401bcb083e1cc618794cb302668f7271cf825a5a6045ff10055e0164baf423a1-19774176963473.jpg" />

A atribuição de view-through no fluxo CTV-to-mobile usa uma <Anchor target="_blank" href="/marketers/pt/docs/set-up-cross-platform-links-for-multi-device-campaigns#setup">URL de impressão do OneLink</Anchor> que se baseia em um template cross-platform do OneLink (e que possui um template ID) criado pelos anunciantes. Isso permite que os anunciantes agrupem múltiplos apps de diferentes plataformas (por exemplo, apps do Android e do iOS) usando uma única URL.

Assim, quando os usuários veem um anúncio na CTV, a URL de impressão é enviada para a AppsFlyer em tempo real. 

Exemplo de URL:

```
https://impressions.onelink.me/{template_id}?pid=__media_source__&af_xplatform=true&af_xplatform_vt_lookback=24h&af_siteid=__CSITE__&c=__CAMPAIGN_NAME__&af_channel=__PLACEMENT__&af_c_id=__CAMPAIGN_ID__&af_adset=__AID_NAME__&af_adset_id=__AID__&af_ad=__CID_NAME__&af_ad_id=__CID__&af_source_platform=__source_platform__&af_source_device_category=__device_category__&af_ad_type=__CTYPE__&af_ip=__IP__&af_ua=__UA__&redirect=false
```

A AppsFlyer envia postbacks para você após cada conversão.

> 📘 **Note**
>
> Este recurso está disponível apenas para parceiros designados. Para saber mais, entre em contato com seu Partner Development Manager (PDM).

<Accordion title="Configurar atribuição de CTV para mobile">

**Para configurar a atribuição de view-through no fluxo CTV-to-mobile com um anunciante**:

1. Certifique-se de que é um <Anchor target="_blank" href="/partners/pt/docs/getting-started-onboarding-guide-for-ad-networks">parceiro integrado da AppsFlyer</Anchor>, de que configurou corretamente os postbacks e de que [testou sua integração de CTV para app mobile](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#test-partner-integration) com a AppsFlyer.
2. Certifique-se de que a URL contenha os [parâmetros obrigatórios](/docs/ctv-to-mobile-app-view-through-attribution-for-ad-networks#parameters), bem como quaisquer outros parâmetros que você queira.
3. Envie o user IP e o user agent para a AppsFlyer. Estes são necessários para a atribuição de visualizações de apps móveis para CTV. Eles podem ser enviados:
   1. Como os parâmetros `af_ip` e `af_ua` na URL de impressão.
   2. Como os parâmetros `<X-Forwarded-For>` e `<User-Agent>` nos cabeçalhos da solicitação.

</Accordion>

<Accordion title="Testar a integração com o parceiro">

**Para testar a atribuição de view-through no fluxo CTV-to-mobile**:

1. Use os seguintes apps de teste: com.appsflyer.android.deviceid e id1192323960
2. Entre em contato com a equipe de Partner Solutions da AppsFlyer para receber uma URL de teste. Para isso, faça login no seu [dashboard de parceiro](https://hq1.appsflyer.com/auth/login) e, no menu superior, clique em **ajuda** > **fale com a nossa equipe**.
   * Exemplo de URL: `https://impressions.onelink.me/dfHa?pid=partner_int&c=test_1&af_xplatform=true&af_xplatform_vt_lookback=24h&af_ip=MACRO&af_ua=MACRO&redirect=false`
3. Confirme se o ID do parceiro no parâmetro `pid` está correto.
4. Insira o seu endereço IP para o parâmetro `af_ip`.
5. Insira o seu user agent para o parâmetro `af_ua`.
6. Insira a URL em um navegador de desktop.
7. No seu dispositivo mobile, vá para a loja de aplicativos e faça o download, instale e inicie o aplicativo.
8. Uma nova instalação aparece na AppsFlyer, junto com um postback correspondente. Se não vir a instalação ou não receber o postback, entre em contato com a equipe de Partner Solutions.

</Accordion>

<Accordion title="Parâmetros">

Os seguintes parâmetros são usados para fornecer dados de atribuição e mensuração aos anunciantes.

| Parâmetro | Obrigatório | Descrição |
| --- | --- | --- |
| template\_id | ✓ | O ID do <Anchor target="_blank" href="/marketers/pt/docs/create-a-onelink-template">modelo OneLink</Anchor>. O modelo contém definições básicas de previsão para os aplicativos dos anunciantes e é a base para criar outros links. Observação: nunca codifique o valor de `template_id`. |
| pid | ✓ | O identificador do parceiro, atribuído pela AppsFlyer à fonte de mídia (ad network) que posiciona o anúncio. |
| af\_xplatform | ✓ | <ul><li>Definido pelo anunciante para indicar se o link oferece suporte à atribuição cross-platform.</li><li>Valores: true/false</li></ul> |
| af\_xplatform\_vt\_lookback | - | Janela configurável que indica o número de horas após a impressão durante as quais a instalação do aplicativo pode ser atribuída à impressão. Valores de parâmetros disponíveis: 1h - 72h (horas). O valor padrão é 24h. |
| af\_ip | ✓ | <ul><li>O endereço IP do dispositivo de CTV que exibe o anúncio.</li><li>Se o endereço IP não for enviado na URL, ele deve ser enviado nos cabeçalhos da solicitação para que a AppsFlyer possa realizar a atribuição de CTV para app mobile.</li></ul> |
| af\_ua | ✓ | <ul><li>O user agent do dispositivo CTV que exibe o anúncio.</li><li>Se o user agent não for enviado na URL, ele deve ser enviado nos cabeçalhos da solicitação para que a AppsFlyer possa realizar a atribuição de CTV para app mobile.</li></ul> |
| af\_source\_platform | - | <ul><li>Um conjunto de valores que representa o sistema operacional onde a impressão ocorre.</li><li>Um rótulo descritivo atribuído a uma campanha publicitária<ul><li>Android</li><li>ios</li><li>tizen</li><li>webos</li><li>smartcast</li><li>roku</li><li>Windows Phone</li><li>vidaa</li><li>PlayStation</li><li>Site</li></ul></li></ul> |
| af\_source\_device\_category | - | <ul><li>Um conjunto de valores que representa o tipo de dispositivo onde a impressão ocorre.<ul><li>tv</li><li>mobile\_phone</li><li>Desktop</li><li>tablet</li><li>set\_top\_box</li><li>games\_console</li><li>unknown\_device\_category</li><li>media\_player</li></ul></li></ul> |

Outros parâmetros que podem ser adicionados à URL podem ser encontrados no <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">artigo sobre a estrutura e os parâmetros de links de atribuição</Anchor>.

</Accordion>

<Accordion title="Características e limitações">

| Caraterística | A descrição |
| --- | --- |
| Janela de atribuição | Entre 1 e 72 horas, dependendo do parâmetro de janela de lookback `af_xplatform_vt_lookback`. |
| Redirecionamento | <ul><li>Reatribuição: disponível para cross-platform-to-mobile. Indisponível para outras plataformas.</li><li>Reengajamento: Indisponível</li></ul> |
| Método de atribuição | Atribuição via visualização usando modelagem probabilística (endereço IP) |
| Atribuição a nível doméstico | Disponível. Significa que várias instalações dentro de uma mesma residência podem ser atribuídas à mesma impressão publicitária do CTV. |
| Testar a integração com o parceiro | Não disponível para redes de anúncios que foram sinalizadas por altas taxas de fraude de app móvel-para-app móvel ou são afiliadas a diferentes fontes de mídia sinalizadas. |

</Accordion>

<div data-zendesk-anchors="ctvtomobile-app-attribution-for-ad-networks=atribui%C3%A7%C3%A3o-de-ctv-to-mobile-app-para-ad-networks h_01HE2X91GTDTPKKFBRRYYFMHDW=atribui%C3%A7%C3%A3o-de-ctv-to-mobile-app-para-ad-networks" />
