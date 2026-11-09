---
title: Relatórios de custos no link de atribuição para ad networks
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
  edited_at: '2026-08-18T00:38:38Z'
  id: 115000748446
  locale: pt
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/pt/articles/115000748446
---
> **Resumo:** Ad networks podem relatar o custo toda vez que um anúncio recebe um clique.

Os anunciantes usam o dashboard da AppsFlyer como fonte confiável para todas as decisões de distribuição de orçamento, agilizando a tomada de decisões sobre onde investir. Para ad networks que desejam ser incluídas nesse processo, o compartilhamento de dados de custo com a AppsFlyer é fundamental.

Os anunciantes geralmente verificam seus parceiros com melhor performance usando a classificação por ROI. Aqueles que não mostram dados de custo sempre aparecem no final da lista.

<Image align="center" alt="" src="https://files.readme.io/ce5b7a7c4af1c016f4f8b2ad72c96c36456a73513e0ba19b8049e1e6fd286ef6-115002046163.png" />

<div id="how-to-share-cost" />

## Como compartilhar o custo

Há duas maneiras de enviar dados de custo a nível de usuário através de URLs de atribuição da AppsFlyer: de forma não criptografada e de forma criptografada. O envio de dados criptografados de custo permite que os parceiros enviem o valor de custo na URL de atribuição de cliques.

Dados de **custo não criptografados** podem ser enviados através dos seguintes 3 parâmetros para a URL de clique:

* af\_cost\_model=CPI (atualmente, o CPI é o único modelo que pode ser visualizado nos relatórios da AppsFlyer)
* af\_cost\_ value=`{insira o valor de CPI, por exemplo: 1,00}`  
  **Atenção:** Valores menores que 1 exigem um 0 antes do decimal, por exemplo: 0,05.
* af\_cost\_currency=`{insira o código de 3 letras da moeda. Se estiver em branco, assumiremos que o valor é USD}`

*ATENÇÃO*: Embora qualquer modelo de custo possa ser enviado por meio do link de atribuição, atualmente apenas o CPI é compatível para a exibição de dados de custo no dashboard. Outros modelos de custo estão disponíveis nos relatórios brutos.

Um exemplo de um link de atribuição com dados de custo não criptografados:

```http
https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD- A12345678910&af_siteid=12345&af_cost_model=CPI&af_cost_value=1.00&af_cost_currency=USD
```

**Custos criptografados**

Se você preferir não revelar o valor de custo real na URL de atribuição, você pode criptografar os parâmetros de custo. Dados de custo criptografados podem ser enviados seguindo um método de criptografia baseado em AES. Além do modelo de custo, valor e moeda, os parceiros precisarão de uma chave específica da ad network para gerar o valor de custo criptografado.

Passos para criptografia:

1. Solicite sua **chave de criptografia de ad network** à sua equipe de PSE usando o <Anchor target="_blank" href="https://support.appsflyer.com/hc/article_attachments/36300175200913">widget de assistente do parceiro</Anchor>.
2. Use o método de criptografia AES (mostrado abaixo) para criptografar os 4 valores necessários (**chave da ad network, valor de custo, modelo de custo e moeda de custo**)
3. Adicione o valor de criptografia gerado à sua URL de atribuição da AppsFlyer no parâmetro **af\_enc\_data=**.

Exemplo de links de atribuição com transferência de valores criptografados:

https://app.appsflyer.com/id554782625?pid=mediasource_int&c=campaignName&idfa=ABCDEFGH-ABCD-ABCD-ABCD-A12345678910&af_siteid=12345 **&af\_enc\_data=DvVvQRow%2F2N0LiQGZh0wvwucFygbll9IwAMSN%2B%2BDQxo%3D**

**Atenção:** Somente as ad networks que realizam a integração de custos criptografados com a AppsFlyer podem enviar dados de custos criptografados nos links de atribuição de seus clientes.

<div id="aes-encryption-process" />

## Processo de criptografia AES

Para realizar a criptografia, os parceiros devem usar o <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Advanced_Encryption_Standard">algoritmo **AES**</Anchor>, com um <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Electronic_Codebook_.28ECB.29">**ECB block mode**</Anchor>, usando <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Padding_(cryptography)#PKCS7">**PKCS5 padding**</Anchor>. Em seguida, eles devem usar <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Base64">**Base-64 encode**</Anchor> nos dados criptografados e, por fim, usar <Anchor target="_blank" href="https://en.wikipedia.org/wiki/Percent-encoding">**URL-encode**</Anchor> no resultado.

As ad networks podem usar qualquer tech stack para realizar esse processo. Veja exemplos abaixo para PHP, Java e Python:

PHP

```php
<?php
$f = fopen( 'php://stdin', 'r' );
echo "Introduza a chave privada: ";
$private_key = trim(fgets($f));
echo "Introduza o modelo de custo: ";
$cost_model = trim(fgets($f));
echo "Introduza o valor do custo: ";
$cost_value = trim(fgets($f));
echo "Introduza a moeda do custo: ";
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
echo "Chave privada: " . $private_key . "\r\n";
echo "String de consulta: " . $query_str . "\r\n";
echo "\n\r";
echo "String de consulta criptografada: " . $enc_url_encoded . "\r\n";
fclose( $f );
?>
```

Java

```java
private static final String CIPHER_ALGORITHM = "AES/ECB/PKCS5Padding";
private static final String encryptionKey = "XXXXXXXXXXXXXXXX"; // chave secreta fornecida pela AppsFlyer
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
  String resultado = urlencode(b64);
  return resultado;
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

## Quais ad networks oferecem suporte aos relatórios de custos?

Para ver uma lista completa das ad networks que oferecem suporte aos relatórios de custos no link de atribuição, clique <Anchor target="_blank" href="/marketers/pt/docs/view-aggregated-cost-data-for-attribution-links#ad-networks-providing-cost-by-click-data">aqui</Anchor>.

Para ver uma lista completa das ad networks que oferecem suporte aos relatórios de custos via API, clique <Anchor target="_blank" href="/marketers/pt/docs/roi360-cost-aggregation-overview#ad-networks-supporting-cost-api">aqui</Anchor>.

<div data-zendesk-anchors="how-to-share-cost=como-compartilhar-o-custo h_01J292SNHC1B88FBJJW1PY5YT2=como-compartilhar-o-custo aes-encryption-process=processo-de-criptografia-aes h_01J292SNHCFG8QP8KK058EVEVQ=processo-de-criptografia-aes which-networks-support-cost-reporting=quais-ad-networks-oferecem-suporte-aos-relat%C3%B3rios-de-custos h_01J292SNHCVFR5GW4ECBYM63S6=quais-ad-networks-oferecem-suporte-aos-relat%C3%B3rios-de-custos" />
