---
title: Аудитории — FAQ по подключениям к рекламным сетям
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Audience Segmentation
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-neama-benhabib
    - Marketers
    - Audience Segmentation
    - Ad Networks
  created_at: '2023-11-27T08:25:39Z'
  edited_at: '2026-10-19T14:36:10Z'
  id: 20459388348305
  locale: ru
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/ru/articles/20459388348305
---
> **Краткий обзор:** Вы рекламная сеть? Найдите ответы на часто задаваемые вопросы о подключениях партнеров аудиторий.

## Ключ API и ключ partner pull

<div id="what-are-the-api-key-and-testing-api-key-used-for" />

<Accordion title="Для чего используются ключ API и тестовый ключ API?">

**Ключ API** — это уникальный ключ, который партнер выдает каждому рекламодателю. Ключ API идентифицирует рекламодателя в каждом вызове API и обычно представляет собой длинную шестнадцатеричную строку (например, d41ac239b3b918e28fa0c). В ходе тестирования вам нужно будет предоставить нам **тестовый API-ключ,** который мы будем использовать для тестирования вашей интеграции аудиторий.

</Accordion>

<div id="what-is-the-partner_pull_key" />

<Accordion title="Что такое PARTNER_PULL_KEY ?">

`PARTNER_PULL_KEY` — это ключ, который AppsFlyer генерирует и предоставляет каждому партнеру. Затем партнер использует его в переменной шаблона в URL-адресе `{{PARTNER_PULL_KEY}}` для загрузки файла сегмента.

</Accordion>

<div id="how-and-when-does-the-partner-get-the-partner_pull_key" />

<Accordion title="Как и когда мы получаем PARTNER_PULL_KEY?">

На более позднем этапе, когда мы будем тестировать вашу конечную точку `/sync`, команда AppsFlyer Audiences отправит вам `PARTNER_PULL_KEY`.

</Accordion>

## Файл аудитории, размер и ограничения

<div id="is-there-a-limitation-on-segment-size" />

<Accordion title="Есть ли ограничение на размер сегмента?">

Мы загружаем данные в AWS S3 с помощью multipart upload. Ограничения AWS см. здесь: supports:https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html

</Accordion>

<div id="how-large-are-the-files" />

<Accordion title="Насколько велики файлы?">

Мы поддерживаем большие файлы. В итоге это CSV-файлы, хранящиеся в AWS S3. Ограничения AWS см. здесь: supports:https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html

</Accordion>

<div id="is-there-an-upper-limit-for-device-id-rows" />

<Accordion title="Есть ли верхний предел для количества строк с идентификаторами устройств?">

Максимальное количество строк зависит от ограничения AWS на размер файла в 5 ТБ.

</Accordion>

<div id="can-we-use-a-direct-amazon-aws-pathbucket-for-the-audience-api" />

<Accordion title="Можем ли мы использовать прямой путь Amazon AWS/бакет для API аудиторий?">

Да, мы предоставим бакет AWS и отправим предварительно подписанный URL-адрес к пути в AWS, где находится файл.

</Accordion>

<div id="is-the-file-compressed" />

<Accordion title="Файл сжат?">

№

</Accordion>

<div id="does-the-audience-have-a-default-validity-period" />

<Accordion title="Есть ли у аудитории срок действия по умолчанию?">

Срок действия аудитории не истекает. После создания и подключения аудитория загружается каждый день. Однако аудиторию можно удалить, и тогда она больше не будет загружаться.

</Accordion>

<div id="is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id" />

<Accordion title="Формат файла разделяется переносами строк (или запятыми)? Первая строка — это заголовок, например advertiser_id ?">

Файл разделен переносами строк, а первая строка содержит заголовок, например `advertiser_id_sha256` (в зависимости от загружаемого идентификатора).

</Accordion>

<div id="will-each-sync-request-have-urls-to-all-3-files-adid-email-and-phone" />

<Accordion title="Будут ли в каждом запросе /sync URL-адреса всех 3 файлов (например, ADID, email и телефона)?">

Каждый запрос `/sync` будет содержать URL-адреса файлов, которые поддерживает интеграция. Если вы поддерживаете ADID, email и телефон, он будет содержать эти 3 URL-адреса.

</Accordion>

<div id="as-a-result-of-step-3-sync-we-get-a-link-to-download-an-audience-file-is-it-possible-to-generate-and-share-such-url-templates-without-an-api-synchronization" />

