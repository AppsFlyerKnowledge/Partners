---
title: Macro postback untuk jaringan iklan
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
  edited_at: '2022-04-20T07:23:31Z'
  id: 207273946
  locale: id
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/id/articles/207273946
---
> **Sekilas:** Sebagai jaringan iklan, Anda dapat menentukan konten dan titik akhir dari postback yang dikirimkan kepada Anda sebagai bagian dari integrasi Anda dengan AppsFlyer. Postback terkait interaksi pengguna aplikasi seperti penginstalan, in-appevent, interaksi ulang, dan sebagainya.

Panduan postback mitra terintegrasi terkait:

* <Anchor target="_blank" href="/partners/id/docs/advanced-privacy-guide-postback-macros-for-ad-networks">Privasi Lanjutan</Anchor>
* <Anchor target="_blank" href="/partners/id/docs/skan-integration-guide-for-ad-networks">SKAdNetwork</Anchor>
* <Anchor target="_blank" href="/partners/id/docs/rejected-attribution-postbacks-to-integrated-partners">Postback atribusi yang ditolak</Anchor>

## Postback untuk jaringan iklan

* **Konfigurasi postback:** Untuk meminta perubahan pada pengaturan postback Anda, hubungi [integrations@appsflyer.com](mailto:integrations@appsflyer.com) atau manajer pengembangan mitra AppsFlyer Anda.
* **Jenis postback**: Postback tersedia untuk penginstalan dan in-app event, penginstalan dan in-app event yang diblokir (karena kecurangan yang teridentifikasi oleh Protect360 atau melanggar aturan validasi penargetan).

| Source | Description |
| --- | --- |
| <Anchor target="_blank" href="/marketers/id/docs/about-link-structure-and-parameters">Parameter link atribusi</Anchor> | Parameter yang diberikan oleh mitra pada URL klik dan tayangan<br /><br />Misalnya: parameter ID klik pada tautan atribusi - "&click\_id=CLICK\_ID" |
| ID mitra di AppsFlyer | ID unik disediakan pada pemasang iklan oleh mitra<br /><br />Misalnya: ID aplikasi, ID akun, ID pengguna, ID jaringan |
| Informasi turunan SDK | Informasi yang diekstrak dari perangkat oleh SDK AppsFlyer<br /><br />Misalnya: ID perangkat iOS dapat diekstrak dengan menggunakan "&IDFA=(idfa)" di postback |
| Berasal dari platform AppsFlyer | Informasi yang diperoleh dari platform AppsFlyer. |
| Protect360 dan aturan validasi | Informasi tentang penginstalan yang diidentifikasi sebagai kecurangan dan penginstalan yang melanggar aturan penargetan kampanye, dan in-app event terkait |

## Macro postback

Saat disertakan dalam postback, macro diganti dengan data yang relevan dengan pengguna. Misalnya, untuk mendapatkan alamat IP pengguna yang menginstal aplikasi, sertakan `country_code=(ip)` dalam struktur postback.  Macro yang didukung tercantum dalam tabel berikut:

Kolom pada tabel berikut memiliki arti berikut:

* **Source (Sumber):** Dari mana data berasal.
  * Tautan: Tautan atribusi
  * SDK: SDK AppsFlyer yang disematkan di aplikasi atau API server-to-server
  * AF: Setelah diproses oleh AppsFlyer
* **Kirim semua**: Jika ya, Anda dapat menerima data penginstalan dan event yang diatribusikan ke jaringan lain atau organik.  (Artinya tidak diatribusikan ke Anda).
* **[Basis] Macro untuk semua postback**: Macro yang relevan dengan penginstalan, in-app event, dan postback event yang ditolak
* **[Opsional]** untuk in-app event dan event yand ditolak seperti yang ditunjukkan dalam kolom (ditolak, in-app)

