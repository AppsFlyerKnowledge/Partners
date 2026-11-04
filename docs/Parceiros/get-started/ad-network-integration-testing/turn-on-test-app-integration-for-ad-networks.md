---
title: Ative a integração do aplicativo de teste para ad networks
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
  created_at: '2021-05-22T15:56:20Z'
  edited_at: '2026-09-10T00:37:43Z'
  id: 360020713538
  locale: pt
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/pt/articles/360020713538
---
> **At a glance:** As ad networks que estiverem realizando testes de integração devem ativar a integração do aplicativo (ativação).

<div id="test-apps-for-ad-networks-ios-and-android" />

## Aplicativos de teste para ad networks (iOS e Android)

Depois de configurar a integração e os postbacks, as ad networks devem testar a integração usando os aplicativos de teste da AppsFlyer. Antes de testar, a ad network deve ativar a integração e habilitar permissões adicionais da ad network, conforme necessário. A ativação é realizada uma vez por aplicativo.

| Tipo de aplicativo de teste | Nome ou ID do aplicativo |
| --- | --- |
| <Anchor target="_blank" href="/partners/pt/docs/getting-started-onboarding-guide-for-ad-networks#parte-2-teste-usando-aplicações-de-anunciantes">com o Android</Anchor> | com.appsflyer.adNetworkTest |
| <Anchor target="_blank" href="/partners/pt/docs/ios-integration-testing-for-ad-networks">/docs/ctv-pc-and-console-platform-attribution-concepts</Anchor> | id1543229303 |
| <Anchor target="_blank" href="/partners/pt/docs/skan-integration-guide-for-ad-networks">Proteção contra fraudes</Anchor> | <ul><li>id888707085</li><li>id888707086</li><li>id888707087</li></ul> |

<div id="activation-procedure" />

### Procedimento de ativação

Use o procedimento a seguir para ativar a integração de um aplicativo de teste específico. Execute o procedimento uma vez por aplicativo.

**Para ativar a integração e conceder permissões a um aplicativo de teste**:

1. No AppsFlyer, selecione um aplicativo de teste entre os listados na tabela anterior.
2. No AppsFlyer, no menu lateral, selecione **Colaborar** > **Integrações de parceiros** > **Integrações ativas**.
3. Selecione sua ad network.
4. **Para ativar a integração com o aplicativo**:  
   1. Acesse a aba de **integração**.
   2. Habilite **Ativar parceiro.**
   3. Clique em **Guardar integração**.
5. **Para conceder permissões**:
   1. Acesse a aba **Permissões**.
   2. Ative **Configurar integração**.
   3. Ative **Configure in-app event postbacks.** Etapa 1:
   4. Clique em **Salvar permissões**.

<div data-zendesk-anchors="test-apps-for-ad-networks-ios-and-android=aplicativos-de-teste-para-ad-networks-ios-e-android h_01HKA15VM7FM69X0AZ1V2H5XPJ=aplicativos-de-teste-para-ad-networks-ios-e-android activation-procedure=procedimento-de-ativa%C3%A7%C3%A3o h_01HKA15VM7J47374WMRG5132GN=procedimento-de-ativa%C3%A7%C3%A3o" />
