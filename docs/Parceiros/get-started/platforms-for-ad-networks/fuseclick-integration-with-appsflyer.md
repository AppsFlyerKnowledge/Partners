---
title: Integração do Fuseclick com a AppsFlyer
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
  created_at: '2016-01-11T14:46:45Z'
  edited_at: '2026-08-18T00:41:05Z'
  id: 207583573
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/207583573
---
> **Visão geral:** As ad networks que usam o FuseClick podem utilizar a solução de modelo probabilístico da AppsFlyer para receber dados de atribuição sobre instalações e eventos in-app.

## Link de atribuição base

Abaixo você pode encontrar o link de atribuição de base com uma explicação detalhada por cada parâmetro:

```http
https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}
```

| URL Base da AppsFlyer | A descrição |
| --- | --- |
| https://app.appsflyer.com | Ponto final da AppsFlyer |
| ativado | ID exclusivo do aplicativo - Valor dinâmico alterado por aplicativo promovido |
| pid | O nome do canal de mídia inclui **\_int** para identificar a rede **integrada** nos servidores AppsFlyer |
| C | Nome da campanha |

**Parâmetros de link de atribuição recomendados:**

| Parâmetro da AppsFlyer | Macros FuseClick | Descrição |
| --- | --- | --- |
| clickid | `{TID}` | ID da solicitação de cada sessão do usuário - **Obrigatório** |
| af\_siteid | `{SC}` | ID do afiliado que promove a oferta - **Opcional** |

Para obter a lista completa de parâmetros da AppsFlyer, <Anchor target="_blank" href="/partners/pt/docs/postback-macros-for-ad-networks">clique aqui</Anchor>

Para obter a lista completa de macros do FuseClick, <Anchor target="_blank" href="https://support.fuseclick.com/documentation/open/iwf/2016/0805/199.html">clique aqui</Anchor>

Template de link de atribuição completo:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={TID}&af_siteid={ADV_SID}
```

### Instalação e postbacks de eventos in-app

Postback de instalação global:

```
https://tracking.zadsmobile.com/pb?tid={TID}
```

Informações adicionais de atribuição podem ser incluídas no postback por solicitação, como Código do país, ID de publicidade, IDFA e muito mais.

## Finalizando seu registro

* Se você tiver uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor>.
* Se você não tiver uma integração com a AppsFlyer, preencha a solicitação de registro de Parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

<div data-zendesk-anchors="basic-attribution-link=link-de-atribui%C3%A7%C3%A3o-base 01JFT0DX287AWQND2BYFSV50HW=link-de-atribui%C3%A7%C3%A3o-base install-and-inapp-event-postbacks=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app 01JFT0DX2B6FFE3K7VTXG1YVJ1=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app finalizing-your-registration=finalizando-seu-registro 01JFT0DX2BD8A19BY9197X11QW=finalizando-seu-registro" />
