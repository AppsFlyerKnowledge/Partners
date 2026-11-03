---
title: Opções de compartilhamento de custos para ad networks
metadata:
  keywords:
    - clicks
    - Partner
    - cost
    - Ad Networks
    - Partners
    - ad spend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2020-09-07T13:50:24Z'
  edited_at: '2026-08-18T00:38:41Z'
  id: 360012893658
  locale: pt
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/pt/articles/360012893658
---
> **Visão geral:** Compare os métodos de compartilhamento de custos disponíveis para as ad networks parceiras da AppsFlyer.

## Compartilhando custos com a AppsFlyer e anunciantes

Anunciantes usam a AppsFlyer como uma fonte confiável para entender seu ROI, faturamento e para tomar decisões de distribuição do seu orçamento de marketing. Para que as ad networks se destaquem, é necessário que elas compartilhem os dados de custo com a AppsFlyer. Ad networks que não possuem dados de custo são exibidas no final da lista no dashboard da AppsFlyer.

As ad networks compartilham dados de custo usando qualquer um desses métodos: 

* **InCost API**: os dados são enviados para a AppsFlyer
* **Cost API**: a AppsFlyer extrai os dados
* **Cost Import**: os arquivos de dados de custo são enviados para a AppsFlyer
* **Custo por clique:** as ad networks relatam o custo cada vez que um link de atribuição recebe um clique

### Cost badge para ad networks

![CostBadge.jpg](https://files.readme.io/6b660b68b932802f7982a3beb3a155ecc350de1b4cb3baede6e84ef0d704388c-360011247338.jpg)

* Um cost badge é exibido na <Anchor target="_blank" href="/marketers/pt/docs/partner-integrations#partner-details-and-performance">página de informações do parceiro</Anchor>, destacando os parceiros que usam a InCost ou Cost API.
* Esse badge é a garantia de que o parceiro possui capacidades de custo.
* Análises internas e extensas pesquisas feitas com nossos usuários apontam que os anunciantes estão sempre à procura de novos parceiros. Aqueles que possuem um cost badge têm mais chances de se destacar, pois os anunciantes querem entender sua performance de marketing com base na análise do ROI.

### Opções de relatórios de custo disponíveis para ad networks

| Opção | Qualifique-se para um cost badge | Mais informações |
| --- | --- | --- |
| <Anchor target="_blank" href="/partners/pt/docs/incost-api-for-ad-networks">InCost API</Anchor> | ✓ | A ad networks tem total propriedade da configuração do relatório InCost.<br /><br />A InCost possui os seguintes recursos:<ul><li>Suporte para todos os modelos de custo</li><li>Precisa e confiável</li><li>Totalmente automatizada</li><li>A ad network parceira controla:<ul><li>Esquema de upload de dados</li><li>Quando o upload é feito (atualização de dados)</li></ul></li><li>O anunciante permite que o parceiro faça o upload de dados de custo em seu dashboard da AppsFlyer</li></ul>**Limitação**:<br /><br />Sem suporte para as contas de agência na AppsFlyer. |
| Cost API | ✓ | <ul><li>Suporte para todos os modelos de custo</li><li>Precisa</li><li>O parceiro mantém um certo controle sobre seus dados de custo na AppsFlyer</li><li>Compatível com o custo para contas de agência na AppsFlyer</li><li>Os anunciantes fornecem suas credenciais de parceiro no dashboard da AppsFlyer</li><li>Atualização de dados: 6 vezes ao dia, a cada quatro horas</li></ul>**Limitação**:<br /><br />A integração está sujeita às prioridades da AppsFlyer. |
| <Anchor target="_blank" href="/partners/pt/docs/cost-import-for-ad-networks">Importação de custos</Anchor><br /><br />(upload do arquivo) | Não | <ul><li>A ad network parceira:<ul><li>Faz o upload manual dos dados, caso ela não tenha os recursos necessários para automatizar esse processo</li><li>Controla quando é feito o upload</li><li>Mantém um certo controle sobre seus dados de custo na AppsFlyer</li><li>A integração é feita por aplicativo. O anunciante permite que o parceiro faça o upload de dados de custo em seu dashboard da AppsFlyer.</li><li>A correspondência com os dados de atribuição se baseia no nome da campanha (não no ID da campanha)</li></ul></li></ul>**Limitação**:<ul><li>Sem suporte para as contas de agência na AppsFlyer.</li><li>Risco de falha se o upload for automatizado via e-mail</li></ul> |
| <Anchor target="_blank" href="/partners/pt/docs/cost-reporting-on-the-attribution-link-for-ad-networks">Custo por clique</Anchor><br /><br />(no link de atribuição) | Não | <ul><li>Solução rápida para campanhas de CPI</li><li>Quase em tempo real</li><li>O custo por clique pode ser menos preciso se o anunciante usar a SKAdNetwork</li></ul>**Limitação**:<ul><li>Limitado ao modelo de custo do CPI</li><li>Se os dados errados forem enviados no link, eles não poderão ser alterados</li><li>Sem suporte para retargeting</li><li>O custo relatado por clique é exibido no dashboard da SKAdNework, quando disponível</li></ul> |

<div data-zendesk-anchors="sharing-cost-with-appsflyer-and-advertisers=compartilhando-custos-com-a-appsflyer-e-anunciantes h_01HN0A1ER3MNZM508ZCG9KP26P=compartilhando-custos-com-a-appsflyer-e-anunciantes cost-badge-for-ad-networks=cost-badge-para-ad-networks h_01HN0A1ER4K1V4479W5SXCEC30=cost-badge-para-ad-networks reporting-cost-options-available-to-ad-networks=op%C3%A7%C3%B5es-de-relat%C3%B3rios-de-custo-dispon%C3%ADveis-para-ad-networks h_01HN0A1ER4Y128ZHJERXS6A8ET=op%C3%A7%C3%B5es-de-relat%C3%B3rios-de-custo-dispon%C3%ADveis-para-ad-networks" />
