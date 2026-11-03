---
title: Especificação de link de atribuição para ad networks
metadata:
  keywords:
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
  created_at: '2021-12-06T10:31:00Z'
  edited_at: '2026-08-18T00:39:01Z'
  id: 4412938154513
  locale: pt
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/pt/articles/4412938154513
---
> **Visão geral:** As ad networks integradas à AppsFlyer especificam seu link de atribuição de acordo com este artigo.

## Links de atribuição para ad networks.

Links de atribuição são usados ​​para notificar a AppsFlyer de que um usuário interagiu com um anúncio ao clicar nele. Ns sua forma mais simples, o link de atribuição é colocado atrás de um anúncio, pelo que quando um usuário clica num anúncio está clicando em um link de atribuição.

### Modelo de atribuição

O que acontece na jornada desde o primeiro clique ou impressão até a atribuição de uma instalação ou evento e muito mais.

[![appsflyer-modelo-de-atribuição-para-parceiros.png](https://files.readme.io/3f7536b15513a38dde0cdd82c889fc299a094a99339901cafcd6cd06c323b005-17990516210449.png)](https://files.readme.io/3f7536b15513a38dde0cdd82c889fc299a094a99339901cafcd6cd06c323b005-17990516210449.png)

1. Um usuário clica em um banner ou em um link de oferta.
2. O banner ou link redireciona o usuário para um link de atribuição da AppsFlyer. O link de atribuição da AppsFlyer é preenchido com informações coletadas durante o clique.
3. Coletamos as informações do link de atribuição e as armazenamos em nosso banco de dados.
4. Uma instalação ocorre e o aplicativo é aberto pela primeira vez. O SDK da AppsFlyer dentro do aplicativo chama nossos servidores com as informações sobre o dispositivo no qual o aplicativo está instalado.
5. Nós combinamos esses dados com nosso banco de dados de cliques usando nossos **métodos de atribuição**:
   * **Correspondência de referenciador**  
     Este método de atribuição é exclusivo para dispositivos Android. Quando um usuário clica em um link e é redirecionado para o Google Play, o Google Play fornece um ID de referenciador exclusivo. Quando a instalação ocorre, coletamos esse ID do dispositivo. Em seguida, combinamos com os registros do Google Play.
   * **Correspondência de ID do dispositivo**  
     Fazemos a correspondência do ID do dispositivo (IDFA para iOS ou GAID para o dispositivo Android) coletado com o clique no ID do dispositivo que executa a instalação.
   * <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-attribution-model#probabilistic-modeling">**Modelagem probabilística**</Anchor>

   Mais sobre <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-attribution-model">métodos de atribuição</Anchor>.

   Procuramos o referenciador, o ID do dispositivo e os pontos de dados de modelagem probabilística (nessa ordem) em nosso banco de dados de cliques. Se encontrarmos uma correspondência, atribuiremos a instalação ao clique. Caso contrário, atribuímos a instalação a um download orgânico.
6. Depois que a instalação é atribuída, enviamos um postback com os detalhes da conversão para a ad network.

No decorrer desse fluxo, usamos links de atribuição para obter informações fornecidas por você, e retornamos essas informações por meio de postbacks enviados para você.

> 📘 **Observação**
>
> Se você usa ferramentas de marketing de desempenho externas, como TUNE, CAKE ou Affise, consulte <Anchor target="_blank" href="/partners/pt/docs/platforms-for-ad-networks">as instruções específicas da plataforma</Anchor>.

### Template de link de atribuição

O link de atribuição (o link por trás do banner/oferta) pode ser o seguinte:

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={clickid}&advertising_id={gaid}&af_siteid={affiliate_id}&af_cost_model=CPI&af_cost_value={cost_value}&af_cost_currency={currency}&c={Campaign}&af_ad_type={AdType}&af_adset={Adset}&af_ad={Ad}&is_incentivized={true\false}&expires={timestamp}&signature={signature}
```

`https://app.appsflyer.com/` é o endpoint da AppsFlyer, `com.yourapp` é o ID do aplicativo, e `pid=mediaName_int` é um nome de fonte de mídia exclusivo que atribuímos à sua ad network.

Essa parte do link é estática e não exige nada de você.

Explicação da estrutura do link:

* Os valores após '=' dentro de `{} são macros preenchidos por você quando o clique ocorre e é enviado para a AppsFlyer. Ao preparar seu modelo, substitua o valor entre colchetes {}` pelos nomes dos parâmetros.
* A nomenclatura de macros não tem significado, desde que seu sistema as substitua pelos valores reais e corretos. Os parâmetros antes do sinal '=' são placeholders usados pela AppsFlyer, para que saibamos quais valores você está nos enviando.
* Para integração com a AppsFlyer, envie-nos o template do link de atribuição por e-mail com seus nomes de macro.

Considere os parâmetros listados na tabela a seguir como os mínimos recomendados. Oferecemos suporte a um conjunto maior de parâmetros. Você deve compartilhar conosco o máximo de informações coletadas sobre o clique. Veja a <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#parâmetros-do-link-de-atribuição">lista de parâmetros de link de atribuição</Anchor>.

#### Parâmetros mínimos recomendados de link de atribuição

| Parâmetro | Descrição |
| --- | --- |
| `&clickid={clickid}` | O ID de clique é um identificador de clique exclusivo para cada clique que acontece na sua ad network. |
| `&advertising_id={gaid}` ou  <br />`&idfa={IDFA}` | O ID do dispositivo no qual o clique ocorre (GAID para Android e IDFA para Apple). |
| `&c={campaign}` | O nome da campanha, como definido pelo anunciante. |
| `&af_siteid={publisher_id}` | ID do publisher, do afiliado do publisher ou do afiliado que impulsionou o clique. |
| `&af_ad_type={search_text}` | Tipo de anúncio. Você pode usar uma das seguintes convenções de nome:  <br />search\_text  <br />banner  <br />interstitial  <br />video  <br />rewarded\_video  <br />playable  <br />sponsored\_content  <br />audio |
| `&af_adset={adsetid}` | Nome do conjunto de anúncios - fornecido pelo anunciante/editor. Conjunto de anúncios é um nível intermediário na hierarquia entre Campanha e Anúncio. <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#níveis-de-granularidade-de-dados">Ver mais</Anchor> |
| `&af_ad={ad_id}` | Nome do anúncio (<Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#níveis-de-granularidade-de-dados">ver mais</Anchor>) - fornecido pelo anunciante/editor |
| `&is_incentivized={true}` | Campanhas incentivadas ou não incentivadas (pode ser verdadeiro/falso) |
| `&af_cost_value={cost_value}` | Valor de custo de conversão - aceita até 4 dígitos após o ponto decimal.  <br />Certifique-se de usar SOMENTE valores numéricos (use o ponto decimal se necessário), por exemplo, "56", "2,85" etc. |
| `&af_cost_currency={currency}` | Moeda de custo — código da moeda (por exemplo, USD, EUR). O valor padrão é USD.  <br /><Anchor target="_blank" href="https://en.wikipedia.org/wiki/ISO_4217">Lista de códigos de moeda</Anchor>. |
| `&expires={timestamp}` | Carimbo de data/hora Unix após o qual a ad network não reivindica o clique. Usado para assinatura de cliques para evitar fraudes de cliques. <Anchor target="_blank" href="/partners/pt/docs/click-signing-for-ad-networks">Saiba mais</Anchor> |
| `&signature={signature}` | Assinatura HMAC-SHA256 usada para validar o clique e evitar fraudes. <Anchor target="_blank" href="/partners/pt/docs/click-signing-for-ad-networks">Saiba mais</Anchor> |

<div data-zendesk-anchors="attribution-links-for-ad-networks=links-de-atribui%C3%A7%C3%A3o-para-ad-networks 01H8GPNM9XTR602BWRBQ5JV8DT=links-de-atribui%C3%A7%C3%A3o-para-ad-networks attribution-model=modelo-de-atribui%C3%A7%C3%A3o 01H8GPNM9XSKS66F02GZQKK8E8=modelo-de-atribui%C3%A7%C3%A3o 01H8GPNM9XBCVVXZ5HFKQZQ79D=observa%C3%A7%C3%A3o attribution-link-template=template-de-link-de-atribui%C3%A7%C3%A3o 01H8GPNM9XS4JE8B1F6TJGKSBR=template-de-link-de-atribui%C3%A7%C3%A3o recommended-minimum-attribution-link-parameters=par%C3%A2metros-m%C3%ADnimos-recomendados-de-link-de-atribui%C3%A7%C3%A3o 01H8GPNM9XD0GASJ93PNDGMDE8=par%C3%A2metros-m%C3%ADnimos-recomendados-de-link-de-atribui%C3%A7%C3%A3o" />
