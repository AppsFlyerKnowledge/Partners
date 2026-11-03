---
title: 'Начало работы: адаптация агентства'
metadata:
  keywords:
    - Agency Account
    - Agency
    - permissions
    - Advertisers
    - Agencies
    - Partners
    - Marketers
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Marketers
    - Platform essentials
    - Agencies
  created_at: '2019-09-02T12:50:49Z'
  edited_at: '2026-08-18T00:40:50Z'
  id: 360002381617
  locale: ru
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/ru/articles/360002381617
---
> **Краткий обзор.** Создайте аккаунт агентства, чтобы начать измерения по кампаниям своих клиентов.

<Embed title="Начало работы: адаптация агентства" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/medias/54qzpj1lm7/swatch" providerUrl="https://fast.wistia.com" />


## Модель атрибуции AppsFlyer

Прежде чем мы продолжим, важно разобраться, как работает атрибуция AppsFlyer. В этом разделе объясняется, что происходит на протяжении всего пути — от первого клика или просмотра до атрибуции установки или события — и далее.

[![ua-agency-flow.png](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)](https://files.readme.io/09b001f7b5395ffa9c6e7f5abf4e7df5919fd9964ea17fa2934579f513fdb615-360004474817.png)

1. Маркетолог или агентство от имени маркетолога настраивает кампанию с определенной рекламной сетью, используя ссылки атрибуции AppsFlyer.
2. Пользователь кликает на одно из рекламных объявлений, например, на баннер или на ссылку в предложении.
3. В ссылку атрибуции AppsFlyer этого рекламного объявления добавляются данные, собранные во время клика. Мы собираем информацию из ссылки атрибуции и сохраняем ее в своей базе данных.
4. Пользователь перенаправляется в магазин приложений.
5. Пользователь устанавливает приложение и открывает его в первый раз. Интегрированный в приложение SDK AppsFlyer отправляет запрос на наши серверы с информацией об устройстве, на котором установлено данное приложение.
6. Мы сопоставляем эти сведения с нашей базой данных по кликам, используя свои <Anchor target="_blank" href="/marketers/ru/docs/appsflyer-attribution-model">методы атрибуции</Anchor>.
7. Если совпадение найдено, установка атрибутируется клику. Если нет, установка считается органической загрузкой.
8. После атрибуции установки данные о ней отображаются на дэшбордах и в отчетах маркетолога и агентства (<Anchor target="_blank" href="/partners/ru/docs/about-agency-accounts#рекламные-сети-с-автоматической-отчетностью">исключение составляют Meta Ads и X Ads</Anchor>).
9. Затем мы отправляем постбэк со сведениями о конверсии в рекламную сеть, которая может использовать эту информацию для дальнейшей оптимизации.

## Роль агентства в цепочке мобильной атрибуции

Маркетолог, которому принадлежит приложение, интегрирует в него SDK AppsFlyer, чтобы количественно оценивать эффективность своих маркетинговых усилий.

Некоторые владельцы приложений предпочитают нанимать маркетинговые агентства, которые проводят рекламные кампании от их имени. Для этого у агентства должен быть аккаунт AppsFlyer, а маркетологи должны предоставить ему <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#разрешения-агентства">доступ к своим приложениям</Anchor>.

Таким образом, агентство не является владельцем приложений, а только продвигает их по маркетинговым каналам, с которыми работает. Также агентство не выполняет технические работы, такие как интеграция SDK. В зависимости от предоставленного маркетологом набора разрешений, агентство может контролировать ряд функций.

Когда установка атрибутируется рекламному объявлению, размещенному агентством, она отображается на дэшборде агентства. Владелец приложения тоже ее увидит и будет знать, что она атрибутирована агентству.

Примечание. Если ваша организация является владельцем приложения или занимается и его разработкой, и маркетингом, вам следует открыть аккаунт маркетолога.

## Цены

Набор функциональных возможностей аккаунта агентства зависит от разрешений, предоставленных владельцами каждого приложения. Поэтому аккаунты агентств **бесплатны**, и за атрибуцию плата взимается только с владельцев приложений. Владельцы приложений и агентства могут использовать данные атрибуции AppsFlyer для расчета компенсации.

## Начало работы

Чтобы настроить новый аккаунт агентства:

1. Заполните <Anchor target="_blank" href="https://www.appsflyer.com/start/agencies/">регистрационную форму</Anchor>.
   * Для регистрации используйте эл. почту с доменом своей компании.
   * Используйте адрес эл. почты, не связанный с существующим аккаунтом AppsFlyer.
2. С вами может связаться специалист AppsFlyer по работе с агентствами по поводу дополнительной информации, необходимой для завершения регистрации.
3. Когда ваш аккаунт будет активирован, вы получите уведомление и сможете начать пользоваться AppsFlyer.

## Добавление членов команды

Когда аккаунт настроен, администратор аккаунта (т. е. пользователь, открывший аккаунт) может добавлять участников с доступом к некоторым или всем приложениям, которыми управляет агентство. Подробное описание процедуры добавления сотрудников см. здесь.

## Добавление приложений в аккаунт

Когда вы только создали аккаунт, с ним еще не связаны приложения.

![agency-start.png](https://files.readme.io/b536dde5f7cc886e7fc6ff22f15c402cea5cf68824fd92f242d13037824072d5-360003986997.png)

Всем сотрудникам и командам агентства требуются разрешения от владельца приложения на:

* доступ к дэшборду приложения
* изменение настроек
* запуск кампаний

Маркетологи <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#разрешения-агентства">предоставляют доступ агентствам</Anchor> непосредственно через платформу. Когда вы настроили аккаунт и получили доступ к приложениям, можно приступать к запуску кампаний с использованием возможностей AppsFlyer.

### Возможности, которые дает разрешение от маркетолога

Когда вы получаете разрешения от маркетолога:

* Приложение появляется в вашем аккаунте.
* Вы можете настроить для приложения интеграции с рекламными сетями (за исключения некоторых сетей, которые требуют, чтобы настройка выполнялась владельцем приложения).
* Вы можете создавать ссылки атрибуции для использования в рекламных кампаниях.
* Вы можете создавать интеграции с партнерами для получения данных о затратах (если партнер предоставляет такие данные).
* Вам видны данные приложения.
* Вы можете предоставлять рекламным сетям и их сотрудникам разрешения на просмотр базовой информации о приложении.  

  > 📘 **Примечание**
  >
  > Агентство получает контроль над основным переключателем разрешений для рекламной сети и отдельными разрешениями, вложенными в него. И агентство, и рекламодатель могут изменять эти настройки, а текущее состояние определяется последним изменением, внесенным любой из сторон.


К дополнительным разрешениям относятся доступ к когортному отчету, дэшборду Protect360 и агрегированным органическим данным. См. <Anchor target="_blank" href="/marketers/ru/docs/set-up-an-integrated-partner#разрешения-агентства">описание различных разрешений для рекламной сети</Anchor>.

### Список приложений

Как только вы получаете разрешение от маркетолога, соответствующее приложение появляется на странице приложений.

Страница приложений вашего аккаунта может содержать до 1000 приложений. Если приложений, по которым у вас есть разрешения, более 1000, в списке показываются не все приложения. Скрытые приложения можно найти через поиск.

![agency-apps.png](https://files.readme.io/6ec28125c938a5fb90d6a5bfe80ef40225432c222dcd4fafd747eeba529f1c49-360003722277.png)

#### Поиск приложений

1. В своем аккаунте в верхнем меню выберите **Мои приложения**.
2. Введите запрос в строке поиска, например,
   * Имя приложения
   * Идентификатор приложения
   * эл. почту владельца приложения

## Дэшборд агентства

Нажмите любое приложение из списка, чтобы открыть его <Anchor target="_blank" href="/marketers/ru/docs/getting-started-with-appsflyer-dashboards">дэшборд</Anchor>. Когда вы начнете проводить кампании, здесь будут отображаться агрегированные данные, атрибутированные вашему агентству.

![agency-dashboard.png](https://files.readme.io/5f541770f60ba7d212c9f18e3a14d625758c5d8911997ce4cc39333ee7530244-360003815398.png)

C дэшборда аккаунта агентства есть доступ по умолчанию к следующим дэшбордам:

* Обзорный дэшборд жизненной ценности
* Дэшборд событий в приложении
* Дэшборд Ретаргетинг

## Проведение кампаний

### Сети с самостоятельной отчетностью (SRN)

Сети с самостоятельной атрибуцией (SRN или SAN) — это сети, которые передают данные о кликах и другие сведения не с помощью ссылки атрибуции AppsFlyer, а через прямую интеграцию с AppsFlyer. К таким сетям относятся <Anchor target="_blank" href="/marketers/ru/docs/meta-ads-faq#attributing-agencies-with-facebook">Meta Ads</Anchor>, <Anchor target="_blank" href="/marketers/ru/docs/x-ads-formerly-twitter-ads-faq-and-discrepancies#any-special-instructions-for-agencies">X Ads</Anchor>, <Anchor target="_blank" href="/marketers/ru/docs/google-ads-adwords-integration-setup-for-agencies">Google Ads</Anchor>, <Anchor target="_blank" href="/marketers/ru/docs/snapchat-advanced-srn-integration-setup">Snapchat</Anchor>, DoubleClick, <Anchor target="_blank" href="/marketers/ru/docs/apple-ads-integration-setup">Apple Ads Search</Anchor>, <Anchor target="_blank" href="/marketers/ru/docs/yahoo-integration-setup">Yahoo</Anchor> и <Anchor target="_blank" href="/marketers/ru/docs/yahoo-japan-search-ads-campaign-configuration#agency-integration">Yahoo! Япония</Anchor>.

У большинства этих сетей свои требования к настройкам для агентств. Например, поскольку интеграцию с Meta Ads и X Ads может настроить только владелец приложения, названия кампаний агентства ДОЛЖНЫ начинаться с названия агентства. Это необходимо, чтобы установки корректно атрибутировались агентству.

Воспользуйтесь указанными выше ссылками, чтобы ознакомиться с руководствами по конкретным сетям и их специальными указаниями по настройкам для агентств.

### Не-SRN

Для большинства рекламных сетей нужны ссылки атрибуции, используемые в рекламных объявлениях. Подробнее о проведении кампаний с такими сетями читайте <Anchor target="_blank" href="/partners/ru/docs/about-agency-accounts#не-srn">здесь</Anchor>.

### Начало работы: адаптация агентства

Инфраструктура SKAdNetwork входит в состав Apple iOS и позволяет маркетологам измерять эффективность кампаний без IDFA и рекламного идентификатора. Хотя Apple не включает агентства в процесс атрибуции SKAdNetwork, и AppsFlyer не может атрибутировать агентства напрямую, у AppsFlyer все еще есть возможность предоставлять данные атрибуции по кампаниям, реализуемым агентствами в SKAdNetwork.

#### Названия кампаний

В AppsFlyer в боковом меню выберите **Настройки** > **Настройки приложений**.

* ваш af\_prt (<Anchor target="_blank" href="/partners/ru/docs/about-agency-accounts#параметр-af_prt">что такое af\_prt и где его найти</Anchor>),
* нижнее подчеркивание,
* фактическое название кампании, составленное по правилам присвоения имен агентства.

Например, если ваш af\_prt — AgencyX, название кампании может выглядеть следующим образом:

`AgencyX_SummerSale`

> 📘 **Примечание**
>
> * Кампании агентств в Sandbox Атрибуции также прозрачны, и идентификатор рекламной сети, запускающей кампанию, не скрывается от маркетолога.

### Кампании агентства в SKAdNetwork

Инфраструктура SKAdNetwork входит в состав Apple iOS и позволяет маркетологам измерять эффективность кампаний без IDFA и рекламного идентификатора. Хотя Apple не включает агентства в процесс атрибуции SKAdNetwork, и AppsFlyer не может атрибутировать агентства напрямую, у AppsFlyer все еще есть возможность предоставлять данные атрибуции по кампаниям, реализуемым агентствами в SKAdNetwork.

#### Разделу "Ретаргетинг"

Чтобы просматривать свои кампании на дэшборде AppsFlyer SKAdNetwork, названия кампаний, которые вы настраиваете с помощью SKAdNetwork, должны содержать ваш партнерский идентификатор и иметь следующую структуру:

* ваш af\_prt (<Anchor target="_blank" href="/partners/ru/docs/about-agency-accounts#параметр-af_prt">что такое af\_prt и где его найти</Anchor>),
* нижнее подчеркивание,
* фактическое название кампании, составленное по правилам присвоения имен агентства.

Если кампания проводится не в рекламных сетях, а в других каналах (социальные сети, рассылки, блоги, СМС), вы можете использовать <Anchor target="_blank" href="/marketers/ru/docs/create-a-onelink-template">настраиваемые ссылки</Anchor>.

`AgencyX_SummerSale`

> 📘 **Примечание**
>
> * Кампании агентств в SKAdNetwork всегда прозрачны, и идентификатор рекламной сети, в которой проводится кампания, не скрывается от маркетолога. Учитывайте, что начиная с iOS 15, маркетолог (владелец приложения) сможет <Anchor target="_blank" href="https://developer.apple.com/documentation/storekit/skadnetwork/receiving_ad_attributions_and_postbacks">настроить получение копии постбэков напрямую.</Anchor>
> * Необходимо попросить маркетолога включить настройку **Активация партнера** на вкладке интеграции. В противном случае AppsFlyer не сможет передавать сетям декодированные данные постбэка, что повлияет на их возможность использовать их для отчетности и оптимизации. Это делается дополнительно к настройке «Активация партнера», доступной вам в интерфейсе пользователя.

#### Доступ к SKAN Conversion Studio

В <Anchor target="_blank" href="/marketers/ru/docs/skan-conversion-studio#основы-работы-с-skan-conversion-studio">SKAN Conversion Studio</Anchor> агентства могут <Anchor target="_blank" href="/marketers/ru/docs/skan-conversion-studio#view-cv-mapping">просматривать и скачивать</Anchor> конфигурацию сопоставления CV в SKAN маркетолога, но не могут настраивать или редактировать параметры.

#### Дэшборд SKAdNetwork

<Embed title="Начало работы: адаптация агентства" typeOfEmbed="iframe" url="https://fast.wistia.com/embed/iframe/jkm7se0jym" providerUrl="https://fast.wistia.com" />

**Другие стать на эту тему:**

* <Anchor target="_blank" href="/marketers/ru/docs/about-att-and-skan">Руководство по началу работы со SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/marketers/ru/docs/skadnetwork-skan-overview-dashboard-by-appsflyer">Дэшборд SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/marketers/ru/docs/skadnetwork-skan-solution-guide">Решение SKAdNetwork</Anchor>

### Единый источник истины (SSOT) для агентств

SSOT унифицирует все методы атрибуции, объединяя данные об атрибуции из различных моделей и удаляя дублирующиеся установки и связанные с ними показатели затрат и доходов. Таким образом, например, правильно рассчитываются eCPI, ROI и ROAS.

Агентства могут получить доступ к данным SSOT на обзорном дэшборде, но не через API.

Чтобы включить в свой обзорный дэшборд флаг SSOT, маркетологу необходимо включить SSOT в Conversion Studio.

**Другие стать на эту тему:**

* <Anchor target="_blank" href="/marketers/ru/docs/single-source-of-truth-ssot-guide-for-ios-attribution">Руководство по единому источнику истины (SSoT) для атрибуции пользователей iOS</Anchor>

## Что еще можно делать

* Измерять удержание пользователей
* Использовать внутренние события приложений для оптимизации кампаний
* Проводить <Anchor target="_blank" href="/marketers/ru/docs/retargeting-attribution-guide">ретаргетинговые</Anchor> кампании
* Экспортировать <Anchor target="_blank" href="/marketers/ru/docs/manage-data-access-permissions">данные</Anchor>
* <Anchor target="_blank" href="/marketers/ru/docs/registering-test-devices">Зарегистрировать свое тестовое устройство</Anchor>
* и многое другое.

О расширенном использовании аккаунта агентства читайте <Anchor target="_blank" href="/partners/ru/docs/about-agency-accounts#agency-setting-up-campaigns">здесь</Anchor>.

Встретился незнакомый термин? Найдите его в нашем <Anchor target="_blank" href="/marketers/ru/docs/appsflyer-knowledge-base-glossary">глоссарии</Anchor>.

Возник срочный технический вопрос? Попробуйте найти ответ в нашем справочном центре. Если нужной информации в нем нет, свяжитесь с командой поддержки через виджет в правом нижнем углу дэшборда.

<div data-zendesk-anchors="appsflyer-attribution-model=%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-appsflyer h_01HFXXKCMW7EREMC7KEYTF3ERH=%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-appsflyer h_01KZTW5D6QWFP2Z3J31M9B6QKR=%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-appsflyer agency-role-in-mobile-attribution-chain=%D1%80%D0%BE%D0%BB%D1%8C-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0-%D0%B2-%D1%86%D0%B5%D0%BF%D0%BE%D1%87%D0%BA%D0%B5-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 h_01HFXXKCMW987FV2PB4EPXH92Z=%D1%80%D0%BE%D0%BB%D1%8C-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0-%D0%B2-%D1%86%D0%B5%D0%BF%D0%BE%D1%87%D0%BA%D0%B5-%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 pricing=%D1%86%D0%B5%D0%BD%D1%8B h_01HFXXKCMWPN6AN98A5RD5YXW7=%D1%86%D0%B5%D0%BD%D1%8B getting-started=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B h_01HFXXKCMWRXVBYTW9RYEX7X8F=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B adding-team-members=%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%87%D0%BB%D0%B5%D0%BD%D0%BE%D0%B2-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B h_01HFXXKCMWB6ZG3PSHDSETC4XC=%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D1%87%D0%BB%D0%B5%D0%BD%D0%BE%D0%B2-%D0%BA%D0%BE%D0%BC%D0%B0%D0%BD%D0%B4%D1%8B adding-apps-to-your-account=%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82 h_01HFXXKCMWBZVTHAEKED1Q27M3=%D0%B4%D0%BE%D0%B1%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-%D0%B0%D0%BA%D0%BA%D0%B0%D1%83%D0%BD%D1%82 what-does-it-mean-to-get-permission-from-a-marketer=%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5-%D0%B4%D0%B0%D0%B5%D1%82-%D1%80%D0%B0%D0%B7%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BE%D1%82-%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B0 h_01HFXXKCMWYNNZWTKP9KEQ4VCD=%D0%B2%D0%BE%D0%B7%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE%D1%81%D1%82%D0%B8-%D0%BA%D0%BE%D1%82%D0%BE%D1%80%D1%8B%D0%B5-%D0%B4%D0%B0%D0%B5%D1%82-%D1%80%D0%B0%D0%B7%D1%80%D0%B5%D1%88%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BE%D1%82-%D0%BC%D0%B0%D1%80%D0%BA%D0%B5%D1%82%D0%BE%D0%BB%D0%BE%D0%B3%D0%B0 h_01JV9KR17EEHA6F2F8J13AEZEV=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 app-list=%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 h_01HFXXKCMWKW78TMC76F40PY2C=%D1%81%D0%BF%D0%B8%D1%81%D0%BE%D0%BA-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 searching-for-apps=%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 h_01HFXXKCMW8S93N577393QZTYX=%D0%BF%D0%BE%D0%B8%D1%81%D0%BA-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B9 agency-dashboard=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0 h_01HFXXKCMWPZVADY15DKATJ7Z4=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0 running-campaigns=%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B9 h_01HFXXKCMWFB9RXY7AVBX5CGB9=%D0%BF%D1%80%D0%BE%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B9 selfreporting-networks-srns=%D1%81%D0%B5%D1%82%D0%B8-%D1%81-%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C%D1%8E-srn h_01HFXXKCMW1Z7FWHDJ3Y6G0NYD=%D1%81%D0%B5%D1%82%D0%B8-%D1%81-%D1%81%D0%B0%D0%BC%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%BE%D1%82%D1%87%D0%B5%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C%D1%8E-srn nonsrns=%D0%BD%D0%B5-srn h_01HFXXKCMWPAMZ373D5AVD5EJF=%D0%BD%D0%B5-srn sandbox-attribution-agency-campaigns=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%B0%D0%B4%D0%B0%D0%BF%D1%82%D0%B0%D1%86%D0%B8%D1%8F-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0 h_01J6PCDYM2W1X6EMMEE7SFB3VE=%D0%BD%D0%B0%D1%87%D0%B0%D0%BB%D0%BE-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%B0%D0%B4%D0%B0%D0%BF%D1%82%D0%B0%D1%86%D0%B8%D1%8F-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0 campaign-naming=%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B9 h_01HFXXKCMWMW1AHXMS19CYD4VC=%D0%BD%D0%B0%D0%B7%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B9 h_01HFXXKCMWEQ41A7TZ2K6DE424=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5-1 skadnetwork-agency-campaigns=%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0-%D0%B2-skadnetwork h_01HFXXKCMWZ19E0QR1VE977BTS=%D0%BA%D0%B0%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2%D0%B0-%D0%B2-skadnetwork 01J6PCG6JGY2R8T5DDCR8APM66=%D1%80%D0%B0%D0%B7%D0%B4%D0%B5%D0%BB%D1%83-%D1%80%D0%B5%D1%82%D0%B0%D1%80%D0%B3%D0%B5%D1%82%D0%B8%D0%BD%D0%B3 01J6PCG6JHK9TGX93SD4DRP393=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5-2 access-to-skan-conversion-studio=%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF-%D0%BA-skan-conversion-studio h_01HFXXKCMWX53HMRG2ZTD9FYQE=%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF-%D0%BA-skan-conversion-studio skadnetwork-dashboard=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-skadnetwork h_01HFXXKCMW1HHMSS3XAXJKME29=%D0%B4%D1%8D%D1%88%D0%B1%D0%BE%D1%80%D0%B4-skadnetwork single-source-of-truth-ssot-for-agencies=%D0%B5%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9-%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA-%D0%B8%D1%81%D1%82%D0%B8%D0%BD%D1%8B-ssot-%D0%B4%D0%BB%D1%8F-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2 h_01HFXXKCMX1E8GZKHJG7EEJ5Y1=%D0%B5%D0%B4%D0%B8%D0%BD%D1%8B%D0%B9-%D0%B8%D1%81%D1%82%D0%BE%D1%87%D0%BD%D0%B8%D0%BA-%D0%B8%D1%81%D1%82%D0%B8%D0%BD%D1%8B-ssot-%D0%B4%D0%BB%D1%8F-%D0%B0%D0%B3%D0%B5%D0%BD%D1%82%D1%81%D1%82%D0%B2 what-else-you-can-do=%D1%87%D1%82%D0%BE-%D0%B5%D1%89%D0%B5-%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE-%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C h_01HFXXKCMXQ2JT63GBMC74PWBA=%D1%87%D1%82%D0%BE-%D0%B5%D1%89%D0%B5-%D0%BC%D0%BE%D0%B6%D0%BD%D0%BE-%D0%B4%D0%B5%D0%BB%D0%B0%D1%82%D1%8C" />
