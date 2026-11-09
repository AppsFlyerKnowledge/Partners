---
title: Protect360 para parceiros integrados
metadata:
  keywords:
    - Protect360
    - Ad Networks
    - Partners
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2017-09-19T08:27:29Z'
  edited_at: '2026-08-19T00:36:45Z'
  id: 115004745523
  locale: pt
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/pt/articles/115004745523
---
> **Visão geral:** Os parceiros integrados, como redes de publicidade e agências, podem visualizar fraudes relacionadas com o seu tráfego, identificadas e bloqueadas pelos motores ProtectLITE e Protect360, bem como observar as regras de validação definidas manualmente pelo cliente.

<div id="overview" />

## Visão geral

A AppsFlyer identifica e bloqueia fraudes através de: 

* <Anchor target="_blank" href="/marketers/pt/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">ProtectLITE</Anchor><Anchor target="_blank" href="/marketers/pt/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting">: Oferece uma proteção básica contra fraudes para todos os clientes.</Anchor>
* <Anchor target="_blank" href="/marketers/pt/docs/protect360-anti-fraud-guide">Protect360</Anchor><Anchor target="_blank" href="/marketers/pt/docs/protect360-anti-fraud-guide">: Oferece uma proteção avançada contra fraudes para os anunciantes com um plano de subscrição premium.</Anchor>

Os anunciantes devem conceder:

* Permissões de ad networks <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions-tab">permissões</Anchor> para **acesso ao dashboard do Protect360 e relatórios de dados brutos** (incluindo o ProtectLITE) e **acesso a dados agregados de eventos in-app** (para fraude de eventos in-app).
* Permissões <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions-tab">às agências</Anchor> para **aceder ao painel e aos dados brutos do Protect360.**

Com as permissões adequadas, os parceiros integrados podem:

* Visualizar dados referentes ao tráfego que geraram.
* Descarregar os <Anchor target="_blank" href="/marketers/pt/docs/protect360-anti-fraud-guide#raw-data">relatórios de dados brutos</Anchor> correspondentes.

Além disso, estão disponíveis <Anchor target="_blank" href="/partners/pt/docs/protect360-reports-for-ad-networks">relatórios de dados brutos</Anchor> para redes de publicidade sobre limites de cliques e impressões e assinaturas de cliques com falha, sem necessidade de permissões dos anunciantes.

<div id="note" />

> 📘 **Nota**
>
> Para anunciantes que colaboram com redes de anúncios através de uma agência, para que tanto a rede de anúncios quanto a agência possam aceder aos dados, o anunciante deve integrar ambas na AppsFlyer e conceder-lhes permissão para aceder aos dados.
>
> Se somente a agência for integrada e receber permissões, a rede de anúncios não terá acesso aos dados.

<div id="dashboard-view" />

### Visualização do painel

**Pré-requisitos**: Permissão do anunciante para aceder ao ProtectLITE e o Protect360. 

Os parceiros integrados podem visualizar o painel e os gráficos; consulte a captura de ecrã abaixo.

Saiba mais sobre os dados disponíveis nos painéis <Anchor target="_blank" href="/marketers/pt/docs/basic-fraud-detection-and-insights-with-protectlite-dashboard-and-reporting#painel">ProtectLITE</Anchor> e <Anchor target="_blank" href="/marketers/pt/docs/protect360-anti-fraud-guide#dashboard">Protect360</Anchor> .   

Limitações:

* As redes de publicidade não têm acesso ao painel de anomalias.

<Image align="center" alt="p360_dashboard_1.jpg" src="https://files.readme.io/234771b87c3343700d42b2cbbc283db5d65db7ea96af6bead7d55eb03d9bde01-44928678658833.jpg" />

