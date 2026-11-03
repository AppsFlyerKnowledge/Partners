---
title: Sinais de receita de anúncios para ad networks de UA
metadata:
  keywords:
    - Ad Network
    - Partner
    - ad revenue
    - Data Locker
    - Ad Networks
    - Partners
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-michael-talapov
    - ROI360
    - Ad Networks
  created_at: '2021-06-21T13:39:13Z'
  edited_at: '2026-08-18T00:38:00Z'
  id: 4402898251409
  locale: pt
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/pt/articles/4402898251409
---
> **Resumo:** As ad networks responsáveis pela aquisição de usuários podem receber dados de receita de anúncios e usá-los para otimizar campanhas de UA de seus clientes.

As ad networks podem receber relatórios via Data Locker com informações valiosas sobre receita de anúncios dos usuários. Esses usuários podem ter sido adquiridos por meio de campanhas veiculadas por eles ou podem ser de um canal de mídia.

As ad networks podem então ingerir esses dados em algoritmos de segmentação e otimização de campanhas e usá-los para melhorar as campanhas de ROAS com base em uma visão completa da receita gerada pela UA.

## Defina o relatório de receita de anúncios no Data Locker

As seguintes atividades precisam ser concluídas para acessar o relatório de receita de anúncios no Data Locker:

