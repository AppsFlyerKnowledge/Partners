---
title: Implementando y usando el inicio de sesión 2FA
metadata:
  keywords:
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
  created_at: '2025-12-04T09:21:41Z'
  edited_at: '2026-08-12T12:29:16Z'
  id: 41585422141585
  locale: es
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/es/articles/41585422141585
---
> **En resumen:** La autenticación de dos factores (2FA) se utiliza para añadir una capa adicional de seguridad al proceso de inicio de sesión. Las credenciales de login de los usuarios de la cuenta se complementan con Google o Microsoft Authenticator.

## Introducción

> 📘 **Advertencia**
>
> Cada persona que acceda a AppsFlyer debe tener su propia cuenta de usuario. Las credenciales de usuario no se pueden compartir y la 2FA debe configurarse individualmente para cada usuario. Si necesitas añadir usuarios a la cuenta, ve a Administración de usuarios y crea nuevos usuarios según sea necesario. Para obtener más información, consulta <Anchor target="_blank" href="/partners/es/docs/user-management-for-agencies">Administración de usuarios.</Anchor>

* AppsFlyer exige el uso de 2FA.
* La 2FA debe configurarse con **Google o Microsoft Authenticator.**

> 🚧 **Dos puntos (:)**
>
> Después de configurar la 2FA, no elimines tu app de autenticación. Si lo haces, se interrumpirá la conexión con AppsFlyer y no podrás iniciar sesión.

<div id="firsttime-setup" />

<Accordion title="Configuración inicial">

#### **Nuevo usuario de cuenta**

1. Sigue las instrucciones del correo electrónico y crea una contraseña.
2. Inicia sesión en **AppsFlyer,** y serás redireccionado a la página de configuración de 2FA.
3. Configura 2FA.
   * Descarga **Google Authenticator** y una aplicación de **QR code**.
   * Escanea el QR code.
   * Ingresa el código de verificación emitido por **Google Authenticator**.
   * Haz clic en **Verificar**, y serás redireccionado a la página de **Mis aplicaciones**.

#### **Usuarios de cuentas existentes**

1. Inicia sesión en **AppsFlyer** (nombre de usuario y contraseña), y serás redireccionado a la página de configuración de 2FA.
2. Configura 2FA.
   * Descarga **Google Authenticator** y una aplicación de **QR code**.
   * Escanea el QR code.
   * Ingresa el código de verificación emitido por **Google Authenticator**.
   * Haz clic en **Verificar**, y serás redireccionado a la página de **Mis aplicaciones**.

</Accordion>

<div id="ongoing-use" />

<Accordion title="Uso continuo">

**Sigue estos pasos para el uso continuo.**

1. Inicia sesión en **AppsFlyer** (nombre de usuario y contraseña), y serás redireccionado a la página de inicio de sesión de 2FA.
2. Abre **Google Authenticator** en tu móvil para obtener el código de verificación.
3. Ingresa el código en la página de 2FA.
4. Haz clic en **Verificar**, y serás redireccionado a la página de **Mis aplicaciones**.

</Accordion>

<div id="reset-a-users-2fa" />

<Accordion title="Restablecer la 2FA de un usuario">

<Embed title="Implementando y usando el inicio de sesión 2FA" typeOfEmbed="youtube" url="https://www.youtube.com/embed/15sYaqz89ys" providerUrl="https://www.youtube.com" />

Para restablecer tu 2FA, ponte en contacto con tu administrador. El administrador debe seguir estos pasos:

Nota: Si eres el propietario de una cuenta, puedes restablecer tu propia 2FA en [los pasos que aparecen a continuación](/docs/implementing-and-using-2fa-login-partners#para-que-el-propietario-de-una-cuenta-restablezca-su-propia-2fa).

#### **Para que un administrador restablezca la 2FA de un usuario**

1. En la barra de menú, haz clic en el menú desplegable de la dirección de correo electrónico.
2. Selecciona **Administración de usuarios**.
3. En la pestaña **Usuarios** , haz clic en las opciones del menú en el extremo derecho de la fila del usuario.
4. Selecciona **Restablecer 2FA** en el menú.

#### **Para que el propietario de una cuenta restablezca su propia 2FA**

1. En la página de login de 2FA, haz clic en **Click here to start the reset process.**
2. Se enviará un correo electrónico con un código y un enlace a la nueva página de login de 2FA.
3. Copia el código del correo electrónico y haz clic en el enlace del correo electrónico.
4. Ingresa el código en la página de configuración de 2FA.
5. Sigue los pasos para configurar tu nueva 2FA [aquí](/docs/implementing-and-using-2fa-login-partners#usuarios-de-cuentas-existentes).

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Especificaciones y limitaciones">

| Nombre | Nota |
| --- | --- |
| Apps de AppsFlyer | Con la 2FA activada, no se pueden usar ambas apps de AppsFlyer, **My Device ID by AppsFlyer** y **AppsFlyer**. Para registrar dispositivos de prueba, usa el método que se describe <Anchor target="_blank" href="/marketers/es/docs/registering-test-devices">aquí</Anchor>. |

</Accordion>

<div data-zendesk-anchors="highlights=introducci%C3%B3n h_01HEHRKE8PY64KWVSSFR6T4F1Z=introducci%C3%B3n h_01KBVXP9J12428VNPQAG7N2B52=advertencia h_01KBVXHY4VHJG6CJWHFTVK4644=dos-puntos- h_01HEHRKE8QQTX3Y9ZY1HZ6GBAG=firsttime-setup new-account-user=nuevo-usuario-de-cuenta h_01KBMCFPDWRBF5NPKWF3JSHBS4=nuevo-usuario-de-cuenta existing-account-users=usuarios-de-cuentas-existentes h_01KBMCFSS5ACAB5T6SAJ2ETNGC=usuarios-de-cuentas-existentes h_01HEHRKE8QHWHCMNB5M7S5YVYJ=ongoing-use h_01KBMBVZX1N60YJKTJRAN66DY7=reset-a-users-2fa for-an-admin-resetting-a-users-2fa=para-que-un-administrador-restablezca-la-2fa-de-un-usuario h_01KBMCSYNWA41JAP498F19JQKZ=para-que-un-administrador-restablezca-la-2fa-de-un-usuario for-an-account-owner-resetting-their-own-2fa=para-que-el-propietario-de-una-cuenta-restablezca-su-propia-2fa h_01KBMCVPFMZAC6Z05SNW3CEHQ4=para-que-el-propietario-de-una-cuenta-restablezca-su-propia-2fa h_01KBVY16MN92WV0TC81QBWCNW4=traits-and-limitations" />
