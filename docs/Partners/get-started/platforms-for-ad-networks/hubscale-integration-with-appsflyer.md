---
title: Integración de Hubscale con AppsFlyer
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Hubscale
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
  created_at: '2017-12-19T12:25:07Z'
  edited_at: '2026-08-12T12:30:29Z'
  id: 115005874869
  locale: es
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/es/articles/115005874869
---
> **Resumen:** Descubre cómo las ad network que usan Hubscale pueden integrarse con AppsFlyer.

**Para iniciar la integración, debes enviar a AppsFlyer**:

1. Tu enlace de atribución
2. Tu postback (para instalaciones y eventos in-app)

<div id="creating-the-attribution-link" />

## Cómo crear el enlace de atribución

el enlace de atribución consta del enlace de atribución base de AppsFlyer que aparece a continuación y de macros adicionales añadidas por la ad network.

A continuación tienes el enlace de atribución base de AppsFlyer con una explicación detallada de cada macro:

| URL base de AppsFlyer | Nota |
| --- | --- |
| https://app.appsflyer.com | Punto de conexión de AppsFlyer |
| id\_aplicación | ID único de la aplicación: valor dinámico que cambia según la app promocionada |
| PID | Nombre de la fuente de medios concatenado con \_int para identificar redes integradas |
| C | Nombre de la campaña |

A continuación puedes ver cómo debe ser el enlace de atribución completo después de añadir las macros adicionales de Hubscale:

```http
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={affiliate_id}&af_sub5={offer_id}af_ad_id=
{offer_file_id}&advertising_id={google_aid}&idfa={ios_ifa}" target="
_blank" rel="nofollow noopener noreferrer" data-is-link="https://
app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid={transaction_id}
&af_siteid={affiliate_id}&af_sub5={offer_id}af_ad_id={offer_file_id}
&advertising_id={google_aid}&idfa={ios_ifa}">
https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=
{transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id=
{google_id}&idfa={ios_ifa}
```

<Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters">Lista completa de parámetros de AppsFlyer</Anchor>

<div id="global-postbacks-for-installs-and-in-app-events" />

## Postbacks globales para instalaciones y eventos in-app:

Hubscale tiene postbacks globales para instalaciones y eventos in-app:

Para instalaciones:

```http
https://companyname.156th.com/conv?transaction_id={publisher_ref_id}&ios_ifa={ios_ifa}
&google_id={google_aid}&app_version={app_version}&language={language}&ext_country_code={country_code}
&ext_city={city}&user_agent={user_agent}&user_ip={device_ip}&adv_revenue={revenue_usd}
```

Para los eventos posteriores a la instalación, Hubscale puede registrar hasta nueve eventos posteriores a la instalación para el mismo ID de transacción. Se deben crear nueve postbacks globales como plantillas, como se muestra a continuación:

<Table>
  <thead>
    <tr>
      <th>
        Número de evento
      </th>
      <th>
        Plantilla de URL
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Evento 2 (el evento 1 es la instalación)
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=2
        ```
      </td>
    </tr>
    <tr>
      <td>
        Evento 3
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=3
        ```
      </td>
    </tr>
    <tr>
      <td>
        Evento 4
      </td>
      <td>
        ...
      </td>
    </tr>
    <tr>
      <td>
        ...
      </td>
      <td>
        ...
      </td>
    </tr>
    <tr>
      <td>
        Evento 10
      </td>
      <td>
        ```http
        https://companyname.156th.com/conv?transaction_id={publisher_ref_id}
        &ios_ifa={ios_ifa}&google_id={google_aid}&app_version={app_version}
        &language={language}&ext_country_code={country_code}&ext_city={city}
        &user_agent={user_agent}&user_ip={device_ip}
        &adv_revenue={revenue_usd}&level=10
        ```
      </td>
    </tr>
  </tbody>
</Table>

La etiqueta de evento es la que introduce el anunciante al asignar los eventos.

<Image align="center" alt="In-App_Events.png" src="https://files.readme.io/5fa9ea3c2428e0dce7ce6a8062ebdf9aca5b2f873cc4e3d76d815d83b3a72b64-360002301369.png" />

Si el nombre del partner que usa Hubscale es PARTNER, entonces el dominio suele ser: partner.156th.com.

Enlace de atribución genérico:

```http
https://app.appsflyer.com/com.appsflyer?pid=partnername_int&clickid={transaction_id}&af_siteid={pub_id}-{sub_pub_id}&advertising_id={google_id}&idfa={ios_ifa}
```

<div id="finalizing-your-registration" />

## Finalización del registro

* Si tienes una integración con AppsFlyer, ponte en contacto con nosotros mediante el <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">widget del asistente para partners</Anchor>.
* Si no tienes una integración con AppsFlyer, completa la solicitud de registro de Partners de anuncios <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">aquí</Anchor>.

<div id="mapping-of-appsflyer-parameters-and-hubscale-macros" />

## Asignación de parámetros de AppsFlyer y macros de Hubscale

| Parámetros de AppsFlyer | Macros de Hubscale | Nota |
| --- | --- | --- |
| PID | pub\_id | Nombre de la fuente de medios: para partners integrados  <br />y no debe cambiarse. <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#partner-id-pid-parameter">Más detalles</Anchor>. |
| C | campaign\_name | Nombre de la campaña: proporcionado por el anunciante. |
| clickid | transaction\_id | El identificador de clics exclusivo de la red de publicidad |
| af\_siteid | pub\_id | ID de publisher de red de publicidad |
| af\_sub\_siteid | sub\_pub\_id | ID de publisher/subred de publicidad |
| af\_c\_id | id\_campaña | ID de campaña: proporcionado por el anunciante |
| af\_conjunto de anuncios |  | Nombre del conjunto de anuncios: proporcionado por el anunciante. El conjunto de anuncios  <br />es un nivel intermedio en la jerarquía entre  <br />campaña y anuncio. <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#niveles-de-granularidad-de-datos">Ver más</Anchor> |
| af\_anuncio | adv\_name | Nombre del anuncio (<Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#niveles-de-granularidad-de-datos">ver más</Anchor>) |
| id\_del\_anuncio\_af | adv\_id | Retargeting: Primer inicio después del re-engagement o la reatribución. |
| af\_modelo\_de\_coste | adv\_payout\_model | Modelo de costo: CPI es actualmente el único  <br />modelo admitido |
| af\_cost\_currency | adv\_payout\_currency | Código de divisa (por ejemplo: USD) |
| af\_valor\_de\_coste | adv\_payout\_amount | Valor del coste |

<div data-zendesk-anchors="creating-the-attribution-link=c%C3%B3mo-crear-el-enlace-de-atribuci%C3%B3n 01JFT1EB6KZE1D6C9HMXQ5A841=c%C3%B3mo-crear-el-enlace-de-atribuci%C3%B3n global-postbacks-for-installs-and-inapp-events=postbacks-globales-para-instalaciones-y-eventos-in-app 01JFT1EB6PH56T619J1197TAK2=postbacks-globales-para-instalaciones-y-eventos-in-app finalizing-your-registration=finalizaci%C3%B3n-del-registro 01JFT1EB70G5V9EBMD4XMAR3GF=finalizaci%C3%B3n-del-registro mapping-of-appsflyer-parameters-and-hubscale-macros=asignaci%C3%B3n-de-par%C3%A1metros-de-appsflyer-y-macros-de-hubscale 01JFT1EB71F36JD4QNB8KHKZRX=asignaci%C3%B3n-de-par%C3%A1metros-de-appsflyer-y-macros-de-hubscale" />
