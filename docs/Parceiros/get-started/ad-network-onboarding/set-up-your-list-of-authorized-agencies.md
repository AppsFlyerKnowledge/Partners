---
title: Configure sua lista de agências autorizadas
metadata:
  keywords:
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
  created_at: '2024-06-09T19:29:56Z'
  edited_at: '2026-08-18T00:40:11Z'
  id: 25774607860113
  locale: pt
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/pt/articles/25774607860113
---
> **Visão geral:** Gerencie quais agências você autoriza a executar campanhas por meio de sua integração de rede.

<div id="overview" />

## Visão geral

Para evitar o uso não autorizado da sua rede, todas as agências que executam campanhas por meio da sua integração de rede devem ser pré-aprovadas. Isso é feito adicionando o ID da agência (`af_prt`) à sua lista de agências autorizadas. As agências que não aparecem na lista não conseguem configurar a integração, pois a janela de configuração do parceiro fica esmaecida. Isso impede que elas gerenciem campanhas. A aprovação é no nível da conta, o que significa que, uma vez que uma agência é aprovada, ela tem acesso a todos os aplicativos que executam campanhas em sua rede.

A partir de 31 de julho de 2024, apenas o tráfego de agências autorizadas pelas ad networks será registado e medido na AppsFlyer. Tráfego não autorizado resultará em uma resposta 403 (Proibido) do AppsFlyer.

<div id="note" />

> 📘 **Observação**
>
> * Isso não se aplica a agências que trabalham com <Anchor target="_blank" href="/marketers/pt/docs/self-reporting-networks-srns">SRNs</Anchor>
> * Somente administradores têm acesso a esta página
> * A lista de agências autorizadas pode incluir até 200 agências

<Image align="center" alt="authorized-agencies-5.jpg" src="https://files.readme.io/10012bde55cffa967f2e581420a9c32b7ce8b9cb120e203ba230bf7f271b0d9a-25977984018833.jpg" />

<div id="manage-authorized-agencies" />

## Gerenciar agências autorizadas

Na página **Agências autorizadas**, você pode adicionar agências, visualizar a lista existente de agências que você aprovou para executar campanhas em sua rede e excluir agências que você não aprova. A página inclui duas seções:

* Painel esquerdo: Adicionar novas agências
* Painel direito:
  * Veja a lista de agências aprovadas
  * Excluir agências

**Para acessar a página Agências autorizadas:**

1. Na barra superior, abra o menu da conta (menu dropdown de endereço de e-mail) > **Central de segurança.**
2. Na seção **Agências autorizadas**, clique em **Gerenciar agências autorizadas**.

<div id="add-an-agency-to-the-list" />

### Adicionar uma agência à lista

1. No painel esquerdo da página **Agências autorizadas**, insira o ID da agência.
2. Clique em **Adicionar à lista**. A agência agora aparece no painel à direita.
3. [Opcional] Repita as etapas 1 a 2 para adicionar mais agências.
4. Clique em **Salvar lista**.

<div id="note-1" />

> 📘 **Observação**
>
> Certifique-se de inserir um ID de agência válido. Por exemplo (af\_prt=) `my_agency_123`

<div id="delete-an-agency-from-the-list" />

### Excluir uma agência da lista

1. No painel direito da página **Agências autorizadas**, passe o mouse sobre a agência que você deseja excluir e clique no ícone da lixeira.
2. Confirme a exclusão. Uma indicação confirma a exclusão bem-sucedida da agência.
3. [Opcional] Repita as etapas 1 a 2 para excluir outras agências.

<div data-zendesk-anchors="overview=vis%C3%A3o-geral h_01HJR00RGQ2PK3T8BB2ZG3PFQN=vis%C3%A3o-geral h_01HJR00RGQX0CQEHDS9BHBGJD4=observa%C3%A7%C3%A3o accessing-the-allowlists=gerenciar-ag%C3%AAncias-autorizadas h_01HZZ5FP1560HJYDVDNSJ8WAAP=gerenciar-ag%C3%AAncias-autorizadas add-an-agency-to-the-list=adicionar-uma-ag%C3%AAncia-%C3%A0-lista h_01HZZ691KMKTYVAETT4RM3AD97=adicionar-uma-ag%C3%AAncia-%C3%A0-lista h_01HZZ7QGY0VTS0FY0HJJAZ2AXV=observa%C3%A7%C3%A3o-1 h_01HJR00RGQ4ZEGE0RDK01S5SQQ=excluir-uma-ag%C3%AAncia-da-lista" />
