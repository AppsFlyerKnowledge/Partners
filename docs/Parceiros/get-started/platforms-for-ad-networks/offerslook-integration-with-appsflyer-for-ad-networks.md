---
title: Integração da Offerslook com a AppsFlyer para ad networks
metadata:
  keywords:
    - Offerslook
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
  created_at: '2016-05-31T08:47:36Z'
  edited_at: '2026-08-18T00:41:11Z'
  id: 209074606
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/209074606
---
> **Em resumo:** Saiba como ad networks que usam a Offerslook podem se integrar à AppsFlyer e receber dados de atribuição de instalação.

Para iniciar a integração, envie à AppsFlyer:

1. Seu link de atribuição

   ```http
   https://networkname.offerstrack.net/index.php?offer_id={offer_id}&aff_id={aff_id}
   ```
2. Seu postback (para instalações)  

   ```http
   https://networkname.offerstrack.net/advBack.php?click_id={click_id}&adv_id={adv_id}
   ```

<div id="creating-your-attribution-link" />

## Como criar seu link de atribuição

O link de atribuição consiste no link de atribuição base da AppsFlyer abaixo e em macros adicionais adicionadas pela ad network.

Veja abaixo o link de atribuição base da AppsFlyer com uma explicação detalhada de cada macro:

| URL Base da AppsFlyer | A descrição | Offerslook |
| --- | --- | --- |
| http://app.appsflyer.com | Endpoint da AppsFlyer |  |
| ativado | ID exclusivo do aplicativo – valor dinâmico alterado por aplicativo promovido |  |
| pid= | Nome do canal de mídia concatenado com \_int para identificar networks integradas |  |
| c= | Campaign name | `{offer_id}` |

Veja abaixo um exemplo de link de atribuição depois que você adicionar macros adicionais da Offerslook:

```http
  https://app.appsflyer.com/com.
  
  appsflyer?pid=mediaName_int&
  
  clickid={click_id}&af_siteid={
  
  aff_id}&advertising_id={ga_id}
  
  &idfa={idfa}
```

Para ver uma lista completa dos parâmetros da AppsFlyer, clique <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">aqui</Anchor>.

Macros disponíveis em links de atribuição da AppsFlyer

As seguintes macros estão disponíveis para uso no link gerado:

| **Nome da macro** | **A descrição** | **Offerslook** |
| --- | --- | --- |
| pid | Nome do canal de mídia - fornecido pela AppsFlyer e não deve ser alterado |  |
| C | Campaign name |  |
| clickid | O identificador de clique único da rede de anúncios | `{click_id}` |
| af\_siteid | ID do publisher da ad network | `{aff_id}` |

<div id="new-macros" />

#### Novas macros

O novo conjunto de macros adiciona uma série de parâmetros adicionais de forma clara, padronizada e estruturada. Recomendamos fortemente usar essas macros antes de voltar às macros af\_sub1-5.

| **Nome da macro** | **A descrição** | **Offerslook** |
| --- | --- | --- |
| af\_c\_id | ID da campanha - fornecido pelo anunciante | `{adv_sub1}<br /><br />{adv_sub2}<br /><br />{adv_sub3}` |
| af\_adset | Nome do conjunto de anúncios - fornecido pelo anunciante. Adset é um nível intermediário na hierarquia entre **Campanha** e **Anúncio**. |  |
| af\_adset\_id | Adset ID |  |
| af\_ad | Ad name |  |
| af\_ad\_id | ID do anúncio |  |
| af\_ad\_type | Tipo de anúncio - use qualquer coisa que "descreva" o formato do anúncio (exemplos: vídeo ou banner, tamanho médio ou grande) |  |
| af\_canal | O canal pelo qual os anúncios são distribuídos (por exemplo: YouTube vs. Pesquisa Google) |  |
| af\_keywords | Lista de palavras-chave para campanhas que usam texto para target. |  |
| af\_cost\_model | Modelo de custo - atualmente, há suporte para CPI, que é o modelo padrão. Os valores de CPC e CPA também são válidos. | `{pricing_type}` |
| af\_cost\_currency | Código da moeda (exemplo: USD) | `{currency}` |
| af\_cost\_value | Valor de custo | `{revenue}` |

**Macros específicas do Android**

| **Nome da macro** | **A descrição** | **Offerslook** |
| --- | --- | --- |
| android\_id | Device Android\_id - requer suporte da ad network | `{android_id}` |
| sha1\_android\_id | Device Android\_id anonimizado com SHA1 - requer suporte da ad network |  |
| advertising\_id | Google Advertising ID – requer suporte da ad network | `{ga_id}` |
| sha1\_publicidade\_id | Google Advertising ID anonimizado com SHA1 - requer suporte da ad network |  |
| af\_r | Somente para fora da loja - URL de redirecionamento de destino |  |
| sha1\_el | Usado para atribuição de desktop para mobile - e-mail com hash SHA1, requer suporte da ad network |  |

**Macros específicas do iOS**

| **Nome da macro** | **A descrição** | **Offerslook** |
| --- | --- | --- |
| idfa | ID de anunciante da Apple — deve ser fornecido em letras maiúsculas; requer suporte da ad network | `{idfa}` |
| sha1\_idfa | ID de anunciante da Apple com hash SHA1 — requer suporte da ad network |  |
| mac | Endereço mac do dispositivo - Requer suporte da ad network | `{mac}` |
| sha1\_mac | Endereço MAC do dispositivo com hash SHA1 — requer suporte da ad network |  |

<div id="creating-your-install-postbacks" />

## Criando seus postbacks de instalação

A seguir, veja uma explicação passo a passo de como criar seus postbacks de instalação usando a plataforma Offerslook:

1. Crie ou selecione uma oferta que use o protocolo postback com ID de transação
2. Na seção de detalhes da página da oferta, clique no link "rastreamento"
3. Copie a URL de postback exibida no campo identificado como postback URL
4. Remova o parâmetro offer\_id e o valor dele da URL de postback para transformar o postback de um postback específico em um postback global

Postback de instalação global:

`http://{networkname}.offerstrack.net/advBack.php?click_id={click_id}&adv_id={adv_id}`

`networkname` é o nome de domínio fornecido pela Offerslook.

**Finalizando seu cadastro**

* Se você tiver uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor>.
* Se você não tiver uma integração com a AppsFlyer, preencha a solicitação de cadastro de parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

<div data-zendesk-anchors="creating-your-attribution-link=como-criar-seu-link-de-atribui%C3%A7%C3%A3o 01JFT1JFND230EFDBRTWNKXKSH=como-criar-seu-link-de-atribui%C3%A7%C3%A3o new-macros=novas-macros 01JFT1JFP8T3HF5GQBR19YHQW5=novas-macros creating-your-install-postbacks=criando-seus-postbacks-de-instala%C3%A7%C3%A3o 01JFT1JFP9BMZM99TKDR58FNZP=criando-seus-postbacks-de-instala%C3%A7%C3%A3o" />