* As ad networks precisam <Anchor target="_blank" href="/partners/pt/docs/data-locker-for-partners#set-up-data-locker">integrar o Data Locker para parceiros</Anchor>.
* As ad networks precisam [configurar as configurações de saída do relatório](#configure-the-report-output-settings) e [habilitar o relatório de Receita de anúncios](#enable-the-ad-revenue-report).
* Os anunciantes precisam permitir que as ad networks visualizem o relatório. <Anchor target="_blank" href="/marketers/pt/docs/share-ad-revenue-data-with-partners#ua-signals-for-ad-networks">Veja as instruções do anunciante</Anchor>

<div id="configure-the-report-output-settings" />

<Accordion title="Defina as configurações de saída do relatório">

Para configurar a saída do relatório, siga as etapas abaixo:

1. **Na AppsFlyer, vá para** **Relatório** > Data Locker.
2. Na área **Configurações de saída do relatório,** ative **Enviar relatórios**.
3. Defina as propriedades de saída do arquivo de relatório.
   * O formato do relatório (Parqet/CSV).
   * O método de compactação do relatório (Snappy/GZIPO/Uncompressed).
   * O número máximo de linhas em um arquivo.
4. Revise o caminho esperado das saídas do arquivo de relatório. O caminho é definido de acordo com suas configurações de conexão. Para saber como configurar a conexão, consulte <Anchor target="_blank" href="/partners/pt/docs/data-locker-for-partners#set-up-data-locker">Configurar Data Locker</Anchor>.

</Accordion>

<div id="enable-the-ad-revenue-report" />

<Accordion title="Habilitar o relatório de Receita de anúncios">

1. Na seção **de conteúdo do Data Locker,** selecione o tipo de relatório **Receita de anúncios [diária]** .
2. Clique em **Salvar conexão**.
3. Certifique-se de que o anunciante permitiu que a rede de anúncios visualizasse o relatório.
4. Para obter instruções, consulte <Anchor target="_blank" href="/marketers/pt/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">Permitir que ad networks obtenham dados de receita de anúncios.</Anchor>

</Accordion>

## Especificação do relatório

<div id="report-considerations" />

<Accordion title="Estrutura e formato do relatório">

* Formato: os dados chegam no formato CSV no bucket S3 do parceiro de UA.
* Nível: contém dimensões e métricas a nível de dispositivo.
* Enriquecimento de dados: inclui dados de receita de anúncios de parceiros de mediação e adiciona dados de atribuição relevantes à ad network da UA (que são limpos de todas as dimensões irrelevantes para a ad network).
* Atualização de dados: <Anchor target="_blank" href="/marketers/pt/docs/about-data-freshness-and-timezone-support#ad-revenue">diária, ou seja, os dados do dia 0 chegam no dia 1</Anchor>. Os dados são gravados diariamente às 21:00 <Anchor target="_blank" href="/marketers/pt/docs/about-data-freshness-and-timezone-support#daily">UTC</Anchor> para h=23 do seu bucket do Data Locker.
* Aplicativos incluídos: um único relatório contém os dados de todos os aplicativos para os quais os anunciantes concederam permissão.
* Os relatórios incluem dados de todos os tipos de conversão: instalações, reatribuições, reengajamentos e reinstalações.
* Moeda: USD. A receita do evento é calculada em dólares americanos no dia em que o evento ocorreu.
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSoV1U_pMUoTFhIpyYQmUI1zQWArY19c8gMmsfpRiAaGXVZEG4WqgSC26u5-fv32j8ZQN4uxtNgVkYs/pub?output=csv">Veja um exemplo de relatório</Anchor>

</Accordion>

<div id="report-structure" />

<Accordion title="Campos do relatório">

| **Campo** | **Observações** |
| --- | --- |
| Versão | Carimbo de data/hora Unix em segundos. Exemplo: 1661315124 |
| ativado | ID do aplicativo na plataforma da AppsFlyer |
| install\_time | <ul><li>Carimbo de data e hora da instalação: AAAA-MM-DD HH:MM:SS<br />Exemplo: 2020-08-16 11:22:33</li><li>Para dispositivos iOS 14+ e usuários sem consentimento, ou se o anunciante tiver a Privacidade Avançada ativada, o horário de instalação é arredondado para a hora mais próxima.</li></ul> |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Preenchido apenas se UA for atribuído ao parceiro que recebe os dados. |
| idfa, idfv, advertising\_id | <ul><li>O mesmo ID de dispositivo, como IDFA, IDFV ou advertiser\_id, poderá ser exibido em diversas linhas se houver mais de um evento de monetização de receita publicitária.</li><li>Para dispositivos iOS 14+ e usuários sem consentimento, ou se o anunciante tiver a Privacidade Avançada ativada, isso não será exibido.</li></ul> |
| platforma | Plataforma do dispositivo: iOS, Android ou Windows Mobile |
| país | Código do país usando <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor> Exemplo: EUA, CN. |
| original\_url | <ul><li>Para dispositivos iOS 14+ e usuários sem consentimento, ou se o anunciante tiver a Privacidade Avançada ativada, isso não será exibido.</li><li>Preenchido apenas se UA for atribuído ao parceiro que recebe os dados.</li></ul> |
| ad\_unit |  |
| placement |  |
| mediation\_network |  |
| engagement\_type |  |

Métricas:

| **Campo** | **Observações** |
| --- | --- |
| impressions | Número de vezes que o usuário viu o anúncio |
| receita\_usd | Receita diária (em USD) gerada para o ID do dispositivo. **Atenção:** quando o valor da receita é pequeno, ele é representado em notação científica. Por exemplo: 8.00E-05 |

</Accordion>

<div data-zendesk-anchors="set-the-ad-revenue-report-in-data-locker=defina-o-relat%C3%B3rio-de-receita-de-an%C3%BAncios-no-data-locker h_01H8Y7ABGVR7BNHEYVFKPFM4JN=defina-o-relat%C3%B3rio-de-receita-de-an%C3%BAncios-no-data-locker h_01H8Y7ABGV2T6GBE9BHJQM6FDF=configure-the-report-output-settings h_01H8Y7ABGVW6Y5RY7CVNM3EJZR=enable-the-ad-revenue-report report-specification=especifica%C3%A7%C3%A3o-do-relat%C3%B3rio h_01H8Y7ABGVXJ9ZQCJ8BR0DST6W=especifica%C3%A7%C3%A3o-do-relat%C3%B3rio h_01H8Y7ABGV0G4GJBRKKGNBSEC5=report-considerations h_01H8Y7ABGV81X0VFWTRMXGHYSA=report-structure" />
