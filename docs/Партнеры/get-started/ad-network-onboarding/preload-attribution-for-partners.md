---
title: Атрибуция предварительной загрузки для партнеров
metadata:
  keywords:
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-alina-koifman
    - Marketers
    - Mobile Attribution
  created_at: '2023-05-15T09:45:55Z'
  edited_at: '2026-10-19T14:35:41Z'
  id: 15321350340241
  locale: ru
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ru/articles/15321350340241
---
> **Кратко:** Атрибутируйте установки мобильного приложения к кампаниям, в рамках которых приложение предустанавливается производителем оригинального оборудования (OEM) или при первом включении устройства пользователем.

<div id="overview" />

## Информация о компании

Благодаря поддержке решений AppsFlyer для атрибуции предварительной загрузки партнеры по предварительной загрузке могут атрибутировать установки приложения к кампаниям предварительной загрузки. Кампании предварительной загрузки используются, когда приложение устанавливается на устройство партнером по предварительной загрузке либо на заводе, либо при активации устройства (когда пользователь впервые включает устройство).

Партнерами по предварительной загрузке являются:

* Производители оригинального оборудования (OEM)
* Платформы для обнаружения приложений
* Мобильные операторы

Способов атрибуции кампаний предварительной загрузки всего три:

* [Рекомендуется] AppsFlyer Referrer
* Автоматическая установка в Google Play (PAI)
* [Устаревшее] Предварительная загрузка на заводе через свойство системы

После каждой конверсии отправляются постбэки.

<Anchor target="_blank" href="/marketers/ru/docs/appsflyer-attribution-model#preload-campaigns">Узнать больше о методах атрибуции кампаний предварительной загрузки</Anchor>

<div id="set-up-preload-attribution" />

## Настройка атрибуции предварительной загрузки

Чтобы настроить атрибуцию предварительной загрузки:

1. Убедитесь, что вы являетесь <Anchor target="_blank" href="/partners/ru/docs/getting-started-onboarding-guide-for-ad-networks">интегрированным партнером AppsFlyer</Anchor>.
2. Выберите решения для атрибуции предварительной загрузки, которые нужно интегрировать (в зависимости от потребностей рекламодателя). **Примечание**: Для каждой интеграции требуется отдельный PID с учетной записью партнера AppsFlyer. Свяжитесь со своей командой решений для партнеров через виджет поддержки.
   * [Рекомендуется] <Anchor target="_blank" href="/marketers/ru/docs/set-up-appsflyer-preload-referrer-attribution">AppsFlyer referrer</Anchor>: обратитесь к своему PDM за инструкциями по интеграции.
   * <Anchor target="_blank" href="/marketers/ru/docs/measure-preload-campaigns-with-google-play-install">Google Play auto-install (PAI)</Anchor>: настройте информацию о медиаисточнике в Google Play Referrer API для кампаний PAI, используя следующие параметры UTM: `utm_source=play-auto-installs&utm_medium=preload&utm_campaign=brandnamepai_int`. Например: `utm_source=play-auto-installs&utm_medium=preload&utm_campaign=xiaomipai_int`.
3. Свяжитесь с командой решений для партнеров AppsFlyer через виджет поддержки чтобы завершить интеграцию и при необходимости настроить постбэки.  
   **Примечание**: Узнайте, какие макросы постбэков поддерживаются для метода предварительной загрузки в <Anchor target="_blank" href="/marketers/ru/docs/measure-preload-campaigns-with-google-play-install#постбэки-для-партнеров-по-предварительной-загрузке">Google PAI</Anchor> и <Anchor target="_blank" href="/partners/ru/docs/postback-macros-for-ad-networks">AppsFlyer referrer/файле манифеста Android</Anchor>.

<div data-zendesk-anchors="organic-search-attribution=%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8 h_01HQFFB20SKDVW1X3ECMZCZQW0=%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B0%D0%BD%D0%B8%D0%B8 set-up-preload-attribution=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%BF%D1%80%D0%B5%D0%B4%D0%B2%D0%B0%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8 h_01HQFFB20S6KJH3PBF5N2190TJ=%D0%BD%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%BF%D1%80%D0%B5%D0%B4%D0%B2%D0%B0%D1%80%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B9-%D0%B7%D0%B0%D0%B3%D1%80%D1%83%D0%B7%D0%BA%D0%B8" />
