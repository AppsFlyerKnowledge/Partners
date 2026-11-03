---
title: Teste a integração da campanha do profissional de marketing com a ad network
metadata:
  keywords:
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
  created_at: '2021-12-08T04:41:04Z'
  edited_at: '2026-08-19T00:38:06Z'
  id: 4413093220113
  locale: pt
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/pt/articles/4413093220113
---
> **Resumo**: teste a integração com a ad network usando aplicativos do profissional de marketing.

## Pré-requisitos

Antes de começar a testar a integração do profissional de marketing com sua ad network, há alguns requisitos:

* Dispositivos na allowlist: você precisa pedir ao profissional de marketing que <Anchor target="_blank" href="/marketers/pt/docs/registering-test-devices">inclua na allowlist</Anchor> todos os dispositivos que você usa para teste
* O aplicativo deve incluir o SDK da AppsFlyer
* Se o aplicativo não estiver publicado no Google Play nem na App Store do iOS, você precisa pedir ao profissional de marketing que forneça o aplicativo
* Independentemente de o aplicativo estar publicado ou não, ele deve estar <Anchor target="_blank" href="/marketers/pt/docs/adding-an-app-to-appsflyer">na conta da AppsFlyer do profissional de marketing</Anchor>

## Getting Started

Abra o seu dashboard da AppsFlyer. Na tela **Busca de aplicativo**, insira o ID do aplicativo do profissional de marketing:

> 📄 **Exemplo**
>
> Android - **com.example.app**
>
> iOS - **id1234123412**

Quando o visto verde aparecer no campo de entrada, clique na seta azul. Ao clicar na seta, o dashboard do aplicativo será aberto.

