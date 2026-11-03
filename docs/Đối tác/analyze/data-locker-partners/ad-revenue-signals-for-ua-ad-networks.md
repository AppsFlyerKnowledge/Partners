---
title: Dấu hiệu doanh thu quảng cáo cho mạng quảng cáo
metadata:
  keywords:
    - Ad Network
    - Partner
    - ad revenue
    - Data Locker
    - Ad Networks
    - Partners
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-michael-talapov
    - ROI360
    - Ad Networks
  created_at: '2021-06-21T13:39:13Z'
  edited_at: '2023-09-11T11:03:05Z'
  id: 4402898251409
  locale: vi
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/vi/articles/4402898251409
---
> **Khái quát:** Các mạng quảng cáo phụ trách thu hút người dùng có thể nhận dữ liệu về doanh thu quảng cáo và sử dụng dữ liệu đó để tối ưu hóa các chiến dịch UA của khách hàng.

Mạng quảng cáo có thể nhận các báo cáo qua Data Locker với thông tin doanh thu quảng cáo có giá trị liên quan đến người dùng. Những người dùng này có thể được thu hút đến từ các chiến dịch được phân bổ thông qua mạng quảng cáo hoặc có thể đến từ một nguồn truyền thông khác.

Sau đó, các mạng quảng cáo có thể nhập dữ liệu này vào các thuật toán tối ưu và nhắm mục tiêu theo chiến dịch, đồng thời sử dụng dữ liệu này để cải thiện chiến dịch ROAS dựa trên cái nhìn toàn diện về doanh thu do UA tạo ra.

## Thiết lập báo cáo Doanh thu Quảng cáo trong Data Locker

Bạn cần hoàn thành các hoạt động sau để truy cập báo cáo Doanh thu Quảng cáo trong Data Locker:

