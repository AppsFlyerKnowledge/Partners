---
title: Integração do AppNexus com a AppsFlyer
metadata:
  keywords:
    - Integration
    - AppNexus
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
  created_at: '2016-01-11T14:45:34Z'
  edited_at: '2026-08-18T00:40:53Z'
  id: 207583523
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/207583523
---
> **Visão geral:** As ad networks que usam a Affise podem usar a solução de modelo probabilístico da AppsFlyer para receber dados de atribuição sobre instalações e eventos in-app.

<div id="starting-the-integration" />

## Iniciando a integração

Para iniciar a integração, você deve enviar à AppsFlyer o link de atribuição e o postback para fins de relatório.

Abaixo você pode encontrar o link de atribuição de base com uma explicação detalhada por cada parâmetro:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| URL Base da AppsFlyer | A descrição |
| --- | --- |
| https://app.appsflyer.com | End-Point da AppsFlyer |
| ativado | ID exclusivo do aplicativo - Valor dinâmico alterado por aplicativo promovido |
| pid | O nome do canal de mídia inclui **\_int** para identificar a rede **integrada** nos servidores AppsFlyer |
| C | Nome da campanha |

**Macros de ID de publicidade do AppNexus**

| Sistema operacional | Macro |
| --- | --- |
| com o Android | &advertising\_id=$`{DEVICE_AAID}` |
| /docs/ctv-pc-and-console-platform-attribution-concepts | idfa=$`{DEVICE_APPLE_IDA}` |

**Parâmetros de link de atribuição recomendados**

| Parâmetro da AppsFlyer | Macros do AppNexus | A descrição |
| --- | --- | --- |
| clickid | $`{SSP_DATA}` | ID da solicitação de cada sessão do usuário - **Obrigatório** |
| af\_siteid | $`{PUBLISHER_ID}` | ID do afiliado que promove a oferta - **Opcional** |

Para obter a lista completa de parâmetros da AppsFlyer, <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">clique aqui</Anchor>.

Para obter a lista completa de macros do AppNexus, <Anchor target="_blank" href="https://wiki.appnexus.com/display/sdk/Welcome">clique aqui</Anchor>.

<div id="complete-attribution-link-template" />

### Template de link de atribuição completo:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=${SSP_DATA}&af_siteid=${PUBLISHER_ID}
```

<div id="install-and-in-app-event-postbacks" />

### Instalação e postbacks de eventos in-app

Postback de instalação global:

```http
https://sspx-router.adnxs.net/sspx?id={ID}&sspdata={clickid}
```

`{ID}`, o ID da network fornecido pelo AppNexus, inserido no dashboard da AppsFlyer por aplicativo.

<div id="appsflyer-install-dashboard" />

### Dashboard de instalações da AppsFlyer

[<Image align="center" alt="appnexus-pixelid.png" src="https://files.readme.io/0f14632fc7421fbbb26f90c13cc37afad58e4e217f4bcebd931cddb7576c5113-360018728918.png" />](https://support.appsflyer.com/hc/article_attachments/49929610810129)

Informações adicionais de atribuição podem ser incluídas no postback por solicitação, como Código do país, ID de publicidade, IDFA e assim por diante.

<div id="finalizing-your-registration" />

## Finalização do seu cadastro

* Se você tiver uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor>.
* Se você não tiver uma integração com a AppsFlyer, preencha a solicitação de registro de Parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

<div data-zendesk-anchors="starting-the-integration=iniciando-a-integra%C3%A7%C3%A3o 01JFT0Z4H4N0SFK6CAKQGW41Q4=iniciando-a-integra%C3%A7%C3%A3o complete-attribution-link-template=template-de-link-de-atribui%C3%A7%C3%A3o-completo 01JFT0Z4H7MA1B9FMNWKESF170=template-de-link-de-atribui%C3%A7%C3%A3o-completo install-and-inapp-event-postbacks=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app 01JFT0Z4H7TZPQCFGZCASNWHD7=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app appsflyer-install-dashboard=dashboard-de-instala%C3%A7%C3%B5es-da-appsflyer 01JFT0Z4H89BP3YWFRSJ69RK6D=dashboard-de-instala%C3%A7%C3%B5es-da-appsflyer finalizing-your-registration=finaliza%C3%A7%C3%A3o-do-seu-cadastro 01JFT0Z4H9TF582WHB69MT9VP2=finaliza%C3%A7%C3%A3o-do-seu-cadastro" />
