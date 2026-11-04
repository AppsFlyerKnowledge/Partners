---
title: Señales de ingresos publicitarios para ad networks de UA
metadata:
  keywords:
    - Ad Network
    - Partner
    - ad revenue
    - Data Locker
    - Ad Networks
    - Partners
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-michael-talapov
    - ROI360
    - Ad Networks
  created_at: '2021-06-21T13:39:13Z'
  edited_at: '2026-08-12T12:27:19Z'
  id: 4402898251409
  locale: es
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/es/articles/4402898251409
---
> **En resumen:** Las ad networks responsables por la adquisición de usuarios pueden recibir datos relativos a los ingresos por publicidad y utilizarlos para optimizar las campañas de UA de sus clientes.

Las ad networks pueden recibir reportes a través de Data Locker con valiosa información sobre los ingresos publicitarios de los usuarios. Estos usuarios pueden haber sido adquiridos a partir de campañas servidas a través de ellas, o pueden proceder de una fuente de medios diferente.

A continuación, las ad networks pueden incorporar estos datos a los algoritmos de targeting y optimización de campañas, y utilizarlos para mejorar las campañas de ROAS basándose en una visión completa de los ingresos generados por UA.

<div id="set-the-ad-revenue-report-in-data-locker" />

## Configuración del reporte de ingresos por publicidad en Data Locker

Para acceder al reporte de ingresos publicitarios en Data Locker, es necesario completar las siguientes actividades:

