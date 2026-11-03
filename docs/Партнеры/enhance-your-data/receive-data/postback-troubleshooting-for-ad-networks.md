---
title: Поиск и устранение неисправностей в постбэках для рекламных сетей
metadata:
  keywords:
    - Postback
    - Ad Networks
    - Partners
    - Mobile Attribution
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2022-07-07T15:16:00Z'
  edited_at: '2026-09-02T00:37:08Z'
  id: 7466104144145
  locale: ru
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ru/articles/7466104144145
---
> **Кратко:** Если у вас возникли проблемы с получением постбэков, ознакомьтесь со следующими решениями.

| **Проблема** | **РЕШЕНИЕ** |
| --- | --- |
| <span id="i-dont-see-my-advertisers-app-under-my-apps"></span>Я не вижу приложение моего рекламодателя в разделе **Мои приложения**. | <ul><li>Если приложение рекламодателя не отображается в разделе **My Apps** (в верхнем меню), свяжитесь с рекламодателем и попросите его <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#разрешения-рекламной-сети">предоставить вам соответствующие разрешения</Anchor>.</li><li>Убедитесь, что <Anchor target="_blank" href="/marketers/ru/docs/partner-activation-deactivation#активировать-интеграцию-партнера">переключатель **Активировать партнера** включен</Anchor>.</li></ul>**Примечание:** Если вы проводите тест с рабочим приложением, обязательно зарегистрируйте свое устройство в соответствии с инструкциями <Anchor target="_blank" href="/marketers/ru/docs/registering-test-devices">здесь</Anchor>. |
| <span id="im-not-receiving-install-postbacks"></span>Я не получаю постбэки об установках | <ul><li>Если установок приложения не было, постбэки об установках не будут отображаться.  Проверьте, есть ли у вашего приложения атрибуции установок: перейдите в **Settings** > **My Apps** > [Выберите приложение] > <Anchor target="_blank" href="/partners/ru/docs/integrated-partners-dashboard">**Overview**</Anchor>.</li></ul> |
| <span id="im-not-receiving-inapp-event-postbacks"></span>Я не получаю постбэки о событиях в приложении | <ul><li>Убедитесь, что события <Anchor target="_blank" href="/marketers/ru/docs/in-app-event-postback-configuration">сопоставлены корректно</Anchor> на вкладке интеграции в разделе **Постбэки событий в приложении**</li></ul>**Примечание:** Имена событий чувствительны к регистру и должны сопоставляться с тем же именем, которое передается через server-to-server/SDK. |
| <span id="im-not-receiving-both-install-and-inapp-event-postbacks"></span>Я не получаю постбэки ни об установках, ни о событиях в приложении | <ul><li>Если установок приложения не было, постбэки об установках не будут отображаться. Проверьте, есть ли у вашего приложения атрибуции установок. Перейдите в **Settings** > **My Apps** > [Выберите приложение] > <Anchor target="_blank" href="/partners/ru/docs/integrated-partners-dashboard">**Overview**</Anchor>.</li><li>Проверьте отчеты по постбэкам установок и событий в приложении и просмотрите следующие поля:<ul><li>**URL-адрес постбэка**: фактически отправленный постбэк. Убедитесь, что в шаблоне не пропущены важные значения.</li><li>**Код ответа HTTP постбэка**: код ответа, который AppsFlyer получает от сервера партнера. Проверьте код ответа HTTP. Если это не 2XX, проверьте конфигурацию вашего внутреннего сервера.</li><li>**Исходный URL-адрес**: URL-адрес клика/показа, который AppsFlyer получает для соответствующей установки/события. Проверьте полноту ссылки атрибуции. Данные, не переданные в ссылке, не могут быть возвращены через постбэк.</li></ul></li><li>Проверьте настройки **Advanced Privacy**: если эта функция включена, <Anchor target="_blank" href="/partners/ru/docs/advanced-privacy-guide-postback-macros-for-ad-networks">данные на уровне пользователя для пользователей, не давших согласие, работающих на iOS 14.5+</Anchor> НЕ доступны в постбэках.<ul><li>Если постбэк Advanced Privacy не определен в вашей интеграции, но рекламодатель решает использовать Advanced Privacy, для пользователей iOS, не давших согласие, постбэки не отправляются.</li></ul></li><li>Проверьте определение <Anchor target="_blank" href="/marketers/ru/docs/in-app-event-postback-configuration#окно-постбэков-по-внутренним-событиям">окна постбэка</Anchor>. Постбэки не отправляются по истечении заданного периода времени.</li><li>Проверьте, определен ли <Anchor target="_blank" href="/marketers/ru/docs/in-app-event-postback-configuration#условные-постбэки-по-событиям-в-приложении">условный постбэк</Anchor>.</li><li>Проверьте, <Anchor target="_blank" href="/partners/ru/docs/rejected-attribution-postbacks-to-integrated-partners">не заблокирован ли трафик</Anchor>: загрузите и просмотрите отчет **Blocked install postbacks**.</li></ul> |

> 📄 **Смотрите также**
>
> * <Anchor target="_blank" href="/marketers/ru/docs/postback-troubleshooting-for-advertisers">Устранение неполадок с постбэками для рекламодателей</Anchor>
> * <Anchor target="_blank" href="/marketers/ru/docs/in-app-event-postback-configuration">Настройка постбэков для событий в приложении</Anchor>

<div data-zendesk-anchors="h_01HDP4JFM42RZNBGM9TTD5SRP0=%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B8%D1%82%D0%B5-%D1%82%D0%B0%D0%BA%D0%B6%D0%B5" />
