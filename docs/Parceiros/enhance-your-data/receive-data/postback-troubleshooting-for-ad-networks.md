---
title: Identificação e solução de problemas para ad networks
metadata:
  keywords:
    - Postback
    - Ad Networks
    - Partners
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2022-07-07T15:16:00Z'
  edited_at: '2026-08-18T00:39:20Z'
  id: 7466104144145
  locale: pt
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/pt/articles/7466104144145
---
> **Em um relance:** Se você estiver com problemas para receber postbacks, revise as seguintes soluções.

| **Problema** | **solução** |
| --- | --- |
| <span id="i-dont-see-my-advertisers-app-under-my-apps"></span>Não vejo o aplicativo do anunciante em **Meus aplicativos** | <ul><li>Se o aplicativo do anunciante não aparecer em **Meus aplicativos** (no menu superior), entre em contato com o anunciante e peça que <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-ad-network">conceda a você as permissões relevantes</Anchor>.</li><li>Verifique se a opção de alternância <Anchor target="_blank" href="/marketers/pt/docs/partner-activation-deactivation#ativar-uma-integração-de-parceiro">**Ativar parceiro** está ativada</Anchor>.</li></ul>**Observação:** Se você estiver executando um teste com um aplicativo de produção, registre seu dispositivo de acordo com as instruções <Anchor target="_blank" href="/marketers/pt/docs/registering-test-devices">aqui</Anchor>. |
| <span id="im-not-receiving-install-postbacks"></span>Não estou recebendo postbacks de instalação | <ul><li>Se não houve instalações do aplicativo, você não verá postbacks de instalação.  Verifique se seu aplicativo tem atribuições de instalação: acesse **Configurações** > **Meus aplicativos** > [Escolha o aplicativo] > <Anchor target="_blank" href="/partners/pt/docs/integrated-partners-dashboard">**Visão geral**</Anchor>.</li></ul> |
| <span id="im-not-receiving-inapp-event-postbacks"></span>Não estou recebendo postbacks de eventos in-app | <ul><li>Verifique se os eventos estão <Anchor target="_blank" href="/marketers/pt/docs/in-app-event-postback-configuration">mapeados corretamente</Anchor> na guia de integração, na seção **Postbacks de eventos in-app**</li></ul>**Observação:** Os nomes dos eventos diferenciam maiúsculas de minúsculas e devem ser mapeados usando o mesmo nome enviado via servidor a servidor/SDK. |
| <span id="im-not-receiving-both-install-and-inapp-event-postbacks"></span>Não estou recebendo postbacks de instalação nem de eventos in-app | <ul><li>Se não houve instalações do aplicativo, você não verá postbacks de instalação. Verifique se seu aplicativo tem atribuições de instalação. Acesse **Configurações** > **Meus aplicativos** > [Escolha o aplicativo] > <Anchor target="_blank" href="/partners/pt/docs/integrated-partners-dashboard">**Visão geral**</Anchor>.</li><li>Verifique os relatórios de postback de instalação/eventos in-app e revise os seguintes campos:<ul><li>**URL de postback**: o postback efetivamente entregue. Verifique se não faltam valores cruciais no modelo.</li><li>**Código de resposta HTTP do postback**: o código de resposta que a AppsFlyer recebe do servidor do parceiro. Verifique o código de resposta HTTP. Se não for 2XX, verifique a configuração do seu servidor interno.</li><li>**URL original**: a URL de clique/impressão que a AppsFlyer recebe para a instalação/evento correspondente. Verifique se o link de atribuição está completo. Os dados não fornecidos no link não podem ser retornados por postback.</li></ul></li><li>Verifique as configurações de **Privacidade Avançada**: quando ativada, os <Anchor target="_blank" href="/partners/pt/docs/advanced-privacy-guide-postback-macros-for-ad-networks">dados em nível de usuário para usuários sem consentimento em execução no iOS 14.5+</Anchor> NÃO ficam disponíveis em postbacks.<ul><li>Se o postback de Privacidade Avançada não estiver definido na sua integração, mas o anunciante decidir usar a Privacidade Avançada, nenhum postback será entregue para usuários de iOS sem consentimento.</li></ul></li><li>Verifique a definição de <Anchor target="_blank" href="/marketers/pt/docs/in-app-event-postback-configuration#janela-de-postback-de-eventos-in-app">Janela de postback</Anchor>. Os postbacks não são enviados após o período definido.</li><li>Verifique se o <Anchor target="_blank" href="/marketers/pt/docs/in-app-event-postback-configuration#postbacks-condicionais-de-eventos-in-app">postback condicional</Anchor> está definido.</li><li>Verifique se o <Anchor target="_blank" href="/partners/pt/docs/rejected-attribution-postbacks-to-integrated-partners">tráfego está bloqueado</Anchor>: faça o download e revise o relatório de **postbacks de instalação bloqueados**.</li></ul> |

> 📄 **Consulte também**
>
> * <Anchor target="_blank" href="/marketers/pt/docs/postback-troubleshooting-for-advertisers">Identificação e solução de problemas de postback para anunciantes</Anchor>
> * <Anchor target="_blank" href="/marketers/pt/docs/in-app-event-postback-configuration">Configuração do evento in-app</Anchor>

<div data-zendesk-anchors="h_01HDP4JFM42RZNBGM9TTD5SRP0=consulte-tamb%C3%A9m" />
