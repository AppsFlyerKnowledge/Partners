---
title: Como implementar a autenticação de dois fatores
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
  edited_at: '2026-08-18T00:39:59Z'
  id: 41585422141585
  locale: pt
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/pt/articles/41585422141585
---
> **Em resumo:** a autenticação de dois fatores (2FA) é usada para adicionar uma camada extra de segurança ao processo de login. As credenciais de login dos usuários da conta são complementadas pelo Google Authenticator ou pelo Microsoft Authenticator.

## Introdução

> 📘 **Atenção**
>
> Cada pessoa que acessa a AppsFlyer deve ter sua própria conta de usuário. As credenciais de usuário não podem ser compartilhadas, e a 2FA deve ser configurada individualmente para cada usuário. Se você precisar adicionar usuários à conta, acesse Gerenciamento de usuários e crie novos usuários conforme necessário. Para mais detalhes, consulte <Anchor target="_blank" href="/partners/pt/docs/user-management-for-agencies">Gerenciamento de usuários.</Anchor>

* A 2FA é obrigatória para a AppsFlyer.
* A 2FA deve ser configurada usando **Google ou Microsoft Authenticator.**

> 🚧 **Importante!**
>
> Depois de configurar a 2FA, não exclua seu aplicativo autenticador. Isso interrompe a conexão com a AppsFlyer, e você não poderá fazer login.

<div id="firsttime-setup" />

<Accordion title="Configuração inicial">

#### **Novo usuário da conta**

1. Siga as instruções do e-mail e crie uma senha.
2. Faça login na **AppsFlyer**. Em seguida, você será redirecionado para a página de configuração da autenticação de dois fatores.
3. Configure o método desejado.
   * Baixe o **Google Authenticator** e um aplicativo de leitura de **QR codes**.
   * Escaneie o QR code.
   * Digite o código de verificação emitido pelo **Google Authenticator**.
   * Clique em **verificar**, e você será redirecionado para a página **meus aplicativos**.

#### **Usuários existentes**

1. Faça login na **AppsFlyer** (nome de usuário e senha). Em seguida, você será redirecionado para a página de configuração da autenticação de dois fatores.
2. Configure o método desejado.
   * Baixe o **Google Authenticator** e um aplicativo de leitura de **QR codes**.
   * Escaneie o QR code.
   * Digite o código de verificação emitido pelo **Google Authenticator**.
   * Clique em **verificar**. Em seguida, você será redirecionado para a página **meus aplicativos**.

</Accordion>

<div id="ongoing-use" />

<Accordion title="Uso contínuo">

**Siga as etapas abaixo para uso contínuo.**

1. Faça login na **AppsFlyer** (nome de usuário e senha). Em seguida, você será redirecionado para a página de login com a autenticação de dois fatores.
2. Abra **Google Authenticator** no seu celular para obter o código de verificação.
3. Digite o código na página de autenticação.
4. Clique em **verificar**. Em seguida, você será redirecionado para a página **meus aplicativos**.

</Accordion>

<div id="reset-a-users-2fa" />

<Accordion title="Redefinir a 2FA de um usuário">

<Embed title="Como implementar a autenticação de dois fatores" typeOfEmbed="youtube" url="https://www.youtube.com/embed/15sYaqz89ys" providerUrl="https://www.youtube.com" />

Para redefinir sua 2FA, entre em contato com seu administrador. O administrador deve seguir estas etapas:

Observação: se você for o proprietário da conta, poderá redefinir sua própria 2FA nas [etapas a seguir](/docs/implementing-and-using-2fa-login-partners#para-um-proprietário-da-conta-redefinir-sua-própria-2fa).

#### **Para um administrador redefinir a 2FA de um usuário**

1. Na barra de menu, clique no menu suspenso do endereço de e-mail.
2. Selecione **Gerenciar usuários.**
3. Na guia **Usuários** , clique nas opções de menu na extremidade direita da linha do usuário.
4. Selecione **Resetar autenticação de dois fatores (2FA)** no menu.

#### **Para um proprietário da conta redefinir sua própria 2FA**

1. Na página de login com 2FA, clique em **Clique aqui para iniciar o processo de redefinição.**
2. Um e-mail será enviado com um código e um link para a nova página de login com 2FA.
3. Copie o código do e-mail e clique no link do e-mail.
4. Digite o código na página de configuração da 2FA.
5. Siga as etapas para configurar sua nova 2FA [aqui](/docs/implementing-and-using-2fa-login-partners#usuários-existentes).

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Especificações e limitações">

| YouTube video player | A descrição |
| --- | --- |
| Aplicativos da AppsFlyer | Com a 2FA ativada, ambos os aplicativos da AppsFlyer, **My Device ID by AppsFlyer** e **AppsFlyer**, não podem ser usados. Para registrar dispositivos de teste, use o método <Anchor target="_blank" href="/marketers/pt/docs/registering-test-devices">aqui</Anchor>. |

</Accordion>

<div data-zendesk-anchors="highlights=introdu%C3%A7%C3%A3o h_01HEHRKE8PY64KWVSSFR6T4F1Z=introdu%C3%A7%C3%A3o h_01KBVXP9J12428VNPQAG7N2B52=aten%C3%A7%C3%A3o h_01KBVXHY4VHJG6CJWHFTVK4644=importante h_01HEHRKE8QQTX3Y9ZY1HZ6GBAG=firsttime-setup new-account-user=novo-usu%C3%A1rio-da-conta h_01KBMCFPDWRBF5NPKWF3JSHBS4=novo-usu%C3%A1rio-da-conta existing-account-users=usu%C3%A1rios-existentes h_01KBMCFSS5ACAB5T6SAJ2ETNGC=usu%C3%A1rios-existentes h_01HEHRKE8QHWHCMNB5M7S5YVYJ=ongoing-use h_01KBMBVZX1N60YJKTJRAN66DY7=reset-a-users-2fa for-an-admin-resetting-a-users-2fa=para-um-administrador-redefinir-a-2fa-de-um-usu%C3%A1rio h_01KBMCSYNWA41JAP498F19JQKZ=para-um-administrador-redefinir-a-2fa-de-um-usu%C3%A1rio for-an-account-owner-resetting-their-own-2fa=para-um-propriet%C3%A1rio-da-conta-redefinir-sua-pr%C3%B3pria-2fa h_01KBMCVPFMZAC6Z05SNW3CEHQ4=para-um-propriet%C3%A1rio-da-conta-redefinir-sua-pr%C3%B3pria-2fa h_01KBVY16MN92WV0TC81QBWCNW4=traits-and-limitations" />
