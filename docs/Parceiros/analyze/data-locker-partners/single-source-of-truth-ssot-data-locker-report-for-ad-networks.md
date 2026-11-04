---
title: Relatório Single Source of Truth (SSOT) no Data Locker para ad networks
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2024-07-31T19:51:34Z'
  edited_at: '2026-08-19T00:36:42Z'
  id: 27168206416017
  locale: pt
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/pt/articles/27168206416017
---
> **Resumo:** O relatório Single Source of Truth (SSOT) no Data Locker oferece uma visão geral unificada e precisa da performance da campanha de aplicativos mesclando dados de vários métodos de atribuição, como ID matching e SKAN.  Ele fornece uma maneira de carregar dados em seus sistemas de BI para melhorar a precisão dos dados.

<div id="note" />

> 📘 **Atenção**
>
> * Antes de começarmos a compartilhar os dados com você, os anunciantes devem [conceder permissões](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions) no dashboard.
> * O relatório do SSOT no Data Locker contém dados baseados em LTV, não dados baseados em atividade. Isso significa que os dados refletem o valor vitalício dos usuários em todos os pontos de contato, em vez de sua atividade no aplicativo ou eventos.

<div id="what-is-data-locker" />

## O que é Data Locker

O Data Locker é uma solução segura que fornece dados diretamente para as principais plataformas de nuvem, como AWS, GCS e Snowflake. Isso permite que você integre e consuma dados facilmente em seus sistemas internos de BI para análise e relatórios abrangentes. <Anchor target="_blank" href="/partners/pt/docs/data-locker-for-partners">Saiba mais</Anchor>.

<div id="what-is-single-source-of-truth-ssot" />

## O que é Single Source of Truth (SSOT)

A solução de Single Source of Truth, (SSOT) tem o objetivo de resolver problemas com a fragmentação de dados oferecendo uma visão geral unificada e precisa do desempenho da campanha de aplicativos mesclando dados de vários métodos de atribuição, como ID matching e SKAN. <Anchor target="_blank" href="/marketers/pt/docs/single-source-of-truth-ssot-guide-for-ios-attribution">Saiba mais</Anchor>.

<div id="benefits-of-ssot-reports-in-data-locker" />

## Vantagens dos relatórios de SSOT no Data Locker

O relatório SSOT oferece o mesmo nível de visibilidade que os profissionais de marketing usam para analisar e mensurar sua performance.

* **Tenha uma visualização de atribuição precisa e completa:** O SSOT lida com a lógica de mesclar dados de diferentes métodos de atribuição, impedindo efetivamente a contagem dupla de instalações atribuídas por vários métodos de atribuição. Isso garante que os dados sejam precisos e reflitam o verdadeiro comportamento e atribuição do usuário.
* **Carregue dados em seus sistemas de BI:** O SSOT fornece uma maneira eficiente e precisa de carregar os dados agregados em seus sistemas internos de BI. Isso inclui atribuições, eventos in-app e dados de receita, abrangendo todas as dimensões e métricas.

<div id="setting-up-data-locker" />

<Accordion title="Configurando o Data Locker">

Siga esse procedimento para configurar o Data Locker. As alterações nas configurações entram em vigor dentro de 3 horas.

**Pré-requisito:**

Complete um ou mais dos seguintes procedimentos de armazenamento:

* Bucket da <Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor>
* Bucket do <Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor>
* [Beta] <Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor> bucket
* <Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor> data warehouse

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Para configurar o Data Locker:**

1. Faça login no seu dashboard  <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">de parceiro da AppsFlyer.</Anchor>
2. Vá para:
   * **Anunciantes:Relatório**>**Data Locker**.
   * **Parceiros de marketing**: Clique no botão **Menu da conta** > **Data Locker**.
3. Siga as instruções <Anchor target="_blank" href="/marketers/pt/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">de configuração do Data Locker,</Anchor> etapas 3-16.

</Accordion>

<div id="permissions" />

<Accordion title="Authorization: Bearer">

Ad networks indicadas (ativadas) por agências: A agência não pode conceder permissão. A agência deve pedir ao anunciante que dê as permissões para ela.

**Para permitir que a ad network obtenha dados do Single Source of Truth, ou SSOT:**

1. Na AppsFlyer, no menu lateral, selecione **Colaborar** > **Parceiros integrados**.
2. Procure e selecione o parceiro.
3. Clique em **configurar integração**. Você será direcionado para a página de configuração da integração.
4. Verifique se a opção **Ativar parceiro** está habilitada. Caso contrário, os dados não serão compartilhados.
5. Vá para aba **Permissões.**
6. Ative as seguintes permissões da ad network.
   * **Acessar dados agregados de conversões**.
   * **Acessar dados agregados de eventos in-app**.
   * **Acessar dados agregados de receita**.
