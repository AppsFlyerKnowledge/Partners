---
title: ROI360 para partners de UA
metadata:
  keywords:
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
  created_at: '2023-08-12T17:09:08Z'
  edited_at: '2026-08-12T12:28:42Z'
  id: 17735150011921
  locale: es
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/es/articles/17735150011921
---
> **De un vistazo:** AppsFlyer proporciona a los partners de UA datos completos y precisos sobre anuncios, compras in-app y suscripciones autorrenovables a través de reportes y postbacks. Los partners pueden procesar la información para optimizar las campañas de UA.

## Introducción

AppsFlyer recibe información de ingresos tanto de sus partners como de las tiendas de aplicaciones (Apple App Store y Google Play Store). Una vez recibidos, los datos se someten a una serie de pasos que incluyen validación, normalización, atribución y enriquecimiento con propiedades y dimensiones adicionales.  AppsFlyer puede enviar la información al partner de UA. Siguiendo este proceso, AppsFlyer transmite los datos enriquecidos y atribuidos al partner de UA. El partner de UA puede entonces utilizar esta información para optimizar sus campañas de adquisición de usuarios y mejorar el servicio que ofrece a los anunciantes.

<div id="what-revenue-types-are-reported-to-the-partners" />

<Accordion title="¿Qué tipos de ingresos se reportan a los partners?">

Las aplicaciones crean dos tipos de ingresos:

* **Ingresos por publicidad:** los ingresos por publicidad se generan cada vez que se muestra un anuncio dentro de la aplicación, incluidos banners, anuncios intersticiales y otros formatos. Se puede calcular independientemente del método de campaña mediante el cual se factura a un anunciante.
* **Compra in-app y suscripción de renovación automática:** los ingresos de la tienda se generan cada vez que se realiza una compra in-app o una transacción relacionada con la suscripción.

</Accordion>

<div id="how-does-appsflyer-provide-revenue-signals-to-ua-partners" />

<Accordion title="¿Cómo proporciona AppsFlyer las señales de ingresos a los partners de UA?">

AppsFlyer proporciona a los partners información sobre anuncios in-app, compras in-app e ingresos por suscripción a través de los siguientes medios:

* **Reporte de señales de UA de ingresos por publicidad**: el reporte enumera los eventos de ingresos por publicidad agregados al nivel de dispositivo. El reporte está disponible diariamente en Data Locker y contiene los datos del día anterior.
* **Postbacks de ingresos por publicidad**: cada vez que se produce una impresión de anuncio en un dispositivo cliente, se envía un postback de AppsFlyer al partner que contiene los detalles del evento de ingresos por publicidad.
* **Postbacks de ingresos de la tienda**: cada vez que ocurre un evento de compra o suscripción, se envía un postback desde AppsFlyer al partner que contiene los detalles del evento generador de ingresos.

</Accordion>

## Configurar el ROI360 para partners

¿Qué acciones deben tomar los partners para recibir el reporte de señales de UA y los postbacks de ingresos por publicidad e ingresos de la tienda?

<div id="how-to-subscribe-to-the-roi360-ua-signals-report" />

<Accordion title="Cómo suscribirse al reporte de señales de UA de ROI360">

Para permitir que el partner obtenga el reporte a través de Data Locker:

* El partner tiene que realizar los siguientes pasos en Data Locker:
  1. <Anchor target="_blank" href="/partners/es/docs/data-locker-for-partners#set-up-data-locker">Configurar Data Locker</Anchor> en la cuenta del partner, incluida la conexión con el proveedor de servicios en la nube y el formato y contenido de los reportes.
  2. <Anchor target="_blank" href="/partners/es/docs/ad-revenue-signals-for-ua-ad-networks#enable-the-ad-revenue-report">Habilitar el reporte de señales UA de ROI360</Anchor>.
* El anunciante tiene que <Anchor target="_blank" href="/marketers/es/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">otorgar permiso al partner para el reporte</Anchor>.

</Accordion>

<div id="how-to-receive-roi360-postbacks-from-appsflyer" />

<Accordion title="Cómo recibir postbacks de ROI360 de AppsFlyer">

Para recibir postbacks de AppsFlyer, los partners deben iniciar una conversación con el equipo de integración de partners de AppsFlyer. Posteriormente, el equipo configurará los valores de postback de ingresos in-app del ROI dentro de la plataforma AppsFlyer.

Para ponerte en contacto con el soporte técnico de AppsFlyer, abre el menú **Ayuda** en tu panel de control y selecciona **Contactar con nuestro equipo**.

[![alt](https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif)](https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif)

</Accordion>

## Reporte de señales de UA de ROI360 para redes de UA

