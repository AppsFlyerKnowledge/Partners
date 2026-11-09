---
title: 애드 네트워크 비용 가져오기
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Gray
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2019-10-20T06:03:13Z'
  edited_at: '2026-10-14T10:29:32Z'
  id: 360002868097
  locale: ko
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ko/articles/360002868097
---
> **한눈에 보기:** 애드 네트워크가 CSV 파일을 통해 광고주의 캠페인 비용을 앱스플라이어에 직접 보고하는 방법을 알아보세요.

<div id="cost-import-for-ad-networks" />

## 애드 네트워크 비용 가져오기

<Image align="center" alt="AdspendIngestion.jpg" src="https://files.readme.io/e870005c5f20531a2d06cc78b47a82a8a1f730f2c04728f5d0a5674c1c70129a-24507313816337.jpg" />

<div id="overview" />

#### 개요

* 다음과 같이 광고 지출 세부 정보가 포함된 CSV 파일을 준비합니다:
  * 지출 날짜
  * 앱 ID (앱이 동일한 소유자에게 속한 경우 파일당 여러 개의 앱 허용)
  * 미디어 소스(파일당 하나만 허용)
  * 캠페인 이름
  * 지출 금액
  * [선택 사항] 지역
  * [선택 사항] 통화(기본 USD)
* 앱스플라이어의 애드 네트워크 계정을 사용하여 이메일/파일 업로드를 통해 파일을 앱스플라이어에 제출합니다.   
  **참고:**
  * 처음으로 파일을 제출하기 전에 광고주가 애드 네트워크에 비용 가져오기 권한을 부여해야 합니다. 이 작업은 각 앱마다 한 번씩 수행해야 하며 매우 간단한 과정입니다.
  * 일단 업로드된 파일은 되돌릴 수 없습니다.
* 파일에서 오류가 발견되지 않았는지 모니터링하고 확인합니다.

<div id="submitting-ad-spend-files-for-ad-networks" />

### 애드 네트워크용 광고 지출 파일 제출

* 업로드하거나 이메일을 사용하여 광고 지출 파일을 수집합니다.
* [모범 사례] 처음에는 업로드 방법을 사용하십시오. 이는 CSV 서식 지정 문제를 더 쉽게 해결할 수 있습니다.
* 애드 네트워크는 에이전시 비용 데이터를 가져올 수 없습니다. 광고주만이 해당 데이터를 가져올 수 있습니다.

<div id="submission-by-file-upload" />

#### 파일 업로드를 통한 제출

**비용 가져오기 파일을 업로드하여 제출하려면 다음과 같이 하세요:**

1. [연동하는 앱마다 이 작업을 한 번씩 수행] <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-permissions-for-ad-networks">광고주에게 비용 가져오기 권한 부여를 요청합니다</Anchor>.
2. <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#prepare-csv-file-with-cost-data">이 형식과 스키마를 사용하여 CSV 파일을 준비합니다</Anchor>.
3. 여기를 클릭하여 <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">앱스플라이어 애드 네트워크 계정에 로그인</Anchor>합니다.
4. <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#upload-file">파일을 업로드하고 수집(ingest)합니다</Anchor>.
5. 앱스플라이어 대시보드에서 수집 상태(ingestion)를 모니터링합니다:

   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">상태</Anchor>
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#matched-rows">일치하는 행</Anchor>
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">비용 가져오기 작업</Anchor>
6. 추가 절차:
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">이전 수집 내용 덮어쓰기</Anchor>
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">되돌리기(취소)</Anchor>

<div id="submission-by-email" />

#### 이메일로 제출

**비용 가져오기 파일을 이메일로 제출하려면 다음과 같이 하세요:**

1. [연동하는 앱마다 이 작업을 한 번씩 수행] <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-permissions-for-ad-networks">광고주에게 비용 가져오기 권한 부여를 요청합니다</Anchor>.
2. <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#prepare-csv-file-with-cost-data">이 형식과 스키마를 사용하여 CSV 파일을 준비합니다</Anchor>.
3. 비용 가져오기 토큰이 없는 경우(파일을 이메일로 보낼 때 필요):
   * 여기를 클릭하여 <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">앱스플라이어 애드 네트워크 계정에 로그인</Anchor>하세요.
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#token-for-email-import">광고 지출 토큰을 받습니다.</Anchor> 참고: 모든 광고주에게 동일한 토큰이 사용됩니다.
4. <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#email-file">이메일</Anchor>로 파일 제출
5. 앱스플라이어는 수집이 성공적으로 이루어졌는지 또는 문제가 발생했는지가 기록된 상태 보고서를 이메일로 전송합니다. **참고**: 상태 메일을 받지 못한 경우 <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">비용 가져오기 대시보드</Anchor>를 확인하세요.
6. 앱스플라이어 대시보드에서 수집 상태(ingestion)를 모니터링합니다:

   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">상태</Anchor>
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#matched-rows">일치하는 행</Anchor>
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">비용 가져오기 작업</Anchor>
7. 추가 절차:
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">이전 수집 내용 덮어쓰기</Anchor>
   * <Anchor target="_blank" href="/marketers/ko/docs/import-cost-data#cost-import-dashboard">되돌리기(취소)</Anchor>

<div data-zendesk-anchors="ad-spend-ingestion-for-ad-networks=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EB%B9%84%EC%9A%A9-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0 h_01HX94WSX07YEG40X66TMRFJGA=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EB%B9%84%EC%9A%A9-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0 overview=%EA%B0%9C%EC%9A%94 h_01HX94WSX0HR2KTGRT7MQ481Y6=%EA%B0%9C%EC%9A%94 submitting-ad-spend-files-for-ad-networks=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%9A%A9-%EA%B4%91%EA%B3%A0-%EC%A7%80%EC%B6%9C-%ED%8C%8C%EC%9D%BC-%EC%A0%9C%EC%B6%9C h_01HX94WSX0G429FTHKYCG07BB9=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%9A%A9-%EA%B4%91%EA%B3%A0-%EC%A7%80%EC%B6%9C-%ED%8C%8C%EC%9D%BC-%EC%A0%9C%EC%B6%9C submission-by-file-upload=%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%A0%9C%EC%B6%9C h_01HX94WSX0ENTJEDMXWRHDCP0D=%ED%8C%8C%EC%9D%BC-%EC%97%85%EB%A1%9C%EB%93%9C%EB%A5%BC-%ED%86%B5%ED%95%9C-%EC%A0%9C%EC%B6%9C submission-by-email=%EC%9D%B4%EB%A9%94%EC%9D%BC%EB%A1%9C-%EC%A0%9C%EC%B6%9C h_01HX94WSX0HVTMFQQ0NMW0VSKP=%EC%9D%B4%EB%A9%94%EC%9D%BC%EB%A1%9C-%EC%A0%9C%EC%B6%9C" />
