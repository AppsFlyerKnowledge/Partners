---
title: Integração do Everflow com a AppsFlyer
metadata:
  keywords:
    - everflow
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
  created_at: '2017-11-21T07:36:24Z'
  edited_at: '2026-08-18T00:41:00Z'
  id: 115005709185
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/115005709185
---
> **Em resumo:** o Everflow é um parceiro integrado da AppsFlyer. A AppsFlyer envia dados de atribuição ao Everflow para instalações e eventos in-app.

## Iniciar a integração com a AppsFlyer

**Para iniciar a integração com a AppsFlyer:**

1. Preencha o <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">**Formulário de Informações para Cadastro de Parceiro**</Anchor>.
2. Depois de enviar o formulário de cadastro acima, você receberá um e-mail de um gerente de desenvolvimento de parceiros em até 24 horas.
3. Responda a esse e-mail com o nome do cliente da AppsFlyer que você está integrando. Envie-nos as seguintes informações usando o widget do assistente de parceiro:
   * Nome da sua empresa
   * Logo transparente
   * O template de link de atribuição recomendado do Everflow (use o template a seguir.)
   * O valor de *pid* precisa ser definido como o nome que você escolheu e aparecerá nos relatórios da AppsFlyer.
   * Quaisquer valores adicionais que você queira usar.
   * Seu ID de network do Everflow (nid) e domínio de postback para as configurações de postbacks de instalação e de evento in-app

### Template de URL de atribuição

```http
https://app.appsflyer.com/{app_id}?pid=mediaName_int&clickid={transaction_id}&af_siteid={affiliate_id}
&af_sub_siteid={affiliate_source_id}&idfa={idfa}&sha1_idfa={idfa_sha1}&advertising_id={google_aid}
&af_cost_value={amount}&af_cost_currency={offer_currency}&af_cost_model=CPI
```

Se você já tem uma integração com a AppsFlyer, entre em contato conosco usando o widget do assistente de parceiro

 e inclua o novo postback do Everflow e o template de link de atribuição.

## Criando seu link de atribuição

O link de atribuição consiste no link de atribuição base da AppsFlyer e em macros adicionais adicionadas pela network de anúncios, conforme detalhado aqui. 

Veja abaixo o link de atribuição base da AppsFlyer com uma explicação detalhada de cada macro:

| URL Base da AppsFlyer | Descrição |
| --- | --- |
| `https://app.appsflyer.com/{app_id}?` | Endpoint da AppsFlyer<br /><br />app\_id= ID exclusivo do Aplicativo — representa o ID do Aplicativo que está sendo promovido |
| pid= | Nome do canal de mídia concatenado com \_int para identificar networks integradas. Exemplo: midiaName\_int |
| c= | Campaign name |

