---
title: Preguntas frecuentes sobre conexiones de audiencias para ad networks
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Audience Segmentation
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-neama-benhabib
    - Marketers
    - Audience Segmentation
    - Ad Networks
  created_at: '2023-11-27T08:25:39Z'
  edited_at: '2026-08-12T12:29:51Z'
  id: 20459388348305
  locale: es
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/es/articles/20459388348305
---
> **De un vistazo:** ¿Eres una ad network? Encuentra respuestas a las preguntas frecuentes sobre las conexiones con partners de audiencias.

<div id="api-key-and-partner-pull-key" />

## Clave de API y clave de extracción de Partners

<div id="what-are-the-api-key-and-testing-api-key-used-for" />

<Accordion title="¿Para qué se usan la clave de API y la clave de API de prueba?">

La **clave de API** es una clave única que el partner emite a cada anunciante. La clave de API identifica al anunciante en cada llamada a la API y normalmente es una cadena hexadecimal larga (por ejemplo, d41ac239b3b918e28fa0c). Durante el proceso de prueba, necesitaremos que nos proporciones una **clave de API de prueba**, que usaremos para probar tu integración de audiencias.

</Accordion>

<div id="what-is-the-partner_pull_key" />

<Accordion title="¿Qué es PARTNER_PULL_KEY ?">

`PARTNER_PULL_KEY` es una clave generada por AppsFlyer y proporcionada a cada partner. Luego, el partner la usa en la variable de plantilla ubicada en la URL `{{PARTNER_PULL_KEY}}` para descargar el archivo de segmento.

</Accordion>

<div id="how-and-when-does-the-partner-get-the-partner_pull_key" />

<Accordion title="¿Cómo y cuándo recibimos el PARTNER_PULL_KEY?">

El equipo de audiencias de AppsFlyer te enviará una `PARTNER_PULL_KEY` cuando probemos tu endpoint `/sync` en una fase posterior.

</Accordion>

<div id="audience-file-size-and-limitations" />

## Archivo de audiencia, tamaño y limitaciones

<div id="is-there-a-limitation-on-segment-size" />

<Accordion title="¿Hay alguna limitación en el tamaño del segmento?">

Subimos los datos a AWS S3 mediante una carga multiparte. Para conocer los límites de AWS, consulta: supports:https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html

</Accordion>

<div id="how-large-are-the-files" />

<Accordion title="¿Qué tamaño tienen los archivos?">

Admitimos archivos de gran tamaño. Al final, son archivos CSV almacenados en AWS S3. Para conocer los límites de AWS, consulta: supports:https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html

</Accordion>

<div id="is-there-an-upper-limit-for-device-id-rows" />

<Accordion title="¿Hay un límite máximo para las filas de ID de dispositivo?">

El número máximo de filas depende del límite de tamaño de archivo de 5 TB de AWS.

</Accordion>

<div id="can-we-use-a-direct-amazon-aws-pathbucket-for-the-audience-api" />

<Accordion title="¿Podemos usar una ruta o bucket directo de Amazon AWS para la API de audiencias?">

Sí, te proporcionaremos un bucket de AWS y te enviaremos una URL prefirmada a una ruta de AWS donde se encuentra el archivo.

</Accordion>

<div id="is-the-file-compressed" />

<Accordion title="¿Está comprimido el archivo?">

N.º

</Accordion>

<div id="does-the-audience-have-a-default-validity-period" />

<Accordion title="¿La audiencia tiene un período de validez predeterminado?">

Una audiencia no caduca. Una vez que se crea y se conecta una audiencia, se carga todos los días. Sin embargo, una audiencia puede eliminarse; en ese caso, dejará de cargarse.

</Accordion>

<div id="is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id" />

<Accordion title="¿El formato del archivo está separado por saltos de línea (o por comas)? ¿La primera línea es un encabezado como advertiser_id ?">

Está separado por saltos de línea, y la primera línea es un encabezado como `advertiser_id_sha256` (según el identificador que se cargue).

</Accordion>

<div id="will-each-sync-request-have-urls-to-all-3-files-adid-email-and-phone" />

<Accordion title="¿Cada solicitud /sync incluirá las URL de los 3 archivos (por ejemplo, ADID, correo electrónico y teléfono)?">

