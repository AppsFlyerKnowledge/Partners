---
title: Спецификация ссылок атрибуции для рекламных сетей
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Ad Networks
    - Data Management
  created_at: '2021-12-06T10:31:00Z'
  edited_at: '2026-08-18T00:39:28Z'
  id: 4412938154513
  locale: ru
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ru/articles/4412938154513
---
> **Краткий обзор.** Рекламные сети, интегрированные с AppsFlyer, указывают свою ссылку на атрибуцию в соответствии с этой статьей.

<div id="attribution-links-for-ad-networks" />

## Ссылки атрибуции для рекламных сетей

Ссылки атрибуции используются для того, чтобы уведомить AppsFlyer о вовлечении пользователя в рекламу путем клика. В самом простом виде ссылка атрибуции размещается за рекламой, поэтому, нажимая на рекламу, пользователь нажимает на ссылку атрибуции.

<div id="attribution-model" />

### Модель атрибуции

Что происходит на пути от первого клика или просмотра до атрибуции установки или события и далее.

<Image align="center" alt="appsflyer-attribution-model-for-partners.png" src="https://files.readme.io/3f7536b15513a38dde0cdd82c889fc299a094a99339901cafcd6cd06c323b005-17990516210449.png" />

1. Пользователь кликает на баннер или на ссылку в предложении.
2. Баннер или ссылка перенаправляют пользователя на ссылку атрибуции AppsFlyer. В ссылку атрибуции добавляются данные, собранные во время клика.
3. Мы собираем информацию из ссылки атрибуции и сохраняем ее в своей базе данных.
4. Происходит установка и приложение открывается в первый раз. Интегрированный в приложение SDK AppsFlyer отправляет запрос на наши серверы с информацией об устройстве, на котором установлено данное приложение.
5. Мы сопоставляем эти сведения с нашей базой данных по кликам, используя свои **методы атрибуции**:
   * **Сопоставление рефералов**  
     Это уникальный метод атрибуции для устройств Android. Когда пользователь нажимает ссылку и перенаправляется в Google Play, Google Play присваивает ему уникальный идентификатор реферера Referrer ID. Когда происходит установка, мы получаем этот идентификатор с устройства. Затем мы сопоставляем его с записями Google Play.
   * **Сопоставление идентификатора устройства**  
     Мы сопоставляем идентификатор устройства (IDFA для iOS или GAID для Android), полученный при клике, с идентификатором устройства, на котором выполняется установка.
   * <Anchor target="_blank" href="/marketers/ru/docs/appsflyer-attribution-model#probabilistic-modeling">**Вероятностное моделирование**</Anchor>

   Подробнее о <Anchor target="_blank" href="/marketers/ru/docs/appsflyer-attribution-model">методах атрибуции</Anchor>.

   Мы ищем реферер, идентификатор устройства и точки данных вероятностного моделирования (в указанном порядке) в нашей базе данных кликов. Если совпадение найдено, установка атрибутируется клику. Если нет, установка считается органической загрузкой.
6. После атрибуции установки мы отправляем в рекламную сеть постбэк с данными о конверсии.

Как следует из этого процесса, для получения информации от вас мы используем ссылки атрибуции, а для отправки информации вам — постбэки.

<div id="note" />

> 📘 **Примечание**
>
> Если вы используете сторонние инструменты performance-маркетинга, такие как TUNE, CAKE или Affise, см. <Anchor target="_blank" href="/partners/ru/docs/platforms-for-ad-networks">инструкции для конкретной платформы</Anchor>.

<div id="attribution-link-template" />

### Шаблон ссылки атрибуции

Ссылка атрибуции (ссылка в баннере / предложении) может выглядеть так:

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={clickid}&advertising_id={gaid}&af_siteid={affiliate_id}&af_cost_model=CPI&af_cost_value={cost_value}&af_cost_currency={currency}&c={Campaign}&af_ad_type={AdType}&af_adset={Adset}&af_ad={Ad}&is_incentivized={true\false}&expires={timestamp}&signature={signature}
```

`https://app.appsflyer.com/` — это конечная точка AppsFlyer, `com.yourapp` — идентификатор приложения, а `pid=mediaName_int` — уникальное имя медиа-источника, которое мы присваиваем вашей рекламной сети.

Эта часть ссылки неизменна, от вас ничего не требуется.

Объяснение структуры ссылки:

* Значения после '=' внутри `{} — это макросы, заполняемые вами при нажатии и отправляемые в AppsFlyer. При подготовке шаблона замените значения в скобках {}` на имена параметров.
* Присваивание имен макросам не имеет значения при условии, что ваша система заменяет их фактическими и правильными значениями. Параметры перед знаком «=» являются заполнителями, которые использует AppsFlyer, чтобы мы знали, какие значения вы нам отправляете.
* Для интеграции с AppsFlyer,пришлите нам по электронной почте шаблон ссылки атрибуции с именами ваших макросов.

