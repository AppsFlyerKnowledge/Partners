---
title: ROI360 untuk mitra UA
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
  edited_at: '2023-09-15T15:36:33Z'
  id: 17735150011921
  locale: id
  section: Receive data
  section_id: 6551235995281
  url: https://support.appsflyer.com/hc/id/articles/17735150011921
---
> **Sekilas:** AppsFlyer memberi mitra UA iklan yang lengkap dan akurat, pembelian dalam aplikasi, dan data berlangganan yang dapat diperbarui secara otomatis melalui laporan dan postback. Mitra dapat menyerap informasi tersebut untuk mengoptimalkan kampanye UA.

## Pengantar

AppsFlyer menerima informasi pendapatan dari mitranya dan app store (Apple App Store dan Google Play Store). Setelah diterima, data menjalani serangkaian langkah termasuk validasi, normalisasi, atribusi, dan pengayaan dengan properti dan dimensi tambahan.  AppsFlyer dapat mengirimkan informasi tersebut ke mitra UA. Setelah proses ini, AppsFlyer mengirimkan data yang diperkaya dan diatribusikan ke mitra UA. Mitra UA kemudian dapat memanfaatkan informasi ini untuk mengoptimalkan kampanye akuisisi pengguna dan meningkatkan layanan yang mereka tawarkan kepada pemasang iklan.

<div id="what-revenue-types-are-reported-to-the-partners" />

<Accordion title="Jenis pendapatan apa yang dilaporkan ke mitra?">

Aplikasi menghasilkan dua jenis pendapatan:

* **Pendapatan iklan:** Pendapatan iklan dihasilkan setiap kali iklan ditampilkan di aplikasi, seperti di spanduk, iklan interstisial, dan format lainnya. Jumlah ini dapat dihitung terlepas dari metode kampanye yang digunakan untuk menagih pemasang iklan.
* **Pembelian dalam aplikasi dan langganan perpanjangan otomatis:** Pendapatan toko dihasilkan setiap kali pembelian dalam aplikasi atau transaksi terkait langganan dilakukan.

</Accordion>

<div id="how-does-appsflyer-provide-revenue-signals-to-ua-partners" />

<Accordion title="Bagaimana AppsFlyer memberikan sinyal pendapatan kepada mitra UA?">

AppsFlyer memberi mitra informasi mengenai iklan dalam aplikasi, pembelian dalam aplikasi, dan pendapatan berlangganan melalui cara berikut:

* **Laporan Sinyal UA Pendapatan Iklan**: Laporan ini mencantumkan event pendapatan iklan yang dikumpulkan ke tingkat perangkat. Laporan tersedia setiap hari di Data Locker dan berisi data hari sebelumnya.
* **Postback Pendapatan Iklan**: Setiap kali impresi iklan terjadi pada perangkat klien, postback dikirim dari AppsFlyer ke mitra yang berisi detail event pendapatan iklan.
* **Postback Pendapatan Toko**: Setiap kali event pembelian atau berlangganan terjadi, postback dikirim dari AppsFlyer ke mitra yang berisi rincian event pendapatan.

</Accordion>

## Siapkan ROI360 untuk mitra

Tindakan apa yang perlu dilakukan mitra untuk menerima laporan sinyal UA serta postback pendapatan iklan dan pendapatan toko?

<div id="how-to-subscribe-to-the-roi360-ua-signals-report" />

<Accordion title="Cara berlangganan laporan Sinyal ROI360 UA">

Untuk memungkinkan mitra mendapatkan laporan melalui Data Locker:

* Mitra harus melakukan langkah-langkah berikut di Data Locker:
  1. <Anchor target="_blank" href="/partners/id/docs/data-locker-for-partners#set-up-data-locker">Siapkan Data Locker</Anchor> di akun mitra termasuk koneksi ke penyedia layanan cloud, serta format dan konten laporan.
  2. <Anchor target="_blank" href="/partners/id/docs/ad-revenue-signals-for-ua-ad-networks#enable-the-ad-revenue-report">Aktifkan laporan Sinyal UA ROI360</Anchor>.
