---
title: Reporte de Data Locker de Single Source of Truth (SSOT) para ad networks
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2024-07-31T19:51:34Z'
  edited_at: '2026-08-12T12:27:33Z'
  id: 27168206416017
  locale: es
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/es/articles/27168206416017
---
> **En resumen:** El reporte de Data Locker de Single Source of Truth (SSOT) ofrece una vista general unificada y precisa del rendimiento de las campañas de aplicaciones mediante la combinación de datos de varios métodos de atribución, como la coincidencia de ID y SKAN.  Proporciona una forma de cargar datos en tus sistemas de BI para obtener la máxima precisión de los datos.

<div id="note" />

> 📘 **Nota**
>
> * Antes de empezar a compartir los datos contigo, los anunciantes deben [otorgar permisos](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions) en el dashboard.
> * El reporte de SSOT Data Locker contiene datos basados en el LTV, no en actividades. Esto significa que los datos reflejan el lifetime value de los usuarios en todos los puntos de contacto, en lugar de su actividad in-app o de eventos.

<div id="what-is-data-locker" />

## ¿Qué es Data Locker?

Data Locker es una solución segura que entrega datos directamente a las principales plataformas en la nube, como AWS, GCS y Snowflake. Esto te permite integrar y consumir datos fácilmente en tus sistemas de BI internos para realizar análisis y reportes completos. <Anchor target="_blank" href="/partners/es/docs/data-locker-for-partners">Saber más</Anchor>

<div id="what-is-single-source-of-truth-ssot" />

## ¿Qué es Single Source of Truth (SSOT)?

Tiene como objetivo resolver los problemas de fragmentación de datos al ofrecer una vista general unificada y precisa del rendimiento de las campañas de aplicaciones mediante la combinación de datos de varios métodos de atribución, como la coincidencia de ID y SKAN. <Anchor target="_blank" href="/marketers/es/docs/single-source-of-truth-ssot-guide-for-ios-attribution">Saber más</Anchor>

<div id="benefits-of-ssot-reports-in-data-locker" />

## Ventajas de los reportes SSOT en Data Locker

El reporte de Single Source of Truth proporciona la misma visibilidad que utilizan los marketers para analizar y medir el rendimiento.

* **Obtén una vista de atribución completa y precisa:** SSOT gestiona la lógica de combinar datos de diferentes métodos de atribución, lo que evita de manera efectiva que se cuenten dos veces las instalaciones atribuidas mediante varios métodos de atribución. Esto garantiza que los datos sean precisos y reflejen el verdadero comportamiento y atribución de los usuarios.
* **Carga datos en tus sistemas de BI:** La SSOT proporciona una forma eficiente y precisa de cargar los datos agregados en tus sistemas de BI internos. Esto incluye las atribuciones, los eventos in-app y los datos de ingresos, que abarcan todas las dimensiones y métricas.

<div id="setting-up-data-locker" />

<Accordion title="Configuración de Data Locker">

Usa este procedimiento para configurar Data Locker. Los cambios en la configuración tienen efecto en 3 horas.

**Requisitos previos:**

Completa uno o más de los siguientes procedimientos de almacenamiento:

* <Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor> bucket
* <Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor> bucket
* [Beta] <Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor> bucket
* Almacén de datos de <Anchor target="_blank" href="/marketers/es/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor>

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Para configurar Data Locker:**

1. Inicia sesión en tu <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">dashboard de partners de AppsFlyer.</Anchor>
2. Ve a:
   * **Anunciantes:Reporte** > **Data Locker**.
   * **Partners de marketing**: Haz clic en el  **menú de la cuenta** > **Data Locker**.
3. Sigue los pasos 3 al 16 para <Anchor target="_blank" href="/marketers/es/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">Instrucciones de configuración de Data Locker</Anchor> .

</Accordion>

<div id="permissions" />

<Accordion title="Permisos">

Ad networks designadas (activadas) por las agencias: La agencia no puede conceder el permiso. La agencia debe pedirle al anunciante que le otorgue los permisos.

**Para permitir que la ad networks obtenga datos de Single Source of Truth (SSOT):**

1. En AppsFlyer, en el menú lateral, selecciona **Colaborar** > **Partners integrados**.
2. Busca al partner y selecciónalo.
3. Haz clic en **Configurar integración**. Se te dirigirá a la página de configuración de la integración.
4. Verifica que **Activar partner**esté encendido. De lo contrario, los datos no se comparten.
5. Ve a la pestaña **Permisos** .
6. Activa los siguientes permisos de ad network:
   * **Acceder a datos agregados de conversiones**.
   * **Acceder a datos agregados de eventos in-app**.
   * **Acceder a datos agregados de ingresos**.
7. Haz clic en **Guardar permisos**.
8. Notifica a la ad network que has concedido los permisos.
9. Si tienes varias aplicaciones, repite el procedimiento para cada aplicación integrada con el partner.

</Accordion>

<div id="ssot-report-facts" />

<Accordion title="Reportar hechos de SSOT">