* Mạng quảng cáo phải <Anchor target="_blank" href="/partners/vi/docs/data-locker-for-partners#set-up-data-locker">giới thiệu Data Locker cho Đối tác</Anchor>.
* Mạng quảng cáo phải [cấu hình cài đặt đầu ra báo cáo](#configure-the-report-output-settings) và [bật tính năng báo cáo Doanh thu quảng cáo](#enable-the-ad-revenue-report).
* Các nhà quảng cáo phải cho phép các mạng quảng cáo xem báo cáo. Để biết các hướng dẫn dành cho nhà quảng cáo, hãy xem <Anchor target="_blank" href="/marketers/vi/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">Cho phép mạng quảng cáo nhận dữ liệu doanh thu quảng cáo.</Anchor>

<div id="configure-the-report-output-settings" />

<Accordion title="Cấu hình cài đặt đầu ra báo cáo">

Để định cấu hình cài đặt đầu ra báo cáo, hãy làm theo các bước bên dưới:

1. Trong AppsFlyer, đi đến **Integration->Data Locker.**
2. Trong khu vực **Report output settings**, bật **Send reports**.
3. Đặt thuộc tính đầu ra của tập tin báo cáo.
   * Định dạng báo cáo (Parqet/CSV).
   * Phương thức nén báo cáo (Snappy/GZIPO/Không nén).
   * Số hàng tối đa trong một tập tin.
4. Xem lại đường dẫn dự kiến của đầu ra tập tin báo cáo. Đường dẫn được đặt theo các cài đặt kết nối của bạn. Để tìm hiểu cách thiết lập kết nối, hãy xem <Anchor target="_blank" href="/partners/vi/docs/data-locker-for-partners#set-up-data-locker">Thiết lập Data Locker</Anchor>.

</Accordion>

<div id="enable-the-ad-revenue-report" />

<Accordion title="Bật báo cáo Doanh thu quảng cáo">

1. Trong phần **Data Locker content**, chọn loại báo cáo **Ad revenue [daily].**
2. Nhấp vào **Lưu kết nối**.
3. Đảm bảo rằng nhà quảng cáo đã cho phép Mạng quảng cáo xem báo cáo.
4. Để được hướng dẫn, hãy xem <Anchor target="_blank" href="/marketers/vi/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">Cho phép mạng quảng cáo nhận dữ liệu doanh thu quảng cáo.</Anchor>

</Accordion>

## Thông số kỹ thuật của báo cáo

<div id="report-considerations" />

<Accordion title="Cấu trúc và định dạng của Báo cáo">

* Định dạng: Dữ liệu đến với định dạng CSV tới bộ chứa S3 của đối tác UA.
* Cấp độ: Chứa các phương diện và số liệu cấp độ thiết bị.
* Làm giàu dữ liệu: Đưa vào dữ liệu doanh thu quảng cáo từ các đối tác trung gian và thêm dữ liệu phân bổ liên quan đến mạng quảng cáo UA (đã được loại sạch tất cả các phương diện không liên quan đến mạng quảng cáo UA).
* Tính cập nhật của dữ liệu: <Anchor target="_blank" href="/marketers/vi/docs/about-data-freshness-and-timezone-support#ad-revenue">Hàng ngày, nghĩa là dữ liệu cho Ngày 0 sẽ đến vào Ngày 1</Anchor>. Dữ liệu được ghi hàng ngày vào lúc 21:00 <Anchor target="_blank" href="/marketers/vi/docs/about-data-freshness-and-timezone-support#daily-processing">giờ UTC</Anchor> vào h=23 trong bộ chứa Data Locker của bạn.
* Ứng dụng bao gồm: Một báo cáo chứa dữ liệu của tất cả các ứng dụng mà nhà quảng cáo đã cấp quyền.
* Tiền tệ: USD. Doanh thu sự kiện được tính bằng USD vào ngày xảy ra sự kiện.
* <Anchor target="_blank" href="https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv">Xem báo cáo mẫu</Anchor>

</Accordion>

<div id="report-structure" />

<Accordion title="Các trường của Báo cáo">

| **Trường** | **Lưu ý** |
| --- | --- |
| Phiên bản | Nhãn thời gian Unix tính bằng giây. Ví dụ: 1661315124 |
| app\_id | ID ứng dụng trong nền tảng AppsFlyer |
| install\_time | <ul><li>Nhãn thời gian của lượt cài đặt: YYYY-MM-DD HH:MM:SS<br />Ví dụ: 2020-08-16 11:22:33</li><li>Đối với các thiết bị iOS 14+ và người dùng không đồng ý hoặc nếu nhà quảng cáo bật Quyền riêng tư Nâng cao, thì thời gian cài đặt sẽ được làm tròn đến giờ gần nhất.</li></ul> |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Chỉ được điền nếu UA được phân bổ cho đối tác nhận dữ liệu. |
| idfa, idfy, advertising\_id | <ul><li>Cùng một ID thiết bị, như IDFA, IDFV hoặc advertiser\_id có thể hiển thị trong nhiều hàng nếu có nhiều sự kiện kiếm tiền từ doanh thu quảng cáo.</li><li>Đối với các thiết bị iOS 14+ và người dùng không đồng ý hoặc nếu nhà quảng cáo đã bật Quyền riêng tư Nâng cao, thì ID thiết bị này sẽ không hiển thị.</li></ul> |
| platform | Nền tảng thiết bị: iOS, Android hoặc Windows Mobile |
| quốc gia | Mã quốc gia sử dụng <Anchor target="_blank" href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166 (alpha-2)</Anchor> Ví dụ: US, CN |
| original\_url | <ul><li>Đối với các thiết bị iOS 14+ và người dùng không đồng ý hoặc nếu nhà quảng cáo đã bật Quyền riêng tư Nâng cao, thì ID thiết bị này sẽ không hiển thị.</li><li>Chỉ được điền nếu UA được phân bổ cho đối tác nhận dữ liệu.</li></ul> |

Số liệu:

| **Trường** | **Lưu ý** |
| --- | --- |
| impressions | Số lần người dùng nhìn thấy quảng cáo |
| revenue\_usd | Doanh thu hàng ngày (tính bằng USD) được tạo cho ID thiết bị. **Lưu ý**: Khi là khoản doanh thu nhỏ thì số tiền doanh thu sẽ được biểu thị bằng ký hiệu khoa học. Ví dụ: 8.00E-05 |

</Accordion>

<div data-zendesk-anchors="set-the-ad-revenue-report-in-data-locker=thi%E1%BA%BFt-l%E1%BA%ADp-b%C3%A1o-c%C3%A1o-doanh-thu-qu%E1%BA%A3ng-c%C3%A1o-trong-data-locker h_01H8Y7ABGVR7BNHEYVFKPFM4JN=thi%E1%BA%BFt-l%E1%BA%ADp-b%C3%A1o-c%C3%A1o-doanh-thu-qu%E1%BA%A3ng-c%C3%A1o-trong-data-locker h_01H8Y7ABGV2T6GBE9BHJQM6FDF=configure-the-report-output-settings h_01H8Y7ABGVW6Y5RY7CVNM3EJZR=enable-the-ad-revenue-report report-specification=th%C3%B4ng-s%E1%BB%91-k%E1%BB%B9-thu%E1%BA%ADt-c%E1%BB%A7a-b%C3%A1o-c%C3%A1o h_01H8Y7ABGVXJ9ZQCJ8BR0DST6W=th%C3%B4ng-s%E1%BB%91-k%E1%BB%B9-thu%E1%BA%ADt-c%E1%BB%A7a-b%C3%A1o-c%C3%A1o h_01H8Y7ABGV0G4GJBRKKGNBSEC5=report-considerations h_01H8Y7ABGV81X0VFWTRMXGHYSA=report-structure" />