* Pemasang iklan harus <Anchor target="_blank" href="/marketers/id/docs/roi360-guide-ad-revenue-attribution#permission-to-get-ad-revenue-data">memberikan izin kepada mitra untuk laporan tersebut</Anchor>.

</Accordion>

<div id="how-to-receive-roi360-postbacks-from-appsflyer" />

<Accordion title="Cara menerima postback ROI360 dari AppsFlyer">

Untuk menerima postback dari AppsFlyer, mitra harus memulai percakapan dengan tim integrasi mitra AppsFlyer. Selanjutnya, tim akan mengonfigurasi nilai postback pendapatan dalam aplikasi ROI dalam platform AppsFlyer.

Untuk menghubungi dukungan mitra AppsFlyer, buka menu **Bantuan** di dashboard Anda dan pilih **Hubungi tim kami**.

[![alt](https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif)](https://files.readme.io/02d80a38dfb950e01127ba8afa33dca1a8bbef9fe137fe11743afaad966244c8-17770060481809.gif)

</Accordion>

## Laporan Sinyal UA ROI360 untuk Jaringan UA

Laporan ini memberikan catatan pendapatan CSV/parket hari x+1 yang lengkap dan akurat ke bucket S3 mitra UA setiap hari. Setiap catatan merupakan kumpulan event pendapatan iklan di tingkat perangkat.

Laporan Sinyal UA tidak menyediakan data real-time seperti yang dilakukan postback pendapatan iklan. Namun, ini lebih akurat dan lengkap. Hal ini karena nilai tayangan dapat berubah seiring berjalannya waktu. Hal ini terutama berlaku bila data pendapatan tingkat tayangan ditujukan untuk tayangan iklan yang dijual melalui penawaran BPS standar, bukan penawaran waktu sebenarnya.

<div id="what-are-the-report-data-sources" />

<Accordion title="Apa sumber data laporannya?">

Bergantung pada jenis integrasi pemasang iklan, data laporan dapat berasal dari:

1. Integrasi <Anchor target="_blank" href="/marketers/id/docs/integrate-the-roi360-ad-revenue-sdk-api">konektor AdRevenue SDK</Anchor> : pelanggan dapat berbagi data pendapatan tingkat impresi yang dimuat oleh mitra ke perangkat klien, dan kemudian dilaporkan ke AppsFlyer hampir secara real-time.
2. Integrasi tingkat perangkat berbasis API S2S: pelanggan dapat mengonfigurasi kredensial mitra mereka dalam UI AppsFlyer di bawah mitra terintegrasi dan memungkinkan pendapatan iklan ROI360 untuk mengumpulkan data pendapatan iklan tingkat perangkat atas nama mereka.
3. Kombinasi keduanya (Freshness to Accuracy/Keaktualan ke Keakuratan).

   **Catatan:** Transfer data dari pemasang iklan ke AppsFlyer bergantung pada izin pemasang iklan dan apakah pemasang iklan merupakan pelanggan tingkat lanjut ROI360.

</Accordion>

<div id="what-data-processing-is-performed-on-the-report-data" />

<Accordion title="Pemrosesan data apa yang dilakukan pada data laporan?">

Pendapatan Iklan ROI360 AppsFlyer melakukan hal berikut:

1. Normalisasi data
2. Atribusi ke sumber media penginstalan dan pengayaan data
3. Pembuatan event pendapatan iklan
4. Event dikumpulkan ke tingkat perangkat

</Accordion>

<div id="how-is-the-report-data-delivered" />

<Accordion title="Bagaimana data laporan dikirim?">

Data tingkat perangkat ditulis setiap hari ke laporan di Data Locker

</Accordion>

<div id="what-is-the-report-data-freshness" />

<Accordion title="Apa yang dimaksud dengan keaktualan data laporan?">

Data ditulis setiap hari ke folder h=23 bucket Data Locker Anda pada pukul 21:00 <Anchor target="_blank" href="/marketers/id/docs/about-data-freshness-and-timezone-support#daily-processing">waktu UTC</Anchor>.

</Accordion>

<div id="what-are-the-report-fields" />

<Accordion title="Apa saja bidang laporannya?">

| **Kolom** | **Catatan** |
| --- | --- |
| Versi | Stempel waktu Unix dalam hitungan detik. Contoh:  1661315124 |
| app\_id | ID Aplikasi di platform AppsFlyer |
| install\_time | • Stempel waktu penginstalan: HH-BB-TTTT JJ:MM:DDContoh: 16-08-2020 11:22:33 • Untuk perangkat iOS 14+ dan pengguna yang tidak memberikan izin, atau jika pemasang iklan mengaktifkan Privasi Lanjutan, waktu penginstalan dibulatkan ke jam terdekat. |
| campaign, campaign\_id, adset\_name, adset\_id, ad\_name, ad\_name, ad\_id, site\_id | Hanya diisi jika UA dikaitkan dengan mitra yang menerima data. |
| idfa, idfv, advertising\_id | • ID perangkat yang sama, seperti IDFA, IDFV, atau advertiser\_id dapat ditampilkan dalam beberapa baris jika terdapat lebih dari satu event monetisasi pendapatan iklan. • Untuk perangkat iOS 14+ dan pengguna yang tidak memberikan izin, atau jika pemasang iklan mengaktifkan Privasi Lanjutan, ini tidak akan ditampilkan. |
| platform | Platform perangkat: iOS, Android, atau Windows Mobile |
| country | Kode negara menggunakan [ISO 3166 (alpha-2)](https://www.iso.org/iso-3166-country-codes.html) Contoh: US, CN |
| original\_url | • Untuk perangkat iOS 14+ dan pengguna yang tidak memberikan izin, atau jika pemasang iklan mengaktifkan Privasi Lanjutan, ini tidak akan ditampilkan. Hanya diisi jika UA dikaitkan dengan mitra yang menerima data. |
| mediation\_network | Jaringan mediasi yang terkait dengan impresi atau tayangan. <Anchor target="_blank" href="/marketers/id/docs/roi360-guide-ad-revenue-attribution#closed-beta--ua-signals-for-ad-networks">Lihat daftar kemungkinan jaringan</Anchor> |
| ad\_unit | Hadir pada Q3 2023: Ad\_unit monetisasi yang dikaitkan dengan impresi atau berbagai impresi |
| penempatan | Hadir pada Q3 2023: Penempatan monetisasi yang dikaitkan dengan impresi atau berbagai impresi |

</Accordion>

<div id="download-the-report-data-sample" />

<Accordion title="Unduh contoh data laporan">

[Klik untuk mengunduh laporan](https://docs.google.com/spreadsheets/d/e/2PACX-1vSiPD52sbLAcl3mGbAFAiqsCZuSpUamrWP8n9BDyvI11DyNlckiKj-Peuo_fbSuIu-XnUxZqwAMEojT/pub?output=csv)

</Accordion>

## Postback pendapatan iklan dalam aplikasi (IAA)

Postback IAA adalah pendekatan penyerapan kedua yang digunakan AppsFlyer untuk mengirimkan informasi pendapatan ke mitra. Keuntungan utama mereka dibandingkan laporan sinyal UA Pendapatan Iklan adalah keaktualannya, karena postback menawarkan pembagian data pendapatan IAA yang hampir real-time. Hal ini berbeda dengan keaktualan X+1 (satu hari setelah tanggal terjadinya event) yang ditawarkan melalui laporan sinyal UA pendapatan iklan.

Namun, keaktualan real-time kurang akurat dibandingkan dengan X+1:

* Data postback IAA real-time rata-rata ±5% kurang akurat dibandingkan data laporan sinyal UA X+1.
* Data postback IAA real-time rata-rata ±7% kurang lengkap dibandingkan laporan sinyal UA data X+1.

<div id="what-are-the-iaa-postback-data-sources" />

<Accordion title="Apa saja sumber data postback IAA?">

Data untuk postback IAA berasal dari data tingkat Impresi yang dimuat mitra ke perangkat klien. Data ini kemudian dibagikan dengan AppsFlyer melalui konektor SDK Pendapatan Iklan ROI360, yang dipasang di perangkat oleh pemasang iklan. Konektor ini memungkinkan pengembang aplikasi melaporkan event impresi, termasuk parameter tertentu seperti ILRD, mata uang, platform mediasi, dan sumber monetisasi.

Transfer data dari perangkat klien pemasang iklan ke AppsFlyer tunduk pada izin pemasang iklan dan apakah pemasang iklan merupakan pelanggan tingkat lanjut ROI360.

</Accordion>

<div id="what-processing-is-performed-on-the-iaa-postback-data" />

<Accordion title="Pemrosesan apa yang dilakukan pada data postback IAA?">

AppsFlyer ROI360 melakukan langkah-langkah berikut untuk setiap data tingkat impresi yang diterima:

1. Normalisasi data
2. Atribusi ke sumber media instalasi dan pengayaan data.
3. Pembuatan event **af\_ad\_revenue** .

</Accordion>

<div id="how-is-the-postback-data-delivered" />

<Accordion title="Bagaimana data postback dikirimkan?">

Event tersebut dikirim ke mitra melalui konfigurasi postback yang sudah ada antara mitra dan AppsFlyer sebagai parameter tambahan.

</Accordion>

## Postback pembelian dalam aplikasi (IAP).

Postback pembelian dalam aplikasi ROI360 memberikan akurasi pelaporan berlapis dengan terlebih dahulu memvalidasi setiap transaksi, menghapus duplikatnya, lalu memotong komisi toko dan pajak penjualan.

<div id="what-are-the-iap-postback-data-sources" />

<Accordion title="Apa saja sumber data postback IAP?">

Data untuk postback IAP berasal dari:

1. Data tingkat transaksi dibaca oleh konektor SDK Pembelian ROI360 setiap kali terjadi pembelian dalam aplikasi atau event berlangganan yang dapat diperpanjang secara otomatis di perangkat.
2. Setiap **notifikasi server App Store dan Google Play (RTDN)** yang masuk juga diproses oleh logika bisnis pembelian dan pendapatan langganan AppsFlyer:
   * Notifikasi mengenai transaksi yang sebelumnya dilaporkan melalui konektor SDK divalidasi dan diproses.
   * Notifikasi mengenai transaksi yang tidak diketahui tidak dilaporkan ke AppsFlyer

   **Catatan:** Transfer data dari pemasang iklan ke AppsFlyer bergantung pada izin pemasang iklan dan apakah pemasang iklan merupakan pelanggan tingkat lanjut ROI360.

</Accordion>

<div id="what-data-processing-is-performed-on-the-iap-postback-data" />

<Accordion title="Pemrosesan data apa yang dilakukan pada data postback IAP?">

AppsFlyer ROI360 melakukan langkah-langkah berikut untuk setiap data tingkat transaksi yang diterima:

1. AppsFlyer **memvalidasi pembelian atau langganan dengan toko yang relevan** untuk memastikan pembelian atau langganan tersebut tidak menipu.
   * Setelah validasi berhasil, AppsFlyer mencatat pembelian atau langganan.
   * Jika validasi tanda terima gagal, event akan ditampilkan dalam laporan data lengkap in-app event yang diblokir (tersedia untuk pelanggan Protect360).
2. AppsFlyer memastikan transaksi tidak terduplikasi, termasuk transaksi terkait keluarga berbagi di iOS.
3. AppsFlyer menghitung data pendapatan bersih dengan memperhitungkan komisi toko dan pajak (**Pendapatan Sejati**).
4. AppsFlyer menghasilkan event pembelian atau siklus hidup internal untuk transaksi yang divalidasi dan diproses.

</Accordion>

<div id="how-is-the-postback-delivered" />

<Accordion title="Bagaimana postback dikirimkan?">

Event IAP dikirim ke mitra melalui integrasi postback yang ada antara mitra dan AppsFlyer.

</Accordion>

<div id="what-are-the-iap-events" />

<Accordion title="Apa saja event IAP?">

Pelanggan ROI360 dapat berbagi nama event yang menghasilkan pendapatan berikut:

**Nama event**

| **Nama Event** | **Deskripsi** |
| --- | --- |
| af\_purchase | Dicatat saat pengguna melakukan pembelian. |
| af\_purchase\_refund | Dicatat saat pembelian dikembalikan dananya. |
| af\_ars\_trial\_converted | Dicatat saat perpanjangan dengan harga penuh dimulai, setelah masa uji coba |
| af\_ars\_subscription\_started | Dicatat saat langganan dengan harga penuh atau diskon dimulai |
| af\_ars\_subscription\_resumed | Dicatat saat langganan dengan harga penuh dilanjutkan setelah langganan dibatalkan atau dikembalikan dananya. |
| af\_ars\_subscription\_refunded | Dicatat saat pelanggan mengembalikan dana. |
| af\_ars\_subscription\_renewed | Dicatat saat langganan diperpanjang otomatis. |
| af\_ars\_subscription\_xgraded | Dicatat saat pelanggan melakukan upgrade, downgrade, atau cross-grade ke produk yang berbeda. |

</Accordion>

<div data-zendesk-anchors="introduction=pengantar 01H7T1DS6SNC7X8GX4DGXT4GC0=pengantar 01H7T1DS6TYHE3A4XWBDNHCFCZ=what-revenue-types-are-reported-to-the-partners 01H7T1DS6T82RWQ4BBWNPQ6BT2=how-does-appsflyer-provide-revenue-signals-to-ua-partners set-up-roi360-for-partners=siapkan-roi360-untuk-mitra 01H7T1DS6TDA8CX1ZF3GGE4EHB=siapkan-roi360-untuk-mitra 01H7T1DS6T0QFB6K6R78PMVVB2=how-to-subscribe-to-the-roi360-ua-signals-report 01H7T1DS6TBNJBBR6M98RTVMFF=how-to-receive-roi360-postbacks-from-appsflyer roi360-ua-signals-report-for-ua-networks=laporan-sinyal-ua-roi360-untuk-jaringan-ua 01H7T1DS6T93844DMZY744ECQE=laporan-sinyal-ua-roi360-untuk-jaringan-ua 01H7T1DS6T4AF6GTETE6HZMYF7=what-are-the-report-data-sources 01H7T1DS6TDNTYDY4JF70F40SV=what-data-processing-is-performed-on-the-report-data 01H7T1DS6T94V4674AMNVCD4T6=how-is-the-report-data-delivered 01H7T1DS6T4F0QV5VE8XZVV1RY=what-is-the-report-data-freshness 01H7T1DS6TYER08FGK9GDKHFEG=what-are-the-report-fields 01H7T1DS6TH98NT4KGKPR7DRDM=download-the-report-data-sample inapp-ad-revenue-iaa-postbacks=postback-pendapatan-iklan-dalam-aplikasi-iaa 01H7T1DS6T0CN30EC97VARN80D=postback-pendapatan-iklan-dalam-aplikasi-iaa 01H7T1DS6TCA8338NAD9Q8CJWW=what-are-the-iaa-postback-data-sources 01H7T1DS6TQ2G43HSQMH8Y6Q4H=what-processing-is-performed-on-the-iaa-postback-data 01H7T1DS6TQZA3W9KE3783G9G1=how-is-the-postback-data-delivered inapp-purchase-iap-postbacks=postback-pembelian-dalam-aplikasi-iap 01H7T1DS6TH8AV2ZTY3M8ZXPYA=postback-pembelian-dalam-aplikasi-iap 01H7T1DS6TGF4XEMD4CRBD8QS2=what-are-the-iap-postback-data-sources 01H7T1DS6T9W85F40QQ2497RNW=what-data-processing-is-performed-on-the-iap-postback-data 01H7T1DS6VAPRMCGZ9YCPTA9EQ=how-is-the-postback-delivered 01H7T1DS6VKE2G6XR02VF4TWH4=what-are-the-iap-events" />
