---
title: Pontuação de riqueza de dados para redes de anúncios
metadata:
  keywords:
    - Ad Networks
    - Partners
    - attribution link
    - data richness score
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-06-03T09:27:03Z'
  edited_at: '2026-08-18T00:40:38Z'
  id: 360009443338
  locale: pt
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/pt/articles/360009443338
---
> **Em resumo:** melhore a qualidade dos dados que você fornece aos anunciantes usando a pontuação de riqueza de dados da AppsFlyer.

A qualidade dos dados que os anunciantes recebem das ad networks nas quais executam suas campanhas pode desempenhar um papel importante nas decisões de marketing.

Os dados fornecidos por diferentes ad networks variam em termos de cobertura, precisão e granularidade. Dados parciais e imprecisos reduzem a capacidade dos anunciantes de analisar e otimizar a performance de suas campanhas na AppsFlyer.

A pontuação de riqueza de dados, uma métrica fornecida pela AppsFlyer, indica a abrangência dos dados das ad networks. Essa pontuação está disponível para todos os anunciantes, para que possam entender os recursos e a qualidade dos dados de cada network e tomar decisões de negócios fundamentadas.

Para maximizar a pontuação, as ad networks devem superar as lacunas de dados que têm.

<div id="data-richness-score" />

## Pontuação de riqueza de dados

**Para ver sua pontuação de riqueza de dados:**

1. Faça login na sua conta.
2. Abra o dashboard de qualquer aplicativo que você gerencia.
3. Clique em **Integrações ativas** na barra lateral esquerda.  
   O indicador de pontuação é exibido abaixo do nome da sua network.

   <Image align="center" alt="integrated-partners-data-richness.png" src="https://files.readme.io/ee68f4ba63ef4e27292ed6b857e2cd05e4d83f8ba65a80655d1bf8b63df94f5f-360009360018.png" />

Os anunciantes podem ver a pontuação de riqueza de dados (baixa, média ou alta) de cada ad network que tenha uma integração com a AppsFlyer.

<div id="included-data" />

### Dados incluídos

Para ver a pontuação em cada categoria de dados incluída na pontuação, passe o cursor sobre o indicador. Um pop-up é aberto, apresentando a pontuação final e os grupos de dados: dados da campanha, dados do anúncio e dados do publisher.

Para receber uma pontuação alta, os seguintes parâmetros devem ser fornecidos por uma ad network em todos os cliques e visualizações:

* Dados da campanha:
  * ID da campanha
  * Campaign name
* Dados do anúncio:  
  * Adset ID
  * Nome do Adset
  * ID do anúncio
  * Ad name
  * Tipo de anúncio
* Dados do editor
  * ID do site
  * ID do subsite
  * Canal

<div id="data-threshold" />

### Limite de dados

* A pontuação é calculada semanalmente e pode subir ou cair dependendo da integridade dos parâmetros listados acima.
* Há uma quantidade mínima de conversões (instalações, reatribuições, reengajamentos) necessária para que a pontuação seja calculada. Se a network tiver menos conversões do que o mínimo em uma determinada semana, na semana seguinte o indicador de pontuação será desativado e nenhuma categoria de dados será exibida.

<div id="next-steps" />

## Próximas etapas

Para adicionar mais parâmetros e melhorar sua integração e visibilidade na plataforma AppsFlyer,

1. Verifique quais parâmetros estão faltando na sua integração.
   * <Anchor target="_blank" href="/partners/pt/docs/getting-started-onboarding-guide-for-ad-networks#parte-1-integração-e-testes">Leia sobre modelos de link de atribuição</Anchor>
   * <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters#parâmetros-do-link-de-atribuição">Verifique a lista completa de parâmetros disponíveis para uso</Anchor>
2. Entre em contato com seu PDM para atualizar o modelo de link ou obter mais informações.

<div data-zendesk-anchors="data-richness-score=pontua%C3%A7%C3%A3o-de-riqueza-de-dados included-data=dados-inclu%C3%ADdos data-threshold=limite-de-dados next-steps=pr%C3%B3ximas-etapas" />
