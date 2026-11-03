---
title: Macro đăng lại cho mạng quảng cáo
metadata:
  keywords:
    - postbacks
    - Advertisers
    - Ad Networks
    - macros
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
  created_at: '2016-01-11T14:41:40Z'
  edited_at: '2022-04-20T07:23:28Z'
  id: 207273946
  locale: vi
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/vi/articles/207273946
---
> **Khai quát:** Là một mạng quảng cáo, bạn có thể xác định nội dung và điểm cuối của các đăng lại được gửi cho bạn như một phần của việc tích hợp với AppsFlyer. Các đăng lại liên quan đến thu hút của người dùng ứng dụng như lượt cài đặt, sự kiện trong ứng dụng, thu hút lại, v.v.

Hướng dẫn đăng lại đối tác tích hợp liên quan:

* <Anchor target="_blank" href="/partners/vi/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Quyền riêng tư Nâng cao</Anchor>
* <Anchor target="_blank" href="/partners/vi/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/partners/vi/docs/rejected-attribution-postbacks-to-integrated-partners">Các đăng lại phân bổ bị từ chối</Anchor>

## Bài đăng lại cho mạng quảng cáo

* **Cấu hình đăng lại:** Để yêu cầu thay đổi cài đặt đăng lại của bạn, hãy liên hệ với [integration@appsflyer.com](mailto:integrations@appsflyer.com) hoặc người quản lý phát triển đối tác AppsFlyer của bạn.
* **Loại đăng lại**: Đăng lại có sẵn cho Lượt cài đặt và sự kiện trong ứng dụng cùng Lượt cài đặt và sự kiện trong ứng dụng bị Chặn do gian lận được Protect360 xác định hoặc vi phạm Quy tắc Xác thực nhắm mục tiêu.

| Nguồn | Mô tả |
| --- | --- |
| <Anchor target="_blank" href="/marketers/vi/docs/about-link-structure-and-parameters">Thông số đường dẫn phân bổ</Anchor> | Các thông số do đối tác cung cấp trên URL lượt nhấp và URL lượt hiển thị<br /><br />Ví dụ: thông số click ID trên liên kết phân bổ - "&click\_id=CLICK\_ID" |
| ID đối tác trong AppsFlyer | ID duy nhất do đối tác cung cấp cho nhà quảng cáo<br /><br />Ví dụ: ID ứng dụng, ID tài khoản, ID người dùng, ID mạng. |
| Thông tin bắt nguồn từ SDK | Thông tin được trích xuất từ thiết bị bằng SDK AppsFlyer.<br /><br />Ví dụ: ID của thiết bị iOS có thể được trích xuất bằng cách dùng "&IDFA=(idfa)" trên đăng lại |
| Được lấy từ nền tảng AppsFlyer | Thông tin được lấy từ nền tảng AppsFlyer. |
| Protect360 và quy tắc xác thực | Thông tin về các lượt cài đặt được xác định là gian lận và các lượt cài đặt vi phạm các quy tắc nhắm mục tiêu của chiến dịch cùng các sự kiện trong ứng dụng liên quan |

## Macro đăng lại

Khi được đưa vào một đăng lại, macro được thay thế bằng dữ liệu có liên quan đến người dùng. Ví dụ: để lấy địa chỉ IP của người dùng cài đặt ứng dụng, hãy thêm `country_code=(ip)` trong cấu trúc đăng lại. Các macro được hỗ trợ được liệt kê trong bảng sau:

Các cột trong bảng dưới đây có ý nghĩa như sau:

* **Nguồn:** Dữ liệu bắt nguồn từ đâu.
  * Liên kết: Đường dẫn phân bổ
  * SDK: SDK AppsFlyer được nhúng trong ứng dụng hoặc API từ máy chủ đến máy chủ
  * AF: Sau khi được AppsFlyer xử lý
* **Gửi tất cả**: Nếu có, bạn có thể nhận dữ liệu về lượt cài đặt và sự kiện được phân bổ cho các mạng khác hoặc tự nhiên. (Có nghĩa là không được phân bổ cho bạn).
* **[Cơ sở] Macro cho tất cả các bài đăng lại**: Các macro có liên quan đến lượt cài đặt, sự kiện trong ứng dụng và các đăng lại sự kiện bị từ chối
* **[Tùy chọn]** cho các sự kiện trong ứng dụng và sự kiện bị từ chối như được chỉ ra trong cột (bị từ chối, trong ứng dụng)

