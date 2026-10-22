---
title: venedash integration with AppsFlyer
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
  created_at: '2020-04-24T21:20:47Z'
  edited_at: '2026-09-09T13:56:49Z'
  id: 360007705617
  locale: en-us
  section: Platforms for ad networks
  section_id: 6551055575185
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/360007705617-venedash-integration-with-AppsFlyer
---
> **At a glance:** Send attribution data from AppsFlyer to venedash. AppsFlyer can send venedash both install and in-app event data.

## venedash integration setup

* If you have an integration with AppsFlyer, contact us using the <Anchor target="_blank" href="https://af-static-content.s3.eu-west-1.amazonaws.com/marketplace/static/logo/Help_GIF_Final-min.gif">partner assistant widget</Anchor>.
* If you don't have an integration with AppsFlyer, complete the ad Partners Registration application <Anchor target="_blank" href="https://www.appsflyer.com/partners-registration/">here</Anchor>.

**To enable the integration with AppsFlyer:**

1. In **AppsFlyer**, go to **Collaborate** > **Partner Integrations > Active Integrations** and select Venedash from the partner list.
2. In the **Integration** tab, enable **Activate partner**.
3. Go to the **Attribution Link** tab and generate an attribution link with the following mandatory parameters:

   

| AppsFlyer parameter | venedash parameter | Description |
| --- | --- | --- |
| &clickid= | `{#ydrid#}` | Request ID of each user session |
| ⁡\_siteid= | `{#ydr_pid#}` | ID of the affiliate who promotes the offer |
| &advertising\_id | `{#android_adv#}` | Android device ID |
| &idfa= | `{#iosidfa#}` | ​iOS device ID |

   Note that the pid parameter is filled by the Appsflyer team.  
   Example:

   ```
   https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#ydrid#&af_siteid=#ydr_pid#&advertising_id=advertising_id&idfa=#iosidfa#">https://app.appsflyer.com/com.appsflyer?pid=mediaName_int&clickid=#ydrid#&af_siteid=#ydr_pid#&advertising_id=advertising_id&idfa=#iosidfa#
   ```

   Learn more about <Anchor target="_blank" href="/marketers/docs/about-link-structure-and-parameters">attribution link parameters</Anchor>.
4. In Venedash, create an offer and paste the AppsFlyer attribution link in the Destination URL field.

   ![venedash-destination_url-en_us.png](https://files.readme.io/2a284eab8d25f57f1bfa2981e2d86bf16bce16b64b61858fdb819d5ac14eac20-360016242798.png)

<div data-zendesk-anchors="h_01HKW87R2DGCXHZSVSV9D9203Z=venedash-integration-setup" />
