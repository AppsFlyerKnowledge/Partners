---
title: Protect360 — Вопросы и ответы для партнеров
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2023-06-12T12:43:34Z'
  edited_at: '2026-08-18T00:41:08Z'
  id: 16091549732497
  locale: ru
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/ru/articles/16091549732497
---
> **Краткий обзор.** Найдите ответы на часто задаваемые вопросы партнеров о Protect360.

<div id="impression-level-anomalies" />

## Аномалии на уровне показов

<div id="why-are-impressionsclicks-being-capped" />

<Accordion title="Почему количество показов ограничено?">

Система AppsFlyer Protect360 учитывает различные параметры при принятии решений об ограничении взаимодействий с объявлением, включая, помимо прочего, объем показов/кликов, CVR, частоту обнаруженных аномалий, нормальные колебания активности, а также отраслевые и географические показатели. Алгоритм динамичен и обновляется ежечасно с учетом меняющихся тенденций.

После срабатывания механизма блокировки Protect360 блокирует показы и клики от рекламной сети для соответствующего приложения в течение текущего 24-часового цикла. Это означает, что любые показы/клики, произошедшие после достижения порогового значения, не регистрируются AppsFlyer и не подлежат атрибуции.

Сеть может избежать превышения порога, останавливая кампании и издателей с необычно высокими объемами взаимодействий с объявлениями, которые не оказывают никакого влияния на результативность.

Рекомендуем ознакомиться с этими статьями:  
<Anchor target="_blank" href="/partners/ru/docs/protect360-for-integrated-partners#ограничение-показов">Ограничение показов и кликов</Anchor>  
<Anchor target="_blank" href="/partners/ru/docs/protect360-for-integrated-partners#faq">Вопросы и ответы об ограничении</Anchor>

</Accordion>

<div id="the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate" />

<Accordion title="Почему установки блокируются из-за клик-флудинга, а коэффициент конверсии высокий?">

Наши алгоритмы клик-флудинга работают с различными интервалами в течение дня, и при достижении порога, основанного на внутренних параметрах и логике, взаимодействия с объявлением от этого издателя не будут учитываться для атрибуции.

**Обратите внимание:** Некоторые из наших алгоритмов клик-флудинга работают в разных приложениях, что означает, что аномалии, происходящие из идентичных мошеннических источников, будут распознаваться и в других рекламируемых приложениях.

Рекомендуем прочитать: <Anchor target="_blank" href="https://www.appsflyer.com/glossary/click-flooding/">Что такое клик-флудинг?</Anchor>

</Accordion>

<div id="installin-app-event-level-anomalies" />

## Аномалии на уровне установок/событий в приложении

<div id="why-was-my-test-install-rejected-from-attribution" />

<Accordion title="Почему моя тестовая установка была отклонена для атрибуции?">

Для обнаружения мошенничества AppsFlyer применяет различные методики на разных уровнях защиты, таких как одиночные установки и кластеры установок. Кластеры рассматриваются в различных совокупностях: по издателям, медиа-источникам, приложениям и так далее. Мошенническая деятельность изучается с помощью различных статистических алгоритмов и алгоритмов машинного обучения, которые рассматривают каждый кластер как единое целое. Таким образом, если кластер признан мошенническим с высокой статистической значимостью, все установки в этом кластере считаются мошенническими. Это хорошо известная тактика мошенников — добавлять несколько законных установок к большому количеству мошеннических действий в надежде, что мошенничество будет достаточно "разбавлено", чтобы не срабатывали механизмы блокировки.

По умолчанию все входящие установки рассматриваются как LIVE-трафик, поэтому, чтобы убедиться, что алгоритмы Protect360 не поместили вашу тестовую установку в какую-либо категорию, вам необходимо выполнить шаги из <Anchor target="_blank" href="/marketers/ru/docs/registering-test-devices">этой статьи</Anchor>, чтобы зарегистрировать свое устройство в качестве тестового перед проведением теста.

</Accordion>

<div id="What-detection-methods-are-used-to-detect-install-rejections" />

<Accordion title="Какие методы обнаружения используются для выявления отклонения установки?">

Посмотрите "подпричину мошенничества", связанную с отклонением установки, чтобы получить больше ясности. Эти данные также доступны в отчетах Protect360 и на дэшборде Protect360 при условии, что соответствующий рекламодатель предоставил доступ.

Рекомендуем прочитать о <Anchor target="_blank" href="/marketers/ru/docs/protect360-raw-data-reports#причины-блокировки">причинах блокировки в Protect360</Anchor>.

</Accordion>

<div id="protect360-data-visibility-and-comprehension" />

## Видимость и понимание данных в Protect360

<div id="how-do-i-gain-visibility-into-the-protect360-results" />

<Accordion title="Как получить представление о результатах работы Protect360?">

Вы можете просмотреть результаты наших усилий по обнаружению на дэшборде Protect360 и в отчетах по сырым данным при условии, что соответствующий рекламодатель предоставил доступ.