Параметры, перечисленные в следующей таблице, следует считать рекомендуемым минимумом. Мы поддерживаем более широкий набор параметров. Вы должны предоставить нам столько информации о клике, сколько соберете. См. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#параметры-ссылки-атрибуции">список параметров ссылки атрибуции</Anchor>.

<div id="recommended-minimum-attribution-link-parameters" />

#### Рекомендуемые минимальные параметры ссылки атрибуции

| Параметр | Описание |
| --- | --- |
| `&clickid={clickid}` | Click ID — это уникальный идентификатор для каждого клика, совершаемого в вашей рекламной сети. |
| `&advertising_id={gaid}` или  <br />`&idfa={IDFA}` | Идентификатор устройства, на котором совершается клик (GAID для Android и IDFA для Apple). |
| `&c={campaign}` | Имя кампании, заданное рекламодателем. |
| `&af_siteid={publisher_id}` | Идентификатор издателя или партнера, принесшего клик. |
| `&af_ad_type={search_text}` | Тип рекламы. Вы можете использовать одно из следующих принятых обозначений:  <br />search\_text  <br />banner  <br />interstitial  <br />video  <br />rewarded\_video  <br />playable  <br />sponsored\_content  <br />audio |
| `&af_adset={adsetid}` | Идентификатор рекламного блока  — предоставляется рекламодателем или издателем. Группа объявлений — это промежуточный уровень в иерархии между кампанией и рекламным объявлением. <Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#уровни-детализации-данных">Подробнее</Anchor> |
| `&af_ad={ad_id}` | Имя рекламного объявления (<Anchor target="_blank" href="/marketers/ru/docs/about-link-structure-and-parameters#уровни-детализации-данных">подробнее</Anchor>). |
| `&is_incentivized={true}` | Бонусные кампании (Incentivized) или кампании, не предлагающие бонус за совершение действия (non-incentivized). Параметр может иметь значение true/false. |
| `&af_cost_value={cost_value}` | Стоимость конверсии. Допустимый формат: до 4 знаков после десятичного разделителя.  <br />Используйте ТОЛЬКО цифры. Не добавляйте к ним символы денежных единиц или десятичные запятые, поскольку они не распознаются. Допускаются только десятичные точки, например «56», «2.85» и т. д. |
| `&af_cost_currency={currency}` | Валюта затрат — код валюты (например, USD, EUR). Значение по умолчанию: USD.  <br /><Anchor target="_blank" href="https://en.wikipedia.org/wiki/ISO_4217">Список кодов валют</Anchor>. |
| `&expires={timestamp}` | Временная метка Unix, после которой рекламная сеть не приписывает клик себе. Используется для подписывания кликов, чтобы предотвратить мошенничество с кликами. <Anchor target="_blank" href="/partners/ru/docs/click-signing-for-ad-networks">Узнать больше</Anchor> |
| `&signature={signature}` | Подпись HMAC-SHA256, используемая для проверки клика и предотвращения мошенничества. <Anchor target="_blank" href="/partners/ru/docs/click-signing-for-ad-networks">Узнать больше</Anchor> |

<div data-zendesk-anchors="attribution-links-for-ad-networks=%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 01H8GPNM9XTR602BWRBQ5JV8DT=%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8-%D0%B4%D0%BB%D1%8F-%D1%80%D0%B5%D0%BA%D0%BB%D0%B0%D0%BC%D0%BD%D1%8B%D1%85-%D1%81%D0%B5%D1%82%D0%B5%D0%B9 attribution-model=%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01H8GPNM9XSKS66F02GZQKK8E8=%D0%BC%D0%BE%D0%B4%D0%B5%D0%BB%D1%8C-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01H8GPNM9XBCVVXZ5HFKQZQ79D=%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D1%87%D0%B0%D0%BD%D0%B8%D0%B5 attribution-link-template=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01H8GPNM9XS4JE8B1F6TJGKSBR=%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 recommended-minimum-attribution-link-parameters=%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D1%83%D0%B5%D0%BC%D1%8B%D0%B5-%D0%BC%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8 01H8GPNM9XD0GASJ93PNDGMDE8=%D1%80%D0%B5%D0%BA%D0%BE%D0%BC%D0%B5%D0%BD%D0%B4%D1%83%D0%B5%D0%BC%D1%8B%D0%B5-%D0%BC%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D0%B0%D0%BC%D0%B5%D1%82%D1%80%D1%8B-%D1%81%D1%81%D1%8B%D0%BB%D0%BA%D0%B8-%D0%B0%D1%82%D1%80%D0%B8%D0%B1%D1%83%D1%86%D0%B8%D0%B8" />