| Nombre | Descripción |
| --- | --- |
| Reportes disponibles | Los siguientes reportes están disponibles:<ul><li>Adquisición de usuarios: atribuye las conversiones a los canales de adquisición de usuarios. Esto incluye la actividad posterior a la instalación que se produce durante las ventanas de reengagement.</li><li>Retargeting: atribuye las conversiones a los canales de retargeting para los eventos que ocurren:<ul><li>Como resultado de reatribuciones.</li><li>Durante una ventana de reengagement.</li></ul></li><li>Unificado: atribuye las conversiones al canal de último contacto, de acuerdo con las reglas de <Anchor target="_blank" href="/marketers/es/docs/resolve-retargeting-double-attribution">doble atribución</Anchor> de AppsFlyer. Esto significa que la actividad posterior a la instalación que se produce durante los reengagements se muestra en la fuente de medios de retargeting y no en la fuente multimedia de UA.</li></ul> |
| Período de reporte | El reporte proporciona métricas de cohorte hasta 7 días después de la instalación. |
| Estructura de directorios | La estructura de directorios está organizada por fecha de instalación. Cada carpeta de fecha de instalación incluye varias versiones creadas a diario. Cada versión refleja los datos acumulativos actualizados para esta fecha de instalación. Esto significa que solo debes procesar la última versión del reporte disponible. <Anchor target="_blank" href="/marketers/es/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#estructura-de-directorios">Saber más</Anchor> |
| Estructura del reporte | El esquema del reporte (incluidas las dimensiones y las métricas) es fijo y no se puede modificar. |
| Zona horaria | UTC |
| Actualización de datos | <ul><li>A diario.</li><li>Las métricas se calculan con los datos disponibles a medianoche UTC, que es el final del día.</li><li>SLA: Los nuevos reportes estarán disponibles en Data Locker antes de las 16:00 UTC. Cada día se crea una nueva versión para las últimas 15 fechas de instalación. <Anchor target="_blank" href="/marketers/es/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#report-folder-hierarchy">Ver más</Anchor></li></ul> |

</Accordion>

<div id="report-structure" />

## Estructura del reporte

El reporte se compone de dimensiones y métricas.

Las métricas cubren los datos de las atribuciones, los ingresos y los usuarios únicos que realizan un evento.

<div id="field-formats" />

<Accordion title="Formatos de campo">

<Table>
  <thead>
    <tr>
      <th>
        Nombre del formato
      </th>
      <th>
        Descripción
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Cadena [n]
      </td>
      <td>
        La longitud máxima de la cadena. Por lo general, no aplicamos limitaciones de longitud de campo al recibir los datos, pero los datos pueden truncarse como consecuencia de ello.
      </td>
    </tr>
    <tr>
      <td>
        Cadena de tiempo
      </td>
      <td>
        Las cadenas tienen el formato:

        ```
        yyyy-mm-dd hh:mm:ss.
        ```

        Por ejemplo:

        ```
        2019-09-17 00:09:25
        ```
      </td>
    </tr>
    <tr>
      <td>
        Enumeración [n]
      </td>
      <td>
        Los campos de enumeración solo pueden contener valores específicos. Por ejemplo, selected\_currency tiene 3 caracteres y solo puede contener los códigos de moneda especificados.
      </td>
    </tr>
    <tr>
      <td>
        Marca de tiempo
      </td>
      <td>
        Marca de tiempo UNIX de 10 dígitos. Ejemplo:  
        4 de agosto de 2020 a las 07:25 UTC se traduce como

        ```
         "timestamp": "1596525944"
        ```
      </td>
    </tr>
    <tr>
      <td>
        Booleano
      </td>
      <td>
        El valor del campo puede ser *TRUE* o *FALSE*
      </td>
    </tr>
    <tr>
      <td>
        Entero
      </td>
      <td>
        Entero
      </td>
    </tr>
    <tr>
      <td>
        Flotante
      </td>
      <td>
        Número flotante real que puede tener un punto decimal y valores después del punto decimal.
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="dimensions" />

<Accordion title="Dimensiones">

