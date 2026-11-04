---
title: Отчёты о затратах по ссылке атрибуции для рекламных сетей
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
  edited_at: '2026-09-02T00:36:30Z'
  id: 115000748446
  locale: ru
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/ru/articles/115000748446
---
> **Краткий обзор:** Рекламные сети могут отчитываться о затратах при каждом клике по рекламе.

Рекламодатели используют дэшборд AppsFlyer как источник правды для всех решений по распределению бюджета, что позволяет им лучше понимать, куда инвестировать средства. Для сетей, которые хотят быть заметными в этом процессе, отправка данных о затратах в AppsFlyer является абсолютной необходимостью.

Рекламодатели нередко смотрят, какие из партнёров являются наиболее эффективными, сортируя всех партнёров по ROI. Те, кто не передаёт данные о затратах, всегда оказываются внизу списка.

![](https://files.readme.io/ce5b7a7c4af1c016f4f8b2ad72c96c36456a73513e0ba19b8049e1e6fd286ef6-115002046163.png)

<div id="how-to-share-cost" />

## Как делиться затратами

Существует два способа передачи данных о затратах на уровне пользователя через URL-адреса атрибуции AppsFlyer: нешифрованный и зашифрованный. Зашифрованная передача затрат позволяет партнёрам отправлять значения затрат в URL-адресе атрибуции клика.

**Нешифрованные затраты** могут быть переданы с помощью жёсткого кодирования следующих трёх параметров в URL-адрес клика:

* af\_cost\_model=CPI (в настоящее время CPI является единственной моделью, доступной к просмотру в отчётах AppsFlyer)
* af\_cost\_ значение=`{вставьте значение CPI, например: 1.00}`   
  **Примечание**: Если значение меньше 1, то перед десятичным разделителем необходимо ставить 0, например: 0.05.
* af\_cost\_currency=`{вставьте трёхбуквенный код валюты. Если значение не задано, по умолчанию предполагается USD}`

*ПРИМЕЧАНИЕ*: Хотя через ссылку атрибуции можно отправлять любую модель затрат, в настоящее время для представления данных о затратах на дэшборде поддерживается только CPI. Другие модели затрат доступны в отчётах о сырых данных.

Пример ссылки атрибуции с нешифрованной передачей затрат:

```http
https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD- 
A12345678910&af_siteid=12345&af_cost_model=CPI&af_cost_value=1.00&af_cost_currency=USD
```

**Зашифрованные затраты**

Если вы предпочитаете не раскрывать фактическое значение затрат в URL-адресе атрибуции, вы можете зашифровать параметры затрат. Зашифрованная стоимость может быть передана с использованием метода шифрования на основе AES. В дополнение к модели затрат, значению и валюте, партнёрам для генерации зашифрованного значения стоимости потребуется ключ, специфичный для данной сети.

Этапы шифрования:

1. Запросите **ключ шифрования сети** у своей команды PSE через виджет <Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/38468505364625">ассистента для партнёров</Anchor>.
2. Используйте метод шифрования AES (показан ниже), чтобы зашифровать необходимые 4 значения (**ключ сети, значение затрат, модель затрат и валюту затрат**).
3. Добавьте сгенерированное зашифрованное значение к вашему URL-адресу атрибуции AppsFlyer в параметре **af\_enc\_data=**.

Пример ссылки атрибуции с передачей зашифрованного значения:

https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD-A12345678910&af_siteid=12345 **&af\_enc\_data=DvVvQRow%2F2N0LiQGZh0wvwucFygbll9IwAMSN%2B%2BDQxo%3D**

**Примечание:** Только рекламные сети, которые выполняют интеграцию шифрования затрат с AppsFlyer, могут отправлять зашифрованные данные о затратах с ссылками атрибуции своих клиентов.

<div id="aes-encryption-process" />

## Процесс шифрования AES

Для шифрования, партнёрам необходимо использовать <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">**алгоритм AES**</Anchor>, в <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_.28ECB.29">**режиме блочного шифра ECB (режим простой замены)**</Anchor>, используя <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7">**дополнение PKCS5**</Anchor>. Затем необходимо применить <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Base64">**кодирование стандарта Base64**</Anchor> к зашифрованным данным, и, наконец, <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Percent-encoding">**закодировать результат с помощью URL-шифрования**</Anchor> результат.

Для этих задач сети могут использовать любой технологический стек. Ниже см. примеры для PHP, Java и Python:

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
private static final String encryptionKey = "XXXXXXXXXXXXXXXX"; // секретный ключ, предоставленный AppsFlyer
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

## Какие сети поддерживают отчётность по затратам?

Полный список сетей, которые поддерживают отчёты о затратах по ссылке атрибуции, нажмите <Anchor target="_blank" href="/marketers/ru/docs/view-aggregated-cost-data-for-attribution-links#ad-networks-providing-cost-by-click-data">здесь</Anchor>.

Полный список сетей, которые поддерживают отчёты о затратах через API, нажмите <Anchor target="_blank" href="/marketers/ru/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">здесь</Anchor>.

<div data-zendesk-anchors="how-to-share-cost=%D0%BA%D0%B0%D0%BA-%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C%D1%81%D1%8F-%D0%B7%D0%B0%D1%82%D1%80%D0%B0%D1%82%D0%B0%D0%BC%D0%B8 h_01J292SNHC1B88FBJJW1PY5YT2=%D0%BA%D0%B0%D0%BA-%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C%D1%81%D1%8F-%D0%B7%D0%B0%D1%82%D1%80%D0%B0%D1%82%D0%B0%D0%BC%D0%B8 aes-encryption-process=%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81-%D1%88%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-aes h_01J292SNHCFG8QP8KK058EVEVQ=%D0%BF%D1%80%D0%BE%D1%86%D0%B5%D1%81%D1%81-%D1%88%D0%B8%D1%84%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F-aes which-networks-support-cost-reporting=%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5-%D1%81%D0%B5%D1%82%D0%B8-%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%B2%D0%B0%D1%8E%D1%82-%D0%BE%D1%82%D1%87%D1%91%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%BF%D0%BE-%D0%B7%D0%B0%D1%82%D1%80%D0%B0%D1%82%D0%B0%D0%BC h_01J292SNHCVFR5GW4ECBYM63S6=%D0%BA%D0%B0%D0%BA%D0%B8%D0%B5-%D1%81%D0%B5%D1%82%D0%B8-%D0%BF%D0%BE%D0%B4%D0%B4%D0%B5%D1%80%D0%B6%D0%B8%D0%B2%D0%B0%D1%8E%D1%82-%D0%BE%D1%82%D1%87%D1%91%D1%82%D0%BD%D0%BE%D1%81%D1%82%D1%8C-%D0%BF%D0%BE-%D0%B7%D0%B0%D1%82%D1%80%D0%B0%D1%82%D0%B0%D0%BC" />
