---
title: Teste de integração do Android para ad networks
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
  created_at: '2021-12-06T10:35:58Z'
  edited_at: '2026-08-18T00:39:37Z'
  id: 4412945443857
  locale: pt
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/pt/articles/4412945443857
---
> **Em resumo:** Teste sua integração do AppsFlyer no Android usando o aplicativo AppsFlyer Partner Integrations para acionar postbacks.

<div id="android-integration-testing" />

## Teste de integração no Android

O teste consiste nos seguintes elementos:

* Use a versão Android do aplicativo AppsFlyer Partner Integrations para gerar eventos in-app de instalação de teste e de compra. Esses testes, por sua vez, acionam postbacks enviados para seus endpoints. Você também pode testar eventos in-app de login e registro.
* Ao receber os postbacks, verifique se você consegue ingeri-los.

**Escopo do teste**

A tabela a seguir lista os cenários de teste de acordo com as combinações de configurações disponíveis.

Para cada cenário, você pode testar instalações e eventos in-app. Para eventos in-app, você pode usar o <Anchor target="_blank" href="/partners/pt/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">mapeamento de eventos in-app</Anchor> para mapear os eventos do anunciante aos seus eventos.

<div id="testing" />

## Testes

Conclua os pré-requisitos e, em seguida, execute os procedimentos de teste nas seções a seguir. Cada seção de teste contém uma tabela que você pode usar para registrar os resultados do teste.

<div id="prerequisites" />

<Accordion title="Pré-requisitos">

Conclua os pré-requisitos antes de começar a executar o procedimento de teste.

| Pré-requisitos |
| --- |
| <Anchor target="_blank" href="/partners/pt/docs/turn-on-test-app-integration-for-ad-networks">Integre o aplicativo de teste do Android à sua conta.</Anchor> |
| Verifique se o aplicativo de teste está integrado à sua conta |
| <Anchor target="_blank" href="/partners/pt/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">Mapeie eventos in-app para os nomes dos seus eventos</Anchor>. Nomes de eventos a serem mapeados: `purchase`, `login`, `registration` |
| <Anchor target="_blank" href="/partners/pt/docs/ios-integration-testing-for-ad-networks#attribution-link">Prepare o link de atribuição</Anchor> |
| Teste a atribuição de instalação usando um dispositivo Android |
| Teste a atribuição de evento in-app usando um dispositivo Android |
| Teste a atribuição de retargeting usando um dispositivo Android |

</Accordion>

<div id="test-install-attribution" />

<Accordion title="Testar atribuição de instalação">

**Para acionar postbacks:**

1. Envie o link de atribuição preparado anteriormente para um dispositivo de teste.
2. Clique no link, instale e depois abra o aplicativo.  
   A página **Install Data** é exibida.
3. Valide a atribuição usando os seguintes parâmetros. Se a validação falhar, consulte <Anchor target="_blank" href="/partners/pt/docs/ios-integration-testing-for-ad-networks#troubleshooting">Solução de problemas</Anchor>.

   1. `install_time`: próximo ao horário atual. O horário está em UTC.
   2. `af_status: Non-organic` Se este não for o caso, a instalação não foi atribuída.
   3. `media_source`: sua ad network
4. Toque em **In-App Event Tests.**
5. Toque em **Purchase Event.**  
   A confirmação do evento Purchase é exibida.
6. Verifique se:
   1. Você recebeu os postbacks de instalação e compra.
   2. O nome do evento está mapeado corretamente (se você mapeou eventos in-app).
   3. Você consegue ingerir o postback.

</Accordion>

<div id="supplementary-information-and-procedures" />

## Informações e procedimentos complementares

<div id="about-the-partner-integrations-test-app" />

<Accordion title="Sobre o aplicativo de teste de integrações de parceiros">

O aplicativo Partner Integrations está disponível no Google Play. O aplicativo envia eventos de instalação e eventos in-app para a plataforma da AppsFlyer.

Quando o aplicativo é aberto pela primeira vez, a página **Install Data** exibe os dados de conversão registrados na plataforma da AppsFlyer. Os eventos in-app de teste são acionados na interface do usuário.

As seguintes funções estão disponíveis:

* **In-App Event Tests**  
  Envie `purchase`, `login` e `registration` e eventos in-app. Ao mapear os nomes dos eventos in-app do aplicativo para os nomes dos seus eventos, os postbacks são preenchidos usando os nomes dos seus eventos.

</Accordion>

<div id="attribution-link" />

<Accordion title="Link de atribuição">

Prepare um link de atribuição no dashboard da AppsFlyer usando um dos seguintes métodos:

