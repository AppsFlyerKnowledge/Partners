---
title: Integração do Hubscale com a AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Hubscale
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
  created_at: '2017-12-19T12:25:07Z'
  edited_at: '2026-08-18T00:41:08Z'
  id: 115005874869
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/115005874869
---
> **Em resumo:** saiba como as ad networks que usam o Hubscale podem se integrar à AppsFlyer.

**Para iniciar a integração, você precisa enviar à AppsFlyer**:

1. Seu link de atribuição
2. Seu postback (para instalações e eventos in-app)

<div id="creating-the-attribution-link" />

## Criação do link de atribuição

o link de atribuição consiste no link de atribuição base da AppsFlyer abaixo e em macros adicionais acrescentadas pela ad network.

Veja abaixo o link de atribuição base da AppsFlyer com uma explicação detalhada de cada macro:

| URL Base da AppsFlyer | A descrição |
| --- | --- |
| https://app.appsflyer.com | Ponto final da AppsFlyer |
| ativado | ID exclusivo do aplicativo – valor dinâmico alterado por aplicativo promovido |
| pid | Nome do canal de mídia concatenado com \_int para identificar networks integradas |
| C | Nome da campanha |

Veja abaixo como o link de atribuição completo deve ficar depois que você adicionar macros adicionais do Hubscale:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={affiliate_id}&af_sub5={offer_id}af_ad_id=
{offer_file_id}&advertising_id={google_aid}&idfa={ios_ifa}" target="
_blank" rel="nofollow noopener noreferrer" data-is-link="https://
app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={transaction_id}
&af_siteid={affiliate_id}&af_sub5={offer_id}af_ad_id={offer_file_id}
&advertising_id={google_aid}&idfa={ios_ifa}">
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id=
{google_id}&idfa={ios_ifa}
```

<Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">Lista completa de parâmetros da AppsFlyer</Anchor>

<div id="global-postbacks-for-installs-and-in-app-events" />

## Postbacks globais para instalações e eventos in-app:

O Hubscale tem postbacks globais para instalações e eventos in-app:

Para instalações:

```http
https://companyname.156th.com/conv?transaction_id={publisher_ref_id}&ios_ifa={ios_ifa}
&google_id={google_aid}&app_version={app_version}&language={language}&ext_country_code={country_code}
&ext_city={city}&user_agent={user_agent}&user_ip={device_ip}&adv_revenue={revenue_usd}
```

Para eventos pós-instalação, o Hubscale pode registrar até nove eventos pós-instalação para o mesmo ID da transação. Nove postbacks globais devem ser criados como modelos, conforme mostrado abaixo:

<Table>
  <thead>
    <tr>
      <th>
        Número do evento
      </th>
      <th>
        Modelo de URL
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Evento 2 (o evento 1 é a instalação)
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=2
        ```
      </td>
    </tr>
    <tr>
      <td>
        Evento 3
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=3
        ```
      </td>
    </tr>
    <tr>
      <td>
        Evento 4
      </td>
      <td>
        ...
      </td>
    </tr>
    <tr>
      <td>
        ...
      </td>
      <td>
        ...
      </td>
    </tr>
    <tr>
      <td>
        Evento 10
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=10
        ```
      </td>
    </tr>
  </tbody>
</Table>

A tag de evento é o que o anunciante insere ao mapear os eventos.

<Image align="center" alt="In-App_Events.png" src="https://files.readme.io/5fa9ea3c2428e0dce7ce6a8062ebdf9aca5b2f873cc4e3d76d815d83b3a72b64-360002301369.png" />

Se o nome do parceiro que usa a Hubscale for PARTNER, então o domínio normalmente será: partner.156th.com.

Link genérico de atribuição:

```http
https://app.appsflyer.com/com.appsflyer?pid=partnername_int&clickid={transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id={google_id}&idfa={ios_ifa}
```

<div id="finalizing-your-registration" />

## Finalizar seu cadastro

* Se você tem uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget de assistente do parceiro</Anchor>.
* Se você não tem uma integração com a AppsFlyer, preencha a solicitação de cadastro de Parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

<div id="mapping-of-appsflyer-parameters-and-hubscale-macros" />

## Mapeamento dos parâmetros da AppsFlyer e das macros da Hubscale

| Parâmetros da AppsFlyer | Macros da Hubscale | Visão geral |
| --- | --- | --- |
| pid | pub\_id | Nome do canal de mídia - para parceiros integrados  <br />e não deve ser alterado. <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#partner-id-pid-parameter">Mais detalhes</Anchor>. |
| C | campaign\_name | Nome da campanha - fornecido pelo anunciante. |
| clickid | transaction\_id | O identificador de clique único da rede de anúncios |
| af\_siteid | pub\_id | ID do publisher da rede de anúncios |
| af\_sub\_siteid | sub\_pub\_id | ID do publisher/sub-rede de anúncios |
| af\_c\_id | id\_da\_campanha | ID da campanha - fornecido pelo anunciante |
| af\_adset |  | Nome do conjunto de anúncios - fornecido pelo anunciante. Adset  <br />é um nível intermediário na hierarquia entre  <br />Campanha e Anúncio. <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#níveis-de-granularidade-de-dados">Ver mais</Anchor> |
| af\_ad | adv\_name | Nome do anúncio (<Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#níveis-de-granularidade-de-dados">ver mais</Anchor>) |
| af\_ad\_id | adv\_id | ID do anúncio |
| af\_cost\_model | adv\_payout\_model | Modelo de custo — o CPI é atualmente o único  <br />modelo com suporte |
| af\_cost\_currency | moeda\_do\_pagamento\_do\_anunciante | Código da moeda (exemplo: USD) |
| af\_cost\_value | valor\_do\_pagamento\_do\_anunciante | Valor de custo |

<div data-zendesk-anchors="creating-the-attribution-link=cria%C3%A7%C3%A3o-do-link-de-atribui%C3%A7%C3%A3o 01JFT1EB6KZE1D6C9HMXQ5A841=cria%C3%A7%C3%A3o-do-link-de-atribui%C3%A7%C3%A3o global-postbacks-for-installs-and-inapp-events=postbacks-globais-para-instala%C3%A7%C3%B5es-e-eventos-in-app 01JFT1EB6PH56T619J1197TAK2=postbacks-globais-para-instala%C3%A7%C3%B5es-e-eventos-in-app finalizing-your-registration=finalizar-seu-cadastro 01JFT1EB70G5V9EBMD4XMAR3GF=finalizar-seu-cadastro mapping-of-appsflyer-parameters-and-hubscale-macros=mapeamento-dos-par%C3%A2metros-da-appsflyer-e-das-macros-da-hubscale 01JFT1EB71F36JD4QNB8KHKZRX=mapeamento-dos-par%C3%A2metros-da-appsflyer-e-das-macros-da-hubscale" />
