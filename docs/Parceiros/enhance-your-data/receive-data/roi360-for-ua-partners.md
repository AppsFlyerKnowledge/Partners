---
title: ROI360 para parceiros UA
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
  created_at: '2023-08-12T17:09:08Z'
  edited_at: '2026-08-18T00:39:25Z'
  id: 17735150011921
  locale: pt
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/pt/articles/17735150011921
---
> **Visão geral:** a AppsFlyer fornece aos parceiros de UA anúncios completos e precisos, compras in-app e dados de assinatura renováveis automaticamente por meio de relatórios e postbacks. Os parceiros podem ingerir as informações para otimizar as campanhas de UA.

<div id="introduction" />

## Introdução

A AppsFlyer recebe informações de receitas de seus parceiros e das lojas de aplicativos (Apple App Store e Google Play Store). Depois de recebidos, os dados passam por uma série de etapas, incluindo validação, normalização, atribuição e enriquecimento com propriedades e dimensões adicionais.   A AppsFlyer pode enviar as informações ao parceiro de UA. Após esse processo, a AppsFlyer transmite os dados enriquecidos e atribuídos ao parceiro de UA. O parceiro de UA pode então utilizar essas informações para otimizar suas campanhas de aquisição de usuários e aprimorar o serviço que oferece aos anunciantes.

<div id="what-revenue-types-are-reported-to-the-partners" />

<Accordion title="Que tipos de receitas são reportados aos parceiros?">

Os aplicativos criam dois tipos de receita:

* **Receita publicitária:** a receita publicitária é gerada sempre que um anúncio é exibido no aplicativo, como em banners, anúncios intersticiais e outros formatos. Pode ser calculado independentemente do método de campanha pelo qual o anunciante é cobrado.
* **Compra in-app e assinatura com renovação automática:** a receita da loja é gerada sempre que uma compra in-app ou transação relacionada à assinatura é realizada.

</Accordion>

<div id="how-does-appsflyer-provide-revenue-signals-to-ua-partners" />

<Accordion title="Como a AppsFlyer fornece sinais de receita aos parceiros de UA?">

A AppsFlyer fornece aos parceiros informações sobre anúncios in-app, compras in-app e receita de assinaturas através dos seguintes meios:

* **Relatório de sinais de UA de receita publicitária**: o relatório lista eventos de receita de anúncios agregados ao nível do dispositivo. O relatório está disponível diariamente no Data Locker e contém os dados do dia anterior.
* **Postbacks de receita publicitária**: sempre que ocorre uma impressão de anúncio em um dispositivo do cliente, um postback é enviado da AppsFlyer para o parceiro contendo os detalhes do evento de receita publicitária.
* **Postbacks de receita da loja**: sempre que ocorre um evento de compra ou assinatura, um postback é enviado da AppsFlyer para o parceiro contendo os detalhes do evento de receita.

</Accordion>

<div id="set-up-roi360-for-partners" />

## Configure o ROI360 para parceiros

Quais ações os parceiros precisam realizar para receber o relatório de sinais de UA e os postbacks de receita publicitária e receita da loja?

<div id="how-to-subscribe-to-the-roi360-ua-signals-report" />

<Accordion title="Como assinar o relatório UA Signals do ROI360">

Para permitir que o parceiro obtenha o relatório por meio do Data Locker:

* O parceiro deve realizar as seguintes etapas no Data Locker:
  1. <Anchor target="_blank" href="/partners/pt/docs/data-locker-for-partners#set-up-data-locker">Configurar o Data Locker</Anchor> na conta do parceiro, incluindo a conexão com o provedor de serviços em nuvem e o formato e conteúdo dos relatórios.
  2. <Anchor target="_blank" href="/partners/pt/docs/ad-revenue-signals-for-ua-ad-networks#enable-the-ad-revenue-report">Ativar o relatório UA Signals do ROI360</Anchor>.
* O anunciante deve <Anchor target="_blank" href="/marketers/pt/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">conceder permissão ao parceiro para o relatório</Anchor>.

</Accordion>

<div id="how-to-receive-roi360-postbacks-from-appsflyer" />

<Accordion title="Como receber postbacks do ROI360 da AppsFlyer">

Para receber postbacks da AppsFlyer, os parceiros devem iniciar uma conversa com a equipe de integração de parceiros da AppsFlyer. Depois, a equipe configurará os valores de postback de receita no aplicativo de ROI na plataforma da AppsFlyer.

Para entrar em contato com o suporte ao parceiro AppsFlyer, abra o menu **Ajuda** no seu painel e selecione **Entre em contato com nossa equipe**.

<Image align="center" alt="alt" src="https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif" />

</Accordion>