Рекомендуем ознакомиться с этими статьями:  
<Anchor target="_blank" href="/marketers/ru/docs/protect360-dashboard">Дэшборд Protect360</Anchor>  
<Anchor target="_blank" href="/marketers/ru/docs/protect360-raw-data-reports#получение-отчетов-по-необработанным-данным">Сырые данные Protect360</Anchor>

</Accordion>

<div id="how-can-i-get-notified-in-realtime-about-blocked-traffic" />

<Accordion title="Как я могу получать уведомления о заблокированном трафике в режиме реального времени?">

AppsFlyer предоставляет рекламным сетям постбэки об отклоненной атрибуции каждой установки, которую блокирует Protect360.

Вы можете включить "постбэки об отклонениях", добавив параметры постбэка об отклонении в шаблон постбэка с помощью <Anchor target="_blank" href="/partners/ru/docs/self-serve-integration-management-for-ad-networks">управления интеграцией</Anchor>.

</Accordion>

<div id="why-do-i-see-spikes-in-postattribution-detections" />

<Accordion title="Почему наблюдаются скачки в обнаружении после атрибуции?">

Обнаружение в реальном времени до атрибуции и обнаружение после атрибуции относятся к механизму обнаружения аномалий Protect360 от AppsFlyer, который применяется в разных временных показателях.

По сравнению с обнаружением в режиме реального времени, обнаружение после атрибуции в большей степени опирается на указатели данных, собранные после установки, и если наблюдаются аномалии, Protect360 будет фиксировать аномальные действия и отображать их в категории "После атрибуции".

Учитывая вышесказанное, некоторые методы обнаружения (timestamp\_anomalies, behavioral\_anomalies и т. д.) с большей вероятностью будут обнаружены на этапе пост-атрибуции, а не в реальном времени, поскольку данные неубедительны на уровне отдельной установки, но приобретают значимость при изучении их распределения в статистическом анализе.

Узнайте больше об <Anchor target="_blank" href="/marketers/ru/docs/protect360-anti-fraud-guide#postattribution-detection">обнаружении после атрибуции</Anchor>.

</Accordion>

<div data-zendesk-anchors="click-impression-level-anomalies=%D0%B0%D0%BD%D0%BE%D0%BC%D0%B0%D0%BB%D0%B8%D0%B8-%D0%BD%D0%B0-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5-%D0%BF%D0%BE%D0%BA%D0%B0%D0%B7%D0%BE%D0%B2 01H8GKS08Y22PX2SBTW5ME02C4=%D0%B0%D0%BD%D0%BE%D0%BC%D0%B0%D0%BB%D0%B8%D0%B8-%D0%BD%D0%B0-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5-%D0%BF%D0%BE%D0%BA%D0%B0%D0%B7%D0%BE%D0%B2 01H8GKS08YXVK4CPNW9TX9XBYN=why-are-impressionsclicks-being-capped 01H8GKS08ZGNTMNZ5JH846T9Q9=the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate install-inapp-event-level-anomalies=%D0%B0%D0%BD%D0%BE%D0%BC%D0%B0%D0%BB%D0%B8%D0%B8-%D0%BD%D0%B0-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 01H8GKS08ZRA7YT9FWJNBBSV4Q=%D0%B0%D0%BD%D0%BE%D0%BC%D0%B0%D0%BB%D0%B8%D0%B8-%D0%BD%D0%B0-%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D0%B5-%D1%83%D1%81%D1%82%D0%B0%D0%BD%D0%BE%D0%B2%D0%BE%D0%BA%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B9-%D0%B2-%D0%BF%D1%80%D0%B8%D0%BB%D0%BE%D0%B6%D0%B5%D0%BD%D0%B8%D0%B8 01H8GKS08Z2M0RTMR4GM1BJE7G=why-was-my-test-install-rejected-from-attribution What-detection-methods-are-used-to-detect-install-rejections%3F=What-detection-methods-are-used-to-detect-install-rejections 01H8H30KARRPAPT9XRREDYKHVT=What-detection-methods-are-used-to-detect-install-rejections protect360-data-visibility-and-understanding=%D0%B2%D0%B8%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C-%D0%B8-%D0%BF%D0%BE%D0%BD%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B2-protect360 01H8GKS08ZX2W1G0K165H96N4Z=%D0%B2%D0%B8%D0%B4%D0%B8%D0%BC%D0%BE%D1%81%D1%82%D1%8C-%D0%B8-%D0%BF%D0%BE%D0%BD%D0%B8%D0%BC%D0%B0%D0%BD%D0%B8%D0%B5-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85-%D0%B2-protect360 01H8GKS08ZGEEK0HQVCRD546MW=how-do-i-gain-visibility-into-the-protect360-results 01H8GKS08ZC6SB4PT53JG5QKHG=how-can-i-get-notified-in-realtime-about-blocked-traffic 01H8GKS08Z673WG6C6JGW31F42=why-do-i-see-spikes-in-postattribution-detections" />
