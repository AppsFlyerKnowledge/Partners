---
title: API lược đồ CV SKAN cho mạng quảng cáo
metadata:
  keywords:
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
table_of_contents: false
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
  created_at: '2022-12-26T15:03:54Z'
  edited_at: '2023-03-05T23:22:27Z'
  id: 11705009866001
  locale: vi
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/vi/articles/11705009866001
---
> **Khái quát**: Xem lược đồ CV SKAN như được nhà quảng cáo ánh xạ.

<div id="skan-cv-schema-api-for-ad-networks" />

## API lược đồ CV SKAN cho mạng quảng cáo

Với phân bổ SKAdNetwork (SKAN), nhà quảng cáo chấm điểm chất lượng người dùng bằng cách cài đặt giá trị chuyển đổi (CV) dựa trên hoạt động của người dùng sau khi cài đặt trong các khoảng thời gian (khung thời gian) cụ thể. <Anchor target="_blank" href="/marketers/vi/docs/skadnetwork-skan-solution-guide">Tìm hiểu thêm về SKAN</Anchor>

iOS báo cáo CV qua các đăng lại được gửi đến mạng quảng cáo đặt quảng cáo. Bắt đầu từ iOS 15, các nhà quảng cáo cũng có thể hướng dẫn iOS gửi đăng lại trực tiếp tới AppsFlyer.

API này cung cấp cho mạng quảng cáo bản đồ CV-to-attribution-events-and-values. Các mạng quảng cáo sử dụng bản đồ này để giải mã các đăng lại mà họ nhận được.

API trả về dưới dạng JSON lồng nhau. Lược đồ cho mỗi ứng dụng là riêng biệt. Ánh xạ theo CV được chứa trong mảng conversion\_value\_mapping.

Để sử dụng API, hãy yêu cầu nhà phát triển của bạn tuân theo <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">hướng dẫn về API lược đồ CV SKAN cho mạng quảng cáo</Anchor>. Để biết danh sách các mã khóa và mô tả của chúng, hãy nhấp vào 200 trong trình giả lập.

**Lưu ý**:

* Phạm vi giá trị CV là:
  * SKAN 4 khung thời gian 1 giá trị đã xử lý: 0-63.
  * SKAN 4 khung thời gian 1, 2 và 3 giá trị thô: thấp, trung bình hoặc cao.
  * SKAN 3 trở xuống: 0-63
* Nhà quảng cáo có thể thay đổi ánh xạ CV bất kỳ lúc nào.
* Bạn, mạng quảng cáo, phải truy vấn API này hàng ngày để đảm bảo rằng bạn có lược đồ cập nhật nhất.

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=api-l%C6%B0%E1%BB%A3c-%C4%91%E1%BB%93-cv-skan-cho-m%E1%BA%A1ng-qu%E1%BA%A3ng-c%C3%A1o" />
