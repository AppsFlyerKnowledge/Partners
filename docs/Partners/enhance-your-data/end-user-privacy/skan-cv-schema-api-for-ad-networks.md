---
title: API de esquema de CV de SKAN para redes de publicidad
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2023-03-07T23:22:16Z'
  id: 11705009866001
  locale: es
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/es/articles/11705009866001
---
> **De un vistazo**: Consulta el esquema de CV de SKAN asignado por el anunciante.

## API de esquema de CV de SKAN para redes de publicidad

Con la atribución de SKAdNetwork (SKAN), los anunciantes califican la calidad del usuario estableciendo valores de conversión (CV) basados en la actividad del usuario post-instalación durante períodos de tiempo específicos (ventanas). <Anchor target="_blank" href="/marketers/es/docs/skadnetwork-skan-solution-guide">Aprender más sobre SKAN</Anchor>

iOS reporta el CV vía postbacks enviados a la red de publicidad que coloca el anuncio. Los anunciantes de iOS 15 también pueden indicar a iOS que envíe los postbacks directamente a AppsFlyer.

Esta API proporciona a las redes de publicidad la asignación de CV a valores y eventos de atribución. Las redes de publicidad la utilizan para decodificar los postbacks que reciben.

La API lo devuelve como un JSON anidado. El esquema para cada aplicación es independiente. Las asignaciones por CV están contenidas dentro de la matriz conversion\_value\_mapping.

Para usar la API, pídele a tu desarrollador que siga su <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">API de esquema de CV de SKAN para las instrucciones para las redes de publicidad</Anchor>. Para obtener una lista de claves y su descripción, haz clic en 200 en el simulador.

**Nota**:

* El rango de valores de CV es:
  * Valor preciso de la ventana 1 de SKAN 4: 0-63.
  * Valor aproximado de las ventanas 1, 2 y 3 de SKAN 4: bajo, medio o alto.
  * SKAN 3 e inferiores: 0-63
* Los anunciantes pueden cambiar la asignación de CV en cualquier momento.
* Tú, la red de publicidad, debes consultar esta API diariamente, para asegurarte de tener el esquema más actualizado.

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=api-de-esquema-de-cv-de-skan-para-redes-de-publicidad" />
