---
title: Sobre el modelado probabilístico
metadata:
  keywords:
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2025-10-21T14:32:11Z'
  edited_at: '2026-05-29T19:29:02Z'
  id: 40188089592209
  locale: es
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/es/articles/40188089592209
---
> **En resumen:** Aprende cómo configurar tus datos de interacción con anuncios para que AppsFlyer pueda aplicar modelado probabilístico cuando no haya señales determinísticas disponibles.

## Sobre el modelado probabilístico

AppsFlyer utiliza el modelado probabilístico como un método estadístico que preserva la privacidad para reportar el performance de las campañas de marketing de los desarrolladores de apps. Genera reportes agregados del performance de campañas a nivel de campaña para desarrolladores de apps.

**Características de implementación**

* Se basa en estadísticas y no en IDs únicos.
* Es un método alternativo que se utiliza cuando no hay disponibles un referer o identificadores publicitarios. Los métodos de atribución determinista, como los clics con referentes o coincidencia de ID, tienen prioridad si ocurren dentro de la ventana de lookback.

### ¿Cuándo se utiliza el modelado probabilístico?

Salvo que el cliente configure lo contrario, el modelado probabilístico se aplicará en los casos en que no haya datos determinísticos disponibles, incluidos:

* Conversiones web-to-app
* Experiencias entre dispositivos (por ejemplo, un anuncio de escritorio seguido de una instalación móvil)
* Entornos de CTV, PC o consola donde la atribución determinista no es posible

<div data-zendesk-anchors="about-probabilistic-modeling-attribution=sobre-el-modelado-probabil%C3%ADstico h_01K83JWQ84H0P1WABG939X55KD=sobre-el-modelado-probabil%C3%ADstico when-is-probabilistic-modeling-used=cu%C3%A1ndo-se-utiliza-el-modelado-probabil%C3%ADstico h_01K83JWQ8412VK2ZN39CQ5TJEZ=cu%C3%A1ndo-se-utiliza-el-modelado-probabil%C3%ADstico" />