7. Clique em **Salvar permissões**.
8. Notifique a ad network para a qual você concedeu as permissões.
9. Se você tiver vários aplicativos, repita o procedimento para cada aplicativo integrado ao parceiro.

</Accordion>

<div id="ssot-report-facts" />

<Accordion title="Fatos do relatório SSOT">

| Nome | Descrição |
| --- | --- |
| Relatórios disponíveis | Os seguintes relatórios estão disponíveis:<ul><li>Aquisição de usuários: atribui conversões para canais de aquisição de usuários. Isso inclui a atividade pós-instalação que ocorre durante as janelas de reengajamento.</li><li>Retargeting: atribui conversões a canais de retargeting para eventos que ocorrem:<ul><li>Como resultado de reatribuições</li><li>Durante uma janela de reengajamento</li></ul></li><li>Unificado: atribui as conversões ao canal de último toque, de acordo com as regras de <Anchor target="_blank" href="/marketers/pt/docs/resolve-retargeting-double-attribution">Dupla atribuição</Anchor> da AppsFlyer. Isso significa que a atividade pós-instalação que ocorre durante os reengajamentos é exibido sob o canal de mídia de retargeting e não sob o canal de mídia da aquisição de usuários (UA).</li></ul> |
| Período coberto pelo relatório | O relatório fornece métricas de coorte até 7 dias pós-instalação. |
| Estrutura do diretório | A estrutura de diretórios é organizada por data de instalação. Cada pasta de data de instalação inclui várias versões criadas diariamente. Cada versão reflete os dados cumulativos atualizados para essa data de instalação. Isso significa que você deve processar apenas a versão mais recente do relatório disponível. <Anchor target="_blank" href="/marketers/pt/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#estrutura-do-diretório">Saiba mais</Anchor> |
| Estrutura do relatório | O esquema do relatório (as dimensões e métricas incluídas) é fixo e não pode ser modificado. |
| Fuso horário | UTC |
| Atualização dos dados | <ul><li>Diária.</li><li>As métricas são calculadas usando os dados disponíveis à meia-noite UTC, que é o final do dia.</li><li>SLA: Novos relatórios estão disponíveis no Data Locker até 16:00 UTC. Uma nova versão é criada para as últimas 15 datas de instalação de cada dia. <Anchor target="_blank" href="/marketers/pt/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#report-folder-hierarchy">Ver mais</Anchor></li></ul> |

</Accordion>

<div id="report-structure" />

## Estrutura do relatório

O relatório é composto por dimensões e métricas.

As métricas abrangem dados de atribuições, receita e usuários únicos que realizam um evento.

<div id="field-formats" />

<Accordion title="Formatos de campo">

<Table>
  <thead>
    <tr>
      <th>
        Nome do formato
      </th>
      <th>
        Descrição
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        String [n]
      </td>
      <td>
        O comprimento máximo da string. Normalmente, não impomos limitações de comprimento de campo no recebimento dos dados, mas os dados podem ficar truncados depois disso.
      </td>
    </tr>
    <tr>
      <td>
        Descrição de tempo
      </td>
      <td>
        As strings têm o formato,

        ```
        yyyy-mm-dd hh:mm:ss.
        ```

        Por exemplo,

        ```
        2019-09-17 00:09:25
        ```
      </td>
    </tr>
    <tr>
      <td>
        Enumeração [n]
      </td>
      <td>
        Os campos de enumeração podem conter apenas valores específicos. Por exemplo, selected\_currency tem 3 caracteres e pode conter apenas códigos de moeda, conforme especificado.
      </td>
    </tr>
    <tr>
      <td>
        Carimbo de data/hora
      </td>
      <td>
        Carimbo de data/hora UNIX de 10 dígitos. Exemplo:  
        4 de agosto de 2020, 07:25 UTC se traduz em

        ```
         "timestamp": "1596525944"
        ```
      </td>
    </tr>
    <tr>
      <td>
        Boolean
      </td>
      <td>
        O valor no campo pode ser *TRUE* ou *FALSE*
      </td>
    </tr>
    <tr>
      <td>
        Inteiro
      </td>
      <td>
        Inteiro
      </td>
    </tr>
    <tr>
      <td>
        float
      </td>
      <td>
        Número flutuante real que pode ter uma vírgula decimal e valores após a vírgula.
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="dimensions" />

<Accordion title="Dimensões">

