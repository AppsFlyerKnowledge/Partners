---
title: 애드 네트워크를 위한 비용 공유 옵션
metadata:
  keywords:
    - clicks
    - Partner
    - cost
    - Ad Networks
    - Partners
    - ad spend
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2020-09-07T13:50:24Z'
  edited_at: '2026-10-14T10:34:10Z'
  id: 360012893658
  locale: ko
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ko/articles/360012893658
---
> **요약:** 앱스플라이어 애드 네트워크 파트너에게 제공되는 비용 공유 방법을 비교합니다.

## 앱스플라이어와 광고주가 비용을 공유하는 방법

광고주는 ROI, 청구서 및 마케팅 예산 배분 결정을 위해 앱스플라이어를 정보 소스로 사용합니다. 애드 네트워크가 눈에 띄려면 앱스플라이어와 비용 데이터를 공유해야 합니다. 비용 데이터가 없는 네트워크는 앱스플라이어 대시보드 목록의 하단에 표시됩니다.

애드 네트워크가 앱스플라이어와 비용을 공유하는 방법

* **InCost API**: 데이터를 앱스플라이어로 푸시합니다.
* **Cost API**: 앱스플라이어가 데이터를 가져옵니다.
* **Cost Import**: 비용 데이터 파일을 앱스플라이어에 업로드하거나 전송합니다.
* **클릭당 비용**: 어트리뷰션 링크를 클릭할 때마다 네트워크에서 비용을 보고합니다.

### 애드 네트워크를 위한 비용 배지

![CostBadge.jpg](https://files.readme.io/6b660b68b932802f7982a3beb3a155ecc350de1b4cb3baede6e84ef0d704388c-360011247338.jpg)

* 비용 배지는 <Anchor target="_blank" href="/marketers/ko/docs/partner-integrations#partner-details-and-performance">파트너 세부 정보 페이지</Anchor>에 표시되며, InCost 또는 Cost API를 사용하는 파트너임을 강조합니다.
* 배지는 파트너가 비용 처리 역량이 있는 파트너임을 인증합니다.
* 내부 분석과 광범위한 유저 설문 조사에 따르면, 광고주는 항상 새로운 파트너를 찾고 있습니다. 비용 배지가 있는 파트너는 더 두드러져 보일 가능성이 큰데, 이는 광고주가 ROI 분석을 기반으로 마케팅 성과를 파악하고 싶어 하기 때문입니다.

### 애드 네트워크에 제공되는 비용 리포팅 옵션

| 옵션 | 비용 배지 자격 | 옵션 특성 |
| --- | --- | --- |
| <Anchor target="_blank" href="/partners/ko/docs/incost-api-for-ad-networks">InCost API</Anchor> | ✓ | 애드 네트워크는 InCost 리포팅을 설정하는 시점을 완전히 제어할 수 있습니다.<br /><br />InCost는 다음과 같은 기능을 제공합니다:<ul><li>모든 비용 모델 지원</li><li>정확하고 신뢰할 수 있음</li><li>완전 자동화</li><li>애드 네트워크 파트너가 제어하는 항목:<ul><li>데이터 업로드 방식</li><li>업로드 시점(데이터 최신성) 평가</li></ul></li><li>광고주는 앱스플라이어 대시보드에서 파트너에게 비용 데이터를 업로드할 권한을 승인합니다.</li></ul>**제한사항**:<br /><br />앱스플라이어 에이전시 계정은 지원되지 않습니다. |
| Cost API | ✓ | <ul><li>모든 비용 모델 지원</li><li>정확함</li><li>파트너가 앱스플라이어에서 비용 데이터를 일부 제어할 수 있음</li><li>앱스플라이어의 에이전시 계정 비용 지원</li><li>광고주는 앱스플라이어 대시보드에 파트너 자격 증명을 제공함</li><li>데이터 새로 고침 빈도: 하루 6회, 4시간마다</li></ul>**제한 사항**:<br /><br />연동은 앱스플라이어의 우선순위에 따라 결정됩니다. |
| <Anchor target="_blank" href="/partners/ko/docs/cost-import-for-ad-networks">비용 가져오기</Anchor><br /><br />(파일 업로드) | 아니요 | <ul><li>애드 네트워크 파트너:<ul><li>엔지니어링 리소스로 자동화할 수 없는 경우 수동으로 데이터 업로드</li><li>데이터 업로드 시점을 제어</li><li>앱스플라이어에서 비용 데이터를 일부 제어</li><li>연동은 앱별로 이루어집니다. 광고주는 앱스플라이어 대시보드에서 파트너가 비용 데이터를 업로드할 수 있도록 권한을 부여합니다.</li><li>캠페인 ID가 아닌 캠페인 이름을 기준으로 어트리뷰션 데이터를 매칭합니다.</li></ul></li></ul>**제한사항**:<ul><li>앱스플라이어 에이전시 계정은 지원되지 않습니다.</li><li>이메일을 통한 자동 업로드 시 실패 위험</li></ul> |
| <Anchor target="_blank" href="/partners/ko/docs/cost-reporting-on-the-attribution-link-for-ad-networks">클릭당 비용</Anchor><br /><br />(어트리뷰션 링크에서) | 아니요 | <ul><li>CPI 캠페인을 위한 빠른 솔루션</li><li>거의 실시간</li><li>광고주가 SKAdNetwork를 사용하는 경우 클릭당 비용이 덜 정확할 수 있습니다.</li></ul>**제한 사항**:<ul><li>CPI 비용 모델로 제한됨</li><li>링크에서 잘못된 데이터가 전송되면 소급하여 변경할 수 없습니다.</li><li>리타겟팅은 지원되지 않음</li><li>클릭당 보고된 비용은 SKAdNetwork 대시보드에서 사용할 수 있을 때 표시됩니다.</li></ul> |

<div data-zendesk-anchors="sharing-cost-with-appsflyer-and-advertisers=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EC%99%80-%EA%B4%91%EA%B3%A0%EC%A3%BC%EA%B0%80-%EB%B9%84%EC%9A%A9%EC%9D%84-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95 h_01HN0A1ER3MNZM508ZCG9KP26P=%EC%95%B1%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B4%EC%96%B4%EC%99%80-%EA%B4%91%EA%B3%A0%EC%A3%BC%EA%B0%80-%EB%B9%84%EC%9A%A9%EC%9D%84-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95 cost-badge-for-ad-networks=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%B9%84%EC%9A%A9-%EB%B0%B0%EC%A7%80 h_01HN0A1ER4K1V4479W5SXCEC30=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EB%A5%BC-%EC%9C%84%ED%95%9C-%EB%B9%84%EC%9A%A9-%EB%B0%B0%EC%A7%80 reporting-cost-options-available-to-ad-networks=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%97%90-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EB%B9%84%EC%9A%A9-%EB%A6%AC%ED%8F%AC%ED%8C%85-%EC%98%B5%EC%85%98 h_01HN0A1ER4Y128ZHJERXS6A8ET=%EC%95%A0%EB%93%9C-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EC%97%90-%EC%A0%9C%EA%B3%B5%EB%90%98%EB%8A%94-%EB%B9%84%EC%9A%A9-%EB%A6%AC%ED%8F%AC%ED%8C%85-%EC%98%B5%EC%85%98" />
