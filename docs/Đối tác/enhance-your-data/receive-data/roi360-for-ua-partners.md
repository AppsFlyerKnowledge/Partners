---
title: ROI360 dành cho các đối tác UA
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
  created_at: '2023-08-12T17:09:08Z'
  edited_at: '2023-09-26T14:06:59Z'
  id: 17735150011921
  locale: vi
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/vi/articles/17735150011921
---
> **Khái quát:** AppsFlyer cung cấp cho các đối tác UA quảng cáo, giao dịch mua hàng trong ứng dụng cũng như dữ liệu đăng ký có thể tự động gia hạn đầy đủ và chính xác thông qua các báo cáo và bài đăng lại. Đối tác có thể nhập thông tin để tối ưu hóa chiến dịch UA.

<div id="introduction" />

## Giới thiệu

AppsFlyer nhận thông tin doanh thu từ cả đối tác và cửa hàng ứng dụng (Apple App Store và Google Play Store). Sau khi được nhận, dữ liệu sẽ trải qua một loạt các bước bao gồm xác thực, chuẩn hóa, phân bổ và làm phong phú thêm các thuộc tính và phương diện bổ sung.  AppsFlyer có thể gửi thông tin cho đối tác UA. Sau quy trình này, AppsFlyer truyền dữ liệu được bổ sung và phân bổ cho đối tác UA. Sau đó, đối tác UA có thể sử dụng thông tin này để tối ưu hóa chiến dịch thu hút người dùng và nâng cao dịch vụ mà họ cung cấp cho nhà quảng cáo.

<div id="what-revenue-types-are-reported-to-the-partners" />

<Accordion title="Các loại doanh thu nào được báo cáo cho các đối tác?">

Ứng dụng tạo ra hai loại doanh thu:

* **Doanh thu quảng cáo:** Doanh thu quảng cáo được tạo bất cứ khi nào quảng cáo được hiển thị trong ứng dụng, chẳng hạn như trong biểu ngữ, quảng cáo xen kẽ và các định dạng khác. Có thể tính doanh thu bất kể phương thức chiến dịch mà nhà quảng cáo được lập hóa đơn theo.
* **Giao dịch mua hàng trong ứng dụng và gói đăng ký tự động gia hạn:** Doanh thu tại cửa hàng được tạo bất cứ khi nào giao dịch mua hàng trong ứng dụng hoặc giao dịch liên quan đến đăng ký được thực hiện.

</Accordion>

<div id="how-does-appsflyer-provide-revenue-signals-to-ua-partners" />

<Accordion title="AppsFlyer cung cấp tín hiệu doanh thu cho đối tác UA bằng cách nào?">

AppsFlyer cung cấp cho đối tác thông tin về quảng cáo trong ứng dụng, giao dịch mua hàng trong ứng dụng và doanh thu đăng ký thông qua các phương thức sau:

* **Báo cáo Tín hiệu UA Doanh thu Quảng cáo**: Báo cáo liệt kê các sự kiện doanh thu quảng cáo được tổng hợp ở cấp thiết bị. Báo cáo có sẵn hàng ngày trong Data Locker và chứa dữ liệu của ngày hôm trước.
* **Đăng lại Doanh thu Quảng cáo**: Mỗi lần lượt hiển thị quảng cáo diễn ra trên thiết bị khách, một đăng lại sẽ được gửi từ AppsFlyer tới đối tác chứa thông tin chi tiết về sự kiện doanh thu quảng cáo đó.
* **Đăng lại Doanh thu Cửa hàng**: Mỗi lần một giao dịch mua hàng hoặc sự kiện doanh thu diễn ra, một đăng lại sẽ được gửi từ AppsFlyer tới đối tác chứa thông tin chi tiết về sự kiện doanh thu đó.

</Accordion>

<div id="set-up-roi360-for-partners" />

## Thiết lập ROI360 cho đối tác

Đối tác cần làm gì để nhận được báo cáo tín hiệu UA cũng như thông tin đăng lại về doanh thu quảng cáo và doanh thu cửa hàng?