<Table>
  <thead>
    <tr>
      <th>
        Nome do campo
      </th>
      <th>
        Descrição
      </th>
      <th>
        Formato
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        af\_ad\_id
      </td>
      <td>
        Identificador de anúncio. Hierarquia da campanha
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_ad
      </td>
      <td>
        Nome do anúncio.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_adset\_id
      </td>
      <td>
        Identificador do conjunto de anúncios. Hierarquia da campanha
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_adset
      </td>
      <td>
        Nome do conjunto de anúncios
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        ativado
      </td>
      <td>
        ID do aplicativo (aplicativo do anunciante) com ID do prefixo.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        attribution\_method
      </td>
      <td>
        O mecanismo usado para atribuir o evento. Exemplos desses mecanismos incluem métodos da AppsFlyer, SKAdNetwork (SKAN) e orgânicos.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        tipo\_de\_toque\_atribuído
      </td>
      <td>
        Valores possíveis: clique em impressão, nulo.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        campanha
      </td>
      <td>
        Nome da campanha informado pela ad network à AppsFlyer.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_c\_id
      </td>
      <td>
        Identificador da campanha.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        dias\_após\_atribuição
      </td>
      <td>
        O número de dias decorridos desde a data da conversão (não o carimbo de data/hora específico da conversão).  
        Dica! Use isso para calcular os dias de retenção e de KPI.
      </td>
      <td>
        int
      </td>
    </tr>
    <tr>
      <td>
        nome\_do\_evento
      </td>
      <td>
        Identifica o evento. Alguns nomes de eventos têm um significado específico, enquanto outros estão relacionados com eventos definidos pelo anunciante na app.

        | nome\_do\_evento | O que o utilizador fez |
        | --- | --- |
        | af\_conversion | Usuário convertido. Use conversion\_type para identificar se é uma instalação, reengajamento ou reatribuição. ou reengajamento. |
        | Anunciante definiu evento in-app | Realizou um evento in-app. |
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        geo
      </td>
      <td>
        O código ISO do país. Derivado do endereço IP do usuário nos métodos de atribuição clássicos da AppsFlyer, enquanto na SKAN os dados são enriquecido através de ad networks ou modelados.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        install\_date
      </td>
      <td>
        SKAN: Estimado pela AppsFlyer com base na hora de chegada do postback.

        AF:

        * UA: Primeiro lançamento após a instalação
        * Retargeting: Primeiro lançamento após reengajamento/reatribuição
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        é\_atribuição\_primária
      </td>
      <td>
        UA: Verdadeiro

        Redirecionamento: Durante uma janela de reengajamento, atribuímos tanto à fonte de media original (antes do reengajamento) como à fonte de media de reengajamento. Enquanto o evento ocorrer dentro da janela de reengajamento. A fonte de media original será Falsa (não é atribuição primária). A fonte de mídia de reengajamento será VERDADEIRA.
      </td>
      <td>
        bool
      </td>
    </tr>
    <tr>
      <td>
        fonte\_de\_mídia
      </td>
      <td>
        Ad network atribuída a um evento.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        moeda\_selecionada
      </td>
      <td>
        Código de 3 letras da moeda (USD, EUR) definido por você nas configurações do aplicativo. Formato ISO-4217. Essa é a mesma moeda usada para exibir a receita na interface do usuário da SSOT.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        tipo\_de\_conversão
      </td>
      <td>
        Valores possíveis:  
        Instalação: O usuário baixa e abre um aplicativo pela primeira vez.  
        Reatribuição: O usuário reinstala e é atribuído a uma nova campanha.  
        Re-download (SKAN): O usuário instala o aplicativo novamente após a desinstalação.  
        Reengajamento: Reengajamento: O usuário reabre o aplicativo depois de interagir com um anúncio de retargeting.
      </td>
      <td>
        string
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="metrics" />

<Accordion title="Métricas">

| nome do dl escolhido | Descrição | Formato |
| --- | --- | --- |
| receita\_moeda\_selecionada | O valor da receita acumulada na moeda selecionada. Máximo de duas casas decimais após a vírgula.  <br />Exemplo: Para event\_name=purchase com days\_post\_attribution=2, o valor reflete a receita total de eventos de compra dentro de dois dias após a instalação (não apenas no segundo dia). | dobro |
| receita\_usd | O valor da receita acumulada em USD.  <br />Exemplo: Para event\_name=purchase com days\_post\_attribution=2, o valor reflete a receita total de eventos de compra dentro de dois dias após a instalação (não apenas no segundo dia). | dobro |
| skan\_duplicates | As instalações atribuídas simultaneamente pelo SKAN e outros métodos AF são removidas para evitar a contagem dupla nos dados de SSOT. | longo |
| uninstalls\_count | Número de usuários do aplicativo que o instalam e posteriormente o desinstalam (excluem) (relevante somente para Aquisição de Usuário) | longo |
| utilizadores\_únicos | O número de usuários distintos que executam um evento. Os valores são cumulativos.  <br />Exemplo: Para event\_name=purchase com days\_post\_attribution=2, o valor reflete usuários únicos que fizeram compras dentro de dois dias após a instalação (não apenas no segundo dia). | int |

</Accordion>

<div id="modeled-data" />

<Accordion title="Dados modelados">

A AppsFlyer modela dados que os relatórios básicos da SKAdNetwork não podem fornecer.

