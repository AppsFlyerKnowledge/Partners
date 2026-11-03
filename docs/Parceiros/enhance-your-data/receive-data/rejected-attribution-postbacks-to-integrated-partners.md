---
title: Atribuições de instalação rejeitadas aos parceiros integrados
metadata:
  keywords:
    - fraud
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
  created_at: '2017-09-19T07:03:47Z'
  edited_at: '2026-08-18T00:39:23Z'
  id: 115004744123
  locale: pt
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/pt/articles/115004744123
---
> **Num relance:** Os parceiros integrados recebem postbacks de instalações e eventos in-app rejeitados devido a fraudes ou não conformidade com as regras de validação.

## Atribuições de instalação rejeitadas relacionadas com fraude e regras de validação

**Terminologia**:

* **Eventos fraudulentos:** instalações e eventos in-app bloqueados pelo Protect360
* **Eventos não conformes**: instalações e eventos in-app que não cumprem as regras de validação
* **Eventos rejeitados**: Eventos fraudulentos e eventos que não cumprem as regras de validação
* **Instalação com atribuição corrigida:** Uma instalação sequestrada identificada e bloqueada, cuja atribuição é subsequentemente corrigida e atribuída à fonte de mídia genuína.

**Postbacks**

* Os parceiros integrados recebem postbacks de eventos rejeitados em tempo real.
* Não há postbacks de eventos fraudulentos para eventos in-app de instalações com atribuição corrigida.
* Os postbacks de eventos rejeitados são enviados para o endpoint especificado pelo parceiro tanto para instalações quanto para eventos rejeitados, com os parâmetros adicionais sendo:  
  * Razão do bloqueio
  * Subrazão da rejeição
  * É-rejeitado
  * Valor da razão da rejeição (quando disponível). Por exemplo: `reject_reason=site_blacklist&reject_reason_value="1123456"&is_rejected=1`

A tabela seguinte lista a razão da rejeição, o valor da razão da rejeição e uma explicação da razão da rejeição:

| Razão da rejeição | Valor da razão da rejeição | Usuário pode configurar | Explicação |
| --- | --- | --- | --- |
| anomalias\_ctit | O tempo medido de clique para instalação em segundos | **X** | Anomalias de CTIT são cliques atribuídos que foram bloqueados com base no CTIT (tempo de clique para instalação) irrazoável. |
| store\_install\_validation | N/D | **X** | Instalações que falharam na validação da App Store |
| lista\_negra\_de\_sites | ID do site | **X** | Instalações provenientes de IDs de sites que a AppsFlyer bloqueou devido a alta densidade de atividade fraudulenta. Determinado pelos nossos algoritmos internos. |
| Bots | N/D | **X** | Tentativas de instalação bloqueadas feitas por bots |
| inundação\_de\_cliques | ID do site ou vazio | **X** | Instalações provenientes de clusters bloqueados pela AppsFlyer devido a um grande número de instalações com alto CTIT e baixa taxa de conversão. |
| anomalias\_comportamentais | N/D | **X** | Anomalias comportamentais sendo fraudes de instalação bloqueadas devido a comportamento pós-instalação inconsistente e anormal. |
| sequestro\_de\_instalação | N/D | **X** | Atribuição de instalação sequestrada sendo bloqueada com base em cliques e tempo de instalação irracional, baseada na API do Servidor Google Play. |
| validação\_bots | Nomes das regras ou vazio | ✓ | Regra definida pelo cliente. |
| validação\_sequestro | Nomes das regras | ✓ | Regra definida pelo cliente. |
| camada\_ai | N/D | **X** | Modelos de IA são utilizados para analisar grandes quantidades de dados, aumentando a capacidade de detecção para identificar atividades fraudulentas de dispositivos e de instalações. |

#### Razões para rejeição de eventos no aplicativo

| Razão da rejeição | Valor da razão da rejeição | Explicação |
| --- | --- | --- |
| Herdado da instalação | Herdado da instalação | Instalação inicial identificada como falsa com base no <Anchor target="_blank" href="/marketers/pt/docs/protect360-raw-data-reports#razões-para-bloqueio">nível de instalação</Anchor> ou na <Anchor target="_blank" href="/marketers/pt/docs/protect360-raw-data-reports#razões-para-bloqueio"> lista de negados</Anchor> razão |
| inapps\_bots | parâmetros\_de\_dispositivos\_falsos | algoritmo\_do\_AppsFlyer\_detecta\_fraude |
| validação\_inapps | nome\_do\_evento\_inválido | Baseado na regra de validação solicitada ou definida manualmente |
| validação\_inapps | valor\_do\_evento\_inválido | Baseado na regra de validação solicitada ou definida manualmente |
| validação\_inapps | Nome da(s) regra(s) | Baseado em regras definidas manualmente |

> 🚧 **Importante!**
>
> * Para conseguir distinguir entre postbacks para eventos legítimos e postbacks rejeitados, deve configurar os <Anchor target="_blank" href="/partners/pt/docs/postback-macros-for-ad-networks#macrosinstalações-eventos-in-app-e-eventos-rejeitados">macros de postback rejeitados</Anchor>.
> * Para ativar postbacks rejeitados para Privacidade Avançada, deve primeiramente adicionar os seguintes parâmetros ao <Anchor target="_blank" href="/partners/pt/docs/self-serve-integration-management-for-ad-networks#postback-padrão">Postback Padrão</Anchor>:
>   * `is-rejected`
>   * `blocked-reason`
>   * `blocked-sub-reason`
>   * `blocked-reason-value`
> * Quando os parâmetros acima forem adicionados tanto ao Postback Padrão como ao Postback de Privacidade Avançada, os postbacks de instalação rejeitada/eventos no aplicativo são ativados.

<div data-zendesk-anchors="rejected-attribution-postbacks-relating-to-fraud-and-validation-rules=atribui%C3%A7%C3%B5es-de-instala%C3%A7%C3%A3o-rejeitadas-relacionadas-com-fraude-e-regras-de-valida%C3%A7%C3%A3o h_01J5597AMDVWR2KTANSF7Y7T4P=atribui%C3%A7%C3%B5es-de-instala%C3%A7%C3%A3o-rejeitadas-relacionadas-com-fraude-e-regras-de-valida%C3%A7%C3%A3o reject-reasons-for-inapp-events=raz%C3%B5es-para-rejei%C3%A7%C3%A3o-de-eventos-no-aplicativo h_01J5597AMDHT5GJQN7QJZKV41F=raz%C3%B5es-para-rejei%C3%A7%C3%A3o-de-eventos-no-aplicativo h_01J5597AMD29TAZSKZS9WTFSM5=importante" />