Cada solicitud `/sync` contendrá las URL de los archivos que admite la integración. Si admites ADID, correo electrónico y teléfono, contendrá esas 3 URL.

</Accordion>

<div id="as-a-result-of-step-3-sync-we-get-a-link-to-download-an-audience-file-is-it-possible-to-generate-and-share-such-url-templates-without-an-api-synchronization" />

<Accordion title="Como resultado del paso 3 ( /sync ), obtenemos un enlace para descargar un archivo de audiencia. ¿Es posible generar y compartir esas plantillas de URL sin una sincronización de API?">

Por el momento, no. Las URL se generan en función de tu `PARTNER_PULL_KEY` único. En la fase de prueba, se proporcionarán las URL y podrán probarse.

Aquí tienes un ejemplo de URL:

`https://audiencespull.appsflyer.com/{{PARTNER_PULL_KEY}}/12cjv4dq1zyxz3nh-HASHED.csv?X-Amz-A` lgorithm=AWS1-HMAC-SHA256&X-Amz-Date=20190503T091923Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=AKIB22QYTATEGB2HBFJR%2F20190603%2Feu-west-1%2Fs3%2Faws4\_request&X-Amz-Signature=c8287819a21d2f7832154df609c55ab8c0afe53540d542918b2739a9234923a

</Accordion>

<div id="what-do-we-need-container_id-for" />

<Accordion title="¿Para qué necesitamos container_id ?">

Enviaremos los ID de dispositivo de la audiencia al ID del contenedor que especifiques a través de la API. La creación del contenedor de audiencia es obligatoria para el desarrollo de la integración de audiencias.

</Accordion>

<div id="api-calls-responses-and-status-codes" />

## Llamadas a la API, respuestas y códigos de estado

<div id="when-should-the-partner-return-a-response" />

<Accordion title="¿Cuándo debemos devolver una respuesta?">

`/validate`: cuando la clave de API coincida con la que se te proporcionó.

`/create`: cuando el contenedor se haya creado por tu parte.

`/sync`: Esperamos recibir una respuesta después de que recibas nuestra llamada y puedas acceder al archivo de sincronización. Puedes descargar y procesar el archivo después de enviar la respuesta. El enlace está disponible para su descarga durante un plazo de 2 horas.

</Accordion>

<div id="how-should-partners-handle-failed-requests" />

<Accordion title="¿Cómo debemos gestionar las solicitudes fallidas?">

Mediante códigos de estado:

200: cuando la solicitud se ha realizado correctamente

401: para una clave de API no válida: autenticación

No admitimos otros casos de forma predeterminada. En estos casos, el anunciante verá que una carga ha fallado debido a un error general. Si hay problemas recurrentes, ponte en contacto con nosotros para analizar estos casos.

</Accordion>

<div id="when-are-these-endpoints-being-called-by-appsflyer" />

<Accordion title="¿Cuándo llama AppsFlyer a nuestros endpoints?">

`/validate`: AppsFlyer llamará a este endpoint una sola vez cuando un anunciante cree una nueva conexión contigo.

`/create`: Se llama a este endpoint solo una vez por contenedor, lo que significa que, para cada audiencia nueva que se conecte contigo por primera vez, llamamos al endpoint `/create` y almacenamos el ID del contenedor. Esperamos recibir un ID de contenedor diferente para cada llamada a `/create`. Separamos las plataformas y los nombres de las audiencias de nuestro lado (en otras palabras, cada plataforma tendrá su propia audiencia de nuestro lado e iniciará una llamada a `/create`).

`/sync`: Se llama a este endpoint cada vez que se inicia una carga, ya sea durante el proceso diario que realiza una carga programada de todas las audiencias de AppsFlyer o cuando un anunciante inicia una carga manual a través de nuestra IU o de una llamada a la API.

</Accordion>

<div id="are-sync-requests-made-only-once-or-will-appsflyer-rerun-the-requests-later" />

<Accordion title="¿Las solicitudes a /sync se realizan solo una vez o AppsFlyer volverá a ejecutarlas más adelante?">

La solicitud a `/sync` se realiza cada vez que se inicia una carga. Esto ocurre durante el proceso diario que realiza una carga programada de todas las audiencias de AppsFlyer o cuando un anunciante inicia una carga manual a través de nuestra IU o de una llamada a la API.