<Table>
  <thead>
    <tr>
      <th>
        Nombre del campo
      </th>
      <th>
        Descripción
      </th>
      <th>
        Formato
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        id\_del\_anuncio\_af
      </td>
      <td>
        Identificador de anuncios. Jerarquía de campañas.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_anuncio
      </td>
      <td>
        Nombre del anuncio.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_adset\_id
      </td>
      <td>
        Identificador del conjunto de anuncios. Jerarquía de campañas.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_conjunto de anuncios
      </td>
      <td>
        Nombre del conjunto de anuncios.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        id\_aplicación
      </td>
      <td>
        ID de aplicación (aplicación del anunciante) con ID de prefijo.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        attribution\_method
      </td>
      <td>
        El mecanismo utilizado para atribuir el evento. Los ejemplos de dichos mecanismos incluyen los métodos de AppsFlyer, SKAdNetwork (SKAN) y orgánicos.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        tipo\_táctil\_atribuido
      </td>
      <td>
        Valores posibles: impresión de clic, nulo.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        campaña única
      </td>
      <td>
        Nombre de la campaña reportada por la ad network a AppsFlyer.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        af\_c\_id
      </td>
      <td>
        Identificador de campaña.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        días\_post\_atribución
      </td>
      <td>
        Número de días transcurridos desde la fecha de conversión (no desde la marca de tiempo específica de la conversión).  
        Consejo: ¡Consejo! Utiliza esto para calcular los días de retención y KPI
      </td>
      <td>
        Entero
      </td>
    </tr>
    <tr>
      <td>
        nombre\_del\_evento
      </td>
      <td>
        Identifica el evento. Algunos nombres de eventos tienen un significado específico, mientras que otros se refieren a eventos in-app establecidos por el anunciante.

        | nombre\_del\_evento | ¿Qué hizo el usuario? |
        | --- | --- |
        | af\_conversion | Usuario convertido. Utiliza conversion\_type para identificar si se trata de una instalación, una descarga repetida, una reatribución o un reengagement. o re-engagement. |
        | Evento in-app definido por el anunciante | Realizó un evento in-app en la aplicación. |
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        geolocalización
      </td>
      <td>
        El código ISO de país. Los datos se derivan de la dirección IP del usuario en los métodos de atribución clásicos de AppsFlyer, mientras que en SKAN los datos se enriquecen a partir de ad networks o se modelan.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        fecha\_de\_instalación
      </td>
      <td>
        SKAN: Estimado por AppsFlyer, en función de la hora de llegada del postback.

        AF:

        * UA: La primera apertura después de la instalación.
        * Retargeting: La primera apertura después del reengagement o la reatribución
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        es\_atribución\_primaria
      </td>
      <td>
        UA: verdadero

        Retargeting: Durante una ventana de re-engagement, atribuimos tanto a la fuente de medios original (previa al re-engagement) como a la fuente de medios de re-engagement. Mientras el evento está dentro de la ventana de re-engagement. La fuente de medios original será FALSE (no es la atribución principal). La fuente de medios de reengagement será TRUE.
      </td>
      <td>
        bool
      </td>
    </tr>
    <tr>
      <td>
        fuente\_de\_medios
      </td>
      <td>
        Ad network atribuida a un evento.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        selected\_currency
      </td>
      <td>
        Código de la moneda de 3 letras (USD, EUR) establecido por ti en la configuración de la aplicación. Formato ISO-4217. Es la misma moneda que se usa para mostrar los ingresos en la interfaz de usuario de SSOT.
      </td>
      <td>
        string
      </td>
    </tr>
    <tr>
      <td>
        tipo\_de\_conversión
      </td>
      <td>
        Valores posibles:  
        Instalación: El usuario descarga y abre una aplicación por primera vez.  
        Reatribución: El usuario vuelve a instalar la app y se atribuye a una nueva campaña.  
        Vuelve a descargar la aplicación (SKAN): El usuario vuelve a instalar la aplicación después de desinstalarla.  
        Reengagement: Reengagement: El usuario vuelve a abrir la aplicación después de interactuar con un anuncio de retargeting.
      </td>
      <td>
        string
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="metrics" />

<Accordion title="Métricas">

| Nombre de ID elegido | Descripción | Formato |
| --- | --- | --- |
| revenue\_selected\_currency | El monto de ingresos acumulados en la moneda seleccionada. Máximo de dos posiciones después del punto decimal.  <br />Ejemplo: En el caso de event\_name=purchase con days\_post\_attribution=2, el valor refleja los ingresos totales de los eventos de compra dentro de los dos días posteriores a la instalación (no solo el segundo día). | double |
| ingresos\_usd | El monto de los ingresos acumulados en USD.  <br />Ejemplo: En el caso de event\_name=purchase con days\_post\_attribution=2, el valor refleja los ingresos totales de los eventos de compra dentro de los dos días posteriores a la instalación (no solo el segundo día). | double |
| skan\_duplicates | Las instalaciones atribuidas simultáneamente por SKAN y otros métodos de AF se eliminan para evitar el doble recuento en los datos de SSOT. | long |
| uninstalls\_count | Cantidad de usuarios de la aplicación que instalan la aplicación y que posteriormente la desinstalan (eliminan) (relevante solo para la adquisición de usuarios). | long |
| usuarios\_únicos | Cantidad de usuarios distintos que realizan un evento. Los valores son acumulativos.  <br />Ejemplo: Para event\_name=purchase con days\_post\_attribution=2, el valor refleja los usuarios únicos que realizaron compras dentro de los dos días posteriores a la instalación (no solo el segundo día). | Entero |

</Accordion>

<div id="modeled-data" />

<Accordion title="Datos modelados">

AppsFlyer modela datos que los reportes básicos de SKAdNetwork no pueden proporcionar.

