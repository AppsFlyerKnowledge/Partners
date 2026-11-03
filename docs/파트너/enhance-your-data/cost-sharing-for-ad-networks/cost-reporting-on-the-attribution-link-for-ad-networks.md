---
title: 광고 네트워크를 위한 어트리뷰션 링크에 대한 비용 리포팅
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
  edited_at: '2026-10-14T10:26:42Z'
  id: 115000748446
  locale: ko
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ko/articles/115000748446
---
> **한눈에 보기:** 애드 네트워크는 광고가 클릭될 때마다 비용을 보고할 수 있습니다.

모든 예산 할당 결정을 할 때 AppsFlyer 대시보드를 사용하는 광고주는 손쉽게 투자 장소를 확인할 수 있습니다. 이 과정에서 가시성을 보이고자 하는 네트워크의 경우, 앱스플라이어와 비용 데이터 공유는 반드시 필수입니다.

광고주는 ROI에 따라 정렬하여 성과가 가장 좋은 파트너를 확인합니다. 비용 데이터가 없는 항목은 항상 목록의 바닥에 표시됩니다.

![](https://files.readme.io/ce5b7a7c4af1c016f4f8b2ad72c96c36456a73513e0ba19b8049e1e6fd286ef6-115002046163.png)

## 비용을 공유하는 방법

앱스플라이어 어트리뷰션 URL을 통해 사용자 수준의 비용 데이터를 전달하는 방법에는 두 가지가 있습니다. 암호화되지 않거나 암호화됩니다. 암호화된 비용 패스를 사용하면 파트너가 클릭 어트리뷰션 URL에서 비용 가치를 보낼 수 있습니다.

**암호화되지 않은 비용은** 다음 3개의 파라미터를 클릭 URL에 하드코딩하여 전달할 수 있습니다.

* af\_cost\_model=CPI (현재 CPI는 앱스플라이어 리포팅에서 볼 수 있는 유일한 모델)
* af\_cost\_ value=`{CPI 값 입력(예: 1.00}`  
  **참고**: 1 미만의 값은 소수점 앞의 0을 필요로 합니다. 예: 0.05.
* af\_cost\_currency= 3 글자 통화 코드 삽입 공백인 경우 USD}를 가정합니다.

*참고:* 어트리뷰션 링크를 통해 모든 비용 모델이 전송될 수 있지만, 현재 대시보드에서 비용 데이터를 표시할 때 CPI만 지원됩니다. 다른 비용 모델은 로데이터 보고서에서 확인할 수 있습니다.

암호화되지 않은 비용 패스가 있는 어트리뷰션 링크 예시:

```http
https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD- 
A12345678910&af_siteid=12345&af_cost_model=CPI&af_cost_value=1.00&af_cost_currency=USD
```

**암호화된 비용**

어트리뷰션 URL에서 실제 비용 값을 공개하지 않으려면 비용 파라미터를 암호화할 수 있습니다. 암호화된 비용은 AES 기반 암호화 방법을 통해 전달될 수 있습니다. 비용 모델, 값 및 통화 외에도 암호화된 비용 값을 생성하기 위해 파트너에게 네트워크별 키가 필요합니다.

암호화 단계:

1. <Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/51858309585681">파트너 어시스트 위젯</Anchor>을 사용하여 PSE 팀으로부터 **네트워크 암호화 키를 요청하세요**.
2. 아래에 표시된 AES 암호화 방법을 사용하여 필요한 4개의 값(**네트워크 키, 비용 값, 비용 모델 및 비용 통화**)을 암호화합니다.
3. 생성된 암호화 값을 앱스플라이어 어트리뷰션 URL에 **af\_enc\_data=** 파라미터에 추가합니다.

암호화된 값 전송 링크 샘플 어트리뷰션:

https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD-A12345678910&af_siteid=12345 **&af\_enc\_data=DvVvQRow%2F2N0LiQGZh0wvucFygbll9IwAMSN%2B%2BDQxo%3D**

**참고:** 앱스플라이어와 비용 암호화 연동을 수행하는 광고 네트워크만이 실제로 고객의 어트리뷰션 링크와 암호화된 비용 데이터를 보낼 수 있습니다.

## AES 암호화 프로세스

암호화를 완료하려면 파트너는 <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7">**PKCS5 패딩을**</Anchor> 사용하여 <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_.28ECB.29">**ECB 블록 모드와**</Anchor> <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">**AES 알고리즘을**</Anchor> 사용해야 합니다. 그런 다음 <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Base64">**Base-64 인코딩**</Anchor>해야 합니다 암호화된 데이터, 마지막으로 <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Percent-encoding">**URL 인코딩**</Anchor> 결과.

네트워크는 이를 위해 어떤 기술 스택을 사용하든 사용할 수 있습니다. 아래 예시를 참고하십시오: PHP, Java, Python

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

피썬

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

## 어떤 네트워크가 비용 리포트를 지원하나요?

어트리뷰션 링크에서 비용 리포팅을 지원하는 네트워크의 전체 목록을 보려면 <Anchor target="_blank" href="/marketers/ko/docs/view-aggregated-cost-data-for-attribution-links#ad-networks-providing-cost-by-click-data">여기를 클릭하십시오</Anchor>.

API를 통해 비용 리포팅을 지원하는 네트워크의 전체 목록을 보려면 <Anchor target="_blank" href="/marketers/ko/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">여기를 클릭하십시오</Anchor>.

<div data-zendesk-anchors="how-to-share-cost=%EB%B9%84%EC%9A%A9%EC%9D%84-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95 h_01J292SNHC1B88FBJJW1PY5YT2=%EB%B9%84%EC%9A%A9%EC%9D%84-%EA%B3%B5%EC%9C%A0%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95 aes-encryption-process=aes-%EC%95%94%ED%98%B8%ED%99%94-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4 h_01J292SNHCFG8QP8KK058EVEVQ=aes-%EC%95%94%ED%98%B8%ED%99%94-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4 which-networks-support-cost-reporting=%EC%96%B4%EB%96%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EA%B0%80-%EB%B9%84%EC%9A%A9-%EB%A6%AC%ED%8F%AC%ED%8A%B8%EB%A5%BC-%EC%A7%80%EC%9B%90%ED%95%98%EB%82%98%EC%9A%94 h_01J292SNHCVFR5GW4ECBYM63S6=%EC%96%B4%EB%96%A4-%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC%EA%B0%80-%EB%B9%84%EC%9A%A9-%EB%A6%AC%ED%8F%AC%ED%8A%B8%EB%A5%BC-%EC%A7%80%EC%9B%90%ED%95%98%EB%82%98%EC%9A%94" />