* Valores de conversão nulos (CV): No SKAN, a Apple pode substituir os dados reais por um valor "Nulo" para manter a privacidade do usuário. Para garantir que nenhum dado seja omitido, esses valores nulos são modelados na SSOT. <Anchor target="_blank" href="/marketers/pt/docs/skan-modeled-data#null-conversion-values">Saiba mais</Anchor>.
* Métricas pós-instalação mais longas: A granularidade de dados da SKAN para períodos pós-instalação além dos dois primeiros dias é limitada, o que pode levar a imprecisões. Para manter a alta qualidade dos dados, modelamos a receita e os usuários únicos de eventos in-app para days\_post\_attribution maiores que 2. <Anchor target="_blank" href="/marketers/pt/docs/skan-modeled-data#revenue-ltv">Saiba mais</Anchor>.

Dados de geolocalização: A SKAN limita a granularidade dos dados, muitas vezes tornando os dados geográficos indisponíveis. Nesses casos, modelamos os dados para permitir uma análise de desempenho eficiente. <Anchor target="_blank" href="/marketers/pt/docs/skan-modeled-data#geo">Saiba mais</Anchor>.

</Accordion>

<div id="partial-data" />

<Accordion title="Dados parciais">

Ao analisar os dias de instalação recentes, as métricas para períodos pós-instalação estendidos (por exemplo, 7 dias) podem não estar totalmente maduras. Nesses casos, as métricas ainda estarão disponíveis, mas refletirão dados parciais.

Algumas regras práticas:

* O relatório mostra todos os dados disponíveis assim que estiverem disponíveis.
* Após 5 dias, as métricas de dois dias após a instalação são concluídas*.
* Após 7 dias, as métricas de sete dias após a instalação são concluídas. Até 15 dias após a instalação, o modelo pode refinar esse valor.

Razões para dados parciais:

* Maturidade dos dados: Quando o tempo desde a data de instalação é menor do que os dias que estão sendo analisados, os dados ainda estão se acumulando e ainda não estão completos.
* Atrasos da SKAN: Os dados da SKAN são recebidos com um atraso aleatório. Por exemplo, a atividade pós-instalação nos primeiros dois dias pode ser recebida até 96 horas (4 dias) após a instalação.
* Tempo de dados modelados: Os dados da SKAN para períodos superiores a 2 dias após a instalação são modelados. Nossos modelos geram o primeiro valor estimado após 7 dias. Durante esse período (dias 2 a 7), os dados dos métodos de atribuição clássicos da AppsFlyer estão disponíveis, enquanto os dados modelados pela SKAN não estão.

Exemplos (assumindo uma data de instalação de 1º de janeiro):

* No dia 2 de janeiro: Os dados do SKAN ainda não foram recebidos. Os dados de 2 dias após a instalação serão iguais aos dados de 7 dias após a instalação, e ambos são parciais, consistindo em dados dos métodos clássicos de atribuição da AppsFlyer.
* No dia 3 de janeiro: Os dados da SKAN são parcialmente recebidos. Os dados de 2 dias após a instalação ainda serão parciais, agora contendo parcialmente os dados do SKAN. Os dados de 7 dias após a instalação ainda não incluirão nenhum dado dp SKAN modelado (o primeiro valor modelado fica disponível após 7 dias da instalação). Portanto, entre 2 a 7 dias após a instalação, podemos ver um valor menor por 7 dias após a instalação em relação a 2 dias após a instalação.
* No dia 6 de janeiro: Os dados da SKAN nos primeiros dois dias após a instalação foram totalmente recebidos, incluindo postbacks com o máximo de atraso possível. As métricas para dois dias após as instalações são concluídas. Neste ponto, as métricas para 7 dias após as instalações ainda não foram concluídas.
* No dia 8 de janeiro: Os dados modelados do SKAN para 7 dias após a instalação são concluídos. Nosso modelo continuará refinando o valor até 16 de janeiro.

</Accordion>

<div id="directory-structure" />

## Estrutura do diretório

<div id="report-folder-hierarchy" />

<Accordion title="Hierarquia de pastas de relatório">

* As pastas primárias são organizadas pelo tipo de relatório. Valores possíveis: 'ssot\_unified', 'ssot\_retargeting' e 'ssot\_user\_acquisition'.
* Dentro dessas pastas, as subpastas são organizadas pela data de instalação.

**Controle de versão**

* Cada pasta de data de instalação contém várias versões, criadas diariamente.
* Cada versão reflete os dados cumulativos atualizados para essa data de instalação.
* Os relatórios incluirão todos os dados disponíveis para a data de instalação. Por exemplo, em 18 de abril, a versão mais recente de cada data de instalação contém todos os dados até aquele ponto de 18 de abril.
* Dica: Sempre processe a versão mais recente do relatório disponível para garantir a precisão.

Cada data de instalação é limitada a até 15 versões. Após 15 dias, todas as métricas são corrigidas por completo. <Anchor target="_blank" href="/marketers/pt/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Saiba mais</Anchor>.