<div id="how-to-subscribe-to-the-roi360-ua-signals-report" />

<Accordion title="Cách đăng ký nhận báo cáo Tín hiệu UA ROI360">

Để cho phép đối tác nhận báo cáo qua Data Locker:

* Đối tác phải thực hiện các bước sau trong Data Locker:
  1. <Anchor target="_blank" href="/partners/vi/docs/data-locker-for-partners#set-up-data-locker">Thiết lập Data Locker</Anchor> trong tài khoản đối tác bao gồm kết nối với nhà cung cấp dịch vụ đám mây cũng như định dạng và nội dung của báo cáo.
  2. <Anchor target="_blank" href="/partners/vi/docs/ad-revenue-signals-for-ua-ad-networks#enable-the-ad-revenue-report">Bật báo cáo Tín hiệu UA ROI360</Anchor>.
* Nhà quảng cáo cần phải <Anchor target="_blank" href="/marketers/vi/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">cấp quyền đối tác cho báo cáo</Anchor>.

</Accordion>

<div id="how-to-receive-roi360-postbacks-from-appsflyer" />

<Accordion title="Cách nhận đăng lại ROI360 từ AppsFlyer">

Để nhận được đăng lại từ AppsFlyer, đối tác phải bắt đầu cuộc trò chuyện với nhóm tích hợp đối tác của AppsFlyer. Sau đó, nhóm sẽ định cấu hình các giá trị đăng lại doanh thu trong ứng dụng ROI trong nền tảng AppsFlyer.

Để liên hệ với bộ phận hỗ trợ đối tác của AppsFlyer, vui lòng mở menu **Help** trong bảng điều khiển của bạn và chọn **Contact our team**.

[![alt](https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif)](https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif)

</Accordion>

<div id="roi360-ua-signals-report-for-ua-networks" />

## Báo cáo Tín hiệu UA ROI360 cho Mạng UA

Hàng ngày, báo cáo sẽ cung cấp bản ghi doanh thu CSV/parquet ngày x+1 đầy đủ và chính xác cho bộ chứa S3 của đối tác UA. Mỗi bản ghi là một bản tổng hợp các sự kiện doanh thu quảng cáo ở cấp thiết bị.

Báo cáo Tín hiệu UA không cung cấp dữ liệu theo thời gian thực như tính năng đăng lại doanh thu quảng cáo. Tuy nhiên, báo cáo sẽ chính xác và đầy đủ hơn. Điều này là do giá trị của lượt hiển thị có thể thay đổi theo thời gian. Điều này đặc biệt đúng khi dữ liệu doanh thu ở cấp độ hiển thị dành cho một lượt hiển thị được bán thông qua đấu thầu CPM tiêu chuẩn thay vì đấu thầu theo thời gian thực.

<div id="what-are-the-report-data-sources" />

<Accordion title="Nguồn dữ liệu báo cáo là gì?">

Tùy thuộc vào loại tích hợp của nhà quảng cáo, dữ liệu báo cáo có thể bắt nguồn từ:

1. Tích hợp <Anchor target="_blank" href="/marketers/vi/docs/integrate-the-roi360-ad-revenue-sdk-api">trình kết nối SDK AdRevenue</Anchor>: khách hàng có thể chia sẻ dữ liệu doanh thu ở cấp độ hiển thị do đối tác tải tới thiết bị của khách hàng và sau đó báo cáo cho AppsFlyer gần như theo thời gian thực.
2. Tích hợp cấp thiết bị dựa trên API S2S: khách hàng có thể định cấu hình thông tin xác thực đối tác của họ trong UI AppsFlyer theo đối tác tích hợp và cho phép doanh thu quảng cáo ROI360 thay mặt họ thu thập dữ liệu doanh thu quảng cáo cấp độ thiết bị.
3. Kết hợp cả hai (Tính cập nhật đến Độ chính xác).

   **Lưu ý:** Việc chuyển dữ liệu từ nhà quảng cáo sang AppsFlyer tùy thuộc vào quyền của nhà quảng cáo và liệu nhà quảng cáo có phải là khách hàng nâng cao ROI360 hay không.

