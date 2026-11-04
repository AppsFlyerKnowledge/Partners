---
title: Gerenciamento de integração de autoatendimento para ad networks
metadata:
  keywords:
    - postbacks
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2021-03-15T10:03:41Z'
  edited_at: '2026-08-19T00:38:29Z'
  id: 360018512658
  locale: pt
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/pt/articles/360018512658
---
> **Visão geral**: Configure e gerencie sua integração a partir do painel da AppsFlyer.

<Embed title="Gerenciamento de integração de autoatendimento para ad networks" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/medias/9kvwrhnzjo/swatch" providerUrl="https://fast.wistia.com" />

<div id="prerequisites" />

## **Pré-requisitos:**

* É necessário ter credenciais de login (nome de usuário e senha) para a AppsFlyer antes de poder gerenciar links de atribuição e postbacks. Para <Anchor target="_blank" href="/partners/pt/docs/getting-started-onboarding-guide-for-ad-networks">criar uma</Anchor> conta de <Anchor target="_blank" href="/partners/pt/docs/getting-started-onboarding-guide-for-ad-networks">parceiro</Anchor>, peça a um cliente da AppsFlyer (anunciante) para <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#convide-novos-parceiros-para-a-appsflyer">convidar você</Anchor>.
* A gestão de links de atribuição e postbacks predefinidos está disponível apenas para parceiros que aderiram após 1 de fevereiro de 2022.
* Verifique se os seus servidores estão prontos para receber postbacks, cumprindo o seguinte:
  * Inclua os <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-server-ip-address-ranges-allowlisting">endereços IP</Anchor> do servidor da AppsFlyer na lista de permissões dos seus sistemas de firewall e segurança para garantir a comunicação com o endpoint.
  * Versões TLS: TLS 1.1, TLS 1.2+ com as <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-https-ssl-encryption-policy-support#mensagens-de-saída-appsflyer-como-cliente">cifras indicadas.</Anchor>
  * Portas: 80, 443
