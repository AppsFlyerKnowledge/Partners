---
title: 확률적 모델링 어트리뷰션 - 파트너 가이드
metadata:
  keywords:
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Data Management
  created_at: '2025-10-21T14:32:11Z'
  edited_at: '2026-10-14T10:28:31Z'
  id: 40188089592209
  locale: ko
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/ko/articles/40188089592209
---
> **한눈에 보기:** 앱스플라이어가 결정론적 신호를 사용할 수 없을 때 확률적 어트리뷰션을 적용할 수 있도록 광고 인게이지먼트 데이터를 설정하는 방법을 알아보세요.

<div id="about-probabilistic-modeling" />

## 확률적 모델링 어트리뷰션

앱스플라이어는 플랫폼 제한이나 유저 개인정보 설정으로 인해 IDFA, GAID 또는 리퍼러 데이터와 같은 결정론적 식별자에 액세스할 수 없는 경우, 확률적 모델링을 사용하여 인스톨과 리인게이지먼트 데이터에 귀속시킵니다.

이 방법은 사용 가능한 기기 및 컨텍스트 신호를 평가하여 가장 가능성이 높은 전환 소스를 선택합니다. 이는 광고주가 측정의 연속성을 유지할 수 있으며, 직접적인 식별자가 없어도 어트리뷰션이 합리적으로 확실할 수 있을 때 네트워크가 공로를 인정받도록 보장합니다.

확률적 어트리뷰션의 정확도는 사용 가능한 신호의 품질에 따라 달라집니다. 네트워크가 제공하는 데이터의 강도와 완전성은 귀사의 기여도 분석의 우선순위와 성공률에 직접적인 영향을 미칩니다. 더 나은 데이터는 여러 후보 가운데 해당 후보가 선별되는 데에 직접적인 역할을 합니다.

<div id="when-is-probabilistic-modeling-used" />

### 확률적 모델링은 언제 사용하나요?

앱스플라이어는 다음과 같이 결정론적 데이터를 사용할 수 없는 사례에 확률적 모델링을 자동으로 적용합니다:

* iOS SKAN 흐름(SKAN 설치 후)
* 웹-투-앱 전환
* 크로스 디바이스 경험(예: 데스크톱 광고에 이어 모바일 인스톨)
* 측정 액세스를 제한하는 기기 또는 환경
* 결정론적 어트리뷰션이 불가능한 CTV, PC 또는 콘솔 환경

### 확률적 모델링 흐름이란 무엇인가요?

확률적 모델링은 다음 단계로 구성됩니다:

1. 유저가 파트너 네트워크에서 광고를 클릭하거나 노출합니다.
2. 파트너는 관련 기기 및 컨텍스트 신호가 포함된 앱스플라이어 어트리뷰션 링크 또는 HTTP 헤더를 전송합니다.
3. 앱이 실행될 때 결정론적으로 일치하는 항목을 찾지 못한 경우:
   * 앱스플라이어는 인게이지먼트와 앱 출시 컨텍스트를 평가합니다.
   * 신호가 확률적 기준을 충족하면 해당 참여는 유효한 어트리뷰션 후보가 됩니다.
4. 그런 다음 앱스플라이어의 어트리뷰션 로직이 가장 최근의 우선순위가 높은 매칭을 선택합니다.

> 📘 **참고**
>
> 확률적 모델링은 결정론적 방법보다 우선하지 않습니다. 이러한 방법이 실패할 때만 적용됩니다.

## 확률적 모델링을 위한 인게이지먼트 데이터 설정하기

확률적 모델링을 지원하려면 다음을 수행해야 합니다:

* 필수 파라미터가 포함된 어트리뷰션 링크 또는 HTTP 헤더를 구현합니다.
* 표준 <Anchor target="_blank" href="/marketers/ko/docs/about-link-structure-and-parameters?utm_source=chatgpt.com">앱스플라이어 링크 구조를</Anchor> 따르세요.

### 필수 파라미터

앱스플라이어는 확률적 어트리뷰션을 위해 다음 시그널을 사용합니다:

| 파라미터 | 설명 | iOS 예시 | 안드로이드 예시 |
| --- | --- | --- | --- |
| `af_ip` | 인게이지먼트 시점의 유저 IP 주소 | `192.168.0.12` | `192.0.2.45` |
| `af_model` | 기기 모델 식별자 | `iPhone14,1` | `SM-G991B` |
| `af_os_version` | 전체 OS 버전 | `17.5.0` | `13` |
| `af_language` | 기기 언어 설정 | `en-US` | `he-IL` |
| `af_ua` | 유저 에이전트 문자열(브라우저 또는 웹뷰) | `Mozilla/5.0 (iPhone; CPU iPhone OS 17_5_1 like Mac OS X)...` | `Mozilla/5.0 (Linux; Android 13; SM-G991B)...` |

> 📘 **참고**
>
> 어트리뷰션 링크에 파라미터가 누락된 경우, 앱스플라이어는 가능한 경우 HTTP 헤더에서 해당 파라미터를 추출하려고 시도합니다.

### 모범 활용 사례

* 표준 링크 구조를 사용합니다: 모든 파라미터는 쿼리 문자열 또는 HTTP 헤더를 통해 전달되어야 합니다.
* 네트워크가 제공하는 데이터의 강도와 완전성은 귀사의 기여도 분석의 우선순위와 성공률에 직접적인 영향을 미칩니다. 더 나은 데이터는 여러 후보 가운데 해당 후보가 선별되는 데에 직접적인 역할을 합니다.
* 신호 강도의 우선순위를 정하세요: 여러 후보가 존재하는 경우, 더 강력하고 가장 최근의 신호가 우선합니다.

<div data-zendesk-anchors="h_01K83JWQ84H0P1WABG939X55KD=%ED%99%95%EB%A5%A0%EC%A0%81-%EB%AA%A8%EB%8D%B8%EB%A7%81-%EC%96%B4%ED%8A%B8%EB%A6%AC%EB%B7%B0%EC%85%98 h_01K83JWQ8412VK2ZN39CQ5TJEZ=%ED%99%95%EB%A5%A0%EC%A0%81-%EB%AA%A8%EB%8D%B8%EB%A7%81%EC%9D%80-%EC%96%B8%EC%A0%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%82%98%EC%9A%94 h_01K83JWQ84GAPWGQMRDYPCKW5S=%ED%99%95%EB%A5%A0%EC%A0%81-%EB%AA%A8%EB%8D%B8%EB%A7%81-%ED%9D%90%EB%A6%84%EC%9D%B4%EB%9E%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%EC%9A%94 h_01K83JWQ84GFYWX9RJFW00Y17F=%EC%B0%B8%EA%B3%A0 h_01K83JWQ84RTTMAB1Y0S8WAE0Q=%ED%99%95%EB%A5%A0%EC%A0%81-%EB%AA%A8%EB%8D%B8%EB%A7%81%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%9D%B8%EA%B2%8C%EC%9D%B4%EC%A7%80%EB%A8%BC%ED%8A%B8-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0 h_01K83JWQ84T02F22K6D7MGKJ14=%ED%95%84%EC%88%98-%ED%8C%8C%EB%9D%BC%EB%AF%B8%ED%84%B0 h_01K83JWQ846RKGG4W8XYW4V65G=%EC%B0%B8%EA%B3%A0-1 h_01K83JWQ84MYQBSEYH86JJF3H8=%EB%AA%A8%EB%B2%94-%ED%99%9C%EC%9A%A9-%EC%82%AC%EB%A1%80" />
