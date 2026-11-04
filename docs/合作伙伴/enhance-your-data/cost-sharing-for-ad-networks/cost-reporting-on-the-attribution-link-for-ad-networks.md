---
title: 广告平台通过归因链接上报成本数据
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
  edited_at: '2026-10-14T10:06:59Z'
  id: 115000748446
  locale: zh-cn
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/zh-cn/articles/115000748446
---
> **概要：** 每当用户点击广告时，广告平台都可以通过归因链接上报对应的广告成本。

广告主可使用AppsFlyer面板作为预算分配决策的唯一可信参考依据，清晰了解预算投放方向。希望在这一过程中获得曝光的广告平台应及时与AppsFlyer对接成本数据。

广告主常常会通过“按ROI排序”查看表现最佳的合作渠道。未对接成本数据的渠道始终会排在列表底部，难以获得关注。

![](https://files.readme.io/ce5b7a7c4af1c016f4f8b2ad72c96c36456a73513e0ba19b8049e1e6fd286ef6-115002046163.png)

<div id="how-to-share-cost" />

## 如何上报成本数据

广告平台可通过AppsFlyer归因链接以两种方式传递用户层级的成本数据：加密传输及为加密传输。加密传输方式允许广告平台将成本值以加密形式附加在点击归因链接中。

要通过**未加密**方式传输，可在点击链接中直接写入以下3个参数：

* af\_cost\_model=CPI（AppsFlyer报告中仅支持展示CPI模式的成本数据）
* af\_cost\_value=`{插入CPI值，例如：1.00}`  
  **注意**：若数值小于1，必须在小数点前加0，例如：0.05.
* af\_cost\_currency=`{填写三位货币代码，例如：USD；如为空，系统默认使用USD}`

*注意*：虽然归因链接可以传递任意成本模式，但目前AppsFlyer面板仅支持以CPI模式展示成本数据。其他成本模式仅可在原始报告中查看。

带有未加密成本传递的归因链接示例：

```http
https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD- 
A12345678910&af_siteid=12345&af_cost_model=CPI&af_cost_value=1.00&af_cost_currency=USD
```

**加密成本传输**

若不希望在归因链接中暴露真实成本值，可通过AES加密方式对成本参数进行加密。除了成本模式、数值和币种外，广告平台还需使用平台专属的密钥来生成加密后的成本数据。

加密步骤:

1. 通过<Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/37302578554897">PSE团队</Anchor>或渠道支持微件工具，申请您的**平台专属加密密钥**（network encryption key）；
2. 使用AES加密方法（如下所示）对4个值进行加密 (**network key, cost value, cost model, and cost currency**)
3. 将生成的加密值作为**af\_enc\_data=** 参数附加到AppsFlyer归因链接。

包含加密成本参数的归因链接：

https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD-A12345678910&af_siteid=12345 **&af\_enc\_data=DvVvQRow%2F2N0LiQGZh0wvwucFygbll9IwAMSN%2B%2BDQxo%3D**

**注意：** 只有完成与AppsFlyer加密成本对接的广告平台，才可通过归因链接为其客户传递加密成本数据。

<div id="aes-encryption-process" />

## AES加密流程

广告平台需使用<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">**AES加密算法**</Anchor>，<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_.28ECB.29">**采用ECB模式**</Anchor>和<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7">**PKCS5填充方式**</Anchor>，对成本数据进行加密处理。加密后的数据需进行<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Base64">**Base-64编码**</Anchor>，最后再进行<Anchor target="_blank" href="https://en.wikipedia.org/wiki/Percent-encoding">**URL编码**</Anchor>，并作为af\_enc\_data=参数附加在归因链接中。

加密操作可使用任意技术栈完成。以下提供PHP、Java和Python的示例代码。

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

java

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

<div id="which-networks-support-cost-reporting" />

## 哪些广告平台支持成本上报？

如需查看支持通过归因链接上报成本数据的广告平台完整列表，请点击此处<Anchor target="_blank" href="/marketers/zh/docs/view-aggregated-cost-data-for-attribution-links#ad-networks-providing-cost-by-click-data">查看</Anchor>。

如需查看支持通过API上报成本数据的广告平台完整列表，请点击<Anchor target="_blank" href="/marketers/zh/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">此处</Anchor>查看。

<div data-zendesk-anchors="how-to-share-cost=%E5%A6%82%E4%BD%95%E4%B8%8A%E6%8A%A5%E6%88%90%E6%9C%AC%E6%95%B0%E6%8D%AE h_01J292SNHC1B88FBJJW1PY5YT2=%E5%A6%82%E4%BD%95%E4%B8%8A%E6%8A%A5%E6%88%90%E6%9C%AC%E6%95%B0%E6%8D%AE aes-encryption-process=aes%E5%8A%A0%E5%AF%86%E6%B5%81%E7%A8%8B h_01J292SNHCFG8QP8KK058EVEVQ=aes%E5%8A%A0%E5%AF%86%E6%B5%81%E7%A8%8B which-networks-support-cost-reporting=%E5%93%AA%E4%BA%9B%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E6%94%AF%E6%8C%81%E6%88%90%E6%9C%AC%E4%B8%8A%E6%8A%A5 h_01J292SNHCVFR5GW4ECBYM63S6=%E5%93%AA%E4%BA%9B%E5%B9%BF%E5%91%8A%E5%B9%B3%E5%8F%B0%E6%94%AF%E6%8C%81%E6%88%90%E6%9C%AC%E4%B8%8A%E6%8A%A5" />