* ![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Apenas os usuários Admin podem acessar e gerir esta seção.

<div id="accessing-integration-management" />

## Gerenciamento de integração %(name) s

1. Faça login na sua conta de parceiro da AppsFlyer.
2. Clique no menu suspenso superior direito > **Gerenciamento de postback**.

<div id="attribution-link" />

## Link de atribuição

O link de atribuição é a parte mais importante da sua integração. Os links de atribuição são usados para notificar a AppsFlyer sobre o engajamento do usuário com um anúncio. Os links de atribuição são colocados por trás dos anúncios, pelo que quando um usuário clica num anúncio está clicando em um link de atribuição.

A conclusão da configuração do link de atribuição é obrigatória

**Para configurar o link de atribuição:**

1. Na aba **Link de atribuição** , adicione os parâmetros a incluir em seu link de atribuição:

   * Nome do parâmetro: Nome da tela do parâmetro AppsFlyer.
   * **Sua macro**: adicione a macro que preenche os parâmetros com valores.
   * **Incluir**: selecione a caixa para incluir o parâmetro no link

   <div id="important" />

   > 🚧 **Importante!**
   >
   > * Adicione parâmetros relacionados com a campanha e os anúncios para fornecer dados mais sólidos sobre o desempenho da campanha.
   > * **O ID do site** é um parâmetro obrigatório
   > * Os anunciantes usam este link como base para a integração de um aplicativo específico e podem acrescentar parâmetros adicionais a ele.
   > * A ID do aplicativo, a duração da janela de lookback e a ID do parceiro são adicionados automaticamente ao link e não é necessário adicioná-los a este modelo.

2. **[Opcional]** Adicione parâmetros personalizados que não são fornecidos pela AppsFlyer:
3. Use a pré-visualização do link para verificar se tudo está correto.
4. Clique em **Salvar**.

<Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">Mais informações sobre links de atribuição e parâmetros disponíveis</Anchor>.

Em caso de problemas, entre em contato pelo <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget do assistente de parceiro</Anchor>.

<div id="default-postback" />

## Postback padrão

Postbacks são URLs contendo macros preenchidas pela AppsFlyer e enviadas para os seus servidores em tempo real após cada conversão (na sua rede ou em outras redes também - dependendo da sua configuração).

**Para configurar o postback predefinido:**

1. Insira os **endereços dos endpoints.** Estes são os endpoints para os quais são enviados postbacks. Introduza os URLs relevantes para instalações, eventos in-app ou ambos. Para poder ativar a integração, é necessário pelo menos o URL de instalação do postback.
2. Adicionar parâmetros ao postback:

   * Nome do parâmetro: Nome da tela do parâmetro AppsFlyer.
   * **Seu parâmetro de recebimento**: o respectivo parâmetro de recebimento do seu lado
   * **Valor do parâmetro** (disponível para alguns parâmetros): escolha o formato do valor. Por exemplo, para valores booleanos, escolha se deseja recebê-los como "true"/"false" ou 1/0.
   * **Instalação**: marque a caixa para incluir o parâmetro no postback de instalação.
   * **Evento in-app**: marque a caixa para incluir o parâmetro no postback do evento in-app.

   <Anchor target="_blank" href="/partners/pt/docs/postback-macros-for-ad-networks">Lista completa de macros de postback</Anchor>

   <div id="important-1" />

   > 🚧 **Importante!**
   >
   > * Para distinguir entre postbacks de eventos legítimos e postbacks rejeitados, é necessário configurar os postbacks das macros rejeitadas.
   > * Para ativar postbacks de eventos de instalação/in-app rejeitados, anexe os seguintes parâmetros ao seu modelo de postback predefinido:
   >   * `is-rejected`
   >   * `motivo-do-bloqueio`
   >   * `blocked-sub-reason`
   >   * `blocked-reason-value`  
   >     **Observação:** Se o postback de Privacidade avançada estiver ativado, anexe os parâmetros acima ao template de Privacidade avançada também.

3. [Opcional] **Parâmetros personalizados:** Configure seus próprios parâmetros para incluir no postback
4. Utilize a pré-visualização do template de postback para verificar se tudo está certo.
5. Clique em **Salvar**.

<Anchor target="_blank" href="/marketers/pt/docs/in-app-event-postback-configuration">Mais informações e exemplos de postback.</Anchor>

Em caso de problemas, use o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget do assistente do parceiro</Anchor>.

<div id="advanced-privacy-and-skan-postbacks" />

## Privacidade avançada e postbacks SKAN

Os postbacks de Privacidade Avançada e SKAN só podem ser configurados depois de o link de atribuição e o postback predefinido terem sido criados.

**Para gerenciar os postbacks:**

1. Selecione um tipo de postback:
   * Postback de privacidade avançada
   * Postback da <Anchor target="_blank" href="/partners/pt/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>.
2. Ative o construtor.
3. **[Apenas para configuração de postback de SKAdNetwork]** Introduza sua ID de SKAdNetwork. Este campo é obrigatório e a configuração não pode ser guardada sem uma ID válida.
4. Insira os **endereços dos endpoints.** Estes são os endpoints para os quais são enviados postbacks. Introduza os URLs relevantes para instalações, eventos in-app ou ambos.
5. Adicionar parâmetros de postback:

   * Nome do parâmetro: Nome da tela do parâmetro AppsFlyer.
   * Seu parâmetro de recebimento: O respetivo parâmetro de recebimento do seu lado.
   * **Valor do parâmetro** (disponível para alguns parâmetros): Selecionar o formato do valor. Por exemplo, para valores booleanos, escolha se deseja recebê-los como "true"/"false" ou 1/0.
   * **Instalação**: marque a caixa para incluir o parâmetro no postback de instalação.
   * Evento in-app: marque a caixa para incluir o parâmetro no postback do evento in-app.

   Lista de <Anchor target="_blank" href="/partners/pt/docs/skan-integration-guide-for-ad-networks#receber-dados-da-appsflyer">macros de postback da SKAdNetwork</Anchor>

   Lista completa de <Anchor target="_blank" href="/partners/pt/docs/advanced-privacy-guide-postback-macros-for-ad-networks#advanced-privacy-postback-specification">macros de postback de Privacidade Avançada.</Anchor>

   <div id="important-2" />

   > 🚧 **Importante!**
   >
   > * Para ativar postbacks de eventos de instalação/in-app rejeitados, anexe os seguintes parâmetros ao seu modelo de postback predefinido:
   >   * `is-rejected`
   >   * `motivo-do-bloqueio`
   >   * `blocked-sub-reason`
   >   * `valor-do-motivo-do-bloqueio`
   > * Para ativar os postbacks rejeitados para Advance Privacy, primeiro você deve anexar os parâmetros acima ao [postback Default](/docs/self-serve-integration-management-for-ad-networks#postback-padrão)
   > * Quando os parâmetros acima são adicionados ao postback Padrão e ao postback Privacidade avançada (se ativado), os postbacks de eventos de instalação/in-app rejeitados são ativados.

6. [Opcional] **Parâmetros personalizados:** Configure seus próprios parâmetros para incluir no postback
7. Utilize a pré-visualização do template de postback para verificar se tudo está certo.
8. Clique em **Salvar**.  
   Observe que, quando você salva o postback, as alterações entram em vigor imediatamente.

Em caso de problemas, contacte-nos usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget do assistente de parceiro</Anchor>.

<div data-zendesk-anchors="prerequisites=pr%C3%A9-requisitos h_01KZTVV00EB224GJD5F7VBP071=pr%C3%A9-requisitos accessing-integration-management=gerenciamento-de-integra%C3%A7%C3%A3o-name-s h_01H9FCSTYR157CCJWTYSNE9JQ0=gerenciamento-de-integra%C3%A7%C3%A3o-name-s attribution-link=link-de-atribui%C3%A7%C3%A3o h_01H9FCSTYR6HRSF9F8KCR4B3X7=link-de-atribui%C3%A7%C3%A3o h_01H9FCSTYR4Q1985DTHNE1M1CC=importante default-postback=postback-padr%C3%A3o h_01H9FCSTYR2WX0M0ZW3B22EKBM=postback-padr%C3%A3o h_01H9FCSTYSEP367WAAKCFHZT58=importante-1 advanced-privacy-and-skan-postbacks=privacidade-avan%C3%A7ada-e-postbacks-skan h_01H9FCSTYSRKBMYR2BYNQJJKVM=privacidade-avan%C3%A7ada-e-postbacks-skan h_01H9FCSTYSEJD59AWCFNXDZMYW=importante-2" />
