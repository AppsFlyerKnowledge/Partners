---
title: Integração da FOCUUS com a AppsFlyer
metadata:
  keywords:
    - Focuus
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
  created_at: '2016-10-02T05:18:19Z'
  edited_at: '2026-08-18T00:41:03Z'
  id: 213374546
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/213374546
---
> **Visão geral:** As ad networks que usam o FOCUUS podem utilizar a solução de modelo probabilístico da AppsFlyer para receber dados de atribuição sobre instalações e eventos in-app.

<div id="creating-your-attribution-link" />

## Criando seu link de atribuição

O link de atribuição consiste no link de atribuição base da AppsFlyer abaixo e em macros adicionais incluídas pela ad network.

Veja abaixo o link de atribuição base da AppsFlyer com uma explicação detalhada por macro:

| URL Base da AppsFlyer | A descrição |
| --- | --- |
| https://app.appsflyer.com | Ponto final da AppsFlyer |
| ativado | ID exclusivo do aplicativo |
| pid | O nome do canal de mídia inclui \_int para identificar a rede integrada nos servidores AppsFlyer |
| C | Campaign name |

<div id="recommended-attribution-link-parameters" />

### Parâmetros de link de atribuição recomendados

| Parâmetro da AppsFlyer | Macros da FOCUUS | A descrição |
| --- | --- | --- |
| **clickid** | **`{tid}`** | **ID da solicitação de cada sessão do usuário** - **Obrigatório** |
| af\_siteid | `{publisher_id}` | ID do afiliado que promove a oferta - Opcional |

Para obter a lista completa de parâmetros da AppsFlyer, <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#parâmetros-do-link-de-atribuição">clique aqui</Anchor>.

A FOCUUS permite um número ilimitado de macros, e você pode nomeá-las como quiser; <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#parâmetros-do-link-de-atribuição">clique</Anchor> <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827379-traffic-source-template-tokens-macros">aqui</Anchor>.

<div id="complete-attribution-link-template" />

### Template de link de atribuição completo

`https://app.appsflyer.com/com.appsflyer?pid={traffic_source}&clickid={tid}&af_siteid={publisher_id}`

Esse link de atribuição é definido no <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827784-adding-a-new-link">destino</Anchor> da sua campanha da FOCUUS.

<div id="install-and-in-app-event-postbacks" />

## Instalação e postbacks de eventos in-app

Para criar seus postbacks de instalação e evento in-app na **FOCUUS**

1. Crie um <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827775-events">novo evento</Anchor> (instalação e quaisquer outros eventos in-app).
2. <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827766-s2s-integration">Gere o pixel</Anchor> (postback) para implementação.
3. Copie a URL do postback exibida na caixa rotulada como <Anchor target="_blank" href="http://support.focuus.com/knowledgebase/articles/827766-s2s-integration">Server2Server Pixel</Anchor>.
4. Substitua o TRANSACTION\_ID pela macro da AppsFlyer — “**clickid**”  
   `https://pixel.focuusing.com/event.php?type=imp&tid={clickid}`

**Parâmetros opcionais de postback**

| Macros da FOCUUS | A descrição | Exemplo |
| --- | --- | --- |
| event\_value | Valor de payout para cada tipo de evento | `https://pixel.focuusing.com/event.php?type=cpi&tid={Your_TRANSACTION_ID}&eid=49816&event_value={25}` |

**O nome do evento (instalação, registro etc.) aparece por padrão no pixel gerado. exemplo:**

* `https://traffic.focuusing.com/install?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/conversion?tid={TRANSACTION_ID}`
* `https://traffic.focuusing.com/ftd?tid={TRANSACTION_ID}`

<div data-zendesk-anchors="creating-your-attribution-link=criando-seu-link-de-atribui%C3%A7%C3%A3o 01JFT11W3GWZ3QFYPHEZTS7EX7=criando-seu-link-de-atribui%C3%A7%C3%A3o recommended-attribution-link-parameters=par%C3%A2metros-de-link-de-atribui%C3%A7%C3%A3o-recomendados 01JFT11W3QWT08KMGEPGK7MV5R=par%C3%A2metros-de-link-de-atribui%C3%A7%C3%A3o-recomendados complete-attribution-link-template=template-de-link-de-atribui%C3%A7%C3%A3o-completo 01JFT11W3Y7HRB7FYS1K173G2W=template-de-link-de-atribui%C3%A7%C3%A3o-completo install-and-inapp-event-postbacks=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app 01JFT11W3YMN4RBW0WFTQ9EADK=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app" />
