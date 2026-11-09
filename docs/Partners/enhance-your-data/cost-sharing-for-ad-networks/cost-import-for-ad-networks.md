---
title: Importación de costos para redes publicitarias
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Gray
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2019-10-20T06:03:13Z'
  edited_at: '2026-08-12T12:27:53Z'
  id: 360002868097
  locale: es
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/es/articles/360002868097
---
> **En resumen:** Descubre cómo las redes publicitarias pueden informar los costos de la campaña del anunciante directamente a AppsFlyer a través de archivos CSV.

<div id="cost-import-for-ad-networks" />

## Importación de costos para redes publicitarias

<Image align="center" alt="AdspendIngestion.jpg" src="https://files.readme.io/e870005c5f20531a2d06cc78b47a82a8a1f730f2c04728f5d0a5674c1c70129a-24507313816337.jpg" />

<div id="overview" />

#### Visión general

* Prepara un archivo CSV que contenga los detalles de la inversión publicitaria de la siguiente manera:
  * Fecha de gasto
  * ID de aplicación (se permiten varias aplicaciones por archivo si las aplicaciones pertenecen al mismo propietario)
  * Fuente de medios (se permite una por archivo)
  * Nombre de la campaña
  * Cantidad gastada
  * [Opcional] Geo
  * [Opcional] Moneda (USD predeterminada)
* Envía el archivo a AppsFlyer por correo electrónico/upload de archivos utilizando la cuenta de la ad network en AppsFlyer.   
  **Nota:**
  * Antes de enviar archivos por primera vez, el anunciante debe otorgarte a ti, la ad network, el permiso de importación de costos. Esto debe hacerse una vez para cada aplicación y es un proceso muy breve.
  * Una vez que se carga un archivo, no se puede revertir.
* Supervisa y verifica que no se hayan encontrado errores en el archivo.

<div id="submitting-ad-spend-files-for-ad-networks" />

### Envío de archivos de gasto publicitario para ad networks

* Utiliza el método de upload o correo electrónico para ingerir archivos de gasto publicitario.
* [Práctica recomendada] Utiliza inicialmente el método de upload, ya que es más fácil resolver problemas de formato CSV.
* Las ad networks no pueden importar datos de costos de agencia; solo los anunciantes pueden.

<div id="submission-by-file-upload" />

#### Envío mediante upload de archivos

**Para enviar archivos de importación de costos mediante upload:**

1. [Debes hacerlo una vez para cada aplicación con la que trabajes] <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-permissions-for-ad-networks">Pídele al anunciante que te dé permiso de importación de costos</Anchor>.
2. <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#prepare-csv-file-with-cost-data">Prepara el archivo CSV usando este formato y esquema</Anchor>.
3. Haz clic aquí para <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">iniciar sesión en tu cuenta de la ad network de AppsFlyer.</Anchor>
4. <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#upload-file">Carga e introduce el archivo</Anchor>.
5. En el dashboard de AppsFlyer puedes supervisar la ingestión:

   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">Estado</Anchor>
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#matched-rows">Filas con coincidencias</Anchor>
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">Acciones de importación de costos</Anchor>
6. Procedimientos adicionales:
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">Sobrescribir la ingestión anterior</Anchor>
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">Revertir (cancelar)</Anchor>

<div id="submission-by-email" />

#### Envío por correo electrónico

**Para enviar archivos de importaciones de costos por correo electrónico:**

1. [Debes hacerlo una vez para cada aplicación con la que trabajes] <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-permissions-for-ad-networks">Pídele al anunciante que te dé permiso de importación de costos</Anchor>.
2. <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#prepare-csv-file-with-cost-data">Prepara el archivo CSV usando este formato y esquema</Anchor>.
3. Si no tienes un token de importación de costos (lo necesitarás cuando envíes el archivo por correo electrónico):
   * Haz clic aquí para <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">iniciar sesión en tu cuenta de la ad network de AppsFlyer</Anchor>.
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#token-for-email-import">Obtén un token de gasto publicitario.</Anchor> Nota: Se utiliza el mismo token para todos los anunciantes.
4. Enviar archivo por <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#email-file">Correo electrónico</Anchor>
5. AppsFlyer envía por correo electrónico un reporte de estado; indica si la ingestión fue exitosa o si se encontraron problemas. **Nota**: Si no se recibió el correo de estado, mira el <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">dashboard de importación de costos</Anchor>.
6. En el dashboard de AppsFlyer puedes supervisar la ingestión:

   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">Estado</Anchor>
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#matched-rows">Filas con coincidencias</Anchor>
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">Acciones de importación de costos</Anchor>
7. Procedimientos adicionales:
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">Sobrescribir la ingestión anterior</Anchor>
   * <Anchor target="_blank" href="/marketers/es/docs/import-cost-data#cost-import-dashboard">Revertir (cancelar)</Anchor>

<div data-zendesk-anchors="ad-spend-ingestion-for-ad-networks=importaci%C3%B3n-de-costos-para-redes-publicitarias h_01HX94WSX07YEG40X66TMRFJGA=importaci%C3%B3n-de-costos-para-redes-publicitarias overview=visi%C3%B3n-general h_01HX94WSX0HR2KTGRT7MQ481Y6=visi%C3%B3n-general submitting-ad-spend-files-for-ad-networks=env%C3%ADo-de-archivos-de-gasto-publicitario-para-ad-networks h_01HX94WSX0G429FTHKYCG07BB9=env%C3%ADo-de-archivos-de-gasto-publicitario-para-ad-networks submission-by-file-upload=env%C3%ADo-mediante-upload-de-archivos h_01HX94WSX0ENTJEDMXWRHDCP0D=env%C3%ADo-mediante-upload-de-archivos submission-by-email=env%C3%ADo-por-correo-electr%C3%B3nico h_01HX94WSX0HVTMFQQ0NMW0VSKP=env%C3%ADo-por-correo-electr%C3%B3nico" />