| Macro đăng lại (tên) | Nguồn | Gửi tất cả | Mô tả | [Cơ sở] Macro cho tất cả các bài đăng lại | [Tùy chọn] Sự kiện trong ứng dụng và bị từ chối |
| --- | --- | --- | --- | --- | --- |
| advertising\_id | SDK | Có | ID thiết bị người dùng có thể đặt lại, AKA GAID. Cũng khả dụng dưới dạng: (sha1-advertiserId) | Có |  |
| app\_name | SDK | Có | Tên ứng dụng do nhà quảng cáo đặt | Có |  |
| appsflyer\_id | SDK | Có | Mã định danh duy nhất của AppsFlyer được ghi nhận khi có chuyển đổi | Có |  |
| attributed\_touch\_type | SDK | Không | Giá trị có thể: lượt nhấp, lượt hiển thị, TV, pre-install | Có |  |
| blocked\_reason | AF | Không | Lý do gian lận/quy tắc xác thực | Không | Bị từ chối |
| blocked\_reason\_value | AF | Không | Giá trị lý do gian lận/quy tắc xác thực (như ID trang web) | Không | Bị từ chối |
| blocked\_sub\_reason | AF | Không | Lý do phụ gian lận/quy tắc xác thực | Không | Bị từ chối |
| bundle\_id | SDK | Có | iOS: Nhận dạng để khớp với một ứng dụng hoặc một nhóm ứng dụng trong iOS (Xem ID gói nhà phát triển của Apple) Android: Tên ứng dụng | Có |  |
| country\_code | AF | Có | Mã Quốc gia sử dụng ISO 3166 (alpha-2) Ví dụ: US, CN. | Có |  |
| event\_name | SDK | Có | Tên được phân bổ cho một sự kiện | Không | Trong ứng dụng |
| event\_revenue\_USD | AF | Có | Giá trị sự kiện theo USD | Không | Trong ứng dụng |
| event\_revenue | SDK | Có | Giá trị sự kiện được SDK báo cáo bằng cách sử dụng event\_revenue\_currency hoặc đơn vị tiền tệ do bạn chọn. | Không | Trong ứng dụng |
| {"event_revenue"}  <br />{"_currency"} | SDK | Có | Mã tiền tệ của doanh thu sự kiện được báo cáo trong sự kiện hoặc đơn vị tiền tệ do bạn chọn | Không | Trong ứng dụng |
| event\_time | SDK | Có | Thời gian sự kiện | Không | Trong ứng dụng |
| event\_value | SDK | Có | sự kiện trong ứng dụng bao gồm các thuộc tính có giá trị, có thể được gửi hoàn toàn trong bài đăng lại ở định dạng JSON. URL được mã hóa bằng macro (mã hóa). | Không | Trong ứng dụng |
| idfa | SDK | Có | ID quảng cáo người dùng có thể đặt lại được tìm thấy trên thiết bị iOS cũng có sẵn dưới dạng: (sha1-idfa) | Có |  |
| idfv | SDK | Có | Mã định danh duy nhất cho mỗi người dùng mỗi nhà cung cấp trên thiết bị IOS | Có |  |
| install\_time | SDK | Có | Nhãn thời gian lượt cài đặt | Có |  |
| install\_unix\_ts | SDK | Có | Install timestamp in unix format | Có |  |
| is\_attributed | AF | Có | Cờ đánh dấu cài đặt hoặc sự kiện có được phân bổ cho nguồn truyền thông này hay không | Có |  |
| is\_lat | SDK | Có | Giới hạn theo dõi quảng cáo (LAT): iOS: Bắt đầu từ iOS 14 LAT không còn được Apple hỗ trợ. Xác định trạng thái quyền riêng tư của người dùng bằng ATT. Trong trường hợp này, bỏ qua is\_lat. Trước iOS 14, nếu là true, IDFA không khả dụng và được đặt thành 0. Android: Khi là true, người dùng đã chọn không tham gia quảng cáo dựa trên sở thích. Điều này không ngăn chặn việc thu thập GAID. | Có |  |
| is\_primary\_attribution | AF | Có | Nếu là false, hãy xem is\_retargeting. | Không | Trong ứng dụng |
| is\_retargeting | Liên kết | Không | Sử dụng kết hợp với is\_primary\_attribution. Tìm hiểu thêm về <Anchor target="_blank" href="/marketers/vi/docs/resolve-retargeting-double-attribution">phân bổ kép các sự kiện nhắm mục tiêu lại.</Anchor><br /><br />Nếu là true (1), sự kiện được báo cáo là một phần của chiến dịch nhắm mục tiêu lại và nguồn truyền thông là nguồn truyền thông nhắm mục tiêu lại.<br /><br />Nếu là false (0) và is\_primary\_attribution là false, thì sự kiện là một phần của chiến dịch nhắm mục tiêu lại nhưng nguồn truyền thông được tham chiếu là nguồn truyền thông phân bổ người dùng | Không |  |
| ngôn ngữ | SDK | Có | Ngôn ngữ (địa phương) được báo cáo bởi thiết bị và được thiết lập bởi HĐH thiết bị. | Có |  |
| OAID | SDK | Có | ID người dùng có thể đặt lại trên một số thiết bị Android thường thay thế cho GAID | Có |  |
| partner\_event\_id | AF | Có | Tên/ID của sự kiện tương ứng trong nền tảng đối tác | Không | Trong ứng dụng |
| nền tảng | SDK | Có | Nền tảng thiết bị: iOS, Android hoặc Windows Mobile | Có |  |
| retargeting\_  <br />conversion\_type | AF | Không | Một cờ đánh dấu đây là phân bổ lại hay thu hút lại | Chỉ nhắm mục tiêu lại |  |
| app\_version | SDK | Có | Tên phiên bản ứng dụng do nhà phát triển đặt trong mã ứng dụng | Có |  |
| app\_id | SDK | Có | ID ứng dụng được ứng dụng báo cáo | Có |  |
| att-0-1 | SDK | Có | Những giá trị khả thi:<ul><li>1: Trạng thái ATT là authorized hoặc af\_authorized.</li><li>0: Bất kỳ trạng thái ATT nào khác.</li></ul> | Có |  |
| att-status | SDK | Có | <Anchor target="_blank" href="/marketers/vi/docs/att-implications-ios-14-and-deprecation-of-lat#att-values">Trạng thái ATT</Anchor> do iOS báo cáo. Như là authorized, not\_determined.<br /><br />Trong một số trường hợp sẽ không có giá trị và trả về "". | Có |  |
| af\_ad | LINK | Không | Tên Quảng cáo (<Anchor target="_blank" href="/marketers/vi/docs/about-link-structure-and-parameters#mức-độ-chi-tiết-dữ-liệu">xem thêm</Anchor>) - do nhà quảng cáo/nhà xuất bản cung cấp | Có | Có |
| af\_ad\_id | LINK | Không | Do nhà quảng cáo/nhà phát hành cung cấp | Có | Có |
| af\_adset | Liên kết | Không | <ul><li>Do nhà quảng cáo/nhà phát hành cung cấp.</li><li>Bộ quảng cáo là cấp trung gian giữa Chiến dịch và Quảng cáo trong cấu trúc phân cấp. <Anchor target="_blank" href="/marketers/vi/docs/about-link-structure-and-parameters#mức-độ-chi-tiết-dữ-liệu">Xem thêm</Anchor></li></ul> | Có | Có |
| af\_adset\_id | Liên kết | Không | Do nhà quảng cáo/nhà phát hành cung cấp | Có | Có |
| c | Liên kết | Không | Do nhà quảng cáo/nhà phát hành cung cấp. Tên của chiến dịch vượt quá 100 ký tự được hiển thị trên bảng điều khiển là "c\_name\_exceeded\_max\_length" | Có | Có |
| af\_c\_id | Liên kết | Không | Do nhà quảng cáo/nhà phát hành cung cấp | Có | Có |
| af\_siteid | Liên kết | Không | <ul><li>ID duy nhất xác định nhà phát hành hiển thị quảng cáo. <Anchor target="_blank" href="/marketers/vi/docs/about-link-structure-and-parameters#site-id-parameter">Tìm hiểu thêm</Anchor></li></ul> | Có | Có |
| af\_subsite\_id | Liên kết | Không | <ul><li>Mạng phụ quảng cáo/ID Nhà phát hành.</li><li>Nếu ngoài nhà phát hành chính (ID trang web), còn có nhà phát hành phụ hoặc bạn muốn thêm thông tin bổ sung, chẳng hạn như loại hình/vị trí đặt quảng cáo trong ứng dụng, như biểu ngữ, quảng cáo xen kẽ, video, v.v., hãy sử dụng af\_sub\_siteid. Ví dụ: af\_sub\_siteid =ABCD\_4567</li></ul> | Có | Có |
| af\_ad\_type | Liên kết | Không | Use the following naming convention:<ul><li>**text:** một đơn vị quảng cáo chỉ chứa văn bản, ví dụ: kết quả tìm kiếm</li><li>**banner:** một định dạng cơ bản xuất hiện ở trên cùng hoặc dưới cùng của màn hình thiết bị</li><li>**interstitial:** quảng cáo toàn trang xuất hiện trong khoảng nghỉ trong trải nghiệm hiện tại</li><li>**video:** một video chuẩn, đó không phải là video xem có thưởng</li><li>**rewarded\_video:** một đơn vị quảng cáo cung cấp phần thưởng trong ứng dụng để đổi lấy việc xem video</li><li>**playable:** một đơn vị quảng cáo chứa bản xem trước tương tác của trải nghiệm ứng dụng</li><li>**sponsored\_content:** một liên kết được bao gồm trong một phần nội dung được tài trợ, giống như một bài viết quảng cáo</li><li>**audio:** một quảng cáo âm thanh</li></ul> | Có | Có |
| imei | SDK | Có | A unique number used to identify mobile phones | Có |  |

