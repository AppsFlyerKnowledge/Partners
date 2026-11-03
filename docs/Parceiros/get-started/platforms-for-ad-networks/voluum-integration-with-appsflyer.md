---
title: Integração do Voluum com a AppsFlyer
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
  created_at: '2016-01-11T14:46:09Z'
  edited_at: '2026-08-18T00:41:26Z'
  id: 207274016
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/207274016
---
> **Visão geral:** As ad networks que usam o Voluum podem utilizar a solução de modelo probabilístico da AppsFlyer para receber dados de atribuição sobre instalações e eventos in-app.

## Iniciando a integração

Para iniciar a integração, você deve enviar à AppsFlyer o link de atribuição e o postback para fins de relatório.

Abaixo você pode encontrar o link de atribuição de base com uma explicação detalhada por cada parâmetro:

`https://app.appsflyer.com/app_id?pid=mediaName_int&c={campaign}`

| URL Base da AppsFlyer | A descrição |
| --- | --- |
| https://app.appsflyer.com | End-Point da AppsFlyer |
| ativado | ID exclusivo do aplicativo - Valor dinâmico alterado por aplicativo promovido |
| pid= | O nome do canal de mídia inclui **\_int** para identificar a network **integrada** nos servidores da AppsFlyer |
| c= | Campaign name |

**Parâmetros de link de atribuição recomendados:**

| Parâmetro da AppsFlyer | Voluum Macros | A descrição |
| --- | --- | --- |
| &clickid= | `{clickid}` | ID de transação exclusivo da sessão do usuário - **Obrigatório** |
| &af\_siteid= | `{trafficsource.id}` | ID da origem do tráfego - **Opcional** |

** Para obter a lista completa de parâmetros da AppsFlyer, <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">clique aqui</Anchor>

** Para obter a lista completa de macros do Voluum, <Anchor target="_blank" href="http://feedback.voluum.com/knowledgebase/articles/318681-click-urls">clique aqui</Anchor>

### Template de link de atribuição completo

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={clickid}&af_siteid={trafficsource.id}
```

### Instalação e postbacks de eventos in-app

Postback de instalação global:

```http
https://{Company-Domain}.voluumtrk.com/postback?cid={clickid}
```

Postback de evento in-app global:

```http
https://{Company-Domain}.trackvoluum.com/postback?cid={clickid}&payout={monetary}&txid={event-name}
```

** `{Company-Domain}` é o nome do ID da network (domínio) fornecido pelo Voluum.  
** txid= Definido como **Event Tag** no dashboard da AppsFlyer para cada Aplicativo pelo anunciante. Este é o nome real do evento in-app do aplicativo.

### Painel de eventos in-app da AppsFlyer

![Voluum_msc_new_1.png](https://files.readme.io/ecad61ab31de52e88c483daeaa05cd223ece998f3d8c22ae400c68fc2b7537f2-21479841978001.png)  
** Informações adicionais de atribuição podem ser incluídas no postback por solicitação, como Código do país, ID de publicidade, IDFA, etc.

## Finalizando seu cadastro

* Se você tem uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor>.
* Se você não tem uma integração com a AppsFlyer, preencha a solicitação de registro de parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

<div data-zendesk-anchors="starting-the-integration=iniciando-a-integra%C3%A7%C3%A3o 01JFT0VZZ5KVMKYRD222JT55NH=iniciando-a-integra%C3%A7%C3%A3o complete-attribution-link-template=template-de-link-de-atribui%C3%A7%C3%A3o-completo 01JFT0VZZ7B1RRY82B65GWF4P7=template-de-link-de-atribui%C3%A7%C3%A3o-completo install-and-inapp-event-postbacks=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app 01JFT0VZZ86KYXSVE1QBD2V0HF=instala%C3%A7%C3%A3o-e-postbacks-de-eventos-in-app appsflyers-inapp-event-dashboard=painel-de-eventos-in-app-da-appsflyer 01JFT0VZZ9A4JWG38KPH0CNQ72=painel-de-eventos-in-app-da-appsflyer finalizing-your-registration=finalizando-seu-cadastro 01JFT0VZZATFYY75QPCPKZF3S6=finalizando-seu-cadastro" />
