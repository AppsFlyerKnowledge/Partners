---
title: Integração de parceiros de gerenciamento de campanha da Meta com a AppsFlyer
metadata:
  keywords:
    - Callbacks
    - Integration
    - Facebook
    - Partner
    - In-App
    - partner account
    - User Level
    - Data policy
    - FMP
    - Partners
    - Developers
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
  created_at: '2015-03-29T12:38:26Z'
  edited_at: '2026-08-18T00:40:48Z'
  id: 207034146
  locale: pt
  section: Marketing partner onboarding
  section_id: 6551118224657
  url: https://support.appsflyer.com/hc/pt/articles/207034146
---
> **Visão geral:** Saiba quais tipos de dados os parceiros de gerenciamento de campanha do Meta podem receber da AppsFlyer.

<div id="install-postbacks" />

## Postbacks de instalação

Após a conversão, a AppsFlyer pode retornar os seguintes parâmetros:

| Nome do parâmetro | Convenção de nome do parâmetro |
| --- | --- |
| Nome da campanha | `{campaign_name}` |
| ID da campanha | `{campaign_id}` |
| Nome do conjunto de anúncios | `{adset_name}` |
| ID do conjunto de anúncios | `{adset_id}` |
| Nome do grupo de anúncios | `{adgroup_name}` |
| ID do grupo de anúncios | `{adgroup_id}` |
| Hora do evento – Arredondada para cima | `{timestamp}` |
| ID de usuário exclusivo da AppsFlyer | `{sha1-appsflyer-device-id}` |
| Device ID com hash MD5 | `{md5IDFA\md4GAID}` |
| Se a atribuição foi de uma visualização | `{is-impression}` |
| Canal (Instagram, Meta Audience Network, Facebook, Messenger) | `{af_channel}` |
| Geografia | `{user_country}` |

<div id="example" />

> 📄 **Exemplo**
>
> http://mcmp_postbackURL.........&mcmp_ADset_name =`{adset_name}`

<div id="in-app-event-postbacks" />

## Aba Permissões

Após eventos in-app, a AppsFlyer pode retornar os seguintes parâmetros (além dos acima):

| Nome do parâmetro | Convenção de nome do parâmetro |
| --- | --- |
| Nome do evento* | `{event_name}` |
| Valor do evento | `{event_value}` |

<div id="example-1" />

> 📄 **Exemplo**
>
> `http://FMP_postbackURL.........&eventname={event_name}`

* O parceiro de gerenciamento de campanhas da Meta pode optar por receber o nome do evento in-app da forma como o anunciante o configurou no SDK da AppsFlyer ou por fazer com que o anunciante preencha um campo de texto livre para cada evento.

<div id="user-level-data-policy" />

## Política de dados em nível de usuário

* A AppsFlyer não pode transmitir o IDFA nem o ID de Publicidade do Android.

* A AppsFlyer transmite os carimbos de data/hora de instalações/eventos arredondados para a hora mais próxima.

Por exemplo: se uma instalação aconteceu às 4.32 pm e 42 segundos, podemos usar 5 pm como carimbo de data/hora

* A AppsFlyer pode usar um ID aleatório, criado por ela mesma, para anexar a eventos. Esse ID não deve ser derivado do IDFA/ID do Android e deve ser exclusivo para anúncios da Meta. O mesmo ID aleatório pode ser transmitido adiante para postbacks de eventos in-app.

<div id="note" />

> 📘 **Nota**
>
> Com base nos Termos da Meta, o envio de postbacks está disponível apenas para empresas que obtenham o seguinte selo: Ad Technology

<div id="example-2" />

> 📄 **Exemplo**
>
> ![](https://files.readme.io/6832879dafaadb91a795988abdc5e51203c9c1775054e35829cfe60cb2175a66-360001440909.png)
>
> Para ver a lista completa de parceiros de gerenciamento de campanhas da Meta, clique <Anchor target="_blank" href="https://www.facebook.com/business/partner-directory/search?programBadges=ADTECH_FB.ADTECH_IG&solution_type=campaign_management">aqui</Anchor>.

<div data-zendesk-anchors="install-postbacks=postbacks-de-instala%C3%A7%C3%A3o inapp-event-postbacks=aba-permiss%C3%B5es userlevel-data-policy=pol%C3%ADtica-de-dados-em-n%C3%ADvel-de-usu%C3%A1rio" />