* Gere o link no dashboard do AppsFlyer.
* Edite o link de exemplo a seguir.

**Para gerar um link no dashboard:**

1. No AppsFlyer, no menu superior, selecione **Meus Aplicativos**.
2. Selecione **adNetworkTest**.
3. No AppsFlyer, no menu lateral, selecione **Collaborate** > **Active Integrations** > selecione sua ad network > a aba **Attribution link**.
4. Na aba Attribution link, defina os parâmetros listados. Você pode adicionar parâmetros adicionais, se necessário. Link para o attribution link 

| Parâmetro | Valor de exemplo | Comentário |
| --- | --- | --- |
| <span id="campaign"></span>Campaign | c-test-2020-12-20 | Defina um valor que seja identificável em seus postbacks |
| <span id="pid"></span>PID | pitestap |  |

5. Copie o link resultante para usar mais tarde.

**Exemplo de link de atribuição:**

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="Aplicativo de teste integrado à sua conta">

**Para verificar se o aplicativo de teste está disponível em sua conta:**

1. Na AppsFlyer, no menu superior, acesse **Meus aplicativos**.
2. Verifique se o app **Partner Integrations adNewtorkTest** é exibido em Apps disponíveis. Se este não for o caso, entre em contato com seu Gerente de Desenvolvimento de Parceiros.

</Accordion>

<div id="troubleshooting" />

<Accordion title="Resolução de problemas">

| Problema | Causa/ação corretiva |
| --- | --- |
| A hora da instalação não é a hora atual | O aplicativo não foi excluído antes da instalação.<br /><br />Exclua o aplicativo e repita o procedimento. |
| O canal de mídia não é o seu canal de mídia | Verifique se você definiu o valor correto de **pid** no link de atribuição. Verifique se você está usando o link de atribuição correto |
| af\_status é orgânico | Verifique o formato do link de atribuição, especialmente o valor de **pid**. |

</Accordion>

<div id="test-retargeting-attribution" />

<Accordion title="Teste de atribuição de retargeting">

Você também pode testar a atribuição de retargeting. O processo é quase o mesmo, exceto por um parâmetro que você adiciona ao link de atribuição.

Gere um novo link de atribuição e adicione o parâmetro `is_retargeting=true` a ele.

```http
https://app.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_click_lookback=7d
          &clickid={clickid}&is_retargeting=true
```