<Accordion title="В результате шага 3 ( /sync ) мы получаем ссылку для загрузки файла аудитории. Можно ли создавать и передавать такие шаблоны URL-адресов без API-синхронизации?">

На данный момент нет. URL-адреса генерируются на основе вашего уникального `PARTNER_PULL_KEY`. На этапе тестирования URL-адреса будут предоставлены, и их можно будет протестировать.

Вот пример URL-адреса:

`https://audiencespull.appsflyer.com/{{PARTNER_PULL_KEY}}/12cjv4dq1zyxz3nh-HASHED.csv?X-Amz-A` lgorithm=AWS1-HMAC-SHA256&X-Amz-Date=20190503T091923Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=AKIB22QYTATEGB2HBFJR%2F20190603%2Feu-west-1%2Fs3%2Faws4\_request&X-Amz-Signature=c8287819a21d2f7832154df609c55ab8c0afe53540d542918b2739a9234923a

</Accordion>

<div id="what-do-we-need-container_id-for" />

<Accordion title="Для чего нужен container_id ?">

Мы будем отправлять идентификаторы устройств аудитории в указанный вами container ID через API. Создание контейнера аудитории обязательно для разработки интеграции аудитории.

</Accordion>

## Вызовы API, ответы и коды статуса

<div id="when-should-the-partner-return-a-response" />

<Accordion title="Когда нужно возвращать ответ?">

`/validate`: когда ключ API совпадает с тем, который вам предоставили.

`/create`: когда контейнер создан на вашей стороне.

`/sync`: мы ожидаем получить ответ после того, как вы получите наш вызов и сможете получить доступ к файлу. Вы можете загрузить и обработать файл после отправки ответа. Ссылка доступна для загрузки в течение 2 часов.

</Accordion>

<div id="how-should-partners-handle-failed-requests" />

<Accordion title="Как следует обрабатывать неудачные запросы?">

С помощью кодов состояния:

200 — если запрос выполнен успешно

401 — при недействительном ключе API — аутентификация

Для других случаев стандартного решения нет. В этих случаях рекламодатель увидит, что загрузка не удалась из-за общей ошибки. Если проблемы повторяются, свяжитесь с нами, чтобы обсудить эти кейсы.

</Accordion>

<div id="when-are-these-endpoints-being-called-by-appsflyer" />

<Accordion title="Когда AppsFlyer вызывает наши эндпоинты?">

`/validate`: AppsFlyer вызовет этот эндпоинт один раз — каждый раз, когда рекламодатель создает новое подключение к вашей системе.

`/create`: Этот эндпоинт вызывается только один раз для каждого контейнера. Это означает, что для каждой новой аудитории, которая впервые подключается к вашей системе, мы вызываем эндпоинт `/create` и сохраняем идентификатор ID контейнера. Мы ожидаем, что в ответ на каждый вызов `/create` будет возвращаться другой идентификатор контейнера. Мы разделяем платформы и названия аудиторий на своей стороне (другими словами, у каждой платформы на нашей стороне будет своя аудитория, и для нее будет инициирован вызов `/create`).

`/sync`: Этот эндпоинт вызывается каждый раз при запуске загрузки: либо в ходе ежедневного процесса, который выполняет запланированную загрузку всех аудиторий AppsFlyer, либо когда рекламодатель инициирует загрузку вручную через наш интерфейс или вызов API.

</Accordion>

<div id="are-sync-requests-made-only-once-or-will-appsflyer-rerun-the-requests-later" />

<Accordion title="Запросы /sync выполняются только один раз или AppsFlyer повторно запускает их позже?">

Запрос `/sync` выполняется каждый раз при запуске загрузки. Это происходит в ходе ежедневного процесса, который выполняет запланированную загрузку всех аудиторий AppsFlyer, либо когда рекламодатель инициирует загрузку вручную через наш интерфейс или вызов API.

</Accordion>

<div id="how-often-does-appsflyer-send-out-calls-to-the-sync-endpoint" />

<Accordion title="Как часто AppsFlyer отправляет вызовы на эндпоинт /sync ?">

Это зависит от количества рекламодателей, с которыми вы работаете, и количества аудиторий, которые они загружают. Для каждой загружаемой аудитории будет вызван эндпоинт `/sync`. Это происходит в ходе ежедневного процесса, который выполняет запланированную загрузку всех аудиторий AppsFlyer, либо когда рекламодатель инициирует загрузку вручную через наш интерфейс или вызов API.