<div id="roi360-ua-signals-report-for-ua-networks" />

## Relatório UA Signals do ROI360 para redes de UA

O relatório fornece registros de receita CSV/parquet completos e precisos do dia x+1 para o bucket S3 do parceiro de UA diariamente. Cada registro é uma agregação de eventos de receita publicitária no nível do dispositivo.

O relatório UA Signals não fornece dados em tempo real como fazem os postbacks de receita publicitária. No entanto, ele é mais preciso e completo. Isso ocorre porque o valor de uma impressão pode mudar com o tempo. Isso é especialmente verdadeiro quando os dados de receita no nível da impressão referem-se a uma impressão de anúncio que foi vendida por meio de lances de CPM padrão, em vez de lances em tempo real.

<div id="what-are-the-report-data-sources" />

<Accordion title="Quais são as fontes de dados do relatório?">

Dependendo do tipo de integração do anunciante, os dados do relatório podem ser provenientes de:

1. Integrações do <Anchor target="_blank" href="/marketers/pt/docs/integrate-the-roi360-ad-revenue-sdk-api">conector do SDK do AdRevenue</Anchor>: os clientes podem compartilhar dados de receita em nível de impressão carregados pelo parceiro para os dispositivos do cliente e, em seguida, reportados à AppsFlyer quase em tempo real.
2. Integrações em nível de dispositivo baseadas na API S2S: os clientes podem configurar suas credenciais de parceiro na UI da AppsFlyer em parceiros integrados e permitir que a receita publicitária do ROI360 colete dados de receita publicitária em seu nome.
3. Uma combinação dos dois (Atualização para Precisão). **Observação:** a transferência de dados do anunciante para a AppsFlyer depende das permissões do anunciante e do fato de o anunciante ser um cliente ROI360 avançado.

</Accordion>

<div id="what-data-processing-is-performed-on-the-report-data" />

<Accordion title="Qual processamento de dados é realizado nos dados do relatório?">

A receita publicitária do ROI360 da AppsFlyer realiza o seguinte:

1. Normalização de dados
2. Atribuição à fonte de mídia de instalação e enriquecimento de dados
3. Geração de eventos de receita publicitária
4. Os eventos são agregados no nível do dispositivo

</Accordion>

<div id="how-is-the-report-data-delivered" />

<Accordion title="Como os dados do relatório são entregues?">

Os dados no nível do dispositivo são gravados diariamente no relatório no Data Locker

</Accordion>

<div id="what-is-the-report-data-freshness" />

<Accordion title="Qual é a atualização dos dados do relatório?">

Os dados são gravados diariamente na pasta h=23 do seu bucket do Data Locker às 21h, <Anchor target="_blank" href="/marketers/pt/docs/about-data-freshness-and-timezone-support#daily">horário UTC</Anchor>.

</Accordion>

<div id="what-are-the-report-fields" />

<Accordion title="Quais são os campos do relatório?">

