---
title: Relatório de performance agregada de campanhas para ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketing Analytics
    - Ad Networks
  created_at: '2021-05-30T12:34:03Z'
  edited_at: '2026-08-19T00:36:21Z'
  id: 360020834237
  locale: pt
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/pt/articles/360020834237
---
> **Visão geral**: Visão geral: as ad networks carregam o relatório de performance agregada (também conhecido como relatório de cohort) em seus sistemas de BI para calcular as métricas de performance da campanha, como o KPI de retenção de 7 dias.

<div id="aggregated-campaign-performance-report" />

## Relatório de performance agregada

Esse relatório oferece dados sobre a performance da campanha, incluindo o número de usuários exclusivos que realizam um determinado evento. Você (a ad network) usa os dados em seus sistemas de BI para calcular métricas de performance da campanha no contexto dos KPIs dos anunciantes. O relatório está disponível diariamente através do <Anchor target="_blank" href="/partners/pt/docs/data-locker-for-partners">Data Locker para Parceiros</Anchor>

**Por que você precisa desse relatório?**

Antes do iOS 14.5, os postbacks enviados pela AppsFlyer continham dados suficientes para calcular métricas exclusivas de eventos do usuário.

A partir do iOS 14.5, e da adoção do anunciante da Privacidade Avançada Agregada (Aggregated Advanced Privacy, AAP), postbacks de usuários que não consentem não incluem identificadores de usuário. A falta de identificadores impede o cálculo de métricas exclusivas do usuário como, por exemplo, a retenção de 7 dias. A falta de métricas de usuários exclusivos prejudica sua capacidade de otimizar campanhas e de definir metas de retenção comuns com os anunciantes.

**O que o relatório contém?**

As métricas são fornecidas com a melhor granularidade possível usando as dimensões relatadas e têm as seguintes métricas de performance:

* Resultados
* Número de vezes que um determinado evento é executado
* Número de usuários únicos que realizam um evento
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vS89RlkFIss7uARroJcOcX1rU6gUmZ2ySYwfTprg9GaA2BYnvDPVqWmOicea1wrBnNuGgEuLPwzL_ac/pub?gid=0&single=true&output=csv">Exemplo de relatório</Anchor>

**Como você obtém o relatório?**