* As ad networks e as Agências não podem acessar o Fraud Protection Studio nem o nível de dados brutos dos dados marcados. No entanto, elas podem vê-los de forma agregada no dashboard do Protect360, em atribuição marcada e eventos in-app marcados. Além de identificar fraude por tipo de tag (nova versão etc.). Para saber mais sobre o FPS, consulte <Anchor target="_blank" href="/marketers/pt/docs/beta-fraud-protection-studio">este artigo</Anchor>.

  <Image align="center" alt="" src="https://files.readme.io/7e8bee04ecaf53148f65ae0aa9b2e3559a550bdbc5a5ebf9047a7e82dc093966-44928678660881.png" width="624px" />

  <Image align="center" alt="" src="https://files.readme.io/fa35e6046d6c06579e602ccc1cb919e5312ec22055b3e29d3ead6b2a7ab5ea82-44928694758161.png" width="624px" />

<div id="raw-data-reports" />

### Relatórios de dados brutos

**Pré-requisitos: Permissão do anunciante para aceder ao ProtectLITE e o Protect360.**

Os relatórios de dados brutos do Protect360 mostram fraudes identificadas e bloqueadas através do ProtectLITE, Protect360 e Regras de Validação.

Os relatórios podem ser acedidos através de:

* Exportar dados: Na AppsFlyer, no menu lateral, escolha **Relatório** > **Exportação de Dados Brutos**
* Permissões <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions-tab">às redes de anúncios</Anchor> para **aceder ao painel do Protect360 e aos relatórios de dados brutos** (incluindo o ProtectLITE) e para **visualizar dados agregados de eventos na aplicação** (em casos de fraude de eventos na aplicação).

Saiba mais sobre os <Anchor target="_blank" href="/marketers/pt/docs/protect360-raw-data-reports">relatórios de dados brutos do Protect360</Anchor>.

<div id="protect360-ad-network-reporting-api" />

## API de Relatórios da Rede de Anúncios Protect360

* Os relatórios de dados brutos listados nesta secção estão acessíveis para redes de anúncios através da API.
* Relatórios equivalentes estão disponíveis no painel, na página Exportar Dados.
* Caso o anunciante não tenha uma subscrição do Protect360, apenas o relatório de Instalações está disponível.

**Pré-requisitos**

* Para obter acesso aos dados do anunciante via API, o anunciante deve conceder à rede de anúncios <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissions-tab">permissões</Anchor> para aceder ao painel do Protect360 e aos dados através da API. Redes de anúncios com acesso ao painel estão autorizadas a usar a API. O anunciante não precisa de tomar qualquer ação adicional.
* Para listar as aplicações para as quais tem permissões do Protect360, utilize a <Anchor target="_blank" href="/partners/pt/docs/app-list-api-for-ad-networks">API para obter lista de aplicações.</Anchor>
* O administrador deve obter um <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">token de autenticação V2.0</Anchor> disponível no painel AppsFlyer.

<div id="protect360-api-reports" />

#### Relatórios da API Protect360

| Relatório | Relevância dos dados | Descrição |
| --- | --- | --- |
| Fraude de eventos na aplicação pós-atribuição | Diariamente às 10h00 UTC | <ul><li>Eventos na aplicação realizados por instalações detectadas como fraudulentas.</li><li>Qualquer outro evento na aplicação considerado fraudulento, independentemente da instalação.</li></ul>O relatório pode ser filtrado opcionalmente por tipo de evento na aplicação, como descrito na tabela de parâmetros que se segue.<br /><br />Tema do relatório: `fraud-post-inapps` |
| Instalações pós-atribuição | Diariamente às 10h00 UTC | <ul><li>Instalações identificadas como fraudulentas após atribuição.</li><li>O relatório pode ser filtrado opcionalmente pela data de deteção, conforme descrito na próxima secção.</li></ul>Tema do relatório:  detecção |
| Instalações | Em tempo real | Instalações bloqueadas com a razão para o bloqueio<br /><br />Tema do relatório:  blocked\_installs\_report |
| Evento na aplicação | Em tempo real | Eventos na aplicação realizados por utilizadores bloqueados<br /><br />Tema do relatório: `blocked_in-app_events_report` |
| Cliques | Em tempo real | Cliques realizados por utilizadores bloqueados<br /><br />Tema do relatório: `blocked_clicks_report` |

<div id="procedure-for-ad-networks-to-get-protect360-reports-by-download" />

#### **Procedimento para redes de anúncios obterem relatórios do Protect360 através de download**

**Para obter um relatório utilizando a API:**

