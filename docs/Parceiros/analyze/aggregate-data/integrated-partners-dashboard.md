---
title: Painel de controle integrado de parceiros
metadata:
  keywords:
    - partner login
    - partner dashboard
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
  created_at: '2016-08-08T08:11:38Z'
  edited_at: '2026-08-19T00:36:23Z'
  id: 212955423
  locale: pt
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/pt/articles/212955423
---
> **Visão geral:** os parceiros integrados usam o painel e os relatórios para visualizar e analisar o tráfego da campanha atribuído a você.

<div id="using-the-appsflyer-dashboard" />

## Usando o painel da AppsFlyer

**Para fazer login na AppsFlyer**:

1. <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">Faça login</Anchor> ou acesse https://hq1.appsflyer.com/auth/login  
   A lista de aplicativos é exibida.
2. Selecione um aplicativo ou faça uma busca por ele.  
   Atenção! Se você não vir o aplicativo necessário, peça ao anunciante para conceder <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions">permissões de ad network</Anchor>. O anunciante faz isso no painel da AppsFlyer na aba de permissões.

<div id="overview-dashboard" />

## Painel de Visão geral

As métricas e os gráficos de desempenho da campanha estão disponíveis no painel de Visão geral. Esse painel contém diferentes tipos de visualização para campanhas de retargeting e UA.

<div id="report-access" />

## Acesso ao relatório

Para ver os dados do relatório:

* No menu lateral, selecione uma das seguintes opções:
  * <Anchor target="_blank" href="/marketers/pt/docs/raw-data-export-page">Exportação de dados brutos</Anchor>
  * <Anchor target="_blank" href="/marketers/pt/docs/aggregated-data-export-page">Exportação de dados agregados</Anchor>  
    A janela Relatórios é aberta.

<div id="note" />

> 📘 **Nota**
>
> * Os dados mostrados nos relatórios de dados brutos são limitados aos dados brutos em postbacks atribuídos apenas ao parceiro.
> * Para assinantes do Protect360, quando a permissão **<Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#access-protect360-dashboard-raw-data">dashboard & dados brutos do Protect360</Anchor>** é concedida pelo anunciante, os parceiros também têm acesso aos relatórios de dados brutos do Protect360.
> * Os dados do **valor do evento** não são exibidos neste relatório. Para obter valores de eventos, você pode fazer o seguinte:
>
> * * Solicite ao anunciante que forneça a você relatórios de dados brutos de eventos in-app
>   * Add `(event-value)` <Anchor target="_blank" href="/partners/pt/docs/postback-macros-for-ad-networks">macro to the postback URL</Anchor>

<div id="using-postback-reports" />

### Usar relatórios de postback

Você pode usar os <Anchor target="_blank" href="/marketers/pt/docs/raw-data-reporting-overview#postbacks%C2%A0">relatórios de postback</Anchor> de eventos de instalação e in-app para encontrar ações “ausentes”, ou seja, quando os dados brutos do anunciante mostram ações do usuário que não foram registradas na ad network.

Faça o download do relatório de Postbacks relevante e procure os campos **URL do postback** e **Código de resposta Http do postback**:

* Se o código de resposta for 200, a AppsFlyer enviará o postback e recebeu a confirmação da rede de anúncios.
* Se o código de resposta estiver faltando, a AppsFlyer enviou o postback, mas não recebeu nenhuma resposta. O campo **Mensagem de erro do postback** descreve o problema.

