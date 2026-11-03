---
title: Activa la integración de la app de prueba para ad networks
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
  created_at: '2021-05-22T15:56:20Z'
  edited_at: '2026-09-11T00:36:50Z'
  id: 360020713538
  locale: es
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/es/articles/360020713538
---
> **At a glance:** Las ad network que realizan pruebas de integración deben activar la integración de la aplicación (activación).

## Aplicaciones de prueba para ad networks (iOS y Android)

Las ad networks, después de configurar la integración y los postbacks, deben probar la integración con las aplicaciones de prueba de AppsFlyer. Antes de realizar las pruebas, la ad network debe activar la integración de la app y habilitar permisos adicionales de la ad network según sea necesario. La activación se realiza una vez por aplicación.

| Tipo de aplicación de prueba | Nombre o ID de la aplicación |
| --- | --- |
| <Anchor target="_blank" href="/partners/es/docs/getting-started-onboarding-guide-for-ad-networks#parte-2-prueba-usando-aplicaciones-de-anunciantes">Android</Anchor> | com.appsflyer.adNetworkTest |
| <Anchor target="_blank" href="/partners/es/docs/ios-integration-testing-for-ad-networks">apps de iOS,</Anchor> | id1543229303 |
| <Anchor target="_blank" href="/partners/es/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> | <ul><li>id888707085</li><li>id888707086</li><li>id888707087</li></ul> |

### Procedimiento de activación

Utiliza el siguiente procedimiento para activar la integración de una app de prueba específica. Realiza el procedimiento una vez por aplicación.

**Para activar la integración y conceder permisos a una aplicación de prueba**:

1. En AppsFlyer, selecciona una aplicación de prueba de las que aparecen en la tabla anterior.
2. En AppsFlyer, en el menú lateral, selecciona **Collaborate** > **Partner Integrations** > **Active Integrations**.
3. Selecciona tu ad network.
4. **Para activar la integración con la aplicación**:  
   1. Ve a la pestaña **Integración**.
   2. Activa **Activar partner.**
   3. Haz clic en **Guardar integración**.
5. **Para conceder permisos**:
   1. Ve a la pestaña **Permissions** (Permisos).
   2. Activa **Configurar integración**.
   3. Activa **Configurar postbacks de eventos in-app.** Sin embargo, asegúrate de crear plantillas separadas con el subdominio; no agregues manualmente el subdominio al ID de plantilla.
   4. Haz clic en **Guardar permisos**.

<div data-zendesk-anchors="test-apps-for-ad-networks-ios-and-android=aplicaciones-de-prueba-para-ad-networks-ios-y-android h_01HKA15VM7FM69X0AZ1V2H5XPJ=aplicaciones-de-prueba-para-ad-networks-ios-y-android activation-procedure=procedimiento-de-activaci%C3%B3n h_01HKA15VM7J47374WMRG5132GN=procedimiento-de-activaci%C3%B3n" />
