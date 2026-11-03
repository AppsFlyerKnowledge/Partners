---
title: API схемы CV SKAN для рекламных сетей
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2023-03-05T14:40:58Z'
  id: 11705009866001
  locale: ru
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/ru/articles/11705009866001
---
> **Краткий обзор**. Просмотрите схему CV SKAN, сопоставленную рекламодателем.

## API схемы CV SKAN для рекламных сетей

С помощью атрибуции SKAdNetwork (SKAN) рекламодатели оценивают качество пользователей, устанавливая значения конверсии (CV) на основе активности пользователей после установки в определенные периоды (окна). <Anchor target="_blank" href="/marketers/ru/docs/skadnetwork-skan-solution-guide">Подробнее о SKAN</Anchor>

iOS сообщает CV через постбэки, отправленные рекламной сети, разместившей объявление. Начиная с iOS 15 рекламодатели также могут указать iOS отправлять постбэки непосредственно в AppsFlyer.

Этот API предоставляет рекламным сетям сопоставление CV с событиями и значениями атрибуции. Рекламные сети используют его для декодирования получаемых ими постбэков.

API возвращает данные в виде вложенного JSON. Схема для каждого приложения своя. Сопоставления для CV содержатся в массиве conversion\_value\_mapping.

Чтобы использовать API, попросите своего разработчика следовать инструкциям <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">API схемы CV SKAN для рекламных сетей</Anchor>. Для получения списка ключей и их описания нажмите 200 в симуляторе.

**Внимание**:

* Диапазон значений CV:
  * SKAN 4 окно 1 точное значение: 0-63.
  * SKAN 4 окна 1, 2 и 3 приблизительное значение: низкое, среднее или высокое.
  * SKAN 3 и ниже: 0-63
* Рекламодатели могут в любое время изменить сопоставление CV.
* Вы, рекламная сеть, должны ежедневно запрашивать этот API, чтобы убедиться, что у вас есть самая актуальная схема.

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=api-%D1%81%D1%85%D0%B5%D0%BC%D1%8B-cv-skan-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9" />
