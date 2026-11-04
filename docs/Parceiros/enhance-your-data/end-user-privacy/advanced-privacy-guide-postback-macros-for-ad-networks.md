---
title: Guia de Privacidade Avançada e macros de postback para ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - ios14
    - SKAD
    - Advanced Privacy
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-07-27T07:09:37Z'
  edited_at: '2026-08-19T00:37:15Z'
  id: 360011316197
  locale: pt
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/pt/articles/360011316197
---
> **Visão geral:** compartilhamento de dados com parceiros quando a Privacidade Avançada está habilitada. Instruções para ad networks sobre a configuração de postbacks de Privacidade Avançada. Atenção! Este artigo não está relacionado aos postbacks de SKAdNetwork nem se destina a anunciantes.

<div id="advanced-privacy-for-ad-networks-news" />

> 📄 **Novidades da Privacidade Avançada para ad networks**
>
> O mecanismo de postback de Privacidade Avançada descrito neste artigo funciona quando todos os itens a seguir são verdadeiros:
>
> * O dispositivo do usuário está executando o iOS 14.5+
> * A Privacidade Avançada está ativada

![AdvancedPrivacy.png](https://files.readme.io/2a80740637c1003e03bc169df274bf0fa6240ee850c7fd6e967c4abea234e0d1-360018213598.png)

Este artigo discute:

* O impacto do compartilhamento de dados da Privacidade Avançada sobre os parceiros
* Requisitos de [clique em URL](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#click-url-requirements) para ser elegível para atribuição
* Configurando seus [postbacks](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification) de Privacidade Avançada no dashboard da AppsFlyer
* A diferença entre [Privacidade Avançada e SKAdNetwork.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#ap-vs-skadnetwork)

<div id="ad-network-advanced-privacy-data-sharing-principles" />

## Princípios de compartilhamento de dados de Privacidade Avançada da ad network

A partir do iOS 14.5+, a AAP (<Anchor target="_blank" href="/marketers/pt/docs/apply-aggregated-advanced-privacy-framework">framework de Privacidade Avançada Agregada - Aggregated Advanced Privacy</Anchor>) da AppsFlyer oferece aos anunciantes a capacidade de controlar a disponibilidade dos dados de atribuição a nível do usuário fornecidos pela plataforma da AppsFlyer.

No contexto das ad networks, o framework de AAP é implementada usando a Privacidade Avançada (AP). Para facilitar a compreensão, os termos Privacidade Avançada e AP são usados de forma intercambiável neste artigo.

A AP (Privacidade Avançada) não afeta a disponibilidade de dados agregados disponíveis para parceiros ou ad networks.

**Quais dados são afetados pela AP**

Quando o AP está ativado, os dados que os clientes podem disponibilizar por meio de postbacks ou outros métodos de relatório são agregados apenas. Os dados em nível de usuário, incluindo relatórios relacionados à fraude do Protect360, não são incluídos.

No contexto de postbacks, isso significa que diferentes tipos de postbacks são usados, dependendo do status de consentimento à ATT do usuário e de outros fatores.

Você pode visualizar a configuração atual da AP, por aplicativo, no dashboard da AppsFlyer. Vá para **Configuração** > **Integrações ativas** > selecione sua ad network > **aba Integração.** A configuração padrão está ativada.

![APforPartners2.png](https://files.readme.io/e4fb5617a47635f24dc83881c2be3d18b770200a576cb67bd3312e6fc2c123e1-360018154777.png)

<div id="types-of-templates-for-sending-postbacks" />

#### Tipos de templates para envio de postbacks

* **Template comum:** seu template de integração existente com a AppsFlyer com identificador de usuário e macros de dados de atribuição. Este template é usado para enviar postbacks contendo dados de atribuição no nível do usuário.
* **Template de privacidade avançada**: um template sem macros de identificador de usuário. Este template é usado para enviar postbacks contendo dados de atribuição agregados.   
  **Observação:** se um postback AP for necessário e você não tiver concluído a integração AP, nenhum postback será enviado. Você pode configurar a integração de AP usando nossa ferramenta autônoma de [Gerenciamento de postbacks](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback).

<div id="note" />

> 📘 **Observação**
>
> * Se um usuário der o consentimento da ATT nos aplicativos do anunciante e do editor ("consentimento duplo"), postbacks regulares serão enviados para as ad networks atribuídas e não atribuídas.
> * **Exceção:** para instalações atribuídas a Apple Search Ads (ASA), o ASA envia postbacks de instalação para a ad network mesmo quando a Privacidade avançada está ativada para o anunciante nas seguintes condições:
>   * o usuário não deu consentimento
>   * postback de instalação na ad network foi definido como **Todas as fontes de mídia, incluindo orgânica**
>   * a ad network não oferece suporte à Privacidade Avançada

<div id="type-of-postback-used" />

### Tipo de postback usado

A tabela a seguir descreve os tipos de postback com base na disponibilidade do ID do Anunciante e no status da Privacidade Avançada.

<div id="postback-type-for-ios-145" />

#### Tipo de postback para iOS 14.5+

<table><thead><tr><th rowspan="2">Status da AP</th><th colspan="2">Status da ATT</th><th rowspan="2">Tipo de template de postbacks para parceiro atribuído\*, que é compatível com a AP </th><th rowspan="2">Tipo de template de postback para o parceiro atribuído\* não compatível com a AP </th><th rowspan="2">Parceiro de postback não atribuído\*</th></tr><tr><th>Aplicativo do publisher</th><th>Aplicativo do anunciante</th></tr></thead><tbody><tr><td>Ativado</td><td>Disponível.</td><td>Não autorizado</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Modelo AP</a> (dados agregados)</td><td>Sem postback</td><td>Nenhum</td></tr><tr><td>Ativado</td><td>Não autorizado</td><td>Disponível.</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Modelo AP</a> (dados agregados)</td><td>Sem postback</td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Autorizado</a></p><p><a href="/marketers/pt/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">Os campos de atribuição</a> não estão disponíveis.\*</p></td></tr><tr><td>Ativado</td><td>Disponível.</td><td>Disponível.</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Template comum</a>. Isso inclui IDs disponíveis como: IDFA, IDFV, CUID, ID de clique e campos de atribuição. </td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Template comum</a>. Isso inclui IDs disponíveis como: IDFA, IDFV, CUID, ID de clique e campos de atribuição. </td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Template comum</a> incluindo IDs disponíveis. <span><a href="/marketers/pt/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">Os campos de atribuição</a> não estão disponíveis.\*</span> </td></tr><tr><td>Ativado</td><td>Não autorizado</td><td>Não autorizado</td><td> <a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipo-de-postback-usado"><span>Modelo AP</span></a> (dados agregados)</td><td>Sem postback</td><td>Nenhum</td></tr><tr><td>Desligado</td><td>Não considerado</td><td>Não considerado</td><td><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Template comum</a></td><td><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Template comum</a></td><td><p><a href="./advanced-privacy-guide-postback-macros-for-ad-networks#tipos-de-templates-para-envio-de-postbacks">Template comum</a>.</p><p><a href="/marketers/pt/docs/about-raw-data-identifier-restrictions#unavailable-attribution-fields" target="_blank">Os campos de atribuição</a> não estão disponíveis.\*</p></td></tr></tbody></table>

**(\*) Princípios para compartilhamento de dados com parceiros**

Para qualquer evento, vários parceiros da ad network podem ter direito a um postback. Os postbacks enviados são os seguintes:

* Parceiro atribuído: ad network creditada pelo evento
* Parceiro não atribuído: parceiro integrado não creditado pelo evento, quando a opção **Envio** **de postback de eventos in-app** está definida como **Todas as fontes de mídia, incluindo orgânicas.** Se o aplicativo do anunciante tiver o consentimento à ATT, o postback conterá IDs de usuário sem dados atribuídos. (Essa opção não é compatível com todas as ad networks.)

  ![InAppEventAll.png](https://files.readme.io/e24037f75b2b82797031eb13d5e063b8c2006812491e69674ff066ac830919f7-35847850644881.png)

<div id="web-campaigns" />

### Campanhas na web

A AP se comporta de maneira diferente quando a ad network exibe um anúncio na web.

Para indicar se um clique veio da web ou de um aplicativo, você deve enviar o parâmetro `af_media_type=web` ou `af_media_type=app` na URL de clique.

Se você não enviar `af_media_type`, o padrão é `app`.

<div id="postback-type-used-for-ios-145-when-ap-is-on" />

#### Tipo de postback usado para iOS 14.5+ quando a AP está ativada

<table><thead><tr><th colspan="2">Status da ATT</th><th rowspan="2">Tipo de postback para parceiro atribuído\*</th><th rowspan="2">Tipo de postback para parceiro não atribuído\*</th></tr><tr><th>Aplicativo do publisher</th><th>Aplicativo de anunciante</th></tr></thead><tbody><tr><td>N/D</td><td>Não autorizado</td><td>Privacidade avançada</td><td>Nenhum</td></tr><tr><td>N/D</td><td>Autorizado</td><td>Comum. Nível do usuário com os seguintes IDs: IDFA, IDFV, CUID, Click ID.</td><td>Comum. Somente IDs a nível do usuário.</td></tr></tbody></table>

<div id="integration" />

## integração

Atualize suas URLs de cliques e conclua a integração com a Privacidade Avançada.

<div id="click-url-requirements" />

<Accordion title="Requisitos da URL de clique">

Em muitos casos, dependendo do consentimento do usuário à ATT, o IDFA não estará disponível no aplicativo do editor, no aplicativo do anunciante ou em nenhum dos dois. Nesses casos, a AppsFlyer pode realizar a atribuição usando a <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-attribution-model#aggregated-advanced-privacy-aap">Privacidade Avançada Agregada</Anchor> e a <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-attribution-model#probabilistic-modeling">modelagem probabilística.</Anchor>

**[Prática recomendada]** Para maximizar suas atribuições, envie todos os parâmetros listados.

1. Anexe os seguintes parâmetros para URLs de clique:

<table><thead><tr><th>Identificador</th><th>Parâmetro de clique</th><th>Exemplo</th></tr></thead><tbody><tr><td>Campanha</td><td>C</td><td>US_20_30</td></tr><tr><td>ID da campanha</td><td>af_c_id</td><td>12345</td></tr><tr><td>Conjunto de anúncios</td><td>af_adset</td><td>ADSET_1</td></tr><tr><td>ID do conjunto de anúncios</td><td>af_adset_id</td><td>56789</td></tr><tr><td>As ad </td><td>af_ad</td><td>creative_name</td></tr><tr><td>ID do anúncio</td><td>af_ad_id</td><td>34567</td></tr><tr><td>ID do site</td><td>af_siteid</td><td>abcdefgh12345678</td></tr><tr><td>ID do subsite</td><td>af_sub_siteid</td><td>abcdefgh12345678</td></tr><tr><td>Canal</td><td>af_canal</td><td>channel_name</td></tr><tr><td>Tipo de anúncio</td><td>af_ad_type</td><td>Vídeo</td></tr><tr><td>Modelo do dispositivo iOS\*</td><td>af_model</td><td><p>O modelo do dispositivo. Valores permitidos:</p><ul><li>iphone (tudo em letra minúscula)</li><li>ipad (tudo em letra minúscula)</li></ul></td></tr><tr><td>Sistema operacional\*</td><td>af_os</td><td>A versão do sistema operacional</td></tr><tr><td colspan="3">\* Algumas informações também podem ser fornecidas por meio do agente do usuário. Nesse caso, o valor enviado usando o identificador específico prevalece.</td></tr></tbody></table>

   Anexar detalhes da campanha à URL de cliques

   O exemplo a seguir mostra como adicionar os detalhes da campanha à URL de clique:

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adsetname}&af_adset_id={adset ID}&af_ad={adname}&af_ad_id={ad ID}&af_ad_type={Adtype}&af_siteid={PublisherId}` |
| --- |

2. Adicione os seguintes parâmetros obrigatórios para clicar em URLs*:

   <div id="caution" />

   > ❗️ **Atenção**
   >
   > Se a sua URL de clique não passar nos parâmetros obrigatórios, você não será creditado pela maioria das instalações impulsionadas por você.


   * IP
   * Agente de usuário

   * Nenhuma ação é necessária ao enviar um clique usando um referenciador HTTP simples que redireciona para a AppsFlyer. 

   Use o método de extração descrito para anexar os parâmetros à URL de clique ao usar um dos seguintes métodos:

   * Redirecionar via in-app
   * Cliques de servidor para servidor (também conhecido como S2S)

   <div id="parameters-for-advanced-privacy-attribution" />

   #### Parâmetros para atribuição de privacidade avançada

   <Table>
     <thead>
       <tr>
         <th>
           Parâmetro
         </th>
         <th>
           Obrigatório
         </th>
         <th>
           Método de extração
         </th>
       </tr>
     </thead>

     <tbody>
       <tr>
         <td>
           **Idioma e localização do dispositivo**

           af\_lang
         </td>
         <td>
           Não
         </td>
         <td>
           NSString *language = [[NSLocale preferredLanguages] objectAtIndex:0];

           [Recomendado] Forneça o idioma e a localização; por exemplo, en-US.
         </td>
       </tr>
       <tr>
         <td>
           **Agente de usuário**

           af\_ua
         </td>
         <td>
           Sim
         </td>
         <td>
           Extraia o user-agent (agente do usuário) com o formato:

           ```
           Mozilla%2F5.0+%28iPhone%3B+CPU+iPhone+OS+13_3_1  
           +like+Mac+OS+X%29 AppleWebKit%2F605.1.15+%28KHTML%2C  
           +like+Gecko%29+Mobile%2F15E148
           ```

           * **Não** extraia o  *user-agent* do CFNetwork, extraia o outro.
           * O user-agent deve ser codificado por URL
         </td>
       </tr>
       <tr>
         <td>
           **Endereço de IP do dispositivo**

           af\_ip
         </td>
         <td>
           Sim
         </td>
         <td>
           Melhor opção: se disponível, forneça o IP do dispositivo sob o parâmetro af\_ip.

           Próxima opção: se disponível, a AppsFlyer usará o IP no X-Forwarded-For.
         </td>
       </tr>
     </tbody>
   </Table>

   Anexar parâmetros à URL de clique

   Para passar esses parâmetros obrigatórios no link de atribuição de cliques, use essa referência:

| `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset name}&af_adset_id={adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad-type}&af_siteid={PublisherId}&af_ua={USER-AGENT}&af_lang={LANGUAGE}&af_ip={IP}` |
| --- |

   **Parâmetro**

| GET `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset` name\}&af\_adset\_id=`{adset ID}&af_ad={ad name}&af_ad_id={ad ID}&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />&af\_ua=Mozilla%2F5.0%20%28iPhone%3B%20CPU%20iPhone%20OS%2012\_1\_4%20  <br />like%20Mac%20OS%20X%29%20AppleWebKit%<br /><br />`2F605.1.15%20%28KHTML%2C%20like%20Gecko%29%20Mobile%2F16D57&af_lang=en-US&af_ip=11.11.1.11` |
| --- |

   * Os parâmetros de consulta devem ser codificados por URL.

   **Transferir dados em cabeçalhos de URL de cliques**

   Para transferir os campos no cabeçalho da URL de clique, use esta referência:

| GET `https://app.appsflyer.com/id123456789?pid=YOUR_NETWORK_ID&c={CampaignName}&af_c_id={CampaignID}&af_adset={adset` name\}&af\_adset\_id=`{adset ID}&af_ad={ad name}&af_ad_id={ad ID}  <br />&af_ad_type={Ad type}&af_siteid={PublisherId}`<br /><br />`accept-language: en-US,en;q=0.`<br /><br />`User-agent: Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 como Mac OS X)`<br /><br />`AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148`<br /><br />`X-Forwarded-For: 11.11.1.11, 222.222.2.222` |
| --- |

</Accordion>

<div id="advanced-privacy-postback-specification" />

<Accordion title="Especificação do postback de Privacidade Avançada">

Para receber postbacks de Privacidade Avançada, você deve configurar uma integração de Privacidade Avançada além da integração normal de postback. Você mesmo pode configurar o [postback de Privacidade Avançada](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback) no dashboard da AppsFlyer.

**Diferenças entre o template comum e o template da Privacidade Avançada**

* O tempo do postback não está relacionado aos tempos reais do evento.
* Macros de carimbo de data/hora:
  * Para instalações e eventos in-app, os carimbos de data/hora são arredondados e se aproximam da hora em que ocorreram. Por exemplo, 22:55:30 é reportado como 22:00:00.
  * São reportados usando o fuso horário UTC. Exemplo de carimbo de data/hora: (2020-07-20 20:00:00)
* Os seguintes parâmetros não estão disponíveis nos postbacks de Privacidade Avançada: Click ID, Customer User ID, AppsFlyer ID, IDFA, IDFV, modelo do dispositivo, versão do sistema operacional e operadora.

**Ação exigida pela ad network para a integração:**

1. [Configure seu postback de Privacidade Avançada no dashboard da AppsFlyer.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#setting-up-your-advanced-privacy-postback)
2. <Anchor target="_blank" href="/partners/pt/docs/ios-integration-testing-for-ad-networks">Teste a integração da Privacidade Avançada</Anchor>

<div id="important" />

> 🚧 **Importante!**
>
> * Para distinguir entre postbacks de eventos legítimos e postbacks rejeitados, é necessário configurar os postbacks das macros rejeitadas.
> * Para habilitar a rejeição de parcelas/postbacks de eventos, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor>.

<div id="advanced-privacy-postback-endpoint-complete-as-required" />

#### Endpoint do postback de Privacidade avançada [complete conforme necessário]

| Tipo de postback |
| --- |
| Instalação |
| in-app |

<div id="advanced-privacy-attribution-macros-available" />

#### Macros de atribuição de Privacidade Avançada disponíveis

<table><thead><tr><th>Macro do postback (nome)</th><th>Observações</th><th>Parâmetros básicos para todos os postbacks</th><th>Parâmetros opcionais para eventos in-app </th><th>Parâmetros opcionais para atribuição rejeitada</th></tr></thead><tbody><tr><td>af_ad</td><td>Nome do criativo</td><td>Sim</td><td> </td><td> </td></tr><tr><td>af_ad_id</td><td>34567</td><td>Sim</td><td> </td><td> </td></tr><tr><td>af_ad_type</td><td>Como: banner, footer, vídeo</td><td>Sim</td><td> </td><td> </td></tr><tr><td>af_adset</td><td>ADSET_1</td><td>Sim</td><td> </td><td> </td></tr><tr><td>af_adset_id</td><td>56789</td><td>Sim</td><td> </td><td> </td></tr><tr><td>ativado</td><td>-</td><td>Sim</td><td> </td><td> </td></tr><tr><td>ativado</td><td>-</td><td>Sim</td><td> </td><td> </td></tr><tr><td>attributed_touch_hour</td><td><p>Arredondado para baixo, para a hora mais próxima. </p><p>Formato, veja nota (1)</p></td><td>Sim</td><td> </td><td> </td></tr><tr><td>tipo_de_toque_atribuído</td><td>Como: clique, impressão</td><td>Sim</td><td> </td><td> </td></tr><tr><td>blocked_reason</td><td>Relaciona-se a regras de validação/Protect360</td><td> </td><td> </td><td>Sim</td></tr><tr><td>blocked_reason_value</td><td>Relaciona-se a regras de validação/Protect360</td><td> </td><td> </td><td>Sim</td></tr><tr><td>blocked_sub_reason</td><td>Relaciona-se a regras de validação/Protect360</td><td> </td><td> </td><td>Sim</td></tr><tr><td>bundle_id</td><td>Conforme definido pelo anunciante</td><td>Sim</td><td> </td><td> </td></tr><tr><td>C</td><td>Nome da campanha, como US_20_30</td><td>Sim</td><td> </td><td> </td></tr><tr><td>af_c_id</td><td>ID da campanha, como 12345</td><td>Sim</td><td> </td><td> </td></tr><tr><td>af_canal</td><td>Nome do canal</td><td>Sim</td><td> </td><td> </td></tr><tr><td>código_país</td><td>Código ISO do país registrado na conversão</td><td>Sim</td><td> </td><td> </td></tr><tr><td>event_hour</td><td><p>Arredondado para baixo, para a hora mais próxima. </p><p>Formato, veja nota (1)</p></td><td>Sim</td><td> </td><td> </td></tr><tr><td>nome_do_evento</td><td>Conforme reportado pelo aplicativo</td><td> </td><td>Sim</td><td> </td></tr><tr><td>event_revenue</td><td>Valor da receita na moeda do evento</td><td> </td><td>Sim</td><td> </td></tr><tr><td>event_revenue_<br/>currency</td><td>Código da moeda da receita</td><td> </td><td>Sim</td><td> </td></tr><tr><td>event_revenue_usd</td><td>Receita convertida em USD</td><td> </td><td>Sim</td><td> </td></tr><tr><td>ativado</td><td><p>Arredondado para baixo, para a hora mais próxima. </p><p>Formato: veja nota (1)</p></td><td>Sim</td><td> </td><td> </td></tr><tr><td>is_first</td><td>Verdadeiro se esta for a primeira vez que esse evento in-app foi acionado por um usuário final específico</td><td> </td><td>Sim</td><td> </td></tr><tr><td>is_primary</td><td><p>Use para desduplicar</p><p>Booleano: 0, 1</p></td><td> </td><td>Sim</td><td> </td></tr><tr><td>is_retargeting</td><td><p>Use para desduplicar </p><p>Formato: veja a nota (2)</p></td><td>Sim</td><td> </td><td> </td></tr><tr><td>is_reengagement</td><td>Formato: veja a nota (2)</td><td> </td><td>Sim</td><td> </td></tr><tr><td>is_reattribution</td><td><p>Use para desduplicar </p><p>Formato: veja a nota (2)</p></td><td>Sim</td><td> </td><td> </td></tr><tr><td>match_type</td><td>Como: id_matching, probabilístico</td><td>Sim</td><td> </td><td> </td></tr><tr><td>Receita associada ao SKU na moeda fornecida no campo <code>event_revenue_currency</code>.</td><td>Nome/ID do evento correspondente na plataforma da ad network</td><td> </td><td>Sim</td><td> </td></tr><tr><td>platforma</td><td>Como: iOS, Android</td><td>Sim</td><td> </td><td> </td></tr><tr><td>postback_id</td><td>ID de postback exclusivo</td><td>Sim</td><td> </td><td> </td></tr><tr><td>retargeting_<br/>conversion_type</td><td>Tais como: reengajamento, reatribuição</td><td>Sim</td><td> </td><td> </td></tr><tr><td>af_siteid</td><td>abcdefgh12345678</td><td>Sim</td><td> </td><td> </td></tr><tr><td>af_sub_siteid</td><td>abcdefgh12345678</td><td>Sim</td><td> </td><td> </td></tr><tr><td colspan="5"><p>Observações:</p><p>(1) Formatos de carimbo de data/hora disponíveis:</p><ul><li>[Padrão] String: AAAA-MM-DD HH:MM:SS</li><li>Marca temporal: carimbo de data/hora Unix de 10 dígitos </li></ul><p>(2) Formato booleano disponível</p><ul><li>[Padrão] Numérico: 0, 1 </li><li>String: <em>false</em>, <em>true</em> </li></ul></td></tr></tbody></table>

</Accordion>

<div id="setting-up-your-advanced-privacy-postback" />

<Accordion title="Configurando seu postback de Privacidade Avançada">

Configure seu postback de AP usando a opção de gerenciamento de postback no dashboard da AppsFlyer.

**Pré-requisitos**:

* Você deve ter uma integração ativa com a AppsFlyer para gerenciar seu postback de Privacidade Avançada. Entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget partner assistant</Anchor> para <Anchor target="_blank" href="/partners/pt/docs/getting-started-onboarding-guide-for-ad-networks">criar uma integração</Anchor>.
* ![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) O gerenciamento de postback é realizado pelo administrador da conta; os membros da equipe não têm acesso.

**Para configurar o postback:**

1. Clique no menu suspenso superior direito > **Gerenciamento de postback**.
2. Selecione o tipo de postback: **Privacidade Avançada.**
3. Ative o criador.

   ![postback-management-enter-endpoint_en-us.png](https://files.readme.io/4ea0ffc61d1ecdb11d3c745876c29a942fde4133b8ebb54a1426a73c1dc63b16-360018215218.png)
4. Insira o **endereço do endpoint**: a URL do endpoint para a qual a AppsFlyer envia postbacks. Insira as URLs relevantes para instalações e/ou eventos in-app.
5. Insira os parâmetros a serem incluídos nos postbacks:

   * **Nome do parâmetro:** nome da tela do parâmetro da AppsFlyer
   * **Seu parâmetro de recebimento**: o respectivo parâmetro de recebimento do seu lado
   * **Valor do parâmetro** (disponível para alguns parâmetros): escolha o formato do valor. Por exemplo, para valores booleanos, escolha se deseja recebê-los como "true"/"false" ou 1/0.
   * **Instalação**: marque a caixa para incluir o parâmetro no postback de instalação.
   * **Evento in-app**: marque a caixa para incluir o parâmetro no postback do evento in-app.

   ![postback-management-parameters_en-us.png](https://files.readme.io/818ef31df9c4e349ca26b5421a0ba0582ed5f7f9fae39f1d0e4ec3b7562f4192-360018213698.png)

   Lista completa de [macros de postback de Privacidade Avançada.](/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification)
6. **[Opcional]** Adicione parâmetros personalizados que não são fornecidos pela AppsFlyer:

   ![postback-management-custom-parameters_en-us.png](https://files.readme.io/6bca46e1d39c6822b0e041eb1dcbb1b2d40e42fa062c34877c8cbf0c2d2847d6-16589581250321.png)
7. Verifique a visualização final do template de postback para ter certeza de que tudo está correto.

   ![postback-management-template_en-us.png](https://files.readme.io/b5e41cad37859365c7818c4561620f8a78250c207d8326dae53ed9b522fe3716-360018213718.png)
8. Clique em **Salvar**. Observe que, quando você salva o postback, as alterações entram em vigor imediatamente.

No caso de problemas, entre em contato conosco usando o widget <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant</Anchor>.

</Accordion>

<div id="additional-information" />

## Informações adicionais

<div id="ap-for-analytics-partners" />

<Accordion title="AP para parceiros de análise">

Os postbacks são enviados aos parceiros de análise da seguinte forma:

* AP desativada: postback a nível do usuário sem restrição.
* AP ativado: o tipo de postback depende da fonte do usuário e da disponibilidade do ID do Anunciante, conforme detalhado na tabela a seguir.

<div id="analytics-partner-postback-type-according-to-att-status-and-user-source" />

#### Tipo de postback do parceiro de análise de acordo com o status da ATT e fonte do usuário

<table><thead><tr><th rowspan="2">Fonte do usuário</th><th colspan="2">Status da ATT</th><th rowspan="2">Tipo de postback para parceiro de análise</th></tr><tr><th>Aplicativo do publisher</th><th> Aplicativo do anunciante</th></tr></thead><tbody><tr><td rowspan="3"><p>Não orgânicas </p></td><td>Disponível.</td><td>Disponível.</td><td>Regular</td></tr><tr><td>Não autorizado</td><td>Disponível.</td><td>Nenhum</td></tr><tr><td>Qualquer valor</td><td>Não autorizado</td><td>Nenhum</td></tr><tr><td>Orgânico ou web</td><td>N/D</td><td>Disponível.</td><td>Regular</td></tr><tr><td>Orgânico ou web</td><td>N/D</td><td>Não autorizado</td><td>Nenhum</td></tr></tbody></table>

</Accordion>

<div id="ap-vs-skadnetwork" />

<Accordion title="AP vs. SKAdNetwork">

<Anchor target="_blank" href="/partners/pt/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> é uma tecnologia de atribuição fornecida pela Apple para dispositivos iOS. A Privacidade Avançada faz parte da estrutura de <Anchor target="_blank" href="/marketers/pt/docs/apply-aggregated-advanced-privacy-framework">Privacidade Avançada Agregada (AAP) da AppsFlyer</Anchor> e está relacionada à atribuição realizada pela AppsFlyer. A AAP oferece aos anunciantes a capacidade de controlar a disponibilidade de dados de atribuição a nível do usuário por meio da plataforma da AppsFlyer. Normalmente, as ad networks têm compatibilidade para a integração entre AP e SKAdNetwork.

</Accordion>

<div data-zendesk-anchors="h_01HJR7MWPM9XA4BXHDRD2K6D56=novidades-da-privacidade-avan%C3%A7ada-para-ad-networks ad-network-advanced-privacy-datasharing-principles=princ%C3%ADpios-de-compartilhamento-de-dados-de-privacidade-avan%C3%A7ada-da-ad-network h_01HJR7MWPNYNMKZ3R8C3BB5EVG=princ%C3%ADpios-de-compartilhamento-de-dados-de-privacidade-avan%C3%A7ada-da-ad-network types-of-templates-for-sending-postbacks=tipos-de-templates-para-envio-de-postbacks h_01HJR7MWPN92BDJRK734P6YXSK=tipos-de-templates-para-envio-de-postbacks h_01HJR7MWPN71TP0KWVVBHPC0H2=observa%C3%A7%C3%A3o type-of-postback-used=tipo-de-postback-usado h_01HJR7MWPNJEDNDT1ZY7P78HMG=tipo-de-postback-usado postback-type-for-ios-145=tipo-de-postback-para-ios-145 h_01HJR7MWPNESP8BDC4D6Y7SBFZ=tipo-de-postback-para-ios-145 web-campaigns=campanhas-na-web h_01HJR7MWPNXHHCSQ6BGCNRBHZK=campanhas-na-web postback-type-used-for-ios-145-when-ap-is-on=tipo-de-postback-usado-para-ios-145-quando-a-ap-est%C3%A1-ativada h_01HJR7MWPNQCCNGHQY5RQHQ6D1=tipo-de-postback-usado-para-ios-145-quando-a-ap-est%C3%A1-ativada integration=integra%C3%A7%C3%A3o h_01HJR7MWPP7YGRXJQR29F3ERHH=integra%C3%A7%C3%A3o h_01HJR7MWPPAXK18KER56E30G8R=click-url-requirements h_01HJR7MWPPRN8XYVSS7HX7NQB9=aten%C3%A7%C3%A3o parameters-for-advanced-privacy-attribution=par%C3%A2metros-para-atribui%C3%A7%C3%A3o-de-privacidade-avan%C3%A7ada h_01HJR7MWPPK2HET3XYW4WBFAZ1=par%C3%A2metros-para-atribui%C3%A7%C3%A3o-de-privacidade-avan%C3%A7ada h_01HJR7MWPQ60F4CESKRRMTQ7HX=advanced-privacy-postback-specification h_01HJR7MWPQ8K06A1YM4KV4RTN8=importante advanced-privacy-postback-endpoint-%5Bcomplete-as-required%5D=endpoint-do-postback-de-privacidade-avan%C3%A7ada-complete-conforme-necess%C3%A1rio h_01HJR7MWPQX9SXJZMBS6QR07WD=endpoint-do-postback-de-privacidade-avan%C3%A7ada-complete-conforme-necess%C3%A1rio advanced-privacy-attribution-macros-available=macros-de-atribui%C3%A7%C3%A3o-de-privacidade-avan%C3%A7ada-dispon%C3%ADveis h_01HJR7MWPQKH52XMD6H9TJ0SM3=macros-de-atribui%C3%A7%C3%A3o-de-privacidade-avan%C3%A7ada-dispon%C3%ADveis h_01HJR7MWPRC44K908A4EAPN9GV=setting-up-your-advanced-privacy-postback additional-information=informa%C3%A7%C3%B5es-adicionais h_01HJR7MWPRVFR6YN56Y0DGBAXH=informa%C3%A7%C3%B5es-adicionais h_01HJR7MWPR6ACNYVZHK7YPHQGP=ap-for-analytics-partners analytics-partner-postback-type-according-to-att-status-and-user-source=tipo-de-postback-do-parceiro-de-an%C3%A1lise-de-acordo-com-o-status-da-att-e-fonte-do-usu%C3%A1rio h_01HJR7MWPRZDJNSZNB981WB5Z1=tipo-de-postback-do-parceiro-de-an%C3%A1lise-de-acordo-com-o-status-da-att-e-fonte-do-usu%C3%A1rio h_01HJR7MWPR3YR7E9S49P9ZZ3CT=ap-vs-skadnetwork" />