</Accordion>

<div id="directory-and-filename-structure" />

<Accordion title="Diretório e estrutura de nomes de arquivos">

O caminho para o relatório consiste no seguinte formato:

`<bucket-name>`/t=`<ssot_unified OU ssot_retargeting OU ssot_user_acquisition>`/install\_date=`<yyyy-mm-dd>`/version=`<unix timestamp>`/`<parquet file number>`

Exemplo de hierarquia de pastas no bucket do anunciante:

```
bucket
|
└── t=ssot_unified
    |
    ├── install_date=2024-05-05
    |   |
    |   └── version=1714890235
    |   |    |
    |   |    ├── part-00000-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    |
    |   |    ├── part-00001-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    │
    |   |    └── part-00002-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |
    |   |
    |   └── version=1714890286
    |        |
    |        ├── part-00000-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        |
    |        ├── part-00001-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        │
    |        └── part-00002-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |   |
    .   . 
    .   .
```

Legenda:

* t: Tópico de relatório (tipo).
* install\_date: A data de instalação do aplicativo. Isso significa que a atividade pós-instalação aparecerá com base na data de instalação em que o usuário baixou o aplicativo, não no dia em que a ação do usuário ocorreu.
* version: Carimbo de data/hora Unix indicando quando a versão foi criada.

</Accordion>

<div id="bi-developer-considerations" />

## Considerações para desenvolvedores de BI

**Escopo dos dados no relatório:**

Os relatórios contêm dados sobre instalações com aquisição de usuários e retargeting com reatribuições (re-download no SKAN) e reengajamentos, juntamente com eventos in-app correlacionados.

<div id="loading-reports" />

<Accordion title="Carregando relatórios">

Você pode carregar relatórios unificados, de aquisição de usuários e de retargeting separadamente ou de uma só vez em seu sistema de BI. Se você carregá-los juntos e quiser filtrar as exibições por conta própria:

* Relatórios unificados: Use is\_primary\_attribution=true ou null field.
* Relatórios de aquisição de usuários: Use conversion\_type=install.
* Relatórios de redirecionamento: Use conversion\_type=reengajamento ou reatribuição.
* Visualização unificada: Se você usar a visualização unificada no processo de carregamento de dados, poderá dividir os dados entre os tipos de campanha:

* Use conversion\_type=install, reengajamento ou reatribuição (re-downloads no SKAN).
* Consulte "Dupla atribuição de eventos de retargeting" para obter mais detalhes

</Accordion>

<div id="days-postattribution" />

<Accordion title="Dias pós-atribuição">

<div id="important" />

> 🚧 **Importante!**
>
> O relatório inclui uma dimensão, days\_post\_attribution, que associa a receita e os dados exclusivos do usuário ao número específico de dias após a instalação

* Para atribuições (instalações, reengajamentos etc.), o valor é 0.
* Para eventos de receita e no aplicativo, os dados são categorizados em coortes predefinidas, atualmente limitadas a "2" dias e "7" dias após a instalação.

**Para analisar com precisão os eventos e a receita no aplicativo, você deve aplicar um filtro para a dimensão days\_post\_attribution.** Veja a consulta de exemplo abaixo.

Um exemplo de erro comum é aplicar uma lógica simplificada que soma a coluna de receita para um conjunto específico de dimensões. Essa abordagem resulta em números incorretos porque alguns dados de receita são contados duas vezes (uma para days\_post\_install=2 e outra para days\_post\_install=7). Este exemplo também é relevante ao analisar usuários únicos para eventos in-app específicos.

</Accordion>

<div id="considerations" />

<Accordion title="Considerações">

**Dicas:**

* Última versão: Sempre consulte a versão mais recente disponível para cada data de instalação para garantir que você esteja trabalhando com os dados mais atualizados e precisos para sua análise.
* Cálculo da receita: A receita em USD é calculada com base na taxa de câmbio do dia do evento.
* Analise as atribuições: Os registros em que event\_name=af\_conversion refletem atribuições (instalações, reatribuições (re-downloads no SKAN) e reengajamentos). A contagem de atribuições aparece na métrica de usuários únicos, e as métricas de receita para esses campos estarão vazias. O valor em days\_post\_attribution será 0.
* Comparação do dashboard: Ao comparar as instalações com o dashboard, some os tipos de conversão de download e instalação, pois o dashboard considera ambos na coluna de instalação.
* Analise eventos in-app: Os registros em que event\_name não é igual a "af\_conversion" refletem eventos in-app. A contagem de usuários únicos que executam o evento aparece na métrica de usuários únicos, enquanto a receita gerada por esses eventos aparece nas métricas de receita.
* Tipo de conversão: Diferencie as conversões de aquisição e retargeting de usuários usando essa dimensão. Observe que uma interrupção adicional para os dados do SKAN está disponível (instalações vs. novos downloads). Ao comparar dados com o dashboard SSOT, ambos os tipos são considerados instalações.
* Eventos de receita de anúncios: são incluídos quando disponíveis.
* Segregação de dados Todos os dados do aplicativo são fornecidos em um único arquivo. Use o campo App ID para separar dados por aplicativo ou defina o Data Locker para segregar por aplicativo.