</Accordion>

<div id="what-data-processing-is-performed-on-the-report-data" />

<Accordion title="Quy trình xử lý dữ liệu nào được thực hiện đối với dữ liệu báo cáo?">

Doanh thu Quảng cáo ROI360 của AppsFlyer thực hiện những mục sau:

1. Chuẩn hóa dữ liệu
2. Phân bổ cho nguồn truyền thông cài đặt và làm phong phú dữ liệu
3. Tạo sự kiện doanh thu quảng cáo
4. Các sự kiện được tổng hợp ở cấp thiết bị

</Accordion>

<div id="how-is-the-report-data-delivered" />

<Accordion title="Dữ liệu báo cáo được phân phối như thế nào?">

Dữ liệu cấp thiết bị được ghi hàng ngày vào báo cáo trong Data Locker

</Accordion>

<div id="what-is-the-report-data-freshness" />

<Accordion title="Tính cập nhật của dữ liệu báo cáo như thế nào?">

Dữ liệu được ghi hàng ngày vào thư mục h=23 trong bộ chứa Data Locker của bạn lúc 21:00 <Anchor target="_blank" href="/marketers/vi/docs/about-data-freshness-and-timezone-support#daily-processing">giờ UTC</Anchor>.

</Accordion>

<div id="what-are-the-report-fields" />

<Accordion title="Các trường báo cáo là gì?">