| **Campo** | **Observações** |
| --- | --- |
| Versão | Carimbo de data/hora Unix em segundos. Exemplo: 1661315124 |
| ativado | ID do aplicativo na plataforma da AppsFlyer |
| install\_time | • Data e hora da instalação: AAAA-MM-DD HH:MM:SSExemplo: 2020-08-16 11:22:33 • Para dispositivos iOS 14+ e usuários sem consentimento, ou se o anunciante tiver a Privacidade Avançada ativada, o horário de instalação é arredondado para a hora mais próxima. |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Preenchido apenas se UA for atribuído ao parceiro que recebe os dados. |
| idfa, idfv, advertising\_id | • O mesmo ID de dispositivo, como IDFA, IDFV ou advertiser\_id, poderá ser exibido em diversas linhas se houver mais de um evento de monetização de receita publicitária. • Para dispositivos iOS 14+ e usuários sem consentimento, ou se o anunciante tiver a Privacidade Avançada ativada, isso não será exibido. |
| platforma | Plataforma do dispositivo: iOS, Android ou Windows Mobile |
| país | Código do país usando [ISO 3166 (alfa-2)](https://www.iso.org/iso-3166-country-codes.html) Exemplo: EUA, CN |
| original\_url | • Para dispositivos iOS 14+ e usuários sem consentimento, ou se o anunciante tiver a Privacidade Avançada ativada, isso não será exibido. • Preenchido apenas se UA for atribuído ao parceiro que recebe os dados. |
| mediation\_network | A rede de mediação associada à impressão ou impressões. <Anchor target="_blank" href="/marketers/pt/docs/roi360-guide-ad-revenue-attribution#%5Bclosed-beta%5D-ua-signals-for-ad-networks">Veja lista de redes possíveis</Anchor> |
| ad\_unit | No terceiro trimestre de 2023: o bloco de anúncios de monetização associado à impressão ou impressões |
| posicionamento | No terceiro trimestre de 2023: o canal de monetização associado à impressão ou impressões |

</Accordion>

<div id="download-the-report-data-sample" />

<Accordion title="Faça download da amostra de dados do relatório">

[Clique para fazer download do relatório](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv)

</Accordion>

<div id="in-app-ad-revenue-iaa-postbacks" />

## Postbacks de receita publicitária in-app (IAA)

Postbacks IAA são a segunda abordagem de ingestão que a AppsFlyer usa para enviar informações de receita aos parceiros. Sua principal vantagem sobre o relatório de sinais de receita de anúncios de UA é sua atualização, já que os postbacks oferecem compartilhamento de dados de receita IAA quase em tempo real. Isso contrasta com a atualização X+1 (um dia após a data de ocorrência do evento) oferecida por meio do relatório de sinais de UA de receita publicitária.

No entanto, a atualização em tempo real é menos precisa em comparação com X+1:

* Os dados de postbacks IAA em tempo real são ±5% menos precisos, em média, do que os dados X+1 do relatório de sinais de UA.
* Os dados de postbacks IAA em tempo real são ±7% menos completos, em média, do que os dados X+1 do relatório de sinais de UA.

<div id="what-are-the-iaa-postback-data-sources" />

<Accordion title="Quais são as fontes de dados de postback IAA?">

Os dados para o postback IAA se originam de dados em nível de impressão que os parceiros carregam nos dispositivos do cliente. Esses dados são então compartilhados com a AppsFlyer por meio do conector do SDK Receita publicitária do ROI360, que é instalado no dispositivo pelo anunciante. O conector permite que o desenvolvedor do aplicativo relate um evento de impressão, incluindo determinados parâmetros como o ILRD, a moeda, a plataforma de mediação e a fonte de monetização.

A transferência de dados dos dispositivos clientes do anunciante para a AppsFlyer está sujeita às permissões do anunciante e ao fato de o anunciante ser um cliente ROI360 avançado.

</Accordion>

<div id="what-processing-is-performed-on-the-iaa-postback-data" />

<Accordion title="Qual processamento é executado nos dados de postback IAA?">

O ROI360 da AppsFlyer executa as seguintes etapas para cada dado de nível de impressão recebido:

1. Normalização de dados.
2. Atribuição à fonte de mídia de instalação e enriquecimento de dados.
3. Geração de um evento **af\_ad\_revenue**.

</Accordion>

<div id="how-is-the-postback-data-delivered" />

<Accordion title="Como os dados de postback são entregues?">

O evento é enviado ao parceiro por meio de uma configuração de postback existente entre o parceiro e a AppsFlyer como parâmetro adicional.

</Accordion>

<div id="in-app-purchase-iap-postbacks" />

## Postbacks de compra in-app (IAP)

Os postbacks de compras in-app do ROI360 oferecem várias camadas de precisão de relatórios, primeiro validando cada transação, desduplicando-a e, em seguida, deduzindo a comissão da loja e o imposto sobre vendas.

<div id="what-are-the-iap-postback-data-sources" />

<Accordion title="Quais são as fontes de dados de postback do IAP?">

Os dados para o postback do IAP são originados de:

1. Dados em nível de transação lidos pelo conector ROI360 Purchase SDK sempre que ocorre uma compra in-app ou um evento de assinatura renovável automaticamente no dispositivo.
2. Quaisquer **notificações recebidas do servidor da App Store e do Google Play (RTDN)** também são processadas pela lógica de negócios de compra e receita de assinatura da AppsFlyer:

   * As notificações sobre transações relatadas anteriormente por meio do conector do SDK são validadas e processadas.
   * Notificações sobre transações desconhecidas não são informadas na AppsFlyer

   **Observação:** a transferência de dados do anunciante para a AppsFlyer depende das permissões do anunciante e do fato de o anunciante ser um cliente ROI360 avançado.

</Accordion>

<div id="what-data-processing-is-performed-on-the-iap-postback-data" />

<Accordion title="Qual processamento de dados é executado nos dados de postback do IAP?">

O ROI360 da AppsFlyer executa as seguintes etapas para cada dado recebido em nível de transação:

1. A AppsFlyer **valida a compra ou assinatura com a loja relevante** para garantir que não seja fraudulenta.
   * Após a validação bem-sucedida, a AppsFlyer registra a compra ou assinatura.
   * Se a validação do recibo falhar, o evento será exibido no relatório de dados brutos de eventos in-app bloqueados (disponível para assinantes do Protect360).
2. A AppsFlyer garante que as transações não sejam duplicadas, incluindo aquelas relacionadas ao compartilhamento familiar no iOS.
3. A AppsFlyer calcula os dados da receita líquida levando em consideração comissões e impostos da loja (**Receita verdadeira**).
4. A AppsFlyer gera uma compra interna ou um evento de ciclo de vida para a transação validada e processada.

</Accordion>

<div id="how-is-the-postback-delivered" />

<Accordion title="Como o postback é entregue?">

O evento IAP é enviado ao parceiro por meio de uma integração de postbacks existente entre o parceiro e a AppsFlyer.

</Accordion>

<div id="what-are-the-iap-events" />

<Accordion title="Quais são os eventos IAP?">

Os clientes do ROI360 podem compartilhar os seguintes nomes de eventos geradores de receita:

**Nomes de eventos**

| **Nome do evento** | **Descrição** |
| --- | --- |
| af\_compra | Registrado quando um usuário faz uma compra |
| af\_purchase\_refund | Registrado quando uma compra é reembolsada |
| af\_ars\_trial\_converted | Registrado quando uma renovação com preço integral começa, após um período de avaliação |
| af\_ars\_subscription\_started | Registrado quando uma assinatura com desconto ou com preço integral começa |
| af\_ars\_subscription\_resumed | Registrado quando uma assinatura com preço integral é retomada após uma assinatura cancelada ou reembolsada |
| af\_ars\_subscription\_refunded | Registrado quando um assinante recebe um reembolso |
| af\_ars\_subscription\_renewed | Registrado quando ocorre uma assinatura de renovação automática |
| af\_ars\_subscription\_xgraded | Registrado quando um assinante faz upgrade, downgrade ou upgrade cruzado para um produto diferente |

</Accordion>

<div data-zendesk-anchors="introduction=introdu%C3%A7%C3%A3o 01H7T1DS6SNC7X8GX4DGXT4GC0=introdu%C3%A7%C3%A3o 01H7T1DS6TYHE3A4XWBDNHCFCZ=what-revenue-types-are-reported-to-the-partners 01H7T1DS6T82RWQ4BBWNPQ6BT2=how-does-appsflyer-provide-revenue-signals-to-ua-partners set-up-roi360-for-partners=configure-o-roi360-para-parceiros 01H7T1DS6TDA8CX1ZF3GGE4EHB=configure-o-roi360-para-parceiros 01H7T1DS6T0QFB6K6R78PMVVB2=how-to-subscribe-to-the-roi360-ua-signals-report 01H7T1DS6TBNJBBR6M98RTVMFF=how-to-receive-roi360-postbacks-from-appsflyer roi360-ua-signals-report-for-ua-networks=relat%C3%B3rio-ua-signals-do-roi360-para-redes-de-ua 01H7T1DS6T93844DMZY744ECQE=relat%C3%B3rio-ua-signals-do-roi360-para-redes-de-ua 01H7T1DS6T4AF6GTETE6HZMYF7=what-are-the-report-data-sources 01H7T1DS6TDNTYDY4JF70F40SV=what-data-processing-is-performed-on-the-report-data 01H7T1DS6T94V4674AMNVCD4T6=how-is-the-report-data-delivered 01H7T1DS6T4F0QV5VE8XZVV1RY=what-is-the-report-data-freshness 01H7T1DS6TYER08FGK9GDKHFEG=what-are-the-report-fields 01H7T1DS6TH98NT4KGKPR7DRDM=download-the-report-data-sample inapp-ad-revenue-iaa-postbacks=postbacks-de-receita-publicit%C3%A1ria-in-app-iaa 01H7T1DS6T0CN30EC97VARN80D=postbacks-de-receita-publicit%C3%A1ria-in-app-iaa 01H7T1DS6TCA8338NAD9Q8CJWW=what-are-the-iaa-postback-data-sources 01H7T1DS6TQ2G43HSQMH8Y6Q4H=what-processing-is-performed-on-the-iaa-postback-data 01H7T1DS6TQZA3W9KE3783G9G1=how-is-the-postback-data-delivered inapp-purchase-iap-postbacks=postbacks-de-compra-in-app-iap 01H7T1DS6TH8AV2ZTY3M8ZXPYA=postbacks-de-compra-in-app-iap 01H7T1DS6TGF4XEMD4CRBD8QS2=what-are-the-iap-postback-data-sources 01H7T1DS6T9W85F40QQ2497RNW=what-data-processing-is-performed-on-the-iap-postback-data 01H7T1DS6VAPRMCGZ9YCPTA9EQ=how-is-the-postback-delivered 01H7T1DS6VKE2G6XR02VF4TWH4=what-are-the-iap-events" />
