---
title: Sobre contas de agência
metadata:
  keywords:
    - In-App Events
    - Agency Account
    - ROI
    - Agency
    - FMP
    - Advertisers
    - Agencies
    - Listed Agency
    - all installs
    - all launches
    - Partners
    - agency sign up
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
  created_at: '2013-12-08T10:02:42Z'
  edited_at: '2026-08-18T00:40:20Z'
  id: 207034106
  locale: pt
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/pt/articles/207034106
---
> **Visão geral:** Aproveite ao máximo a sua conta de agência AppsFlyer com uma configuração avançada.

## Sobre contas de agência

As contas de agência são usadas pelas equipas de agência para medir campanhas de marketing de apps realizadas pela agência para clientes de marketing (proprietários das apps).

* As principais métricas de antes e depois da instalação estão disponíveis para garantir que as agências oferecem um desempenho ideal em todo o seu portefólio de clientes.
* Os painéis de contas de agência oferecem capacidades e conteúdos semelhantes aos dos painéis dos profissionais de marketing. Isto inclui os seguintes painéis:
  * Visão geral do valor ao longo da vida
  * Eventos na app
  * Redirecionamento
* Os KPIs disponíveis incluem impressões, cliques, instalações, lealdade do utilizador, custo e ROI. Sobre o <Anchor target="_blank" href="/marketers/pt/docs/getting-started-with-appsflyer-dashboards">painel.</Anchor>

### Acesso da agência aos dados de marketing

As agências têm sempre acesso aos dados de tráfego atribuídos à agência. Os profissionais de marketing podem <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">conceder acesso às agências a</Anchor> dados adicionais, por exemplo, dados agregados orgânicos. Consulte o <Anchor target="_blank" href="/marketers/pt/docs/manage-data-access-permissions">acesso aos dados por diferentes tipos de utilizadores.</Anchor>

### Acesso da agência às integrações de redes de anúncios

