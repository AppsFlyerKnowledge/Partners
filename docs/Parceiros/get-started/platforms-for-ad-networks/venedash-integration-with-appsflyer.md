---
title: integração da venedash com a AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
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
    - Ad Networks
  created_at: '2020-04-24T21:20:47Z'
  edited_at: '2026-09-10T00:39:16Z'
  id: 360007705617
  locale: pt
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/pt/articles/360007705617
---
> **Visão geral:** envie dados de atribuição da AppsFlyer para a venedash. A AppsFlyer pode enviar para a venedash dados de instalação e de eventos in-app.

## configuração da integração da Venedash

* Se você tiver uma integração com a AppsFlyer, entre em contato conosco usando o <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget do partner assistant</Anchor>.
* Se você não tiver uma integração com a AppsFlyer, preencha a inscrição de registro de parceiros de anúncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aqui</Anchor>.

**Para habilitar a integração com a AppsFlyer:**

1. No **AppsFlyer**, acesse **Colaborar** > **Integrações de Parceiros > Integrações ativas** e selecione Venedash na lista de parceiros.
2. Na guia **Integração**, ative **Ativar parceiro**.
3. Acesse a guia **Link de atribuição** e gere um link de atribuição com os seguintes parâmetros obrigatórios:

   

| Parâmetro da AppsFlyer | parâmetro do Venedash | A descrição |
| --- | --- | --- |
| &clickid= | `{#ydrid#}` | ID da solicitação de cada sessão do usuário |
| &af\_siteid= | `{#ydr_pid#}` | ID do afiliado que promove a oferta |
| &advertising\_id | `{#android_adv#}` | ID do dispositivo Android |
| &idfa= | `{#iosidfa#}` | Device ID do dispositivo iOS |

   Observe que o parâmetro pid é preenchido pela equipe da AppsFlyer.  
   Exemplo:

   ```http
   https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#ydrid#&af_siteid=#ydr_pid#&advertising_id=advertising_id&idfa=#iosidfa#">https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#ydrid#&af_siteid=#ydr_pid#&advertising_id=advertising_id&idfa=#iosidfa#
   ```

   Saiba mais sobre os <Anchor target="_blank" href="/marketers/pt/docs/about-link-structure-and-parameters">parâmetros do link de atribuição</Anchor>.
4. No Venedash, crie uma oferta e cole o link de atribuição da AppsFlyer no campo URL de destino.

   ![venedash-destination_url-en_us.png](https://files.readme.io/2a284eab8d25f57f1bfa2981e2d86bf16bce16b64b61858fdb819d5ac14eac20-360016242798.png)

<div data-zendesk-anchors="venedash-integration-setup=configura%C3%A7%C3%A3o-da-integra%C3%A7%C3%A3o-da-venedash h_01HKW87R2DGCXHZSVSV9D9203Z=configura%C3%A7%C3%A3o-da-integra%C3%A7%C3%A3o-da-venedash" />