* Las ad networks deben realizar el <Anchor target="_blank" href="/partners/es/docs/data-locker-for-partners#set-up-data-locker">onboarding de Data Locker para partners</Anchor>.
* Las ad networks deben [configurar los ajustes de salida del reporte](#configure-the-report-output-settings) y [habilitar el reporte de ingresos por publicidad](#enable-the-ad-revenue-report).
* Los anunciantes deben permitir que las ad networks puedan ver el reporte. <Anchor target="_blank" href="/marketers/es/docs/share-ad-revenue-data-with-partners#ua-signals-for-ad-networks">Ver instrucciones para anunciantes</Anchor>

<div id="configure-the-report-output-settings" />

<Accordion title="Configuración de la salida de reportes">

Para configurar la salida de reportes, sigue estos pasos:

1. En AppsFlyer, ve a **Reporte** > **Data Locker**.
2. En el área de **Configuración de salida de reportes**, activa **Enviar reportes**.
3. Establece las propiedades de salida del archivo de reporte.
   * El formato del reporte (Parqet/CSV).
   * El método de compresión del reporte (Snappy/GZIPO/Sin comprimir).
   * Número máximo de filas de un archivo.
4. Revisa la ruta esperada de las salidas del archivo de reporte. La ruta se establece en función de la configuración de tu conexión. Para saber cómo configurar la conexión, consulta <Anchor target="_blank" href="/partners/es/docs/data-locker-for-partners#set-up-data-locker">Configurar Data Locker</Anchor>.

</Accordion>

<div id="enable-the-ad-revenue-report" />

<Accordion title="Activación del reporte de ingresos por publicidad">

1. En la sección de **Contenido de Data Locker**, selecciona el tipo de reporte **Ingresos por publicidad [a diario].**
2. Haz clic en **Guardar conexión**.
3. Asegúrate de que el anunciante ha permitido a la ad network ver el reporte.
4. Para obtener instrucciones, consulta <Anchor target="_blank" href="/marketers/es/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">Permitir que las ad networks obtengan datos de ingresos por publicidad.</Anchor>

</Accordion>

<div id="report-specification" />

## Especificación del reporte

<div id="report-considerations" />

<Accordion title="Estructura y formato del reporte">

* Formato: Los datos llegan en formato CSV al bucket S3 del partner de UA.
* Nivel: Contiene dimensiones y métricas a nivel de dispositivo.
* Enriquecimiento de datos: Incluye datos de ingresos publicitarios de partners de mediación y agrega datos de atribución relevantes para la ad network de UA (que se limpian de todas las dimensiones irrelevantes para la ad network de UA).
* Actualización de datos: <Anchor target="_blank" href="/marketers/es/docs/about-data-freshness-and-timezone-support#ad-revenue">A diario, lo que significa que los datos del Día 0 llegan el Día 1</Anchor>. Los datos se escriben diariamente a las <Anchor target="_blank" href="/marketers/es/docs/about-data-freshness-and-timezone-support#daily">21:00 UTC</Anchor> en la h=23 de tu bucket de Data Locker.
* Aplicaciones incluidas: Un único reporte contiene los datos de todas las aplicaciones para las que los anunciantes han concedido permiso.
* Los reportes incluyen datos sobre todos los tipos de conversión: Instalaciones, re-engagements, re-atribuciones y reinstalaciones.
* Moneda: En USD. Los ingresos por eventos se calculan en USD el día en que se produjo el evento.
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSoV1U_pMUoTFhIpyYQmUI1zQWArY19c8gMmsfpRiAaGXVZEG4WqgSC26u5-fv32j8ZQN4uxtNgVkYs/pub?output=csv">Ver ejemplo de reporte</Anchor>

</Accordion>

<div id="report-structure" />

<Accordion title="Campos del reporte">

| **Campo** | **Observaciones** |
| --- | --- |
| Versión | Marca de tiempo de Unix en segundos. Ejemplo: 1661315124 |
| id\_aplicación | ID de aplicación en la plataforma AppsFlyer |
| hora\_de\_instalación | <ul><li>Marca de tiempo de la instalación: AAAA-MM-DD HH: MM:SS<br />Ejemplo: 2020-08-16 11:22:33</li><li>Para dispositivos iOS 14+ y usuarios que no consiente, o si el anunciante tiene activada la Privacidad avanzada, la hora de instalación se redondea a la hora más cercana.</li></ul> |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Solo se rellenan si la UA se atribuye al partner que recibe los datos. |
| idfa, idfv, advertising\_id | <ul><li>El mismo ID de dispositivo, como el IDFA, IDFV o advertiser\_id, podría mostrarse en varias filas si hay más de un evento de monetización de ingresos por publicidad.</li><li>Para dispositivos iOS 14+ y usuarios que no dan su consentimiento, o si el anunciante tiene la Privacidad Avanzada activada, esto no se muestra.</li></ul> |
| Identificador de origen | Plataforma del dispositivo: iOS, Android o Windows Mobile |
| País | Código del país con <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor> Por ejemplo: |
| original\_url | <ul><li>Para dispositivos iOS 14+ y usuarios que no dan su consentimiento, o si el anunciante tiene la Privacidad Avanzada activada, esto no se muestra.</li><li>Solo se rellenan si la UA se atribuye al partner que recibe los datos.</li></ul> |
| ad\_unit |  |
| Suscripción IAP |  |
| mediation\_network |  |
| tipo\_de\_engagement |  |

Métricas:

| **Campo** | **Observaciones** |
| --- | --- |
| Validación de compra de AppsFlyer | Número de veces que el usuario vio el anuncio |
| ingresos\_usd | Ingresos diarios (en USD) generados para el ID del dispositivo. **Nota**: Cuando el monto de los ingresos es pequeño, se representa en notación científica. Por ejemplo: 8.00E-05 |

</Accordion>

<div data-zendesk-anchors="set-the-ad-revenue-report-in-data-locker=configuraci%C3%B3n-del-reporte-de-ingresos-por-publicidad-en-data-locker h_01H8Y7ABGVR7BNHEYVFKPFM4JN=configuraci%C3%B3n-del-reporte-de-ingresos-por-publicidad-en-data-locker h_01H8Y7ABGV2T6GBE9BHJQM6FDF=configure-the-report-output-settings h_01H8Y7ABGVW6Y5RY7CVNM3EJZR=enable-the-ad-revenue-report report-specification=especificaci%C3%B3n-del-reporte h_01H8Y7ABGVXJ9ZQCJ8BR0DST6W=especificaci%C3%B3n-del-reporte h_01H8Y7ABGV0G4GJBRKKGNBSEC5=report-considerations h_01H8Y7ABGV81X0VFWTRMXGHYSA=report-structure" />