</Accordion>

<div id="if-it-has-high-traffic-can-partners-have-a-different-api-than-the-other-two-ie-routes-or-even-domain" />

<Accordion title="Если у нас высокий трафик, можем ли мы поддерживать несколько эндпоинтов API (например, несколько маршрутов или даже доменов)?">

Предпочтительное решение — убедиться, что текущий API может обрабатывать относительно высокий трафик. Доступна модификация API, однако это может привести к задержкам на недели или месяцы при завершении интеграции.

</Accordion>

## Правила именования

<div id="in-the-validate-interface-is-the-api_key-field-a-string-or-string-array" />

<Accordion title="В интерфейсе /validate поле api_key — это строка или массив строк?">

Это строка.

</Accordion>

<div id="in-the-create-interface-does-the-name-field-audience-name-only-need-to-support-pure-english-or-does-it-need-to-support-other-character-sets-what-are-the-validation-rules-for-names" />

<Accordion title="В интерфейсе /create должно ли поле name (имя аудитории) поддерживать только английские символы или также другие наборы символов? Каковы правила валидации для имен?">

Имя аудитории совпадает с именем в интерфейсе AppsFlyer.

* Имя должно быть уникальным и содержать от 2 до 100 символов
* Поддерживаются все языки
* Поддерживаются специальные символы (например, $, %, ^, @ и т. д.)

</Accordion>

<div id="in-the-create-interface-must-container_id-be-pure-numbers-or-can-it-support-english" />

<Accordion title="В интерфейсе /create поле container_id должно содержать только цифры или может также поддерживать английские символы?">

Поддерживаются и цифры, и английские символы.

</Accordion>

## SHA256 и хешированный URL

<div id="we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded" />

<Accordion title="Почему наша попытка декодировать SHA256 GAID/IDFA аудитории не удалась?">

SHA256 не предназначен для декодирования. Этот механизм предназначен для того, чтобы вы и AppsFlyer могли кодировать идентификатор устройства (что позволяет сопоставлять закодированные значения, если у вас есть доступ к исходному идентификатору устройства).

</Accordion>

<div id="does-appsflyer-provide-nonhashed-identifiers" />

<Accordion title="Предоставляет ли AppsFlyer нам нехешированные идентификаторы?">

Нет, нехешированные идентификаторы устройств доступны только рекламодателям. Чтобы обеспечить конфиденциальность данных, мы хешируем идентификаторы рекламодателей в файлах сегментов с помощью алгоритма SHA256. Идентификаторы рекламодателей будут передаваться в полезной нагрузке запроса с использованием этого ключа: `url_adid_sha256`.

</Accordion>

<div id="if-all-gaids-are-hashed-how-can-the-partner-know-which-gaid-they-received" />

<Accordion title="Если все GAID хешированы, как мы можем узнать, какие GAID мы получили?">

Если у вас есть обычный GAID из приложения и хешированный GAID из AppsFlyer, вы можете хешировать обычный GAID с помощью SHA256, а затем сопоставить его с хешированным GAID из AppsFlyer.

</Accordion>