El reporte proporciona registros de ingresos completos y precisos del día x+1 CSV/parquet al bucket S3 del partner de UA diariamente. Cada registro es una agregación de eventos de ingresos por publicidad a nivel de dispositivo.

El reporte se señales de UA no proporciona datos en tiempo real como lo hacen los postbacks de ingresos por publicidad. Sin embargo, es a la vez más preciso y completo. Esto se debe a que el valor de una impresión puede cambiar con el tiempo. Esto es especialmente cierto cuando los datos de ingresos a nivel de impresión son para una impresión publicitaria que se vendió a través de una oferta estándar de CPM en lugar de una oferta en tiempo real.

<div id="what-are-the-report-data-sources" />

<Accordion title="¿Cuáles son las fuentes de datos del reporte?">

Dependiendo del tipo de integración del anunciante, los datos del reporte pueden originarse de:

1. Integraciones de <Anchor target="_blank" href="/marketers/es/docs/integrate-the-roi360-ad-revenue-sdk-api">conectores AdRevenue SDK</Anchor>: los clientes pueden compartir los datos de ingresos a nivel de impresiones cargados por el partner a los dispositivos del cliente y luego reportarlos a AppsFlyer casi en tiempo real.
2. Integraciones a nivel de dispositivo basadas en la API S2S: los clientes pueden configurar sus credenciales de partner dentro de la interfaz de usuario de AppsFlyer bajo partners integrados y permitir que los ingresos por publicidad de ROI360 recopilen datos de ingresos por publicidad a nivel de dispositivo en su nombre.
3. Una combinación de los dos (Actualización a Precisión). **Nota:** La transferencia de datos del anunciante a AppsFlyer depende de los permisos del anunciante y de si el anunciante es un cliente avanzado de ROI360.

</Accordion>

<div id="what-data-processing-is-performed-on-the-report-data" />

<Accordion title="¿Qué procesamiento de datos se realiza en los datos del reporte?">

Los ingresos por publicidad de ROI360 de AppsFlyer realizan lo siguiente:

1. Normalización de datos
2. Atribución a la fuente de medios de instalación y enriquecimiento de datos
3. Generación de eventos de ingresos por publicidad
4. Los eventos se agregan a nivel de dispositivo

</Accordion>

<div id="how-is-the-report-data-delivered" />

<Accordion title="¿Cómo se entregan los datos del reporte?">

Los datos a nivel de dispositivo se escriben diariamente en el reporte en Data Locker.

</Accordion>

<div id="what-is-the-report-data-freshness" />

<Accordion title="¿Qué es la actualización de los datos del reporte?">

Los datos se escriben diariamente en la carpeta h=23 de tu bucket de Data Locker a las 21:00, <Anchor target="_blank" href="/marketers/es/docs/about-data-freshness-and-timezone-support#daily">hora UTC</Anchor>.

</Accordion>

<div id="what-are-the-report-fields" />

<Accordion title="¿Cuáles son los campos del reporte?">

