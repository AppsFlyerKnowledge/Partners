---
title: Начало работы — руководство по ознакомлению для рекламных сетей
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
  edited_at: '2026-08-18T00:40:23Z'
  id: 360001300998
  locale: ru
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ru/articles/360001300998
---
> **Краткий обзор:** Завершите интеграцию с AppsFlyer, настроив и протестировав ссылки атрибуции и интеграции постбэков. Изучите этапы, временные рамки и зависимости процесса.

<Image align="center" alt="AdNetworks_-_Onboarding__2_.png" src="https://files.readme.io/33217648d1f5c1ef327871b9b2ccfaadb6b9ae34fb2645ffcfbe187c378dd054-30603793569297.png" />

<div id="what-is-appsflyer" />

## Что такое AppsFlyer?

AppsFlyer, лидер в области мобильной атрибуции, приветствует вас в качестве нашего интегрированного партнера рекламной сети. Эта статья предназначена для рекламных сетей, которые завершили регистрацию партнеров AppsFlyer. Если вы хотите зарегистрироваться как партнер, попросите <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#приглашайте-новых-партнёров-в-appsflyer">клиента AppsFlyer (рекламодателя) пригласить вас.</Anchor>

<div id="ad-network-onboarding" />

## Ознакомление рекламной сети

Шаги интеграции и примерное время на их выполнение указаны в разделе **Шаги ознакомления** данной статьи.

Интеграция включает:

* AppsFlyer регистрирует ваши взаимодействия (клики и показы). Взаимодействия атрибутируются согласно <Anchor target="_blank" href="/marketers/ru/docs/appsflyer-attribution-model">модели атрибуции AppsFlyer</Anchor>.
* Постбэки в требуемом формате отправляются на ваши конечные точки.
* Вы можете получить доступ к функциям AppsFlyer, таким как подписывание кликов, Protect360, Data Locker и т. д.

<div id="if-you-need-help" />

<Accordion title="Если вам нужна помощь">

* Посмотрите <Anchor target="_blank" href="/partners/ru/docs/integrated-partners-faq">FAQ</Anchor> для партнера
* Ознакомьтесь со статьей <Anchor target="_blank" href="/partners/ru/docs/integration-requests-for-partners">Запросы на изменение интеграции</Anchor>

</Accordion>

Учтите:

* Оценки времени в этой статье основаны на нашем опыте работы с рекламными сетями. Каждая интеграция немного отличается, поэтому фактическое время может варьироваться.
* AppsFlyer поддерживает множество <Anchor target="_blank" href="/partners/ru/docs/platforms-for-ad-networks">платформ для повышения эффективности</Anchor>. Если вы используете платформу из списка, перед интеграцией обязательно ознакомьтесь с инструкциями для этой платформы.

<div id="onboarding-steps" />

## Шаги ознакомления

**Для интеграции с AppsFlyer**:

