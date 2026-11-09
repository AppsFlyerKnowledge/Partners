---
title: Mapeamento dinâmico de eventos para eventos in-app
metadata:
  keywords:
    - In-App
    - Mapping
    - Dynamic Event Mapping
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2016-05-26T08:48:23Z'
  edited_at: '2026-08-18T00:40:58Z'
  id: 208996726
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/208996726
---
> **Em resumo:** Configure seu link de atribuição para que seus parceiros (como TUNE ou CAKE) possam receber diferentes postbacks para um único evento in-app, com base nos IDs de objetivo.

<div id="introduction" />

## Introdução

Diferentes postbacks podem ser enviados para um evento in-app dependendo do ID de objetivo.

Esse recurso oferece suporte a networks que usam HasOffers, CAKE ou outras networks que querem receber diferentes postbacks de eventos in-app para um único evento in-app do SDK.

Na página Integrações ativas no dashboard, os anunciantes mapeiam cada um dos eventos do SDK para a tag de evento dinâmica preferida de cada parceiro. A tag de evento inclui tanto eventos in-app quanto postbacks de eventos in-app rejeitados.

Isso permite que as ad networks abram várias campanhas com uma tag de evento dinâmica separada (exemplo: a HasOffers chama isso de goal\_id) para cada campanha. As tags de evento dinâmicas são então passadas para a ad network no postback com base no valor inserido na URL de clique.

<div id="attribution-link" />

## Link de atribuição

<div id="attribution-link-example" />

> 📄 **Exemplo de link de atribuição**
>
> **Decodificado**:
>
> ```http
> https://app.appsflyer.com/com.xyz.abc?pid=mediasource_int&clickid={transaction_id}
> &goalid_1={XXX}&goalid_2={YYY}
> ```

O anunciante deve mapear todos os goal\_ids na seção de eventos in-app (veja abaixo) de acordo com as instruções da network.

No exemplo abaixo, level20\_finished é mapeado como $$click(goalid\_1) e level25\_finished é mapeado como $$click(goalid\_2).

Quando o usuário do aplicativo conclui o nível 20, a AppsFlyer retorna ao valor relevante (neste caso, XXX, como aparece no link de atribuição acima) e o envia no postback.

Se o mesmo usuário ou outro usuário concluir o nível 25, a AppsFlyer retornará novamente ao link de atribuição, preencherá dinamicamente o goal\_id com o valor relevante (neste caso, YYY) e o enviará no postback.

<Image align="center" alt="Goadid.png" src="https://files.readme.io/35390305a93cc7a49f193fa1667b491827736252a9133bc01d01c07dfdc38586-360001400478.png" />

<div data-zendesk-anchors="introduction=introdu%C3%A7%C3%A3o attribution-link=link-de-atribui%C3%A7%C3%A3o" />
