---
title: Acceso a herramientas de análisis agregados para Partners de API
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Premium API
    - Marketers
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketers
    - Marketing Analytics
    - Ad Networks
  created_at: '2020-02-17T10:50:10Z'
  edited_at: '2026-08-22T00:35:57Z'
  id: 360005854857
  locale: es
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/es/articles/360005854857
---
> **At a glance:** Los partners de API pueden usar su token de API para acceder a los datos de los anunciantes cuando el anunciante les concede permiso, lo que les permite extraer métricas de rendimiento de la plataforma.

<div id="api-token-permissions" />

## Permisos del token de API

<Image alt="api-access-permissions.jpg" src="https://files.readme.io/7961394cb39cf1e6f85d77cd732183edea5fb1408c220ca05b23ae7bbb50138e-23701010316689.jpg" width="439px" />

Los anunciantes pueden conceder los siguientes permisos a nivel de App:

| Tipo de permiso | Herramienta de reportes | Limitaciones |
| --- | --- | --- |
| Reportes analíticos agregados | <Anchor target="_blank" href="/marketers/es/docs/cohort-analytics-via-data-locker">Datos de análisis de cohortes a través de DataLocker</Anchor> | Los datos de campañas de X Ads no están disponibles para los partners de API debido a sus restricciones. |
| Reportes de SKAN | <ul><li><Anchor target="_blank" href="/marketers/es/docs/skan-aggregated-performance-report-api">Reporte de rendimiento de SKAN</Anchor></li><li><Anchor target="_blank" href="/marketers/es/docs/skan-aggregated-postback-arrival-date-api">Reporte agregado de postbacks de SKAN</Anchor></li></ul> | -- |


<div id="considerations" />

### Consideraciones

* **Perspectiva del anunciante**
  * Los anunciantes pueden conceder al partner de API los permisos indicados en la tabla anterior.
* **Perspectiva del partner**
  * Extrae datos a través de la API. **Nota**: la seguridad se implementa mediante un token de autenticación <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">token</Anchor> disponible en el dashboard de AppsFlyer. El mismo token es válido para todas las aplicaciones y todos los anunciantes.
  * Obtén datos a través de Data Locker
  * Los anunciantes pueden revocar los permisos de acceso a los datos de su aplicación. Esto no afectará a tus credenciales de partner.

<Accordion title="Conceder acceso al partner">

> 🚧 **Important**
>
> **advertencia**
>
> * El tipo de permiso permite al partner acceder a los datos, incluido el tráfico aportado por otros partners y datos orgánicos.
> * No compartas tu token con partners.

**Para conceder acceso a la API al partner:**

1. En AppsFlyer, en el menú lateral, selecciona **Collaborate** > **Integrated partners**.
2. Busque al socio y selecciónelo.
3. Haz clic en **Set up integration**. Se te dirigirá a la página de configuración de la integración.
4. En la pestaña **Acceso a la API**, activa uno o varios permisos. Selecciona una opción de:
   * **Reportes analíticos agregados**
   * **Reportes de SKAdNetwork** (para aplicaciones iOS, no relevante para Data Locker)
5. Haz clic en **Guardar acceso a la API**.
6. Notifica al partner que has habilitado el acceso a la API necesario.

</Accordion>

<div data-zendesk-anchors="api-access-permissions=permisos-del-token-de-api h_01HGG3N6KVF9MCQRW8594YG0HV=permisos-del-token-de-api considerations=consideraciones h_01HT2J7ZFVDA812R35948XXEM1=consideraciones h_01KZXND2TWVKK51RH3JWNMFENK=consideraciones" />
