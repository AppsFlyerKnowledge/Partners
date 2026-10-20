---
title: Implementing and using 2FA login
excerpt: >-
  Two-factor authentication (2FA) is used to add an extra layer of security to
  the login process. Login credentials for account users are supplemented by
  Google or Microsoft Authenticator.
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
  edited_at: '2026-08-09T07:02:53Z'
  id: 41585422141585
  locale: en-us
  section: Ad network onboarding
  section_id: 6551058566033
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/41585422141585-Implementing-and-using-2FA-login
---
## Intro

> 📘 **Note**
>
> Each person who accesses AppsFlyer must have their own user account. User credentials can’t be shared, and 2FA must be set up individually for every user. If you need to add users to the account, go to User management and create new users as needed. For details, see [User management.](/docs/user-management-for-agencies)

* 2FA is mandatory by AppsFlyer.
* 2FA must be set up using **Google or Microsoft Authenticator.**

> 📘 **Important!**
>
> After you set up 2FA, don’t delete your authenticator app. Doing so breaks the connection to AppsFlyer, and you won’t be able to log in.

<div id="firsttime-setup" />

<Accordion title="First-time setup">

#### **New account user**

1. Follow email instructions and create a password.
2. Log in to **AppsFlyer,** and you'll be redirected to the 2FA setup page.
3. Set up 2FA.
   * Download **Google or Microsoft Authenticator**.
   * Scan the QR code.
   * Enter the **Google or Microsoft Authenticator**-issued verification code.
   * Click **Verify**, and you'll be redirected to the **My apps** page.

#### **Existing account users**

1. Log in to **AppsFlyer** (username and password), and you'll be redirected to the 2FA setup page.
2. Set up 2FA.
   * Download **Google or Microsoft Authenticator**.
   * Scan the QR code.
   * Enter the **Google or Microsoft Authenticator**-issued verification code.
   * Click **Verify,** and you'll be redirected to the **My apps** page.

</Accordion>

<div id="ongoing-use" />

<Accordion title="Ongoing use">

**Follow these steps for ongoing use.**

1. Log in to **AppsFlyer** (username and password), and you'll be redirected to the 2FA login page.
2. Open **Google or Microsoft Authenticator** on your phone to get the verification code.
3. Enter the code on the 2FA page.
4. Click **Verify,** and you'll be redirected to the **My apps** page.

</Accordion>

<div id="reset-a-users-2fa" />

<Accordion title="Reset a user's 2FA">

<Embed title="Implementing and using 2FA login" typeOfEmbed="youtube" url="https://www.youtube.com/embed/15sYaqz89ys" providerUrl="https://www.youtube.com" />

To reset your 2FA, contact your Admin. The admin should follow these steps:

Note: If you are an account owner, you can reset your own 2FA in [the steps that follow](/docs/implementing-and-using-2fa-login-partners#for-an-account-owner-resetting-their-own-2fa).

#### **For an Admin resetting a user's 2FA**

1. In the menu bar, click the email address dropdown.
2. Select **User management**.
3. On the **Users** tab, click the menu options on the far right side of the user’s row.
4. Select **Reset 2FA** from the menu.

#### **For an Account owner resetting their own 2FA**

1. On the 2FA login page, click **Click here to start the reset process.**
2. An email will be sent with a code and a link to the new 2FA login page.
3. Copy the code from the email and click the link in the email.
4. Enter the code in the 2FA setup page.
5. Follow the steps for setting up your new 2FA [here](/docs/implementing-and-using-2fa-login-partners#existing-account-users).

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Traits and limitations">

| Name | Description |
| --- | --- |
| AppsFlyer apps | With 2FA enabled, both the AppsFlyer apps, **My Device ID by AppsFlyer** and **AppsFlyer**, cannot be used. To register test devices, use the method [here](/marketers/docs/registering-test-devices). |

</Accordion>

<div data-zendesk-anchors="highlights=intro h_01HEHRKE8PY64KWVSSFR6T4F1Z=intro h_01KBVXP9J12428VNPQAG7N2B52=note h_01KBVXHY4VHJG6CJWHFTVK4644=important h_01HEHRKE8QQTX3Y9ZY1HZ6GBAG=firsttime-setup h_01KBMCFPDWRBF5NPKWF3JSHBS4=new-account-user h_01KBMCFSS5ACAB5T6SAJ2ETNGC=existing-account-users h_01HEHRKE8QHWHCMNB5M7S5YVYJ=ongoing-use h_01KBMBVZX1N60YJKTJRAN66DY7=reset-a-users-2fa h_01KBMCSYNWA41JAP498F19JQKZ=for-an-admin-resetting-a-users-2fa h_01KBMCVPFMZAC6Z05SNW3CEHQ4=for-an-account-owner-resetting-their-own-2fa h_01KBVY16MN92WV0TC81QBWCNW4=traits-and-limitations" />
