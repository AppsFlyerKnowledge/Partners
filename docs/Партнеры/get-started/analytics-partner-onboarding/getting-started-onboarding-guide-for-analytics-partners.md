---
title: Начало работы — руководство по онбордингу для партнеров по аналитике
metadata:
  keywords:
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
  created_at: '2025-04-16T13:54:22Z'
  edited_at: '2026-09-02T00:38:14Z'
  id: 34444156204689
  locale: ru
  section: Analytics partner onboarding
  section_id: 34732438397841
  url: https://support.appsflyer.com/hc/ru/articles/34444156204689
---
> **Кратко:** настройте интеграцию с партнером по аналитике в AppsFlyer, включая конфигурацию шаблонов постбэков. В этой статье описаны шаги, сроки и зависимости, связанные с процессом онбординга.

<Image align="center" alt="54150 Онбординг партнеров KB.png" src="https://files.readme.io/f8d8abe52561baf06cb3125d7f49760d2510aaa1ed63c6c0515d3543418dad91-34615688043409.png" />

<div id="about-the-analytics-partner-integration" />

## Об интеграции с партнером по аналитике

Аккаунт партнера по аналитике в AppsFlyer — это специализированный аккаунт для поставщиков аналитики. Он предоставляет доступ к данным постбэков об установках и событиях в приложении, что позволяет партнерам анализировать поведение пользователей, результаты кампаний и эффективность приложения. Эта статья предназначена для поставщиков аналитики, которые хотят настроить партнерскую интеграцию с AppsFlyer.

<div id="set-up-the-integration" />

## Настройка интеграции

**Чтобы настроить интеграцию, выполните следующие действия:**

<div id="step-1-account-registration-and-eligibility" />

<Accordion title="Шаг 1: Зарегистрируйте аккаунт">

1. **Создание нового PID по приглашению рекламодателя:**   
   Аккаунты партнеров по аналитике (и создание PID) можно инициировать только по приглашению рекламодателя. Поделитесь этой <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#приглашайте-новых-партнёров-в-appsflyer">ссылкой</Anchor> с вашим рекламодателем и попросите его отправить вам приглашение.
2. **Завершите регистрацию:**   
   Чтобы завершить процесс регистрации в рекламной сети, выполните шаги, указанные в электронном письме с приглашением.   

   **Примечание:** Убедитесь, что адрес электронной почты, используемый для регистрации, не связан с существующей учетной записью AppsFlyer в качестве участника команды или администратора.

</Accordion>

<div id="step-2-postback-configuration-and-profile-setup" />

<Accordion title="Шаг 2: Настройте конечную точку постбэка и профиль">

1. **Письмо с подтверждением:** После одобрения вашей регистрации вы получите электронное письмо с приглашением выполнить обязательные шаги интеграции.
2. **Настройте конечную точку постбека:** Обратитесь к статье <Anchor target="_blank" href="/partners/ru/docs/postback-macros-for-analytics-partners">Макросы постбеков для партнеров по аналитике</Anchor>, чтобы настроить конечную точку постбека и макросы с помощью <Anchor target="_blank" href="/partners/ru/docs/self-serve-integration-management-for-ad-networks">платформы управления постбеками</Anchor> AppsFlyer.
3. **Настройка профиля:**
   1. В AppsFlyer в строке меню выберите свой адрес электронной почты > **Настройка партнера**.
   2. На вкладке «Профиль» заполните информацию о компании и загрузите логотип компании.
   3. Нажмите **Сохранить**, чтобы применить изменения.

</Accordion>

<div id="step-3-convert-account-type" />

<Accordion title="Шаг 3: Измените тип аккаунта">

1. **Откройте заявку для конверсии учетной записи:**  
   в AppsFlyer в верхнем меню выберите **Помощь** > **Связаться с нашей командой**. Используйте виджет помощника партнера, чтобы отправить запрос на конверсию вашей учетной записи в аналитическую учетную запись. Обязательно укажите следующую информацию:
   * Список общих рекламодателей, которые планируют сотрудничать с вашей компанией.
   * Обзор предыстории вашей компании и информация об основных услугах, которые вы предоставляете.
2. **Валидация и конверсия:** AppsFlyer проверит ваш запрос и после верификации конвертирует учетную запись вашей рекламной сети в аккаунт аналитики.

</Accordion>

<div id="faq" />

## Часто задаваемые вопросы

<div id="can-i-change-my-current-ad-network-account-to-an-analytics-account" />

<Accordion title="Можно ли изменить мою текущую учетную запись рекламной сети на аналитический аккаунт?">

Нет, в аналитический аккаунт можно конвертировать только вновь зарегистрированный PID. Новый PID — это PID, который еще не отправлял в AppsFlyer клики или показы.

</Accordion>

<div id="do-i-have-access-to-raw-data-export" />

<Accordion title="Есть ли у меня доступ к экспорту сырых данных?">

Нет, аналитические аккаунты могут получать только постбэки по установкам и событиям в приложении.

</Accordion>

<div id="can-i-use-attribution-links-to-generate-traffic-for-advertisers-in-an-analytics-account" />

<Accordion title="Можно ли использовать атрибуционные ссылки, чтобы генерировать трафик для рекламодателей в аналитическом аккаунте?">

Нет, в аккаунте аналитики нет атрибуционных ссылок, и он не может отправлять в AppsFlyer клики или показы.

</Accordion>

<div data-zendesk-anchors="what-is-an-analytics-account=%D0%BE%D0%B1-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D0%BE%D0%BC-%D0%BF%D0%BE-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B5 h_01JRZE65YT0KASS4T56P0HBDWA=%D0%BE%D0%B1-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8-%D1%81-%D0%BF%D0%B0%D1%80%D1%82%D0%BD%D0%B5%D1%80%D0%BE%D0%BC-%D0%BF%D0%BE-%D0%B0%D0%BD%D0%B0%D0%BB%D0%B8%D1%82%D0%B8%D0%BA%D0%B5 onboarding-steps=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 h_01JRZE6BJT65Q7SQZHH1JDS6DQ=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 h_01JRZE9YJXSVZ10K582F45TME6=step-1-account-registration-and-eligibility h_01JRZE9YJY2VWM47X1254EHHQN=step-2-postback-configuration-and-profile-setup h_01JRZE9YJYYHT1XEZ0PC900Y0A=step-3-convert-account-type faq=%D1%87%D0%B0%D1%81%D1%82%D0%BE-%D0%B7%D0%B0%D0%B4%D0%B0%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5-%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B h_01JRZH0CCGQVN5Y199TCRHKYB7=%D1%87%D0%B0%D1%81%D1%82%D0%BE-%D0%B7%D0%B0%D0%B4%D0%B0%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5-%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B h_01JRZH6MH4PT29S12H0QJBECW5=can-i-change-my-current-ad-network-account-to-an-analytics-account h_01JRZH6MH4ZMJA0D8N7W3JBCSJ=do-i-have-access-to-raw-data-export h_01JRZH6MH4EXZ2MFMTYPTBFYSJ=can-i-use-attribution-links-to-generate-traffic-for-advertisers-in-an-analytics-account" />
