---
title: Реализация и использование входа с помощью двухфакторной аутентификации
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
  edited_at: '2026-09-02T00:37:46Z'
  id: 41585422141585
  locale: ru
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ru/articles/41585422141585
---
> **Краткий обзор:** Двухфакторная аутентификация (2FA) используется для добавления дополнительного уровня безопасности в процесс входа в систему. Учётные данные для входа в систему пользователей аккаунта дополняются Google Authenticator или Microsoft Authenticator.

## Введение

> 📘 **Примечание**
>
> У каждого, кто получает доступ к AppsFlyer, должна быть собственная учётная запись пользователя. Учётные данные пользователя нельзя передавать другим, а 2FA необходимо настраивать отдельно для каждого пользователя. Если вам нужно добавить пользователей в аккаунт, перейдите в раздел «Управление пользователями» и при необходимости создайте новых пользователей. Подробнее см. в статье <Anchor target="_blank" href="/partners/ru/docs/user-management-for-agencies">Управление пользователями</Anchor>

* 2FA является обязательной в AppsFlyer.
* 2FA необходимо настроить с помощью **Google Authenticator или Microsoft Authenticator.**

> 🚧 **Двоеточие (:)**
>
> После настройки двухфакторной аутентификации (2FA) не удаляйте приложение-аутентификатор. Это приведёт к разрыву соединения с AppsFlyer, и вы не сможете войти в систему.

<div id="firsttime-setup" />

<Accordion title="Первоначальная настройка">

#### **Новый пользователь аккаунта**

1. Следуйте инструкциям, описанным в электронном письме, и создайте пароль.
2. Войдите в **AppsFlyer**, после чего вы будете перенаправлены на страницу настройки 2FA.
3. Настройте 2FA.
   * Скачайте **Google Authenticator** и приложение для сканирования **QR-кода**.
   * Отсканируйте QR-код.
   * Введите код подтверждения, сгенерированный приложением **Google Authenticator**.
   * Нажмите **Verify (Подтвердить)**, затем вы будете перенаправлены на страницу **My apps (Мои приложения)**.

#### **Существующие пользователи аккаунта**

1. Войдите в **AppsFlyer** (имя пользователя и пароль), после чего вы будете перенаправлены на страницу настройки 2FA.
2. Настройте 2FA.
   * Скачайте **Google Authenticator** и приложение для сканирования **QR-кода**.
   * Отсканируйте QR-код.
   * Введите код подтверждения, сгенерированный приложением **Google Authenticator**.
   * Нажмите **Verify (Подтвердить)**, затем вы будете перенаправлены на страницу **My apps (Мои приложения)**.

</Accordion>

<div id="ongoing-use" />

<Accordion title="Постоянное использование">

**Следуйте этим шагам для постоянного использования.**

1. Войдите в **AppsFlyer** (имя пользователя и пароль), после чего вы будете перенаправлены на страницу входа 2FA.
2. Откройте **Google Authenticator** на своём телефоне, чтобы получить код подтверждения.
3. Введите код на странице 2FA.
4. Нажмите **Verify (Подтвердить)**, затем вы будете перенаправлены на страницу **My apps (Мои приложения)**.

</Accordion>

<div id="reset-a-users-2fa" />

<Accordion title="Сброс 2FA пользователя">

<Embed title="Реализация и использование входа с помощью двухфакторной аутентификации" typeOfEmbed="youtube" url="https://www.youtube.com/embed/15sYaqz89ys" providerUrl="https://www.youtube.com" />

Чтобы сбросить 2FA, обратитесь к своему администратору. Администратор должен выполнить следующие действия:

