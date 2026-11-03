---
title: 앱 스토어로 사용자 리디렉션하기
metadata:
  keywords:
    - clicks
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
  created_at: '2018-04-30T08:08:25Z'
  edited_at: '2026-10-14T10:39:15Z'
  id: 360000807629
  locale: ko
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ko/articles/360000807629
---
> **한눈에 보기:** 광고가 송출된 후 사용자를 애플 앱 스토어로 리디렉션하는 방법에 대해 알아보고, 앱스플라이어에 인게이지먼트 데이터를 전송하는 방법을 배워봅니다.

## 개요

앱스플라이어는 다음과 같이 다양한 방식으로 어트리뷰션을 위한 인게이지먼트 데이터(클릭수와 노출수)를 수집합니다.

* 사용자가 광고를 **클릭**하면 [앱스플라이어로 리디렉션](#앱스플라이어를-통해-리디렉션된-사용자들)된 뒤, 앱 스토어로 이동합니다.
* 사용자가 광고를 **클릭하거나 조회한 뒤**, [바로 앱 스토어로 이동](#애드-네트워크가-직접-보낸-사용자)되고, **디바이스에서 앱스플라이어에 어트리뷰션 링크가 전송됩니다**.

이 두 경우에 모두, 정규 <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters">어트리뷰션 링크 구조와 파라미터들</Anchor>이 사용됩니다.

> 📘 **참고**
>
> SRN의 어트리뷰션에 대해서는, 전문 API를 통해 데이터가 수신됩니다

## 앱스플라이어를 통해 리디렉션된 사용자들

광고를 클릭하면, 사용자는 먼저 앱스플라이어로 이동되며, 그 다음으로는 다음과 같은 흐름에 따라 앱 스토어로 리디렉션됩니다:

1. 사용자가 앱스플라이어로 리디렉션됩니다
2. 앱스플라이어가 클릭을 기록합니다
3. 앱스플라이어가 사용자를 앱 스토어로 이동시킵니다
4. 사용자가 앱을 설치합니다
5. 앱스플라이어가 설치를 어트리뷰션합니다

## 애드 네트워크가 직접 보낸 사용자

광고를 클릭할 때 사용자는 리디렉션 횟수를 최소화하면서 애드 네트워크에 의해 바로 앱 스토어로 이동됩니다:

1. 사용자가 앱 스토어로 이동됩니다
2. 애드 네트워크가 디바이스로부터 인게이지먼트 데이터를 앱스플라이어에 전달합니다
3. 사용자가 앱을 설치합니다
4. 앱스플라이어가 설치를 어트리뷰션합니다

### 앱스플라이어로 인게이지먼트 데이터 전송하기

사용자를 앱 스토어로 직접 보내는 것은 리디렉션 횟수를 줄여 사용자 경험을 개선합니다. 이를 통해 설치의 정확한 어트리뷰션을 보장하며, 고품질의 트래픽 확보가 가능합니다.

애드 네트워크는 **사용자의 디바이스를 통해** 앱스플라이어에 클릭 및 노출만을 보고할 수 있습니다.

#### 리디렉션 전송 타이밍

애드 네트워크의 어트리뷰션 및 수익 손실을 방지하기 위해서, 클릭 및 노출은 앱스플라이어에 실시간으로 전송되어야 합니다:

* **노출 URL**은 광고가 송출된 직후에 보고되어야 합니다
* **클릭 URL**은 사용자가 광고를 클릭한 직후에 보고되어야 합니다

<div data-zendesk-anchors="overview=%EA%B0%9C%EC%9A%94 h_01HDY3CARC0A9504XGMJHYHGY4=%EA%B0%9C%EC%9A%94 h_01HDY3CARCZK06C5XHEQFQYA8W=%EC%B0%B8%EA%B3%A0 redirect-users-via-appsflyer=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EB%A5%BC-%ED%86%B5%ED%95%B4-%EB%A6%AC%EB%94%94%EB%A0%89%EC%85%98%EB%90%9C-%EC%82%AC%EC%9A%A9%EC%9E%90%EB%93%A4 01HDYFGYW3FDR64C54KKPXRHDF=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EB%A5%BC-%ED%86%B5%ED%95%B4-%EB%A6%AC%EB%94%94%EB%A0%89%EC%85%98%EB%90%9C-%EC%82%AC%EC%9A%A9%EC%9E%90%EB%93%A4 send-users-directly-by-the-ad-network=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EA%B0%80-%EC%A7%81%EC%A0%91-%EB%B3%B4%EB%82%B8-%EC%82%AC%EC%9A%A9%EC%9E%90 01HDYFH8ZCSP2SN4ZYQQVG7EED=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EA%B0%80-%EC%A7%81%EC%A0%91-%EB%B3%B4%EB%82%B8-%EC%82%AC%EC%9A%A9%EC%9E%90 send-engagement-data-to-appsflyer=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EB%A1%9C-%EC%9D%B8%EA%B2%8C%EC%9D%B4%EC%A7%80%EB%A8%BC%ED%8A%B8-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EC%86%A1%ED%95%98%EA%B8%B0 h_01HDYGSEFHVF8ZD43XCVNGYT9N=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EB%A1%9C-%EC%9D%B8%EA%B2%8C%EC%9D%B4%EC%A7%80%EB%A8%BC%ED%8A%B8-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%A0%84%EC%86%A1%ED%95%98%EA%B8%B0 timing-of-sending-redirects=%EB%A6%AC%EB%94%94%EB%A0%89%EC%85%98-%EC%A0%84%EC%86%A1-%ED%83%80%EC%9D%B4%EB%B0%8D h_01HDXXDDXDEP43YHE3GF81BSKV=%EB%A6%AC%EB%94%94%EB%A0%89%EC%85%98-%EC%A0%84%EC%86%A1-%ED%83%80%EC%9D%B4%EB%B0%8D" />
