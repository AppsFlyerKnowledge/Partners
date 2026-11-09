---
title: Integração do PeerClick com a AppsFlyer
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
  created_at: '2024-01-07T08:27:18Z'
  edited_at: '2026-08-18T00:41:16Z'
  id: 21479841979793
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/21479841979793
---
> **Visão geral:** As redes de anúncios que usam o PeerClick podem se beneficiar da solução de modelagem probabilística da AppsFlyer para receber dados de atribuição sobre instalações e eventos in-app.

<div id="starting-the-integration" />

## Iniciando a integração

Para iniciar a integração, você deve enviar à AppsFlyer o link de atribuição e o postback para fins de relatório.

Abaixo você pode encontrar o link de atribuição de base com uma explicação detalhada por cada parâmetro:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| URL Base da AppsFlyer | Descrição |
| --- | --- |
| https://app.appsflyer.com | End-Point da AppsFlyer |
| ativado | ID exclusivo do aplicativo - Valor dinâmico alterado por aplicativo promovido |
| pid= | O nome do canal de mídia inclui **\_int** para identificar a rede **integrada** nos servidores AppsFlyer |
| c= | Nome da campanha |

**Parâmetros de link de atribuição recomendados:**

| Parâmetro da AppsFlyer | Voluum Macros | Descrição |
| --- | --- | --- |
| &clickid= | `{clickid}` | ID de transação exclusivo da sessão do usuário - **Obrigatório** |
| &af\_siteid= | `{trafficsource.id}` | ID da origem do tráfego - **Opcional** |

<div id="note" />

> 📘 **Observação**
>
> * Para obter a lista completa de parâmetros da AppsFlyer, <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">clique aqui</Anchor>
> * Para a lista completa do PeerClick, <Anchor target="_blank" href="https://help-center.peerclick.com/en/">clique aqui</Anchor>

<div id="complete-attribution-link-template" />

### Template de link de atribuição completo

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

<div id="install-and-in-app-event-postbacks" />

### Instalação e postbacks de eventos in-app

**Postback de instalação global:**

```http
https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}
```

**Postback de evento in-app global:**

`https://pstb.gopeerclick.com/postback?userid={peerclick_userid}&cid={clickid}&payout={monetary}&txid={event-name}`

* **userid:** O ID do usuário fornecido pelo PeerClick
* **txid:** O nome real do evento in-app do aplicativo, definido como **Event Tag** no painel da AppsFlyer para cada aplicativo pelo anunciante

<div id="appsflyers-in-app-event-dashboard" />

### Painel de eventos in-app da AppsFlyer

<Image align="center" alt="Voluum_msc_new_1.png" src="https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png" />
Informações adicionais de atribuição podem ser incluídas no postback por solicitação, como Código do país, ID de publicidade, IDFA, etc.

<div data-zendesk-anchors="starting-the-integration=iniciando-a-integra%C3%A7%C3%A3o h_01HKHFT3RFWF5H349GP7MHDAYX=iniciando-a-integra%C3%A7%C3%A3o h_01HM8M27S5WFJVKBG0JAFW548H=observa%C3%A7%C3%A3o complete-attribution-link-template=template-de-link-de-atribui%C3%A7%C3%A3o-completo h_01HKHFT3RFDW6GZM3E72SYPJSD=template-de-link-de-atribui%C3%A7%C3%A3o-completo install-and-inapp-event-postbacks=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app h_01HKHFT3RF1PTSJ4SF9RTQ93N8=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app appsflyers-inapp-event-dashboard=painel-de-eventos-in-app-da-appsflyer h_01HKHFT3RFDVPCSKJGZPRFB55V=painel-de-eventos-in-app-da-appsflyer" />