* Valores de conversión nulos (CV): En SKAN, Apple puede reemplazar los datos reales por un valor "Nulo" para mantener la privacidad del usuario. Para garantizar que no se omita ningún dato, estos valores nulos se modelan en SSOT. <Anchor target="_blank" href="/marketers/es/docs/skan-modeled-data#null-conversion-values">Saber más</Anchor>
* Métricas posteriores a la instalación más largas: La granularidad de los datos de SKAN para los períodos posteriores a la instalación más allá de los dos primeros días es limitada, lo que puede generar imprecisiones. Para mantener una alta calidad de los datos, modelamos los ingresos y los usuarios únicos de eventos in-app para days\_post\_attribution superiores a 2. <Anchor target="_blank" href="/marketers/es/docs/skan-modeled-data#revenue-ltv">Saber más</Anchor>

Datos de geolocalización: SKAN limita la granularidad de los datos y, a menudo, hace que los datos de geolocalización no estén disponibles. En estos casos, modelamos los datos para permitir un análisis de rendimiento eficiente. <Anchor target="_blank" href="/marketers/es/docs/skan-modeled-data#geo">Saber más</Anchor>

</Accordion>

<div id="partial-data" />

<Accordion title="Datos parciales">

Al analizar los últimos días de instalación, es posible que las métricas de los períodos prolongados posteriores a la instalación (por ejemplo, 7 días) no sean completas. En esos casos, las métricas seguirán estando disponibles, pero reflejarán datos parciales.

Algunas reglas generales:

* El reporte muestra todos los datos existentes tan pronto como estén disponibles.
* Transcurridos 5 días, se completan las métricas de los dos días posteriores a la instalación*.
* Transcurridos 7 días, se completan las métricas de los siete días posteriores a la instalación. Hasta 15 días después de la instalación, el modelo puede refinar este valor.

Motivos de los datos parciales:

* Madurez de los datos: Cuando el tiempo transcurrido desde la fecha de instalación es inferior al de los días que se están analizando, los datos se siguen acumulando y aún no están completos.
* Retrasos de SKAN: Los datos de SKAN se reciben con un retraso aleatorio. Por ejemplo, la actividad posterior a la instalación de los dos primeros días se puede recibir hasta 96 horas (4 días) después de la instalación.
* Sincronización de datos modelados: Se modelan los datos de SKAN para períodos superiores a 2 días después de la instalación. Nuestros modelos generan el primer valor estimado después de 7 días. Durante este período (días del 2 al 7), los datos de los métodos de atribución clásicos de AppsFlyer están disponibles, mientras que los datos modelados de SKAN no.

Ejemplos (suponiendo que la fecha de instalación sea el 1 de enero):

* El 2 de enero: Aún no se han recibido los datos de SKAN. Los datos de 2 días después de la instalación equivaldrán a los datos de menos de 7 días después de la instalación, y ambos son parciales y consisten en datos de los métodos de atribución clásicos de AppsFlyer.
* El 3 de enero: Los datos SKAN se reciben parcialmente. Los datos de los 2 días posteriores a la instalación seguirán siendo parciales y ahora contienen parcialmente datos de SKAN. Los datos de los 7 días posteriores a la instalación aún no incluirán ningún dato SKAN modelado (el primer valor modelado está disponible 7 días después de la instalación). Por lo tanto, entre los días 2 y 7 después de la instalación, es posible que veamos un valor inferior para los 7 días posteriores a la instalación en comparación con los 2 días posteriores a la instalación.
* El 6 de enero: Los datos de SKAN de los dos primeros días posteriores a la instalación se recibieron en su totalidad, incluidos los postbacks con el máximo retraso posible. Se han completado las métricas correspondientes a los dos días posteriores a la instalación. En este momento, las estadísticas de los 7 días posteriores a la instalación aún no se han completado.
* El 8 de enero: Los datos modelados de SKAN durante los 7 días posteriores a la finalización de las instalaciones. Nuestro modelo seguirá refinando el valor hasta el 16 de enero.

</Accordion>

<div id="directory-structure" />

## Estructura de directorios

<div id="report-folder-hierarchy" />

<Accordion title="Jerarquía de carpetas de reportes">

* Las carpetas principales están organizadas por tipo de reporte. Valores posibles: ‘ssot\_unified’, ‘ssot\_retargeting’, and ‘ssot\_user\_acquisition’.
* Dentro de estas carpetas, las subcarpetas se organizan por fecha de instalación.

**Versiones**

* Cada carpeta de fecha de instalación contiene varias versiones, que se crean a diario.
* Cada versión refleja los datos acumulativos actualizados para esa fecha de instalación.
* Los reportes incluirán todos los datos disponibles para la fecha de instalación. Por ejemplo, el 18 de abril, la versión más reciente de cada fecha de instalación contiene todos los datos hasta ese momento del 18 de abril.
* Consejo: Procesa siempre la última versión del reporte disponible para garantizar la precisión.

Cada fecha de instalación está limitada a un máximo de 15 versiones. Después de 15 días, todas las métricas están completamente corregidas y completadas. <Anchor target="_blank" href="/marketers/es/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Saber más</Anchor>