</Accordion>

<div id="example-use-cases" />

<Accordion title="Exemplo de casos de uso">

A seguir estão exemplos de alguns usos práticos dos dados via Data Locker. Cada exemplo é ilustrado por uma instrução SQL e uma amostra visual do Excel.

<div id="calculating-total-attributions-per-campaign" />

<Accordion title="Cálculo do total de atribuições por campanha">

Nessa consulta, nós:

* Somamos o total de atribuições únicas por campanha para cada data de instalação.
* Filtramos as conversões com o nome do evento "af\_conversion" e um código de campanha específico (af\_c\_id).

```sql
SELECT install_date, SUM(unique_users) AS total_attributions FROM ssot_unified WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND app_id = 'YOUR_APP' GROUP BY install_date;
```

</Accordion>

<div id="calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign" />

<Accordion title="Cálculo da conversões (instalações e re-downloads) para comparar com as instalações no painel por campanha única">

Nessa consulta, nós:

* Contamos as conversões distinguindo entre novas instalações e novos downloads por campanha exclusiva e data de instalação.
* Comparamos as instalações com a métrica de instalação do dashboard, que mescla os tipos de conversão "install" e "re-download".

```sql
SELECT install_date, conversion_type, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND conversion_type IN ('install', 're-download')    
-- The dashboard sums both under the install field
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type;
```

</Accordion>

<div id="calculating-retargeting-conversions-per-geo" />

<Accordion title="Cálculo de conversões de retargeting por geolocalização">

Nessa consulta, nós:

* Contamos as conversões de campanhas de retargeting divididas por localização geográfica.
* Considerando os tipos "re-attribution" e "re-engagement" para essas conversões.

```sql
SELECT install_date, conversion_type, geo, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type IN ('re-attribution', 're-engagement')    
-- Both types are relevant for re-targeting
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type, geo;
```

</Accordion>

<div id="calculating-installs-by-attribution-method-per-media-source" />

<Accordion title="Cálculo de instalações por método de atribuição por fonte de mídia">

Nessa consulta, nós:

* Contamos as instalações por métodos de atribuição (SKAN, métodos da AppsFlyer e orgânicos) e as separamos por fonte de mídia.
* Filtramos com base em eventos "af\_conversion" com um tipo de conversão "install".

```sql
SELECT install_date, attribution_method, media_source, SUM(unique_users)   
AS total_installs
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type = 'install'
    AND app_id = 'YOUR_APP'
GROUP BY install_date, attribution_method, media_source;
```

</Accordion>

<div id="calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset" />

<Accordion title="Cálculo da receita acumulada de 7 dias após a instalação do Facebook por conjunto de anúncios">

Nessa consulta, mensuramos a receita acumulada em um período de 7 dias após a instalação via anúncios exibidos no Facebook.

```sql
SELECT install_date,
       af_adset,
       SUM(revenue_usd) AS total_revenue_day_7
FROM ssot_unified
WHERE media_source = 'facebook'
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_adset;
```

</Accordion>

<div id="calculating-cumulative-revenue-for-selected-postinstall-periods" />

<Accordion title="Cálculo da receita cumulativa para períodos pós-instalação selecionados">

Nessa consulta, nós:

* Calculamos a receita acumulada para vários dias selecionados após a instalação, dividindo as somas para o dia 2 e o dia 7.
* Observe que, ao analisar instalações dos últimos 7 dias, os dados de 7 dias após a instalação podem estar incompletos. <Anchor target="_blank" href="/marketers/pt/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Saiba mais</Anchor>

```sql
SELECT install_date,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) AS total_revenue_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) AS total_revenue_day7
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source" />

<Accordion title="Cálculo da receita de um evento in-app específico (compra) por canal de mídia">

Nessa consulta, nós:

* Mensuramos o valor da receita de um evento in-app específico (como "af\_purchase") e somamos esses dados por canal de mídia.
* Filtramos os dias selecionados após a instalação para garantir que os dados não fossem contados duas vezes.

```sql
SELECT install_date, media_source, SUM(revenue_usd) AS total_purchase_revenue
FROM ssot_unified
WHERE event_name = 'af_purchase'  -- Change to your specific event
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

<div id="calculating-inapp-event-conversion-rate-for-2-days-postinstalls" />

<Accordion title="Cálculo da taxa de conversão de eventos in-app para 2 dias após as instalações">

Nessa consulta, calculamos a taxa de conversão de um evento in-app específico (como "af\_complete\_tutorial") em relação a todas as instalações.

