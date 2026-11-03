---
title: Reporte agregado de rendimiento de la campaña para redes publicitarias
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketing Analytics
    - Ad Networks
  created_at: '2021-05-30T12:34:03Z'
  edited_at: '2026-08-12T12:27:11Z'
  id: 360020834237
  locale: es
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/es/articles/360020834237
---
> **De un vistazo**: De un vistazo: Las redes de publicidad cargan el reporte de estadísticas agregadas de rendimiento (también conocido como reporte de cohorte) en sus sistemas de Business Intelligence para calcular las métricas de rendimiento de la campaña, como el KPI de retención de 7 días.

## Reporte agregado de rendimiento de la campaña

Este reporte proporciona datos de rendimiento de la campaña, incluso la cantidad de usuarios únicos que realizan un evento determinado. Tú (la red publicitaria) usas los datos en tus sistemas de BI para calcular las métricas del rendimiento de la campaña en el contexto de los KPI de los anunciantes. El reporte está disponible diariamente a través de <Anchor target="_blank" href="/partners/es/docs/data-locker-for-partners">Data Locker para Socios</Anchor>

**¿Por qué necesitas el reporte?**

Antes de iOS 14.5, los postbacks que AppsFlyer enviaba contenían datos suficientes para calcular métricas únicas de eventos de usuarios.

A partir de iOS 14.5, y de la adopción por parte del anunciante de la Privacidad Avanzada Agregada (AAP), los postbacks de usuarios no autorizados no incluyen identificadores de usuario. La falta de identificadores impide calcular métricas de usuario únicas, por ejemplo, la retención de 7 días. La falta de métricas de usuario únicas perjudica tu capacidad de optimizar las campañas y la capacidad de establecer objetivos de retención comunes con los anunciantes.

**¿Qué contiene el reporte?**

Las métricas se proporcionan con la mejor granularidad posible usando las dimensiones reportadas y tienen las siguientes métricas de rendimiento:

* Ingresos
* Cantidad de veces que se realizó un evento
* Cantidad de usuarios únicos que realizan un evento
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vS89RlkFIss7uARroJcOcX1rU6gUmZ2ySYwfTprg9GaA2BYnvDPVqWmOicea1wrBnNuGgEuLPwzL_ac/pub?gid=0&single=true&output=csv">Ejemplo de informe</Anchor>

**¿Cómo se obtiene el reporte?**