1. [Выполните часть 1 — интеграция и тестирование.](/docs/getting-started-onboarding-guide-for-ad-networks#часть-1-интеграция-и-тестирование)
2. [Выполните часть 2 — тестирование с приложениями рекламодателей.](/docs/getting-started-onboarding-guide-for-ad-networks#часть-2-тестирование-при-помощи-приложений-рекламодателя)
3. [Выполните часть 3 — используйте дэшборд AppsFlyer и инструменты отчетности.](/docs/getting-started-onboarding-guide-for-ad-networks#часть-3-дэшборд-appsflyer-и-параметры-отчетности)

<div id="part-1-integration-and-testing" />

### Часть 1: Интеграция и тестирование

<table><thead><tr><th>Действие</th><th>Требуемые минуты</th></tr></thead><tbody><tr><td>Дождитесь электронного письма с подтверждением регистрации, которое предложит вам выполнить обязательные шаги интеграции.</td><td>--</td></tr><tr><td colspan="2"> <strong>Обязательные шаги интеграции</strong> </td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#ссылка-атрибуции" target="_blank">Укажите ссылку атрибуции</a>: Ссылки атрибуции — это URL-адреса с макросами. Эти макросы заполняются вами фактическими ценностями, значениями и отправляются в AppsFlyer каждый раз, когда пользователь нажимает на ссылку. <br/>Примечание! Если вы используете платформу сети эффективности, поддерживаемую AppsFlyer, вам необходимо учитывать инструкцию, специфичную для этой платформы. См. <a href="./platforms-for-ad-networks" target="_blank">Руководства по сетям эффективности</a>. </td><td>60</td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#постбэк-по-умолчанию" target="_blank">Укажите макросы постбэка</a>: Постбэки — это URL-адреса, содержащие макросы, которые заполняются в AppsFlyer и отправляются на ваши серверы в реальном времени после каждой конверсии.</td><td>60</td></tr><tr><td>Войдите в <a href="https://hq1.appsflyer.com/auth/login" target="_blank">дэшборд AppsFlyer</a>, используя предоставленные учетные данные. </td><td> </td></tr><tr><td><p>Загрузите логотип вашей компании. Ваш логотип должен быть в формате прозрачного PNG размером 200 X 50. </p><ol><li>В AppsFlyer в строке меню выберите свой адрес электронной почты &gt; <strong>Настройка партнера</strong>. </li><li>На вкладке <strong>Профиль</strong> загрузите логотип своей компании. </li><li>Нажмите <strong>Сохранить</strong>.</li></ol></td><td>5</td></tr><tr><td><p>Проверьте интеграцию с помощью тестовых приложений AppsFlyer:</p><ul><li><a href="./android-integration-testing-for-ad-networks" target="_blank">Android;</a></li><li><a href="./ios-integration-testing-for-ad-networks" target="_blank">https://files.readme.io/f28d0aac1797ee18fdc6083d9ea6d5d2f87d37a894a6c27ab0ea9b6ca51c53a1-49839256665233.png</a></li></ul></td><td>10</td></tr><tr><td colspan="2"><strong>Дополнительные шаги интеграции</strong></td></tr><tr><td>[iOS] Если вашим рекламодателям необходима функция AppsFlyer Aggregated Advanced Privacy, выполните интеграцию <a href="./self-serve-integration-management-for-ad-networks#постбэки-для-расширенной-конфиденциальности-и-постбэки-skan" target="_blank">Advanced Privacy</a>.</td><td>60</td></tr><tr><td>[iOS] Если вы запускаете кампании SKAdNetwork, выполните интеграцию <a href="./self-serve-integration-management-for-ad-networks#постбэки-для-расширенной-конфиденциальности-и-постбэки-skan" target="_blank">SKAdNetwork</a>. </td><td>60</td></tr><tr><td><h4><strong><span id="authorized-agencies"></span>Авторизованные агентства</strong></h4><p>Создайте и управляйте списком агентств, которым вы даете разрешение на проведение кампаний через вашу интеграцию сети. Это делается путем ввода идентификатора агентства (af_prt) в разделе <a href="./set-up-your-list-of-authorized-agencies" target="_blank"><strong>Авторизованные агентства</strong></a>  Центра безопасности. Чтобы получить идентификатор агентства, агентство должно связаться с вами и предоставить его.</p></td><td>2</td></tr><tr><td colspan="2"><p><strong>Дополнительные функции и соображения</strong><br/> </p><p>Рассмотрите возможность внедрения интеграций и опций на основе требований рекламодателя.</p></td></tr><tr><td>Чтобы исключить отправку мошеннических кликов с использованием вашего партнерского идентификатора, внедрите <a href="./click-signing-for-ad-networks" target="_blank">подписание кликов</a>. </td><td>&gt;60</td></tr><tr><td>Для рекламодателей, использующих Protect360 или правила валидации, добавьте <a href="./postback-macros-for-ad-networks#макросы-установки-внутренние-события-приложения-и-отклоненные-события" target="_blank">отклоненные постбэки атрибуции</a>.</td><td>15</td></tr><tr><td>Отправка стоимости в AppsFlyer через API. См. <a href="./incost-api-for-ad-networks" target="_blank">InCost API</a>.</td><td>&gt;60</td></tr><tr><td> <a href="/marketers/ru/docs/retargeting-attribution-guide" target="_blank">Интеграция ретаргетинга</a>.</td><td>15</td></tr><tr><td> <a href="/marketers/ru/docs/measure-view-through-engagements" target="_blank">Интеграция атрибуции по просмотрам</a>.</td><td>15</td></tr></tbody></table>

<div id="part-2-test-using-advertiser-apps" />

### Часть 2: Тестирование при помощи приложений рекламодателя

В этой части вы будете тестировать интеграцию, используя Приложение, принадлежащее рекламодателю. Поэтому вам необходимо связаться с рекламодателем и попросить его выполнить некоторые шаги в этом разделе. В этом разделе ссылки на рекламодателей также могут подразумевать агентства, если они действуют от имени рекламодателя.

| Выполняется | Действие | Требуемые минуты |
| --- | --- | --- |
| Рекламодатель | Включите <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#integration-tab">активацию партнера.</Anchor><br /><br />Если эта функция включена, AppsFlyer рассматривает привлеченные вами взаимодействия как кандидатов на атрибуцию. | 2 |
| Рекламодатели | Предоставьте <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#разрешения-рекламной-сети">разрешения на рекламную сеть*</Anchor> и добавьте членов своей команды.<br /><br />Если эта функция включена, данные об эффективности приложения будут доступны на вашем дэшборде AppsFlyer. Доступ к данным имеют только указанные члены команды. | 2 |
| Рекламная сеть | <Anchor target="_blank" href="/marketers/ru/docs/user-management#creating-users">Добавьте участников команды в свою учетную запись</Anchor>. | 2 |
| Рекламодатель (администратор) | <Anchor target="_blank" href="/marketers/ru/docs/registering-test-devices">Зарегистрируйте свои тестовые устройства</Anchor>. Попросите рекламодателя сделать это от вашего имени. | 3 |
| Рекламные сети | <Anchor target="_blank" href="/partners/ru/docs/test-marketer-campaign-integration-with-the-ad-network">Протестируйте интеграцию с помощью приложений рекламодателя.</Anchor> | 60 |

<div id="part-3-appsflyer-dashboard-and-reporting-options" />

### Часть 3: Дэшборд AppsFlyer и параметры отчетности

| Вариант |
| --- |
| <Anchor target="_blank" href="/partners/ru/docs/integrated-partners-dashboard">Использование дэшборда партнера</Anchor>. |
| Получайте агрегированные данные об эффективности через облачное хранилище с помощью <Anchor target="_blank" href="/partners/ru/docs/data-locker-for-partners">Data Locker</Anchor> для рекламных сетей. |
| Получите необработанные данные Protect360<Anchor target="_blank" href="/marketers/ru/docs/raw-data-export-page">.</Anchor> |

<div id="integration-validation-period" />

## Период проверки интеграции

Для обеспечения сохранности экосистемы AppsFlyer и защиты внутренних систем от недопустимого трафика все новые интеграции рекламных сетей проходят период проверки. В течение этого периода AppsFlyer тщательно проверяет трафик и оценивает его качество, прежде чем сделать интеграцию доступной другим рекламодателям на <Anchor target="_blank" href="/marketers/ru/docs/partner-integrations">маркетплейсе</Anchor>. Интеграции рекламных сетей, которые после проверки не соответствуют критериям высококачественного трафика, могут быть подвергнуты блокировке аккаунта.

<div id="validation-periodfaq" />

### Период проверки — часто задаваемые вопросы

| **Вопрос** | **Ответ** |
| --- | --- |
| <span id="why-cant-advertisers-find-me-on-the-marketplace"></span>Почему рекламодатели не могут найти меня на маркетплейсе, хотя я завершил интеграцию? | В период проверки ваша интеграция видна только тому рекламодателю, который вас направил. Когда мы подтвердим качество вашего трафика, вы получите электронное сообщение с уведомлением о том, что ваша интеграция доступна всем рекламодателям. |
| <span id="what-should-i-do-to-make-the-integration-available-for-all-advertiers"></span>Что я могу сделать, чтобы убедиться, что моя интеграция будет одобрена? | Обеспечьте значительный объем высококачественного трафика для рекламодателя, который вас направил. |
| <span id="when-should-i-expect-to-receive-the-validation-completion-email"></span>Когда мне следует ожидать получения электронной почты о завершении проверки? | После проверки достаточного объема трафика, вы получите электронную почту с уведомлением об окончании периода проверки. |
| <span id="can-i-know-the-current-status-of-the-validation-period"></span>Могу ли я узнать текущий статус проверки моей проверки? | Вы узнаете, что период проверки закончен, только после получения уведомления на электронную почту. |
| <span id="what-are-the-validation-criteria-based-on"></span>На чем основаны критерии проверки? | Критерии проверки основаны на динамических алгоритмах машинного обучения <Anchor target="_blank" href="/marketers/ru/docs/protect360-anti-fraud-guide">Protect360</Anchor>. Учитываются такие факторы, как качество трафика, объем, общая достоверность данных и лучшие практики индустрии. |
| <span id="another-adviertiser-wants-to-work-with-me"></span>Что делать, если другой рекламодатель захочет начать работать со мной во время периода проверки? | Во время периода проверки ваша интеграция видна только тому рекламодателю, который вас направил. Другие рекламодатели смогут работать с вами после успешного завершения периода проверки. |
| <span id="my-integration-fails"></span>Что произойдет, если моя интеграция не пройдет проверку? | Период проверки может быть продлен для отслеживания улучшений качества трафика, или ваша интеграция может быть навсегда удалена с платформы AppsFlyer. В любом случае, вы получите уведомление. |

<div data-zendesk-anchors="what-is-appsflyer=%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-appsflyer h_01J09255QNBFRV8DYZPGG990A0=%D1%87%D1%82%D0%BE-%D1%82%D0%B0%D0%BA%D0%BE%D0%B5-appsflyer ad-network-onboarding=%D0%BE%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D0%BE%D0%B9-%D1%81%D0%B5%D1%82%D0%B8 h_01J09255QN61VPW292PC2CH9KN=%D0%BE%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D0%BE%D0%B9-%D1%81%D0%B5%D1%82%D0%B8 h_01J09255QNGD66T140ERW4WP8Z=if-you-need-help onboarding-steps=%D1%88%D0%B0%D0%B3%D0%B8-%D0%BE%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F h_01J09255QNZ9QXXFB54YRYCM8P=%D1%88%D0%B0%D0%B3%D0%B8-%D0%BE%D0%B7%D0%BD%D0%B0%D0%BA%D0%BE%D0%BC%D0%BB%D0%B5%D0%BD%D0%B8%D1%8F part-1-integration-and-testing=%D1%87%D0%B0%D1%81%D1%82%D1%8C-1-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B8-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5 h_01J09255QN35ZBKE2R2HDDZWSZ=%D1%87%D0%B0%D1%81%D1%82%D1%8C-1-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D1%8F-%D0%B8-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5 h_01J0JS136CTYEF6F29H8R1NV29=authorized-agencies part-2-test-using-advertiser-apps=%D1%87%D0%B0%D1%81%D1%82%D1%8C-2-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BE%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8F h_01J09255QP11XJD3C83VZZXXQZ=%D1%87%D0%B0%D1%81%D1%82%D1%8C-2-%D1%82%D0%B5%D1%81%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8-%D0%BF%D0%BE%D0%BC%D0%BE%D1%89%D0%B8-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BE%D0%B4%D0%B0%D1%82%D0%B5%D0%BB%D1%8F part-3-appsflyer-dashboard-and-reporting-options=%D1%87%D0%B0%D1%81%D1%82%D1%8C-3-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-appsflyer-%D0%B8-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%B8 h_01J09255QPSSD8CF0HR059RWXZ=%D1%87%D0%B0%D1%81%D1%82%D1%8C-3-%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-appsflyer-%D0%B8-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D0%B8 integration-validation-period=%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B8-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 h_01J09255QP82ZYZDJMA74SRYGZ=%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B8-%D0%B8%D0%BD%D1%82%D0%B5%D0%B3%D1%80%D0%B0%D1%86%D0%B8%D0%B8 validation-period%E2%80%94faq=%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B8--%D1%87%D0%B0%D1%81%D1%82%D0%BE-%D0%B7%D0%B0%D0%B4%D0%B0%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5-%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B h_01J09255QP77BME57P9B7S222V=%D0%BF%D0%B5%D1%80%D0%B8%D0%BE%D0%B4-%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D1%80%D0%BA%D0%B8--%D1%87%D0%B0%D1%81%D1%82%D0%BE-%D0%B7%D0%B0%D0%B4%D0%B0%D0%B2%D0%B0%D0%B5%D0%BC%D1%8B%D0%B5-%D0%B2%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B" />