Instale o aplicativo usando o link de retargeting. O fluxo é o mesmo descrito em [teste de atribuição de instalação](/docs/android-integration-testing-for-ad-networks#test-install-attribution).

<div id="viewing-retargeted-installs-in-the-dashboard" />

### Visualização de instalações retargeteadas no dashboard

Acesse seu dashboard da AppsFlyer e clique em **Retargeting** no menu lateral esquerdo. Aguarde até 30 minutos para que a instalação de retargeting apareça no dashboard.

[![com_appsflyer_adNetworkTest-retargeting.png](https://files.readme.io/e46789b004be2f4fc15f095ba11a0f3f5d03abb1240e54e4b534285e3e4efd8d-21266228899601.png)](https://files.readme.io/e46789b004be2f4fc15f095ba11a0f3f5d03abb1240e54e4b534285e3e4efd8d-21266228899601.png)

</Accordion>

<div id="test-viewthrough-attribution" />

<Accordion title="Testar a atribuição de view-through">

1. Na AppsFlyer, acesse **My Apps**.
2. Selecione **adNetworkTest**.
3. Na AppsFlyer, no menu lateral, selecione **Collaborate** > **Active Integrations** > selecione sua ad network > guia **Integration**.
4. Verifique se **Enable view-through attribution** está ativado.
5. Copie o link de atribuição de impressões.

   ```http
   https://impression.appsflyer.com/com.appsflyer.adNetworkTest?pid=YOUR_PID&c=YOUR_CAMPAIGN&af_viewthrough_lookback=24h&advertising_id=YOUR_GAID&af_siteid=YOUR_SITEID
   ```

   Substitua os parâmetros da seguinte forma:

   * YOUR\_PID - seu ID de parceiro fornecido pela AppsFlyer (terminando em *\_int*)
   * YOUR\_CAMPAIGN - qualquer nome de campanha
   * YOUR\_GAID - seu Google Advertising ID
   * YOUR\_SITEID - qualquer ID de site

   Observação: os parâmetros no link são os parâmetros básicos usados aqui para fins de teste. Você pode incluir outros parâmetros no link de atribuição view-through de acordo com suas necessidades.
6. Envie o link de atribuição view-through para o dispositivo de teste.
7. Abra o link no navegador e instale o aplicativo na loja.
8. Inicie o aplicativo.  
   A tela a seguir é exibida:

   ![vta-testing-postback.png](https://files.readme.io/88b6720928d7540eeb2fe8f42f39ecdccc04655aa49f95d08dba5741d5e39982-4831106525457.png)

   Se você não vir esta mensagem, verifique se o link de atribuição view-through está formatado corretamente. Desinstale o aplicativo e reinstale-o usando o link de atribuição view-through com o novo dispositivo de teste.

Observação

Para obter resultados mais detalhados, repita o processo de instalação usando o link de atribuição view-through com o novo dispositivo de teste. Desinstale o aplicativo, altere os parâmetros no link (o nome da campanha, af\_siteid e advertising\_id) e instale novamente clicando na URL.

<div id="view-installs-in-the-dashboard" />

### Ver instalações no dashboard

Depois de instalar e iniciar o aplicativo, você pode ver os resultados no dashboard do AppsFlyer.

Aguarde até 30 minutos para que a instalação apareça no dashboard do aplicativo.

</Accordion>

<div id="raw-data-export" />

<Accordion title="Exportação de dados brutos">

Os dados relacionados a aplicativos cuja instalação é atribuída à sua ad network podem ser exportados em formato CSV.

Os dados incluem o seguinte:

* de instalações
* https://files.readme.io/797989d738fddcce1de7a45a98e13b898d53817c285c839ff1fbb5a92522ccf0-19284078965009.jpg
* Instalações de retargeting
* Eventos in-app de aplicativos instalados a partir de campanhas de retargeting

**Para exportar dados brutos**:

1. No AppsFlyer, acesse **Report** > **Raw data export**.
2. Selecione o intervalo de datas.
3. Selecione um relatório.  
   O relatório é baixado em alguns minutos.

</Accordion>

<div id="verify-postback-data" />

<Accordion title="Verificar dados de postback">

Cada instalação gera um postback que é enviado aos seus servidores. Para verificar a URL de postback, sua estrutura e os parâmetros anexados a ela, exporte o relatório **Installation postbacks**.

O relatório **Installation postbacks** contém uma coluna chamada **Postback URL**. Esta coluna lista as URLs de postback geradas para cada instalação.

Revise os dados dessa coluna para verificar o seguinte:

* O endpoint da URL é o correto
* Os parâmetros acrescentados à URL correspondem aos acrescentados ao link de atribuição da AppsFlyer
* A coluna **Mensagem de erro do postback** está vazia

</Accordion>

<div data-zendesk-anchors="android-integration-testing=teste-de-integra%C3%A7%C3%A3o-no-android h_01HJR6V0MYJXD4QSRT95SVXTWH=teste-de-integra%C3%A7%C3%A3o-no-android testing=testes h_01HJR6V0MYBPC3CSAJTTQSWGAR=testes h_01HJR6V0MYG42PPWXT7H2AGTAE=prerequisites h_01HJR6V0MYDRZGQQ74TJWDJ2WS=test-install-attribution supplementary-information-and-procedures=informa%C3%A7%C3%B5es-e-procedimentos-complementares h_01HJR6V0MYZ5NG21FEKB4HY6HT=informa%C3%A7%C3%B5es-e-procedimentos-complementares h_01HJR6V0MYTZCS097RQP9HG7GY=about-the-partner-integrations-test-app h_01HJR6V0MYVCNVHNCPZ29KRA4K=attribution-link h_01HJR6V0MY6JZXP2NX9YJ9ZY2T=test-app-integrated-in-your-account h_01HJR6V0MYWK7WAAFHRYPCVM7N=troubleshooting h_01HJR6V0MY2SSP17ZEWRM3NXKE=test-retargeting-attribution viewing-retargeted-installs-in-the-dashboard=visualiza%C3%A7%C3%A3o-de-instala%C3%A7%C3%B5es-retargeteadas-no-dashboard h_01HJR6V0MYPC0AZF05YF32Z571=visualiza%C3%A7%C3%A3o-de-instala%C3%A7%C3%B5es-retargeteadas-no-dashboard h_01HJR6V0MY027J9PKXZZ4TCXRX=test-viewthrough-attribution view-installs-in-the-dashboard=ver-instala%C3%A7%C3%B5es-no-dashboard h_01HJR6V0MZ4VA3V8CA3PN5Z31K=ver-instala%C3%A7%C3%B5es-no-dashboard h_01HJR6V0MZCZ3E8NCR6DG6P6P1=raw-data-export h_01HJR6V0MZAHSXCTEZKTVWM96V=verify-postback-data" />