</Accordion>

<div id="how-often-does-appsflyer-send-out-calls-to-the-sync-endpoint" />

<Accordion title="¿Con qué frecuencia envía AppsFlyer llamadas al endpoint /sync ?">

Depende del número de anunciantes con los que trabajes y del número de audiencias que carguen. Por cada audiencia cargada, se llamará al endpoint `/sync`. Esto ocurre durante el proceso diario que realiza una carga programada de todas las audiencias de AppsFlyer o cuando un anunciante inicia una carga manual a través de nuestra IU o de una llamada a la API.

</Accordion>

<div id="if-it-has-high-traffic-can-partners-have-a-different-api-than-the-other-two-ie-routes-or-even-domain" />

<Accordion title="Si tenemos mucho tráfico, ¿podemos mantener varios endpoints de API (por ejemplo, varias rutas o incluso varios dominios)?">

La solución recomendada es asegurarte de que la API actual pueda gestionar un tráfico relativamente alto. Hay disponible una modificación de la API; sin embargo, esto podría provocar retrasos de semanas o meses en la finalización de la integración.

</Accordion>

<div id="naming-rules" />

## Reglas de nomenclatura

<div id="in-the-validate-interface-is-the-api_key-field-a-string-or-string-array" />

<Accordion title="En la interfaz /validate , ¿el campo api_key es una cadena o una matriz de cadenas?">

Es una cadena.

</Accordion>

<div id="in-the-create-interface-does-the-name-field-audience-name-only-need-to-support-pure-english-or-does-it-need-to-support-other-character-sets-what-are-the-validation-rules-for-names" />

<Accordion title="En la interfaz /create , ¿el campo name (nombre de la audiencia) debe admitir solo caracteres ingleses o también otros conjuntos de caracteres? ¿Cuáles son las reglas de validación para los nombres?">

El nombre de la audiencia es idéntico al nombre de la interfaz de usuario de AppsFlyer.

* Debe ser un nombre único de entre 2 y 100 caracteres
* Se admiten todos los idiomas
* Se admiten símbolos especiales (p. ej., $, %, ^, @, etc.)

</Accordion>

<div id="in-the-create-interface-must-container_id-be-pure-numbers-or-can-it-support-english" />

<Accordion title="En la interfaz /create , ¿ container_id debe contener solo números o también puede admitir caracteres ingleses?">

Se admiten tanto números como caracteres ingleses.

</Accordion>

<div id="sha256-and-hashed-url" />

## SHA256 y URL con Hashing

<div id="we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded" />

<Accordion title="¿Por qué falló nuestro intento de descodificar el GAID/IDFA SHA256 de las audiencias?">

SHA256 no está pensado para descodificarse. Este mecanismo está diseñado para que tú y AppsFlyer codifiquéis el ID del dispositivo (lo que te permite hacer coincidir los valores codificados si tienes acceso al ID de dispositivo original).

</Accordion>

<div id="does-appsflyer-provide-nonhashed-identifiers" />

<Accordion title="¿AppsFlyer nos proporciona identificadores sin hash?">

No, los ID de dispositivo sin hash solo están disponibles para los anunciantes. Para garantizar la Privacidad de Datos, aplicamos Hashing a los ID de anunciante en los archivos de segmentos mediante el algoritmo SHA256. Los ID de anunciante se enviarán con esta clave en la carga útil de la solicitud: `url_adid_sha256`.

</Accordion>

<div id="if-all-gaids-are-hashed-how-can-the-partner-know-which-gaid-they-received" />

<Accordion title="Si todos los GAID tienen hash, ¿cómo podemos saber qué GAID hemos recibido?">

Si tienes un GAID en texto sin formato de la aplicación y un GAID con hash de AppsFlyer, puedes aplicar SHA256 al GAID en texto sin formato y luego hacerlo coincidir con el GAID con hash de AppsFlyer.

</Accordion>

