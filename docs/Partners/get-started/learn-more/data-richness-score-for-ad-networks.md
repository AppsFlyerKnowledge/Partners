---
title: Calificación de riqueza de datos para ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - attribution link
    - data richness score
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2020-06-03T09:27:03Z'
  edited_at: '2026-08-12T12:29:54Z'
  id: 360009443338
  locale: es
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/es/articles/360009443338
---
> **En resumen:** Mejora la calidad de los datos que proporcionas a los anunciantes con la calificación de riqueza de datos de AppsFlyer.

La calidad de los datos que los anunciantes reciben de las ad networks en las que ejecutan sus campañas puede desempeñar un papel importante en las decisiones de marketing.

Los datos proporcionados por distintas ad networks varían en cuanto a cobertura, precisión y granularidad. Los datos parciales e inexactos reducen la capacidad de los anunciantes para analizar y optimizar el rendimiento de sus campañas en AppsFlyer.

La calificación de riqueza de datos, una métrica proporcionada por AppsFlyer, indica el grado de exhaustividad de los datos de las ad networks. Esta calificación está disponible para todos los anunciantes, por lo que pueden comprender las capacidades y la calidad de los datos de cada red y tomar decisiones empresariales fundamentadas.

Para maximizar la calificación, las ad networks deben subsanar las carencias de datos que tengan.

## Calificación de riqueza de datos

**Para ver tu calificación de riqueza de datos:**

1. Inicia sesión en tu cuenta.
2. Abre el dashboard de cualquier aplicación que gestiones.
3. Haz clic en **Integraciones activas** en la barra lateral izquierda.  
   El indicador de la calificación se muestra debajo del nombre de tu red.

   ![integrated-partners-data-richness.png](https://files.readme.io/ee68f4ba63ef4e27292ed6b857e2cd05e4d83f8ba65a80655d1bf8b63df94f5f-360009360018.png)

Los anunciantes pueden ver la calificación de riqueza de datos (baja, media o alta) de cada ad network que tenga una integración con AppsFlyer.

### Datos incluidos

Para ver la calificación en cada categoría de datos incluida en la calificación, pasa el cursor sobre el indicador. Se abre una ventana emergente que muestra la calificación final y los grupos de datos: datos de campaña, datos del anuncio y datos del publisher.

Para recibir una calificación alta, una ad network debe proporcionar los siguientes parámetros en todos los clics y visualizaciones:

* Datos de la campaña:
  * Cadena
  * Solo disponible en <Anchor target="_blank" href="/marketers/es/docs/about-data-locker-advanced-reports">reportes avanzados</Anchor>.
* Datos del anuncio:  
  * ID del adset
  * Nota
  * Retargeting: Primer inicio después del re-engagement o la reatribución.
  * Nota
  * Tipo de anuncio
* Datos del publisher
  * Parámetros de seguimiento adicionales utilizados para la atribución.
  * ID de sub sitio
  * Ejemplo

### Umbral de datos

* La calificación se calcula semanalmente y puede subir o bajar en función de la integridad de los parámetros indicados arriba.
* Se requiere una cantidad mínima de conversiones (instalaciones, reatribuciones y reengagements) para que se calcule la calificación. Si la red tiene menos conversiones que el mínimo durante una semana determinada, la semana siguiente el indicador de la calificación se desactivará y no se mostrará ninguna categoría de datos.

## Siguientes pasos

Para añadir más parámetros y mejorar tu integración y visibilidad en la plataforma AppsFlyer,

1. Comprueba qué parámetros faltan en tu integración.
   * <Anchor target="_blank" href="/partners/es/docs/getting-started-onboarding-guide-for-ad-networks#parte-1-integración-y-pruebas">Lee sobre las plantillas de enlace de atribución</Anchor>
   * <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#parámetros-del-enlace-de-atribución">Consulta la lista completa de parámetros disponibles para usar</Anchor>
2. Ponte en contacto con tu PDM para actualizar la plantilla de enlace o recibir más información.

<div data-zendesk-anchors="data-richness-score=calificaci%C3%B3n-de-riqueza-de-datos included-data=datos-incluidos data-threshold=umbral-de-datos next-steps=siguientes-pasos" />
