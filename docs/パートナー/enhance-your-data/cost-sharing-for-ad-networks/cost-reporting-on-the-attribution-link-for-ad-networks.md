---
title: クリックでのコスト計測：アドネットワーク向け
metadata:
  keywords:
    - cost sharing
    - cost
    - Agencies
    - Ad Networks
    - Partners
    - Marketers
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - Marketers
    - ROI360
    - Ad Networks
  created_at: '2017-02-12T14:54:50Z'
  edited_at: '2026-10-14T09:30:04Z'
  id: 115000748446
  locale: ja
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ja/articles/115000748446
---
> **概要：** アドネットワークは広告のクリック毎（=計測URLの発火毎）にコスト情報をAppsFlyerへ共有することが可能です。

広告主は、AppsFlyerの管理画面をすべての予算配分の決定における信頼できる情報源として利用し、投資すべき配信先を簡単に確認することが可能です。このプロセスにおいてより可視化されたい場合に、連携済みパートナーはAppsFlyerに対してコストデータを共有することが必要不可欠です。

多くの場合、広告主はROIでソートして優れたパフォーマンスを発揮しているパートナーはどこなのかを確認しています。このとき、コストデータがないパートナーは常にリストの一番下の表示されてしまいます。

![](https://files.readme.io/ce5b7a7c4af1c016f4f8b2ad72c96c36456a73513e0ba19b8049e1e6fd286ef6-115002046163.png)

## コスト情報の共有方法

AppsFlyerの計測URLを介してユーザーレベルのコストデータを渡すには、非暗号化 / 暗号化の2つがあります。暗号化されたコストパスにより、パートナーはクリックアトリビューションURLにコスト値を送信することができます。

**暗号化していないコスト情報**の場合、以下3つのパラメータをクリックURLにハードコーディングする形で渡すことが可能です：

* af\_cost\_model=CPI （現状はCPIモデルのみが計測可能です。）
* af\_cost\_value=`{CPIの値 - 例：1.00}`  
  　**注：** 1より小さい値の場合は、小数の前に0が必要です：0.05
* af\_cost\_currency=`{3桁の国コード - 空欄の場合はUSD}`

*注記：*計測URLを介して任意のコストモデルを送信できますが、管理画面上でのコストデータの表示は現状CPIのみ対応しています。それ以外のコストモデルは、ローデータレポートでのみ確認可能ですので注意してください。

暗号化していないコスト情報がある計測URLのサンプル：

```http
https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD- 
A12345678910&af_siteid=12345&af_cost_model=CPI&af_cost_value=1.00&af_cost_currency=USD
```

**暗号化したコスト情報**

計測URL上に実際のコストの値を表示したくない場合には、コストに関するパラメータを暗号化できます。暗号化したコスト情報は、AES基準の暗号化方式に従って渡すことが可能です。コストモデル、コスト値、通貨単位に加え、パートナーは暗号化したコスト値を解読するためのネットワーク固有のキーが必要になります。

暗号化の手順：

1. あなたのPSEチームに**ネットワーク暗号化キー**をリクエストしてください<Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/51858295256977">パートナーアシスタントウィジェット</Anchor>.
2. AES暗号化方式(以下参照)を使用して、必要な4つの値（**ネットワークキー、コスト値、コストモデル、および通貨単位**）を暗号化してください。
3. **af\_enc\_data=** のパラメータで、生成した暗号化値をAppsFlyerの計測URLに追加してください。

暗号化した値を持つ計測URLのサンプル：

https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD-A12345678910&af_siteid=12345 **&af\_enc\_data=DvVvQRow%2F2N0LiQGZh0wvwucFygbll9IwAMSN%2B%2BDQxo%3D**

**注記：** AppsFlyerとコストの暗号化連携を実行したアドネットワークのみが、暗号化したコスト情報を広告主の計測URLと共に実際に送信できます。

## AESの暗号化プロセス

暗号化を成功させるには、<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_.28ECB.29">**ECB block mode**</Anchor>と一緒に、<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7">**PKCS5 paddhing**</Anchor>を使いながら、<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">**AESアルゴリズムを**</Anchor>使用する必要があります。そして、暗号化されたデータを<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Base64">**Base 64でエンコード**</Anchor>し、最後に結果を<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Percent-encoding">**URLエンコード**</Anchor>する必要があります。

各パートナーは、これを克服するために任意の方法を利用可能です。PHP、Java、Pythonの以下の例を参照してください：

PHP

```php
<?php
$f = fopen( 'php://stdin', 'r' );
echo "Enter private key: ";
$private_key = trim(fgets($f));
echo "Enter cost model: ";
$cost_model = trim(fgets($f));
echo "Enter cost value : ";
$cost_value = trim(fgets($f));
echo "Enter cost currency : ";
$cost_currency = trim(fgets($f));
$params = array(
	'af_cost_model' => $cost_model,
	'af_cost_value' => $cost_value,
	'af_cost_currency' => $cost_currency
);
$query_str = http_build_query($params);
$block_size = mcrypt_get_block_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_ECB);
$padding_size = $block_size - (strlen($query_str) % $block_size);
$padded_query_str = $query_str . str_repeat(chr($padding_size), $padding_size);
$enc_raw = mcrypt_encrypt(MCRYPT_RIJNDAEL_128, $private_key, $padded_query_str, "ecb");
$enc_b64 = base64_encode($enc_raw);
$enc_url_encoded = urlencode($enc_b64);
echo "\n\n\r";
echo "Private key: " . $private_key . "\r\n";
echo "Query string: " . $query_str . "\r\n";
echo "\n\r";
echo "Encrypted query string: " . $enc_url_encoded . "\r\n";
fclose( $f );
?>
```

Java

```java
private static final String CIPHER_ALGORITHM = "AES/ECB/PKCS5Padding";
private static final String encryptionKey = "XXXXXXXXXXXXXXXX"; // secret key provided by appsflyer
private static final SecretKeySpec key = new SecretKeySpec(encryptionKey.getBytes(), "AES");
public static void main(String[] args) throws Exception {
  String queryParams = "bid_value=0.01&bid_type=cpc";
  String cipher = encrypt(queryParams);
  System.out.println(cipher);
}
public static String encrypt(String str) throws Exception {
  Cipher cipherEncrypt = Cipher.getInstance(CIPHER_ALGORITHM);
  cipherEncrypt.init(Cipher.ENCRYPT_MODE, key);
  byte[] cipher = cipherEncrypt.doFinal(str.getBytes("UTF-8"));
  String b64 = encode64(cipher);
  String result = urlencode(b64);
  return result;
}
```

Python

```python
import sys
import base64
import urllib
from Crypto.Cipher import AES
def read_number(t):
  try:
    start = input("enter " + t + ": ")
    start = float(start)
    return start
  except ValueError:
    print("\n\r" + t + " must be a number")
    exit()
def encrypt (secret_key, msg):
  cipher = AES.new(secret_key, AES.MODE_ECB)
  ciphertext = cipher.encrypt(msg)
  return ciphertext
def padding (data):
  length = 16 - (len(data) % 16)
  data += chr(length)*length
  return data

secret_key = input("enter secret key: ").strip()
currency = input("enter cost currency: ").strip()
model = "CPI"
if len(currency) == 3:
  currency = currency.upper()
else:
  print("currency must have 3 character (e.g. USD)")
  exit()
start = read_number("starting value")
end = read_number("final value")
step = read_number("step")
if end >= start:
  while start <= end:
    msg = "af_cost_currency=%s&af_cost_model=%s&af_cost_value=%.2f" % (currency, model, start)
    msg = padding(msg)
    enc = encrypt(secret_key, msg)
    start += step
print(msg)
print(urllib.quote_plus(base64.b64encode(enc)))
```

## コスト計測をサポートしているアドネットワーク

クリックでのコスト計測をサポートしている全媒体を確認するには、こちらを参照してください。

クリックでのコスト計測をサポートしている全媒体を確認するには、こちらを参照してください。

<div data-zendesk-anchors="how-to-share-cost=%E3%82%B3%E3%82%B9%E3%83%88%E6%83%85%E5%A0%B1%E3%81%AE%E5%85%B1%E6%9C%89%E6%96%B9%E6%B3%95 h_01J292SNHC1B88FBJJW1PY5YT2=%E3%82%B3%E3%82%B9%E3%83%88%E6%83%85%E5%A0%B1%E3%81%AE%E5%85%B1%E6%9C%89%E6%96%B9%E6%B3%95 aes-encryption-process=aes%E3%81%AE%E6%9A%97%E5%8F%B7%E5%8C%96%E3%83%97%E3%83%AD%E3%82%BB%E3%82%B9 h_01J292SNHCFG8QP8KK058EVEVQ=aes%E3%81%AE%E6%9A%97%E5%8F%B7%E5%8C%96%E3%83%97%E3%83%AD%E3%82%BB%E3%82%B9 which-networks-support-cost-reporting=%E3%82%B3%E3%82%B9%E3%83%88%E8%A8%88%E6%B8%AC%E3%82%92%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF h_01J292SNHCVFR5GW4ECBYM63S6=%E3%82%B3%E3%82%B9%E3%83%88%E8%A8%88%E6%B8%AC%E3%82%92%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%81%97%E3%81%A6%E3%81%84%E3%82%8B%E3%82%A2%E3%83%89%E3%83%8D%E3%83%83%E3%83%88%E3%83%AF%E3%83%BC%E3%82%AF" />
