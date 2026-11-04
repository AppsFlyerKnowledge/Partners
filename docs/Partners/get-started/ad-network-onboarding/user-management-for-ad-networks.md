---
title: Administración de usuarios para redes de publicidad
metadata:
  keywords:
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
  created_at: '2021-12-19T11:16:28Z'
  edited_at: '2026-08-12T12:29:30Z'
  id: 4414238502289
  locale: es
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/es/articles/4414238502289
---
> **En resumen:** Crea y administra los usuarios de AppsFlyer de tu cuenta de red de publicidad y asígnales un rol que defina a qué funciones pueden acceder.

<div id="background" />

## Antecedentes

Las cuentas de red de publicidad de AppsFlyer admiten varios usuarios, cada uno con un rol que define su acceso a las características y funciones.

El rol de **administrador** tiene acceso a todas las capacidades. El rol de **marketing** tiene acceso a un conjunto de funciones más limitado. Encontrarás una lista completa de las capacidades por rol en la [pestaña Roles](/docs/user-management-for-ad-networks#pestaña-roles) de la página **Administración de usuarios**.

<div id="more-about-roles" />

## Aprende más sobre roles

Como regla general, todos los roles están predefinidos y las capacidades funcionales de cada rol están fijas: no se permite "mezclar y hacer coincidir". Sin embargo, puedes cambiar las capacidades funcionales de un usuario en cualquier momento cambiando su rol (excepto el [propietaria de la cuenta](/docs/user-management-for-ad-networks#administrador-un-rol-especial), como se explica a continuación).

<div id="example" />

> 📄 **Ejemplo**
>
> Has asignado a Bill Bates la función de **marketing**. Este rol le da a Bill la capacidad de administrar las **Reglas de validación** pero no le permite acceder a **Registro de auditoría.**
>
> **Pregunta:** ¿Puedo mantener a Bill en el rol de marketing pero también darle la posibilidad de acceder al registro de auditoría? ¿Puedo quitarle la capacidad de administrar las reglas de validación?
>
> **Respuesta:** No. Mientras Bill permanezca en el rol de marketing, no puedes darle la posibilidad de acceder al registro de auditoría. Tampoco puedes eliminar su capacidad para administrar las reglas de validación. Por supuesto, puedes asignar un rol diferente a Bill, y sus capacidades cambiarán a las definidas por ese rol.

<div id="temp-rolesan-exception-to-the-rule" />

### Roles temporales: excepción a la regla

Si tu cuenta de AppsFlyer existía en nuestro sistema de gestión de usuarios anterior (cuando los únicos tipos de cuenta disponibles eran Administrador y Miembro del Equipo), todos los usuarios se incorporaron al nuevo sistema con sus capacidades sin cambios. Como resultado, la mayoría de estos usuarios aparecen en el sistema actual con **roles temporales**.

Aprende más sobre la [administración de roles temporales](/docs/user-management-for-ad-networks#managing-temp-roles).

<div id="admina-special-role" />

### Administrador: un rol especial

Una cuenta de AppsFlyer puede tener **uno o más** administradores, pero todas las cuentas tienen al menos uno. Este rol especial tiene varias características únicas:

* El rol de administrador tiene acceso a **todas** las capacidades de la cuenta, incluidas las siguientes:

  * Todas las características y funciones
  * Todas las aplicaciones actuales y futuras
  * Todas las fuentes de medios y geolocalizaciones

  Esta característica de "acceso completo" del rol de administrador no se puede cambiar ni limitar.
* <span id="account-owner"></span>Propietario de la cuenta Al usuario creado en el momento en que se abrió la cuenta se le asigna la función de administrador de forma predeterminada.
  * El propietario de la cuenta no se puede eliminar, su rol de administrador no puede ser desactivado ni se puede editar de ninguna otra forma desde la página de [Administración de usuarios.](/docs/user-management-for-ad-networks#página-de-administración-de-usuarios) Asimismo, la dirección de correo electrónico del propietario de la cuenta no se puede cambiar.
    * Si necesitas cambiar el propietario de la cuenta, sigue los [pasos que se enumeran a continuación](/docs/user-management-for-ad-networks#changing-the-account-owner).
  * El propietario de la cuenta es inicialmente responsable de crear usuarios adicionales (hasta que se creen usuarios adicionales con capacidades de administración de usuarios).
* Los administradores pueden <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">gestionar los tokens de API y S2S</Anchor>.
* Cualquier administrador que no sea el propietario de la cuenta **puede** cambiarse a un rol diferente o eliminarse de la cuenta de AppsFlyer a través de la página de Administración de usuarios.

<div id="user-management-page" />

## Página de administración de usuarios

**Para acceder a la página de Administración de usuarios:**

1. En la barra de menú superior, haz clic en el menú desplegable de direcciones de correo electrónico.
2. Selecciona **Administración de usuarios.**

<div id="users-tab" />

### Pestaña usuarios

La pestaña **Usuarios** muestra una tabla de todos los usuarios existentes en tu cuenta. Es el punto de partida para crear, administrar y eliminar usuarios.

* Haz clic en el encabezado de la columna **Usuario** para ordenar la tabla alfabéticamente (ascendente/descendente).
* Utiliza el cuadro de búsqueda para buscar y mostrar usuarios específicos.
* Haz clic en el icono de filtro <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> en el encabezado de la columna para filtrar los usuarios por su rol (incluidos los roles temporales).
  * Para borrar el filtro, selecciona **Ninguno** en la lista desplegable de filtros.
* Utiliza las casillas de verificación para seleccionar y [editar varios usuarios](/docs/user-management-for-ad-networks#edición-multiusuario) al mismo tiempo.

<div id="roles-tab" />

### Pestaña Roles

La pestaña **Roles** muestra una lista de todos los roles definidos en tu cuenta, incluidos:

* Los 2 [roles predefinidos](/docs/user-management-for-ad-networks#aprende-más-sobre-roles) de administración y marketing
* Cualquier [rol temporal](/docs/user-management-for-ad-networks#roles-temporales-excepción-a-la-regla) asignado actualmente a los usuarios

Haz clic en el nombre de cualquier rol en el panel izquierdo para ver:

* Detalles completos de las capacidades del rol
* El número de usuarios asignados actualmente a ese rol (en la esquina superior derecha de la pantalla)
  * Desplázate sobre el icono de usuario <Image alt="user_icon.png" src="https://files.readme.io/afd47a11e82e0cfac3240fe39582bd141639465952f6eef76bcf1f6e7532d6a9-16162513473937.png" width="21px" /> para ver una lista de los 20 primeros.

<div id="creating-a-user" />

## Crear un usuario

**Para crear un nuevo usuario:**

1. En la pestaña **Usuarios**, haz clic en el botón **Nuevo usuario**.
2. Ingresa el nombre del usuario (obligatorio):
   * Puedes incluir letras, números, espacios, puntos (.), guiones (-), guiones bajos (\_) y comillas simples (') o dobles (").
   * No se permiten otros caracteres especiales.
3. Introduce la dirección de correo electrónico del usuario (obligatorio):

   * Puedes incluir letras, números, apóstrofes ('),ampersands (&), signos de dólar ($), símbolos hash (#), guiones (-), guiones bajos (\_) y puntos (.)
   * No se permiten dos puntos consecutivos (..) ni otros caracteres especiales.
   * Debe terminar con un dominio de correo electrónico válido.

   <div id="important" />

   > 🚧 **¡Importante!**
   >
   > La dirección de correo electrónico de un usuario es la que los identifica en la plataforma AppsFlyer, lo que significa:
   >
   > * No se puede cambiar más tarde sin eliminar y volver a crear el usuario.
   > * Debe ser una dirección de correo electrónico válida en la que el usuario pueda recibir el correo electrónico.
   > * No puede estar asociada con otro usuario en ninguna cuenta de AppsFlyer.
   >   * Si la dirección de correo electrónico ya está en uso (ya sea en tu cuenta o en otra), verás el mensaje *No se puede crear este usuario.* Sigue los [pasos para la resolución de problemas a continuación](/docs/user-management-for-ad-networks#troubleshooting-can-t-create-this-user) para resolver este problema.

4. Selecciona el departamento del usuario (opcional).
5. Selecciona el rol del usuario (obligatorio).
6. Selecciona las aplicaciones a las que puede acceder el usuario:
   1. La configuración predeterminada permite el acceso a todas las aplicaciones actuales y futuras de la cuenta. Para cambiar esta configuración, usa las casillas de verificación para seleccionar y deseleccionar aplicaciones.
   2. Un usuario puede tener acceso a todas las aplicaciones futuras solo si tiene acceso a todas las aplicaciones actuales.
7. Haz clic en **Guardar** para crear el usuario.
8. **Del lado del usuario:** Para convertirse en un usuario activo (miembro del equipo), el usuario debe [activar su cuenta](#convertirse-en-un-usuario-activo) desde la invitación por correo electrónico que recibió.

<div id="becoming-an-active-user" />

#### Convertirse en un usuario activo

Tras hacer clic en **Guardar** para finalizar el procedimiento de [creación de un usuario](/docs/user-management-for-ad-networks#crear-un-usuario) (arriba), el usuario recibe una invitación por correo electrónico para activar su cuenta. El enlace de activación es válido por 48 horas. Si el usuario no recibió la invitación o si el enlace ha expirado, puedes [volver a enviar la invitación](/docs/user-management-for-ad-networks#resending-a-user-invitation).

Puedes ver al nuevo usuario en la página de administración de usuarios, con el icono de sobre ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png) junto a su nombre. Esto indica que se ha enviado una invitación y que la cuenta está pendiente de activación. Después de que el usuario activa su cuenta, el sobre desaparece.

<div id="editing-users" />

## Edición de usuarios

Los usuarios se pueden editar uno a la vez o en grupos.

<div id="individual-editing" />

### Edición individual

**Para editar un usuario individual:**

1. En la pestaña **Usuarios**, haz clic en el botón **Acciones** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> en el extremo derecho de la fila del usuario.
2. Selecciona **Editar** en el menú.
3. Edita la configuración del usuario según sea necesario.
   * Todos los ajustes que no sean la dirección de correo electrónico se pueden editar.
4. Haz clic en **Guardar**.

<div id="multi-user-editing" />

### Edición multiusuario

La edición multiusuario es una forma eficaz de cambiar el rol de varios usuarios a la vez. El uso de esta función en combinación con las capacidades de búsqueda y filtrado de la pestaña **Usuarios** puede resultar particularmente útil para administrar un gran número de usuarios.

<div id="note" />

> 📘 **Nota:**
>
> No puedes eliminar usuarios ni asignarlos al rol de administrador mediante la edición multiusuario.

**Para editar varios usuarios:**

1. En la pestaña **Usuarios**, selecciona las casillas de verificación del usuario o de los usuarios que deseas editar.
   * Selecciona la casilla de verificación en el encabezado de la columna para seleccionar todos los usuarios visibles.
   * El número de usuarios seleccionados actualmente se muestra en el lado derecho del cuadro de búsqueda. Ten en cuenta que el [propietario de la cuenta](/docs/user-management-for-ad-networks#administrador-un-rol-especial) no se puede seleccionar y no se incluye en la cantidad de usuarios seleccionados.
2. Haz clic en el botón **Rol** que aparece en la parte superior derecha de la tabla.
3. Realiza los cambios necesarios. ¡Recuerda que tus cambios se aplican a todos los usuarios seleccionados!
4. Los usuarios editados se resaltan en la tabla y los usuarios aparecen como aparecerán una vez que se guarden los cambios. Sin embargo, aún tienes la oportunidad de revisar tus cambios y confirmarlos o cancelarlos en el siguiente paso.
5. Revisa tus cambios. Haz clic en **Guardar** para confirmar o en **Cancelar** para deshacer la acción.

<div id="deleting-users" />

## Eliminar usuarios

**Para eliminar un usuario:**

1. En la pestaña **Usuarios**, haz clic en el botón <Image alt="" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" />**Acciones** altactions\_icon.pngalt en el extremo derecho de la fila del usuario.
2. Selecciona **Eliminar** en el menú.

<div id="special-situations-and-additional-procedures" />

## Situaciones especiales y procedimientos adicionales

<div id="managing-temp-roles" />

<Accordion title="Administrar roles temporales">

Si tu cuenta utilizaba anteriormente nuestro sistema de administración de usuarios anterior, se asignaban [roles temporales](/docs/user-management-for-ad-networks#roles-temporales-excepción-a-la-regla) a los usuarios existentes para garantizar que se incorporaran al nuevo sistema sin cambios en sus capacidades.

* A los usuarios con las mismas capacidades se les asignó el mismo rol temporal.
* Utiliza las características de la [pestaña Roles](/docs/user-management-for-ad-networks#pestaña-roles) para revisar las capacidades de cada rol temporal y una lista de usuarios que se encuentran actualmente en él.

<div id="temp-role-limitations" />

#### Limitaciones de los roles temporales

Los roles temporales se diseñaron específicamente para permitir una transición fluida desde nuestro sistema de administración de usuarios anterior. Por lo tanto, solo están disponibles en situaciones limitadas:

* Los roles temporales no se pueden asignar a otros usuarios (ya sean nuevos o existentes).
* A un usuario con un rol temporal no se le puede asignar un rol temporal diferente.
* Cuando un usuario con un rol temporal se cambia a un rol predefinido, no se puede devolver al rol temporal asignado anteriormente (o a cualquier otro rol temporal).
* Si el último usuario en un rol temporal se elimina, el rol ya no aparecerá en tu cuenta.

<div id="example-1" />

> 📄 **Ejemplo**
>
> Tu cuenta utilizó anteriormente nuestro sistema de administración de usuarios anterior. Diana y Edward eran usuarios existentes en el momento en que tu cuenta se movió al nuevo sistema. Diana ahora está en el rol temporal 1, y Edward está en el rol temporal 2.
>
> * Contratas a una nueva empleada, Fiona. Puedes asignar a Fiona la función de administrador o de marketing. Sin embargo, no puedes asignar a Fiona el rol temporal 1 o el rol temporal 2.
> * Diana no se puede mover del rol temporal 1 al rol temporal 2. Sin embargo, puedes asignarle la función de administradora o de marketing.
> * Si trasladas a Diana del rol temporal 1 al rol marketing, no podrá volver más tarde al rol temporal 1.
> * Si Diana era el último usuario en el rol Temporal 1 cuando la moviste al rol de marketing, el rol Temporal 1 ya no aparecerá en tu cuenta.

<div id="changing-the-account-owner" />

<Accordion title="Cambiar el propietario de la cuenta">

Como todos los administradores tienen los mismos permisos que el propietario de la cuenta, no suele ser necesario cambiar el propietario de la cuenta. Pero si necesitas cambiar el propietario de la cuenta, sigue estos pasos para hacerlo.

<div id="important-1" />

> 🚧 **¡Importante!**
>
> Algunas cosas a considerar antes de comenzar:
>
> El cambio del propietario de la cuenta debe completarse manualmente de acuerdo con estos pasos. No se puede hacer desde la página de **Administración de usuarios.**

<div id="1send-your-request-via-the-chat-widget" />

#### #1 — Envía tu solicitud a través del widget de chat

Para comenzar el proceso de cambiar el propietario de la cuenta, abre el widget de chat <Anchor target="_blank" href="https://hq1.appsflyer.com/apps/search?openAssistant=true">usando este enlace</Anchor> o haciendo clic en el botón Ayuda en la parte superior derecha de la barra de menús. Incluye la siguiente información en el chat:

* Nombre del propietario de la cuenta que quieres reemplazar
* Nombre, cargo y correo electrónico del nuevo propietario de la cuenta

<div id="2next-steps" />

#### #2 – Próximos pasos

Una vez que se haya procesado el cambio, recibirás una notificación por correo electrónico de AppsFlyer.

* Si deseas que el propietario anterior de la cuenta continúe usando tu cuenta de AppsFlyer, <Anchor target="_blank" href="/marketers/es/docs/user-management#creating-users">crea un nuevo usuario</Anchor> para él y asígnale un nuevo rol.
* Las API que usan el token v2 no se ven afectadas por cambiar el propietario de la cuenta.  Aprender más sobre cómo administrar tokens<Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">.</Anchor>

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="Resolución del problema 'No se puede crear este usuario'">

Si recibes el mensaje de error *No se puede crear este usuario* al ingresar la dirección de correo electrónico de un nuevo usuario, generalmente significa que el correo electrónico ya está asociado con un usuario de AppsFlyer (ya sea en tu cuenta o en uno diferente). Sigue los pasos pertinentes a tu situación:

Si el usuario está en tu cuenta:

* Comprueba si el usuario ha activado su cuenta. De lo contrario, [vuelve a enviar la invitación](/docs/user-management-for-ad-networks#resending-a-user-invitation) si es necesario.
* Si el usuario ha activado su cuenta, pídele que intente iniciar sesión nuevamente con la dirección de correo electrónico asociada con su usuario. Indícale que siga los pasos de **¿Olvidaste tu contraseña?** si es necesario.

Si el correo electrónico del usuario se utiliza en una cuenta diferente o no puedes determinar la cuenta en la que se utiliza el correo electrónico del usuario, selecciona una de las siguientes opciones:

* Elimínalo de la otra cuenta y agrégalo a la tuya (es necesario que tengas los permisos requeridos en la otra cuenta); o
* Agrégalo a tu cuenta con otra dirección de correo electrónico. Debe ser una dirección de correo electrónico válida en la que pueda recibir un correo electrónico; o
* Contacta con el soporte de AppsFlyer para Partners a través del <Anchor target="_blank" href="/partners/es/docs/using-the-partner-assistant-chatbot">chatbot del asistente para Partners</Anchor>.

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="Reenviar una invitación de usuario">

Si un nuevo usuario no recibió su [invitación de activación de cuenta](/docs/user-management-for-ad-networks#convertirse-en-un-usuario-activo) o si no se activó dentro de las 48 horas, puedes volver a enviar el correo electrónico de la siguiente manera:

1. En la pestaña **Usuarios**, haz clic en el botón <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> en el extremo derecho de la fila del usuario.
   * Ten en cuenta que el usuario todavía se muestra con un icono de sobre ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png), lo que indica que aún no ha activado su cuenta).
2. Selecciona **Reenviar invitación por correo electrónico** en el menú.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="Restablecer la autenticación de dos factores (2FA)">

Si tu cuenta usa 2FA, puede haber ocasiones en las que necesites restablecer la configuración 2FA de un usuario. Hazlo de la siguiente manera:

1. En la pestaña **Usuarios**, haz clic en el botón <Image alt="" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" />**Acciones** altactions\_icon.pngalt en el extremo derecho de la fila del usuario.
2. Selecciona **Restablecer 2FA** en el menú.

**Nota:** Un administrador puede restablecer la 2FA de cualquier otro administrador que no sea la suya o la del [propietario de la cuenta](/docs/user-management-for-ad-networks#administrador-un-rol-especial). Para restablecer la autenticación de dos factores del propietario de la cuenta, comunícate con el equipo de soporte de AppsFlyer.

</Accordion>

</Accordion>

<div data-zendesk-anchors="background=antecedentes h_01HEN51924E23493MKXPEKHS03=antecedentes more-about-roles=aprende-m%C3%A1s-sobre-roles h_01HEN51924R007XNM3N45CA73A=aprende-m%C3%A1s-sobre-roles h_01HEN51924WBY63ASRGH7ZQFP4=ejemplo temp-roles%E2%80%94an-exception-to-the-rule=roles-temporales-excepci%C3%B3n-a-la-regla h_01HEN51924DT5GVPMJBQD3ZY9R=roles-temporales-excepci%C3%B3n-a-la-regla admin%E2%80%94a-special-role=administrador-un-rol-especial h_01HEN51924G6GXVH8HH5DAWZ26=administrador-un-rol-especial user-management-page=p%C3%A1gina-de-administraci%C3%B3n-de-usuarios h_01HEN51924PQEM4R974HMWPH98=p%C3%A1gina-de-administraci%C3%B3n-de-usuarios users-tab=pesta%C3%B1a-usuarios h_01HEN51924RDZFSJN0KN0YJFND=pesta%C3%B1a-usuarios roles-tab=pesta%C3%B1a-roles h_01HEN519249AHVKGM5CDTXPEP7=pesta%C3%B1a-roles creating-a-user=crear-un-usuario h_01HEN51924C56PAKQYTQM05DMV=crear-un-usuario h_01HEN519241VD35W7AYQ08NMHJ=importante becoming-an-active-user=convertirse-en-un-usuario-activo h_01HEN51924F0G8287RP08EB464=convertirse-en-un-usuario-activo editing-users=edici%C3%B3n-de-usuarios 01HEPXYXV78HEXK5SD4QBDGEGH=edici%C3%B3n-de-usuarios individual-editing=edici%C3%B3n-individual h_01HEN51924AP4TT97C2X5CRB35=edici%C3%B3n-individual multiuser-editing=edici%C3%B3n-multiusuario h_01HEN519246HC2M4BB35GR29SQ=edici%C3%B3n-multiusuario h_01HEN51925ZWQ8V3XJNAD4F4V9=nota deleting-users=eliminar-usuarios h_01HEN51925Q9P2GFJWWWW9MMQ2=eliminar-usuarios special-situations-and-additional-procedures=situaciones-especiales-y-procedimientos-adicionales h_01HEN51925JBC3R887CVFNFA27=situaciones-especiales-y-procedimientos-adicionales h_01HEN519258745RNY4RNT4MWK6=managing-temp-roles temp-role-limitations=limitaciones-de-los-roles-temporales h_01HEN51925REZEKBA501T0RMME=limitaciones-de-los-roles-temporales h_01HEN51925FMKJ5D7BE93GVN2G=ejemplo-1 h_01HEN51925J3NKAJSKYEF9AMMJ=changing-the-account-owner h_01HEN51925FR6AGT1M2YHJJB6A=importante-1 1%E2%80%93send-an-email-request=1--env%C3%ADa-tu-solicitud-a-trav%C3%A9s-del-widget-de-chat h_01HEN51925GQGFAZYRTHPBBXA2=1--env%C3%ADa-tu-solicitud-a-trav%C3%A9s-del-widget-de-chat 2%E2%80%93next-steps=2--pr%C3%B3ximos-pasos h_01HEN51925SPRA034581N8BWYK=2--pr%C3%B3ximos-pasos troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HEN51925YAY0E37S799S7S1J=troubleshooting-can-t-create-this-user h_01HEN519253VMNBPNW61M10QZW=resending-a-user-invitation h_01HEN51925C7X1AEM2FJ6152Z1=resetting-twofactor-authentication-2fa" />