1. Identifique o relatório necessário na lista anterior.
2. Use o exemplo curl adequado (na secção seguinte) para preparar o seu script.
3. Garanta que substitui os seguintes espaços reservados:
   1. ID da aplicação
   2. Data de início
   3. Data de fim
   4. Token de autenticação (<Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">token V2.0 da AppsFlyer</Anchor>)
4. Algumas chamadas têm [parâmetros opcionais](/docs/protect360-for-integrated-partners#api-parameters), conforme descrito neste artigo.

<div id="curl-examples" />

### Exemplos de curl

<div id="installs-blocked_installs_report" />

<Accordion title="Instalações (relatório_de_instalações_bloqueadas)">

Substitua os espaços reservados app\_id, from, to e token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_installs_report/app/{app_id}?from={2020-07-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="postattribution-installs-detection" />

<Accordion title="Instalações pós-atribuição (deteção)">

Substitua os espaços reservados app\_id, from, to e token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/detection/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additonal-fields=fraud_reason,fraud_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="inapp-event-blocked_in_app_events_report" />

<Accordion title="Evento na aplicação (relatório_de_eventos_na_app_bloqueados)">

Substitua os espaços reservados app\_id, from, to e token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_in_app_events_report/app/?from=YYYY-MM-DD&to=YYYY-MM-DD&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="postattribution-inapp-events-fraud-fraud_post_inapps" />

<Accordion title="Fraude em eventos na aplicação pós-atribuição (fraude_eventos_na_app_pós_atribuição)">

Substitua os espaços reservados app\_id, from, to e token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/fraud-post-inapps/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=match_type,device_category,gp_referrer,gp_click_time,gp_install_begin,fraud_reason,fraud_sub_reason,detection_date' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \
```

</Accordion>

<div id="clicks-blockedclicks_report" />

<Accordion title="Cliques (relatório_de_cliques_bloqueados)">

Substitua os espaços reservados app\_id, from, to e token.

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/adnets-data/v1/export/blocked_clicks_report/app/{app-id}?from={2020-06-10}&to={2020-07-20}&additional_fields=keyword_id,store_reinstall,deeplink_url,oaid,blocked_reason,blocked_reason_value,blocked_reason_rule,blocked_sub_reason,gp_referrer,gp_click_time,gp_install_begin,amazon_aid,keyword_match_type' \
-H 'Authorization: Bearer {V2.0 api token placeholder. Note: The token has more than 700 characters.}' \ \
```

</Accordion>

<div id="protect360-ad-network-api-reference-guide" />

### Guia de referência API da rede de anúncios Protect360

<div id="api-basics" />

<Accordion title="Noções básicas da API">

Noções básicas da API da rede de anúncios Protect360:

| Caminho | `https://hq1.appsflyer.com/api/adnets-data/v1/export/report_topic/app/app_id` |
| --- | --- |
| Método | BAIXAR |
| Parâmetros de caminho (obrigatórios) | <ul><li>`app_id`:<ul><li>O identificador da aplicação, conforme mostrado no painel da AppsFlyer. Insira-o exatamente como exibido no painel.</li><li>Certifique-se de prefixar as aplicações iOS com **id.**</li></ul></li><li>API: Veja a próxima secção dedicada à [API de relatórios da rede de anúncios](/docs/protect360-for-integrated-partners#api-de-relatórios-da-rede-de-anúncios-protect360).</li></ul> |
| Tipos de conteúdo aceitos | `application/json` |
| Autorização | <ul><li>Token de autenticação no cabeçalho da requisição.</li><li>![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png)Peça ao administrador para obter o token V2.0 na página de <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">tokens</Anchor>. Este token tem cerca de 700 caracteres de comprimento.</li></ul> |
| Limitação de taxa | <Anchor target="_blank" href="/marketers/pt/docs/report-generation-quotas-rate-limitations">Limitações de taxa</Anchor> |
| Limitação de intervalo de datas | <ul><li>Data mais antiga suportada: 90 dias antes dos dados atuais</li><li>31 dias dentre os 90 dias anteriores</li></ul> |
| Limitações de linha | 200 mil linhas |
| Características do relatório | <ul><li>Fuso horário: UTC</li><li>Moeda: USD</li></ul> |

</Accordion>

<div id="api-parameters" />

<Accordion title="Parâmetros da API">

Parâmetros da API Protect360:

| Parâmetro | Descrição | Formato | Obrigatório |
| --- | --- | --- | --- |
| ID\_da\_app | ID da aplicação conforme aparece na AppsFlyer | Sequência de caracteres | Sim |
| início | Início do intervalo de datas:<ul><li>Para instalações, esta é a data de instalação.</li><li>Para eventos na aplicação, esta é a data do evento.</li></ul> | AAAA-MM-DD | Sim |
| para | Fim do período:<ul><li>Para instalações, esta é a data de instalação.</li><li>Para eventos na aplicação, esta é a data do evento.</li></ul> | AAAA-MM-DD | Sim |
| nome\_do\_evento | [Opcional para fraude em eventos na aplicação pós-atribuição]<br /><br />Filtrar eventos por eventos na aplicação. Limite o relatório a eventos específicos. Um ou mais eventos podem ser incluídos.<br /><br />Exemplo de uso: `&event_name=af_purchase,af_login` | Sequência de caracteres | Não |
| detetar de | [Opcional para instalações pós-atribuição]<br /><br />Início do intervalo de datas para deteção de fraude. (A predefinição é a partir de.) | AAAA-MM-DD | Não |
| detetar até | [Opcional para instalações pós-atribuição]<br /><br />Fim do intervalo de datas para deteção de fraude. (O valor predefinido é até.) | AAAA-MM-DD | Não |

</Accordion>

<div id="protect360-api-http-return-codes" />

<Accordion title="Códigos de retorno HTTP da API Protect360">

Códigos de erro e soluções:

| Estado | Código | Sintoma/mensagem | Solução |
| --- | --- | --- | --- |
| OK | 200 | Ficheiro CSV vazio | `addtional_fields`utilizado mais de uma vez no URI |
| OK | 200 | Ficheiro CSV vazio | Assegure-se de que as datas 'de' e 'até' estão no formato aaaa-mm-dd |
| OK | 200 | A página de login HTML da AppsFlyer retorna | Não há token no cabeçalho do token bearer |
| Pedido incorreto | 400 | Pedido incorreto | <ul><li>Limitação do intervalo de datas.<ul><li>A data mais antiga permitida é de 90 dias antes do dia atual</li><li>O período não pode exceder 60 dias para instalações e 90 dias para relatórios de aplicações</li></ul></li></ul> |
| Não autorizado | 401 | Não autorizado | Foi encontrado um token, mas não é válido. Verifique se possui o token V2.0 atual para a sua conta. Peça ao administrador para obter o token atual no painel de controlo. |
| Não encontrado | 404 |  | <ul><li>O endpoint especificado está incorreto</li><li>Verifique se o ID da aplicação está correto</li><li>Não tem autorização para aceder à aplicação</li></ul> |

</Accordion>

<div id="impression-capping" />

## Limitação de impressões

Se uma rede de anúncios apresentar taxas extremamente altas de impressão ou fraude de cliques, o Protect360 bloqueará as impressões ou cliques da rede durante um ciclo de 24 horas. Isso significa que quaisquer impressões/cliques que ocorram após atingir o limite não serão registados pela AppsFlyer nem serão elegíveis para atribuição. As impressões/cliques bloqueados aparecem no painel e nos relatórios do Protect360.

O algoritmo de proteção contra fraudes da AppsFlyer considera vários parâmetros na deteção de fraudes, incluindo volume de impressões/cliques, CVR, taxa de fraude detetada, flutuações normais na atividade, benchmarks da indústria e geográficos, além de parâmetros proprietários. O algoritmo é dinâmico e atualizado hora a hora para considerar as mudanças nas tendências.

**Acionar repetidamente limites de inundação de impressões ou cliques pode resultar na remoção permanente da integração do parceiro da plataforma AppsFlyer.**

Limites de impressões e cliques:

* Aplicam-se de igual forma a todas as redes de publicidade. Ou seja, não há rede de anúncios para a qual taxas extremamente altas de fraude de impressões ou cliques não resultem em limitações.
* Aplicam-se ao nível da aplicação/rede de anúncios. Ou seja, a análise de fraude considera todas as campanhas da rede de anúncios numa aplicação, e o bloqueio afeta relatórios e atribuição para todas as campanhas dessa rede numa aplicação (independentemente de a conta possuir o Protect360).
* São reiniciados após um ciclo de 24 horas e os bloqueios aplicam-se até ao final do ciclo. Os detalhes de quando começa e termina o ciclo são mantidos em sigilo pela AppsFlyer.
* Não podem ser alterados ou interrompidos. O Protect360 é minuciosamente ajustado e preciso na deteção de fraudes, e o algoritmo não pode ser ajustado ou desligado manualmente.
* Podem ser evitados interrompendo campanhas e editores com atividade anómala.

<div id="faq" />

<Accordion title="Perguntas Frequentes">

Perguntas Frequentes sobre Limitação de Impressões e Cliques:

| **Questão: Qual é o limite da rede?**<br /><br />**Resposta**: Os detalhes do mecanismo de limitação de cliques são protegidos para evitar tentativas de contornar o sistema. Dito isto, o limite só é atingido se houver um volume extremo de impressões/cliques, além do que seria esperado de um comportamento humano. Analisar o número diário de impressões, cliques e instalações dar-lhe-á uma ideia clara se há um problema de inundação resultado de um ou mais editores. |
| --- |
| **P: Como uma rede pode ser desbloqueada?**<br /><br />**Resposta**: Uma rede pode evitar o limite parando campanhas e editores com atividades anómalas. Uma vez bloqueada, a rede precisa aguardar até ao final do ciclo de 24 horas para que os cliques voltem a ser registados. |
| **Questão: O bloqueio afeta os clientes da AppsFlyer sem o Protect360?**<br /><br />**Resposta**: Sim, o limite afetará independentemente de o cliente ter ou não o Protect360. O mecanismo de limitação protege todos os clientes contra o abuso de cliques/impressões. |
| **P**: Isto não é fraude. A rede trabalha com fontes económicas e por vezes a qualidade delas é baixa.<br /><br />**Resposta**: O fraco desempenho em escala normal de fontes não suspeitas não aciona o limite de cliques. O algoritmo identifica desempenhos que não podem ser humanos. |
| **P**: Isto impede-nos de aumentar campanhas, e não queremos que essas impressões/cliques sejam bloqueados.<br /><br />**Resposta**: O algoritmo de proteção contra fraudes da AppsFlyer protege os clientes de casos extremos e flagrantes de cliques em excesso. Não afeta a capacidade de escalar, pois lida com impressões/cliques não gerados por humanos, onde a maioria dos bloqueios só causa problemas detalhados. Se tiver preocupações, contacte a AppsFlyer para resolver as suas questões. |
| **P**: Isto não é fraude. Será que a AppsFlyer tem dificuldades em lidar com o volume de impressões/cliques?<br /><br />**Resposta**: Não temos dificuldades em lidar com o volume. Apoiamos alguns dos maiores anunciantes globais e processamos bilhões de pontos de dados em tempo real diariamente, incluindo enormes quantidades de cliques legítimos. Como parte do nosso compromisso para sustentar um crescimento em larga escala com dados ricos e precisos, agimos no melhor interesse dos nossos clientes, bloqueando casos claros de cliques em excesso. |
| Questão: O que podemos fazer se anteciparmos um aumento significativo no tráfego e no volume de impressões/cliques (por exemplo, devido a novas campanhas)? Como podemos evitar ser bloqueados?<br /><br />Resposta:**O algoritmo é dinâmico e atualizado a cada hora, para considerar as diferentes tendências. É bastante sofisticado para lidar com picos e não é acionado por flutuações normais de atividade, incluindo aumentos bruscos e significativos de volume. Nesse sentido, os parceiros podem usar seus dados e relatórios de impressões/cliques para identificar fontes suspeitas e interromper essas campanhas.** |
| Questão: Como podemos verificar o tráfego problemático e melhorar o desempenho das campanhas?<br /><br />Resposta:**Os parceiros podem utilizar os seus dados e relatórios de impressões/cliques para identificar fontes suspeitas e interromper essas campanhas. Além disso, os parceiros conseguem ver dados de impressões e cliques bloqueados no painel do Protect360/ProtectLITE, nas colunas dedicadas, desde que tenham autorização do anunciante para visualizar dados de fraude no painel.** |

</Accordion>

<div id="click-signing" />

### Assinatura de cliques

As redes de publicidade podem adicionar assinaturas HMAC-SHA256 <Anchor target="_blank" href="/partners/pt/docs/click-signing-for-ad-networks">aos seus cliques</Anchor>.

Essas assinaturas permitem à AppsFlyer validar os cliques e assegurar que a informação dos cliques não foi adulterada por fraudadores.

* Os cliques validados são registados e atribuídos à rede de publicidade.
* Os cliques invalidados são rejeitados e:
  * São incluídos em relatórios do Protect360 disponibilizados para a rede de publicidade.
  * Não afetam a taxa de conversão nem o limite de cliques da rede de publicidade.

<div data-zendesk-anchors="overview=vis%C3%A3o-geral h_01HGSXTKYQB4Q1QQX4ZQS60AAJ=vis%C3%A3o-geral h_01HGSXTKYQN42EEMPSZMWVAMWD=nota dashboard-view=visualiza%C3%A7%C3%A3o-do-painel h_01HGSXTKYQPQP72R2VJB68ZDRZ=visualiza%C3%A7%C3%A3o-do-painel rawdata-reports=relat%C3%B3rios-de-dados-brutos h_01HGSXTKYQWRZECN905RGSEQ42=relat%C3%B3rios-de-dados-brutos protect360-ad-network-reporting-api=api-de-relat%C3%B3rios-da-rede-de-an%C3%BAncios-protect360 h_01HGSXTKYQ9388SCQTT2MX59Q9=api-de-relat%C3%B3rios-da-rede-de-an%C3%BAncios-protect360 protect360-api-reports=relat%C3%B3rios-da-api-protect360 h_01HGSXTKYQXZN2DMNZ09HE7355=relat%C3%B3rios-da-api-protect360 procedure-for-ad-networks-to-get-protect360-reports-by-download=procedimento-para-redes-de-an%C3%BAncios-obterem-relat%C3%B3rios-do-protect360-atrav%C3%A9s-de-download h_01HGSXTKYQ913MF0G38B23NYBG=procedimento-para-redes-de-an%C3%BAncios-obterem-relat%C3%B3rios-do-protect360-atrav%C3%A9s-de-download curl-examples=exemplos-de-curl h_01HGSXTKYQX3VN5NRMNQWW4AE4=exemplos-de-curl h_01HGSXTKYQQBJTM4ZMMQZ0VZNH=installs-blocked_installs_report h_01HGSXTKYQ5KTCD7K63DSVS6E2=postattribution-installs-detection h_01HGSXTKYQ6MA96W8E6R2SXBS5=inapp-event-blocked_in_app_events_report h_01HGSXTKYQMMC0WNWP56Q9J0ZS=postattribution-inapp-events-fraud-fraud_post_inapps h_01HGSXTKYQEG0JXJHS7QBAEBCA=clicks-blockedclicks_report protect360-ad-network-api-reference-guide=guia-de-refer%C3%AAncia-api-da-rede-de-an%C3%BAncios-protect360 h_01HGSXTKYQJRE1Y9C5RSCANWT2=guia-de-refer%C3%AAncia-api-da-rede-de-an%C3%BAncios-protect360 h_01HGSXTKYQE24FAPYHHMFP0B3X=api-basics h_01HGSXTKYRFSZRPHNPDHNREDH2=api-parameters h_01HGSXTKYRGSQ230NVN06SP6DG=protect360-api-http-return-codes impression-and-click-capping=limita%C3%A7%C3%A3o-de-impress%C3%B5es h_01HGSXTKYRN6TP3KDYX5YZJV7N=limita%C3%A7%C3%A3o-de-impress%C3%B5es h_01HGSXTKYR8BK5A2J6TJECMKZA=faq click-signing=assinatura-de-cliques h_01HGSXTKYR915V6E4NWGWR61PG=assinatura-de-cliques" />