```sql
SELECT install_date,
  SUM(IF(days_post_attribution = 2 AND   
event_name = 'af_complete_tutorial', unique_users, 0)) 
  / SUM(IF(event_name = 'af_conversion', unique_users, 0))   
AS conversion_rate_day2_af_tutorial_conversion
FROM ssot_unified
WHERE conversion_type = 'install'    
-- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id" />

<Accordion title="Cálculo do ARPU para 7 dias e 2 dias após a instalação por ID de campanha">

Nessa consulta, nós:

* Calculamos a receita média por usuário (ARPU) para o dia 2 e o dia 7 após a instalação em todas as campanhas.
* Observe que, ao analisar instalações dos últimos 7 dias, os dados de 7 dias após a instalação podem estar incompletos. <Anchor target="_blank" href="/marketers/pt/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Saiba mais</Anchor>

```sql
SELECT install_date,
       af_c_id,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day7
FROM ssot_unified
WHERE conversion_type = 'install'  
       -- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_c_id;
```

</Accordion>

<div id="calculating-amount-of-duplicates-per-media-source-in-this-query" />

<Accordion title="Cálculo da quantidade de duplicatas por canal de mídia nesta consulta">

Nessa consulta, contamos o total de atribuições de usuário duplicadas por canal de mídia e data de instalação para descobrir quais canais de mídia podem ter mais duplicatas na atribuição do usuário.

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
    AND event_name = 'af_conversion'
GROUP BY install_date, media_source;
```

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Características e limitações">

| Caraterística | Observação |
| --- | --- |
| Disponibilidade de relatórios por dia | Um relatório SSOT somente é criado quando o botão do SSOT for ativado. Ou seja, se você ativar o botão em um determinado dias, as instalações daquele dia aparecerão no dashboard ao final desse dia. |
| Métricas pós-instalação de dois dias | <ul><li>Para SKAN 4 no Conversion Studio: Os dados são registrados 2 dias após a instalação.</li><li>Para SKAN 3 no Conversion Studio: Os dados se baseiam na janela de atividade da SKAN.<br />Exemplo: Se a janela de atividade for de 24 horas, os eventos que ocorrem dentro dessa janela (mesmo no Dia X+1) são contados.</li></ul> |
| Disponibilidade de eventos in-app | Disponível apenas para eventos ocorridos durante o período da Janela 1. |
| Detalhamento de redownloads na SKAN | Disponível. No dashboard do SSOT, esse detalhamento não está disponível e as instalações e os novos downloads são incluídos na métrica de instalações. |
| Alterações na configuração do SKAN Conversion Studio | Alterar a configuração do SKAN Conversion Studio pode causar imprecisões nos dados SSOT por aproximadamente 96 horas, pois os postbacks de instalações codificadas com o esquema anterior ainda chegam. |
| Fuso horário | O fuso horário específico do aplicativo não está disponível. |
| Dados orgânicos | <ul><li>Disponível 7 dias após a instalação.</li></ul> |
| Dados pós-conversão (instalação, reatribuição, reengajamento) | Limitados a 7 dias após a conversão |
| Transparência das agências | Com suporte. |
| Mudanças no nome da campanha | Indisponível. Use o ID da campanha para agrupar e filtrar se os nomes da campanha forem alterados. |
| Redes de anúncios | <ul><li>Podem acessar relatórios DataLocker SSOT para ver os dados atribuídos ao seu canal de mídia se:<ul><li>O anunciante ativou o SSOT no Conversion Studio.</li><li>A ad network está executando campanhas do SKAN.</li><li>A ad network deve ter as [permissões necessárias](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions) do anunciante para acessar dados agregados.</li></ul></li></ul> |
| Acesso à agência | Indisponível. Os usuários da agência podem visualizar os dados de SSOT no dashboard do SSOT. |
| Métricas D7 | <ul><li>Métricas D7 para tráfego orgânico estão disponíveis a partir de 16 de fevereiro de 2025.</li><li>Pode estar ausente ou menor que as métricas D2 se:<ul><li>O intervalo de datas inclui datas para as quais não se passaram 8 dias.</li><li>Os dados modelados não estão disponíveis (por exemplo, menos de 14 dias de dados de receita). <Anchor target="_blank" href="/marketers/pt/docs/skan-modeled-data#revenue-ltv">Saiba mais</Anchor>.</li><li>A configuração do SKAN Conversion Studio foi alterada nos últimos 14 dias.</li><li>Existem menos de 10 instalações para uma determinada data.</li></ul></li></ul> |
| Nomes de eventos predefinidos | Como o nome do evento "af\_conversion" é usado para indicar diferentes tipos de conversões, os aplicativos que têm um evento especificamente chamado "af\_conversion" verão o evento original renomeado para "af\_conversion\_event". |
| Diferença em moeda local | Como o dashboard SSOT e o relatório SSOT no DataLocker não são calculados simultaneamente, pequenas discrepâncias podem ocorrer ao comparar a receita em moeda local no dashboard com a moeda selecionada no relatório. Isso se deve às taxas de câmbio ligeiramente diferentes usadas nos momentos em que os dados foram calculados. |
| Dados parciais do SKAN D7 | Como os dados do SKAN D7 são modelados e a versão inicial está pronta 7 dias após a instalação, ao analisar as métricas D7 para dias nos últimos 7 dias, os dados D7 serão parciais. Para registros em que o método de atribuição é SKAN, as métricas D7 serão inferiores às métricas D2. |
| Granularidade limitada para receita D7 e métricas de eventos no aplicativo | As métricas de receita e eventos únicos do usuário para 7 dias após a instalação não estão disponíveis nos níveis de granularidade do conjunto de anúncios, do anúncio e do tipo de conversão. Como esse nível de detalhe normalmente não está disponível na SKAN, o modelo não leva em conta essas dimensões. |
| Atualização dos dados de receita de anúncios | Os dados de receita de anúncios têm um atraso de um dia.<br /><br />Por exemplo, um relatório criado na manhã de 3 de julho incluirá dados de receita de anúncios até (e incluindo) 1 de julho. |

