---
title: Acceso a herramientas de análisis agregadas para socios de API
metadata:
  keywords:
    - Anunciantes
    - Redes de anuncios
    - Socios
    - Premium API
    - Marcadores
    - Análisis de marketing
x-zendesk:
  category: Socios
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marcadores
    - Análisis de marketing
    - Redes de anuncios
  created_at: '2020-02-17T10:50:10Z'
  edited_at: '08-2026-13T13:36:27Z'
  id: 360005854857
  locale: es-es
  section: Agregar datos
  section_id: 6551715006353
  url: >-
    https://support.appsflyer.com/hc/es/articles/360005854857-Access-to-aggregated-analytics-tools-for-API-partners
---
> **De un vistazo:** Los socios de la API pueden usar su token API para acceder a los datos de los anunciantes cuando el anunciante concede el permiso del anunciante permitiéndoles extraer métricas de rendimiento de la plataforma.

<div id="api-token-permissions" />

## Permisos de token API

<Image align="center" alt="api-access-permissions.jpg" src="https://files.readme.io/7961394cb39cf1e6f85d77cd732183edea5fb1408c220ca05b23ae7bbb50138e-23701010316689.jpg" width="439px" />

Los anunciantes pueden conceder los siguientes permisos a nivel de aplicación:

| Tipo de permiso               | Herramienta de reporte                                                                                                                                                                                                                                                                           | Limitaciones                                                                                                  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Informes analíticas agregados | <Anchor target="_blank" href="/marketers/docs/cohort-analytics-via-data-locker">datos analíticos de Cohort a través de DataLocker</Anchor>                                                                                                                                                       | Los datos de campaña de X anuncios no están disponibles para los socios de la API debido a sus restricciones. |
| Informes SKAN                 | <ul><li><Anchor target="_blank" href="/marketers/docs/skan-aggregated-performance-report-api">El rendimiento de SKAN reporta</Anchor></li><li><Anchor target="_blank" href="/marketers/docs/skan-aggregated-postback-arrival-date-api">SKAN agregación de postback reportando</Anchor></li></ul> | --                                                                                                            |

<div id="considerations" />

### Consideraciones

- **Perspectiva del anuncio**
  - Los anunciantes pueden conceder permisos a los socios de la API tal como se muestra en la tabla anterior.
- **Perspectiva de socio**
  - Extraer datos por API. **Nota**: La seguridad se implementa a través de una autenticación<Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">token</Anchor> disponible en el panel de control de AppsFlyer. El mismo token es válido para todas las aplicaciones y anunciantes.
  - Obtener datos a través de Data Locker
  - Los anunciantes pueden revocar los permisos para acceder a sus datos de la aplicación. Esto no afectará a sus credenciales de socio.

<Accordion title="Granting access to the partner">

<div id="important" />

> 🚧 **Importante**
>
> **advertencia**
>
> - El tipo de permisos permite al socio acceder a los datos, incluyendo el tráfico traído por otros socios y datos orgánicos.
> - No compartas tu token con tus socios.

**Para conceder acceso a la API al socio:**

1. En AppsFlyer, en el menú lateral seleccione **Colaborar** > **Socios integrados**.
2. Busca al socio y selecciónalo.
3. Haga clic en **Configurar integración**. Has sido dirigido a la página de configuración de integración.
4. Desde la pestaña **acceso API**, activa uno o más permisos. Seleccionar desde:
   - **Informes analíticos agregados**
   - **Informes SKAdNetwork** (para aplicaciones iOS, no relevantes para Locker de Datos)
5. Haga clic en **Guardar acceso API**.
6. Notificar al socio que ha habilitado el acceso a la API necesario.

</Accordion>

<div data-zendesk-anchors="api-access-permissions=api-token-permissions h_01HGG3N6KVF9MCQRW8594YG0HV=api-token-permissions h_01HT2J7ZFVDA812R35948XXEM1=considerations h_01KZXND2TWVKK51RH3JWNMFENK=considerations" />
