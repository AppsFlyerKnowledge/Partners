---
title: Primeiros passos—integração de agências
metadata:
  keywords:
    - Agency Account
    - Agency
    - permissions
    - Advertisers
    - Agencies
    - Partners
    - Marketers
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Marketers
    - Platform essentials
    - Agencies
  created_at: '2019-09-02T12:50:49Z'
  edited_at: '2026-08-19T00:38:44Z'
  id: 360002381617
  locale: pt
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/pt/articles/360002381617
---
> **Visão geral:** configure uma conta de agência e comece a mensurar as campanhas dos seus clientes.

<Embed title="Primeiros passos—integração de agências" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/medias/54qzpj1lm7/swatch" providerUrl="https://fast.wistia.com" />


<div id="appsflyer-attribution-model" />

## Template de atribuição da AppsFlyer

Antes de prosseguir, é importante entender como a atribuição da AppsFlyer funciona. Esta seção explica o que acontece desde o primeiro clique ou impressão até a atribuição de uma instalação ou evento, e muito mais.

[![ua-agency-flow.png](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)

1. Um profissional de marketing ou uma agência em nome do anunciante configura uma campanha com uma determinada ad network, usando links de atribuição da AppsFlyer.
2. Um usuário clica em um de seus anúncios – por exemplo, um banner ou um link de oferta.
3. O link de atribuição da AppsFlyer por trás do anúncio é preenchido com informações coletadas durante o clique. Coletamos as informações do link de atribuição e as armazenamos em nosso banco de dados.
4. O usuário é redirecionado para uma app store.
5. O usuário instala o aplicativo e o abre pela primeira vez. O SDK da AppsFlyer dentro do aplicativo chama nossos servidores com as informações sobre o dispositivo no qual o aplicativo está instalado.
6. Combinamos esses dados ao nosso banco de dados de cliques usando nossos <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-attribution-model">métodos de atribuição</Anchor>.
7. Se encontrarmos uma correspondência, atribuiremos a instalação ao clique. Caso contrário, atribuímos a instalação a um download orgânico.
8. Uma vez atribuída a instalação, nós a mostramos nos dashboards e relatórios do profissional de marketing e da agência (<Anchor target="_blank" href="/partners/pt/docs/about-agency-accounts#redes-de-anúncios-com-autorrelato">exceto Meta ads e Twitter</Anchor>).
9. Em seguida, enviamos um postback com os detalhes da conversão para a ad network, que pode usar essas informações para otimização adicional.

<div id="agency-role-in-mobile-attribution-chain" />

## Função da agência na cadeia de atribuição mobile

Um profissional de marketing, proprietário do aplicativo, integra o SDK da AppsFlyer dentro dele a fim de quantificar seu esforço de marketing.

Alguns proprietários de aplicativos optam por contratar agências de marketing para executar campanhas de anúncios em seu nome. Para isso, a agência deve ter uma conta na AppsFlyer, e os profissionais de marketing devem dar à agência <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">acesso a seus aplicativos</Anchor>.

Portanto, a agência tecnicamente não é proprietária dos aplicativos, mas apenas os promove nos canais de marketing com os quais trabalha, sem o envolvimento técnico, como a integração com o SDK. Dependendo do conjunto de permissões dadas por um profissional de marketing, uma agência pode ter controle sobre uma série de funções.

Quando uma instalação é atribuída a um anúncio colocado por uma agência, ela é exibida no dashboard da agência. O proprietário do aplicativo também o verá e saberá que ela foi atribuída à agência.

Observação: se sua organização é proprietária do aplicativo, ou cuida de seu desenvolvimento, assim como do marketing, você deve abrir uma conta de profissional de marketing.

<div id="pricing" />

## Preços

O escopo da funcionalidade de conta de agência depende das permissões fornecidas pelo proprietário do aplicativo para cada aplicativo. Portanto, as contas da agência são oferecidas **gratuitamente** e apenas os proprietários de aplicativos são cobrados pela atribuição. Os proprietários de aplicativos e agências podem usar dados de atribuição da AppsFlyer para fins de compensação.

## Getting Started

Para configurar uma nova conta de agência:

1. Preencha o <Anchor target="_blank" href="https://www.appsflyer.com/start/agencies/">formulário de registro</Anchor>.
   * Use o domínio de e-mail da sua empresa para o registro.
   * Use um endereço de e-mail que não esteja associado a uma conta existente da AppsFlyer.
2. Pode ser que um membro da equipe de agências da AppsFlyer entre em contato com você para obter mais informações necessárias para concluir o registro.
3. Depois que sua conta for ativada, você receberá uma notificação e poderá começar a usar a AppsFlyer.

<div id="adding-team-members" />

## Adicionando membros à equipe

Quando sua conta estiver ativa, o administrador da conta (a pessoa que a abriu) pode adicionar mais membros da equipe, que podem ter acesso a alguns ou a todos os aplicativos gerenciados pela agência. Para obter detalhes sobre como adicionar novos membros da equipe, clique aqui.

<div id="adding-apps-to-your-account" />

## Adicionando aplicativos à sua conta

Quando você cria sua conta pela primeira vez, ela não possui aplicativos associados a ela:

![agency-start.png](https://files.readme.io/b536dde5f7cc886e7fc6ff22f15c402cea5cf68824fd92f242d13037824072d5-360003986997.png)

Qualquer pessoa ou equipe da agência deve ter a permissão do proprietário do aplicativo para:

* obter acesso ao dashboard do aplicativo
* fazer alterações na configuração
* executar campanhas

Os profissionais de marketing <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">fornecem acesso a qualquer agência</Anchor> diretamente através da plataforma. Uma vez que sua conta esteja configurada e você tenha recebido acesso aos aplicativos, você pode começar a executar campanhas usando os recursos da AppsFlyer.

<div id="what-does-it-mean-to-get-permission-from-a-marketer" />

### O que significa obter permissão de um profissional de marketing

Quando você obtém permissão um de um profissional de marketing:

* O aplicativo aparece em sua conta.
* Você pode configurar integrações com ad networks para o aplicativo (com exceção de algumas redes que exigem configuração pelo proprietário do aplicativo).
* Você pode criar links de atribuição para usar em suas campanhas.
* Você pode configurar integrações de custo com parceiros (que permitem isso).
* Você pode ver os dados do aplicativo.
* Você pode conceder permissão para que as ad networks e seus membros de equipe visualizem informações básicas sobre o aplicativo.  

  <div id="note" />

  > 📘 **Observação**
  >
  > A agência obtém controle sobre o botão de alternância principal das permissões da ad network e sobre as permissões individuais aninhadas nele. Tanto a agência quanto o anunciante podem alterar essas configurações, e a alteração mais recente feita por qualquer uma das partes determina o estado atual.


As permissões adicionais incluem acesso ao relatório de Cohort, dashboard do Protect360 e dados orgânicos agregados. Veja uma <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">descrição das diferentes permissões da ad network</Anchor>.

<div id="app-list" />

### Lista de aplicativos

Depois que você tiver permissão do profissional de marketing, o aplicativo aparece na página do aplicativo.

A página de aplicativos na sua conta lista até 1000 aplicativos. Se a lista de aplicativos para os quais você tem permissões exceder 1000, alguns aplicativos não serão exibidos na lista. Você ainda pode encontrá-los usando a pesquisa.

![agency-apps.png](https://files.readme.io/6ec28125c938a5fb90d6a5bfe80ef40225432c222dcd4fafd747eeba529f1c49-360003722277.png)

<div id="searching-for-apps" />

#### Pesquisando aplicativos

1. Na sua conta, clique em ***Meus aplicativos*** no menu superior
2. No campo de pesquisa, insira o termo de pesquisa, por exemplo:
   * Nome do aplicativo
   * ID da aplicação
   * E-mail do proprietário do aplicativo

<div id="agency-dashboard" />

## Dashboard da agência

Clique em qualquer aplicativo na lista de aplicativos para acessar seu <Anchor target="_blank" href="/marketers/pt/docs/getting-started-with-appsflyer-dashboards">dashboard</Anchor>. Quando você começa a executar campanhas, os dados agregados atribuídos a você são exibidos aqui.

![agency-dashboard.png](https://files.readme.io/5f541770f60ba7d212c9f18e3a14d625758c5d8911997ce4cc39333ee7530244-360003815398.png)

O dashboard Conta de agência inclui acesso padrão a:

* Painel de Visão geral do valor do tempo de vida (Life Time Value - LTV)
* Dashboard de eventos in-app
* Painel de Retargeting

<div id="running-campaigns" />

## Executando campanhas

<div id="self-reporting-networks-srns" />

### Networks de autorrelato (SRNs)

As SRNs, também conhecidas como SANs (redes de autoatribuição), são ad networks que não exigem o link de atribuição da AppsFlyer para reportar cliques e outros dados, e usam a integração direta com a AppsFlyer. Entre essas redes estão <Anchor target="_blank" href="/marketers/pt/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta ads</Anchor>, <Anchor target="_blank" href="/marketers/pt/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">Twitter</Anchor>, <Anchor target="_blank" href="/marketers/pt/docs/google-ads-adwords-integration-setup-for-agencies">Google Ads</Anchor>, <Anchor target="_blank" href="/marketers/pt/docs/snapchat-advanced-srn-integration-setup">Snapchat</Anchor>, DoubleClick, <Anchor target="_blank" href="/marketers/pt/docs/apple-ads-integration-setup">Apple Ads Search</Anchor>, <Anchor target="_blank" href="/marketers/pt/docs/yahoo-integration-setup">Yahoo</Anchor> e <Anchor target="_blank" href="/marketers/pt/docs/yahoo-japan-search-ads-campaign-configuration#agency-integration">Yahoo! JAPÃO</Anchor>.

A maioria dessas ad networks exige uma configuração especial para agências. Por exemplo, como a integração do Meta ads e do Twitter só pode ser configurada pelo proprietário de um aplicativo, os nomes de campanha da agência DEVEM começar com o nome da agência para garantir que as instalações sejam corretamente atribuídas a ela.

Clique nos links acima para ver guias de rede e instruções específicas para as configurações da agência.

<div id="non-srns" />

### Não-SRNs

A maioria das ad networks precisa que os links de atribuição sejam colocados atrás de um anúncio. Saiba mais sobre a execução de campanhas com esses links <Anchor target="_blank" href="/partners/pt/docs/about-agency-accounts#não-srns">aqui</Anchor>.

<div id="sandbox-attribution-agency-campaigns" />

### Atribuição no Sandbox para campanhas de agência

A infraestrutura do SKAdNetwork, parte do iOS da Apple, permite aos profissionais de marketing medir o sucesso da campanha sem IDFA ou identificação publicitária. Embora a Apple não inclua agências como parte do processo de atribuição do SKAdNetwork, e a Appsflyer não possa atribuir agências diretamente, a AppsFlyer tem a capacidade de fornecer dados de atribuição para campanhas de agência em execução em SKAdNetworks.

<div id="campaign-naming" />

#### Nome da campanha

Se você executar campanhas em mídias diferentes de ad networks (mídias sociais, e-mails, blogs, SMS), você poderá usar <Anchor target="_blank" href="/marketers/pt/docs/create-a-onelink-template">links personalizados</Anchor> para elas.

* seu af\_prt (<Anchor target="_blank" href="/partners/pt/docs/about-agency-accounts#parâmetro-af_prt">O que é o seu af\_prt e onde encontrá-lo</Anchor>),
* sublinhado,
* o nome real da campanha que segue a convenção de nomenclatura da agência.

Por exemplo, se o af\_prt for AgencyX, o nome da campanha pode ficar assim:

`Agencyx_SummerSale`

<div id="note-1" />

> 📘 **Observação**
>
> * As campanhas de agência na atribuição do Sandbox também são transparentes, e a identidade da ad network que executa a campanha não é mascarada para o profissional de marketing.

<div id="skadnetwork-agency-campaigns" />

### Campanhas da agência de SKAdNetwork

A infraestrutura do SKAdNetwork, parte do iOS da Apple, permite aos profissionais de marketing medir o sucesso da campanha sem IDFA ou identificação publicitária. Embora a Apple não inclua agências como parte do processo de atribuição do SKAdNetwork, e a Appsflyer não possa atribuir agências diretamente, a AppsFlyer tem a capacidade de fornecer dados de atribuição para campanhas de agência em execução em SKAdNetworks.

<div id="campaign-naming-1" />

#### Primeiros passos—integração de agências

Para visualizar suas campanhas no dashboard de SKAdNetwork da AppsFlyer, os nomes das campanhas que você configura com a SKAdNetwork devem incluir o identificador de parceiro e ser estruturado da seguinte forma:

* seu af\_prt (<Anchor target="_blank" href="/partners/pt/docs/about-agency-accounts#parâmetro-af_prt">O que é o seu af\_prt e onde encontrá-lo</Anchor>),
* sublinhado,
* o nome real da campanha que segue a convenção de nomenclatura da agência.

Se o profissional de marketing desabilitar as permissões da agência, os dados históricos da agência (como instalações e custos) não serão transparentes

`Transparência`

<div id="note-2" />

> 📘 **Observação**
>
> * As campanhas de agência no SKAdNetwork são sempre transparentes e a identidade da ad network que executa a campanha não é mascarada do profissional de marketing. Considere que a partir do iOS 15, o profissional de marketing (proprietário do aplicativo) pode <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/receiving_ad_attributions_and_postbacks">optar por receber diretamente uma cópia do postback.</Anchor>
> * <mark>Você deve solicitar ao profissional de marketing que habilite a configuração **Ativação do parceiro**</mark>  na aba de integração. Se isso não for feito, a AppsFlyer não compartilhará os dados de postback decodificados com as networks, o que afetará a capacidade delas de usá-los para relatórios e otimização. Isso deve ser feito além da configuração de ativação do parceiro, que pode ser acessada na interface do usuário.

<div id="access-to-skan-conversion-studio" />

#### Acesso ao SKAN Conversion Studio

As agências podem <Anchor target="_blank" href="/marketers/pt/docs/skan-conversion-studio#view-cv-mapping">visualizar e fazer download</Anchor>  de uma configuração de mapeamento de CV SKAN de um profissional de marketing no <Anchor target="_blank" href="/marketers/pt/docs/skan-conversion-studio#conceitos-básicos-do-skan-conversion-studio">Conversion Studio</Anchor>, mas não podem configurar ou editar as configurações.

<div id="skadnetwork-dashboard" />

#### Dashboard de SKAdNetwork

<Embed title="Primeiros passos—integração de agências" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/jkm7se0jym" providerUrl="https://fast.wistia.com" />

**Leitura adicional**

* <Anchor target="_blank" href="/marketers/pt/docs/about-att-and-skan">Guia rápido da SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/marketers/pt/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">Dashboard de SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/marketers/pt/docs/skadnetwork-skan-solution-guide">Solução de SKAdNetwork</Anchor>

<div id="single-source-of-truth-ssot-for-agencies" />

### Uma única fonte confiável (SSOT) para agências

O SSOT unifica todos os métodos de atribuição combinando dados de atribuição de diferentes modelos e removendo instalações duplicadas e as métricas associadas relacionadas a custos e receitas. Dessa forma, eCPI, ROI e ROAS, por exemplo, são calculados corretamente.

As agências podem acessar os dados SSOT no painel de visão geral, mas não através da API.

Para incluir o sinalizador SSOT em seu painel de visão geral, o profissional de marketing deve ativar o SSOT no Conversion Studio.

**Leitura adicional**

* <Anchor target="_blank" href="/marketers/pt/docs/single-source-of-truth-ssot-guide-for-ios-attribution">Guia de Single Source of Truth (SSOT) para atribuição no iOS</Anchor>

<div id="what-else-you-can-do" />

## O que mais você pode fazer

* Mensurar a retenção de usuários
* Usar eventos in-app para otimizar suas campanhas
* Executar campanhas de <Anchor target="_blank" href="/marketers/pt/docs/retargeting-attribution-guide">retargeting</Anchor>
* Exportar seus <Anchor target="_blank" href="/marketers/pt/docs/manage-data-access-permissions">dados</Anchor>
* <Anchor target="_blank" href="/marketers/pt/docs/registering-test-devices">Registrar seu dispositivo de teste</Anchor>
* e muito mais.

Você pode encontrar mais informações sobre o uso avançado da Conta de agência <Anchor target="_blank" href="/partners/pt/docs/about-agency-accounts#agency-setting-up-campaigns">aqui</Anchor>.

Encontrou um termo desconhecido? Veja-o em nosso <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-knowledge-base-glossary">Glossário</Anchor>.

Tem uma pergunta técnica urgente? Pesquise em nossa Central de Ajuda: provavelmente temos uma resposta. Se não encontrar uma resposta, entre em contato com nossa equipe de suporte através do canto inferior direito do seu dashboard.

<div data-zendesk-anchors="appsflyer-attribution-model=template-de-atribui%C3%A7%C3%A3o-da-appsflyer h_01HFXXKCMW7EREMC7KEYTF3ERH=template-de-atribui%C3%A7%C3%A3o-da-appsflyer h_01KZTW5D6QWFP2Z3J31M9B6QKR=template-de-atribui%C3%A7%C3%A3o-da-appsflyer agency-role-in-mobile-attribution-chain=fun%C3%A7%C3%A3o-da-ag%C3%AAncia-na-cadeia-de-atribui%C3%A7%C3%A3o-mobile h_01HFXXKCMW987FV2PB4EPXH92Z=fun%C3%A7%C3%A3o-da-ag%C3%AAncia-na-cadeia-de-atribui%C3%A7%C3%A3o-mobile pricing=pre%C3%A7os h_01HFXXKCMWPN6AN98A5RD5YXW7=pre%C3%A7os h_01HFXXKCMWRXVBYTW9RYEX7X8F=getting-started adding-team-members=adicionando-membros-%C3%A0-equipe h_01HFXXKCMWB6ZG3PSHDSETC4XC=adicionando-membros-%C3%A0-equipe adding-apps-to-your-account=adicionando-aplicativos-%C3%A0-sua-conta h_01HFXXKCMWBZVTHAEKED1Q27M3=adicionando-aplicativos-%C3%A0-sua-conta what-does-it-mean-to-get-permission-from-a-marketer=o-que-significa-obter-permiss%C3%A3o-de-um-profissional-de-marketing h_01HFXXKCMWYNNZWTKP9KEQ4VCD=o-que-significa-obter-permiss%C3%A3o-de-um-profissional-de-marketing h_01JV9KR17EEHA6F2F8J13AEZEV=observa%C3%A7%C3%A3o app-list=lista-de-aplicativos h_01HFXXKCMWKW78TMC76F40PY2C=lista-de-aplicativos searching-for-apps=pesquisando-aplicativos h_01HFXXKCMW8S93N577393QZTYX=pesquisando-aplicativos agency-dashboard=dashboard-da-ag%C3%AAncia h_01HFXXKCMWPZVADY15DKATJ7Z4=dashboard-da-ag%C3%AAncia running-campaigns=executando-campanhas h_01HFXXKCMWFB9RXY7AVBX5CGB9=executando-campanhas selfreporting-networks-srns=networks-de-autorrelato-srns h_01HFXXKCMW1Z7FWHDJ3Y6G0NYD=networks-de-autorrelato-srns nonsrns=n%C3%A3o-srns h_01HFXXKCMWPAMZ373D5AVD5EJF=n%C3%A3o-srns sandbox-attribution-agency-campaigns=atribui%C3%A7%C3%A3o-no-sandbox-para-campanhas-de-ag%C3%AAncia h_01J6PCDYM2W1X6EMMEE7SFB3VE=atribui%C3%A7%C3%A3o-no-sandbox-para-campanhas-de-ag%C3%AAncia campaign-naming=nome-da-campanha h_01HFXXKCMWMW1AHXMS19CYD4VC=nome-da-campanha h_01HFXXKCMWEQ41A7TZ2K6DE424=observa%C3%A7%C3%A3o-1 skadnetwork-agency-campaigns=campanhas-da-ag%C3%AAncia-de-skadnetwork h_01HFXXKCMWZ19E0QR1VE977BTS=campanhas-da-ag%C3%AAncia-de-skadnetwork 01J6PCG6JGY2R8T5DDCR8APM66=primeiros-passosintegra%C3%A7%C3%A3o-de-ag%C3%AAncias 01J6PCG6JHK9TGX93SD4DRP393=observa%C3%A7%C3%A3o-2 access-to-skan-conversion-studio=acesso-ao-skan-conversion-studio h_01HFXXKCMWX53HMRG2ZTD9FYQE=acesso-ao-skan-conversion-studio skadnetwork-dashboard=dashboard-de-skadnetwork h_01HFXXKCMW1HHMSS3XAXJKME29=dashboard-de-skadnetwork single-source-of-truth-ssot-for-agencies=uma-%C3%BAnica-fonte-confi%C3%A1vel-ssot-para-ag%C3%AAncias h_01HFXXKCMX1E8GZKHJG7EEJ5Y1=uma-%C3%BAnica-fonte-confi%C3%A1vel-ssot-para-ag%C3%AAncias what-else-you-can-do=o-que-mais-voc%C3%AA-pode-fazer h_01HFXXKCMXQ2JT63GBMC74PWBA=o-que-mais-voc%C3%AA-pode-fazer" />
