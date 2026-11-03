---
title: 에이전시를 위한 데이터 락커 리포트
metadata:
  keywords:
    - Agencies
    - Partners
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Data Locker
    - Agencies
  created_at: '2022-03-02T09:16:03Z'
  edited_at: '2026-10-14T10:33:36Z'
  id: 4543231254417
  locale: ko
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/ko/articles/4543231254417
---
> **간단히 보기**: 요약: 본 기사에 기재한 리포트는 사용자(에이전시)가 데이터 락커에서 사용할 수 있습니다. 데이터를 공유하려면 먼저 광고주(앱 소유자)가 본 기사에 설명된 대로 데이터 액세스 권한을 부여해야 합니다.

## 에이전시를 위한 데이터 락커 리포트

다음의 데이터 공유 원칙이 적용됩니다.

* 논오가닉 데이터 af\_prt 필드를 사용하여 사용자에게 어트리뷰트된 트래픽을 결정합니다.
* 오가닉 데이터
* 데이터 락커
* [출시 예정] 다른 파트너에게 어트리뷰트된 논오가닉 데이터.

### 리포트당 필요한 권한(광고주가 부여)

리포트당 필요한 권한은 다음 표에 기재되어 있습니다. 에이전시인 사용자는 광고주에게 다음 절차를 수행하도록 요청해야 합니다.

**광고주가 에이전시에게 권한을 부여하는 방법:**

1. 이 절차는 필요한 권한을 가진 광고주 팀 구성원이 수행해야 합니다.
2. 앱스플라이어에서 **콜라보레이트** > **연동 파트너**로 이동합니다.
3. 연동 파트너(에이전시)를 선택합니다.
4. **권한** 탭으로 이동합니다.
5. 가이드로 다음 표를 사용하여 데이터 액세스 권한을 부여합니다. 데이터 공유 정책에 따라 권한을 부여해야 합니다.

#### 에이전시에게 제공되는 리포트

<table><thead><tr><th><span>리포트 유형 (주제)</span></th><th>필수 권한(광고주가 부여)</th><th><span>데이터 최신성\*</span></th></tr></thead><tbody><tr><td><a href="/marketers/ko/docs/cohort-analytics-via-data-locker" target="_blank">코호트 통합</a></td><td><ul><li>리텐션 및 코호트 리포트에 액세스</li><li>오가닉 집계 데이터에 접근</li><li>[출시 예정] 다른 파트너에게 어트리뷰트됨</li></ul></td><td>일일 </td></tr><tr><td><a href="/marketers/ko/docs/cohort-analytics-via-data-locker" target="_blank">코호트 사용자 인입</a></td><td><ul><li>리텐션 및 코호트 리포트에 액세스</li><li>오가닉 집계 데이터에 접근</li><li>[출시 예정] 다른 파트너에게 어트리뷰트됨</li></ul></td><td>일일</td></tr><tr><td><a href="/marketers/ko/docs/cohort-analytics-via-data-locker" target="_blank">코호트 리타게팅</a></td><td><ul><li>리텐션 및 코호트 리포트에 액세스</li><li>오가닉 집계 데이터에 접근</li><li>[출시 예정] 다른 파트너에게 어트리뷰트됨</li></ul></td><td>일일 </td></tr><tr><td colspan="3"><p>\* 축약형을 위한 열쇠어</p><p><strong><span>일별</span></strong><span>:</span></p><ul><li><span>리포트는 h=23 폴더로 스트리밍됩니다.</span></li><li><span>이 리포트는 선행하는 날의 h=23 폴더에서 보통 09:00-12:00 UTC에 사용 가능합니다.</span></li><li><span>예를 들어, 월요일에 발생한 데이터에 대한 리포트는 월요일 h = 23 폴더에 있습니다.</span></li><li> <span>데이터는 화요일에 사용할 수 있습니다.</span><ul><li>집약 캠페인 성과 리포트  </li><li> </li><li>차단된 클릭 및 노출, 그리고 실패한 클릭 서명의 경우: 07:00 UTC 이후. </li></ul></li></ul></td></tr></tbody></table>

<div data-zendesk-anchors="data-locker-reports-for-agencies=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4-%EB%A6%AC%ED%8F%AC%ED%8A%B8 h_01HE7RC367DWWDQHAVFSKV6VEK=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%9D%BD%EC%BB%A4-%EB%A6%AC%ED%8F%AC%ED%8A%B8 permissions-required-per-report-granted-by-the-advertiser=%EB%A6%AC%ED%8F%AC%ED%8A%B8%EB%8B%B9-%ED%95%84%EC%9A%94%ED%95%9C-%EA%B6%8C%ED%95%9C%EA%B4%91%EA%B3%A0%EC%A3%BC%EA%B0%80-%EB%B6%80%EC%97%AC h_01HE7RC367NTSVESAYE69Q7NJY=%EB%A6%AC%ED%8F%AC%ED%8A%B8%EB%8B%B9-%ED%95%84%EC%9A%94%ED%95%9C-%EA%B6%8C%ED%95%9C%EA%B4%91%EA%B3%A0%EC%A3%BC%EA%B0%80-%EB%B6%80%EC%97%AC reports-available-to-agencies=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EC%97%90%EA%B2%8C-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EB%A6%AC%ED%8F%AC%ED%8A%B8 h_01HE7RC368VVM3SMDN7S8YV6DY=%EC%97%90%EC%9D%B4%EC%A0%84%EC%8B%9C%EC%97%90%EA%B2%8C-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EB%A6%AC%ED%8F%AC%ED%8A%B8" />
