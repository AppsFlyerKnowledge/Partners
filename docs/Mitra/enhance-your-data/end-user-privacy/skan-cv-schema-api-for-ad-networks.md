---
title: API SKAN CV skema untuk jaringan iklan
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
  edited_at: '2023-03-05T14:40:05Z'
  id: 11705009866001
  locale: id
  section: End-user privacy
  section_id: 6551186412689
  url: https://support.appsflyer.com/hc/id/articles/11705009866001
---
> **Sekilas**: Lihat skema CV SKAN seperti yang dipetakan oleh pemasang iklan.

## API SKAN CV skema untuk jaringan iklan

Dengan atribusi SKAdNetwork (SKAN), pemasang iklan menilai kualitas pengguna dengan menetapkan nilai konversi (CV) berdasarkan aktivitas pengguna setelah penginstalan selama jangka waktu tertentu (windows/jendela). <Anchor target="_blank" href="/marketers/id/docs/skadnetwork-skan-solution-guide">Pelajari lebih lanjut tentang SKAN</Anchor>

iOS melaporkan CV melalui postback yang dikirim ke jaringan iklan yang memasang iklan. Mulai iOS 15, pemasang iklan juga dapat menginstruksikan iOS untuk mengirimkan postback secara langsung ke AppsFlyer.

API ini memberikan peta CV-ke-atribusi-event-dan-nilai ke jaringan iklan. Jaringan iklan menggunakannya untuk mengkodekan postback yang mereka terima.

API kembali sebagai JSON bersarang. Skema untuk setiap aplikasi terpisah. Pemetaan per CV terdapat dalam larik conversion\_value\_mapping.

Untuk menggunakan API, minta developer Anda untuk mengikuti <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/overview">API skema SKAN CV mereka untuk petunjuk jaringan iklan</Anchor>. Untuk daftar kunci dan deskripsinya, klik 200 di simulator.

**Catatan**:

* Kisaran nilai CV adalah:
  * Nilai halus SKAN 4 jendela 1: 0-63.
  * SKAN 4 jendela 1, 2, dan 3 nilai kasar: rendah, sedang, atau tinggi.
  * SKAN 3 ke bawah: 0-63
* Pemasang iklan dapat mengubah pemetaan CV kapan saja.
* Anda, jaringan iklan, harus mengkueri API ini setiap hari, untuk memastikan bahwa Anda memiliki skema terbaru.

<div data-zendesk-anchors="skan-cv-schema-api-for-ad-networks=api-skan-cv-skema-untuk-jaringan-iklan" />
