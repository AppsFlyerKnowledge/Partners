---
title: Turn on test app integration for ad networks
metadata:
  keywords:
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
  created_at: '2021-05-22T15:56:20Z'
  edited_at: '2026-10-13T01:49:17Z'
  id: 360020713538
  locale: ko
  section: Ad network integration testing
  section_id: 6551070667537
  url: https://support.appsflyer.com/hc/ko/articles/360020713538
---
> **At a glance:** Ad networks performing integration testing must turn on app integration (activation).

## Test apps for ad networks (iOS and Android)

Ad networks after setting up integration and postbacks must test integration using AppsFlyer test apps. Before testing, the ad network must activate the app integration and enable additional ad network permissions as needed. The activation is performed once per app.

| Test app type | App name or ID |
| --- | --- |
| <Anchor target="_blank" href="/partners/ko/docs/getting-started-onboarding-guide-for-ad-networks#2부-광고주-앱을-사용하여-테스트하세요">Android</Anchor> | com.appsflyer.adNetworkTest |
| <Anchor target="_blank" href="/partners/ko/docs/ios-integration-testing-for-ad-networks">iOS</Anchor> | id1543229303 |
| <Anchor target="_blank" href="/partners/ko/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor> | <ul><li>id888707085</li><li>id888707086</li><li>id888707087</li></ul> |

### Activation procedure

Use the procedure that follows to activate the integration for a given test app. Perform the procedure once per app.

**To activate integration and grant permissions to a test app**:

1. In AppsFlyer, select a test app from those listed in the previous table.
2. In AppsFlyer, from the side menu, select **Collaborate** > **Partner Integrations** > **Active Integrations**.
3. Select your ad network.
4. **To activate integration with the app**:  
   1. Go to the **Integration** tab.
   2. Turn on **Activate Partner**.
   3. Click **Save integration**.
5. **To grant permissions**:
   1. Go to the **Permissions** tab.
   2. Turn on **Configure integration**.
   3. Turn on **Configure in-app event postbacks.**
   4. Click **Save permissions**.

<div data-zendesk-anchors="h_01HKA15VM7FM69X0AZ1V2H5XPJ=test-apps-for-ad-networks-ios-and-android h_01HKA15VM7J47374WMRG5132GN=activation-procedure" />
