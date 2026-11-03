---
title: Tentativas de novo envio de postback
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
  created_at: '2018-08-06T04:59:54Z'
  edited_at: '2026-08-18T00:39:18Z'
  id: 360001376085
  locale: pt
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/pt/articles/360001376085
---
> **Em resumo:** Saiba como funcionam as tentativas de novo envio de postback na AppsFlyer e como os parceiros integrados podem configurar seus mecanismos de postback.

## Introdução

Os postbacks para parceiros são uma parte crítica da integração entre a AppsFlyer e nossos parceiros. Como qualquer sistema pode apresentar problemas momentâneos de resposta, a AppsFlyer pode tentar novamente os postbacks com falha.

## Informações importantes

<div id="when-does-appsflyer-retry-a-failed-postback" />

<Accordion title="Quando a AppsFlyer tenta novamente um postback com falha?">

Um postback é tentado novamente quando a resposta indica um erro no servidor de recebimento, erros 5XX no lado do servidor.

</Accordion>

<div id="how-often-does-appsflyer-retry-a-failed-postback" />

<Accordion title="Com que frequência a AppsFlyer tenta novamente um postback com falha?">

O primeiro postback com falha é tentado novamente até quatro vezes adicionais, em intervalos de 15 minutos. No total, um único postback pode ser enviado até cinco vezes.

</Accordion>

<div id="can-retried-postbacks-be-identified-in-postback-reports" />

<Accordion title="É possível identificar os postbacks tentados novamente nos relatórios de postback?">

No relatório de postback de dados brutos: "Postback Retry". O primeiro postback enviado tem um valor em branco nesta coluna. Qualquer postback tentado novamente contém o valor TRUE nesta coluna.

</Accordion>

<div id="how-can-a-partner-identify-the-total-eventual-failed-postbacks-in-the-postback-report" />

<Accordion title="Como um parceiro pode identificar o total de postbacks que acabaram falhando no relatório de postback?">

Um postback que tem quatro valores TRUE listados na coluna "Postback Retry" e também contém códigos de erro na coluna "Postback HTTP Response Code" é um postback cujo envio ao parceiro falhou completamente.

</Accordion>

<div id="is-there-anything-special-a-partner-should-consider-about-retried-postbacks" />

<Accordion title="Há algo especial que um parceiro deva considerar sobre postbacks tentados novamente?">

Se o postback tiver chegado ao seu sistema e tiver sido processado com sucesso, mas tiver ocorrido um erro ou atraso no envio de uma resposta, isso será considerado um postback com falha, e novas tentativas serão enviadas após 15 minutos. Isso pode causar duplicação no lado do parceiro. O parceiro deve implementar um mecanismo de desduplicação no seu lado.

</Accordion>

<div id="are-postback-retries-automatically-enabled-for-all-partners" />

<Accordion title="As tentativas de novo envio de postback são ativadas automaticamente para todos os parceiros?">

Sem. Se um parceiro quiser tentar novamente postbacks com falha, deverá entrar em contato com seu PDM para ativar esse recurso.

</Accordion>

<div data-zendesk-anchors="introduction=introdu%C3%A7%C3%A3o important-information=informa%C3%A7%C3%B5es-importantes" />
