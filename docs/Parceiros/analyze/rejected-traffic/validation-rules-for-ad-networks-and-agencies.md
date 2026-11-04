---
title: Regras de validação para ad networks e agências
metadata:
  keywords:
    - Agency
    - Networks
    - Validation Rules
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2017-09-18T13:53:49Z'
  edited_at: '2026-08-18T00:38:23Z'
  id: 115004751486
  locale: pt
  section: Rejected traffic
  section_id: 6551666000273
  url: https://support.appsflyer.com/hc/pt/articles/115004751486
---
> **Visão geral:** os anunciantes usam as regras de validação para definir manualmente as condições para bloquear instalações, atribuição e eventos in-app de instalações/IAEs não compatíveis. Os parceiros integrados (ad networks e agências) podem visualizar as regras e obter relatórios de instalações bloqueadas, atribuição e IAEs.

<div id="about-validation-rules" />

## Sobre as regras de validação

Regras de validação:

* São definidas pelo anunciante em um criador de regras usando condições e lógica personalizadas que filtram e selecionam quais instalações de aplicativos ou eventos in-app devem ser mantidos ou bloqueados.
* São baseadas em uma variedade de parâmetros para vários casos de uso, incluindo:
  * Instalações não direcionadas para sua campanha (geolocalização ou versão do sistema operacional errada etc.)
  * Instalações que não atendam à ordem de inserção assinada entre o anunciante e você.
  * Instalações sequestradas por editores fraudulentos, malware etc.
  * Instalações falsas ou eventos in-app enviados de bots, emuladores ou device farms.
* Definidas para eventos in-app só entram em vigor em IAEs associadas a instalações que não foram bloqueadas anteriormente.
* Isso inclui uma ad network visível para essa ad network (mas eles não podem ver outras ad networks incluídas na regra).
* Executadas em tempo real e tomam medidas imediatas. Um postback de rejeição é enviado para parceiros que rejeitaram postbacks configurados. <Anchor target="_blank" href="/partners/pt/docs/rejected-attribution-postbacks-to-integrated-partners">Saiba mais</Anchor>.
* Opções adicionais de regras de validação estão disponíveis para os clientes do <Anchor target="_blank" href="/marketers/pt/docs/protect360-anti-fraud-guide">Protect360</Anchor>, além do bloqueio e detecção automáticos de fraudes do Protect360. Essas condições são conhecidas por ajudar na detecção de vários tipos de hijacking de instalação, instalação falsa e fraude de eventos in-app falsos.

<div id="availability-to-ad-networks-and-agencies" />

## Disponibilidade para ad networks e agências

As regras que regem o acesso às redes e agências de publicidade são as seguintes:

* Os parceiros integrados podem ver a lista de regras de validação que se aplicam a eles.
  * Eles veem que outros parceiros estão incluídos na regra, embora os outros nomes de parceiros não sejam revelados.
  * Se uma regra de validação se aplica a vários aplicativos, mas um parceiro só está integrado para um ou alguns dos aplicativos, ele só pode ver a regra e o aplicativo para o qual está integrado.
* Para clicar em uma regra específica e visualizar seus detalhes, é necessário a permissão do anunciante para **Ver regras de validação**.
  * Por padrão, a permissão fica desativada.
  * Se estiver desativada, um parceiro pode clicar em **Solicitar acesso**. O anunciante recebe então uma notificação do pedido.
* Uma ad network não pode criar ou editar regras.

<div id="agencies" />

### Agências

As regras que regem o acesso a regras de validação adicionais às agências são as seguintes:

* As agências podem criar, editar e excluir regras, se tiverem permissão do anunciante para **Adicionar regras de validação**.
  * As agências só podem editar ou apagar regras que elas criam, não as criadas pelo anunciante.
* Para adicionar regras com as condições da Protect360:
  * O anunciante precisa ter uma assinatura do Protect360.
  * É necessária a permissão do anunciante para **Acessar o painel do Protect360 e dados brutos**.
* Se uma agência faz uma regra para múltiplos aplicativos com os quais está integrada, e então a integração para um ou mais aplicativos é removida pelo anunciante, a regra é dividida em regras separadas para cada aplicativo, e as regras para os aplicativos que não estão integrados ficam inativas.

**Para acessar as regras de validação**:

1. Na AppsFlyer, no menu lateral, selecione **configurações** > **regras de validação**.
2. Para exibir a regra de validação, selecione uma **conta de proprietário do aplicativo**.
   * A lista de regras definidas pela conta do proprietário do aplicativo para o tráfego que pode vir de você é exibida.
   * Para obter uma explicação de como os conjuntos de regras funcionam, consulte <Anchor target="_blank" href="/marketers/pt/docs/implement-validation-rules-to-prevent-fraud">Regras de validação para proprietários de aplicativos</Anchor>.

<div id="reports" />

## Relatórios

<div id="protect360-fraud-export-data" />

### Fraude Protect360: exportar dados

Os anunciantes podem conceder aos parceiros (ad networks e agências) <Anchor target="_blank" href="/marketers/pt/docs/raw-data-reporting-overview#protect360-fraud-and-validation-rules">permissão</Anchor> para baixar os seguintes relatórios em **Relatórios** > **Exportar dados**:

* Instalações: instalações bloqueadas ou instalações com atribuição bloqueada.
* Eventos in-app bloqueados: eventos in-app rejeitados (requer que o anunciante tenha uma assinatura do Protect360).
* Postbacks de instalação bloqueados: um único relatório dos postbacks de rejeição enviados a você em tempo real.

Os campos **Motivo da rejeição** e **Valor do motivo da rejeição** são preenchidos nos relatórios. O **Valor do motivo da rejeição** inclui o nome da regra que causou a rejeição.

<div id="validation-rules-rejected-installation-postbacks" />

## Regras de validação rejeitaram postbacks de instalação

Os parceiros integrados que se integram à AppsFlyer podem <Anchor target="_blank" href="/partners/pt/docs/rejected-attribution-postbacks-to-integrated-partners">receber postbacks de instalação bloqueados</Anchor> em tempo real sempre que uma instalação for rejeitada devido à aplicação das regras.

Entre em contato com seu representante de desenvolvimento de parceiros para mais detalhes.

<div data-zendesk-anchors="about-validation-rules=sobre-as-regras-de-valida%C3%A7%C3%A3o h_01HKA04414ZAS0EZX6AGHVTZHY=sobre-as-regras-de-valida%C3%A7%C3%A3o availability-to-ad-networks-and-agencies=disponibilidade-para-ad-networks-e-ag%C3%AAncias h_01HKA04415K37N997EDS8X26PK=disponibilidade-para-ad-networks-e-ag%C3%AAncias agencies=ag%C3%AAncias h_01HKA044155S4Y7DAGP05S5FJA=ag%C3%AAncias reports=relat%C3%B3rios h_01HKA04415P5K6J4VXS64GA2SP=relat%C3%B3rios protect360-fraud-export-data=fraude-protect360-exportar-dados h_01HKA0441501DKTQHT3X0G0RC7=fraude-protect360-exportar-dados validation-rules-rejected-installation-postbacks=regras-de-valida%C3%A7%C3%A3o-rejeitaram-postbacks-de-instala%C3%A7%C3%A3o h_01HKA04415BR5XJABRHSWYTTS7=regras-de-valida%C3%A7%C3%A3o-rejeitaram-postbacks-de-instala%C3%A7%C3%A3o" />
