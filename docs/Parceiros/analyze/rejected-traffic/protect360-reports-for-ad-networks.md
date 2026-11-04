---
title: Relatórios do Protect360 para ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Ad Networks
  created_at: '2022-02-08T14:53:48Z'
  edited_at: '2026-08-19T00:36:47Z'
  id: 4420246395793
  locale: pt
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/pt/articles/4420246395793
---
> **Em resumo:** As ad networks responsáveis pela aquisição de usuários e pelo retargeting podem receber dados sobre cliques e impressões bloqueados.

<div id="protect360-reports-for-ad-networks" />

## Relatórios do Protect360 para ad networks

**Aviso legal**: este artigo fornece informações sobre relatórios do Protect360 disponíveis apenas para ad networks. Para dados que também estão disponíveis para anunciantes, consulte <Anchor target="_blank" href="/partners/pt/docs/protect360-for-integrated-partners">Protect360 para parceiros integrados</Anchor>.

As ad networks podem receber relatórios por meio do <Anchor target="_blank" href="/partners/pt/docs/data-locker-for-partners">Data Locker for Partners</Anchor> com informações valiosas sobre cliques e impressões bloqueados por um dos seguintes motivos:

* Cliques e impressões bloqueados que ocorrem quando as ad networks ultrapassam seu limite de fraude. O relatório inclui o total de bloqueios, bem como bloqueios devido ao limite de cliques e impressões. <Anchor target="_blank" href="/partners/pt/docs/protect360-for-integrated-partners#limitação-de-impressões">Saiba mais sobre capping</Anchor>
* Assinaturas de clique com falha que ocorrem quando um clique com o parâmetro PID da network e uma assinatura de clique para validar cliques não podem ser validados. <Anchor target="_blank" href="/partners/pt/docs/click-signing-for-ad-networks">Saiba mais sobre assinatura de clique</Anchor>

As ad networks podem então ingerir esses dados em nível de network, com visibilidade entre clientes dos seus cliques e impressões bloqueados, e usá-los para se proteger contra fraudes.

<div id="report-considerations" />

### Considerações sobre o relatório

* Os dados chegam em formato CSV ao bucket do parceiro de UA/retargeting.
* Contém dimensões e métricas relevantes para a ad network (limpas de todas as dimensões irrelevantes para a ad network).
* Disponível via <Anchor target="_blank" href="/partners/pt/docs/data-locker-for-partners">Data Locker for Partners</Anchor>.
* Atualização dos dados: <Anchor target="_blank" href="/marketers/pt/docs/about-data-freshness-and-timezone-support#ad-revenue">Diária, ou seja, os dados do dia 0 chegam no dia 1</Anchor>. Os dados são gravados diariamente às 07:00 <Anchor target="_blank" href="/marketers/pt/docs/about-data-freshness-and-timezone-support#daily">horário UTC</Anchor> em h=23 do seu bucket do Data Locker.
* Aplicativos incluídos: um único relatório contém os dados de todos os aplicativos.

<div id="report-types" />

## Tipos de relatório

<div id="blocked-clicks-and-impressions" />

<Accordion title="Cliques e impressões bloqueados">

Este relatório contém dados em nível agregado sobre cliques e impressões que são bloqueados devido ao limite ou por qualquer outro motivo.  

<div id="report-structure-fieldsdimensions" />

#### Estrutura do relatório: Campos/Dimensões

| **Campo** | **Considerações** |
| --- | --- |
| ativado | ID do aplicativo na plataforma da AppsFlyer. |
| id\_do\_site | ID que identifica o publisher que exibe o anúncio. |
| data | Data do bloqueio |
| agency | <ul><li>Agência que trouxe o tráfego por meio desta ad network.</li><li>Retorna null se não houver agência envolvida.</li></ul> |

<div id="report-structure-metrics" />

#### Estrutura do relatório: Métricas

| **Campo** | **Considerações** |
| --- | --- |
| número\_de\_cliques\_bloqueados | Número total de cliques bloqueados da network |
| número\_de\_impressões\_bloqueadas | Número total de impressões bloqueadas da network |
| número\_de\_cliques\_limitados | O número de cliques cobertos pela ad network (do total de cliques bloqueados) |
| número\_de\_impressões\_limitadas | O número de impressões limitadas da network (do total de impressões bloqueadas) |

</Accordion>

<div id="failed-click-signatures" />

<Accordion title="Assinaturas com cliques que falharam">

Este relatório contém dados em nível de usuário sobre assinaturas de clique com falha. Ou seja, quando as ad networks usam o <Anchor target="_blank" href="/partners/pt/docs/click-signing-for-ad-networks">método de assinatura de clique da AppsFlyer</Anchor>, o relatório contém cliques de URLs com o PID da network que não têm assinaturas de clique validadas, seja porque a assinatura é inválida ou expirou, seja porque o clique não foi assinado. Falhas na assinatura de clique podem ocorrer quando há erros técnicos na implementação das assinaturas de clique pela ad network ou quando os cliques são enviados em nome da network (com seu PID) por outra parte.

<div id="report-structure-fieldsdimensions-1" />

#### Estrutura do relatório: Campos/Dimensões

| **Campo** | **Considerações** |
| --- | --- |
| event\_time |  |
| original\_url |  |
| motivo\_da\_falha\_de\_assinatura | Exemplo:<ul><li>Assinatura inválida</li><li>Assinatura faltando</li><li>Assinatura expirada</li><li>Chave secreta expirada</li></ul> |
| bloqueio\_está\_ativado | Refere-se ao modo de configuração da <Anchor target="_blank" href="/partners/pt/docs/click-signing-for-ad-networks">API de assinatura de clique</Anchor>:<ul><li>TRUE para habilitado.</li><li>FALSE para somente relatório.</li><li>Não incluído no relatório para desabilitado.</li></ul> |

</Accordion>

<div data-zendesk-anchors="protect360-reports-for-ad-networks=relat%C3%B3rios-do-protect360-para-ad-networks report-considerations=considera%C3%A7%C3%B5es-sobre-o-relat%C3%B3rio report-types=tipos-de-relat%C3%B3rio report-structure-fieldsdimensions=estrutura-do-relat%C3%B3rio-camposdimens%C3%B5es report-structure-metrics=estrutura-do-relat%C3%B3rio-m%C3%A9tricas report-structure-fieldsdimensions::44afb679=estrutura-do-relat%C3%B3rio-camposdimens%C3%B5es-1" />