<div data-zendesk-anchors="api-key-and-partner_pull_key=clave-de-api-y-clave-de-extracci%C3%B3n-de-partners h_01HG7Y7M665JKBJEQK5Z48KYWT=clave-de-api-y-clave-de-extracci%C3%B3n-de-partners h_01HG7YC3NBYN46DXCGJRBZKQ8N=what-are-the-api-key-and-testing-api-key-used-for h_01HG7YC3NB8KW79307GPATW5AH=what-is-the-partner_pull_key h_01HG7YC3NB71TV7EBKX7JH2DVB=how-and-when-does-the-partner-get-the-partner_pull_key audience-file-size-and-limitations=archivo-de-audiencia-tama%C3%B1o-y-limitaciones h_01HG7Z1DS1P6VDHEGDM2DMENYK=archivo-de-audiencia-tama%C3%B1o-y-limitaciones h_01HG7Z5PQFMJQXRF9EQ89RZRF8=is-there-a-limitation-on-segment-size h_01HG7Z5PQFBQGT9STXQ4XVEWEM=how-large-are-the-files h_01HG7Z5PQFN91RC6GDWAGDJS9V=is-there-an-upper-limit-for-device-id-rows h_01HG7Z5PQFPBJPFKD0T38AM7SK=can-we-use-a-direct-amazon-aws-pathbucket-for-the-audience-api h_01HG7Z5PQFZB6F3H917JHH8QR4=is-the-file-compressed h_01HG7Z5PQFVFA8GXVD7HND7AV1=does-the-audience-have-a-default-validity-period is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like-%E2%80%98advertiser_id%E2%80%99=is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id h_01HG7Z5PQF349SS37F3X5ESNBH=is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id h_01HG7Z5PQFQAN19PD09GQMSF06=will-each-sync-request-have-urls-to-all-3-files-adid-email-and-phone h_01HGTJD9HQ4ZSZ1GQ9PH4NP6B5=as-a-result-of-step-3-sync-we-get-a-link-to-download-an-audience-file-is-it-possible-to-generate-and-share-such-url-templates-without-an-api-synchronization h_01HG7Z5PQFV6RZJ9PMBETRCM3G=what-do-we-need-container_id-for api-calls-responses-and-status-codes=llamadas-a-la-api-respuestas-y-c%C3%B3digos-de-estado h_01HG7ZMJ4FS76K8HF7PP4PJGY3=llamadas-a-la-api-respuestas-y-c%C3%B3digos-de-estado h_01HG7ZQCBXRKMRYTC8PB2YDTQ1=when-should-the-partner-return-a-response h_01HG7ZQCBXRHF78ZSBP4RZ8JE3=how-should-partners-handle-failed-requests h_01HG7ZQCBXXPZZ4V7361H43WVX=when-are-these-endpoints-being-called-by-appsflyer h_01HG7ZQCBX5GGP0KFGKZG8N27R=are-sync-requests-made-only-once-or-will-appsflyer-rerun-the-requests-later h_01HG7ZQCBXEFAYE0KJN4DTTVBG=how-often-does-appsflyer-send-out-calls-to-the-sync-endpoint h_01HG7ZQCBXC765AFJSPTE2CC6Z=if-it-has-high-traffic-can-partners-have-a-different-api-than-the-other-two-ie-routes-or-even-domain naming-rules=reglas-de-nomenclatura h_01HG800JBTMXQS4GPEFCK64D7H=reglas-de-nomenclatura h_01HG80352MXGGZ6KVG0REGN12Q=in-the-validate-interface-is-the-api_key-field-a-string-or-string-array h_01HG80352MYBAWEQQJT4GSR36G=in-the-create-interface-does-the-name-field-audience-name-only-need-to-support-pure-english-or-does-it-need-to-support-other-character-sets-what-are-the-validation-rules-for-names h_01HG80352MYFPQF3SZ05J58VCB=in-the-create-interface-must-container_id-be-pure-numbers-or-can-it-support-english sha256-and-hashed-url=sha256-y-url-con-hashing h_01HG814F103B5M3Q2K5110WDEM=sha256-y-url-con-hashing we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can%E2%80%99t-sha256-be-decoded=we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded h_01HG816BDJPN86WVFE5RM09KZ8=we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded h_01HG816BDJN9WJZTDG0TG930G9=does-appsflyer-provide-nonhashed-identifiers h_01HG816BDJ7A6GMZC14RKERQB1=if-all-gaids-are-hashed-how-can-the-partner-know-which-gaid-they-received" />