| **Campo** | **Observaciones** |
| --- | --- |
| Versión | Marca de tiempo de Unix en segundos. Ejemplo: 1661315124 |
| id\_aplicación | ID de aplicación en la plataforma AppsFlyer |
| hora\_de\_instalación | • Marca de tiempo de instalación: AAAA-MM-DD HH: MM:SS Ejemplo: 2020-08-16 11:22:33 • Para dispositivos iOS 14+ y usuarios que no consienten, o si el anunciante tiene la Privacidad avanzada activada, el tiempo de instalación se redondea a la hora más cercana. |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Solo se rellenan si UA se atribuye al partner que recibe los datos. |
| idfa, idfv, advertising\_id | • El mismo ID de dispositivo, como IDFA, IDFV o advertiser\_id, podría mostrarse en varias filas si hay más de un evento de monetización de ingresos por publicidad. • Para dispositivos iOS 14+ y usuarios que no consienten, o si el anunciante tiene la Privacidad avanzada activada, esto no se muestra. |
| Identificador de origen | Plataforma del dispositivo: iOS, Android o Windows Mobile |
| País | Código de país con [ISO 3166 (alfa-2)](https://www.iso.org/iso-3166-country-codes.html) Ejemplo: |
| original\_url | • Para dispositivos iOS 14+ y usuarios que no consienten, o si el anunciante tiene la Privacidad avanzada activada, esto no se muestra. • Solo se rellena si UA se atribuye al partner que recibe los datos. |
| mediation\_network | La red de mediación asociada a la impresión o impresiones. <Anchor target="_blank" href="/marketers/es/docs/roi360-guide-ad-revenue-attribution#%5Bclosed-beta%5D-ua-signals-for-ad-networks">Ver lista de posibles redes</Anchor> |
| ad\_unit | Próximamente, en el tercer trimestre de 2023: la ad\_unit de monetización asociada a la impresión o impresiones |
| Suscripción IAP | Próximamente, en el tercer trimestre de 2023: la ubicación de monetización asociada a la impresión o impresiones |

</Accordion>

<div id="download-the-report-data-sample" />

<Accordion title="Descargar la muestra de datos del reporte">

[Haz clic para descargar el reporte.](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv)

</Accordion>

## Postbacks de ingresos por publicidad in-app (IAA)

Los postbacks de IAA son el segundo enfoque de ingestión que AppsFlyer utiliza para enviar información de ingresos a los partners. Su principal ventaja sobre el reporte de señales de ingresos por publicidad de UA es su actualización ya que los postbacks ofrecen un intercambio de datos de ingresos de IAA casi en tiempo real. Esto contrasta con la actualización X+1 (un día después de la fecha de ocurrencia del evento) ofrecida a través del reporte de señales de UA de ingresos por publicidad.

Sin embargo, la actualización en tiempo real es menos precisa en comparación con X+1:

* Los datos de postbacks IAA en tiempo real son ± 5% menos precisos en promedio que los datos del reporte de señales de UA X+1.
* Los datos de postbacks IAA en tiempo real son ± 7% menos completos en promedio que los datos del reporte de señales de UA X+1.

<div id="what-are-the-iaa-postback-data-sources" />

<Accordion title="¿Cuáles son las fuentes de datos postback de IAA?">

Los datos para el postback de IAA se originan a partir de datos a nivel de impresión que los partners cargan en los dispositivos del cliente. Estos datos son luego compartidos con AppsFlyer a través del conector ROI360 Ad Revenue SDK, que es instalado en el dispositivo por el anunciante. El conector permite al desarrollador de la aplicación reportar un evento de impresión que incluye ciertos parámetros como el ILRD, la divisa, la plataforma de mediación y la fuente de monetización.

La transferencia de datos desde los dispositivos de cliente del anunciante a AppsFlyer está sujeta a los permisos del anunciante y si un anunciante es un cliente avanzado de ROI360.

</Accordion>

<div id="what-processing-is-performed-on-the-iaa-postback-data" />

<Accordion title="¿Qué procesamiento se realiza en los datos de postback de IAA?">

ROI360 de AppsFlyer realiza los siguientes pasos para cada dato de nivel de impresión:

1. Normalización de datos
2. Atribución a la fuente de medios de instalación y enriquecimiento de datos
3. Generación de un evento **af\_ad\_revenue**

</Accordion>

<div id="how-is-the-postback-data-delivered" />

<Accordion title="¿Cómo se entregan los datos de postback?">

El evento se envía al partner a través de una configuración de postback existente entre el partner y AppsFlyer como parámetro adicional.

</Accordion>

## Postbacks de compras in-app (IAP)

Los postbacks de compras in-app de ROI360 ofrecen múltiples capas de precisión de reportes al validar primero cada transacción, deduplicarla y luego deducir la comisión de la tienda y el impuesto sobre las ventas.

<div id="what-are-the-iap-postback-data-sources" />

<Accordion title="¿Cuáles son las fuentes de datos de postbacks de IAP?">

Los datos para el postback IAP se originan a partir de:

1. Datos a nivel de transacciones leídos por el conector ROI360 Purchase SDK cada vez que se produce una compra in-app o un evento de suscripción autorrenovable en el dispositivo.
2. Cualquier **notificación entrante del servidor del App Store y Google Play (RTDN)** también se procesa mediante la lógica de negocio de ingresos de compras y suscripciones de AppsFlyer:

   * Las notificaciones relativas a transacciones previamente reportadas a través del conector SDK son validadas y procesadas.
   * Las notificaciones sobre transacciones desconocidas no se reportan a AppsFlyer.

   **Nota:** La transferencia de datos del anunciante a AppsFlyer depende de los permisos del anunciante y de si el anunciante es un cliente avanzado de ROI360.

</Accordion>

<div id="what-data-processing-is-performed-on-the-iap-postback-data" />

<Accordion title="¿Qué procesamiento de datos se realiza en los datos de postback de IAP?">

ROI360 de AppsFlyer realiza los siguientes pasos para cada dato de nivel de transacción recibido:

1. AppsFlyer **valida la compra o suscripción con la tienda correspondiente** para asegurarse de que no sea fraudulenta.
   * Tras la validación exitosa, AppsFlyer registra la compra o suscripción.
   * Si la validación de recibo falla, el evento se muestra en el reporte de raw data de eventos in-app bloqueados (disponible para suscriptores de Protect360).
2. AppsFlyer garantiza que las transacciones no se dupliquen, incluidas las relacionadas con el uso compartido en familia en iOS.
3. AppsFlyer calcula los datos de ingresos netos teniendo en cuenta la comisión de la tienda y los impuestos (**Ingresos reales**).
4. AppsFlyer genera un evento interno de compra o ciclo de vida para la transacción validada y procesada.

</Accordion>

<div id="how-is-the-postback-delivered" />

<Accordion title="¿Cómo se entrega el postback?">

El evento de IAP se envía al partner a través de una integración de postbacks existente entre el partner y AppsFlyer.

</Accordion>

<div id="what-are-the-iap-events" />

<Accordion title="¿Cuáles son los eventos de IAP?">

Los clientes de ROI360 pueden compartir los siguientes nombres de eventos con ingresos:

**Nombres de los eventos**

| **Nombre del evento** | **Descripción** |
| --- | --- |
| af\_compra | Se registra cuando un usuario realiza una compra. |
| af\_purchase\_refund | Se registra cuando se reembolsa una compra. |
| af\_ars\_trial\_converted | Se registra cuando comienza una renovación a precio completo, después de un período de prueba. |
| af\_ars\_subscription\_started | Se registra cuando se inicia una suscripción con descuento o a precio completo. |
| af\_ars\_subscription\_resumed | Se registra cuando se reanuda una suscripción de precio completo después de una suscripción abandonada o reembolsada. |
| af\_ars\_subscription\_refunded | Se registra cuando se emite un reembolso al suscriptor. |
| af\_ars\_subscription\_renewed | Se registra cuando tiene lugar una suscripción con renovación automática. |
| af\_ars\_subscription\_xgraded | Se registra cuando un suscriptor actualiza, baja de categoría o cambia de producto. |

</Accordion>

<div data-zendesk-anchors="introduction=introducci%C3%B3n 01H7T1DS6SNC7X8GX4DGXT4GC0=introducci%C3%B3n 01H7T1DS6TYHE3A4XWBDNHCFCZ=what-revenue-types-are-reported-to-the-partners 01H7T1DS6T82RWQ4BBWNPQ6BT2=how-does-appsflyer-provide-revenue-signals-to-ua-partners set-up-roi360-for-partners=configurar-el-roi360-para-partners 01H7T1DS6TDA8CX1ZF3GGE4EHB=configurar-el-roi360-para-partners 01H7T1DS6T0QFB6K6R78PMVVB2=how-to-subscribe-to-the-roi360-ua-signals-report 01H7T1DS6TBNJBBR6M98RTVMFF=how-to-receive-roi360-postbacks-from-appsflyer roi360-ua-signals-report-for-ua-networks=reporte-de-se%C3%B1ales-de-ua-de-roi360-para-redes-de-ua 01H7T1DS6T93844DMZY744ECQE=reporte-de-se%C3%B1ales-de-ua-de-roi360-para-redes-de-ua 01H7T1DS6T4AF6GTETE6HZMYF7=what-are-the-report-data-sources 01H7T1DS6TDNTYDY4JF70F40SV=what-data-processing-is-performed-on-the-report-data 01H7T1DS6T94V4674AMNVCD4T6=how-is-the-report-data-delivered 01H7T1DS6T4F0QV5VE8XZVV1RY=what-is-the-report-data-freshness 01H7T1DS6TYER08FGK9GDKHFEG=what-are-the-report-fields 01H7T1DS6TH98NT4KGKPR7DRDM=download-the-report-data-sample inapp-ad-revenue-iaa-postbacks=postbacks-de-ingresos-por-publicidad-in-app-iaa 01H7T1DS6T0CN30EC97VARN80D=postbacks-de-ingresos-por-publicidad-in-app-iaa 01H7T1DS6TCA8338NAD9Q8CJWW=what-are-the-iaa-postback-data-sources 01H7T1DS6TQ2G43HSQMH8Y6Q4H=what-processing-is-performed-on-the-iaa-postback-data 01H7T1DS6TQZA3W9KE3783G9G1=how-is-the-postback-data-delivered inapp-purchase-iap-postbacks=postbacks-de-compras-in-app-iap 01H7T1DS6TH8AV2ZTY3M8ZXPYA=postbacks-de-compras-in-app-iap 01H7T1DS6TGF4XEMD4CRBD8QS2=what-are-the-iap-postback-data-sources 01H7T1DS6T9W85F40QQ2497RNW=what-data-processing-is-performed-on-the-iap-postback-data 01H7T1DS6VAPRMCGZ9YCPTA9EQ=how-is-the-postback-delivered 01H7T1DS6VKE2G6XR02VF4TWH4=what-are-the-iap-events" />
