---
title: Postback retries
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
  edited_at: '2026-10-13T01:47:53Z'
  id: 360001376085
  locale: zh-cn
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/zh-cn/articles/360001376085
---
> **At a glance:** Learn how postback retries work in AppsFlyer and how integrated partners can configure their postback mechanisms.

## Introduction

Postbacks to partners are a critical part of the integration between AppsFlyer and our partners. Since any system can experience momentary issues in its responsiveness, AppsFlyer is able to retry failed postbacks.

## Important information

<div id="when-does-appsflyer-retry-a-failed-postback" />

<Accordion title="When does AppsFlyer retry a failed postback?">

A postback is retried when the response indicates an error on the receiving server-side 5XX errors.

</Accordion>

<div id="how-often-does-appsflyer-retry-a-failed-postback" />

<Accordion title="How often does AppsFlyer retry a failed postback?">

The first failed postback is retried up to four additional times in 15-minute intervals. In total, a single postback can be sent up to five times.

</Accordion>

<div id="can-retried-postbacks-be-identified-in-postback-reports" />

<Accordion title="Can retried postbacks be identified in postback reports?">

The raw data Postback report: "Postback Retry". The first postback sent has a blank value in this column. Any retried postback contains the value TRUE in this column.

</Accordion>

<div id="how-can-a-partner-identify-the-total-eventual-failed-postbacks-in-the-postback-report" />

<Accordion title="How can a partner identify the total eventual failed postbacks in the Postback report?">

A postback that has four TRUE values listed in the "Postback Retry" column and also contains error codes in the Postback HTTP Response Code is a postback that has entirely failed to have been sent to the partner.

</Accordion>

<div id="is-there-anything-special-a-partner-should-consider-about-retried-postbacks" />

<Accordion title="Is there anything special a partner should consider about retried postbacks?">

If the postback has reached your system and has been processed successfully, but there was an error or delay in sending a response—this is considered a failed postback, and retries are sent after 15 minutes. This can cause duplication on the partner's end. The partner must implement a deduplication mechanism on their end.

</Accordion>

<div id="are-postback-retries-automatically-enabled-for-all-partners" />

<Accordion title="Are postback retries automatically enabled for all partners?">

No. If a partner wants to retry failed postbacks, they should reach out to their PDM to enable this feature.

</Accordion>