* Proporcionado a través de Data Locker para Socios. El reporte actualiza la <Anchor target="_blank" href="/marketers/es/docs/about-data-freshness-and-timezone-support#daily">hora UTC diaria</Anchor>.
* Antes de empezar a compartir los datos contigo, los anunciantes deben [otorgar permisos](/docs/aggregated-campaign-performance-report-for-ad-networks#permission-to-get-aggregated-performance-data) en el dashboard.

## Sobre el reporte

<div id="report-structure" />

<Accordion title="Estructura del informe">

#### Dimensiones

<Table>
  <thead>
    <tr>
      <th>
        Nombre del campo
      </th>
      <th>
        Observaciones
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        id\_aplicación
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        fuente\_medios
      </td>
      <td>

      </td>
    </tr>
    <tr>
      <td>
        tipo\_de\_conversión
      </td>
      <td>
        * Valores posibles: instalación, re-engagement, reatribución
        * Macro de postback equivalente: is\_retargeting
      </td>
    </tr>
    <tr>
      <td>
        tipo\_táctil\_atribuido
      </td>
      <td>
        Valores posibles: click, impressions, pre-install, unknown, tv, null
      </td>
    </tr>
    <tr>
      <td>
        días\_post\_atribución
      </td>
      <td>
        La cantidad de días transcurridos desde el evento de atribución.  
        La cantidad máxima de días es de 180.

        Consejo: Consejo! Utiliza esto para calcular los días de retención y KPI
      </td>
    </tr>
    <tr>
      <td>
        Cadena
      </td>
      <td>
        La fecha en que ocurrió el evento.

        Formato: aaaa-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        fecha\_de\_conversión
      </td>
      <td>
        Formato: aaaa-mm-dd
      </td>
    </tr>
    <tr>
      <td>
        nombre\_del\_evento
      </td>
      <td>
        Identifica el evento. Algunos nombres de eventos tienen un significado específico, mientras que otros se relacionan con eventos in-app establecidos por el anunciante en la aplicación.

        | nombre\_del\_evento | ¿Qué hizo el usuario? |
        | --- | --- |
        | af\_conversion | Usuario convertido. Utiliza conversion\_type para identificar si se trata de una instalación, un reengagement o una reatribución. |
        | af\_sessions | Abrió la aplicación. |
        | af\_uninstall | Desinstaló la aplicación. |
        | Evento dentro de la aplicación definido por el anunciante. | Realizó un evento in-app en la aplicación. Los nombres de eventos in-app no se asignan a los nombres de eventos del socio. |
      </td>
    </tr>
    <tr>
      <td>
        campaña
      </td>
      <td>
        Jerarquía de campaña.
      </td>
    </tr>
    <tr>
      <td>
        id\_campaña
      </td>
      <td>
        Jerarquía de campaña.
      </td>
    </tr>
    <tr>
      <td>
        conjunto de anuncios
      </td>
      <td>
        Jerarquía de campaña.
      </td>
    </tr>
    <tr>
      <td>
        id\_anuncio
      </td>
      <td>
        Jerarquía de campaña.
      </td>
    </tr>
    <tr>
      <td>
        anuncio
      </td>
      <td>
        Jerarquía de campaña.
      </td>
    </tr>
    <tr>
      <td>
        id\_adset
      </td>
      <td>
        Jerarquía de campaña.
      </td>
    </tr>
    <tr>
      <td>
        canal
      </td>
      <td>
        Jerarquía de campaña.
      </td>
    </tr>
    <tr>
      <td>
        id\_sitio
      </td>
      <td>
        Jerarquía de campaña.
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        Úsalo para identificar y deduplicar datos de retargeting
      </td>
    </tr>
    <tr>
      <td>
        código\_de\_país
      </td>
      <td>
        Derivado de la dirección IP del usuario
      </td>
    </tr>
    <tr>
      <td>
        agencia
      </td>
      <td>
        Si está en blanco, no hay ninguna agencia asociada
      </td>
    </tr>
    <tr>
      <td>
        Palabras clave
      </td>
      <td>
        [Disponible a partir del 27 de abril de 2022] Palabra(s) utilizada(s) en la búsqueda en línea del usuario. Según lo reportado por la red de publicidad.
      </td>
    </tr>
    <tr>
      <td>
        ID de palabra clave
      </td>
      <td>
        [Disponible a partir del 27 de abril de 2022] ID de palabra clave devuelto por la red de publicidad.
      </td>
    </tr>
  </tbody>
</Table>

#### Métricas

| Nombre | Campo | Usuarios únicos que realizan el evento |
| --- | --- | --- |
| Usuarios únicos | usuarios\_únicos | Cantidad de usuarios únicos que realizan el evento |
| Ingresos | ingresos\_usd | Ingresos acumulados en USD. Por ejemplo, $100.00 se refleja como 100. |
| recuento\_eventos | recuento\_eventos | Cantidad de ocurrencias de eventos |

</Accordion>

<div id="bi-developer-considerations" />

<Accordion title="Consideraciones para desarrolladores de BI">

**Alcance de los datos en el informe**

El reporte contiene atribuciones, instalaciones, reatribuciones y re-engagements, y sus eventos in-app relacionados.

En tu proceso de consumo de datos, debes utilizar la lógica para dividir los datos entre los tipos de campaña. Es decir, atribución del usuario (instalaciones) y retargeting (re-engagements). Para hacerlo, usa el campo conversion\_type e is\_primary\_attribution. Consulta <Anchor target="_blank" href="/marketers/es/docs/resolve-retargeting-double-attribution">Doble atribución de eventos de retargeting.</Anchor>

**Consideraciones a nivel de campo**

* Usa los días post-atribución para facilitar el cálculo de métricas de retención.
* Cálculo de usuarios únicos usando las dimensiones de nombre de campaña y ID de campaña: Si puedes ignorar la precisión del nombre de la campaña, puedes sumar el recuento único por ID de campaña y las métricas serán correctas.
* Puedes agregar los datos usando los campos de jerarquía de la campaña.
* Los eventos in-app usan el nombre del evento del anunciante y no se asignan a los nombres de tus eventos. Pide al anunciante que te proporcione las asignaciones o que las vea en el dashboard. <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#g-in-app-event-postback-configuration">Asignación de eventos in-app para socios</Anchor>.
* Los ingresos en USD se calculan usando el tipo de cambio del día del evento.
* Los eventos de ingresos por publicidad se incluyen cuando están disponibles, pero se actualizan con un retraso de hasta 5 días.

**Consideraciones generales**

* Actualización de datos: Los datos se escriben en la carpeta Data Locker h=23.
* Los datos disponibles son datos de atribución de trayectoria del usuario atribuidos por AppsFlyer. Es decir, SKAdNetwork reportado por los postbacks de iOS no se incluye en este conjunto de datos.
* Los datos están contenidos en archivos que contienen varias aplicaciones. Usa el campo app\_id para identificar la aplicación.
* Si no obtienes datos para una aplicación determinada, verifica que el anunciante te haya otorgado los permisos necesarios.

</Accordion>

<div id="retention-report-considerations" />

<Accordion title="Consideraciones del reporte de retención">

Para crear métricas de retención, por ejemplo, el día 7 de retención, hazlo configurando filtros en los siguientes campos:

* days\_post\_install=7
* event\_name=af\_session
* conversion\_type según sea necesario
* Para evitar la inclusión de <Anchor target="_blank" href="/marketers/es/docs/resolve-retargeting-double-attribution">eventos de retargeting duplicados</Anchor>, selecciona is\_primary\_attribution=true o usa conversion\_type para limitar el conjunto de datos a las instalaciones.
* Agrupar por: campaña y otras dimensiones según sea necesario.
* Suma: unique\_users\_count

Al agregar o eliminar dimensiones, puedes obtener métricas con diferente granularidad.

</Accordion>

## Permisos

Tú (la red publicitaria) debes pedirle al anunciante que te conceda los permisos que se enumeran aquí. El anunciante debe realizar este procedimiento una vez por aplicación.

<div id="permission-to-get-aggregated-performance-data" />

<Accordion title="Permiso para obtener datos de rendimiento agregados">

Redes de publicidad designadas (activadas) por las agencias: La agencia no puede conceder el permiso. La agencia debe pedirle al anunciante que le otorgue los permisos.

**Para permitir que la red publicitaria obtenga datos de rendimiento agregados:**

1. En AppsFlyer, en el menú lateral, selecciona **Colaborar** > Partners integrados.
2. Busque al socio y selecciónelo.
3. Haz clic en **Configurar integración**. Se te dirigirá a la página de configuración de la integración.
4. Verifica que **Activar Partner** esté encendido. De lo contrario, los datos no se comparten.
5. Ve a la pestaña **Permissions** (Permisos).
6. Activa los siguientes permisos de red de publicidad:
   * **Acceder a datos agregados de conversiones**.
   * **Acceder a datos agregados de eventos in-app**.
   * **Acceder a datos agregados de ingresos**.
7. Haz clic en Guardar permisos.
8. Notifica a la red publicitaria que has concedido los permisos.
9. Si tienes varias aplicaciones, repite el procedimiento para cada aplicación integrada con el partner.

</Accordion>

<div data-zendesk-anchors="aggregated-campaign-performance-report=reporte-agregado-de-rendimiento-de-la-campa%C3%B1a h_01HM8SQ5RE1FGQDY6V1A8MMEQX=reporte-agregado-de-rendimiento-de-la-campa%C3%B1a about-the-report=sobre-el-reporte h_01HM8SQ5REM6MW5GBRSXTF0N73=sobre-el-reporte h_01HM8SQ5RETK7HCPZGGX8KX9VG=report-structure dimensions=dimensiones h_01HM8SQ5RE11PW6HGTWGC2AGR5=dimensiones metrics=m%C3%A9tricas h_01HM8SQ5RGQEH6G6W75FVWJKSP=m%C3%A9tricas h_01HM8SQ5RGCGTWTSRHB8B4FSY2=bi-developer-considerations h_01HM8SQ5RG4JEE75F6CBTFCBB5=retention-report-considerations permissions=permisos h_01HM8SQ5RGNXENZ89GD74KJWH2=permisos h_01HM8SQ5RGQADHTEP5ED3W87VZ=permission-to-get-aggregated-performance-data" />
