---
title: Rejected attribution postbacks to integrated partners
metadata:
  keywords:
    - fraud
    - Ad Networks
    - Partners
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Mobile Attribution
    - Ad Networks
  created_at: '2017-09-19T07:03:47Z'
  edited_at: '2024-08-13T10:50:27Z'
  id: 115004744123
  locale: en-us
  section: Receive data
  section_id: 6551235995281
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/115004744123-Rejected-attribution-postbacks-to-integrated-partners
---
**At a glance:** Integrated partners get postbacks of rejected installs and in-app events due to fraud or non-compliance with validation rules.

## Rejected attribution postbacks relating to fraud and validation rules

**Terminology**:

* **Fraud events:** install and in-app events blocked by Protect360
* **Non-compliant events**: installs and in-app events that don't comply with validation rules
* **Rejected events**: Fraud events and non-compliant validation rule events
* **Attribution corrected install:** A hijacked install identified and blocked, whose attribution is subsequently corrected and attributed to the genuine media source.

**Postbacks**

* Integrated partners get rejected event postbacks in real-time.
* There are no fraud event postbacks for in-app events of attribution corrected installs.
* Rejected event postbacks are sent to the endpoint specified by the partner for both install and rejected event postbacks, with additional parameters being:  
  * Block reason
  * Reject sub-reason
  * Is-rejected
  * Reject reason value (when available). For example: `reject_reason=site_blacklist&reject_reason_value="1123456"&is_rejected=1`

The following table lists the reject reason, reject reason value, and an explanation of the reject reason:

| Reject reason | Reject reason value | User can configure | Explanation |
| --- | --- | --- | --- |
| ctit\_anomalies | The measured click-to-install time in seconds | **x** | CTIT anomalies are attributed clicks that have been blocked based on unreasonable CTIT (click to install time). |
| store\_install\_validation | N/A | **x** | Installs that failed validation from the App Store |
| site\_blacklist | Site ID | **x** | Installs coming from Site IDs that AppsFlyer blocked due to a high density of fraudulent activity. Determined by our internal algorithms. |
| bots | N/A | **x** | Blocked install attempts made by Bots |
| click\_flood | Site ID or empty | **x** | Installs coming from clusters blocked by AppsFlyer due to a large number of installs with a high CTIT and low conversion rate. |
| behavioral\_anomalies | N/A | **x** | Behavioral anomalies being install fraud blocked due to inconsistent and abnormal post-install behavior. |
| install\_hijacking | N/A | **x** | Install hijacking being attributed clicks blocked based on unreasonable click and install time, based on Google Play Server-Side API. |
| validation\_bots | Rule names or empty | **✓** | Customer-defined rule. |
| validation\_hijacking | Rule names | **✓** | Customer-defined rule. |
| ai\_layer | N/A | **x** | AI models are utilized to analyze vast amounts of data points, enhancing detection capabilities for identifying fraudulent device and installation activities. |

#### Reject reasons for in-app events

| Reject reason | Reject reason value | Explanation |
| --- | --- | --- |
| Inherits from install | Inherits from install | Initial install identified as fake based on <Anchor target="_blank" href="/marketers/docs/protect360-raw-data-reports#blocked-reasons">install</Anchor> or<Anchor target="_blank" href="/marketers/docs/protect360-raw-data-reports#blocked-reasons"> denylisted</Anchor> level reason |
| inapps\_bots | fake\_device\_parameters | AppsFlyer algorithm detects fraud |
| validation\_inapps | invalid\_event\_name | Based on requested or manually defined validation rule |
| validation\_inapps | invalid\_event\_value | Based on requested or manually defined validation rule |
| validation\_inapps | Rule name/s | Based on manually-defined rules |

> 🚧 **Important!**
>
> * To be able to distinguish between postbacks for legitimate events and rejected postbacks, you must configure the <Anchor target="_blank" href="/partners/docs/postback-macros-for-ad-networks#macrosinstalls-in-app-events-and-rejected-events">rejected postback macros</Anchor>.
> * To enable rejected postbacks for Advance Privacy you must first append the following parameters to the <Anchor target="_blank" href="/partners/docs/self-serve-integration-management-for-ad-networks#default-postback">Default postback</Anchor>:
>   * `is-rejected`
>   * `blocked-reason`
>   * `blocked-sub-reason`
>   * `blocked-reason-value`
> * When the parameters above are added to both the Default postback and the Advanced Privacy postback, rejected install/in-app event postbacks are enabled.

<div data-zendesk-anchors="h_01J5597AMDVWR2KTANSF7Y7T4P=rejected-attribution-postbacks-relating-to-fraud-and-validation-rules reject-reasons-for-inapp-events=reject-reasons-for-in-app-events h_01J5597AMDHT5GJQN7QJZKV41F=reject-reasons-for-in-app-events h_01J5597AMD29TAZSKZS9WTFSM5=important" />