Примечание. Если вы являетесь владельцем аккаунта, вы можете самостоятельно сбросить 2FA, выполнив [следующие шаги](/docs/implementing-and-using-2fa-login-partners#если-владелец-аккаунта-сбрасывает-собственную-2fa).

#### **Если администратор сбрасывает 2FA пользователя**

1. В строке меню нажмите раскрывающийся список с адресом электронной почты.
2. Выберите **Управление пользователями**.
3. На вкладке **Пользователи** нажмите на пункт меню в крайней правой части строки пользователя.
4. В меню выберите **Reset 2FA (Сбросить 2FA)**.

#### **Если владелец аккаунта сбрасывает собственную 2FA**

1. На странице входа в систему с 2FA нажмите **Нажмите здесь, чтобы начать процесс сброса.**
2. Будет отправлено электронное письмо с кодом и ссылкой на новую страницу входа с 2FA.
3. Скопируйте код из письма и нажмите на ссылку в письме.
4. Введите код на странице настройки 2FA.
5. Выполните шаги по настройке новой 2FA [здесь](/docs/implementing-and-using-2fa-login-partners#существующие-пользователи-аккаунта).

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Спецификации и ограничения">

| YouTube video player | Description(Описание) |
| --- | --- |
| Приложения AppsFlyer | При включенной 2FA оба приложения AppsFlyer — **My Device ID by AppsFlyer** и **AppsFlyer** — нельзя использовать. Чтобы зарегистрировать тестовые устройства, используйте метод, описанный <Anchor target="_blank" href="/marketers/ru/docs/registering-test-devices">здесь</Anchor>. |

</Accordion>

<div data-zendesk-anchors="highlights=%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5 h_01HEHRKE8PY64KWVSSFR6T4F1Z=%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5 h_01KBVXP9J12428VNPQAG7N2B52=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 h_01KBVXHY4VHJG6CJWHFTVK4644=%D0%B4%D0%B2%D0%BE%D0%B5%D1%82%D0%BE%D1%87%D0%B8%D0%B5- h_01HEHRKE8QQTX3Y9ZY1HZ6GBAG=firsttime-setup new-account-user=%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B0 h_01KBMCFPDWRBF5NPKWF3JSHBS4=%D0%BD%D0%BE%D0%B2%D1%8B%D0%B9-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8C-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B0 existing-account-users=%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%D0%B5-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B0 h_01KBMCFSS5ACAB5T6SAJ2ETNGC=%D1%81%D1%83%D1%89%D0%B5%D1%81%D1%82%D0%B2%D1%83%D1%8E%D1%89%D0%B8%D0%B5-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D0%B8-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B0 h_01HEHRKE8QHWHCMNB5M7S5YVYJ=ongoing-use h_01KBMBVZX1N60YJKTJRAN66DY7=reset-a-users-2fa for-an-admin-resetting-a-users-2fa=%D0%B5%D1%81%D0%BB%D0%B8-%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80-%D1%81%D0%B1%D1%80%D0%B0%D1%81%D1%8B%D0%B2%D0%B0%D0%B5%D1%82-2fa-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F h_01KBMCSYNWA41JAP498F19JQKZ=%D0%B5%D1%81%D0%BB%D0%B8-%D0%B0%D0%B4%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80%D0%B0%D1%82%D0%BE%D1%80-%D1%81%D0%B1%D1%80%D0%B0%D1%81%D1%8B%D0%B2%D0%B0%D0%B5%D1%82-2fa-%D0%BF%D0%BE%D0%BB%D1%8C%D0%B7%D0%BE%D0%B2%D0%B0%D1%82%D0%B5%D0%BB%D1%8F for-an-account-owner-resetting-their-own-2fa=%D0%B5%D1%81%D0%BB%D0%B8-%D0%B2%D0%BB%D0%B0%D0%B4%D0%B5%D0%BB%D0%B5%D1%86-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B0-%D1%81%D0%B1%D1%80%D0%B0%D1%81%D1%8B%D0%B2%D0%B0%D0%B5%D1%82-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%83%D1%8E-2fa h_01KBMCVPFMZAC6Z05SNW3CEHQ4=%D0%B5%D1%81%D0%BB%D0%B8-%D0%B2%D0%BB%D0%B0%D0%B4%D0%B5%D0%BB%D0%B5%D1%86-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82%D0%B0-%D1%81%D0%B1%D1%80%D0%B0%D1%81%D1%8B%D0%B2%D0%B0%D0%B5%D1%82-%D1%81%D0%BE%D0%B1%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D1%83%D1%8E-2fa h_01KBVY16MN92WV0TC81QBWCNW4=traits-and-limitations" />
