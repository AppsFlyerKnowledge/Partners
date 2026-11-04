---
title: ROI360 — opções de relatórios de custo para agências
metadata:
  keywords:
    - clicks
    - cost
    - Agencies
    - Partners
    - ad spend
    - Xpend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Agencies
    - ROI360
  created_at: '2020-10-04T15:07:34Z'
  edited_at: '2026-08-18T00:38:46Z'
  id: 360014054998
  locale: pt
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/pt/articles/360014054998
---
> **Em resumo:** Reporte dados de custo pela API de custo (requer uma assinatura da solução premium ROI360) e custo por clique.

<div id="cost-reporting-for-agencies" />

## Relatórios de custo para agências

Anunciantes usam a AppsFlyer como uma fonte confiável para entender seu ROI, faturamento e para tomar decisões de distribuição do seu orçamento de marketing. Para fazer isso, elas precisam ter todas as informações de custo em uma única plataforma. O ROI360, uma solução premium da AppsFlyer, permite que anunciantes e agências coletem dados de custo via API, disponibilizando-os para visualização nos dashboards e nas ferramentas de relatório da AppsFlyer. 

Os dados de custo podem ser agregados por um dos seguintes métodos: 

* **API de custo**: a AppsFlyer extrai dados dos parceiros
* **Custo por clique:** networks reportam o custo cada vez que um link de atribuição é clicado

A tabela a seguir lista os recursos de agregação de custo disponíveis com e sem o ROI360.

| Opção | Requer assinatura do ROI360 | Descrição |
| --- | --- | --- |
| <Anchor target="_blank" href="/marketers/pt/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">Cost API</Anchor> | Yes | <ul><li>As agências usam as credenciais da API da ad network para se conectar e habilitar a API de custo no dashboard da AppsFlyer.</li><li>Os dados de custo são refletidos de acordo com a <Anchor target="_blank" href="/marketers/pt/docs/view-agency-data">transparência da agência</Anchor>. (Para SRNs, isso inclui cliques e impressões.)</li><li>Suporte para todos os modelos de custo</li><li>Precisa</li><li>Atualização de dados: 6 vezes ao dia, a cada quatro horas.</li></ul> |
| <Anchor target="_blank" href="/partners/pt/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Custo por clique</Anchor><br /><br />(no link de atribuição) | Sem | <ul><li>As agências enviam o CPI, o valor e a moeda de custo no link de atribuição. A AppsFlyer agrega o custo.</li><li>Atualização dos dados: quase em tempo real</li></ul>**Limitações:**<ul><li>Limitado ao modelo de custo do CPI</li><li>Se os dados errados forem enviados no link, eles não poderão ser alterados.</li><li>O custo reportado por clique não está disponível no dashboard do SKAdNework.</li><li>O custo por clique pode ser menos preciso se o anunciante usar a SKAdNetwork.</li></ul> |

<div data-zendesk-anchors="cost-reporting-for-agencies=relat%C3%B3rios-de-custo-para-ag%C3%AAncias" />