</Accordion>

<div id="directory-and-filename-structure" />

<Accordion title="Estructura de directorios y nombres de archivos">

La ruta al reporte tiene el siguiente formato:

`<bucket-name>`/t=`<ssot_unified OR ssot_retargeting OR ssot_user_acquisition>`/install\_date=`<yyyy-mm-dd>`/version=`<unix timestamp>`/`<parquet file number>`

Ejemplo de jerarquía de carpetas en el bucket del anunciante:

```
bucket
|
└── t=ssot_unified
    |
    ├── install_date=2024-05-05
    |   |
    |   └── version=1714890235
    |   |    |
    |   |    ├── part-00000-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    |
    |   |    ├── part-00001-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    │
    |   |    └── part-00002-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |
    |   |
    |   └── version=1714890286
    |        |
    |        ├── part-00000-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        |
    |        ├── part-00001-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        │
    |        └── part-00002-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |   |
    .   . 
    .   .
```

Leyenda:

* t: Tema del reporte (tipo).
* install\_date: La fecha de instalación de la aplicación. install\_date: La fecha de instalación de la aplicación Esto significa que la actividad posterior a la instalación aparecerá en función de la fecha de instalación en la que el usuario descargó la aplicación, no del día en que se produjo la acción del usuario.
* Versión: Marca de tiempo de Unix que indica cuándo se creó la versión.

</Accordion>

<div id="bi-developer-considerations" />

## Consideraciones para desarrolladores de BI

**Alcance de los datos en el reporte:**

Los reportes contienen datos sobre las instalaciones de adquisición de usuarios, las reatribuciones de retargeting (descargas repetidas en SKAN) y los reengagements, junto con sus eventos in-app relacionados.

<div id="loading-reports" />

<Accordion title="Carga de reportes">

Puedes cargar reportes unificados, de adquisición de usuarios y de retargeting por separado o juntos en tu BI. Si los cargas juntos y quieres filtrar las vistas por tu cuenta:

* Reportes unificados: Utiliza el campo is\_primary\_attribution=true o null.
* Reportes de adquisición de usuarios: Utiliza conversion\_type=install.
* Reportes de retargeting Utiliza conversion\_type=re-engagement o re-attribution.
* Vista unificada: Si utilizas la vista unificada en el proceso de carga de datos, puedes dividir los datos entre los tipos de campaña:

* Usa conversion\_type=install, re-engagement o re-attribution (descargas repetidas en SKAN).
* Consulta la sección “Doble atribución de eventos de retargeting” para obtener más información

</Accordion>

<div id="days-postattribution" />

<Accordion title="Días después de la atribuación">

<div id="important" />

> 🚧 **¡Importante!**
>
> El reporte incluye una dimensión, days\_post\_attribution, que asocia los ingresos y los datos de usuario únicos con el número específico de días posteriores a la instalación.

* Para las atribuciones (instalaciones, re-engagements, etc.), el valor es 0.
* En cuanto a los ingresos y los eventos in-app, los datos se clasifican en grupos predefinidos, actualmente limitados a “2” días y “7” días después de la instalación.

**Para analizar con precisión los eventos in-app y los ingresos, debes aplicar un filtro para la dimensión days\_post\_attribution.** Consulta el ejemplo de query que aparece a continuación.

Un ejemplo de error común es aplicar una lógica simplificada que suma la columna de ingresos de un conjunto específico de dimensiones. Este enfoque da como resultado números incorrectos porque algunos datos de ingresos se cuentan dos veces (una vez para days\_post\_install=2 y otra para days\_post\_install=7). Este ejemplo también es relevante cuando se analizan usuarios únicos para eventos in-app específicos.

</Accordion>

<div id="considerations" />

<Accordion title="Consideraciones">

**Consejos y consideraciones:**

* Última versión: Consulta siempre la última versión disponible para cada fecha de instalación para asegurarte de que estás trabajando con los datos más actualizados y precisos para tu análisis.
* Cálculo de ingresos: Los ingresos en USD se calculan usando el tipo de cambio del día del evento.
* Analiza las atribuciones: Registros en los que event\_name=af\_conversion reflejan las atribuciones (instalaciones, reatribuciones (descargas en SKAN) y re-engagements). El recuento de atribuciones aparece en la métrica de usuarios únicos y las métricas de ingresos de estos campos estarán vacías. El valor de days\_post\_attribution será 0.
* Comparación de dashboard: Al comparar las instalaciones con las del dashboard, suma los tipos de conversión que se vuelven a descargar y los que se instalan, ya que el dashboard considera ambos en la columna de instalación.
* Analiza los eventos in-app: Los registros en los que event\_name no es igual a 'af\_conversion' reflejan eventos in-app. El recuento de usuarios únicos que realizan el evento aparece en la métrica de usuarios únicos, mientras que los ingresos generados por estos eventos aparecen en las métricas de ingresos.
* Tipo de conversión: Diferencia las conversiones de adquisición de usuarios y de retargeting utilizando esta dimensión. Ten en cuenta que hay disponible una pausa adicional para los datos de SKAN (instalaciones vs volver a descargar la app). Al comparar los datos con el dashboard de SSOT, ambos tipos se consideran instalaciones.
* Eventos de ingresos por publicidad: Se incluyen cuando están disponibles.
* Segregación de datos: Todos los datos de la aplicación se proporcionan en un único archivo. Usa el campo ID de aplicación para segregar datos por aplicación o configura Data Locker para que segregue por aplicación.