<div data-zendesk-anchors="api-key-and-partner_pull_key=%D0%BA%D0%BB%D1%8E%D1%87-api-%D0%B8-%D0%BA%D0%BB%D1%8E%D1%87-partner-pull h_01HG7Y7M665JKBJEQK5Z48KYWT=%D0%BA%D0%BB%D1%8E%D1%87-api-%D0%B8-%D0%BA%D0%BB%D1%8E%D1%87-partner-pull h_01HG7YC3NBYN46DXCGJRBZKQ8N=what-are-the-api-key-and-testing-api-key-used-for h_01HG7YC3NB8KW79307GPATW5AH=what-is-the-partner_pull_key h_01HG7YC3NB71TV7EBKX7JH2DVB=how-and-when-does-the-partner-get-the-partner_pull_key audience-file-size-and-limitations=%D1%84%D0%B0%D0%B9%D0%BB-%D0%B0%D1%83%D0%B4%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B8-%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80-%D0%B8-%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D1%8F h_01HG7Z1DS1P6VDHEGDM2DMENYK=%D1%84%D0%B0%D0%B9%D0%BB-%D0%B0%D1%83%D0%B4%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B8-%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80-%D0%B8-%D0%BE%D0%B3%D1%80%D0%B0%D0%BD%D0%B8%D1%87%D0%B5%D0%BD%D0%B8%D1%8F h_01HG7Z5PQFMJQXRF9EQ89RZRF8=is-there-a-limitation-on-segment-size h_01HG7Z5PQFBQGT9STXQ4XVEWEM=how-large-are-the-files h_01HG7Z5PQFN91RC6GDWAGDJS9V=is-there-an-upper-limit-for-device-id-rows h_01HG7Z5PQFPBJPFKD0T38AM7SK=can-we-use-a-direct-amazon-aws-pathbucket-for-the-audience-api h_01HG7Z5PQFZB6F3H917JHH8QR4=is-the-file-compressed h_01HG7Z5PQFVFA8GXVD7HND7AV1=does-the-audience-have-a-default-validity-period is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like-%E2%80%98advertiser_id%E2%80%99=is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id h_01HG7Z5PQF349SS37F3X5ESNBH=is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id h_01HG7Z5PQFQAN19PD09GQMSF06=will-each-sync-request-have-urls-to-all-3-files-adid-email-and-phone h_01HGTJD9HQ4ZSZ1GQ9PH4NP6B5=as-a-result-of-step-3-sync-we-get-a-link-to-download-an-audience-file-is-it-possible-to-generate-and-share-such-url-templates-without-an-api-synchronization h_01HG7Z5PQFV6RZJ9PMBETRCM3G=what-do-we-need-container_id-for api-calls-responses-and-status-codes=%D0%B2%D1%8B%D0%B7%D0%BE%D0%B2%D1%8B-api-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D1%8B-%D0%B8-%D0%BA%D0%BE%D0%B4%D1%8B-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%B0 h_01HG7ZMJ4FS76K8HF7PP4PJGY3=%D0%B2%D1%8B%D0%B7%D0%BE%D0%B2%D1%8B-api-%D0%BE%D1%82%D0%B2%D0%B5%D1%82%D1%8B-%D0%B8-%D0%BA%D0%BE%D0%B4%D1%8B-%D1%81%D1%82%D0%B0%D1%82%D1%83%D1%81%D0%B0 h_01HG7ZQCBXRKMRYTC8PB2YDTQ1=when-should-the-partner-return-a-response h_01HG7ZQCBXRHF78ZSBP4RZ8JE3=how-should-partners-handle-failed-requests h_01HG7ZQCBXXPZZ4V7361H43WVX=when-are-these-endpoints-being-called-by-appsflyer h_01HG7ZQCBX5GGP0KFGKZG8N27R=are-sync-requests-made-only-once-or-will-appsflyer-rerun-the-requests-later h_01HG7ZQCBXEFAYE0KJN4DTTVBG=how-often-does-appsflyer-send-out-calls-to-the-sync-endpoint h_01HG7ZQCBXC765AFJSPTE2CC6Z=if-it-has-high-traffic-can-partners-have-a-different-api-than-the-other-two-ie-routes-or-even-domain naming-rules=%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F h_01HG800JBTMXQS4GPEFCK64D7H=%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0-%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F h_01HG80352MXGGZ6KVG0REGN12Q=in-the-validate-interface-is-the-api_key-field-a-string-or-string-array h_01HG80352MYBAWEQQJT4GSR36G=in-the-create-interface-does-the-name-field-audience-name-only-need-to-support-pure-english-or-does-it-need-to-support-other-character-sets-what-are-the-validation-rules-for-names h_01HG80352MYFPQF3SZ05J58VCB=in-the-create-interface-must-container_id-be-pure-numbers-or-can-it-support-english sha256-and-hashed-url=sha256-%D0%B8-%D1%85%D0%B5%D1%88%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-url h_01HG814F103B5M3Q2K5110WDEM=sha256-%D0%B8-%D1%85%D0%B5%D1%88%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D1%8B%D0%B9-url we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can%E2%80%99t-sha256-be-decoded=we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded h_01HG816BDJPN86WVFE5RM09KZ8=we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded h_01HG816BDJN9WJZTDG0TG930G9=does-appsflyer-provide-nonhashed-identifiers h_01HG816BDJ7A6GMZC14RKERQB1=if-all-gaids-are-hashed-how-can-the-partner-know-which-gaid-they-received" />
