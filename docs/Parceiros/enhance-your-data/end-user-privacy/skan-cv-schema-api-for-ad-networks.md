---
title: API de esquema CV SKAN para ad networks
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2023-03-05T14:40:50Z'
  id: 11705009866001
  locale: pt
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/pt/articles/11705009866001
---
> **Visão geral**: veja o esquema SKAN CV conforme mapeado pelo anunciante.

<div id="skan-cv-schema-api-for-ad-networks" />

## API de esquema CV SKAN para ad networks

Com a atribuição SKAdNetwork (SKAN), os anunciantes classificam a qualidade do usuário definindo valores de conversão (CV) com base na atividade do usuário pós-instalação durante períodos de tempo específicos (janelas). <Anchor target="_blank" href="/marketers/pt/docs/skadnetwork-skan-solution-guide">Saiba mais sobre SKAN</Anchor>

O iOS informa o currículo por meio de postbacks enviados à ad network que está colocando o anúncio. A partir do iOS 15, os anunciantes também podem instruir o iOS a enviar os postbacks diretamente para a AppsFlyer.

Essa API fornece às ad networks o mapa de CV para eventos e valores de atribuição. As ad networks o usam para decodificar os postbacks que recebem.

A API retorna como um JSON aninhado. O esquema para cada aplicativo é separado. Os mapeamentos por CV estão contidos na matriz conversion\_value\_mapping.

Para usar a API, peça ao seu desenvolvedor para seguir <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">a API do esquema SKAN CV para instruções de ad networks</Anchor>. Para obter uma lista de chaves e sua descrição, clique em 200 no simulador.

**Observação**:

* A faixa de valores CV é:
  * Valor refinado da janela 1 do SKAN 4: 0-63.
  * SKAN 4 janelas 1, 2 e 3 valor aproximado: baixo, médio ou alto.
  * SKAN 3 e abaixo: 0-63
* Os anunciantes podem alterar o mapeamento do currículo a qualquer momento.
* Você, a ad network, deve consultar essa API diariamente, para garantir que tenha o esquema mais atualizado.

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=api-de-esquema-cv-skan-para-ad-networks" />
