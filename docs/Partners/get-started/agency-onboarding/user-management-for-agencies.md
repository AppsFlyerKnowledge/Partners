---
title: Administración de usuarios para redes de publicidad
metadata:
  keywords:
    - Agencies
    - Partners
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Platform essentials
    - Agencies
  created_at: '2021-12-19T11:18:09Z'
  edited_at: '2026-08-12T12:29:44Z'
  id: 4414231896337
  locale: es
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/es/articles/4414231896337
---
> **En resumen:** Crea y administra los usuarios de AppsFlyer de tu cuenta de agencia y asígnales permisos para acceder a funciones y aplicaciones.

## Funciones de usuario y permisos de acceso

Las cuentas de AppsFlyer permiten múltiples usuarios, cada uno con permisos administrados de manera individual. Los permisos de cada usuario se definen a lo largo de 2 dimensiones principales:

* **Rol** (capacidad para acceder a funciones y realizar tareas)
* **Acceso a aplicaciones** para aplicaciones actuales y futuras

Los permisos dentro de cada una de estas dimensiones se asignan de forma independiente. En otras palabras, puedes asignar a un usuario un **rol** con amplias capacidades funcionales, pero permitirles ejercer esas capacidades solo dentro de un conjunto de **aplicaciones** muy definido.

La única excepción es la [función de administrador](/docs/user-management-for-agencies#administrador-un-rol-especial), como se explica a continuación, que tiene acceso a todas las funciones y aplicaciones.

### Roles predefinidos

#### hash de roles predefinidos

A cada usuario de AppsFlyer de una cuenta de agencia se le asigna una de las cuatro funciones predefinidas:

* Administrador
* Administrador de equipo
* marketing
* Contribuyente

Cada uno de estos roles define las características específicas de AppsFlyer a las que el usuario puede acceder y las funciones que puede realizar. Encontrarás una lista completa de las capacidades por rol en la [pestaña Roles](/docs/user-management-for-agencies#pestaña-roles) de la página **Administración de usuarios**.

Como regla general, todos los roles están predefinidos y las capacidades funcionales de cada rol están fijas: no se permite "mezclar y hacer coincidir". Sin embargo, puedes cambiar las capacidades funcionales de un usuario en cualquier momento cambiando su rol (excepto el [propietaria de la cuenta](/docs/user-management-for-agencies#hash-del-propietario-de-la-cuenta), como se explica a continuación).

> 📄 **Ejemplo**
>
> Has asignado a Bill Bates el rol de **Administrador del equipo.** Esta función le da a Bill la capacidad de administrar **la configuración de la aplicación**, pero no le permite acceder al **registro de auditoría.**
>
> **Pregunta:** ¿Puedo mantener a Bill en el puesto de administrador de equipo pero también darle la posibilidad de acceder al registro de auditoría? ¿Puedo quitarle la capacidad de gestionar la configuración de la aplicación?
>
> **Respuesta:** No. Mientras Bill permanezca en el puesto de administrador de equipo, no puedes darle la posibilidad de acceder al registro de auditoría. Tampoco puedes eliminar su capacidad para administrar la configuración de la aplicación. Por supuesto, puedes asignar un rol diferente a Bill, y sus capacidades cambiarán a las definidas por ese rol.

### Roles temporales: excepción a la regla

Si tu cuenta de AppsFlyer existía en nuestro sistema de gestión de usuarios anterior (cuando los únicos tipos de cuenta disponibles eran Administrador y Miembro del Equipo), todos los usuarios se incorporaron al nuevo sistema con sus capacidades sin cambios. Como resultado, la mayoría de estos usuarios aparecen en el sistema actual con **roles temporales**.

Aprende más sobre la [administración de roles temporales](/docs/user-management-for-agencies#managing-temp-roles).

### Administrador: un rol especial

Una cuenta de AppsFlyer puede tener **uno o más** administradores, pero todas las cuentas tienen al menos uno. Este rol especial tiene varias características únicas:

* El rol de administrador tiene acceso a **todas** las capacidades de la cuenta, incluidas las siguientes:
  * Todas las características y funciones
  * Todas las aplicaciones actuales y futuras
  * Todas las fuentes de medios y geolocalizacionesEsta característica de "acceso completo" del rol de administrador no se puede cambiar ni limitar.

  #### hash del propietario de la cuenta
* El usuario creado en el momento en que se abrió la cuenta (el **"propietario de la cuenta"**) tiene asignado el rol de Administrador de forma predeterminada.
  * El propietario de la cuenta no se puede eliminar, su rol de administrador no puede ser desactivado ni se puede editar de ninguna otra forma desde la página de [**Administración de usuarios.**](/docs/user-management-for-agencies#página-de-administración-de-usuarios) Asimismo, la dirección de correo electrónico del propietario de la cuenta no se puede cambiar.
    * Si necesitas cambiar el propietario de la cuenta, sigue los [pasos que se enumeran a continuación](/docs/user-management-for-agencies#changing-the-account-owner).
  * El propietario de la cuenta es inicialmente responsable de crear usuarios adicionales (hasta que se creen usuarios adicionales con capacidades de administración de usuarios).
* Solo un usuario con un rol de administrador puede <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">administrar los tokens de API y S2S.</Anchor>
* Cualquier administrador que no sea el propietario de la cuenta **puede** cambiarse a un rol diferente o eliminarse de la cuenta de AppsFlyer a través de la página de Administración de usuarios.

## Página de administración de usuarios

**Para acceder a la página de Administración de usuarios:**

1. En la barra de menús superior, haz clic en y abre el menú de la cuenta (menú desplegable de direcciones de correo electrónico).
2. Selecciona **Administración de usuarios.**

### Pestaña usuarios

La pestaña **Usuarios** muestra una tabla de todos los usuarios existentes en tu cuenta. Es el punto de partida para crear, administrar y eliminar usuarios.

* Haz clic en el encabezado de la columna **Usuario** para ordenar la tabla alfabéticamente (ascendente/descendente).
* Utiliza el cuadro de búsqueda para buscar y mostrar usuarios específicos.
* Haz clic en el icono de filtro <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> en el encabezado de la columna para filtrar los usuarios por su rol (incluidos los roles temporales).
  * Para borrar el filtro, selecciona **Ninguno** en la lista desplegable de filtros.
* Utiliza las casillas de verificación para seleccionar y [editar varios usuarios](/docs/user-management-for-agencies#edición-multiusuario) al mismo tiempo.

### Pestaña Roles

La pestaña **Roles** muestra una lista de todos los roles definidos en tu cuenta, incluidos:

* Los 4 [roles predefinidos](#roles-predefinidos)
* Cualquier [rol temporal](/docs/user-management-for-agencies#roles-temporales-excepción-a-la-regla) asignado actualmente a los usuarios

Haz clic en el nombre de cualquier rol en el panel izquierdo para ver:

* Detalles completos de las capacidades del rol
* El número de usuarios asignados actualmente a ese rol (en la esquina superior derecha de la pantalla)
  * Desplázate sobre el icono de usuario <Image alt="user_icon.png" src="https://files.readme.io/afd47a11e82e0cfac3240fe39582bd141639465952f6eef76bcf1f6e7532d6a9-16162513473937.png" width="21px" /> para ver una lista de los 20 primeros.

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

   > 🚧 **Importante:**
   >
   > La dirección de correo electrónico de un usuario es la que los identifica en la plataforma AppsFlyer, lo que significa:
   >
   > * No se puede cambiar más tarde sin eliminar y volver a crear el usuario.
   > * Debe ser una dirección de correo electrónico válida en la que el usuario pueda recibir el correo electrónico.
   > * No puede estar asociada con otro usuario en ninguna cuenta de AppsFlyer.
   >   * Si la dirección de correo electrónico ya está en uso (ya sea en tu cuenta o en otra), verás el mensaje *No se puede crear este usuario.* Sigue los [pasos para la resolución de problemas a continuación](/docs/user-management-for-agencies#troubleshooting-can-t-create-this-user) para resolver este problema.

4. Selecciona el departamento del usuario (opcional).
5. Selecciona el rol del usuario (obligatorio).
6. Selecciona las aplicaciones a las que puede acceder el usuario:
   * La configuración predeterminada permite el acceso a todas las aplicaciones actuales y futuras de la cuenta. Para cambiar esta configuración, usa las casillas de verificación para seleccionar y deseleccionar aplicaciones.
   * Un usuario puede tener acceso a todas las aplicaciones futuras solo si tiene acceso a todas las aplicaciones actuales.
7. Haz clic en **Guardar** para crear el usuario.

   * Se envía al usuario una invitación por correo electrónico para activar su cuenta.

   #### hash de activación de cuenta

   * El usuario se muestra en la tabla de usuarios. El icono del sobre ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png) indica que se ha enviado una invitación y que la cuenta está pendiente de activación. Una vez que el usuario active su cuenta, el sobre desaparecerá.
   * El enlace de activación enviado al usuario tiene una validez de 48 horas. Si el usuario no recibió la invitación o si el enlace ha expirado, puedes [volver a enviar la invitación](/docs/user-management-for-agencies#resending-a-user-invitation).

## Edición de usuarios

Los usuarios se pueden editar uno a la vez o en grupos.

### Edición individual

**Para editar un usuario individual:**

1. En la pestaña **Usuarios**, haz clic en el botón **Acciones** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> en el extremo derecho de la fila del usuario.
2. Selecciona **Editar** en el menú.
3. Edita la configuración del usuario según sea necesario.
4. Todos los ajustes que no sean la dirección de correo electrónico se pueden editar.
5. Haz clic en **Guardar**.

### Edición multiusuario

La edición multiusuario es una forma eficiente de cambiar los permisos de cuenta de varios usuarios a la vez. El uso de esta función en combinación con las capacidades de búsqueda y filtrado de la pestaña **Usuarios** puede resultar particularmente útil para administrar un gran número de usuarios.

> 📘 **Nota:**
>
> No puedes eliminar usuarios ni asignarlos al rol de administrador mediante la edición multiusuario.

**Para editar varios usuarios:**

1. En la pestaña **Usuarios**, selecciona las casillas de verificación del usuario o de los usuarios que deseas editar.
   * Selecciona la casilla de verificación en el encabezado de la columna para seleccionar todos los usuarios visibles.
   * El número de usuarios seleccionados actualmente se muestra en el lado derecho del cuadro de búsqueda. Ten en cuenta que el [propietario de la cuenta](/docs/user-management-for-agencies#hash-del-propietario-de-la-cuenta) no se puede seleccionar y no se incluye en la cantidad de usuarios seleccionados.
2. Los botones **Rol** y **Aplicaciones** se muestran en la parte superior derecha de la tabla.
   * Si uno o más de los usuarios seleccionados tienen acceso a aplicaciones futuras, el botón **Aplicaciones** no estará disponible. (Consulta [Limitaciones del rol temporal](/docs/user-management-for-agencies#limitaciones-de-los-roles-temporales) a continuación).
3. Haz clic en el botón de los permisos que deseas cambiar.
4. Realiza los cambios necesarios utilizando el cuadro de diálogo o las listas desplegables que se muestran.
   * ¡Recuerda que tus cambios se aplican a todos los usuarios seleccionados!
5. Los usuarios editados se resaltan en la tabla y los usuarios aparecen como aparecerán una vez que se guarden los cambios. Sin embargo, aún tienes la oportunidad de revisar tus cambios y confirmarlos o cancelarlos en el siguiente paso.
6. Revisa tus cambios. Haz clic en **Guardar** para confirmar o en **Cancelar** para deshacer la acción.

> 📄 **Ejemplo**
>
> **Escenario:**
>
> * Hay 10 usuarios en tu cuenta. Seis de ellos están en el rol de **Marketing**.
> * Alice, Bill y Charlie acaban de recibir ascensos y quieres cambiarlos del rol de **Marketing** al rol de **Administrador de equipo**.
> * Alice trabajará con la aplicación Astounding. Bill trabajará con la aplicación Beautiful. Charlie trabajará con la aplicación Charming.
>
> **Pasos:**
>
> 1. Utiliza el filtro de funciones <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> para ver solo los usuarios del rol de **Marketing**.
> 2. Cambia a Alice, Bill y Charlie al rol de **Administrador de equipo**:
>    * Selecciona las casillas de verificación de Alice, Bill y Charlie.
>    * Haz clic en el botón **Rol**.
>    * Selecciona **Administrador de equipo** en la lista desplegable.
>    * Haz clic en **Guardar** para confirmar.
>    * Ten en cuenta que una vez que confirmes los cambios, el filtro **Rol** se borrará y la tabla mostrará todos los usuarios.
> 3. Proporciona a Alice, Bill y Charlie el acceso adecuado a la aplicación:
>    * Utiliza el cuadro de búsqueda para encontrar a Alice y, a continuación, edita individualmente su usuario para darle acceso a la aplicación Astounding.
>    * Repite estos pasos para Bill y Charlie para darles acceso a Beautiful y Charming, respectivamente.

## Eliminar usuarios

**Para eliminar un usuario:**

1. En la pestaña **Usuarios**, haz clic en el botón <Image alt="" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" />**Acciones** altactions\_icon.pngalt en el extremo derecho de la fila del usuario.
2. Selecciona **Eliminar** en el menú.

## Situaciones especiales y procedimientos adicionales

<div id="managing-temp-roles" />

<Accordion title="Administrar roles temporales">

Si tu cuenta utilizaba anteriormente nuestro sistema de administración de usuarios anterior, se asignaban [**roles temporales**](/docs/user-management-for-agencies#roles-temporales-excepción-a-la-regla) a los usuarios existentes para garantizar que se incorporaran al nuevo sistema sin cambios en sus capacidades.

* A los usuarios con las mismas capacidades se les asignó el mismo rol temporal.
* Utiliza las características de la [pestaña Roles](/docs/user-management-for-agencies#pestaña-roles) para revisar las capacidades de cada rol temporal y una lista de usuarios que se encuentran actualmente en él.

#### Limitaciones de los roles temporales

Los roles temporales se diseñaron específicamente para permitir una transición fluida desde nuestro sistema de administración de usuarios anterior. Por lo tanto, solo están disponibles en situaciones limitadas:

* Los roles temporales no se pueden asignar a otros usuarios (ya sean nuevos o existentes).
* A un usuario con un rol temporal no se le puede asignar un rol temporal diferente (aunque puedes cambiar las aplicaciones a las que tiene acceso).
  * Ten en cuenta que el acceso de un usuario a aplicaciones futuras **no se** puede cambiar mientras el usuario tiene un rol temporal.
* Cuando un usuario con un rol temporal se cambia a un rol predefinido, no se puede devolver al rol temporal asignado anteriormente (o a cualquier otro rol temporal).
* Si el último usuario en un rol temporal se elimina, el rol ya no aparecerá en tu cuenta.

> 📄 **Ejemplo**
>
> Tu cuenta utilizó anteriormente nuestro sistema de administración de usuarios anterior. Diana y Edward eran usuarios existentes en el momento en que tu cuenta se movió al nuevo sistema. Diana ahora está en el rol temporal 1, y Edward está en el rol temporal 2.
>
> * Contratas a una nueva empleada, Fiona. Puedes asignar a Fiona cualquiera de los 4 [roles predefinidos](#roles-predefinidos). Sin embargo, no puedes asignar a Fiona el rol temporal 1 o el rol temporal 2.
> * Diana no se puede mover del rol temporal 1 al rol temporal 2. Sin embargo, puedes asignarle cualquiera de los 4 roles predefinidos. También puedes cambiar su acceso a la aplicación según sea necesario.
> * Si trasladas a Diana del rol temporal 1 al rol Administrador de equipo, no podrá volver más tarde al rol temporal 1.
> * Si Diana era el último usuario en el rol Temporal 1 cuando la moviste al rol de Administrador de equipo, el rol Temporal 1 ya no aparecerá en tu cuenta.

</Accordion>

<div id="changing-the-account-owner" />

<Accordion title="Cambiar el propietario de la cuenta">

Como todos los administradores tienen los mismos permisos que el propietario de la cuenta, no suele ser necesario cambiar el propietario de la cuenta. Pero si necesitas cambiar el propietario de la cuenta, sigue estos pasos para hacerlo.

> 🚧 **Importante:**
>
> Algunas cosas a considerar antes de comenzar:
>
> * Si sigues usando las API Pull, Master o GDPR con el token v1, cambiar el propietario de la cuenta restablece automáticamente estos servicios. Para evitar la pérdida de datos, <Anchor target="_blank" href="/marketers/es/docs/bulletin-api-token-changes">haz la transición para empezar a usar estas API con el token v2</Anchor> **antes de cambiar el propietario de la cuenta**.
> * El cambio del propietario de la cuenta debe completarse manualmente de acuerdo con estos pasos. No se puede hacer desde la página de **Administración de usuarios.**

#### #1 — Envía tu solicitud a través del widget de chat

Para comenzar el proceso de cambiar el propietario de la cuenta, abre el widget de chat <Anchor target="_blank" href="https://hq1.appsflyer.com/apps/search?openAssistant=true">usando este enlace</Anchor> o haciendo clic en el botón Ayuda en la barra de menú superior. Incluye la siguiente información en el chat:

* Nombre del propietario de la cuenta que quieres reemplazar
* Nombre, cargo y correo electrónico del nuevo propietario de la cuenta

#### #2 – Próximos pasos

Una vez que se haya procesado el cambio, recibirás una notificación por correo electrónico de AppsFlyer.

* Si deseas que el propietario anterior de la cuenta continúe usando tu cuenta de AppsFlyer, <Anchor target="_blank" href="/marketers/es/docs/user-management#creating-users">crea un nuevo usuario</Anchor> para él y asígnale un nuevo rol.
* Las API que usan el token v2 no se ven afectadas por cambiar el propietario de la cuenta. <Anchor target="_blank" href="/marketers/es/docs/managing-appsflyer-tokens">Aprender más sobre cómo administrar tokens</Anchor>.

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="Resolución del problema 'No se puede crear este usuario'">

Si recibes el mensaje de error *No se puede crear este usuario* al ingresar la dirección de correo electrónico de un nuevo usuario, generalmente significa que el correo electrónico ya está asociado con un usuario de AppsFlyer (ya sea en tu cuenta o en uno diferente). Sigue los pasos pertinentes a tu situación:

Si el usuario está en tu cuenta:

* Comprueba si el usuario ha activado su cuenta. De lo contrario, [vuelve a enviar la invitación](/docs/user-management-for-agencies#resending-a-user-invitation) si es necesario.
* Si el usuario ha activado su cuenta, pídele que intente iniciar sesión nuevamente con la dirección de correo electrónico asociada con su usuario. Indícale que siga los pasos de **¿Olvidaste tu contraseña?** si es necesario.

Si el correo electrónico del usuario se utiliza en una cuenta diferente o no puedes determinar la cuenta en la que se utiliza el correo electrónico del usuario, selecciona una de las siguientes opciones:

* Elimínalo de la otra cuenta y agrégalo a la tuya (es necesario que tengas los permisos requeridos en la otra cuenta); o
* Agrégalo a tu cuenta con otra dirección de correo electrónico. Debe ser una dirección de correo electrónico válida en la que pueda recibir un correo electrónico; o
* Comunícate con tu Customer Success Manager (CSM) o envía un correo electrónico a nuestro equipo de Engagement con el Cliente a [hello@appsflyer.com](mailto:hello@appsflyer.com).

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="Reenviar una invitación de usuario">

Si un nuevo usuario no recibió su [invitación de activación de cuenta](/docs/user-management-for-agencies#hash-de-activación-de-cuenta) o si no se activó dentro de las 48 horas, puedes volver a enviar el correo electrónico de la siguiente manera:

1. En la pestaña **Usuarios**, haz clic en el botón **Acciones** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> en el extremo derecho de la fila del usuario.
   * Ten en cuenta que el usuario todavía se muestra con un icono de sobre ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png), lo que indica que aún no ha activado su cuenta).
2. Selecciona **Reenviar invitación por correo electrónico** en el menú.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="Restablecer la autenticación de dos factores (2FA) de un usuario">

En el caso de las cuentas que utilizan una autenticación de dos factores, puede haber ocasiones en las que necesites restablecer la autenticación de dos factores de un usuario. Consulta <Anchor target="_blank" href="/marketers/es/docs/implementing-and-using-2fa-login#reset">aquí</Anchor> cómo hacerlo.

</Accordion>

<div data-zendesk-anchors="background=funciones-de-usuario-y-permisos-de-acceso h_01HC72J0H988V27YCTWPFGF7EP=funciones-de-usuario-y-permisos-de-acceso predefined-roles=roles-predefinidos h_01HC72J0H98447W34RD0ND2MC0=roles-predefinidos predefined-roles-hash=hash-de-roles-predefinidos h_01HC72J0H9RVA83J9F5QN4YS79=hash-de-roles-predefinidos h_01HC72J0H9Y54Q2Y6AGP6H1DG0=ejemplo temp-roles%E2%80%94an-exception-to-the-rule=roles-temporales-excepci%C3%B3n-a-la-regla h_01HC72J0H9NXMKJN64C73ZXZN1=roles-temporales-excepci%C3%B3n-a-la-regla admin%E2%80%94a-special-role=administrador-un-rol-especial h_01HC72J0HANGXV4GVJCQ5X2T84=administrador-un-rol-especial account-owner-hash=hash-del-propietario-de-la-cuenta h_01HC72J0HA5RFZE1G0KNKR30KV=hash-del-propietario-de-la-cuenta user-management-page=p%C3%A1gina-de-administraci%C3%B3n-de-usuarios h_01HC72J0HANQ3Z6FCWXA0TF3TN=p%C3%A1gina-de-administraci%C3%B3n-de-usuarios users-tab=pesta%C3%B1a-usuarios h_01HC72J0HAFBMYM792GXMCEY3T=pesta%C3%B1a-usuarios roles-tab=pesta%C3%B1a-roles h_01HC72J0HAXC2NAVQC4J2PMB0Z=pesta%C3%B1a-roles creating-a-user=crear-un-usuario h_01HC72J0HATN656W4B9DT82M60=crear-un-usuario h_01HC72J0HAP1GDH8JKGMT6XH67=importante account-activation-hash=hash-de-activaci%C3%B3n-de-cuenta h_01HC72J0HA3QJ2CH8TGEMJBY3A=hash-de-activaci%C3%B3n-de-cuenta editing-users=edici%C3%B3n-de-usuarios h_01HC72J0HAG2XF42NSYRZDEKVN=edici%C3%B3n-de-usuarios individual-editing=edici%C3%B3n-individual h_01HC72J0HAF739MQPF482T0WVA=edici%C3%B3n-individual multiuser-editing=edici%C3%B3n-multiusuario h_01HC72J0HA3BKXJCAVRQ5SJYYE=edici%C3%B3n-multiusuario h_01HC72J0HAZM2NBXN5ZHZET4BS=nota h_01HC72J0HAE70AMWSDP5BXGWK9=ejemplo-1 deleting-users=eliminar-usuarios h_01HC72J0HAQFD33VT0ARRWG0ZF=eliminar-usuarios special-situations-and-additional-procedures=situaciones-especiales-y-procedimientos-adicionales h_01HC72J0HAF5QFC5ZR7EHFMBM6=situaciones-especiales-y-procedimientos-adicionales h_01HC72J0HAD8JXPPFET4N2P3EK=managing-temp-roles temp-role-limitations=limitaciones-de-los-roles-temporales h_01HC72J0HA8PP79VV1F03E5AXV=limitaciones-de-los-roles-temporales h_01HC72J0HAJES0N195DZ797C4V=ejemplo-2 h_01HC72J0HAVXK83AK99NQVDT8T=changing-the-account-owner h_01HC72J0HANXBK4T1SD6V2KHE4=importante-1 1%E2%80%93send-an-email-request=1--env%C3%ADa-tu-solicitud-a-trav%C3%A9s-del-widget-de-chat h_01HC72J0HAJ3C8WJ767KG2307C=1--env%C3%ADa-tu-solicitud-a-trav%C3%A9s-del-widget-de-chat 2%E2%80%93next-steps=2--pr%C3%B3ximos-pasos h_01HC72J0HAM13NY9EKNKG8R1CA=2--pr%C3%B3ximos-pasos troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HC72J0HAWRBVWGVT12W6M711=troubleshooting-can-t-create-this-user h_01HC72J0HANPD39FRCWSPMRY5D=resending-a-user-invitation h_01HC72J0HARYRSXHKX41A41MPG=resetting-twofactor-authentication-2fa" />
