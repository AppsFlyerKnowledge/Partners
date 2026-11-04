---
title: Atribución de precarga para partners
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
  edited_at: '2026-08-12T12:29:22Z'
  id: 15321350340241
  locale: es
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/es/articles/15321350340241
---
> **De un vistazo:** Atribuye las instalaciones de aplicaciones móviles a campañas que precargan la app en el fabricante de equipos originales (OEM) o cuando el usuario enciende el dispositivo por primera vez.

<div id="overview" />

## Visión general

Al proporcionar soporte a las soluciones de atribución de precarga de AppsFlyer, los Partners de precarga pueden tener las instalaciones de la app atribuidas a campañas de precarga. Las campañas de precarga son para cuando una app se instala en un dispositivo por un Partner de precarga, ya sea en la fábrica o al activar el dispositivo (cuando el dispositivo se enciende por primera vez).

Los partners de precarga son:

* Original Equipment Manufacturers (OEMs)
* Plataformas de descubrimiento de aplicaciones
* Operadores móviles

Hay 3 formas de atribuir campañas precargadas:

* [Recomendado] Referer de AppsFlyer
* Instalación automática de Google Play (PAI)
* [Heredado] Precarga en fábrica mediante la propiedad del sistema

Se te envían postbacks después de cada conversión.

<Anchor target="_blank" href="/marketers/es/docs/appsflyer-attribution-model#preload-campaigns">Saber más sobre los métodos de atribución de campañas de precarga</Anchor>

<div id="set-up-preload-attribution" />

## Configurar la atribución de precarga

Para configurar la atribución de precarga:

1. Asegúrate de ser un <Anchor target="_blank" href="/partners/es/docs/getting-started-onboarding-guide-for-ad-networks">partner integrado de AppsFlyer</Anchor>.
2. Elige las soluciones de atribución de precarga que vas a integrar (según las necesidades del anunciante). **Nota**: Cada integración necesita un PID independiente con una cuenta de Partner de AppsFlyer. Ponte en contacto con tu equipo de soluciones para partners a través del widget de soporte.
   * [Recomendado] <Anchor target="_blank" href="/marketers/es/docs/set-up-appsflyer-preload-referrer-attribution">Referer de AppsFlyer</Anchor>: Ponte en contacto con tu PDM para obtener instrucciones de integración.
   * <Anchor target="_blank" href="/marketers/es/docs/measure-preload-campaigns-with-google-play-install">Instalación automática de Google Play (PAI)</Anchor>: Configura la información de la fuente de medios en la API de Google Play Referrer para las campañas de PAI con los siguientes parámetros UTM: `utm_source=play-auto-installs&utm_medium=preload&utm_campaign=brandnamepai_int`. Por ejemplo: `utm_source=play-auto-installs&utm_medium=preload&utm_campaign=xiaomipai_int`.
3. Ponte en contacto con el equipo de soluciones para partners de AppsFlyer a través del widget de soporte para completar la integración y, si quieres, configurar postbacks.  
   **Nota**: Consulta qué macros de postback son compatibles con el método de precarga de <Anchor target="_blank" href="/marketers/es/docs/measure-preload-campaigns-with-google-play-install#postbacks-para-partners-de-precarga">Google PAI</Anchor> y <Anchor target="_blank" href="/partners/es/docs/postback-macros-for-ad-networks">AppsFlyer referrer/archivo de manifiesto de Android</Anchor>.

<div data-zendesk-anchors="organic-search-attribution=visi%C3%B3n-general h_01HQFFB20SKDVW1X3ECMZCZQW0=visi%C3%B3n-general set-up-preload-attribution=configurar-la-atribuci%C3%B3n-de-precarga h_01HQFFB20S6KJH3PBF5N2190TJ=configurar-la-atribuci%C3%B3n-de-precarga" />