[![](https://files.readme.io/e846104ebdd43b6bdd5c635e645ba5806aa152e6fa84d92f957b754b22fd819a-360005578257.png)](https://files.readme.io/e846104ebdd43b6bdd5c635e645ba5806aa152e6fa84d92f957b754b22fd819a-360005578257.png)

<div id="viewing-configuration-settings-and-data" />

## Visualizar configurações e dados

Click **Integrated Partners** on the left side of the window to view the current configuration settings. Mesmo que você não tenha recebido permissões, poderá visualizar as definições de configuração (modo somente leitura).

A ad network pode visualizar a configuração no próprio dashboard somente quando ela é definida pelo anunciante. 

As agências podem configurar a ad network ao receber a permissão relevante do anunciante. Observe que **quando** **a configuração é feita por uma agência, a ad network a vê como inativa**.

<div id="permissions" />

## Authorization: Bearer

Usando a aba **Permissões**, os anunciantes podem <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions">conceder diferentes tipos de permissões às ad networks</Anchor>.

<div id="enabling-permissions" />

### Ativar permissões

O primeiro passo é que seu cliente habilite as permissões. Seu cliente deve ativar as **Permissões de ad network**. Depois, ocorre o seguinte:

1. O aplicativo é exibido na sua conta de ad network.
2. O administrador da sua conta de ad network recebe acesso para visualizar o dashboard do aplicativo do seu cliente. No primeiro estágio, somente o administrador tem acesso. Se você quiser que um membro da sua equipe também visualize o dashboard do aplicativo, seu cliente precisará conceder permissões a essa pessoa.
3. As permissões para visualizar o dashboard do aplicativo são concedidas somente à sua ad network.

<div id="granting-permissions-to-ad-network-team-members" />

### Conceder permissões a membros da equipe da ad network

Se você quiser que um membro da sua equipe também visualize o dashboard do aplicativo, seu cliente precisará conceder permissões a essa pessoa.

1. Forneça ao seu cliente os e-mails dos membros da equipe aos quais você quer que o cliente conceda permissões.
2. O cliente deve <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions">adicioná-los à integração com sua ad network</Anchor>.

<div id="granting-additional-permissions" />

### Conceder permissões adicionais

Seu cliente pode conceder permissão adicional para que a ad network e os membros da equipe dela visualizem o seguinte:

* Configuração de parâmetros de integração
* Configuração do evento in-app
* Relatório de retenção
* Usuário fidelizados
* https://files.readme.io/797989d738fddcce1de7a45a98e13b898d53817c285c839ff1fbb5a92522ccf0-19284078965009.jpg
* Resultados
* Protect360 dashboard - available only to Protect360 customers

To allow this, contact your client to select you from the Integrated Partners list and grant you access to the relevant section within the Permissions tab.

Quando o anunciante concede permissão para a ad network configurar o link de atribuição dele e mapear eventos in-app, ela pode acessar as guias relevantes e fazer as alterações necessárias.

<div id="note-1" />

> 📘 **Nota**
>
> * Any changes made to the configuration overwrites the current configuration irrespective of whether it is set by the advertiser or the ad network.
> * As agências podem adicionar membros da equipe da ad network à configuração, mas somente os proprietários do aplicativo podem conceder permissões a ad networks.

Once your client has granted you permission to the integration parameter configurations, you are able to access it from the left side of the main dashboard and select **Integrated Partners.**

Se o seu cliente tiver concedido a você permissão para o Relatório de retenção, você poderá acessá-lo no lado esquerdo do dashboard principal e selecionar **Retenção.**

<div data-zendesk-anchors="using-the-appsflyer-dashboard=usando-o-painel-da-appsflyer h_01HCF5VPHN5RRQFXVJJFPFQBSW=usando-o-painel-da-appsflyer overview-dashboard=painel-de-vis%C3%A3o-geral h_01HCF5VPHNXBQZNF9MNEVCQ243=painel-de-vis%C3%A3o-geral report-access=acesso-ao-relat%C3%B3rio h_01HCF5VPHN08CV555KDHB7QP1Z=acesso-ao-relat%C3%B3rio h_01HCF5VPHN3REJ2FPD8386Z92S=nota using-postback-reports=usar-relat%C3%B3rios-de-postback h_01HCF5VPHN8RV3GBX1NNFX10P0=usar-relat%C3%B3rios-de-postback viewing-configuration-settings-and-data=visualizar-configura%C3%A7%C3%B5es-e-dados h_01HCF5VPHNSW9X7SNQPC17Q45A=visualizar-configura%C3%A7%C3%B5es-e-dados permissions=authorization-bearer h_01HCF5VPHN6AJ7SE6MGW57BPW8=authorization-bearer enabling-permissions=ativar-permiss%C3%B5es h_01HCF5VPHNRCQ5P3MZF9S5RWZW=ativar-permiss%C3%B5es granting-permissions-to-ad-network-team-members=conceder-permiss%C3%B5es-a-membros-da-equipe-da-ad-network h_01HCF5VPHP2EXY705GW2VM5YMA=conceder-permiss%C3%B5es-a-membros-da-equipe-da-ad-network granting-additional-permissions=conceder-permiss%C3%B5es-adicionais h_01HCF5VPHPHS8QQBMVTGV7B4VJ=conceder-permiss%C3%B5es-adicionais h_01HCF5VPHPCD52R9222AFQH176=nota-1" />
