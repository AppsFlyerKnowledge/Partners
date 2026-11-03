---
title: Atribuição de pré-carga para parceiros
metadata:
  keywords:
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-alina-koifman
    - Marketers
    - Mobile Attribution
  created_at: '2023-05-15T09:45:55Z'
  edited_at: '2026-08-18T00:40:06Z'
  id: 15321350340241
  locale: pt
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/pt/articles/15321350340241
---
> **Em resumo:** Atribua instalações de app mobile a campanhas que pré-carregam o app no Fabricante de Equipamento Original (OEM) ou quando o dispositivo é ligado pela primeira vez pelo usuário.

## Escritórios

Ao oferecer suporte às soluções de atribuição de pré-carga da AppsFlyer, os parceiros de pré-carga podem ter instalações de aplicativos atribuídas a campanhas de pré-carga. As campanhas de pré-carga se aplicam quando um aplicativo é instalado em um dispositivo por um parceiro de pré-carga, seja na fábrica ou na ativação do dispositivo (quando o dispositivo é ligado pela primeira vez).

Os parceiros de pré-carga são:

* Fabricante do equipamento original (OEM na sigla em inglês)
* Plataformas de descoberta de aplicativos
* Operadoras móveis

Há 3 maneiras de atribuir campanhas pré-carregadas:

* [Recomendado] Referrer AppsFlyer
* Google Play auto-install (PAI)
* [Legado] Pré-carregamento na fábrica via propriedade do sistema

Postbacks são enviados para você após cada conversão.

<Anchor target="_blank" href="/marketers/pt/docs/appsflyer-attribution-model#preload-campaigns">Saiba mais sobre os métodos de atribuição de campanhas de pré-carga</Anchor>

## Configurar atribuição de pré-carga

Para configurar a atribuição de pré-carga:

1. Verifique se você é um <Anchor target="_blank" href="/partners/pt/docs/getting-started-onboarding-guide-for-ad-networks">parceiro integrado da AppsFlyer</Anchor>.
2. Escolha as soluções de atribuição de pré-carga que serão integradas (com base nas necessidades do anunciante). **Observação**: Cada integração precisa de um PID independente com uma conta de parceiro da AppsFlyer. Entre em contato com a equipe de soluções para parceiros pelo widget de suporte.
   * [Recomendado] <Anchor target="_blank" href="/marketers/pt/docs/set-up-appsflyer-preload-referrer-attribution">Referrer da AppsFlyer</Anchor>: Entre em contato com seu PDM para obter instruções de integração.
   * <Anchor target="_blank" href="/marketers/pt/docs/measure-preload-campaigns-with-google-play-install">Instalação automática do Google Play (PAI)</Anchor>: Configure as informações do canal de mídia na API Google Play Referrer para campanhas PAI usando os seguintes parâmetros UTM: `utm_source=play-auto-installs&utm_medium=preload&utm_campaign=brandnamepai_int`. Por exemplo: `utm_source=play-auto-installs&utm_medium=preload&utm_campaign=xiaomipai_int`.
3. Entre em contato com a equipe de soluções para parceiros da AppsFlyer pelo widget de suporte para concluir a integração e, opcionalmente, configurar postbacks.  
   **Observação**: Veja quais macros de postback são compatíveis com o método de pré-carga do <Anchor target="_blank" href="/marketers/pt/docs/measure-preload-campaigns-with-google-play-install#postbacks-para-parceiros-de-pré-carga">Google PAI</Anchor> e do <Anchor target="_blank" href="/partners/pt/docs/postback-macros-for-ad-networks">referrer da AppsFlyer/arquivo de manifesto do Android</Anchor>.

<div data-zendesk-anchors="organic-search-attribution=escrit%C3%B3rios h_01HQFFB20SKDVW1X3ECMZCZQW0=escrit%C3%B3rios set-up-preload-attribution=configurar-atribui%C3%A7%C3%A3o-de-pr%C3%A9-carga h_01HQFFB20S6KJH3PBF5N2190TJ=configurar-atribui%C3%A7%C3%A3o-de-pr%C3%A9-carga" />
