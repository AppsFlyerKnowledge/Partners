---
title: 'Protect360: preguntas frecuentes para partners'
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2023-06-12T12:43:34Z'
  edited_at: '2026-08-12T12:29:59Z'
  id: 16091549732497
  locale: es
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/es/articles/16091549732497
---
> **En resumen:** Encuentra respuestas a las preguntas más frecuentes de los partners sobre Protect360.

<div id="impression-level-anomalies" />

## Anomalías a nivel de clics/impresiones

<div id="why-are-impressionsclicks-being-capped" />

<Accordion title="¿Por qué se están limitando las impresiones?">

El sistema Protect360 de AppsFlyer tiene en cuenta varios parámetros a la hora de tomar decisiones sobre la limitación de los engagements en anuncios, incluidos, entre otros, el volumen de impresiones/clics, el CVR, la tasa de anomalías detectadas, las fluctuaciones normales de la actividad, así como los puntos de referencia geográficos y de la industria. El algoritmo es dinámico y se actualiza cada hora, para tener en cuenta las tendencias cambiantes.

Una vez que se activa el mecanismo de limitación, Protect360 bloquea las impresiones o los clics de la red de publicidad para la aplicación relacionada dentro del ciclo actual de 24 horas. Esto significa que AppsFlyer no registra las impresiones/clics que ocurran después del umbral, ni son elegibles para la atribución.

Una red puede evitar superar el umbral deteniendo las campañas y los publishers con volúmenes inusualmente altos de engagements de anuncios que no muestran ningún impacto en los resultados de rendimiento.

Te recomendamos que eches un vistazo a estos artículos:  
<Anchor target="_blank" href="/partners/es/docs/protect360-for-integrated-partners#umbral-de-impresiones">Limitación de clics e impresiones</Anchor>  
<Anchor target="_blank" href="/partners/es/docs/protect360-for-integrated-partners#faq">Preguntas frecuentes sobre la limitación</Anchor>

</Accordion>

<div id="the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate" />

<Accordion title="¿Por qué se bloquean las instalaciones debido a la inundación de clics, pero la tasa de conversión es alta?">

Nuestros algoritmos de inundación de clics se ejecutan en varios intervalos a lo largo del día y, cada vez que se supera el umbral, en función de los parámetros internos y la lógica, los engagements de anuncios del publisher no serán aptos para la atribución.

**Ten en cuenta:** Algunos de nuestros algoritmos de inundación de clics funcionan en todas las aplicaciones, lo que implica que las anomalías que se originan en fuentes fraudulentas idénticas también se reconocerán para otras aplicaciones anunciadas.

Te recomendamos leer: <Anchor target="_blank" href="https://www.appsflyer.com/glossary/click-flooding/">¿Qué es la inundación de clics?</Anchor>

</Accordion>

<div id="installin-app-event-level-anomalies" />

## Anomalías a nivel de instalación/evento in-app

<div id="why-was-my-test-install-rejected-from-attribution" />

<Accordion title="¿Por qué se rechazó mi instalación de prueba de la atribución?">

La detección antifraude de AppsFlyer aplica diferentes metodologías en varias capas de protección, como instalaciones individuales y clústeres de instalación. Los clústeres se revisan en varias agregaciones: por publisher, fuente de medios, aplicación, etc. La actividad fraudulenta se examina utilizando varios algoritmos estadísticos y algoritmos de aprendizaje automático que consideran cada clúster como un todo. Por lo tanto, si se determina que un clúster es fraudulento con una alta significación estadística, todas las instalaciones de ese clúster se consideran fraudulentas. Es una táctica bien conocida de los estafadores mezclar algunas instalaciones legítimas con grandes volúmenes de actividad fraudulenta con la esperanza de que el fraude se "diluya" lo suficiente como para evitar desencadenar mecanismos de bloqueo.

De forma predeterminada, todas las instalaciones entrantes se consideran tráfico EN VIVO, por lo tanto, para asegurarte de que tu instalación de prueba no se clasifique en los algoritmos de Protect360, debes seguir los pasos mencionados en <Anchor target="_blank" href="/marketers/es/docs/registering-test-devices">este artículo</Anchor> para registrar tu dispositivo como dispositivo de prueba antes de realizar una prueba.

</Accordion>

<div id="What-detection-methods-are-used-to-detect-install-rejections" />

<Accordion title="¿Qué métodos de detección se utilizan para detectar rechazos de instalaciones?">

Revisa el "submotivo del fraude" asociado con el rechazo para mayor claridad. Estos datos también están disponibles en los reportes de Protect360 y en el panel de control de Protect360, sujeto al acceso otorgado por el anunciante respectivo.