[![partner-app-search.png](https://files.readme.io/9fb3454de2eb7ea1cc7015151d75a9ae0835a60134b244227bf4da7f614a2a37-21414453165457.png)](https://files.readme.io/9fb3454de2eb7ea1cc7015151d75a9ae0835a60134b244227bf4da7f614a2a37-21414453165457.png)

## Teste de aplicativos publicados

No dashboard da AppsFlyer do seu aplicativo, no menu lateral, selecione **Integrações ativas**. Escolha sua ad network e clique em **Link de atribuição**.

> 🚧 **Importante!**
>
> Se as opções em **Link de atribuição** estiverem esmaecidas, peça ao profissional de marketing para <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions-tab">habilitar as permissões da ad network</Anchor>. As permissões necessárias são **Permitir configurar integração** e **Permitir configurar postbacks de eventos in-app**.
>
> Como alternativa, você pode pedir ao profissional de marketing que forneça o link de atribuição.

<div id="installing-the-app-through-the-attribution-link" />

<Accordion title="Instalação do aplicativo por meio do link de atribuição">

Agora você pode gerar um link de atribuição para testar a atribuição de instalação.

Adicione parâmetros ao link de atribuição de acordo com suas necessidades e com os dados que você deseja registrar.

[![partner-configure-attribution-link.png](https://files.readme.io/9402ab5b3d1750ffd3ae8a2867c751545bdfd5b79202e09c8c90b9bc0bbbef95-21414453180817.png)](https://files.readme.io/9402ab5b3d1750ffd3ae8a2867c751545bdfd5b79202e09c8c90b9bc0bbbef95-21414453180817.png)

> 👍 **Observação**
>
> Para saber mais sobre os parâmetros que você pode adicionar ao link de atribuição, consulte <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">a estrutura e os parâmetros do link de atribuição da AppsFlyer</Anchor>.

</Accordion>

<div id="testing-install-attribution" />

<Accordion title="Testando a atribuição de instalações">

Envie o link de atribuição para o dispositivo de teste. Abra o link no navegador, instale o aplicativo e execute-o.

Executar o aplicativo é crucial para o fluxo de atribuição. Se o aplicativo não for iniciado, nenhuma atribuição será registrada.

Em seguida, você pode [ver a instalação no seu dashboard](/docs/test-marketer-campaign-integration-with-the-ad-network#visualização-de-instalações-no-dashboard).

</Accordion>

## Teste de aplicativos em desenvolvimento

Você pode testar a integração de campanha de um profissional de marketing com sua ad network mesmo que o aplicativo ainda não esteja disponível. No entanto, você precisa pedir ao profissional de marketing que forneça o aplicativo (um arquivo .apk ou .ipa) para que você possa instalá-lo nos seus dispositivos de teste.

<div id="generate-an-attribution-link" />

<Accordion title="Gerar um link de atribuição">

Gere um link de atribuição. Você pode usar as [mesmas instruções listadas acima](/docs/test-marketer-campaign-integration-with-the-ad-network#installing-the-app-through-the-attribution-link). Envie o link de atribuição para o dispositivo de teste e acesse-o usando o navegador do dispositivo.

A seguinte tela aparecerá:

[![app-not-available.png](https://files.readme.io/fda6290e4f0f995dbf04966c0a36b24fb246c4665ec367907178ed1d04edcf0c-21414453195921.png)](https://files.readme.io/fda6290e4f0f995dbf04966c0a36b24fb246c4665ec367907178ed1d04edcf0c-21414453195921.png)

Esse é o resultado esperado. Como o aplicativo não está ativo, o link de atribuição não leva a nenhuma loja de aplicativos. No entanto, o link de atribuição ainda é válido para fins de atribuição. o link de atribuição e seus parâmetros são registrados pelos servidores da AppsFlyer, e os dados são usados para atribuição.

</Accordion>

<div id="installing-the-app" />

<Accordion title="Instalação do aplicativo">

Instale o aplicativo no dispositivo de teste usando o arquivo fornecido pelo profissional de marketing e, em seguida, inicie o aplicativo. Exclua o aplicativo e repita o processo (para gerar várias instalações). Em seguida, você pode [ver as instalações no seu dashboard](/docs/test-marketer-campaign-integration-with-the-ad-network#visualização-de-instalações-no-dashboard).

</Accordion>

## Teste de eventos in-app

> 📘 **Atenção**
>
> Você pode testar postbacks de eventos in-app tanto para aplicativos ativos quanto para aplicativos em desenvolvimento.

Antes de testar postbacks de eventos in-app, entre em contato com o profissional de marketing para saber quais tipos de eventos in-app ele registra e como você pode acioná-los a partir do aplicativo.

<div id="mapping-events" />

<Accordion title="Mapeamento de eventos">

Se o profissional de marketing tiver habilitado a permissão <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">**Configure in-app event postbacks**</Anchor> nas configurações de integração da sua ad network, você poderá mapear eventos da AppsFlyer para os eventos que registra nos seus servidores.

No dashboard da AppsFlyer do seu aplicativo, no menu lateral, selecione **Active integrations** e escolha sua ad network. Na aba **Integration**, role para baixo até **In-app event settings**. Escolha o evento in-app e mapeie-o para o evento correspondente:

[![partner-in-app-events-postbacks-mapping.png](https://files.readme.io/2fe64793de5946d457a8fcb567db761c539755bdbe4cf910953b178eca84d841-21414453211793.png)](https://files.readme.io/2fe64793de5946d457a8fcb567db761c539755bdbe4cf910953b178eca84d841-21414453211793.png)

</Accordion>

<div id="triggering-inapp-events" />

<Accordion title="Acionamento de eventos in-app">

Depois de saber quais eventos in-app o profissional de marketing registra, e com o mapeamento de eventos em vigor, acione alguns eventos no aplicativo instalado.

> 📘 **Atenção**
>
> As ad networks não têm acesso ao Dashboard de eventos e só podem ver eventos in-app no Dashboard Overview depois que o anunciante habilitar a **Acessar dados agregados de eventos in-app** <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions-tab">permissão da ad network</Anchor>. No entanto, you pode exportar dados relacionados a eventos in-app do relatório [Postback de eventos in-app](/docs/test-marketer-campaign-integration-with-the-ad-network#verificação-de-dados-de-postback).

No relatório de postback de eventos in-app, você pode encontrar dados como a URL de postback e os parâmetros mapeados. Use os dados no relatório e compare-os com os dados nos seus servidores (do postback) para garantir que os dados dos postbacks estejam corretos e sejam registrados adequadamente pelos seus servidores.

Depois de exportar o relatório de postbacks de eventos in-app, você pode analisá-lo para verificar o seguinte:

1. O evento é atribuído a você como ad network, no campo **canal de mídia**
2. O nome do evento está correto, no campo **Event name**
3. O postback, se estiver habilitado, contém o nome e o valor do evento, no campo **Postback URL**
4. Os eventos in-app estão mapeados corretamente no campo **Postback URL**

</Accordion>

## Visualização de instalações no Dashboard

Depois de instalar e abrir o aplicativo, você poderá ver os resultados no seu dashboard.

> 🚧 **Importante!**
>
> Para gerar várias instalações, [o dispositivo deve estar na lista de permissões](/docs/test-marketer-campaign-integration-with-the-ad-network#pré-requisitos).

Acesse o dashboard da AppsFlyer e, no menu lateral, selecione **Analisar** >  **Visão geral**.

Filtre pela sua ad network. Você pode ver o número de cliques e instalações atribuídos à sua ad network.

Os dados relacionados a cliques e instalações aparecem na parte superior da tela **Overview**. A tela **Overview** também inclui **Breakdown by campaign** e **Aggregated performance report**. Verifique se as campanhas que aparecem nessas seções correspondem ao parâmetro de campanha no link de atribuição.

## Verificação de dados de postback

Cada instalação atribuída à sua ad network gera um postback de instalação. Se os postbacks de eventos in-app estiverem habilitados, os eventos provenientes de um aplicativo cuja instalação foi atribuída à sua ad network também gerarão postbacks.

Abra a <Anchor target="_blank" href="/marketers/pt/docs/raw-data-export-page">página de exportação de dados brutos</Anchor> e gere 2 relatórios de postback:

1. **de instalações**
2. https://files.readme.io/797989d738fddcce1de7a45a98e13b898d53817c285c839ff1fbb5a92522ccf0-19284078965009.jpg

Ambos os relatórios contêm uma coluna com o título **URL de postback**. Essa coluna lista URLs de postback para instalações ou eventos in-app (dependendo do tipo de relatório).

Revise os dados nessa coluna para verificar o seguinte:

* O endpoint do URL é o correto
* Os parâmetros adicionados à URL correspondem aos adicionados ao link de atribuição da AppsFlyer
* Nos postbacks de eventos in-app, os eventos são mapeados corretamente, ou seja:  
  Nos postbacks de eventos in-app, os eventos são mapeados corretamente, ou seja:  
  `sdk_event=af_purchase&mapped-event=purchase`  
  `sdk_event=af_login&mapped-event=login`
* A coluna **Mensagem de erro do postback** está vazia

<div data-zendesk-anchors="prerequisites=pr%C3%A9-requisitos h_01HKA1DE8VKXM92D7S5BANFZJ4=pr%C3%A9-requisitos h_01HKA1DE8V9A9AJWYQR9VJQ0H8=getting-started h_01HKA1DE8VA7HAM8BT3KZ8HYGP=exemplo testing-live-apps=teste-de-aplicativos-publicados h_01HKA1DE8V0J2Y8DQ60J9S5DAK=teste-de-aplicativos-publicados h_01HKA1DE8VDQGKYSYFDF5K2HSX=importante h_01HKA1DE8VEEH8YE1QT28QVFZQ=installing-the-app-through-the-attribution-link h_01HKA1DE8VV0K8J2AG7W0FDDWY=observa%C3%A7%C3%A3o h_01HKA1DE8VEH7S0JAJTJ91KE7X=testing-install-attribution testing-apps-in-development=teste-de-aplicativos-em-desenvolvimento h_01HKA1DE8VK9RQGQ8BCG157H1Y=teste-de-aplicativos-em-desenvolvimento h_01HKA1DE8VSPE0FFM65AFQRJ8S=generate-an-attribution-link h_01HKA1DE8V68Z5CM4EF7YBPHPS=installing-the-app testing-inapp-events=teste-de-eventos-in-app h_01HKA1DE8VVJXK11BM77D3YWA5=teste-de-eventos-in-app h_01HKA1DE8W2VT648E022BHJP0K=aten%C3%A7%C3%A3o h_01HKA1DE8WQVGPSTG2SQCM2BQW=mapping-events h_01HKA1DE8WRZPCX3GGV01ZK10K=triggering-inapp-events h_01HKA1DE8W8XXM4BK7843TAEJQ=aten%C3%A7%C3%A3o-1 viewing-installs-in-the-dashboard=visualiza%C3%A7%C3%A3o-de-instala%C3%A7%C3%B5es-no-dashboard h_01HKA1DE8WY7VCST4XDN1HWGC7=visualiza%C3%A7%C3%A3o-de-instala%C3%A7%C3%B5es-no-dashboard h_01HKA1DE8WYRTTNC2Q0VGKMM82=importante-1 verifying-postback-data=verifica%C3%A7%C3%A3o-de-dados-de-postback h_01HKA1DE8WEQY58XAPS9MBNGKE=verifica%C3%A7%C3%A3o-de-dados-de-postback" />