| Macro postback (nama) | Source | Send all | Description | [Basis] Macro untuk semua postback | [Opsional] In-app dan event yang ditolak |
| --- | --- | --- | --- | --- | --- |
| advertising\_id | SDK | Ya | ID perangkat yang dapat diatur ulang pengguna, ATAU GAID. Juga tersedia sebagai: (sha1-advertiserId) | Ya |  |
| app\_name | SDK | Ya | Nama aplikasi yang ditetapkan oleh pemasang iklan | Ya |  |
| appsflyer\_id | SDK | Ya | AppsFlyer unique identifier recorded upon conversion | Ya |  |
| attributed\_touch\_type | SDK | Tidak | Possible values: click, impression, TV, pre-install | Ya |  |
| blocked\_reason | AF | Tidak | Alasan kecurangan/aturan validasi | Tidak | Ditolak |
| blocked\_reason\_value | AF | Tidak | Nilai alasan kecurangan/aturan validasi (seperti ID situs) | Tidak | Ditolak |
| blocked\_sub\_reason | AF | Tidak | Sub-alasan kecurangan/aturan validasi | Tidak | Ditolak |
| bundle\_id | SDK | Ya | iOS: Identifikasi untuk mencocokkan satu aplikasi atau sekelompok aplikasi di iOS (Lihat ID paket pengembang Apple) Android: Nama aplikasi | Ya |  |
| country\_code | AF | Ya | Kode Negara menggunakan ISO 3166 (alpha-2) Misalnya: US, CN. | Ya |  |
| event\_name | SDK | Ya | Nama yang dialokasikan ke event | Tidak | In-app |
| event\_revenue\_USD | AF | Ya | Event value in USD | Tidak | In-app |
| event\_revenue | SDK | Ya | Nilai event yang dilaporkan oleh SDK menggunakan event\_revenue\_currency atau mata uang yang dipilih oleh Anda. | Tidak | In-app |
| {"event_revenue"}  <br />{"_currency"} | SDK | Ya | Kode mata uang pendapatan event yang dilaporkan dalam event atau mata uang yang dipilih oleh Anda | Tidak | In-app |
| event\_time | SDK | Ya | Event Time | Tidak | In-app |
| event\_value | SDK | Ya | in-app event menyertakan atribut dengan nilai, yang dapat dikirim seluruhnya di postback dalam format JSON. Penyandian URL menggunakan macro (penyandian). | Tidak | In-app |
| idfa | SDK | Ya | ID iklan pengguna yang dapat diatur ulang ditemukan di perangkat iOS juga tersedia sebagai: (sha1-idfa) | Ya |  |
| idfv | SDK | Ya | Pengenal unik per pengguna per vendor di perangkat IOS | Ya |  |
| install\_time | SDK | Ya | Stempel waktu penginstalan | Ya |  |
| install\_unix\_ts | SDK | Ya | Install timestamp in unix format | Ya |  |
| is\_attributed | AF | Ya | A flag marking if the install or event is attributed to this media source | Ya |  |
| is\_lat | SDK | Ya | Batas Pelacakan Iklan (Limit ad tracking/LAT): iOS: Sejak iOS 14, LAT dihentikan oleh Apple. Tentukan status privasi pengguna menggunakan ATT. Dalam hal ini abaikan is\_lat. Sebelum iOS 14, jika true (benar), IDFA tidak tersedia dan diatur ke 0. Android: Jika true (benar), pengguna menonaktifkan iklan berbasis minat. Ini tidak mencegah pengumpulan GAID. | Ya |  |
| is\_primary\_attribution | AF | Ya | Jika false (salah), lihat is\_retargeting. | Tidak | In-app |
| is\_retargeting | Link | Tidak | Gunakan bersama dengan is\_primary\_attribution. Pelajari lebih lanjut tentang <Anchor target="_blank" href="/marketers/id/docs/resolve-retargeting-double-attribution">atribusi ganda dari event penargetan ulang.</Anchor><br /><br />Jika true (1), event dilaporkan sebagai bagian dari kampanye penargetan ulang dan sumber medianya adalah sumber media penargetan ulang.<br /><br />Jika false (0) dan is\_primary\_attribution false, event menjadi bagian dari kampanye penargetan ulang tetapi sumber media yang dirujuk adalah sumber media atribusi pengguna | Tidak |  |
| language | SDK | Ya | Bahasa (lokal) dilaporkan oleh perangkat dan diatur oleh OS perangkat. | Ya |  |
| oaid | SDK | Ya | ID yang dapat diatur ulang pengguna di beberapa perangkat Android biasanya sebagai alternatif untuk GAID | Ya |  |
| partner\_event\_id | AF | Ya | Nama/ID event terkait di platform mitra | Tidak | In-app |
| platform | SDK | Ya | Platform perangkat: iOS, Android, atau Windows Mobile | Ya |  |
| retargeting\_  <br />conversion\_type | AF | Tidak | Tanda bendera jika ini adalah atribusi ulang atau interaksi ulang | Khusus penargetan ulang |  |
| app\_version | SDK | Ya | Nama versi aplikasi yang diatur oleh pengembang di kode aplikasi | Ya |  |
| app\_id | SDK | Ya | The app ID as reported by the app | Ya |  |
| att-0-1 | SDK | Ya | Possible values:<ul><li>1: The ATT status is authorized or af\_authorized.</li><li>0: Any other ATT status.</li></ul> | Ya |  |
| att-status | SDK | Ya | The <Anchor target="_blank" href="/marketers/id/docs/att-implications-ios-14-and-deprecation-of-lat#att-values">ATT status</Anchor> reported by iOS. Like authorized, not\_determined.<br /><br />In some cases there is no value and "" is returned. | Ya |  |
| af\_ad | LINK | Tidak | Ad Name (<Anchor target="_blank" href="/marketers/id/docs/about-link-structure-and-parameters#tingkat-perincian-data">see more</Anchor>) provided by the advertiser/publisher | Ya | Ya |
| af\_ad\_id | LINK | Tidak | Provided by the advertiser/publisher | Ya | Ya |
| af\_adset | Link | Tidak | <ul><li>Provided by the advertiser/publisher.</li><li>Adset is an intermediate level in the hierarchy between Campaign and Ad. <Anchor target="_blank" href="/marketers/id/docs/about-link-structure-and-parameters#tingkat-perincian-data">See more</Anchor></li></ul> | Ya | Ya |
| af\_adset\_id | Link | Tidak | Provided by the advertiser/publisher | Ya | Ya |
| c | Link | Tidak | Provided by the advertiser/publisher. Campaign names that exceed 100 characters in length are displayed on the dashboard as "c\_name\_exceeded\_max\_length" | Ya | Ya |
| af\_c\_id | Link | Tidak | Provided by the advertiser/publisher | Ya | Ya |
| af\_siteid | Link | Tidak | <ul><li>ID unik yang mengidentifikasi penerbit yang menampilkan iklan. <Anchor target="_blank" href="/marketers/id/docs/about-link-structure-and-parameters#site-id-parameter">Pelajari lebih lanjut</Anchor></li></ul> | Ya | Ya |
| af\_subsite\_id | Link | Tidak | <ul><li>Sub-jaringan iklan/ID Penerbit.</li><li>Jika selain penerbit utama (ID situs), ada sub-penerbit, atau jika Anda menyertakan informasi tambahan, seperti jenis iklan/penempatan dalam aplikasi, seperti spanduk, iklan interstisial, video, dll. gunakan af\_sub\_siteid. Misalnya: af\_sub\_siteid =ABCD\_4567</li></ul> | Ya | Ya |
| af\_ad\_type | Link | Tidak | Use the following naming convention:<ul><li>**teks:** unit iklan yang hanya berisi teks, misalnya hasil pencarian</li><li>**banner:** a basic format that appears at the top or bottom of the device screen</li><li>**interstitial:** a full-page ad that appears during breaks in the current experience</li><li>**video:** a video standar, non-reward</li><li>**rewarded\_video:** an ad unit offering in-app rewards in exchange for watching a video</li><li>**playable:** an ad unit containing an interactive preview of the app experience</li><li>**sponsored\_content:** a link included in a piece of sponsored content, like an advertorial article</li><li>**audio:** an audio ad</li></ul> | Ya | Ya |
| imei | SDK | Ya | A unique number used to identify mobile phones | Ya |  |

