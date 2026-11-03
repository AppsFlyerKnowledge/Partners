---
title: Redirecionar usuários para a loja de aplicativos
metadata:
  keywords:
    - clicks
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2018-04-30T08:08:25Z'
  edited_at: '2026-08-18T00:39:10Z'
  id: 360000807629
  locale: pt
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/pt/articles/360000807629
---
> **Resumo:** Saiba mais sobre as opções para redirecionar usuários para a loja de aplicativos depois que um anúncio é veiculado e como enviar dados de engajamento para a AppsFlyer.

## Visão geral

A AppsFlyer recebe dados de engajamento (cliques e impressões) para atribuição de diversas maneiras:

* O usuário **clica** no anúncio e é [redirecionado para a AppsFlyere](#usuários-redirecionados-via-appsflyer) depois para a loja de aplicativos.
* O usuário **clica ou visualiza** o anúncio e é [enviado diretamente para a loja de aplicativos](#usuários-enviados-diretamente-pela-ad-network), enquanto o **link de atribuição é enviado para a AppsFlyer a partir do servidor**.

Em ambos os casos, a <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">estrutura e os parâmetros regulares do link de atribuição</Anchor> são usados.

> 📘 **Nota**
>
> Para SRNs, os dados são recebidos por meio de APIs especializadas

## Usuários redirecionados via AppsFlyer

Quando um anúncio é clicado, o usuário é direcionado para a AppsFlyer, que o redireciona para a loja de aplicativos pelo seguinte fluxo:

1. O usuário é redirecionado para a AppsFlyer
2. A AppsFlyer registra o clique
3. A AppsFlyer redireciona o usuário para a loja de aplicativos
4. O usuário instala o aplicativo
5. A AppsFlyer atribui a instalação

## Usuários enviados diretamente pela ad network

Quando um anúncio é clicado, o usuário é direcionado para a loja de aplicativos pela ad network, minimizando o número de redirecionamentos:

1. O usuário é enviado para a loja de aplicativos
2. A ad network reporta os dados de engajamento para a AppsFlyer a partir do dispositivo
3. O usuário instala o aplicativo
4. A AppsFlyer atribui a instalação

### Enviar dados de engajamento para a AppsFlyer

Enviar o usuário diretamente para a loja de aplicativos melhora sua experiência pois reduz o número de redirecionamentos. Isso também garante a atribuição precisa das instalações e permite tráfego de alta qualidade.

As ad networks só podem reportar cliques e impressões à AppsFlyer **diretamente a partir do dispositivo do usuário**.

#### Tempo de envio de redirecionamentos

Para evitar perda de atribuições e receita para a ad network, cliques e impressões devem ser enviados à AppsFlyer em tempo real:

* **URLs de impressão** devem ser reportados quando um anúncio é veiculado
* **Os URLs de clique** devem ser informados quando um usuário clica no anúncio

<div data-zendesk-anchors="overview=vis%C3%A3o-geral h_01HDY3CARC0A9504XGMJHYHGY4=vis%C3%A3o-geral h_01HDY3CARCZK06C5XHEQFQYA8W=nota redirect-users-via-appsflyer=usu%C3%A1rios-redirecionados-via-appsflyer 01HDYFGYW3FDR64C54KKPXRHDF=usu%C3%A1rios-redirecionados-via-appsflyer send-users-directly-by-the-ad-network=usu%C3%A1rios-enviados-diretamente-pela-ad-network 01HDYFH8ZCSP2SN4ZYQQVG7EED=usu%C3%A1rios-enviados-diretamente-pela-ad-network send-engagement-data-to-appsflyer=enviar-dados-de-engajamento-para-a-appsflyer h_01HDYGSEFHVF8ZD43XCVNGYT9N=enviar-dados-de-engajamento-para-a-appsflyer timing-of-sending-redirects=tempo-de-envio-de-redirecionamentos h_01HDXXDDXDEP43YHE3GF81BSKV=tempo-de-envio-de-redirecionamentos" />
