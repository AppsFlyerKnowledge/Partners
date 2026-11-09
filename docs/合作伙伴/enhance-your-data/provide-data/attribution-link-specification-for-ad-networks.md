---
title: Attribution link specification for ad networks
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
  edited_at: '2026-10-13T01:47:04Z'
  id: 4412938154513
  locale: zh-cn
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/zh-cn/articles/4412938154513
---
> **At a glance:** Ad networks integrating with AppsFlyer specify their attribution link according to this article.

## Attribution links for ad networks

Attribution links are used to notify AppsFlyer that a user engaged with an ad by clicking it. In its simplest form, the attribution link is placed behind an ad so that when a user clicks on an ad they are clicking on an attribution link.

### Attribution model

What happens on the journey from a first click or impression to the attribution of an install or an event—and beyond.

<Image align="center" alt="appsflyer-attribution-model-for-partners.png" src="https://files.readme.io/3f7536b15513a38dde0cdd82c889fc299a094a99339901cafcd6cd06c323b005-17990516210449.png" />

1. A user clicks on a banner or an offer link.
2. The banner or link redirects the user to an AppsFlyer attribution link. The AppsFlyer attribution link is then populated with information that is collected during the click.
3. We gather the information from the attribution link and store it in our database.
4. An install occurs and the app is opened for the first time. The AppsFlyer SDK inside the app calls our servers with the information about the device that the app is installed on.
5. We match this data to our click database using our **Attribution methods**:
   * **Referrer matching**  
     This attribution method is unique to Android devices. When a user clicks on a link and gets redirected to Google Play, Google Play gives it a unique Referrer ID. When the install takes place, we collect this ID from the device. Then we match it with Google Play records.
   * **Device ID matching**  
     We match the Device ID (IDFA for the iOS or GAID for the Android device) collected upon the click to the ID of the device that performs the install.
   * <Anchor target="_blank" href="/marketers/zh/docs/appsflyer-attribution-model#probabilistic-modeling">**Probabilistic modeling**</Anchor>

   More about <Anchor target="_blank" href="/marketers/zh/docs/appsflyer-attribution-model">attribution methods</Anchor>.

   We look for the referrer, device ID, and probabilistic modeling data points (in that order) in our click database. If we find a match, we attribute the install to the click. If not, we attribute the install to an organic download.
6. Once the install is attributed, we send a postback with the conversion details to the ad network.

As it follows from this flow, we use attribution links to get information from you, and postbacks to send the information back to you.

> 📘 **Note**
>
> If you use third-party performance marketing tools such as TUNE, CAKE, or Affise, see <Anchor target="_blank" href="/partners/zh/docs/platforms-for-ad-networks">platform-specific instructions</Anchor>.

### Attribution link template

The attribution link (the link behind the banner/offer) can look like this:

```http
https://app.appsflyer.com/com.yourapp?pid=mediaName_int&clickid={clickid}&advertising_id={gaid}&af_siteid={affiliate_id}&af_cost_model=CPI&af_cost_value={cost_value}&af_cost_currency={currency}&c={Campaign}&af_ad_type={AdType}&af_adset={Adset}&af_ad={Ad}&is_incentivized={true\false}&expires={timestamp}&signature={signature}
```

`https://app.appsflyer.com/` is the AppsFlyer endpoint, `com.yourapp` is App ID, and `pid=mediaName_int` is a unique media source name that we assign to your Ad Network.

This part of the link is static and doesn’t require anything from you.

Link structure explanation:

* The values after ‘=’ inside `{} are macros populated by you when the click takes place and gets sent to AppsFlyer. When you prepare your template, replace the value in brackets {}` with your parameter names.
* Macro naming has no significance provided that your system replaces them with the actual and correct values. The parameters before the ‘=’ sign are placeholders used by AppsFlyer so we know which values you are sending us.
* To integrate with AppsFlyer, send us the attribution link template by email with your macro names.

Regard the parameters listed in the table that follows as the recommended minimum. We support a larger set of parameters. You should share with us as much information on the click as you collect. See the <Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters#归因链接参数">list of attribution link parameters</Anchor>.

#### Recommended minimum attribution link parameters

| Parameter | Description |
| --- | --- |
| `&clickid={clickid}` | Click ID is a unique click identifier for each click that happens on your ad network. |
| `&advertising_id={gaid}` or  <br />`&idfa={IDFA}` | The device ID of the device on which the click takes place (GAID for Android and IDFA for Apple). |
| `&c={campaign}` | The campaign name, as defined by the advertiser. |
| `&af_siteid={publisher_id}` | Publisher or affiliate ID of the publisher or affiliate that drove the click. |
| `&af_ad_type={search_text}` | Ad Type. You can use one of the following name conventions:  <br />search\_text  <br />banner  <br />interstitial  <br />video  <br />rewarded\_video  <br />playable  <br />sponsored\_content  <br />audio |
| `&af_adset={adsetid}` | Adset Name - provided by the advertiser/publisher. Adset is an intermediate level in the hierarchy between Campaign and Ad. <Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters#数据粒度级别">See more</Anchor> |
| `&af_ad={ad_id}` | Ad Name (<Anchor target="_blank" href="/marketers/zh/docs/about-link-structure-and-parameters#数据粒度级别">see more</Anchor>) - provided by the advertiser/publisher |
| `&is_incentivized={true}` | Incentivized or non-incentivized campaigns (can be true/false) |
| `&af_cost_value={cost_value}` | Conversion Cost Value - supports up to 4 digits after the decimal point.  <br />Make sure to use ONLY numerical digits (use the decimal point if needed), e.g., "56", "2.85" etc. |
| `&af_cost_currency={currency}` | Cost Currency — currency code (e.g. USD, EUR). The default value is USD.  <br /><Anchor target="_blank" href="https://en.wikipedia.org/wiki/ISO_4217">List of currency codes</Anchor>. |
| `&expires={timestamp}` | Unix timestamp after which the ad network doesn't claim the click. Used for click signing to prevent click fraud. <Anchor target="_blank" href="/partners/zh/docs/click-signing-for-ad-networks">Learn more</Anchor> |
| `&signature={signature}` | HMAC-SHA256 signature used to validate the click and prevent fraud. <Anchor target="_blank" href="/partners/zh/docs/click-signing-for-ad-networks">Learn more</Anchor> |

<div data-zendesk-anchors="01H8GPNM9XTR602BWRBQ5JV8DT=attribution-links-for-ad-networks 01H8GPNM9XSKS66F02GZQKK8E8=attribution-model 01H8GPNM9XBCVVXZ5HFKQZQ79D=note 01H8GPNM9XS4JE8B1F6TJGKSBR=attribution-link-template 01H8GPNM9XD0GASJ93PNDGMDE8=recommended-minimum-attribution-link-parameters" />