### Macro khusus in-app event

Contoh berikut terkait dengan postback in-app event yang tersedia untuk mitra.

> 📄 **Contoh**
>
> Event postback template "&event=(event)&json=(encode)" was translated to the following postback for a specific af\_purchase event:
>
> ```http
> &event=af_purchase&json=%7B%22af_quantity%22%3A1%2C%22
> af_revenue%22%3A%2212000%22%2C%22af_currency%22%3A%
> 22USD%22%2C%22af_content_id%22%3A%221107%22%2C%22
> af_content_type%22%3A%22default_type%22%7D%0A
> ```
>
> Nilai JSON yang disandikan dari postback ini adalah
>
> ```json
> {"af_quantity":1,"af_revenue":"12000","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}
> ```

#### **Nilai yang disandikan**

Postback dapat berisi karakter tidak beraturan, yang bukan alfanumerik. Untuk mentransfer nilai ini dengan benar melalui postback, URL AppsFlyer menyandikan nilai non alfanumerik.

Untuk memecahkan kode atau menyandikan postback, gunakan <Anchor target="_blank" href="https://www.urldecoder.org/">layanan web penyandian.</Anchor>

### Sample postbacks

### General install postback examples

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

### General in-app event postback examples

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

### Contoh postback in-app event

Event Parameters:

* Nama Event: af\_revenue
* Pendapatan Event: 120.00
* Mata Uang Event: USD
* Event Value: `{"af_quantity":1,"af_revenue":"120","af_currency":"USD","af_content_id":"1107","af_content_type":"default_type"}`

Postback:

```http
http://YourCompanyDomain.com?clickid=8594845&site_id=click123&device_ip=
38.166.144.142&advertising_id=121sxxxx-xxxx-xxxx-xxxx-52454bd7500b&
android_id=9aaeecc4455xxxxx&;install_time=1451923560&event_name=af_purchase&
currency=USD&revenue=120.00&json=%7B%22af_quantity%22%3A1%2C%22 />af_revenue
%22%3A%22120.10%22%2C%22af_currency%22%3A%22USD%22%2C%22af_content_id
%22%3A%221107%22%2C%22af_content_type%22%3A%22default_type%22%7D%0A
```