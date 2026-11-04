---
title: Especificación de enlaces de atribución para redes de publicidad
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2021-12-06T10:31:00Z'
  edited_at: '2026-08-12T12:28:17Z'
  id: 4412938154513
  locale: es
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/es/articles/4412938154513
---
> **En resumen:** Las redes de publicidad que se integran con AppsFlyer especifican su enlace de atribución como se describe en este artículo.

<div id="attribution-links-for-ad-networks" />

## Enlaces de atribución para redes de publicidad

Los enlaces de atribución se utilizan para notificar a AppsFlyer que un usuario interactuó con un anuncio al hacer clic en él. En su forma más simple, el enlace de atribución se coloca detrás de un anuncio, de modo que cuando un usuario hace clic en un anuncio, hace clic en un enlace de atribución.

<div id="attribution-model" />

### Modelo de atribución

Qué sucede en la trayectoria desde un primer clic o impresión hasta la atribución de una instalación o un evento, y más allá.

[![appsflyer-attribution-model-for-partners.png](https://files.readme.io/3f7536b15513a38dde0cdd82c889fc299a094a99339901cafcd6cd06c323b005-17990516210449.png)](https://files.readme.io/3f7536b15513a38dde0cdd82c889fc299a094a99339901cafcd6cd06c323b005-17990516210449.png)

1. Un usuario hace clic en un banner o en un enlace de oferta.
2. El banner o enlace redirige al usuario a un enlace de atribución de AppsFlyer. El enlace de atribución de AppsFlyer se completa con la información que se recopila durante el clic.
3. Recopilamos la información del enlace de atribución y la almacenamos en nuestra base de datos.
4. Se produce una instalación y la aplicación se abre por primera vez. El SDK de AppsFlyer dentro de la aplicación llama a nuestros servidores con la información sobre el dispositivo en el que está instalada la aplicación.
5. Emparejamos estos datos con nuestra base de datos de clics usando nuestros **métodos de atribución**:
   * **Coincidencia de referente**  
     Este método de atribución es exclusivo de los dispositivos Android. Cuando un usuario hace clic en un enlace y es redirigido a Google Play, Google Play le otorga un ID de referente único. Cuando se realiza la instalación, recopilamos este ID del dispositivo. Luego lo emparejamos con los registros de Google Play.
   * **Coincidencia de ID de dispositivo**  
     Emparejamos el ID del dispositivo (IDFA para dispositivos iOS o GAID para dispositivos Android) recopilado al hacer clic con el ID del dispositivo que realiza la instalación.
   * <Anchor target="_blank" href="/marketers/es/docs/appsflyer-attribution-model#probabilistic-modeling">**Modelado probabilístico**</Anchor>

   Más información sobre los <Anchor target="_blank" href="/marketers/es/docs/appsflyer-attribution-model">métodos de atribución</Anchor>.

   Buscamos el referente, el ID del dispositivo y los puntos de datos de modelado probabilístico (en ese orden) en nuestra base de datos de clics. Si encontramos una coincidencia, atribuimos la instalación al clic. Si no, atribuimos la instalación a una descarga orgánica.
6. Una vez que se atribuye la instalación, enviamos un postback con los detalles de la conversión a la red de publicidad.

Como se desprende de este flujo, utilizamos enlaces de atribución para obtener información sobre ti y postbacks para enviarte la información de vuelta.

<div id="note" />

> 📘 **Nota**
>
> Si utilizas herramientas de marketing de rendimiento de terceros, como TUNE, CAKE o Affise, consulta las <Anchor target="_blank" href="/partners/es/docs/platforms-for-ad-networks">instrucciones específicas de la plataforma</Anchor>.

<div id="attribution-link-template" />

### Plantilla de enlace de atribución

El enlace de atribución (el enlace detrás del banner/oferta) puede tener este aspecto:

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={clickid}&advertising_id={gaid}&af_siteid={affiliate_id}&af_cost_model=CPI&af_cost_value={cost_value}&af_cost_currency={currency}&c={Campaign}&af_ad_type={AdType}&af_adset={Adset}&af_ad={Ad}&is_incentivized={true\false}&expires={timestamp}&signature={signature}
```

`https://app.appsflyer.com/` es el punto de conexión de AppsFlyer, `com.yourapp` es el ID de la aplicación y `pid=mediaName_int` es un nombre de fuente de medios único que asignamos a tu red de publicidad.

Esta parte del enlace es estática y no requiere nada de tu parte.

Explicación de la estructura del enlace:

* Los valores después de '=' dentro de `{} son macros que completas cuando se realiza el clic y se envía a AppsFlyer. Cuando prepares tu plantilla, reemplaza el valor entre corchetes {}` con los nombres de tus parámetros.
* Los nombres de las macros no tienen importancia siempre que tu sistema los reemplace con los valores reales y correctos. Los parámetros antes del signo '=' son marcadores de posición utilizados por AppsFlyer para que sepamos qué valores nos envías.
* Para integrar con AppsFlyer, envíanos la plantilla de enlace de atribución por correo electrónico con los nombres de tus macros.

Considera los parámetros enumerados en la tabla siguiente como el mínimo recomendado. Admitimos un conjunto más amplio de parámetros. Deberías compartir con nosotros tanta información sobre el clic como recopiles. Consulta la <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#parámetros-del-enlace-de-atribución">lista de parámetros de enlaces de atribución</Anchor>.

<div id="recommended-minimum-attribution-link-parameters" />

#### Parámetros mínimos recomendados del enlace de atribución

| Parámetro | Descripción |
| --- | --- |
| `&clickid={clickid}` | El ID de clic es un identificador de clic único para cada clic que ocurre en tu red de publicidad. |
| `&advertising_id={gaid}` o  <br />`&idfa={IDFA}` | El ID del dispositivo en el que se realiza el clic (GAID para Android e IDFA para Apple). |
| `&c={campaign}` | El nombre de la campaña, tal como lo define el anunciante. |
| `&af_siteid={publisher_id}` | ID del publisher o afiliado que realizó el clic. |
| `&af_ad_type={search_text}` | Tipo de anuncio. Puedes utilizar una de las siguientes convenciones de nombres:  <br />search\_text  <br />banner  <br />interstitial  <br />video  <br />rewarded\_video  <br />playable  <br />sponsored\_content  <br />audio |
| `&af_adset={adsetid}` | Nombre del anuncio: proporcionado por el anunciante/publisher. El conjunto de anuncios representa un nivel intermedio en la jerarquía entre campaña y anuncio. <Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#niveles-de-granularidad-de-datos">Ver más</Anchor> |
| `&af_ad={ad_id}` | Nombre de anuncio (<Anchor target="_blank" href="/marketers/es/docs/about-link-structure-and-parameters#niveles-de-granularidad-de-datos">ver más</Anchor>): provisto por el anunciante/publisher. |
| `&is_incentivized={true}` | Campañas incentivadas o no incentivadas (pueden ser true/false) |
| `&af_cost_value={cost_value}` | Valor de costo de conversión: admite hasta 4 dígitos después del punto decimal.  <br />Asegúrate de utilizar ÚNICAMENTE dígitos numéricos (utiliza el punto decimal si es necesario), por ejemplo, "56", "2.85", etc. |
| `&af_cost_currency={currency}` | Divisa de costo: código de divisa (por ejemplo, USD, EUR). El valor predeterminado es USD.  <br /><Anchor target="_blank" href="https://en.wikipedia.org/wiki/ISO_4217">Lista de códigos de divisa</Anchor>. |
| `&expires={timestamp}` | Marca de tiempo de Unix después de la cual la red de publicidad no reclama el clic. Se utiliza para firmar los clics para evitar el fraude de clics. <Anchor target="_blank" href="/partners/es/docs/click-signing-for-ad-networks">Saber más</Anchor> |
| `&signature={signature}` | Firma HMAC-SHA256 utilizada para validar el clic y evitar fraudes. <Anchor target="_blank" href="/partners/es/docs/click-signing-for-ad-networks">Saber más</Anchor> |

<div data-zendesk-anchors="attribution-links-for-ad-networks=enlaces-de-atribuci%C3%B3n-para-redes-de-publicidad 01H8GPNM9XTR602BWRBQ5JV8DT=enlaces-de-atribuci%C3%B3n-para-redes-de-publicidad attribution-model=modelo-de-atribuci%C3%B3n 01H8GPNM9XSKS66F02GZQKK8E8=modelo-de-atribuci%C3%B3n 01H8GPNM9XBCVVXZ5HFKQZQ79D=nota attribution-link-template=plantilla-de-enlace-de-atribuci%C3%B3n 01H8GPNM9XS4JE8B1F6TJGKSBR=plantilla-de-enlace-de-atribuci%C3%B3n recommended-minimum-attribution-link-parameters=par%C3%A1metros-m%C3%ADnimos-recomendados-del-enlace-de-atribuci%C3%B3n 01H8GPNM9XD0GASJ93PNDGMDE8=par%C3%A1metros-m%C3%ADnimos-recomendados-del-enlace-de-atribuci%C3%B3n" />