</Accordion>

<div id="example-use-cases" />

<Accordion title="Ejemplos de casos de uso">

Los siguientes son ejemplos de algunas aplicaciones prácticas y populares de los datos que los desarrolladores de BI pueden extraer a través de Data Locker. Cada ejemplo está ilustrado por una declaración SQL y un objeto visual de Excel de muestra.

<div id="calculating-total-attributions-per-campaign" />

<Accordion title="Calcular el total de atribuciones por campaña">

En esta consulta, hacemos lo siguiente:

* Suma el total de atribuciones únicas por campaña para cada fecha de instalación.
* Filtra las conversiones con el nombre del evento “af\_conversion” y un ID de campaña específico (af\_c\_id).

```sql
SELECT install_date, SUM(unique_users) AS total_attributions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Cambia a tu campaña específica
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign" />

<Accordion title="Calcular las conversiones (instalaciones y descargas repetidas) para compararlas con las instalaciones en el dashboard por campaña única">

En esta consulta, hacemos lo siguiente:

* Cuenta las conversiones distinguiendo entre nuevas instalaciones y descargas repetidas por campaña y fecha de instalación únicas.
* Compara las instalaciones con la métrica de instalación del dashboard, que combina los tipos de conversión “instalación” y “volver a descargar”.

```sql
SELECT install_date, conversion_type, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND conversion_type IN ('install', 're-download')    
-- The dashboard sums both under the install field
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type;
```

</Accordion>

<div id="calculating-retargeting-conversions-per-geo" />

<Accordion title="Calcular las conversiones de retargeting por zona geográfica">

En esta consulta, hacemos lo siguiente:

* Cuenta las conversiones de las campañas de retargeting desglosadas por ubicación geográfica.
* Teniendo en cuenta los tipos de “reatribución” y “re-engagement” para estas conversiones.

```sql
SELECT install_date, conversion_type, geo, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type IN ('re-attribution', 're-engagement')    
-- Both types are relevant for re-targeting
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type, geo;
```

</Accordion>

<div id="calculating-installs-by-attribution-method-per-media-source" />

<Accordion title="Cálculo de las instalaciones por método de atribución por fuente de medios">

En esta consulta, hacemos lo siguiente:

* Cuenta las instalaciones por métodos de atribución (SKAN, métodos de AppsFlyer y orgánicos) y divídelas por fuente de medios.
* Filtra según los eventos de “af\_conversion” con un tipo de conversión de “instalar”.

```sql
SELECT install_date, attribution_method, media_source, SUM(unique_users)   
AS total_installs
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type = 'install'
    AND app_id = 'YOUR_APP'
GROUP BY install_date, attribution_method, media_source;
```

</Accordion>

<div id="calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset" />

<Accordion title="Calcular los ingresos acumulados de 7 días después de la instalación para Facebook por conjunto de anuncios">

En esta consulta, medimos los ingresos acumulados en un período de 7 días después de la instalación de los anuncios publicados en Facebook.

```sql
SELECT install_date,
       af_adset,
       SUM(revenue_usd) AS total_revenue_day_7
FROM ssot_unified
WHERE media_source = 'facebook'
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_adset;
```

</Accordion>

<div id="calculating-cumulative-revenue-for-selected-postinstall-periods" />

<Accordion title="Calcular los ingresos acumulados para los períodos posteriores a la instalación seleccionados">

En esta consulta, hacemos lo siguiente:

* Calcula los ingresos acumulados para varios días seleccionados después de la instalación, desglosando las sumas para el día 2 y el día 7.
* Ten en cuenta que al analizar las instalaciones de los últimos 7 días, es posible que los datos de los 7 días posteriores a la instalación estén incompletos. <Anchor target="_blank" href="/marketers/es/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Saber más</Anchor>

```sql
SELECT install_date,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) AS total_revenue_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) AS total_revenue_day7
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source" />

<Accordion title="Calcular los ingresos de un evento in-app específico (compra) por fuente de medios">

En esta consulta, hacemos lo siguiente:

* Mide el valor de los ingresos de un evento in-app específico (como “af\_purchase”) y suma esos datos por fuente de medios.
* Filtra los días seleccionados después de la instalación para asegurarte de que los datos no se cuenten dos veces.

