---
title: Cost reporting on the attribution link for ad networks
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
  edited_at: '2026-06-22T10:03:59Z'
  id: 115000748446
  locale: en-us
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/115000748446-Cost-reporting-on-the-attribution-link-for-ad-networks
---
**At a glance:** Ad networks can report cost every time an ad is clicked.

Advertisers use the AppsFlyer dashboard as their source of truth for all budget allocation decisions, making it easy to see where to invest. For networks wanting to be visible in that process, sharing cost data with AppsFlyer is an absolute must.

Advertisers often check their top-performing partners using sort by ROI. Those that have no cost data always appear at the bottom of the list.

![](https://files.readme.io/ce5b7a7c4af1c016f4f8b2ad72c96c36456a73513e0ba19b8049e1e6fd286ef6-115002046163.png)

## How to share cost

There are two ways to pass user-level cost data through AppsFlyer attribution URLs: unencrypted and encrypted. Encrypted cost pass allows partners to send cost value in the click attribution URL.

**Unencrypted cost** can be passed by hardcoding the following 3 parameters to the click URL:

* af\_cost\_model=CPI (currently CPI is the only model viewable in AppsFlyer reporting)
* af\_cost\_value=`{insert CPI value, for example: 1.00}`  
  **Note**: Values less than 1 require a 0 before the decimal, for example: 0.05.
* af\_cost\_currency=`{insert 3 letter currency code. If blank we will assume USD}`

*NOTE*: While any cost model can be sent via the attribution link, only CPI is currently supported for presenting cost data on the dashboard. Other cost models are available in the raw reports.

An example of an attribution Link with an unencrypted cost pass:

```
https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD- 
A12345678910&af_siteid=12345&af_cost_model=CPI&af_cost_value=1.00&af_cost_currency=USD
```

**Encrypted cost**

If you prefer not to reveal the actual cost value in the attribution URL, you can encrypt the cost parameters. The encrypted cost can be passed by following an AES-based encryption method. In addition to the cost model, value, and currency, partners will need a network-specific key to generate the encrypted cost value.

Steps for encryption:

1. Request your **network encryption key** from your PSE team using the <Anchor target="_blank" href="https://files.readme.io/fdc0cc0d6ff35e06535dc5cc94b4aed0901a94031a4306fa29f744d4521086d7-34951742603025.gif">partner assistant widget</Anchor>.
2. Use the AES encryption method (shown below) to encrypt the required 4 values (**network key, cost value, cost model, and cost currency**)
3. Append the generated encryption value to your AppsFlyer attribution URL in the **af\_enc\_data=** parameter.

Sample attribution link with encrypted value pass:

https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD-A12345678910&af_siteid=12345 **&af\_enc\_data=DvVvQRow%2F2N0LiQGZh0wvwucFygbll9IwAMSN%2B%2BDQxo%3D**

**Note:** Only ad networks that perform the cost encryption integration with AppsFlyer can actually send encrypted cost data with their clients' attribution links.

## AES encryption process

To accomplish the encryption, partners must use the <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">**AES algorithm**</Anchor>, with an <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_.28ECB.29">**ECB block mode**</Anchor>, using <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7">**PKCS5 padding**</Anchor>. Then they must <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Base64">**Base-64 encode**</Anchor> the encrypted data, and finally, <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Percent-encoding">**URL-encode**</Anchor> the result.

Networks can use any tech stack to accomplish this. See examples below for PHP, Java, and Python:

PHP

```
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

## Which networks support cost reporting?

To see a full list of the networks that support cost reporting on the attribution link, click <Anchor target="_blank" href="/marketers/docs/view-aggregated-cost-data-for-attribution-links#ad-networks-providing-cost-by-click-data">here</Anchor>.

To see a full list of the networks that support cost reporting via API, click <Anchor target="_blank" href="/marketers/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">here</Anchor>.

<div data-zendesk-anchors="h_01J292SNHC1B88FBJJW1PY5YT2=how-to-share-cost h_01J292SNHCFG8QP8KK058EVEVQ=aes-encryption-process h_01J292SNHCVFR5GW4ECBYM63S6=which-networks-support-cost-reporting" />
