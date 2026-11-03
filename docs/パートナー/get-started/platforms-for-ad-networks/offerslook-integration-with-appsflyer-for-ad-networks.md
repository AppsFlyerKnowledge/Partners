---
title: Offerslook integration with AppsFlyer for ad networks
metadata:
  keywords:
    - Offerslook
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
  created_at: '2016-05-31T08:47:36Z'
  edited_at: '2026-10-01T00:41:28Z'
  id: 209074606
  locale: ja
  section: Platforms for ad networks
  section_id: 6551055575185
  url: https://support.appsflyer.com/hc/ja/articles/209074606
---
> **At a glance:** Learn how ad networks that use Offerslook can integrate with AppsFlyer and receive install attribution data.

To initiate integration, send to AppsFlyer:

1. Your Attribution Link

   ```http
   https://networkname.offerstrack.net/index.php?offer_id={offer_id}&aff_id={aff_id}
   ```
2. Your Postback (for installs)  

   ```http
   https://networkname.offerstrack.net/advBack.php?click_id={click_id}&adv_id={adv_id}
   ```

## Creating your Attribution Link

The attribution link consists of the below AppsFlyer base attribution link and additional macros added by the ad-network.

See below AppsFlyer’s base attribution link with a detailed explanation per macro:

| AppsFlyer Base URL | Description | Offerslook |
| --- | --- | --- |
| http://app.appsflyer.com | AppsFlyer end point |  |
| app\_id | Application unique ID – dynamic value changed per app promoted |  |
| pid= | Media source name concatenated with \_int to identify integrated networks |  |
| c= | Campaign name | `{offer_id}` |

See below for an example of an attribution Link once you have added additional Offerslook macros:

```http
  https://app.appsflyer.com/com.
  
  appsflyer?pid=mediaName_int&
  
  clickid={click_id}&af_siteid={
  
  aff_id}&advertising_id={ga_id}
  
  &idfa={idfa}
```

For a complete list of AppsFlyer parameters, click <Anchor target="_blank" href="/marketers/ja/docs/about-link-structure-and-parameters">here</Anchor>.

Available Macros on AppsFlyer Attribution Links

The following macros are available to use within the generated link:

| **Macro Name** | **Description** | **Offerslook** |
| --- | --- | --- |
| pid | Media source name - provided by AppsFlyer and should not be changed |  |
| c | Campaign name |  |
| clickid | The Ad network unique click identifier | `{click_id}` |
| af\_siteid | Ad network publisher ID | `{aff_id}` |

#### New Macros

The new set of macros adds a number of additional parameters in a clear, standardized, and structured manner. We strongly recommend using these macros before reverting to the af\_sub1-5 macros.

| **Macro Name** | **Description** | **Offerslook** |
| --- | --- | --- |
| af\_c\_id | Campaign ID - provided by the advertiser | `{adv_sub1}<br /><br />{adv_sub2}<br /><br />{adv_sub3}` |
| af\_adset | Adset name - provided by the advertiser. Adset is an intermediate level in the hierarchy between **Campaign** and **Ad**. |  |
| af\_adset\_id | Adset ID |  |
| af\_ad | Ad name |  |
| af\_ad\_id | Ad ID |  |
| af\_ad\_type | Ad type - use anything that "describes" the ad format (examples: video or banner, medium size or big size) |  |
| af\_channel | The channel through which the ads are distributed (for example: YouTube vs Google Search) |  |
| af\_keywords | Keywords list for text-targeted campaigns |  |
| af\_cost\_model | Cost model - CPI is currently supported and the default model. CPC and CPA values are also valid. | `{pricing_type}` |
| af\_cost\_currency | Currency code (example: USD) | `{currency}` |
| af\_cost\_value | Cost value | `{revenue}` |

**Android Specific Macros**

| **Macro Name** | **Description** | **Offerslook** |
| --- | --- | --- |
| android\_id | Device Android\_id - Requires ad network support | `{android_id}` |
| sha1\_android\_id | Device Android\_id hashed with SHA1 - Requires ad network support |  |
| advertising\_id | Google Advertising ID - Requires ad network support | `{ga_id}` |
| sha1\_advertising\_id | Google Advertising ID hashed with SHA1 - Requires ad network support |  |
| af\_r | For out of store only - Target redirect URL |  |
| sha1\_el | Used for desktop to mobile attribution - email hashed with SHA1, requires ad network support |  |

**iOS Specific Macros**

| **Macro Name** | **Description** | **Offerslook** |
| --- | --- | --- |
| idfa | Apple Advertiser ID - should be provided using upper case format, requires ad network support | `{idfa}` |
| sha1\_idfa | Apple Advertiser ID hashed with SHA1 - Requires ad network support |  |
| mac | Device mac address - Requires ad network support | `{mac}` |
| sha1\_mac | Device mac address hashed with SHA1 - Requires ad network support |  |

## Creating your Install Postbacks

Following is a step-by-step explanation of how to create your install postbacks using the Offerslook platform:

1. Create or select an offer that uses the Postback w/Transaction ID protocol
2. In the details section of the offer page, click the link labeled "tracking"
3. Copy the postback URL appearing in the field labeled postback URL
4. Remove the offer\_id parameter and value from the postback url to change the postback from a specific postback into a global postback

Global Install Postback:

`http://{networkname}.offerstrack.net/advBack.php?click_id={click_id}&adv_id={adv_id}`

`networkname` is the domain name provided by Offerslook.

**Finalizing your Registration**

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

<div data-zendesk-anchors="01JFT1JFND230EFDBRTWNKXKSH=creating-your-attribution-link 01JFT1JFP8T3HF5GQBR19YHQW5=new-macros 01JFT1JFP9BMZM99TKDR58FNZP=creating-your-install-postbacks" />