```sql
SELECT install_date, media_source, SUM(revenue_usd) AS total_purchase_revenue
FROM ssot_unified
WHERE event_name = 'af_purchase'  -- Change to your specific event
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

<div id="calculating-inapp-event-conversion-rate-for-2-days-postinstalls" />

<Accordion title="Calcular la tasa de conversión de eventos in-app durante 2 días después de la instalación">

En esta consulta, calculamos la tasa de conversión de un evento in-app específico (como “af\_complete\_tutorial”) en relación con todas las instalaciones.

```sql
SELECT install_date,
  SUM(IF(days_post_attribution = 2 AND   
event_name = 'af_complete_tutorial', unique_users, 0)) 
  / SUM(IF(event_name = 'af_conversion', unique_users, 0))   
AS conversion_rate_day2_af_tutorial_conversion
FROM ssot_unified
WHERE conversion_type = 'install'    
-- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id" />

<Accordion title="Calcular el ARPU durante 7 días y 2 días después de la instalación por ID de campaña">

En esta consulta, hacemos lo siguiente:

* Calcula el ingreso promedio por usuario (ARPU) para el día 2 y el día 7 después de la instalación en todas las campañas.
* Ten en cuenta que al analizar las instalaciones de los últimos 7 días, es posible que los datos de los 7 días posteriores a la instalación estén incompletos. <Anchor target="_blank" href="/marketers/es/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">Saber más</Anchor>

```sql
SELECT install_date,
       af_c_id,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day7
FROM ssot_unified
WHERE conversion_type = 'install'  
       -- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_c_id;
```

</Accordion>

<div id="calculating-amount-of-duplicates-per-media-source-in-this-query" />

<Accordion title="Calcular la cantidad de duplicados por fuente de medios">

En esta consulta, contamos el número total de atribuciones de usuarios duplicadas por fuente de medios y fecha de instalación, para destacar los canales multimedia que pueden tener una mayor duplicación en la atribución de usuarios.

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
    AND event_name = 'af_conversion'
