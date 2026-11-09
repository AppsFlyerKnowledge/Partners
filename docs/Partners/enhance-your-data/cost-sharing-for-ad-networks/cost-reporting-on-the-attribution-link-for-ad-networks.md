---
title: Reportes de costo sobre el enlace de atribución para ad networks
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
  edited_at: '2026-08-12T12:27:56Z'
  id: 115000748446
  locale: es
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/es/articles/115000748446
---
> **En resumen:** Las ad networks pueden reportar el costo cada vez que se hace clic en un anuncio.

Los anunciantes utilizan el dashboard de AppsFlyer como fuente fiable para todas las decisiones de asignación presupuestaria, lo que facilita ver dónde invertir. Para las redes que desean ser visibles en ese proceso, compartir los datos de costos con AppsFlyer es una necesidad absoluta.

Los anunciantes suelen comprobar a sus partners con mejor rendimiento ordenándolos por el ROI. Los que no tienen datos de costos siempre aparecen al final de la lista.

<Image align="center" alt="" src="https://files.readme.io/ce5b7a7c4af1c016f4f8b2ad72c96c36456a73513e0ba19b8049e1e6fd286ef6-115002046163.png" />

<div id="how-to-share-cost" />

## Cómo compartir los costos

Hay dos maneras de pasar los datos de costos a nivel de usuario a través de las URL de atribución de AppsFlyer: cifrados y sin cifrar. La transmisión de costos cifrada permite a los partners enviar el valor del costo en la URL de atribución del clic.

**El costo sin cifrar** se puede transferir codificando los siguientes 3 parámetros en la URL del clic:

* af\_cost\_model=CPI (actualmente, el CPI es el único modelo que se puede ver en los reportes de AppsFlyer)
* af\_cost\_ value=`{inserta el valor del CPI, por ejemplo: 1.00}`  
  **Nota**: Los valores inferiores a 1 requieren un 0 antes del decimal, por ejemplo: 0.05.
* af\_cost\_currency=`{inserta un código de divisa de 3 letras. Si está en blanco, asumiremos que es USD}`

*NOTA*: Si bien cualquier modelo de costo se puede enviar a través del enlace de atribución, actualmente solo se admite el CPI para presentar los datos de costos en el panel de control. Otros modelos de costos están disponibles en los reportes de raw data.

Un ejemplo de enlace de atribución con transmisión de costo sin cifrar:

```http
https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD- 
A12345678910&af_siteid=12345&af_cost_model=CPI&af_cost_value=1.00&af_cost_currency=USD
```

**Costo cifrado**

Si prefieres no revelar el valor de costo real en la URL de atribución, puedes cifrar los parámetros de costo. El costo cifrado se puede transmitir siguiendo un método de cifrado basado en AES. Además del modelo de costo, el valor y la divisa, los partners necesitarán una clave específica de la red para generar el valor de costo cifrado.

Pasos para el cifrado:

1. Solicita tu **clave de red cifrado** a tu equipo de PSE mediante el <Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/36156242411537">widget partner assistant</Anchor>.
2. Utiliza el método de cifrado AES (que se muestra a continuación) para cifrar los 4 valores necesarios (**clave de red, valor de costo, modelo de costo y divisa de costo**).
3. Agrega el valor de cifrado generado a tu URL de atribución de AppsFlyer, en el parámetro **af\_enc\_data=**.

Ejemplo de enlace de atribución con transmisión de valor cifrado:

https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD-A12345678910&af_siteid=12345 **&af\_enc\_data=DvVvQRow%2F2N0LiQGZh0wvwucFygbll9IwAMSN%2B%2BDQxo%3D**

**Nota:** Solo las ad networks que realizan la integración del cifrado de costos con AppsFlyer pueden enviar datos de costos cifrados con los enlaces de atribución de sus clientes.

<div id="aes-encryption-process" />

## Proceso de cifrado AES

Para lograr el cifrado, los partners deben usar el <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">**algoritmo AES**</Anchor>, con un <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_.28ECB.29">**modo de bloqueo ECB**</Anchor>, utilizando el relleno <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7">**PKCS5**</Anchor>.  Luego, deben <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Base64">**codificar en Base-64**</Anchor> los datos cifrados y, por último, <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Percent-encoding">**codificar en URL**</Anchor> el resultado.

Las redes pueden usar cualquier pila tecnológica para lograr esto. Consulta los ejemplos siguientes para PHP, Java y Python:

PHP

```php
<?php
$f = fopen( 'php://stdin', 'r' );
echo "Introduce la clave privada: ";
$private_key = trim(fgets($f));
echo "Introduce el modelo de Costo: ";
$cost_model = trim(fgets($f));
echo "Introduce el valor del Costo : ";
$cost_value = trim(fgets($f));
echo "Introduce la moneda del Costo : ";
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
echo "Clave privada: " . $private_key . "\r\n";
echo "Cadena de consulta: " . $query_str . "\r\n";
echo "\n\r";
echo "Cadena de consulta cifrada: " . $enc_url_encoded . "\r\n";
fclose( $f );
?>
```

Java

```java
private static final String CIPHER_ALGORITHM = "AES/ECB/PKCS5Padding";
private static final String encryptionKey = "XXXXXXXXXXXXXXXX"; // clave secreta proporcionada por AppsFlyer
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
from Crypto. Cipher import AES
def read_number(t):
  try:
    start = input("enter " + t + ": ")
    start = float(start)
    return start
  except ValueError:
    print("\n\r" + t + " must be a number")
    exit()
def encrypt (secret_key, msg):
  cipher = AES.new(secret_key, AES. MODE_ECB)
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

## ¿Qué redes admiten los reportes de costos?

Para ver una lista completa de las redes que admiten los reportes de costos en el enlace de atribución, haz clic <Anchor target="_blank" href="/marketers/es/docs/view-aggregated-cost-data-for-attribution-links#ad-networks-providing-cost-by-click-data">aquí</Anchor>.

Para ver una lista completa de las redes que admiten los reportes de costos, haz clic <Anchor target="_blank" href="/marketers/es/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">aquí</Anchor>.

<div data-zendesk-anchors="how-to-share-cost=c%C3%B3mo-compartir-los-costos h_01J292SNHC1B88FBJJW1PY5YT2=c%C3%B3mo-compartir-los-costos aes-encryption-process=proceso-de-cifrado-aes h_01J292SNHCFG8QP8KK058EVEVQ=proceso-de-cifrado-aes which-networks-support-cost-reporting=qu%C3%A9-redes-admiten-los-reportes-de-costos h_01J292SNHCVFR5GW4ECBYM63S6=qu%C3%A9-redes-admiten-los-reportes-de-costos" />