* Oferecido através do Data Locker para Parceiros. O relatório é atualizado <Anchor target="_blank" href="/marketers/pt/docs/about-data-freshness-and-timezone-support#daily">Diariamente em horário UTC</Anchor>.
* Antes de começarmos a compartilhar os dados com você, os anunciantes devem [conceder permissões](/docs/aggregated-campaign-performance-report-for-ad-networks#permission-to-get-aggregated-performance-data) no painel.

<div id="about-the-report" />

## Sobre o relatório

<div id="report-structure" />

<Accordion title="Estrutura do relatório">

<div id="dimensions" />

#### Dimensões

<Table>
  <thead>
    <tr>
      <th>
        Nome do campo
      </th>
      <th>
        Observações
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        conjunto\_de\_anúncios
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        fonte\_de\_mídia
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        tipo\_de\_conversão
      </td>
      <td>
        * Valores possíveis: instalação, reengajamento, reatribuição
        * Macro de postback equivalente: is\_retargeting
      </td>
    </tr>
    <tr>
      <td>
        tipo\_de\_toque\_atribuído
      </td>
      <td>
        Valores possíveis: clique, impressões, pré-instalação, desconhecido, tv, nulo
      </td>
    </tr>
    <tr>
      <td>
        dias\_após\_atribuição
      </td>
      <td>
        O número de dias decorridos desde o evento de atribuição.  
        O número máximo de dias é 180.

        Dica! Use isso para calcular os dias de retenção e de KPI.
      </td>
    </tr>
    <tr>
      <td>
        event\_date
      </td>
      <td>
        A hora em que o evento ocorreu

        Formato: aaaa-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        data\_da\_conversão
      </td>
      <td>
        Formato: aaaa-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        nome\_do\_evento
      </td>
      <td>
        Identifica o evento. Alguns nomes de eventos têm um significado específico, enquanto outros se relacionam com eventos in-app definidos pelo anunciante no aplicativo.

        | nome\_do\_evento | O que o utilizador fez |
        | --- | --- |
        | af\_conversion | Usuário convertido. Use conversion\_type para identificar se é uma instalação, reengajamento ou reatribuição. |
        | af\_sessions | Abriu a app |
        | af\_uninstall | Desinstalou a app |
        | Evento na app definido pelo anunciante | Realizou um evento in-app. Os nomes de eventos in-app não são mapeados para nomes de eventos de parceiros. |
      </td>
    </tr>
    <tr>
      <td>
        campanha
      </td>
      <td>
        Hierarquia da campanha
      </td>
    </tr>
    <tr>
      <td>
        id\_da\_campanha
      </td>
      <td>
        Hierarquia da campanha
      </td>
    </tr>
    <tr>
      <td>
        conjunto\_de\_anúncios
      </td>
      <td>
        Hierarquia da campanha
      </td>
    </tr>
    <tr>
      <td>
        id\_conjunto\_de\_anúncios
      </td>
      <td>
        Hierarquia da campanha
      </td>
    </tr>
    <tr>
      <td>
        anúncio
      </td>
      <td>
        Hierarquia da campanha
      </td>
    </tr>
    <tr>
      <td>
        id\_anúncio
      </td>
      <td>
        Hierarquia da campanha
      </td>
    </tr>
    <tr>
      <td>
        canal
      </td>
      <td>
        Hierarquia da campanha
      </td>
    </tr>
    <tr>
      <td>
        id\_do\_site
      </td>
      <td>
        Hierarquia da campanha
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        Use para identificar e deduplicar dados de retargeting
      </td>
    </tr>
    <tr>
      <td>
        código\_país
      </td>
      <td>
        Derivado do endereço de IP do usuário
      </td>
    </tr>
    <tr>
      <td>
        agência
      </td>
      <td>
        Se estiver em branco, não há agência associada
      </td>
    </tr>
    <tr>
      <td>
        Palavras-chave
      </td>
      <td>
        [Disponível a partir de 27 de abril de 2022] Palavra(s) usadas na pesquisa online do usuário. Conforme relatado pela ad network.
      </td>
    </tr>
    <tr>
      <td>
        ID da palavra-chave
      </td>
      <td>
        [Disponível a partir de 27 de abril de 2022] ID de palavra-chave retornado pela ad network.
      </td>
    </tr>
  </tbody>
</Table>

<div id="metrics" />

#### Métricas

| Nome | Campo | Usuários únicos que executam o evento |
| --- | --- | --- |
| Utilizadores únicos | utilizadores\_únicos | Número de usuários únicos que executam o evento |
| Resultados | receita\_usd | Receita cumulativa em USD. Por exemplo, 100,00 dólares são refletidos como 100. |
| contagem\_de\_eventos | contagem\_de\_eventos | Número de ocorrências de eventos |

</Accordion>

<div id="bi-developer-considerations" />

<Accordion title="Considerações para o desenvolvedor de BI">

**Âmbito dos dados no relatório**

O relatório contém atribuições, instalações, reatribuições e reengajamentos do usuário e seus eventos in-app relacionados.

No processo de consumo de dados, você deve usar a lógica para dividir os dados entre tipos de campanha. Significado, atribuição do usuário (instalações) e retargeting (reengajamentos). Para isso, use o campo conversion\_type e is\_primary\_attribution. Consulte <Anchor target="_blank" href="/marketers/pt/docs/resolve-retargeting-double-attribution">Atribuição dupla de eventos de retargeting.</Anchor>

**Considerações ao nível do campo**

* Utilize os dias pós-atribuição para facilitar a análise das métricas de retenção.
* Cálculo de utilizadores únicos usando as dimensões de nome de campanha e ID de campanha: Se puder desconsiderar a granularidade do nome da campanha, pode somar a contagem única no ID da campanha, e as métricas estarão corretas.
* Pode agregar os dados utilizando os campos da hierarquia da campanha.
* Os eventos in-app usam o nome do evento do anunciante e não são mapeados para os nomes de eventos. Peça ao anunciante que forneça os mapeamentos ou os visualize no dashboard. <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">Mapeamento de eventos in-app de parceiros</Anchor>.
* A receita está em USD e é calculada usando a taxa de câmbio no dia do evento.
* Eventos de receita de anúncios são incluídos quando disponíveis, mas são atualizados com um atraso de até 5 dias.

**Considerações gerais**

* Atualização dos dados: diariamente, a partir das 08:00 UTC. Atualização de dados: Os dados são registrados na pasta Data Locker h=23.
* Os dados disponíveis são dados de atribuição de jornada do usuário atribuídos pela AppsFlyer. Ou seja, dados de SKAdNetwork reportados por postbacks do iOS não estão incluídos neste conjunto de dados.
* Os dados estão contidos em arquivos que contêm vários aplicativos. Use o campo app\_id para identificar o aplicativo.
* Se você não receber os dados de um determinado aplicativo, verifique se o anunciante lhe concedeu as permissões necessárias.

</Accordion>

<div id="retention-report-considerations" />

<Accordion title="Considerações sobre relatórios de retenção">

Para criar métricas de retenção, por exemplo, dia 7 da retenção, faça isso definindo filtros nos seguintes campos:

* days\_post\_install=7
* event\_name=af\_session
* conversion\_type conforme necessário
* Para evitar a inclusão de <Anchor target="_blank" href="/marketers/pt/docs/resolve-retargeting-double-attribution">eventos de retargeting duplicados</Anchor>, selecione is\_primary\_attribution=true ou use conversion\_type para limitar o conjunto de dados às instalações.
* Agrupar por: campanha e outras dimensões, conforme necessário.
* Soma: unique\_users\_count

Ao adicionar ou remover dimensões, você pode obter métricas com granularidades diferentes.

</Accordion>

<div id="permissions" />

## Authorization: Bearer

Você (a ad network) deve pedir ao anunciante que lhe dê as permissões listadas aqui. O anunciante deve executar esse procedimento uma vez por aplicativo.

<div id="permission-to-get-aggregated-performance-data" />

<Accordion title="Permissão para obter dados de performance agregada">

Ad networks indicadas (ativadas) por agências: A agência não pode conceder permissão. A agência deve pedir ao anunciante que dê as permissões para ela.

**Para permitir que a ad network receba dados de performance agregada:**

1. Na AppsFlyer, no menu lateral, selecione **Colaborar** > Parceiros integrados.
2. Procure e selecione o parceiro.
3. Clique em **configurar integração**. Você será direcionado para a página de configuração da integração.
4. Verifique se a opção **Ativar parceiro** está habilitada. Caso contrário, os dados não serão compartilhados.
5. Acesse a aba de **Permissões**.
6. Ative as seguintes permissões da ad network.
   * **Acessar dados agregados de conversões**.
   * **Acessar dados agregados de eventos in-app**.
   * **Acessar dados agregados de receita**.
7. Clique em **Salvar permissões**.
8. Notifique a ad network para a qual você concedeu as permissões.
9. Se você tiver vários aplicativos, repita o procedimento para cada aplicativo integrado ao parceiro.

</Accordion>

<div data-zendesk-anchors="aggregated-campaign-performance-report=relat%C3%B3rio-de-performance-agregada h_01HM8SQ5RE1FGQDY6V1A8MMEQX=relat%C3%B3rio-de-performance-agregada about-the-report=sobre-o-relat%C3%B3rio h_01HM8SQ5REM6MW5GBRSXTF0N73=sobre-o-relat%C3%B3rio h_01HM8SQ5RETK7HCPZGGX8KX9VG=report-structure dimensions=dimens%C3%B5es h_01HM8SQ5RE11PW6HGTWGC2AGR5=dimens%C3%B5es metrics=m%C3%A9tricas h_01HM8SQ5RGQEH6G6W75FVWJKSP=m%C3%A9tricas h_01HM8SQ5RGCGTWTSRHB8B4FSY2=bi-developer-considerations h_01HM8SQ5RG4JEE75F6CBTFCBB5=retention-report-considerations permissions=authorization-bearer h_01HM8SQ5RGNXENZ89GD74KJWH2=authorization-bearer h_01HM8SQ5RGQADHTEP5ED3W87VZ=permission-to-get-aggregated-performance-data" />