Para permitir o acesso às integrações de redes de anúncios e medir as suas campanhas, a sua agência deve ser pré-aprovada pela rede de anúncios. Isto é feito ao incluir o ID da sua agência (af\_prt) na lista de agências autorizadas da rede de anúncios. Contacte o parceiro para garantir a inclusão da sua agência. [Veja aqui](/docs/about-agency-accounts#parâmetro-af_prt) como encontrar o ID da sua agência.

> 📘 **Observação**
>
> * Também se aplica a parâmetros af\_prt vazios em links de atribuição
> * Não se aplica a agências que trabalham com <Anchor target="_blank" href="/marketers/pt/docs/self-reporting-networks-srns">SRNs</Anchor>

### Transparência da agência

Por padrão, o tráfego da agência é definido como transparente. <Anchor target="_blank" href="/partners/pt/docs/getting-started-agency-onboarding#transparency">Saiba mais</Anchor>

## Comparação de diferentes tipos de contas

<div id="agency-versus-marketer-accounts" />

<Accordion title="Contas de agência versus contas de marketing">

* **As contas de marketing** são direcionadas para servir o proprietário da app e dos dados. Os profissionais de marketing adicionam apps às suas contas e determinam as permissões de acesso aos dados.
* **As contas de agência** são projetadas especificamente para equipas de agências. Elas incluem ferramentas para a medição e análise eficazes de campanhas de marketing em todo o seu portefólio de clientes.

As estruturas de contas permitem a partilha de conhecimento entre equipas de agências globais e possibilitam a medição, cálculos, relatórios e otimização do ROI a nível de grupo.

#### Diferenças entre contas de marketing e de agência

|  | Marketing | **Agência** |
| --- | --- | --- |
| Implementação ao nível do código | Sim | Não; apenas promoção da aplicação |
| Definições ao nível da conta | Membros da equipa, permissões dos membros da equipa, definições, preferências de pagamento | Membros da equipa da agência e respetivas permissões. |
| Definições ao nível da aplicação | Janela de reatribuição, configuração do OneLink, fuso horário, moeda | Todas as outras definições seguem as estipuladas pelo marketer |
| Configuração ao nível de parceiro integrado | <ul><li>Permissões da agência</li><li>Todas as configurações não-SRN (redes de anúncios baseadas em links de atribuição)</li><li>Configurações SRN</li><li>Gestão de links</li></ul> | <ul><li>Todas as outras configurações não-SRN</li><li>Algumas configurações SRN que requerem intervenção mínima por parte do marketer:</li></ul><ul><li>Doubleclick do Google<ul><li>Snapchat</li><li>Tencent</li></ul></li></ul>Outros SRN devem ser configurados pelo marketer para que a agência os possa utilizar.<ul><li>Gestão de links (utilizando modelos definidos pelos marketers)</li></ul> |
| Funcionalidades adicionais | Sim (alguns, se incluídos no plano de subscrição) | De acordo com a subscrição do marketer e as <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">permissões</Anchor> concedidas à agência (ver tabela abaixo) |

### Funcionalidades disponíveis para agências

| Disponível por defeito | Não disponível | Requer autorização do marketer |
| --- | --- | --- |
| <ul><li>Painel de visão geral do valor vitalício</li><li>Painel de eventos na aplicação</li><li>Painel de redirecionamento</li><li>Integrações ativas</li><li><Anchor target="_blank" href="/partners/pt/docs/getting-started-agency-onboarding#uma-única-fonte-confiável-ssot-para-agências">Painel SSOT</Anchor>\*\*</li></ul>\*\* Disponível apenas após ativação por parte do marketer. | <ul><li>Painel de atividades</li><li>Painel personalizado</li><li>Análise baseada em pessoas</li><li>Audiências</li><li>Relatório de pivot</li><li>API push</li><li>Data Locker</li></ul>*Apenas relatórios de coorte disponíveis mediante permissão do marketer | <ul><li>Relatório de retenção</li><li>Relatório do painel de coorte</li><li><Anchor target="_blank" href="/partners/pt/docs/data-locker-reports-for-agencies">Relatório de coorte do Data Locker</Anchor></li><li>Os alertas do Protect360 são atualizados no horário UTC diário.</li><li>Exportação de dados brutos</li><li>Dados orgânicos agregados</li><li>API de extração</li></ul> |

</Accordion>

<div id="agency-vs-ad-network-account" />

<Accordion title="Agência vs. conta de rede de anúncios">

#### Diferenças entre contas de rede de anúncios e agências

<table><thead><tr><th>Rede de anúncios</th><th>Agência</th></tr></thead><tbody><tr><td>Parâmetro de link de atribuição para identificação: <code>pid</code> </td><td>Parâmetro de link de atribuição para identificação: <code>af_prt</code> </td></tr><tr><td>Coloca anúncios de apps na sua própria plataforma</td><td>Promove a app através de múltiplas fontes de mídia</td></tr><tr><td>Vê apenas tráfego de anúncios na sua plataforma</td><td>Vê apenas tráfego das fontes de mídia anunciadas</td></tr><tr><td>Pode receber informações em tempo real sobre instalações e eventos na app via postbacks</td><td>Não pode receber informações em tempo real sobre instalações e eventos na app via postbacks</td></tr><tr><td>Pode configurar postbacks de eventos dentro da app para qualquer tráfego proveniente de si próprio\*</td><td>Pode configurar postbacks de eventos dentro da app para alguns dos parceiros de onde traz tráfego\*</td></tr><tr><td colspan="2">\* Requer permissão do responsável de marketing</td></tr></tbody></table>

</Accordion>

## Contas de agência — campanhas e relatórios

<div id="agency-setting-up-campaigns" />

<Accordion title="Agência: configuração de campanhas">

As agências podem medir os seguintes tipos de tráfego principais:

* [Redes de anúncios que fazem autorrelato (SRNs)](/docs/about-agency-accounts#redes-de-anúncios-com-autorrelato)
* [Não SRNs (redes de anúncios que usam links de atribuição)](/docs/about-agency-accounts#não-srns)

> 🚧 **Importante!**
>
> Ao trabalhar com agências, desativar um parceiro integrado não desativa automaticamente certos recursos de atribuição para as agências conectadas a esse parceiro:
>
> Para desativar esses recursos para agências, o anunciante deve desativar manualmente as seguintes configurações antes de desativar o parceiro:
>
> 1. Atribuição de instalação de view-through
> 2. Prioridade de atribuição igual entre plataformas
>
> Depois de desativar essas opções, o anunciante deverá seguir com a desativação do parceiro.
>
> **Atenção:** Se o anunciante desativar o parceiro sem desativar essas configurações primeiro, as agências poderão continuar usando os recursos de atribuição.

### Redes de anúncios com autorrelato

As redes de autorrelato, como Meta Ads, Google Ads ou X Ads, não utilizam links de atribuição externos. Cada rede tem os seus próprios métodos e APIs que a AppsFlyer utiliza para comunicar novas instalações, eventos dentro da app, etc.

#### Configurações SRN

| SRN | O profissional de marketing deve realizar a configuração inicial do SRN | Detalhes |
| --- | --- | --- |
| Anúncios de Busca da Apple | Sim | Para detalhes sobre a configuração de agências para campanhas Apple Search Ads, clique <Anchor target="_blank" href="/marketers/pt/docs/apple-ads-integration-setup#configurando-agências-e-parceiros-de-marketing">aqui</Anchor>. |
| Google Ads | Sim | Para detalhes sobre a configuração de agências para campanhas Google Ads, clique <Anchor target="_blank" href="/marketers/pt/docs/google-ads-adwords-integration-setup-for-agencies">aqui</Anchor>. |
| Plataforma de Marketing do Google (GMP) | Não | O GMP possui duas APIs diferentes. Saiba mais sobre as <Anchor target="_blank" href="/marketers/pt/docs/google-marketing-platform-display-video-360-dv360-integration#comparing-the-legacy-and-new-integrations">diferenças entre ambas</Anchor> e escolha aquela que é relevante para si. |
| Meta Ads  <br />e  <br />X Ads | Sim | **Nota:** Esta secção refere-se aos Meta Ads. Para atribuição de posts no Facebook Social, leia sobre [Meios Próprios](/docs/about-agency-accounts#owned-media%E2%80%94onelink-and-custom-links).<br /><br />**Todas as campanhas Meta Ads e X Ads devem começar com o nome da conta da agência seguido por "\_".** O nome é definido na plataforma AppsFlyer.<br />Campanhas que não estejam corretamente nomeadas são visíveis para o profissional de marketing, mas permanecem invisíveis para a conta da agência.<br /><br />**Nota:**<ul><li>O nome da agência diferencia maiúsculas e minúsculas.</li><li>Veja mais detalhes sobre a configuração de <Anchor target="_blank" href="/marketers/pt/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta Ads</Anchor> e <Anchor target="_blank" href="/marketers/pt/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor> para agências.</li><li>Contacte [agency@appsflyer.com](mailto:agency@appsflyer.com) se tiver alguma dúvida sobre isto.</li></ul>**Exemplo**<br />A agencyx realiza uma campanha de Meta Ads chamada agencyx\_brilliantcampaign, que é visível para si.<br /><br />A agencyz realiza uma campanha X Ads chamada AgencyZ\_whathaveidonewrong, mas não vê resultados. Isto ocorre porque a parte do nome da agência na campanha é diferente do nome da agência definido (com A e Z maiúsculos). |
| Snapchat | Não | Para obter detalhes sobre a configuração da agência para campanhas no Snapchat, clique <Anchor target="_blank" href="/marketers/pt/docs/snapchat-advanced-srn-integration-setup">aqui</Anchor>. |
| TikTok para Empresas | Sim | Para obter detalhes sobre a configuração da agência para campanhas do TikTok for Business, clique <Anchor target="_blank" href="/marketers/pt/docs/tiktok-for-business-advanced-srn-integration-setup#setting-up-tiktok-for-business-for-agencies">aqui</Anchor>. |
| Yahoo (Oath: Plataformas de anúncios / Yahoo Gemini) | Sim | Para detalhes da configuração da agência para campanhas do Yahoo, <Anchor target="_blank" href="/marketers/pt/docs/yahoo-integration-setup#configuração-da-agência">clique aqui</Anchor>. |

### Não-SRNs

Ao contrário dos SRNs, a maioria das redes de anúncios utiliza links de atribuição para fins de atribuição. <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#attribution-link-tab">Esses links de atribuição já estão disponíveis</Anchor> nas configurações de cada rede no AppsFlyer e podem ser copiados diretamente de lá.

Para as agências, o processo é quase idêntico ao dos profissionais de marketing. Ao acessar a janela de configuração de qualquer rede de anúncios padrão, o link de atribuição já está presente. A única diferença é a adição automática do parâmetro `af_prt` ao link de atribuição.

#### Visibilidade da configuração de redes de anúncios

A configuração da rede de anúncios é visível para as próprias redes apenas quando o profissional de marketing (dono da aplicação) a configura. Quando uma agência ativa e configura a integração da rede de anúncios, a rede vê essa seção como inativa.

#### Parâmetro af\_prt

O valor do parâmetro `af_prt` é o nome da agência. Quando o nome da agência é inserido no parâmetro `af_prt`, ele é convertido para letras minúsculas.

Quando `af_prt` com o nome da sua agência faz parte do link de atribuição, novas instalações podem ser atribuídas à sua conta de agência. Caso contrário, novas instalações são atribuídas diretamente à rede de anúncios.

[![agência-af-prt.png](https://files.readme.io/61559e2e1628e9411665b7e8d3d3d440a55effb3bccda79c7fe1ee02fd43fb8c-32355631649937.png)](https://files.readme.io/61559e2e1628e9411665b7e8d3d3d440a55effb3bccda79c7fe1ee02fd43fb8c-32355631649937.png)

**Não utilize links recebidos do profissional de marketing**: certifique-se de que está a utilizar os links da sua própria conta para evitar atribuições incorretas.

#### Caso especial: Redes de todas as instalações e lançamentos

Alguns não-SRNs exigem (ou permitem) que os profissionais de marketing enviem postbacks **para dispositivos que não lhes são atribuídos**.

Rede de todas as instalações

A rede aceita um postback para cada nova instalação de aplicação, de qualquer fonte

Rede de todos os lançamentos

A rede aceita um postback para cada novo lançamento de aplicação, de qualquer fonte

Alguns exemplos de redes de todas as instalações são Vungle, WeChat, Startapp, Unity Ads, e outros.

A tabela abaixo mostra a lista completa das redes de todos os lançamentos:

| Nome da rede | PID da rede (em links de atribuição da AF) |
| --- | --- |
| Supersonicads (uma rede legada da ironSource) | supersonicads\_int |
| Remarketing Adelphic | adelphicremarketing\_int |
| Grow Mobile | growmobile\_int |
| ONE by AOL | advertising.com\_int |
| Lemmonet Mobile | lemmonetmobile\_int |
| Clickky | clickky\_int |
| Remerge | remerge\_int |
| MyThings | mythings\_int |
| TikTok para Empresas | bytedanceglobal\_int |

#### Como configurar a atribuição de agência com todas as redes de instalações/lançamentos?

Trabalhar com estas redes implica enviar informações de instalações que não foram geradas pela agência. Portanto, estas redes exigem que o especialista de marketing as configure ANTES da **agência**.

> 📄 **Exemplo**
>
> Vamos usar a configuração de atribuição de agência com o Tapjoy como exemplo:
>
> 1. O especialista de marketing acede à janela de configuração do Tapjoy no painel do especialista de marketing.
> 2. O especialista de marketing introduz o ID da App do Tapjoy, fornecido ao **especialista** pelo Tapjoy, no campo de texto **app\_id**.
> 3. No separador **Integração** > Postbacks padrão, o especialista de marketing seleciona **Todas as fontes de mídia, incluindo orgânicas**.
> 4. A agência acede à janela de configuração do Tapjoy no painel da agência.
> 5. A agência introduz o ID da App do Tapjoy, fornecido à **agência** pelo Tapjoy, no campo de texto **app\_id**.

### Deep linking

Deep linking é o lançamento de uma App móvel ao abrir conteúdo personalizado e/ou enviar os utilizadores para atividades específicas dentro da App. Isto pode proporcionar uma experiência de utilizador superior e aumentar o envolvimento dos seus usuários.

Para que o deep linking funcione, a App móvel DEVE ser desenvolvida com capacidades e infraestrutura para tal. Contacte o proprietário da App para verificar se esta suporta deep linking antes de configurar as campanhas.

### Redirecionamento

* * A <Anchor target="_blank" href="/marketers/pt/docs/retargeting-attribution-guide">atribuição de retargeting</Anchor> permite que você direcione utilizadores existentes ou antigos nas suas campanhas. As campanhas de retargeting geralmente requerem capacidades de deep linking para funcionarem corretamente.

### Eventos na app

Proprietários de Apps podem ter vários eventos em suas Apps (ex.: compra, assistir a um tutorial, passar de nível, etc.), que podem ser registrados e analisados na AppsFlyer. As agências podem ver os dados dos eventos atribuídos a elas na página Eventos em suas contas.

#### Postbacks de eventos na aplicação

As agências podem receber permissão para configurar <Anchor target="_blank" href="/marketers/pt/docs/in-app-event-postback-configuration">postbacks de eventos na aplicação</Anchor> (incluindo o evento <Anchor target="_blank" href="/marketers/pt/docs/measure-sessions">af\_app\_opened</Anchor>) para redes de anúncios, após receberem permissão do profissional de marketing.

As agências podem dar permissão às redes de anúncios para configurarem postbacks in-app para si. A <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">permissão é concedida</Anchor> pelos profissionais de marketing no separador de permissões da agência.

</Accordion>

<div id="reporting-for-agencies" />

<Accordion title="Relatórios para agências">

* As estatísticas de tráfego podem ser visualizadas e descarregadas diretamente a partir do painel da AppsFlyer.
* Os relatórios são acessíveis através da página <Anchor target="_blank" href="/marketers/pt/docs/raw-data-reporting-overview">Exportar dados</Anchor> no painel da AppsFlyer. Também pode aceder aos relatórios de coorte através do <Anchor target="_blank" href="/partners/pt/docs/data-locker-reports-for-agencies">Data Locker</Anchor>.
* Os seguintes tipos de relatórios estão disponíveis:
  * Dados agregados
  * Dados brutos
* Na maioria dos casos, os profissionais de marketing e as agências não têm acesso aos mesmos dados no painel, nos relatórios, etc.
* As agências geralmente gerem apenas uma parte do tráfego do profissional de marketing, limitando assim o seu acesso aos dados, em comparação com os profissionais de marketing.
* <Anchor target="_blank" href="/marketers/pt/docs/manage-data-access-permissions">Este artigo</Anchor> explica em detalhe estas diferenças. As secções seguintes destacam estas diferenças.

> 📘 **Nota**
>
> Devido aos termos de serviço dos Meta Ads e X Ads, as **agências**, consideradas terceiros, **não têm acesso aos dados brutos de tráfego provenientes de anúncios Meta ou X Ads**.

### Acesso a dados agregados

* Os relatórios de desempenho, ou relatórios de dados agregados, estão por defeito disponíveis para as contas de agência. Leitura adicional: <Anchor target="_blank" href="/marketers/pt/docs/aggregated-and-analytics-reporting-overview">Relatórios de desempenho agregados</Anchor>
* O acesso a relatórios de dados orgânicos agregados requer a <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">permissão</Anchor> do profissional de marketing.
* As agências podem ter acesso aos relatórios de Retenção e de Coorte, bem como ao painel do Protect360. Isto exige que o profissional de marketing ative <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">**Permitir acesso aos seus relatórios de retenção e coorte**</Anchor> ou <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-agência">**Permitir acesso ao painel do Protect360**</Anchor>, respetivamente, no separador **Permissões** de **Integrações ativas**.

### Acesso a dados brutos

<Anchor target="_blank" href="/marketers/pt/docs/raw-data-reporting-overview">Os relatórios de dados brutos</Anchor> (relatórios de dados ao nível do utilizador) contêm informações de atribuição e estão organizados por tópicos.

### Fuso horário e moeda

As agências podem visualizar as aplicações com o fuso horário e a moeda definidos, mas apenas os profissionais de marketing podem alterar essas definições.

### Relatórios de custos

As agências podem ativar **Obter dados de custos** ao configurar um parceiro integrado que <Anchor target="_blank" href="/marketers/pt/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">suporte dados de custos</Anchor>.

**Para ativar a funcionalidade Obter dados de custos:**

1. Na AppsFlyer, no menu lateral, selecione **Colaborar** > **Integrações ativas**.
2. Filtre os parceiros por Custo: Na parte superior da página **Integrações ativas**, selecione **Funcionalidades suportadas** > **Custo**.
3. Selecione o parceiro. Será redirecionado para o separador **Integração**. Selecione o separador **Custo**.
4. Ative a opção **Obter dados de custo**.
5. Insira a chave API fornecida pelo parceiro.
6. Clique em **Guardar**.

#### Acesso e visualização dos dados de custo

Os dados de custo estão disponíveis para a agência nas seguintes fontes de dados:

* Página **Visão Geral**: os dados de custo são visíveis no **Relatório de Desempenho Agregado** na página Visão Geral.
* **Relatórios**: os dados de custo estão disponíveis nos relatórios exportados, como **Instalações** em **Relatórios de Dados Brutos** e **Parceiros (fontes de mídia)** em **Relatórios de Desempenho**.

### Acesso a dados de conta híbrida

As contas híbridas são contas de agência que gerem algumas aplicações como Agência (parceiro da aplicação) e outras como Profissional de Marketing (proprietário da aplicação).

As seguintes funcionalidades ao nível da conta têm disponibilidade limitada:

* <Anchor target="_blank" href="/marketers/pt/docs/custom-dashboards">Painel Personalizado</Anchor>: não disponível para agências e contas híbridas.
* Relatório de Cohorte: disponível mediante permissão do profissional de marketing.
* Protect360: disponível mediante permissão do profissional de marketing.

Se tiver uma conta híbrida, estas funcionalidades podem aparecer no seu painel, mas receberá um erro 404 ao tentar abri-las.

Se desejar utilizar essas funcionalidades, é recomendável criar uma nova conta de Profissional de Marketing e separar as suas aplicações entre Marketing e Agência. As funcionalidades mencionadas estarão disponíveis na sua conta de Marketing se as tiver ativado.

</Accordion>

<div data-zendesk-anchors="about-agency-accounts=sobre-contas-de-ag%C3%AAncia h_01HDNYNZYR2FTMQ71EV2AY3A3A=sobre-contas-de-ag%C3%AAncia agency-access-to-marketer-data=acesso-da-ag%C3%AAncia-aos-dados-de-marketing h_01HDNYNZYRZKK97GZ6R0MB9RQN=acesso-da-ag%C3%AAncia-aos-dados-de-marketing agency-access-to-ad-network-integrations=acesso-da-ag%C3%AAncia-%C3%A0s-integra%C3%A7%C3%B5es-de-redes-de-an%C3%BAncios h_01J00RYT8J0MBPHTGK5T4WEE43=acesso-da-ag%C3%AAncia-%C3%A0s-integra%C3%A7%C3%B5es-de-redes-de-an%C3%BAncios h_01HJR00RGQX0CQEHDS9BHBGJD4=observa%C3%A7%C3%A3o agency-transparency=transpar%C3%AAncia-da-ag%C3%AAncia h_01HDNYNZYRYHJ98YQWVVENZ07P=transpar%C3%AAncia-da-ag%C3%AAncia comparing-different-types-of-accounts=compara%C3%A7%C3%A3o-de-diferentes-tipos-de-contas h_01HDNYNZYR65409AGM9F2PZRC8=compara%C3%A7%C3%A3o-de-diferentes-tipos-de-contas h_01HDNYNZYS7A2H60EEAJ114VSM=agency-versus-marketer-accounts differences-between-marketer-and-agency-accounts=diferen%C3%A7as-entre-contas-de-marketing-e-de-ag%C3%AAncia h_01HDNYNZYSS7WSQ07S7KRADN7Z=diferen%C3%A7as-entre-contas-de-marketing-e-de-ag%C3%AAncia features-available-to-agencies=funcionalidades-dispon%C3%ADveis-para-ag%C3%AAncias h_01HDNYNZYSX4WPQKS0H6JN6FCP=funcionalidades-dispon%C3%ADveis-para-ag%C3%AAncias h_01HDNYNZYS8KRSPM5CPVJEJ74Y=agency-vs-ad-network-account differences-between-ad-network-and-agency-accounts=diferen%C3%A7as-entre-contas-de-rede-de-an%C3%BAncios-e-ag%C3%AAncias h_01HDNYNZYS4VPZMY34WA3SG5JT=diferen%C3%A7as-entre-contas-de-rede-de-an%C3%BAncios-e-ag%C3%AAncias agency-accounts%E2%80%94campaigns-and-reporting=contas-de-ag%C3%AAncia--campanhas-e-relat%C3%B3rios h_01HDNYNZYS32SNR5F0WKJ4G9Q1=contas-de-ag%C3%AAncia--campanhas-e-relat%C3%B3rios h_01HDNYNZYSNF2RQ3E7PM4HK433=agency-setting-up-campaigns h_01KC9MDDRPTB05PV6NCGZVFRMJ=importante selfreporting-ad-networks=redes-de-an%C3%BAncios-com-autorrelato h_01HDNYNZYS8X1VA4T46DQYQZFE=redes-de-an%C3%BAncios-com-autorrelato srn-configurations=configura%C3%A7%C3%B5es-srn h_01HDNYNZYS8AM2MFPRXFA4JXNS=configura%C3%A7%C3%B5es-srn h_01HDNYNZYSFXZXR99T6ME2R43F=exemplo nonsrns=n%C3%A3o-srns h_01HDNYNZYSN28VZQKCBRGXAVY0=n%C3%A3o-srns ad-network-configuration-visibility=visibilidade-da-configura%C3%A7%C3%A3o-de-redes-de-an%C3%BAncios h_01HDNYNZYSG5MQDDKV55HF4X9C=visibilidade-da-configura%C3%A7%C3%A3o-de-redes-de-an%C3%BAncios af_prt-parameter=par%C3%A2metro-af_prt h_01HDNYNZYSC7XNJCJ1F27KTM9Z=par%C3%A2metro-af_prt special-case-allinstalls-and-alllaunches-networks=caso-especial-redes-de-todas-as-instala%C3%A7%C3%B5es-e-lan%C3%A7amentos h_01HDNYNZYSB4MKXD47E1VHDN62=caso-especial-redes-de-todas-as-instala%C3%A7%C3%B5es-e-lan%C3%A7amentos how-to-setup-agency-attribution-with-all-installslaunches-networks=como-configurar-a-atribui%C3%A7%C3%A3o-de-ag%C3%AAncia-com-todas-as-redes-de-instala%C3%A7%C3%B5eslan%C3%A7amentos h_01HDNYNZYSHNV2B27JQV4EEVFM=como-configurar-a-atribui%C3%A7%C3%A3o-de-ag%C3%AAncia-com-todas-as-redes-de-instala%C3%A7%C3%B5eslan%C3%A7amentos h_01HDNYNZYS5WYADGW24AVK9RCZ=exemplo h_01HDNYNZYS5W0SMCF1YC6C3G4C=deep-linking retargeting=redirecionamento h_01HDNYNZYS3Z7RE51M7G7386VZ=redirecionamento inapp-events=eventos-na-app h_01HDNYNZYTDFN4MB6QBEQ8P5XW=eventos-na-app inapp-event-postbacks=postbacks-de-eventos-na-aplica%C3%A7%C3%A3o h_01HMDP38S3NPE5R4QZJ5CW404W=postbacks-de-eventos-na-aplica%C3%A7%C3%A3o h_01HDNYNZYTA767NGSTNECTBCV2=reporting-for-agencies h_01HDNYNZYTYBWGMY2PP8MPQE2F=nota access-to-performance-reports=acesso-a-dados-agregados h_01HDNYNZYTDH4S38XG3JCZQYJJ=acesso-a-dados-agregados access-to-raw-data=acesso-a-dados-brutos h_01HDNYNZYT4ZKBNGDR3QR1VTEZ=acesso-a-dados-brutos time-zone-and-currency=fuso-hor%C3%A1rio-e-moeda h_01HDNYNZYT97ET1TQHKSRDMWDC=fuso-hor%C3%A1rio-e-moeda cost-reporting=relat%C3%B3rios-de-custos h_01HDNYNZYTYT9NHMHQQ77PK8CQ=relat%C3%B3rios-de-custos accessing-and-viewing-cost-data=acesso-e-visualiza%C3%A7%C3%A3o-dos-dados-de-custo h_01HDNYNZYTWB5WVYY8C347G1ME=acesso-e-visualiza%C3%A7%C3%A3o-dos-dados-de-custo hybrid-account-data-access=acesso-a-dados-de-conta-h%C3%ADbrida h_01HDNYNZYTKZTCBSBKZEJ7M0JN=acesso-a-dados-de-conta-h%C3%ADbrida" />
