---
title: 'Primeros pasos: guía de incorporación para redes publicitarias'
metadata:
  keywords:
    - Ad Network
    - Advertisers
    - Ad Networks
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
  created_at: '2019-03-28T08:41:59Z'
  edited_at: '2026-08-12T12:29:14Z'
  id: 360001300998
  locale: es
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/es/articles/360001300998
---
> **De un vistazo:** Completa la integración con AppsFlyer configurando y probando tu enlace de atribución e integraciones de postback. Entiende los pasos, las cronologías y las dependencias del proceso.

<Image align="center" alt="Redes publicitarias_-_Incorporación__2_.png" src="https://files.readme.io/33217648d1f5c1ef327871b9b2ccfaadb6b9ae34fb2645ffcfbe187c378dd054-30603793569297.png" />

<div id="what-is-appsflyer" />

## ¿Qué es AppsFlyer?

AppsFlyer, líder en atribución móvil, te da la bienvenida como socio integrado de nuestra red publicitaria. Este artículo está dirigido a las redes publicitarias que han completado el registro de socios de AppsFlyer. Si deseas registrarte como socio, debes pedir a un <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#invita-a-nuevos-partners-a-appsflyer">cliente de AppsFlyer (anunciante) que te invite a hacerlo.</Anchor>

<div id="ad-network-onboarding" />

## Incorporación a la red publicitaria

Los pasos necesarios para la integración y el tiempo estimado para completarlos están listados en la sección **Pasos de incorporación** de este artículo.

La integración implica que:

* AppsFlyer registra tus interacciones (clics e impresiones). Las interacciones se atribuyen según el <Anchor target="_blank" href="/marketers/es/docs/appsflyer-attribution-model">modelo de atribución de AppsFlyer</Anchor>.
* Se envían postbacks en el formato que requieres a tus puntos finales.
* Puedes acceder a funciones de AppsFlyer como la firma de clics, Protect360, Data Locker, entre otros.

<div id="if-you-need-help" />

<Accordion title="Si necesitas ayuda">

* Consulta las <Anchor target="_blank" href="/partners/es/docs/integrated-partners-faq">preguntas frecuentes</Anchor> para socios
* Revisa el artículo <Anchor target="_blank" href="/partners/es/docs/integration-requests-for-partners">Solicitudes de cambio de integración</Anchor>

</Accordion>

Ten en cuenta:

* Las estimaciones de tiempo de este artículo se basan en nuestra experiencia con redes publicitarias. Cada integración es algo distinta, por lo que los tiempos reales pueden variar.
* AppsFlyer es compatible con muchas <Anchor target="_blank" href="/partners/es/docs/platforms-for-ad-networks">plataformas de rendimiento</Anchor>. Si usas una de las plataformas de la lista, debes revisar las instrucciones específicas antes de integrar.

<div id="onboarding-steps" />

## Pasos de incorporación

**Para integrarte con AppsFlyer**:

1. [Completa la parte 1: integración y pruebas.](/docs/getting-started-onboarding-guide-for-ad-networks#parte-1-integración-y-pruebas)
2. [Completa la parte 2: pruebas con aplicaciones de anunciantes.](/docs/getting-started-onboarding-guide-for-ad-networks#parte-2-prueba-usando-aplicaciones-de-anunciantes)
3. [Completa la parte 3: usa el panel de control y las herramientas de informes de AppsFlyer.](/docs/getting-started-onboarding-guide-for-ad-networks#parte-3-panel-de-appsflyer-y-opciones-de-informes)

<div id="part-1-integration-and-testing" />

### Parte 1: Integración y pruebas

<table><thead><tr><th>Acción</th><th>Minutos requeridos</th></tr></thead><tbody><tr><td>Espera el correo de aprobación de tu registro invitándote a completar los pasos de integración obligatorios.</td><td>--</td></tr><tr><td colspan="2"> <strong>Pasos de integración obligatorios</strong> </td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#enlace-de-atribución" target="_blank">Especifica tu enlace de atribución</a>: Los enlaces de atribución son URLs con macros. Usted completa estas macros con valores reales y las envía a AppsFlyer cada vez que un usuario hace clic en un enlace. <br/>¡Atención! <br/>¡Atención! Si utiliza una plataforma de red de rendimiento compatible con AppsFlyer, debe tener en cuenta las instrucciones específicas de esa plataforma. Consulte las <a href="./platforms-for-ad-networks" target="_blank">guías de redes de rendimiento</a>. </td><td>60</td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#postback-predeterminado" target="_blank">Especificar macros de postback</a>: Los postbacks son URLs que contienen macros completadas por AppsFlyer y se envían a sus servidores en tiempo real después de cada conversión.</td><td>60</td></tr><tr><td>Inicie sesión en el <a href="https://hq1.appsflyer.com/auth/login" target="_blank">panel de control de AppsFlyer</a> utilizando las credenciales proporcionadas. </td><td> </td></tr><tr><td><p>Suba el logotipo de su empresa. Su logotipo debe tener el formato 200 X 50 PNG transparente. </p><ol><li>En AppsFlyer, en la barra de menú, seleccione su dirección de correo electrónico &gt; <strong>Configuración del socio</strong>. </li><li>En la pestaña <strong>Perfil</strong>, cargue el logotipo de su empresa. </li><li>Haga clic en <strong>Guardar</strong>.</li></ol></td><td>5</td></tr><tr><td><p>Pruebe la integración utilizando las aplicaciones de prueba de AppsFlyer:</p><ul><li><a href="./android-integration-testing-for-ad-networks" target="_blank">Android</a></li><li><a href="./ios-integration-testing-for-ad-networks" target="_blank">apps de iOS,</a></li></ul></td><td>10</td></tr><tr><td colspan="2"><strong>Pasos de integración opcionales</strong></td></tr><tr><td>[iOS] Si sus anunciantes requieren la Privacidad Avanzada Agregada de AppsFlyer, complete la integración de <a href="./self-serve-integration-management-for-ad-networks#postbacks-de-privacidad-avanzada-y-skan" target="_blank">Privacidad Avanzada</a>.</td><td>60</td></tr><tr><td>[iOS] Si ejecuta campañas de SKAdNetwork, complete la <a href="./self-serve-integration-management-for-ad-networks#postbacks-de-privacidad-avanzada-y-skan" target="_blank">integración de SKAdNetwork</a>. </td><td>60</td></tr><tr><td><h4><strong><span id="authorized-agencies"></span>Agencias autorizadas</strong></h4><p>Cree y gestione una lista de agencias que usted aprueba para ejecutar campañas a través de su integración de red. Esto se hace ingresando su ID de agencia (af_prt) en la sección <a href="./set-up-your-list-of-authorized-agencies" target="_blank"><strong>Agencias autorizadas</strong></a>  del Centro de Seguridad. Para obtener el ID de agencia, la agencia debe contactarle y proporcionárselo.</p></td><td>2</td></tr><tr><td colspan="2"><p><strong>Características opcionales y consideraciones</strong><br/> </p><p>Considere implementar integraciones y opciones según los requisitos de los anunciantes.</p></td></tr><tr><td>Para asegurarse de que no se envíen clics fraudulentos utilizando su identificador de socio, implemente la <a href="./click-signing-for-ad-networks" target="_blank">firma de clics</a>. </td><td>60+</td></tr><tr><td>Para los anunciantes que implementan Protect360 o reglas de validación, añada <a href="./postback-macros-for-ad-networks#macros-instalaciones-eventos-in-app-y-eventos-rechazados" target="_blank">postbacks de atribución rechazados</a>.</td><td>15</td></tr><tr><td>Envía el coste a AppsFlyer mediante API. Consulte <a href="./incost-api-for-ad-networks" target="_blank">API InCost</a>.</td><td>60+</td></tr><tr><td> <a href="/marketers/es/docs/retargeting-attribution-guide" target="_blank">Integración de retargeting</a>.</td><td>15</td></tr><tr><td> <a href="/marketers/es/docs/measure-view-through-engagements" target="_blank">Integración de atribución por visualización</a>.</td><td>15</td></tr></tbody></table>

<div id="part-2-test-using-advertiser-apps" />

### Parte 2: Prueba usando aplicaciones de anunciantes

En esta parte, probará su integración utilizando una aplicación que pertenece a un anunciante. Por lo tanto, es necesario que contactes al anunciante y le pidas que complete algunos de los pasos de esta sección. En esta sección, las menciones a anunciantes también pueden referirse a agencias si actúan en nombre de un anunciante.

| Realizado por | Acción | Minutos requeridos |
| --- | --- | --- |
| AppsFlyer | Activa <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#integration-tab">activar socio.</Anchor><br /><br />Cuando está activado, AppsFlyer considera tus interacciones como posibles candidatas para la atribución. | 2 |
| Anunciantes | Concede <Anchor target="_blank" href="/marketers/es/docs/set-up-an-integrated-partner#permisos-de-ad-network">permisos de red publicitaria*</Anchor> y añade a los miembros de tu equipo.<br /><br />Cuando está activado, los datos de rendimiento de la aplicación se muestran en el panel de control de AppsFlyer. Solo los miembros del equipo listados pueden acceder a los datos. | 2 |
| Red publicitaria | <Anchor target="_blank" href="/marketers/es/docs/user-management#creating-users">Añade miembros del equipo a tu cuenta</Anchor>. | 2 |
| Anunciante (administrador) | <Anchor target="_blank" href="/marketers/es/docs/registering-test-devices">Registra tus dispositivos de prueba</Anchor>. Pídele al anunciante que lo haga en tu nombre. | 3 |
| Redes publicitarias | <Anchor target="_blank" href="/partners/es/docs/test-marketer-campaign-integration-with-the-ad-network">Prueba la integración utilizando las aplicaciones de los anunciantes.</Anchor> | 60 |

<div id="part-3-appsflyer-dashboard-and-reporting-options" />

### Parte 3: Panel de AppsFlyer y opciones de informes

| Opción |
| --- |
| <Anchor target="_blank" href="/partners/es/docs/integrated-partners-dashboard">Usa el panel de socios</Anchor>. |
| Obtén datos de rendimiento agregados mediante almacenamiento en la nube con <Anchor target="_blank" href="/partners/es/docs/data-locker-for-partners">Data Locker</Anchor> para redes publicitarias. |
| Obtén datos en bruto de Protect360<Anchor target="_blank" href="/marketers/es/docs/raw-data-export-page">.</Anchor> |

<div id="integration-validation-period" />

## Periodo de validación de integración

Para asegurar la integridad del ecosistema AppsFlyer y proteger los sistemas internos de tráfico inválido, todas las nuevas integraciones de redes publicitarias pasan por un periodo de validación. Durante este periodo, AppsFlyer verifica minuciosamente el tráfico y evalúa su calidad antes de hacer la integración disponible para otros anunciantes en el <Anchor target="_blank" href="/marketers/es/docs/partner-integrations">Marketplace</Anchor>. Las integraciones de redes publicitarias que no cumplan con los altos estándares de calidad de tráfico tras la validación pueden enfrentar la cancelación de la cuenta.

<div id="validation-periodfaq" />

### Periodo de validación - FAQ

| **Pregunta** | **Respuesta** |
| --- | --- |
| <span id="why-cant-advertisers-find-me-on-the-marketplace"></span>¿Por qué los anunciantes no pueden encontrarme en el Marketplace incluso después de haber completado la integración? | Durante el periodo de validación, tu integración solo será visible para el anunciante que te refirió. Una vez que hayamos validado la calidad de tu tráfico, recibirás un correo electrónico informándote de que tu integración está disponible para todos los anunciantes. |
| <span id="what-should-i-do-to-make-the-integration-available-for-all-advertiers"></span>¿Qué puedo hacer para asegurar que mi integración sea aprobada? | Entregue un volumen significativo de tráfico de alta calidad al anunciante que le refirió. |
| <span id="when-should-i-expect-to-receive-the-validation-completion-email"></span>¿Cuándo debo esperar recibir el correo electrónico confirmando la finalización de la validación? | Después de que hayamos validado suficiente tráfico, recibirás un correo electrónico informándote de que el período de validación ha terminado. |
| <span id="can-i-know-the-current-status-of-the-validation-period"></span>¿Puedo conocer el estado actual de mi evaluación de validación? | Solo lo sabrás cuando finalice el período de validación, tras recibir una notificación por correo electrónico. |
| <span id="what-are-the-validation-criteria-based-on"></span>¿En qué se basan los criterios de validación? | Los criterios de validación se basan en algoritmos dinámicos de aprendizaje automático de <Anchor target="_blank" href="/marketers/es/docs/protect360-anti-fraud-guide">Protect360</Anchor>. Se consideran factores como la calidad del tráfico, el volumen y la validez general de los datos, combinados con las mejores prácticas del sector. |
| <span id="another-adviertiser-wants-to-work-with-me"></span>¿Qué ocurre si otro anunciante quiere comenzar a trabajar conmigo durante mi período de validación? | Durante el período de validación, tu integración solo será visible para el anunciante que te refirió. Otros anunciantes podrán trabajar contigo una vez que tu período de validación haya finalizado con éxito. |
| <span id="my-integration-fails"></span>¿Qué ocurre si mi integración no supera la validación? | El período de validación puede extenderse para monitorear mejoras en la calidad del tráfico, o tu integración puede eliminarse permanentemente de la plataforma AppsFlyer. Serás notificado en cualquiera de los casos. |

<div data-zendesk-anchors="what-is-appsflyer=qu%C3%A9-es-appsflyer h_01J09255QNBFRV8DYZPGG990A0=qu%C3%A9-es-appsflyer ad-network-onboarding=incorporaci%C3%B3n-a-la-red-publicitaria h_01J09255QN61VPW292PC2CH9KN=incorporaci%C3%B3n-a-la-red-publicitaria h_01J09255QNGD66T140ERW4WP8Z=if-you-need-help onboarding-steps=pasos-de-incorporaci%C3%B3n h_01J09255QNZ9QXXFB54YRYCM8P=pasos-de-incorporaci%C3%B3n part-1-integration-and-testing=parte-1-integraci%C3%B3n-y-pruebas h_01J09255QN35ZBKE2R2HDDZWSZ=parte-1-integraci%C3%B3n-y-pruebas h_01J0JS136CTYEF6F29H8R1NV29=authorized-agencies part-2-test-using-advertiser-apps=parte-2-prueba-usando-aplicaciones-de-anunciantes h_01J09255QP11XJD3C83VZZXXQZ=parte-2-prueba-usando-aplicaciones-de-anunciantes part-3-appsflyer-dashboard-and-reporting-options=parte-3-panel-de-appsflyer-y-opciones-de-informes h_01J09255QPSSD8CF0HR059RWXZ=parte-3-panel-de-appsflyer-y-opciones-de-informes integration-validation-period=periodo-de-validaci%C3%B3n-de-integraci%C3%B3n h_01J09255QP82ZYZDJMA74SRYGZ=periodo-de-validaci%C3%B3n-de-integraci%C3%B3n validation-period%E2%80%94faq=periodo-de-validaci%C3%B3n---faq h_01J09255QP77BME57P9B7S222V=periodo-de-validaci%C3%B3n---faq" />
