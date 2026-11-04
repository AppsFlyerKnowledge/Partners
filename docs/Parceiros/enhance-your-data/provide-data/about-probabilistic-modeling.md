---
title: Sobre modelagem probabilística
metadata:
  keywords:
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2025-10-21T14:32:11Z'
  edited_at: '2026-08-18T00:38:58Z'
  id: 40188089592209
  locale: pt
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/pt/articles/40188089592209
---
> **Resumo:** configure seus dados de engajamento para garantir que a AppsFlyer aplique a modelagem probabilística quando sinais determinísticos não estiverem disponíveis.

<div id="about-probabilistic-modeling" />

## Sobre modelagem probabilística

A AppsFlyer usa a modelagem probabilística como um método estatístico seguro para criar relatórios de performance das campanhas de marketing de aplicativos. Esse modelo gera relatórios agregados de performance a nível de campanha.

**Características de implementação**

* Usa estatísticas e não se baseia em IDs exclusivos.
* É um método com fallback, utilizado quando referrer ou advertising IDs estão indisponíveis. Métodos determinísticos de atribuição, ou seja, cliques com referrer ou ID matching recebem prioridade se ocorrerem dentro da janela de lookback.

<div id="when-is-probabilistic-modeling-used" />

### Quando usamos o modelo probabilístico?

O modelo é aplicado sempre que dados determinísticos não estão disponíveis. Se o cliente optar por não aplicá-lo, a modelagem probabilística não é implementada. Veja abaixo alguns exemplos nos quais o modelo pode ser utilizado:

* Conversões web-to-app
* Experiências cross-device (por exemplo, um anúncio visualizado no desktop seguido de uma instalação no mobile)
* Ambientes de CTV, PC e console, onde não é possível realizar a atribuição determinística

<div data-zendesk-anchors="about-probabilistic-modeling-attribution=sobre-modelagem-probabil%C3%ADstica h_01K83JWQ84H0P1WABG939X55KD=sobre-modelagem-probabil%C3%ADstica when-is-probabilistic-modeling-used=quando-usamos-o-modelo-probabil%C3%ADstico h_01K83JWQ8412VK2ZN39CQ5TJEZ=quando-usamos-o-modelo-probabil%C3%ADstico" />