### Sự kiện trong ứng dụng chỉ có macro

Các ví dụ tiếp theo liên quan đến đăng lại sự kiện trong ứng dụng có sẵn cho các đối tác.

> 📄 **Ví dụ:**
>
> Mẫu postback sự kiện "&event=(event)&json=(encode)" đã được dịch thành postback sau đây cho sự kiện af\_purchase cụ thể:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> Giá trị JSON được giải mã của postback này là
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

#### **Giá trị được mã hóa**

Đăng lại có thể cần chứa các ký tự bất quy tắc, không phải chữ và số. Để chuyển chính xác các giá trị này qua các đăng lại, URL AppsFlyer mã hóa các giá trị không phải chữ và số.

Để giải mã hoặc mã hóa một bài đăng lại, hãy sử dụng một <Anchor target="_blank" href="https://www.urldecoder.org/">dịch vụ web mã hóa.</Anchor>

### Postback mẫu

### Ví dụ về Postback Cài Đặt tổng quan

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)
&advertising_id=(advertiser_id)&android_id=(android_id)
&install_time=(install_unix_ts)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?&site_id=(publisher_id)&
device_ip=(ip)&;idfa=(idfa)&install_time=(install_unix_ts)
```

</Tab>
</Tabs>

### Ví dụ về Postback Sự kiện trong ứng dụng chung

<Tabs>
<Tab title="Android">

```http
http://YourCompanyDomain.com?site_id=(publisher_id)&
device_ip=(ip)&advertising_id=(advertiserId)&android_id=(android_id)&
install_time=(install_unix_ts)&event_name=(event_name)&currency=(currency)&
json=(event_value)
```

</Tab>

<Tab title="iOS">

```http
http://YourCompanyDomain.com?clickid=(clickid)&site_id=(publisher_id)&
device_ip=(ip)&idfa=(idfa)&install_time=(install_unix_ts)
&event_name=(event_name)&currency=(currency)&json=(event_value)
```

</Tab>
</Tabs>

### Ví dụ về đăng lại sự kiện trong ứng dụng

Thông số sự kiện:

* Tên sự kiện: af\_revenue
* Doanh thu của Sự kiện: 120,00
* Đơn vị tiền tệ của sự kiện: USD
* Giá trị của Sự kiện: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

Postback:

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```