| **Trường** | **Lưu ý** |
| --- | --- |
| Phiên bản | Nhãn thời gian Unix tính bằng giây. Ví dụ: 1661315124 |
| app\_id | ID ứng dụng trong nền tảng AppsFlyer |
| install\_time | • Nhãn thời gian lượt cài đặt: YYYY-MM-DD HH:MM:SSVí dụ: 2020-08-16 11:22:33 • Đối với các thiết bị iOS 14+ và người dùng không đồng ý hoặc nếu nhà quảng cáo bật tùy chọn Quyền riêng tư Nâng cao, thì thời gian cài đặt sẽ được làm tròn đến giờ gần nhất. |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Chỉ được điền nếu UA được phân bổ cho đối tác nhận dữ liệu. |
| idfa, idfy, advertising\_id | • Cùng một ID thiết bị, như IDFA, IDFV hoặc advertiser\_id có thể hiển thị trong nhiều hàng nếu có nhiều sự kiện kiếm tiền từ doanh thu quảng cáo. • Đối với các thiết bị iOS 14+ và người dùng không đồng ý hoặc nếu nhà quảng cáo đã bật tùy chọn Quyền riêng tư Nâng cao, thì ID thiết bị này sẽ không hiển thị. |
| platform | Nền tảng thiết bị: iOS, Android hoặc Windows Mobile |
| country | Mã quốc gia sử dụng [ISO 3166 (alpha-2)](https://www.iso.org/iso-3166-country-codes.html) Ví dụ: US, CN |
| original\_url | • Đối với các thiết bị iOS 14+ và người dùng không đồng ý hoặc nếu nhà quảng cáo đã bật tùy chọn Quyền riêng tư Nâng cao, thì ID thiết bị này sẽ không hiển thị. • Chỉ được điền nếu UA được phân bổ cho đối tác nhận dữ liệu. |
| mediation\_network | Mạng lưới trung gian liên kết với (các) lượt hiển thị. <Anchor target="_blank" href="/marketers/vi/docs/roi360-guide-ad-revenue-attribution#closed-beta--ua-signals-for-ad-networks">Xem danh sách các mạng lưới khả thi</Anchor> |
| ad\_unit | Vào Q3 của năm 2023 sắp tới: ad\_unit kiếm tiền được liên kết với (các) lượt hiển thị |
| placement | Vào Q3 của năm 2023 sắp tới: Vị trí đặt quảng cáo kiếm tiền được liên kết với (các) lượt hiển thị |

</Accordion>

<div id="download-the-report-data-sample" />

<Accordion title="Tải xuống mẫu dữ liệu báo cáo">

[Nhấp để tải xuống báo cáo](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv)

</Accordion>

<div id="in-app-ad-revenue-iaa-postbacks" />

## Đăng lại doanh thu quảng cáo trong ứng dụng (IAA)

Đăng lại IAA là phương thức nhập thứ hai mà AppsFlyer sử dụng để gửi thông tin doanh thu cho đối tác. Lợi thế chính của chúng so với báo cáo tín hiệu UA Doanh thu Quảng cáo là tính cập nhật, vì tính năng đăng lại cung cấp tính năng chia sẻ dữ liệu doanh thu IAA gần như theo thời gian thực. Điều này trái ngược với tính cập nhật X+1 (một ngày sau ngày xảy ra sự kiện) được cung cấp thông qua báo cáo tín hiệu UA doanh thu quảng cáo.

Tuy nhiên, tính cập nhật theo thời gian thực kém chính xác hơn so với X+1:

* Dữ liệu đăng lại IAA theo thời gian thực có độ chính xác trung bình kém hơn ±5% so với dữ liệu X+1 của báo cáo tín hiệu UA.
* Dữ liệu đăng lại IAA theo thời gian thực trung bình kém hoàn chỉnh hơn ±7% so với dữ liệu X+1 của báo cáo tín hiệu UA.

<div id="what-are-the-iaa-postback-data-sources" />

<Accordion title="Nguồn dữ liệu đăng lại IAA là gì?">

Dữ liệu cho đăng lại IAA bắt nguồn từ dữ liệu cấp độ Lượt hiển thị mà các đối tác tải lên thiết bị khách. Sau đó, dữ liệu này được chia sẻ với AppsFlyer thông qua trình kết nối SDK Doanh thu Quảng cáo ROI360, được nhà quảng cáo cài đặt trên thiết bị. Trình kết nối cho phép nhà phát triển ứng dụng báo cáo sự kiện hiển thị bao gồm các thông số nhất định như ILRD, đơn vị tiền tệ, nền tảng trung gian và nguồn kiếm tiền.

Việc chuyển dữ liệu từ thiết bị khách của nhà quảng cáo sang AppsFlyer tùy thuộc vào quyền của nhà quảng cáo và liệu nhà quảng cáo có phải là khách hàng nâng cao ROI360 hay không.

</Accordion>

<div id="what-processing-is-performed-on-the-iaa-postback-data" />

<Accordion title="Quy trình xử lý nào được thực hiện đối với dữ liệu đăng lại IAA?">

AppsFlyer ROI360 thực hiện các bước sau cho từng dữ liệu cấp độ hiển thị nhận được:

1. Chuẩn hóa dữ liệu.
2. Phân bổ cho nguồn truyền thông cài đặt và làm phong phú dữ liệu.
3. Tạo sự kiện **af\_ad\_revenue**.

</Accordion>

<div id="how-is-the-postback-data-delivered" />

<Accordion title="Dữ liệu đăng lại được phân phối như thế nào?">

Sự kiện được gửi tới đối tác thông qua cấu hình đăng lại hiện có giữa đối tác và AppsFlyer dưới dạng thông số bổ sung.

</Accordion>

<div id="in-app-purchase-iap-postbacks" />

## Đăng lại giao dịch mua hàng trong ứng dụng (IAP)

Tính năng đăng lại giao dịch mua hàng trong ứng dụng ROI360 mang lại nhiều lớp chính xác trong báo cáo bằng cách trước tiên xác thực từng giao dịch, loại bỏ giao dịch trùng lặp, sau đó khấu trừ hoa hồng cửa hàng và thuế bán hàng.

<div id="what-are-the-iap-postback-data-sources" />

<Accordion title="Nguồn dữ liệu đăng lại IAP là gì?">

Dữ liệu cho đăng lại IAP bắt nguồn từ:

1. Dữ liệu cấp giao dịch được đọc bởi trình kết nối SDK Mua hàng ROI360 bất cứ khi nào có giao dịch mua hàng diễn ra trong ứng dụng hoặc sự kiện đăng ký tự động gia hạn trên thiết bị.
2. Mọi **thông báo từ máy chủ của App Store và Google Play (RTDN)** đến cũng được xử lý theo logic kinh doanh giao dịch mua hàng và doanh thu đăng ký của AppsFlyer:
   * Các thông báo liên quan đến giao dịch được báo cáo trước đó qua trình kết nối SDK sẽ được xác thực và xử lý.
   * Thông báo về các giao dịch không xác định không được báo cáo vào AppsFlyer

   **Lưu ý:** Việc chuyển dữ liệu từ nhà quảng cáo sang AppsFlyer tùy thuộc vào quyền của nhà quảng cáo và liệu nhà quảng cáo có phải là khách hàng nâng cao ROI360 hay không.

</Accordion>

<div id="what-data-processing-is-performed-on-the-iap-postback-data" />

<Accordion title="Quy trình xử lý dữ liệu nào được thực hiện đối với dữ liệu đăng lại IAP?">

AppsFlyer ROI360 thực hiện các bước sau cho từng dữ liệu cấp độ giao dịch nhận được:

1. AppsFlyer **xác thực giao dịch mua hoặc đăng ký với cửa hàng có liên quan** để đảm bảo đó không phải là giao dịch gian lận.
   * Sau khi xác thực thành công, AppsFlyer ghi nhật ký giao dịch mua hoặc gói đăng ký.
   * Nếu xác thực biên lai không thành công, sự kiện sẽ hiển thị trong báo cáo dữ liệu thô đối với sự kiện trong ứng dụng bị chặn (dành cho người đăng ký Protect360).
2. AppsFlyer đảm bảo rằng các giao dịch không bị trùng lặp, bao gồm cả những giao dịch liên quan đến chia sẻ gia đình trên iOS.
3. AppsFlyer tính toán dữ liệu doanh thu ròng có tính đến hoa hồng và thuế của cửa hàng (**Doanh thu Thực**).
4. AppsFlyer tạo sự kiện mua hàng nội bộ hoặc sự kiện trong vòng đời cho giao dịch được xác thực và xử lý.

</Accordion>

<div id="how-is-the-postback-delivered" />

<Accordion title="Đăng lại được phân phối như thế nào?">

Sự kiện IAP được gửi tới đối tác thông qua tích hợp đăng lại hiện có giữa đối tác và AppsFlyer.

</Accordion>

<div id="what-are-the-iap-events" />

<Accordion title="Sự kiện IAP là gì?">

Khách hàng ROI360 có thể chia sẻ tên sự kiện mang lại doanh thu sau:

**Tên sự kiện**

| **Tên của sự kiện** | **Mô tả** |
| --- | --- |
| af\_purchase | Được ghi lại khi người dùng thực hiện giao dịch mua |
| af\_purchase\_refund | Ghi lại khi giao dịch mua được hoàn lại tiền |
| af\_ars\_trial\_converted | Được ghi lại khi bắt đầu gia hạn trả phí đầy đủ sau thời gian dùng thử |
| af\_ars\_subscription\_started | Được ghi lại khi bắt đầu gói đăng ký giảm giá hoặc trả phí đầy đủ |
| af\_ars\_subscription\_resumed | Được ghi lại khi một gói đăng ký trả phí đầy đủ tiếp tục hoạt động lại sau khi khách hàng bỏ đăng ký hoặc gói đăng ký được hoàn tiền |
| af\_ars\_subscription\_refunded | Được ghi lại khi một người đăng ký được hoàn tiền |
| af\_ars\_subscription\_renewed | Được ghi lại khi gói đăng ký được gia hạn tự động |
| af\_ars\_subscription\_xgraded | Được ghi lại khi người đăng ký nâng cấp, hạ cấp hoặc chuyển đổi chéo sang một sản phẩm khác |

</Accordion>

<div data-zendesk-anchors="introduction=gi%E1%BB%9Bi-thi%E1%BB%87u 01H7T1DS6SNC7X8GX4DGXT4GC0=gi%E1%BB%9Bi-thi%E1%BB%87u 01H7T1DS6TYHE3A4XWBDNHCFCZ=what-revenue-types-are-reported-to-the-partners 01H7T1DS6T82RWQ4BBWNPQ6BT2=how-does-appsflyer-provide-revenue-signals-to-ua-partners set-up-roi360-for-partners=thi%E1%BA%BFt-l%E1%BA%ADp-roi360-cho-%C4%91%E1%BB%91i-t%C3%A1c 01H7T1DS6TDA8CX1ZF3GGE4EHB=thi%E1%BA%BFt-l%E1%BA%ADp-roi360-cho-%C4%91%E1%BB%91i-t%C3%A1c 01H7T1DS6T0QFB6K6R78PMVVB2=how-to-subscribe-to-the-roi360-ua-signals-report 01H7T1DS6TBNJBBR6M98RTVMFF=how-to-receive-roi360-postbacks-from-appsflyer roi360-ua-signals-report-for-ua-networks=b%C3%A1o-c%C3%A1o-t%C3%ADn-hi%E1%BB%87u-ua-roi360-cho-m%E1%BA%A1ng-ua 01H7T1DS6T93844DMZY744ECQE=b%C3%A1o-c%C3%A1o-t%C3%ADn-hi%E1%BB%87u-ua-roi360-cho-m%E1%BA%A1ng-ua 01H7T1DS6T4AF6GTETE6HZMYF7=what-are-the-report-data-sources 01H7T1DS6TDNTYDY4JF70F40SV=what-data-processing-is-performed-on-the-report-data 01H7T1DS6T94V4674AMNVCD4T6=how-is-the-report-data-delivered 01H7T1DS6T4F0QV5VE8XZVV1RY=what-is-the-report-data-freshness 01H7T1DS6TYER08FGK9GDKHFEG=what-are-the-report-fields 01H7T1DS6TH98NT4KGKPR7DRDM=download-the-report-data-sample inapp-ad-revenue-iaa-postbacks=%C4%91%C4%83ng-l%E1%BA%A1i-doanh-thu-qu%E1%BA%A3ng-c%C3%A1o-trong-%E1%BB%A9ng-d%E1%BB%A5ng-iaa 01H7T1DS6T0CN30EC97VARN80D=%C4%91%C4%83ng-l%E1%BA%A1i-doanh-thu-qu%E1%BA%A3ng-c%C3%A1o-trong-%E1%BB%A9ng-d%E1%BB%A5ng-iaa 01H7T1DS6TCA8338NAD9Q8CJWW=what-are-the-iaa-postback-data-sources 01H7T1DS6TQ2G43HSQMH8Y6Q4H=what-processing-is-performed-on-the-iaa-postback-data 01H7T1DS6TQZA3W9KE3783G9G1=how-is-the-postback-data-delivered inapp-purchase-iap-postbacks=%C4%91%C4%83ng-l%E1%BA%A1i-giao-d%E1%BB%8Bch-mua-h%C3%A0ng-trong-%E1%BB%A9ng-d%E1%BB%A5ng-iap 01H7T1DS6TH8AV2ZTY3M8ZXPYA=%C4%91%C4%83ng-l%E1%BA%A1i-giao-d%E1%BB%8Bch-mua-h%C3%A0ng-trong-%E1%BB%A9ng-d%E1%BB%A5ng-iap 01H7T1DS6TGF4XEMD4CRBD8QS2=what-are-the-iap-postback-data-sources 01H7T1DS6T9W85F40QQ2497RNW=what-data-processing-is-performed-on-the-iap-postback-data 01H7T1DS6VAPRMCGZ9YCPTA9EQ=how-is-the-postback-delivered 01H7T1DS6VKE2G6XR02VF4TWH4=what-are-the-iap-events" />