GROUP BY install_date, media_source;
```

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Rasgos y limitaciones">

| Caducado | Nota |
| --- | --- |
| Disponibilidad de reporte por día | Solo los días de instalación en los que el selector de SSOT estaba activado al final del día tendrán un reporte de SSOT para ese día. |
| Métricas de dos días post-instalación | <ul><li>Para SKAN 4 en Conversion Studio: Los datos son de 2 días posteriores a la instalación.</li><li>Para SKAN 3 en Conversion Studio: Los datos se basan en la ventana de actividad de SKAN definida.<br />Ejemplo: Si el período de actividad es de 24 horas, se cuentan los eventos que ocurren dentro de este período (incluso el día X+1).</li></ul> |
| Disponibilidad de eventos in-app | Disponible solo para los eventos que se produjeron durante el período de la ventana 1. |
| Desglose de descarga repetida de SKAN | Disponible. En el dashboard de SSOT, este desglose no está disponible y tanto las instalaciones como las descargas repetidas se incluyen en la métrica de instalaciones. |
| Cambios en la configuración de SKAN Conversion Studio | Cambiar la configuración de SKAN Conversion Studio puede provocar imprecisiones en los datos de SSOT durante aproximadamente 96 horas, ya que aún llegan postbacks de instalaciones codificadas con el esquema anterior. |
| Zona horaria | La zona horaria específica de la aplicación no está disponible. |
| Datos orgánicos | <ul><li>Disponibles para las métricas de 7 días posteriores a la instalación.</li></ul> |
| Datos sobre los días posteriores a la conversión (instalación, reatribución y reengagement) | Limitado a 7 días después de la conversión |
| Transparencia de agencia | Compatible |
| Cambios de nombre de la campaña | No se admiten. Utiliza el ID de campaña para agrupar y filtrar si se cambiaron los nombres de las campañas. |
| Redes publicitarias | <ul><li>Puedes acceder a los reportes de SSOT de Data Locker para ver los datos atribuidos a su fuente de medios si:<ul><li>El anunciante tiene SSOT activado en Conversion Studio.</li><li>La ad network está ejecutando campañas de SKAN.</li><li>La ad network tiene los [permisos](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions) necesarios del anunciante para acceder a los datos agregados.</li></ul></li></ul> |
| Acceso de agencias | No disponible. Los usuarios de agencias pueden ver los datos de SSOT en el dashboard SSOT. |
| Métricas D7 | <ul><li>Las métricas del D7 para el tráfico orgánico están disponibles a partir del 16 de febrero de 2025.</li><li>Es posible que falten o que sean inferiores a las métricas del D2 si:<ul><li>El intervalo de fechas incluye fechas en las que no han pasado 8 días.</li><li>Los datos modelados no están disponibles (p. ej., menos de 14 días de datos de ingresos). <Anchor target="_blank" href="/marketers/es/docs/skan-modeled-data#revenue-ltv">Saber más</Anchor></li><li>La configuración de SKAN Conversion Studio ha cambiado en los últimos 14 días.</li><li>Hay menos de 10 instalaciones para una fecha determinada.</li></ul></li></ul> |
| Nombres de eventos predefinidos | Dado que el nombre del evento 'af\_conversion' se usa para indicar diferentes tipos de conversiones, las aplicaciones que tienen un evento llamado específicamente 'af\_conversion' verán su evento original renombrado como 'af\_conversion\_event'. |
| Diferencia en moneda local | Como el dashboard de SSOT y el reporte de SSOT de Data Locker no se calculan simultáneamente, pueden producirse pequeñas discrepancias al comparar los ingresos en moneda local del dashboard con la moneda seleccionada en el reporte. Esto se debe a los tipos de cambio ligeramente diferentes utilizados en el momento en que se calcularon los datos. |
| Datos parciales del D7 de SKAN | A medida que se modelen los datos del D7 de SKAN y la versión inicial esté lista 7 días después de la instalación, al analizar las métricas del D7 durante los últimos 7 días, los datos D7 serán parciales. Para los registros en los que el método de atribución es SKAN, las métricas D7 serán más bajas que las métricas D2. |
| Granularidad limitada para las métricas de ingresos y eventos in-app del D7 | Las métricas de ingresos y eventos de usuario únicos durante los 7 días posteriores a la instalación no están disponibles en los niveles de granularidad de conjunto de anuncios, anuncio y tipo de conversión. Dado que este nivel de detalle no suele estar disponible en SKAN, el modelo no tiene en cuenta estas dimensiones. |
| Actualización de los datos de ingresos por publicidad | Los datos de ingresos por publicidad tienen un retraso de un día.<br /><br />Por ejemplo, un reporte creado en la mañana del 3 de julio incluirá los datos de ingresos por publicidad hasta el 1 de julio inclusive. |

</Accordion>

<div data-zendesk-anchors="h_01J455DHWAB1J9611A4KA40PZM=nota ssot-reports-in-data-locker=qu%C3%A9-es-data-locker h_01J454K90GWKME8F4JCDQKM3CK=qu%C3%A9-es-data-locker what-is-single-source-of-truth-ssot=qu%C3%A9-es-single-source-of-truth-ssot h_01J454K90GRCFR3PSAQRTX98B4=qu%C3%A9-es-single-source-of-truth-ssot benefits-of-ssot-reports-in-data-locker=ventajas-de-los-reportes-ssot-en-data-locker h_01J454PANH9J6ZZ069RS6FVWZM=ventajas-de-los-reportes-ssot-en-data-locker h_01J46C54ZB4YYTZ6CDHHC0EC8P=setting-up-data-locker h_01J455Q07J5XPYEBVP3BZ1FMVH=permissions h_01J29BTC9CESJF592P616WMK46=ssot-report-facts report-structure::673746b9=estructura-del-reporte h_01J29CQ5K4JBEP4X8YQ0V32WYR=estructura-del-reporte h_01J29CHBX2QNFTAQSA1W01PFH0=field-formats h_01J29BTC9CJ8GZDDCHK9NBZ4YX=dimensions h_01J29BTC9C86YMVEY17QQZNZCV=metrics h_01J29BTC9CH3DAA7ZRHG8C04MF=modeled-data h_01J29M72WAPH3KEW9N60JHTT3W=partial-data directory-structure=estructura-de-directorios h_01J29MB7B7Q3PJ9YWFQESWN0KD=estructura-de-directorios h_01J29MCSH4V41CPB7ZG41751QW=report-folder-hierarchy h_01J29MCSH40ATHNAJMY8KR7ANZ=directory-and-filename-structure bi-developer-considerations=consideraciones-para-desarrolladores-de-bi h_01J29MS6XV7XYTA9Q81454WEQN=consideraciones-para-desarrolladores-de-bi h_01J2F4HG8YHDGYFKHBBC5KSN2G=loading-reports h_01J2F4HG8YKNEVGEWTR91ADSDS=days-postattribution h_01J3YT1X908JVMDXKRQBCRD1JR=importante h_01J2F4HG8YAAE0E04Y6Q9Z62NZ=considerations h_01J3A82HZF14CCS027FE991M0T=example-use-cases h_01J3A883DQFQE0WTTY4FMX3AQ4=calculating-total-attributions-per-campaign h_01J3A883DQ82K71XY408M2BW0B=calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign h_01J3A883DQ5QAVH6AX7CGCBSWG=calculating-retargeting-conversions-per-geo h_01J3A883DQE25X31SPPF166BRH=calculating-installs-by-attribution-method-per-media-source h_01J3A883DQ8QVR8WKPPX1QF414=calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset h_01J3A883DQ51T3Z6H239P5JDJ1=calculating-cumulative-revenue-for-selected-postinstall-periods h_01J3A883DQXRCQ4NWY0BCX886E=calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source h_01J3A883DQRR62BWQ6JBTZ7238=calculating-inapp-event-conversion-rate-for-2-days-postinstalls h_01J3A883DRPEVDQCWKCT9M3EC1=calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id h_01J3A883DRRZ9Y8F3KNAAPZT2S=calculating-amount-of-duplicates-per-media-source-in-this-query h_01J29MV69M667QDHMS5WGYKPCZ=traits-and-limitations" />
