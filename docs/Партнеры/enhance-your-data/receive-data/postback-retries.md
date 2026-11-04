---
title: Повторные попытки отправки постбэков
metadata:
  keywords:
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
  created_at: '2018-08-06T04:59:54Z'
  edited_at: '2026-09-02T00:37:06Z'
  id: 360001376085
  locale: ru
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/ru/articles/360001376085
---
> **Кратко:** Узнайте, как работают повторные попытки отправки постбэков в AppsFlyer и как интегрированные партнеры могут настроить свои механизмы постбэков.

<div id="introduction" />

## Введение

Постбэки партнерам — это критически важная часть интеграции между AppsFlyer и нашими партнерами. Поскольку в любой системе могут возникать кратковременные проблемы с откликом, AppsFlyer может повторно отправлять неудачные постбэки.

<div id="important-information" />

## Важная информация

<div id="when-does-appsflyer-retry-a-failed-postback" />

<Accordion title="Когда AppsFlyer повторно отправляет неудачный постбэк?">

Повторная отправка постбэка выполняется, если ответ указывает на ошибку 5XX на стороне принимающего сервера.

</Accordion>

<div id="how-often-does-appsflyer-retry-a-failed-postback" />

<Accordion title="Как часто AppsFlyer повторно отправляет неудачный постбэк?">

Первая неудачная отправка постбэка повторяется до четырех раз с дополнительными попытками через 15 минут. Всего один постбэк может быть отправлен до пяти раз.

</Accordion>

<div id="can-retried-postbacks-be-identified-in-postback-reports" />

<Accordion title="Можно ли определить повторно отправленные постбэки в отчетах по постбэкам?">

В отчете по постбэкам в сырых данных есть столбец "Postback Retry". У первого отправленного постбэка в этом столбце пустое значение. У любого повторно отправленного постбэка в этом столбце указано значение TRUE.

</Accordion>

<div id="how-can-a-partner-identify-the-total-eventual-failed-postbacks-in-the-postback-report" />

<Accordion title="Как партнеру определить в отчете по постбэкам общее число постбэков, которые в итоге не удалось отправить?">

Постбэк, у которого в столбце "Postback Retry" указаны четыре значения TRUE и при этом в поле Postback HTTP Response Code содержатся коды ошибок, — это постбэк, который полностью не удалось отправить партнеру.

</Accordion>

<div id="is-there-anything-special-a-partner-should-consider-about-retried-postbacks" />

<Accordion title="Есть ли что-то особенное, что партнеру следует учитывать в отношении повторно отправленных постбэков?">

Если постбэк достиг вашей системы и был успешно обработан, но при отправке ответа произошла ошибка или возникла задержка, такое уведомление считается неудачным постбэком, и через 15 минут предпринимаются повторные попытки его отправки. Это может привести к дублированию на стороне партнера. Партнер должен реализовать на своей стороне механизм дедупликации.

</Accordion>

<div id="are-postback-retries-automatically-enabled-for-all-partners" />

<Accordion title="Включены ли повторные попытки отправки постбэков автоматически для всех партнеров?">

№ № Если партнер хочет повторно отправлять неудачные постбэки, ему следует обратиться к своему PDM, чтобы включить эту функцию.

</Accordion>

<div data-zendesk-anchors="introduction=%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5 important-information=%D0%B2%D0%B0%D0%B6%D0%BD%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F" />
