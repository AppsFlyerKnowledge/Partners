---
title: Reintentos de postback
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
  edited_at: '2026-08-12T12:28:34Z'
  id: 360001376085
  locale: es
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/es/articles/360001376085
---
> **De un vistazo:** Aprende cómo funcionan los reintentos de postback en AppsFlyer y cómo los Partners integrados pueden configurar sus mecanismos de postback.

<div id="introduction" />

## Introducción

Los postbacks a partners son una parte esencial de la integración entre AppsFlyer y nuestros partners. Como cualquier sistema puede experimentar problemas momentáneos de respuesta, AppsFlyer puede reintentar los postbacks fallidos.

<div id="important-information" />

## Información importante

<div id="when-does-appsflyer-retry-a-failed-postback" />

<Accordion title="¿Cuándo reintenta AppsFlyer un postback fallido?">

Se reintenta un postback cuando la respuesta indica un error del lado del servidor receptor: errores 5XX.

</Accordion>

<div id="how-often-does-appsflyer-retry-a-failed-postback" />

<Accordion title="¿Con qué frecuencia reintenta AppsFlyer un postback fallido?">

El primer postback fallido se reintenta hasta cuatro veces más, en intervalos de 15 minutos. En total, un solo postback se puede enviar hasta cinco veces.

</Accordion>

<div id="can-retried-postbacks-be-identified-in-postback-reports" />

<Accordion title="¿Se pueden identificar los postbacks reintentados en los reportes de postback?">

El reporte de postback de raw data: «Postback Retry». El primer postback enviado tiene un valor en blanco en esta columna. Cualquier postback reintentado contiene el valor TRUE en esta columna.

</Accordion>

<div id="how-can-a-partner-identify-the-total-eventual-failed-postbacks-in-the-postback-report" />

<Accordion title="¿Cómo puede un partner identificar en el reporte de Postback el total de postbacks que finalmente han fallado?">

Un postback que tiene cuatro valores TRUE en la columna «Postback Retry» y que además contiene códigos de error en la columna Postback HTTP Response Code es un postback cuyo envío al partner ha fallado por completo.

</Accordion>

<div id="is-there-anything-special-a-partner-should-consider-about-retried-postbacks" />

<Accordion title="¿Hay algo especial que un partner deba tener en cuenta sobre los postbacks reintentados?">

Si el postback ha llegado a tu sistema y se ha procesado correctamente, pero se ha producido un error o un retraso al enviar una respuesta, se considera un postback fallido y se envían reintentos al cabo de 15 minutos. Esto puede causar duplicación del lado del partner. El partner debe implementar un mecanismo de deduplicación de su lado.

</Accordion>

<div id="are-postback-retries-automatically-enabled-for-all-partners" />

<Accordion title="¿Los reintentos de postback están habilitados automáticamente para todos los partners?">

N.º Si un partner quiere reintentar postbacks fallidos, debe ponerse en contacto con su PDM para habilitar esta función.

</Accordion>

<div data-zendesk-anchors="introduction=introducci%C3%B3n important-information=informaci%C3%B3n-importante" />