Te recomendamos leer sobre los <Anchor target="_blank" href="/marketers/es/docs/protect360-raw-data-reports#motivos-de-bloqueo">Motivos de bloqueo de Protect360</Anchor>.

</Accordion>

<div id="protect360-data-visibility-and-comprehension" />

## Visibilidad y comprensión de datos de Protect360

<div id="how-do-i-gain-visibility-into-the-protect360-results" />

<Accordion title="¿Cómo puedo obtener visibilidad de los resultados de Protect360?">

Puedes ver los resultados de nuestros esfuerzos de detección utilizando el panel de control de Protect360 y los reportes de raw data, sujeto al acceso otorgado por el anunciante respectivo.

Te recomendamos que eches un vistazo a estos artículos:  
<Anchor target="_blank" href="/marketers/es/docs/protect360-dashboard">Panel de control de Protect360</Anchor>  
<Anchor target="_blank" href="/marketers/es/docs/protect360-raw-data-reports#obteniendo-informes-de-datos-sin-procesar">Raw data de Protect360</Anchor>

</Accordion>

<div id="how-can-i-get-notified-in-realtime-about-blocked-traffic" />

<Accordion title="¿Cómo puedo recibir notificaciones en tiempo real sobre el tráfico bloqueado?">

AppsFlyer proporciona postbacks de atribución rechazados a las redes de publicidad por cada instalación que Protect360 rechaza de la atribución.

Puedes habilitar los "postbacks rechazados" anexando los parámetros de "postback rechazado" a la plantilla de postback mediante la <Anchor target="_blank" href="/partners/es/docs/self-serve-integration-management-for-ad-networks">Gestión de la integración</Anchor>.

</Accordion>

<div id="why-do-i-see-spikes-in-postattribution-detections" />

<Accordion title="¿Por qué veo picos en las detecciones posteriores a la atribución?">

La detección en tiempo real antes de la atribución y la detección posterior a la atribución pertenecen al mecanismo de detección de anomalías Protect360 de AppsFlyer que se aplica en diferentes dimensiones de tiempo.

En comparación con la detección en tiempo real, la detección posterior a la atribución se basa más en los indicadores de datos recopilados después de la instalación, durante los cuales, si se observan anomalías, Protect360 registrará las actividades anómalas y las mostrará en la categoría posterior a la atribución.

Teniendo en cuenta lo anterior, es más probable que ciertos métodos de detección (timestamp\_anomalies, behavioral\_anomalies, etc.) se detecten en la etapa posterior a la atribución que en tiempo real, ya que los datos no son concluyentes a nivel de una instalación individual, pero adquieren importancia cuando se examinan para su distribución en el análisis estadístico.

Saber más sobre la <Anchor target="_blank" href="/marketers/es/docs/protect360-anti-fraud-guide#postattribution-detection">detección posterior a la atribución</Anchor>.

</Accordion>

<div data-zendesk-anchors="click-impression-level-anomalies=anomal%C3%ADas-a-nivel-de-clicsimpresiones 01H8GKS08Y22PX2SBTW5ME02C4=anomal%C3%ADas-a-nivel-de-clicsimpresiones 01H8GKS08YXVK4CPNW9TX9XBYN=why-are-impressionsclicks-being-capped 01H8GKS08ZGNTMNZ5JH846T9Q9=the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate install-inapp-event-level-anomalies=anomal%C3%ADas-a-nivel-de-instalaci%C3%B3nevento-in-app 01H8GKS08ZRA7YT9FWJNBBSV4Q=anomal%C3%ADas-a-nivel-de-instalaci%C3%B3nevento-in-app 01H8GKS08Z2M0RTMR4GM1BJE7G=why-was-my-test-install-rejected-from-attribution What-detection-methods-are-used-to-detect-install-rejections%3F=What-detection-methods-are-used-to-detect-install-rejections 01H8H30KARRPAPT9XRREDYKHVT=What-detection-methods-are-used-to-detect-install-rejections protect360-data-visibility-and-understanding=visibilidad-y-comprensi%C3%B3n-de-datos-de-protect360 01H8GKS08ZX2W1G0K165H96N4Z=visibilidad-y-comprensi%C3%B3n-de-datos-de-protect360 01H8GKS08ZGEEK0HQVCRD546MW=how-do-i-gain-visibility-into-the-protect360-results 01H8GKS08ZC6SB4PT53JG5QKHG=how-can-i-get-notified-in-realtime-about-blocked-traffic 01H8GKS08Z673WG6C6JGW31F42=why-do-i-see-spikes-in-postattribution-detections" />
