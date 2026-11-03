---
title: teste de integração do iOS para ad networks
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
  created_at: '2020-12-16T11:39:36Z'
  edited_at: '2026-08-19T00:38:04Z'
  id: 360016588278
  locale: pt
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/pt/articles/360016588278
---
> **Em resumo:** Teste sua integração do iOS com a AppsFlyer usando o aplicativo AppsFlyer Partner Integrations para acionar postbacks regulares e de Privacidade Avançada.

## teste de integração do iOS

O teste consiste nos seguintes elementos:

* Use a versão para iOS do aplicativo AppsFlyer Partner Integrations para gerar eventos in-app de instalação e compra de teste. Esses testes, por sua vez, acionam postbacks enviados aos seus endpoints. Você também tem a opção de testar eventos in-app de login e registro.
* Ao receber os postbacks, verifique se você consegue ingerí-los.

### Escopo do teste

Os anunciantes controlam os dados compartilhados com ad networks pela configuração de Privacidade Avançada. Essa configuração, em conjunto com a configuração de <Anchor target="_blank" href="/marketers/pt/docs/att-implications-ios-14-and-deprecation-of-lat">ATT</Anchor> do usuário do aplicativo, afeta o tipo de postback e os dados compartilhados com ad networks, conforme descrito no <Anchor target="_blank" href="/partners/pt/docs/advanced-privacy-guide-postback-macros-for-ad-networks">guia de postback de Privacidade Avançada</Anchor>. A tabela a seguir lista os cenários de teste de acordo com as combinações de configuração disponíveis.

Para cada cenário, você pode testar instalações e eventos in-app. Em relação aos eventos in-app, você pode usar o <Anchor target="_blank" href="/partners/pt/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">mapeamento de eventos in-app</Anchor> para mapear eventos do anunciante para os seus eventos.

#### Combinações de cenários de teste

| Cenário | Configuração de Privacidade Avançada | Configuração de ATT no aplicativo | Tipo de postback enviado |
| --- | --- | --- | --- |
| E | Desligado | Permitir | Regular |
| B | Ativado | Pedir ao aplicativo para não rastrear | Agregada da AppsFlyer |

## Testes

Conclua os pré-requisitos e, em seguida, execute os procedimentos de teste nas seções a seguir. As seções de teste contêm, cada uma, uma tabela que você pode usar para registrar os resultados dos testes.

<div id="prerequisites" />

<Accordion title="Pré-requisitos">

Conclua os pré-requisitos antes de começar a executar o procedimento de teste.