</Accordion>

<div data-zendesk-anchors="h_01J455DHWAB1J9611A4KA40PZM=aten%C3%A7%C3%A3o ssot-reports-in-data-locker=o-que-%C3%A9-data-locker h_01J454K90GWKME8F4JCDQKM3CK=o-que-%C3%A9-data-locker what-is-single-source-of-truth-ssot=o-que-%C3%A9-single-source-of-truth-ssot h_01J454K90GRCFR3PSAQRTX98B4=o-que-%C3%A9-single-source-of-truth-ssot benefits-of-ssot-reports-in-data-locker=vantagens-dos-relat%C3%B3rios-de-ssot-no-data-locker h_01J454PANH9J6ZZ069RS6FVWZM=vantagens-dos-relat%C3%B3rios-de-ssot-no-data-locker h_01J46C54ZB4YYTZ6CDHHC0EC8P=setting-up-data-locker h_01J455Q07J5XPYEBVP3BZ1FMVH=permissions h_01J29BTC9CESJF592P616WMK46=ssot-report-facts report-structure::673746b9=estrutura-do-relat%C3%B3rio h_01J29CQ5K4JBEP4X8YQ0V32WYR=estrutura-do-relat%C3%B3rio h_01J29CHBX2QNFTAQSA1W01PFH0=field-formats h_01J29BTC9CJ8GZDDCHK9NBZ4YX=dimensions h_01J29BTC9C86YMVEY17QQZNZCV=metrics h_01J29BTC9CH3DAA7ZRHG8C04MF=modeled-data h_01J29M72WAPH3KEW9N60JHTT3W=partial-data directory-structure=estrutura-do-diret%C3%B3rio h_01J29MB7B7Q3PJ9YWFQESWN0KD=estrutura-do-diret%C3%B3rio h_01J29MCSH4V41CPB7ZG41751QW=report-folder-hierarchy h_01J29MCSH40ATHNAJMY8KR7ANZ=directory-and-filename-structure bi-developer-considerations=considera%C3%A7%C3%B5es-para-desenvolvedores-de-bi h_01J29MS6XV7XYTA9Q81454WEQN=considera%C3%A7%C3%B5es-para-desenvolvedores-de-bi h_01J2F4HG8YHDGYFKHBBC5KSN2G=loading-reports h_01J2F4HG8YKNEVGEWTR91ADSDS=days-postattribution h_01J3YT1X908JVMDXKRQBCRD1JR=importante h_01J2F4HG8YAAE0E04Y6Q9Z62NZ=considerations h_01J3A82HZF14CCS027FE991M0T=example-use-cases h_01J3A883DQFQE0WTTY4FMX3AQ4=calculating-total-attributions-per-campaign h_01J3A883DQ82K71XY408M2BW0B=calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign h_01J3A883DQ5QAVH6AX7CGCBSWG=calculating-retargeting-conversions-per-geo h_01J3A883DQE25X31SPPF166BRH=calculating-installs-by-attribution-method-per-media-source h_01J3A883DQ8QVR8WKPPX1QF414=calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset h_01J3A883DQ51T3Z6H239P5JDJ1=calculating-cumulative-revenue-for-selected-postinstall-periods h_01J3A883DQXRCQ4NWY0BCX886E=calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source h_01J3A883DQRR62BWQ6JBTZ7238=calculating-inapp-event-conversion-rate-for-2-days-postinstalls h_01J3A883DRPEVDQCWKCT9M3EC1=calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id h_01J3A883DRRZ9Y8F3KNAAPZT2S=calculating-amount-of-duplicates-per-media-source-in-this-query h_01J29MV69M667QDHMS5WGYKPCZ=traits-and-limitations" />