Veja abaixo um link de atribuição completo após adicionar as macros adicionais do Everflow:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={transaction_id}&af_siteid={affiliate_id}
&af_sub_siteid={affiliate_source_id}&idfa={idfa}&sha1_idfa={idfa_sha1}&advertising_id={google_aid}
&af_cost_value={amount}&af_cost_currency={offer_currency}&af_cost_model=CPI
```

> 📘 **Nota**
>
> * Para modelos de custo de campanha diferentes de CPI, atualize o **&af\_cost\_model=** parâmetro para o modelo apropriado. Exemplo:  CPA, CPC
> * Se você já é parceiro da AppsFlyer e está migrando para a Everflow a partir de uma plataforma diferente, adicione `&af_additional_postback=1` aos seus links de atribuição.

Para ver a lista completa de parâmetros da AppsFlyer, clique <Anchor target="_blank" href="/partners/pt/docs/postback-macros-for-ad-networks">aqui</Anchor>.

Para ver a lista completa de macros da Everflow, clique <Anchor target="_blank" href="https://help.everflow.io/support/solutions/articles/22000176119-parameters-and-macros">aqui</Anchor>.

## Integração dos seus postbacks de instalação e de eventos in-app

> 📘 **Nota**
>
> * Veja abaixo uma explicação de como formatar postbacks de instalação e de eventos in-app para a plataforma Everflow.
> * Você deve enviar à AppsFlyer seu domínio personalizado da Everflow no lugar de  [everflow\_domain\_placeholder] nos postbacks abaixo.
> * NID é o ID da network fornecido pela Everflow.

## Postback de instalação global

```http
https://[everflow_domain_placeholder]/?nid=[everflow_network_placeholder]&transaction_id=$$click(clickid)
```

## Postback global de evento in-app

```http
https://[everflow_domain_placeholder]/?event_id=[everflow_eventid_placeholder]&nid=[everflow_network_placeholder]&transaction_id=$$click(clickid)
```

**Event\_ID**

O ID exclusivo do evento in-app gerado pela Everflow para cada evento da oferta.

**Event\_ID= Definido como Event Tag no dashboard da AppsFlyer para cada aplicativo pelo anunciante**

Este é o nome real do evento in-app do aplicativo.

Para detalhes sobre o Dynamic Event Mapping para eventos in-app, clique <Anchor target="_blank" href="/partners/pt/docs/dynamic-event-mapping-for-in-app-events">aqui</Anchor>

## Configuração de eventos no Everflow

**Para configurar um evento no Everflow, siga as etapas abaixo**:

1. Para configurar os eventos no nível da oferta, use o guia <Anchor target="_blank" href="https://help.everflow.io/support/solutions/articles/22000176131-add-post-conversion-events-">aqui</Anchor>.
2. Depois de configurar os eventos, lembre-se de qual ID de evento corresponde a cada um. No exemplo abaixo, o ID do evento 275 é para Purchase e o ID do evento 276 é para Registration
3. Adicione estes eventos ao link de atribuição da AppsFlyer.  
   Você deve ter um ID de evento para cada valor de "&goalid\_x".  
   Substitua o "x" por um número de goalid diferente. Neste exemplo, usamos &goalid\_1=275 e &goalid\_2=276
4. Adicione-os ao link de atribuição da AppsFlyer na página **Geral** depois de editar a oferta. [![](https://files.readme.io/2c8e34fb91800fefac0da3c9285579833cdb17366234529001683ae008fba851-360002535645.png)](https://files.readme.io/2c8e34fb91800fefac0da3c9285579833cdb17366234529001683ae008fba851-360002535645.png)
5. Adicione &goalid\_1=275&goalid\_2=276 ao link de atribuição da AppsFlyer e clique em salvar.  
   Ao concluir, deve ficar assim (os IDs de evento podem ser diferentes): [![](https://files.readme.io/9c62bc03423febe5e990bb230c5a5c3023dba723b7c8877ead5d3328a24ee3bb-360002539489.png)](https://files.readme.io/9c62bc03423febe5e990bb230c5a5c3023dba723b7c8877ead5d3328a24ee3bb-360002539489.png)
6. Peça ao anunciante para mapear esses eventos na AppsFlyer. Para mais detalhes sobre o mapeamento dinâmico de eventos para eventos in-app.
7. Extraia o postback de evento da Everflow e envie-o para a AppsFlyer. Certifique-se de que você está mapeando as macros de goalid corretas para os eventos correspondentes do lado do anunciante.

<div data-zendesk-anchors="initiating-the-integration-with-appsflyer=iniciar-a-integra%C3%A7%C3%A3o-com-a-appsflyer h_01KPJWT3XQ0WZRT7PD6GVRR6SH=iniciar-a-integra%C3%A7%C3%A3o-com-a-appsflyer attribution-url-template=template-de-url-de-atribui%C3%A7%C3%A3o h_01KPJWT3XQZKMBEP7S20TNT82Q=template-de-url-de-atribui%C3%A7%C3%A3o creating-your-attribution-link=criando-seu-link-de-atribui%C3%A7%C3%A3o h_01KPJWT3XQ4M7Z0G1EDD2BNGXP=criando-seu-link-de-atribui%C3%A7%C3%A3o h_01KPJWT3XQEX5TFPKBW14CZPQ3=nota integrating-your-install-and-inapp-event-postbacks=integra%C3%A7%C3%A3o-dos-seus-postbacks-de-instala%C3%A7%C3%A3o-e-de-eventos-in-app h_01KPJWT3XQ86V1D429YC6FSP2Z=integra%C3%A7%C3%A3o-dos-seus-postbacks-de-instala%C3%A7%C3%A3o-e-de-eventos-in-app h_01KPJWT3XQ8E01ZJAZPXSFH55P=nota-1 global-install-postback=postback-de-instala%C3%A7%C3%A3o-global h_01KPJWT3XQW3TKNPR7Z6K2NCQZ=postback-de-instala%C3%A7%C3%A3o-global global-inapp-event-postback=postback-global-de-evento-in-app h_01KPJWT3XQCM2BWTJVDXSVSBQP=postback-global-de-evento-in-app event-setup-in-everflow=configura%C3%A7%C3%A3o-de-eventos-no-everflow h_01KPJWT3XQ9K4WPVCSGGGC4Z6S=configura%C3%A7%C3%A3o-de-eventos-no-everflow" />