| Pré-requisitos |
| --- |
| <Anchor target="_blank" href="/partners/pt/docs/getting-started-onboarding-guide-for-ad-networks#parte-1-integração-e-testes">Conclua a integração padrão com a AppsFlyer.</Anchor> Se necessário, entre em contato com a AppsFlyer usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget do assistente de parceiros</Anchor>. |
| <Anchor target="_blank" href="/partners/pt/docs/self-serve-integration-management-for-ad-networks#privacidade-avançada-e-postbacks-skan">Conclua a integração de Privacidade Avançada com a AppsFlyer.</Anchor> Se necessário, entre em contato com a AppsFlyer usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget do assistente do parceiro</Anchor>. |
| <Anchor target="_blank" href="/partners/pt/docs/turn-on-test-app-integration-for-ad-networks">Integre o aplicativo de teste do iOS à sua conta.</Anchor> |
| [Verifique se o aplicativo de teste está integrado à sua conta](/docs/ios-integration-testing-for-ad-networks#test-app-integrated-in-your-account) |
| <Anchor target="_blank" href="/partners/pt/docs/test-marketer-campaign-integration-with-the-ad-network#mapping-events">Mapeie os eventos in-app para os nomes dos seus eventos</Anchor>. Nomes de eventos a serem mapeados: `purchase`, `login`, `registration` |
| [Preparar link de atribuição](/docs/ios-integration-testing-for-ad-networks#attribution-link) |
| Teste usando um dispositivo com iOS 14.5+ |

</Accordion>

<div id="test-advanced-privacy-off" />

<Accordion title="Teste — Privacidade avançada desativada">

**Para acionar postbacks:**

1. No dashboard da AppsFlyer, defina [Habilitar privacidade avançada](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy) como desativado.
2. No dispositivo:
   1. Verifique se o aplicativo de teste não está instalado. Exclua-o se necessário.
   2. Nas configurações de Privacidade, verifique se **Permitir que Aplicativos Solicitem para Rastrear** está ativado.  

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. Envie o link de atribuição para o dispositivo de teste.
4. Abra o link de atribuição no navegador do dispositivo.  
   Você é redirecionado para a App Store.
5. Faça o download e abra o aplicativo.  
   A caixa de diálogo de consentimento do ATT é exibida.

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. Toque em **Permitir**.  
   A página **Dados de instalação** é exibida.

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. Toque em **ATT Status**.  
   O status **Authorized** é exibido.
8. Valide a atribuição usando os seguintes parâmetros. Se a validação falhar, consulte [Solução de problemas](/docs/ios-integration-testing-for-ad-networks#troubleshooting).

   1. `install_time`: próximo ao horário atual. O horário está em UTC.
   2. `af_status: não orgânico` Se não for o caso, a instalação não foi atribuída.
   3. `media_source`: sua ad network
9. Toque em **Testes de eventos in-app.**

   [![CompraNoAplicativo.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. Toque em **Evento de compra.**  
    A confirmação do evento de compra é exibida.
11. Verifique se:
    1. Você recebeu os postbacks de instalação e compra.
    2. O nome do evento está mapeado corretamente (se você mapeou eventos in-app).
    3. Você consegue receber o postback.

#### Privacidade avançada desativada — Resultados do teste

| Postback | Horário em que você acionou o evento | Tipo de postback esperado | Postback efetivamente recebido (aprovado/reprovado) | Validação do postback (aprovado/reprovado) |
| --- | --- | --- | --- | --- |
| não relacionada |  | Regular |  |  |
| Evento in-app: Compra |  | Regular |  |  |

</Accordion>

<div id="test-advanced-privacy-on" />

<Accordion title="Teste — Privacidade avançada ativada">

**Para acionar postbacks:**

1. No dashboard da AppsFlyer, defina [Enable Advanced Privacy](/docs/ios-integration-testing-for-ad-networks#set-advanced-privacy) como ativado.
2. No dispositivo:
   1. Verifique se o aplicativo de teste não está instalado. Exclua-o, se necessário.
   2. Nas configurações de Privacidade, verifique se a opção **Permitir que aplicativos solicitem rastreamento** está ativada.

      <Image alt="PartnerIntegrationAllow.png" src="https://files.readme.io/f4ee4fdebd5e5ecda3d07a0605c901a66466b85335b7ec29e53a108fd8f09302-360015109697.png" width="201px" />
3. Envie o link de atribuição para o dispositivo de teste.
4. Abra o link de atribuição no navegador do dispositivo.  
   Você será redirecionado para a App Store.
5. Faça o download e abra o aplicativo.  
   A caixa de diálogo de consentimento do ATT é exibida.

   ![AppDialogue_us-en.png](https://files.readme.io/73eb2816ccb3b231646e1cf2d8697e1dfbd4714bf2b0b08532db78d359157da1-360015254318.png)
6. Toque em **Solicitar ao aplicativo que não rastreie.** A página **Dados de instalação** é exibida.

   [<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)
7. Toque em **Status do ATT**.  
   O status **Negado** é exibido.
8. Valide a atribuição usando os parâmetros listados. Se a validação falhar, consulte [Solução de problemas](/docs/ios-integration-testing-for-ad-networks#troubleshooting).

   1. `install_time`: próximo ao horário atual. O horário está em UTC.
   2. `af_status: Non-organic` Se esse não for o caso, a instalação não foi atribuída.
   3. `media_source`: sua ad network
9. Toque em **Testes de Eventos in-app.**

   [![AppPurchase.png](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)](https://files.readme.io/d4458cd562afa693d28827a23152a038a208142360488111bc62ca55a378bc4d-360015251478.png)
10. Toque em **Evento de compra.**
11. Verifique se:
    1. Você recebeu postbacks de instalação e compra.
    2. O nome do evento está mapeado corretamente (se você mapeou eventos in-app).
    3. Você consegue ingerir o postback.

#### Privacidade avançada ativada — Resultados do teste

| Postback | Horário em que você acionou o evento | Tipo de postback esperado | Postback real recebido (aprovado/reprovado) | Validação do postback (aprovado/reprovado) |
| --- | --- | --- | --- | --- |
| não relacionada |  | Agregada da AppsFlyer |  |  |
| Evento in-app: Compra |  | Agregada da AppsFlyer |  |  |

</Accordion>

## Informações e procedimentos complementares

<div id="about-the-partner-integrations-test-app" />

<Accordion title="Sobre o aplicativo de teste de integrações de parceiros">

O aplicativo Partner Integrations está disponível na loja de aplicativos. O aplicativo envia eventos de instalação e in-app para a plataforma AppsFlyer.

Quando o aplicativo é aberto pela primeira vez, a caixa de diálogo do iOS **Solicitar rastreamento** é exibida, seguida pela página **Dados de instalação**, que mostra os dados de conversão registrados na plataforma AppsFlyer. Os eventos in-app de teste são acionados na interface do usuário.

[<Image alt="PartnerIntegrationInstallData.png" src="https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png" width="246px" />](https://files.readme.io/50c601ba330631ce96abcc7fd5b765b16858216eb503df2b0573f1420b58641d-360015093657.png)

As seguintes funções estão disponíveis:

* **Testes de evento in-app**Envia eventos in-app `purchase`, `login` e `registration`. Ao mapear os nomes dos eventos in-app do aplicativo para os nomes dos seus eventos, os postbacks são preenchidos usando os nomes dos seus eventos.
* **Status de ATT**Retorna o status atual de ATT reportado pelo iOS como **Authorized** ou **Denied**. O status de ATT depende do consentimento do usuário para rastrear na caixa de diálogo de consentimento de ATT e da configuração do dispositivo **Permitir que aplicativos solicitem para rastrear**.

</Accordion>

<div id="attribution-link" />

<Accordion title="Link de atribuição">

Prepare um link de atribuição no dashboard da AppsFlyer usando um dos seguintes métodos:

* Gere o link no dashboard da AppsFlyer.
* Edite o link de exemplo a seguir.

**Para gerar um link no dashboard:**

1. Na AppsFlyer, acesse **My Apps**.
2. Selecione **id1543229303**.
3. No menu lateral, selecione **Collaborate** > **Active Integrations** > selecione sua ad network > a aba **Attribution link**.
4. Na aba Link de atribuição, defina os parâmetros listados. Você pode adicionar parâmetros adicionais, se necessário. 

| Parâmetro | Valor de exemplo | Comentário |
| --- | --- | --- |
| Campaign | c-test-2020-12-20 | Defina um valor que seja identificável em seus postbacks |

5. Copie o link resultante para usar depois.

**Exemplo de link de atribuição:**

```http
https://app.appsflyer.com/id1543229303?pid=pitestap_int&c=c-test-2020-12-20
```

</Accordion>

<div id="set-advanced-privacy" />

<Accordion title="Definir Privacidade avançada">

<Image alt="AdvancedPrivacyOff.png" src="https://files.readme.io/ef845ea74cbaa0d3214e61c6e2229fd4b9026d0e221b19fecb9e3486e9b795eb-360014980157.png" width="357px" />

**Para alterar a configuração Ativar Privacidade avançada:**

1. Na AppsFlyer, acesse **My Apps**.
2. Selecione o aplicativo id1543229303.
3. No menu lateral, selecione **Collaborate** > **Active Integrations** > selecione sua ad network > a aba **Integration** .
4. Defina **Enable Advanced Privacy** para a configuração apropriada para cada cenário de teste.
5. Clique em **Salvar Integração**.

</Accordion>

<div id="test-app-integrated-in-your-account" />

<Accordion title="Aplicativo de teste integrado à sua conta">

**Para verificar se o aplicativo de teste está disponível na sua conta:**

1. Na AppsFlyer, acesse **My Apps**.
2. Verifique se o aplicativo **Partner Integrations id1543229303** é exibido em Apps disponíveis. Se esse não for o caso, entre em contato com seu Gerente de Desenvolvimento de Parceiros.

</Accordion>

<div id="troubleshooting" />

<Accordion title="Resolução de problemas">

| Problema | Causa/ação corretiva |
| --- | --- |
| O horário da instalação não é o horário atual | O aplicativo não foi excluído antes da instalação.<br /><br />Exclua o aplicativo e repita o procedimento. |
| O canal de mídia não é o seu canal de mídia | Verifique se você definiu o valor correto de **pid** no link de atribuição. Verifique se você está usando o link de atribuição correto |
| af\_status é orgânico | Verifique se a versão do iOS do dispositivo está de acordo com a indicada nos pré-requisitos.<br /><br />Verifique o formato do link de atribuição, especialmente o valor de **pid**. |

</Accordion>

<div data-zendesk-anchors="ios-integration-testing=teste-de-integra%C3%A7%C3%A3o-do-ios h_01HJR5YDW9ENA1B1AC1DQVX8SF=teste-de-integra%C3%A7%C3%A3o-do-ios testing-scope=escopo-do-teste h_01HJR5YDW92MXP9DDBX9C1928V=escopo-do-teste test-scenario-combinations=combina%C3%A7%C3%B5es-de-cen%C3%A1rios-de-teste h_01HJR5YDW9Q7B10MXB1V4AKH2D=combina%C3%A7%C3%B5es-de-cen%C3%A1rios-de-teste testing=testes h_01HJR5YDW9AGY148E1ZD97JFRB=testes h_01HJR5YDW9SGN9KH63CPZ54RM5=prerequisites test%E2%80%94advanced-privacy-off=test-advanced-privacy-off h_01HJR5YDWA20EQT5RE1EJ7QK2X=test-advanced-privacy-off advanced-privacy-off%E2%80%94test-results=privacidade-avan%C3%A7ada-desativada--resultados-do-teste h_01HJR5YDWAEAR22NPXF8ZD5QX6=privacidade-avan%C3%A7ada-desativada--resultados-do-teste test%E2%80%94advanced-privacy-on=test-advanced-privacy-on h_01HJR5YDWAY6B55BFQ1B0WJEHR=test-advanced-privacy-on advanced-privacy-on%E2%80%94test-results=privacidade-avan%C3%A7ada-ativada--resultados-do-teste h_01HJR5YDWAK3DZ1Q0W3TSR7ZKZ=privacidade-avan%C3%A7ada-ativada--resultados-do-teste supplementary-information-and-procedures=informa%C3%A7%C3%B5es-e-procedimentos-complementares h_01HJR5YDWA74Q46F6XKY5J375C=informa%C3%A7%C3%B5es-e-procedimentos-complementares h_01HJR5YDWASJWC1NGNABWR1VW5=about-the-partner-integrations-test-app h_01HJR5YDWA0WXWN5B5VNPK40FY=attribution-link h_01HJR5YDWA73BQB478D6N0R8GP=set-advanced-privacy h_01HJR5YDWAGZ5XMQJG1KX3J6CP=test-app-integrated-in-your-account h_01HJR5YDWAXRD7DVHTZPJCFM56=troubleshooting" />
