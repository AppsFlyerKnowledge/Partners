---
title: Cliquez sur Signature pour les réseaux publicitaires
metadata:
  keywords:
    - Ad Network
    - Advertisers
    - Protect360
    - Ad Networks
    - Partners
    - Marketers
    - Data Management
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-yael-sharabi
    - Marketers
    - Ad Networks
    - Data Management
  created_at: '2021-02-22T09:33:52Z'
  edited_at: '2024-08-07T10:24:58Z'
  id: 360017831497
  locale: fr
  section: Provide data
  section_id: 6551209900817
  url: https://support.appsflyer.com/hc/fr/articles/360017831497
---
> **En bref :** Ajoutez une validation de signature aux clics pour éviter les responsabilités liées à la fraude et pour que les clics frauduleux ne soient pas attribués à votre réseau publicitaire.

<div id="about-click-signing" />

## À propos de la signature par clic

Avec une technologie minimale, les fraudeurs peuvent envoyer des clics au nom d'un réseau publicitaire et créer des milliers, voire des millions, de faux clics qui sont envoyés à AppsFlyer. Parfois, les réseaux publicitaires eux-mêmes ne sont pas conscients du problème. 

Pour qu'un réseau publicitaire puisse s'assurer que les clics attribués par AppsFlyer proviennent authentiquement de leur propre réseau et non d'un fraudeur générant de faux clics, il est essentiel que les réseaux publicitaires signent leurs clics à l'aide de signatures<Anchor target="_blank" href="https://en.wikipedia.org/wiki/HMAC">HMAC-SHA256</Anchor>.

La signature des clics empêche également le réseau publicitaire d'être bloqué en raison d'un afflux massif de clics. Ce qui veut dire quesi un réseau publicitaire atteint le seuil de blocage des clics en raison d'un afflux massif de clics, AppsFlyer cesse d'enregistrer et d'attribuer leurs clics pour le reste de la journée.

Les signatures permettent à AppsFlyer de valider les clics et de garantir que les informations de clic n'ont pas été manipulées par des fraudeurs.

* Les clics validés sont enregistrés et attribués au réseau publicitaire
* Les clics invalidés sont rejetés et : 
  * Sont mis à disposition dans les rapports Protect360 pour les réseaux publicitaires (pas les annonceurs). <Anchor target="_blank" href="/partners/fr/docs/protect360-reports-for-ad-networks#failed-click-signatures">En savoir plus</Anchor>
  * N'impactent pas le taux de conversion ni le seuil de blocage des clics du réseau publicitaire.

<div id="click-signature-integration" />

## Cliquez sur l'intégration de la signature

<div id="flow" />

### Flux

Le tableau suivant décrit le flux depuis le développement initial et les tests de base jusqu'aux tests de production, et enfin, à la production. 

![Click_signing_integration_flow.png](https://files.readme.io/3bc0103090535c22db027fb09f72ad89d88210bba8f2b6f43d1166c2911d71cd-360017572558.png)

<div id="procedure" />

### Marche à suivre

**Conditions préalables :** <Anchor target="_blank" href="/marketers/fr/docs/managing-appsflyer-tokens">Jeton API V2.0</Anchor> de l'administrateur pour autoriser l'API de signature par clic.

**Pour signer vos clics**:

1. Générez une clé secrète avec l'API Générer une clé secrète.  
   Bonne pratique : générer et utiliser une nouvelle clé secrète toutes les 24 heures, avec une expiration de 36 heures.
2. Développez du code sur vos serveurs qui appelle l’API Générer une clé secrète, prend la clé secrète et génère une signature HMAC-SHA256. Voir l'exemple de code.  
   Vous pouvez utiliser les autres API comme décrit dans le tableau suivant.
3. Le code ajoute les éléments suivants à vos URL de clic :
   * Un paramètre **d'expiration** qui contient un horodatage Unix (en UTC) après lequel le réseau publicitaire ne réclame pas le clic.
   * La signature HMAC-SHA256.  
     Exemple :

     ```http
     https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_siteid=12345&expires=1597657118&signature_v2=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk
     ```

<div id="note" />

> 📘 **Remarque**
>
> Assurez-vous que tout codage d'URL de caractères spéciaux ou d'espaces dans votre lien se produit avant la génération de la signature de clic. La génération de la signature entraîne d’abord un échec de vérification.

<div id="creating-a-click-signature" />

## Créer une signature de clic

Pour créer une signature de clic, vous devez :

1. Créez un JSON en utilisant la liste des attributs et des règles JSON ci-dessous
2. Créez la signature à partir de ce JSON en utilisant HMAC56

<div id="list-of-attributes" />

### Liste des attributs

La liste d'attributs suivante est prise en charge pour la signature par clic et engagement.

| Commande | Paramètre | Obligatoire | Remarques |
| --- | --- | --- | --- |
| 1 | link\_domain | Oui | Le domaine de l'URL du clic, par exemple :<ul><li>app.appsflyer.com</li><li>myapp.onelink.me</li><li>click.mycustomdomain.com</li></ul> |
| 2 | link\_path | Oui | Le chemin de l'URL de clic n'inclut pas de barre oblique inverse au début.  <br />**app-id** pour les liens de plateforme uniques ou **template-id** pour OneLink |
| 3 | pid | Oui |  |
| 4 | af\_prt | Non |  |
| 5 | af\_siteid | Oui |  |
| 6 | clickid | Oui | Un identifiant à usage unique du clic |
| 7 | expires | Oui | Expiration du clic |
| 8 | af\_engagement\_type | Non |  |
| 9 | af\_click\_lookback | Non |  |
| 10 | af\_viewthrough\_lookback | Non |  |
| 11 | af\_reengagement\_window | Non |  |
| 12 | is\_retargeting | Non |  |
| 13 | af\_ip | Non |  |
| 14 | advertising\_id | Non |  |
| 15 | OAID | Non |  |
| 16 | fire\_advertising\_id | Non |  |
| 17 | idfa | Non |  |
| 18 | idfv | Non |  |

<div id="attribute-and-json-rules" />

### Attributs et règles JSON

<div id="order-and-appearance-of-attributes" />

#### Ordre et apparence des attributs

* Les paramètres pris en charge dans l'URL d'engagement avec une valeur doivent être au format JSON
* Les attributs doivent être répertoriés dans le JSON dans l'ordre indiqué dans le tableau ci-dessus

<div id="empty-attributes" />

#### Attributs vides

* Les attributs répertoriés dans le JSON ne peuvent pas être des valeurs vides ou contenir uniquement des espaces

<div id="json-data-structure" />

#### Structure de données JSON

* La structure de données JSON doit être un tableau d'attributs
  * Chaque attribut sera au format ["clé", "valeur"]  
    Exemple :   
    `[["key-1","value-1"],["key-2","value-2"]...["key-n","value-n"]]`

<div id="attribute-value-escaping" />

#### Échappement de la valeur d'attribut

* Les valeurs dans le JSON doivent être écrites dans **des chaînes minuscules** comme défini dans la <Anchor target="_blank" href="https://www.w3docs.com/snippets/java/how-should-i-escape-strings-in-json.html">norme JSON</Anchor>.

<div id="json-spaces" />

#### Espaces JSON

* Le JSON doit être compacté. Il ne doit contenir aucun espace, aucune tabulation ni aucun caractère de nouvelle ligne entre les valeurs.

<div id="signature-algorithm" />

#### Algorithme de signature

* Utilisez HmacSHA256 avec la clé secrète pour créer la signature du JSON
* Encoder la signature avec Base64 **sans** remplissage
* Ajoutez la signature à l'URL de clic avec un paramètre signature\_v2

```json
//generate a signature from the click url and encode it with base64 without padding String generatedSignature = Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(jsonString.getBytes()));
```

<div id="signature-example" />

### Exemple de signature

<div id="building-a-signature-example" />

<Accordion title="Créer un exemple de signature">

Exemple d'URL de clic OneLink (multiplateforme) :

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&clickid=sdkfjasksjskdfj9845weh&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615
```

Exemple d'objet json pour la signature (avant de supprimer les espaces vides) :

```json
[
	["link_domain","yourbrand.onelink.me"],
	["link_path","qswl"],
	["pid","mediasource_int"],
	["af_siteid","my_site"],
	["clickid","12345"],
	["expires","1689695615"]
]
```

Exemple d'objet json pour la signature (après avoir supprimé les espaces vides)

```json
[["link_domain","yourbrand.onelink.me"],["link_path","qswl"],["pid","mediasource_int"],["template-id","qswl"],["af_siteid","my_site"],["clickid","12345"],["expires","1689695615"]]
```

URL du clic final avec la signature :

```http
https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012  
&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign  
&expires=1689695615  
&signature_v2=WIfCmfLAPSsVrBTqCqfihMeLCnbE4dIAlhHF84WsiWA
```

</Accordion>

<div id="code-examples" />

### Exemples de code

<div id="signingsupportedparamsjson" />

<Accordion title="signing-supported-params.json">

```json
[
  {"index":1, "name":"pid", "mandatory":true},
  {"index":2, "name":"af_prt", "mandatory":false},
  {"index":3, "name":"af_siteid", "mandatory":true},
  {"index":4, "name":"clickid", "mandatory":true},
  {"index":5, "name":"expires", "mandatory":true},
  {"index":6, "name":"af_engagement_type", "mandatory":false},
  {"index":7, "name":"af_click_lookback", "mandatory":false},
  {"index":8, "name":"af_viewthrough_lookback", "mandatory":false},
  {"index":9, "name":"af_reengagement_window", "mandatory":false},
  {"index":10, "name":"is_retargeting", "mandatory":false},
  {"index":11, "name":"af_ip", "mandatory":false},
  {"index":12, "name":"advertising_id", "mandatory":false},
  {"index":13, "name":"oaid", "mandatory":false},
  {"index":14, "name":"fire_advertising_id", "mandatory":false},
  {"index":15, "name":"idfa", "mandatory":false},
  {"index":16, "name":"idfv", "mandatory":false}
]
```

</Accordion>

<div id="signatureexamplego" />

<Accordion title="signature-example.go">

```json
package main

import (
	"crypto/hmac"
	"crypto/sha256"
	"encoding/base64"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/url"
	"os"
	"strings"
	"time"
)

type Param struct {
	Name      string
	Mandatory bool
}

func LoadSupportedParams() ([]Param, error) {
	path := "./signing-supported-params.json"
	jsonFile, _ := os.Open(path)
	defer jsonFile.Close()
	byteValue, err := io.ReadAll(jsonFile)
	if err != nil {
		return nil, errors.New("failed loading " + path)
	}
	var params []Param
	_ = json.Unmarshal(byteValue, &params)
	return params, nil
}

func computeHmac256(message, secret string) (res string, errResult error) {
	defer func() {
		if r := recover(); r != nil {
			errResult = r.(error)
			fmt.Println("failed to invoke ComputeHmac256. err: %+v", errResult)
			res = ""
			return
		}
	}()

	key := []byte(secret)
	h := hmac.New(sha256.New, key)
	h.Write([]byte(message))
	return base64.URLEncoding.WithPadding(base64.NoPadding).EncodeToString(h.Sum(nil)), nil
}

// this function accepts a click url, a ttl for the click in seconds, and the list of supported params
// the function:
// 1. adds the expiration to the click based on the provided ttl
// 2. builds a json for the signature
// 3. create an HMAC256 signature
// 4. adds the signature to the click url
func signURLV2(originalURL string, secret string, clickTtlSeconds int64, supportedParams []Param) (signedURL string, err error) {

	//add an expiration to the click
	expires := time.Now().UTC().Unix() + clickTtlSeconds
	urlWithExpired := fmt.Sprintf("%s%s%d", originalURL, "&expires=", expires)

	//parse the url
	parsedURL, err := url.Parse(urlWithExpired)
	if err != nil {
		return "", errors.New("failed parsing URL")
	}

	//build a json from the url
	jsonStr, err := buildJSONFromURLV2(parsedURL, supportedParams)
	if err != nil {
		return "", err
	}

	//create a signature
	signatureV2, err := computeHmac256(jsonStr, secret)
	if err != nil {
		fmt.Println("Failed to computeHMAC256 for url %s. err: %+v", jsonStr, err)
		return "", errors.New("fail to computeHMAC256 for url")
	}

	//add the signature to the url
	signedURL = fmt.Sprintf("%s%s%s", urlWithExpired, "&signature_v2=", signatureV2)

	return signedURL, nil

}

// this function builds a json from a given click url.
// It returns a string representation of the json ready to be signed.
func buildJSONFromURLV2(parsedURL *url.URL, supportedParams []Param) (string, error) {
	//initiate an empty json in the structure [[key-1,val-1],[key-2,val-2]...[key-n,val-n]]
	var jsonData [][2]string

	//add the url host domain to the json
	domain := parsedURL.Host
	param := [2]string{"link_domain", domain}
	jsonData = append(jsonData, param)

	//add the path (app-id or template-id) to the json
	path := parsedURL.Path
	if len(path) > 1 {
		param := [2]string{"link_path", path[1:]}
		jsonData = append(jsonData, param)
	}

	//loop over the ordered list of supported parameters and add them to the json
	for i := 0; i <len(supportedParams); i++ {name := supportedParams[i].Name val := parsedURL.Query().Get(name) if len(val) > 0 {
			param := [2]string{name, val}
			jsonData = append(jsonData, param)
		} else if supportedParams[i].Mandatory {
			return "", errors.New("missing mandatory param: " + name)
		}
	}

	//generate string representation of the json object
	jsonObj, _ := json.Marshal(jsonData)
	return strings.ToLower(string(jsonObj)), nil
}

func main() {

	supportedParams, err := LoadSupportedParams()
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	}

	var secretKey = "tqJU4Qd/eFTEWfqW7KCG9asDO0bmZoFzv8GY3VPSPAM="
	var clickTtlSeconds int64 = 60
	var originalUrl = "https://yourbrand.onelink.me/qsWL?pid=mediasource_int&advertising_id=12345678-1234-1234-1234-123456789012&clickid=1234&af_ad_type=video&af_adset=MMP&af_siteid=my_site&af_viewthrough_lookback=2h&c=my_campaign"

	fmt.Println("Original URL: ", originalUrl)

	signedUrl, err := signURLV2(originalUrl, secretKey, clickTtlSeconds, supportedParams)
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(1)
	} else {
		fmt.Println("Signed URL: ", signedUrl)
	}
}
```

</Accordion>

<div id="click-signature-apis" />

## API de signature de clics

AppsFlyer fournit des API qui permettent aux réseaux publicitaires de gérer et de tester le processus de signature des clics. Consultez la liste des API dans le tableau ci-dessous, ainsi que les sections qui suivent avec les informations nécessaires à l'utilisation de l'API.

<div id="click-signature-apis-1" />

#### API de signature de clics

| Méthode API | Remarques |
| --- | --- |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-post">Générer une clé secrète</Anchor> | Générer des clés secrètes à utiliser dans la signature. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-secret-delete">Révoquer la clé secrète</Anchor> | Annuler les clés secrètes compromises. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-test-post">Test</Anchor> | Envoyez des clics simples pour tester la signature. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-update-put">Mode de configuration</Anchor> | Configurer le mode de signature par clic :<ul><li>**désactivé** (par défaut) : Aucune validation de signature de clic n'est effectuée.</li><li>**rapport uniquement** (mode test) : AppsFlyer valide les signatures de clics, mais ne bloque pas les clics avec des signatures non valides. Le réseau publicitaire peut utiliser le **RAPI de rapport électronique** pour obtenir des statistiques sur les clics réussis/échoués. Utilisez ceci pour tester la signature des clics sans impacter la production et le trafic réel.</li><li>Activé AppsFlyer bloque les clics avec des signatures non valides ou manquantes.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-circuit-breaker-put">Configurer le disjoncteur</Anchor> | Configurez le mode du disjoncteur qui protège le réseau publicitaire contre un trop grand nombre de clics bloqués :<ul><li>**activé** (par défaut) : si le système Protect360 détecte que trop de clics sont marqués comme non valides, protégez le réseau publicitaire contre des clics potentiellement bloqués par erreur :<ul><li>Configurez les modifications de l'API en mode rapport uniquement.</li><li>Une alerte par e-mail est envoyée au réseau publicitaire pour vérifier que l'API de signature de clic est correctement configurée.</li></ul></li><li>**désactivé** : Protect360 continue de bloquer tous les clics marqués comme non valides, même lorsque le pourcentage de blocage est inhabituellement élevé.</li></ul> |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-get">Obtenir la configuration</Anchor> | Obtenez le mode et les identifiants des clés secrètes actives. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-report-get">Rapport</Anchor> | Obtenez des statistiques sur les clics réussis et échoués lorsque le système est en mode **rapport uniquement** ou **activé** . Utilisez ceci pour tester la signature des clics sans impacter la production et le trafic réel. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-add">Exclure l'app</Anchor> | Configurez les ID d’app à exclure de la signature par clic. |
| <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/click-signing-config-excluded-apps-delete">Supprimer l'application exclue</Anchor> | Configurez les ID d’app à inclure dans la signature par clic après avoir été exclus. |

<div id="legacy-versions" />

## Versions héritées

Ces versions ne doivent pas être utilisées et sont répertoriées à titre de référence uniquement

<div id="v1-legacy" />

<Accordion title="V1 - Héritée">

<div id="generate-secret-key-method" />

### Méthode de génération de clé secrète

<div id="generate-secret-key-basics" />

<Accordion title="Les bases de la génération de clés secrètes">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>POST</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/secret?ttlHours=&lt;ttlHours&gt;</span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td>La clé secrète est renvoyée dans un JSON</td></tr><tr><td> </td><td>Limite de demande</td><td>Maximum de 2 clés secrètes actives à la fois</td></tr></tbody></table>

</Accordion>

<div id="api-request" />

<Accordion title="Demande d'API">

**Méthode**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=<ttlHours>
```

<div id="parameters" />

#### Paramètres

| Paramètre | Description |
| --- | --- |
| ttlHours | <ul><li>Temps de vie pour la clé secrète, en heures, de 1 à 1440 heures.</li><li>La valeur par défaut est de 36 heures</li></ul> |

</Accordion>

<div id="json-response" />

<Accordion title="Réponse JSON">

| **Clé** | **Description** |
| --- | --- |
| secret-key-id | Un ID pour la clé secrète |
| Clé secrète | La clé secrète de la signature du clic |
| expiration | Expiration en millisecondes |

</Accordion>

<div id="generate-secret-key-curl-example-and-response" />

<Accordion title="Générer un exemple et une réponse de clé secrète curl">

**Requête Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/secret?ttlHours=36' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Réponse JSON**

```json
{
	"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
	"secret-key": "zGW6Rhrmb8+vuhHtL/Kp6rW5Ci9PNsjH1J5MGO9SIeg=",
	"expiration": 1610533263
}
```

</Accordion>

<div id="http-response-codes" />

<Accordion title="Codes de réponse HTTP">

<div id="response-codes" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="revoke-secret-key-method" />

### Méthode de révocation de la clé secrète

<div id="revoke-secrete-key-basics" />

<Accordion title="Révoquer les bases de la clé secrète">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>DELETE</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer.<span>com/api/p360-</span>click-signing/secret/&lt;secret-id&gt;</span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td>Vide</td></tr></tbody></table>

</Accordion>

<Accordion title="Demande d'API">

**Méthode**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/secret/<secret-id>
```

<div id="parameters-1" />

#### Paramètres

| Paramètre | Description |
| --- | --- |
| secret-id | L'ID de la clé secrète à révoquer |

</Accordion>

<div id="generate-secret-key-curl-example-and-response::5a4174fc" />

<Accordion title="Générer un exemple et une réponse de clé secrète curl">

**Requête Curl**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/secret/59ad6547-affc-45eb-a6c9-9805f88ee755' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::7dc4ee64" />

<Accordion title="Codes de réponse HTTP">

<div id="response-codes-1" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="test-method" />

### Méthode d'essai

<div id="test-basics" />

<Accordion title="Notions de base sur les tests">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>POST</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/test</span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td>Renvoie dans un JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="Demande d'API">

**Méthode**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/test
```

<div id="parameters-2" />

#### Paramètres

| Paramètre | Description |
| --- | --- |
| url | L'URL de clic (y compris la signature) pour test |

</Accordion>

<div id="json-response::cd966b82" />

<Accordion title="Réponse JSON">

| **Clé** | **Description** |
| --- | --- |
| test-status | Soit réussi, soit échoué |
| message | Raison de l'échec du test Exemple :<ul><li>Signature manquante</li><li>Signature invalide</li><li>Expiré</li></ul> |

</Accordion>

<div id="test-curl-example-and-response" />

<Accordion title="Exemple de test curl et réponse">

**Requête Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/test' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
--header 'Content-Type: application/json' \
--data-raw '{
   "url": "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345&expires=1597657118&signature=8fnDVzZP_WRZnv3KNJaREOEfvB5p9oRc_XlKEvUo8gk"
}'
```

**Réponse JSON**

```json
{
	"test-status":"Passed / Failed",
	"message": "Invalid signature"
}
```

</Accordion>

<div id="http-response-codes::22d1011c" />

<Accordion title="Codes de réponse HTTP">

<div id="response-codes-2" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="configure-mode-method" />

### Méthode du mode de configuration

<div id="configure-mode-basics" />

<Accordion title="Notions de base sur le mode de configuration">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>POST</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>mode/&lt;mode&gt;</span></strong></span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td>Renvoie dans un JSON</td></tr></tbody></table>

</Accordion>

<div id="api-request::b2432cce" />

<Accordion title="Demande d'API">

**Méthode**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/mode/<mode>
```

<div id="parameters-3" />

#### Paramètres

| Paramètre | Description |
| --- | --- |
| mode | Options :<ul><li>activé<br />**Attention !** Activez le mode uniquement après avoir exécuté le mode rapport uniquement pendant quelques heures et vérifié vos rapports pour vous assurer que la configuration est correcte et que tous les clics ont passé la validation de signature.</li><li>désactivé</li><li>rapport uniquement</li></ul> |

</Accordion>

<div id="configure-mode-curl-example" />

<Accordion title="Exemple de configuration du mode curl">

**Requête Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/mode/report-only' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<Accordion title="Codes de réponse HTTP">

<div id="response-codes-3" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Demande incorrecte | Mode invalide |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="configure-circuit-breaker-method" />

### Configurer la méthode du disjoncteur

<div id="configure-circuit-breaker-basics" />

<Accordion title="Configurer les bases du disjoncteur">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>POST</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker</span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td><span>Statut HTTP</span></td></tr></tbody></table>

</Accordion>

<div id="api-request::1ede8b9c" />

<div id="api-request::ef73eae0" />

<Accordion title="Demande d'API">

**Méthode**

```http
POST https://hq1.appsflyer.com/p360-click-signing/config/circuit-breaker
```

<div id="request-body-json" />

#### Corps de la requête JSON

| Paramètre | Description |
| --- | --- |
| Statut | <ul><li>activé</li><li>désactivé</li></ul> |

</Accordion>

<div id="configure-circuit-breaker-curl-example-and-response" />

<Accordion title="Exemple de configuration et de réponse du disjoncteur curl">

**Requête Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/circuit-breaker' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
--data-raw '{
"status":"enabled"
}'
```

</Accordion>

<div id="http-response-codes::b3328f8b" />

<div id="http-response-codes::d35e3a62" />

<Accordion title="Codes de réponse HTTP">

<div id="response-codes-4" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 400 | Demande incorrecte | Statut invalide |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="get-configuration-method" />

### Obtenir la méthode de configuration

<div id="get-configuration-basics" />

<Accordion title="Obtenir les bases de la configuration">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>GET</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config</span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td>Renvoie dans un JSON</td></tr></tbody></table>

</Accordion>

<Accordion title="Demande d'API">

**Méthode**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/config
```

</Accordion>

<div id="json-response::fee92c" />

<Accordion title="Réponse JSON">

| **Clé** | **Description** |
| --- | --- |
| mode | Parmi :<ul><li>activé</li><li>désactivé</li><li>rapport uniquement</li></ul> |
| circuit-breaker-config | Un objet JSON contenant **le statut**, l'un des suivants :<ul><li>activé</li><li>désactivé</li></ul> |
| active-key-ids | Un tableau JSON contenant des clés actives :<ul><li>**secret-key-id**: ID généré aléatoirement de la clé secrète</li><li>**expiration**: expiration en millisecondes de la clé secrète</li></ul> |
| excluded-app-ids | Un tableau JSON avec des ID d’app exclus |

</Accordion>

<div id="get-configuration-curl-example-and-response" />

<Accordion title="Obtenir l'exemple de configuration curl et la réponse">

**Requête Curl**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/config' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

**Réponse JSON**

```json
{
	"mode": "report-only",
	"active-key-ids": [
		{
			"secret-key-id": "59ad6547-affc-45eb-a6c9-9805f88ee755",
			"expiration": 1610533263
		}
	],
	"excluded-app-ids": [
		"app-id-1", 	"app-id-2"
	]

}
```

</Accordion>

<Accordion title="Codes de réponse HTTP">

<div id="response-codes-5" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="report-method" />

### Méthode de rapport

<div id="report-basics" />

<Accordion title="Notions de base sur les rapports">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>GET</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/report</span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td>Renvoyé dans un fichier CSV</td></tr></tbody></table>

</Accordion>

<div id="api-request::a2a93b39" />

<div id="api-request::b28cedb0" />

<Accordion title="Demande d'API">

**Méthode**

```http
GET https://hq1.appsflyer.com/api/p360-click-signing/report
```

<div id="parameters-4" />

#### Paramètres

<table><tbody><tr><th><p>Paramètre</p></th><th>Description</th></tr><tr><td>start-date</td><td><p>Date et heure de début du rapport. Format : aaaa-mm-jjThh</p></td></tr><tr><td>end-date</td><td><p><span>Date et heure de fin du rapport. Format : aaaa-mm-jjThh</span></p></td></tr><tr><td colspan="2"><span>L'API requiert <strong>soit</strong> une date de début et une date de fin, soit <strong>aucune</strong> des deux. Si la date de début/fin n'est pas fournie, le rapport affiche les résultats des dernières 24 heures.</span></td></tr></tbody></table>

</Accordion>

<div id="csv-response" />

<Accordion title="Réponse CSV">

| **Colonne** | **Description** |
| --- | --- |
| time | Date et heure des clics. Format aaaa-mm-jjThh |
| total\_clicks | Nombre total de clics au cours de la période de référence |
| valid\_clicks | Nombre de clics valides au cours de la période de rapport |
| missing\_signature | Nombre de clics sans signatures au cours de la période de référence |
| expired\_clicks | Nombre de clics expirés au cours de la période de rapport |
| invalid\_signature | Nombre de clics avec une signature non valide au cours de la période de rapport |
| no\_active\_secrets | Nombre de clics rejetés car il n'y a pas de clés secrètes actives dans le système (généralement lorsque le système est en mode rapport uniquement) |

</Accordion>

<div id="test-curl-example-and-response::66e922" />

<Accordion title="Exemple de test curl et réponse">

**Requête Curl**

```bash
curl --location --request GET 'https://hq1.appsflyer.com/api/p360-click-signing/report?start-date=2021-01-07T07&end-date=2021-01-17T12' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}' \
```

**Réponse CSV**

| **time** | **total\_clicks** | **valid\_clicks** | **missing\_signature** | **expired\_clicks** | **invalid\_signature** | **no\_active\_signatures** |
| --- | --- | --- | --- | --- | --- | --- |
| 2021-01-17T07 | 928082156 | 928082156 | 0 | 0 | 0 | 0 |
| 2021-01-17T08 | 923796132 | 923796132 | 0 | 0 | 0 | 0 |
| 2021-01-17T09 | 917541373 | 917541373 | 0 | 0 | 0 | 0 |
| 2021-01-17T10 | 909977064 | 909977064 | 0 | 0 | 0 | 0 |
| 2021-01-17T11 | 965104299 | 965104299 | 0 | 0 | 0 | 0 |
| 2021-01-17T12 | 975134824 | 975134824 | 0 | 0 | 0 | 0 |

</Accordion>

<Accordion title="Codes de réponse HTTP">

<div id="response-codes-6" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="exclude-app-method" />

### Méthode d'exclusion de l'application

<div id="exclude-app-method-basics" />

<Accordion title="Principes de base de la méthode d'exclusion de l'application">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>POST</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>excluded-app/&lt;app-id&gt;</span></strong></span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td>Vide</td></tr></tbody></table>

</Accordion>

<div id="api-request::1054abca" />

<Accordion title="Demande d'API">

**Méthode**

```http
POST https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-5" />

#### Paramètres

| Paramètre | Description |
| --- | --- |
| app-id | ID d'application à exclure de la validation de signature par clic |

</Accordion>

<div id="exclude-app-curl-example" />

<Accordion title="Exemple d'exclusion d'application curl">

**Requête Curl**

```bash
curl --location --request POST 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::90a409c" />

<Accordion title="Codes de réponse HTTP">

<div id="response-codes-7" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="remove-excluded-app-method" />

### Supprimer la méthode d’exclusion d’app

<div id="remove-excluded-app-method-basics" />

<Accordion title="Supprimer les bases de la méthode d’exclusion d’app">

<table><thead><tr><th>Catégorie</th><th>Élément</th><th><p><span>Description</span></p></th></tr></thead><tbody><tr><td rowspan="3">Requête</td><td>Méthode HTTP</td><td><code>DELETE</code></td></tr><tr><td>Chemin</td><td><p><span>https://hq1.appsflyer<span>.com/api/p360-</span>click-signing/config/<strong><span>excluded-app/&lt;app-id&gt;</span></strong></span></p></td></tr><tr><td>En-tête d'autorisation </td><td><ul><li>L'en-tête d'autorisation obligatoire contient un jeton Bearer. </li><li>L'administrateur obtient le jeton dans le tableau de bord comme suit :  <a href="/marketers/fr/docs/managing-appsflyer-tokens" target="_blank">L'administrateur accède à la liste déroulante des e-mails &gt; jetons API pour obtenir le jeton V2.0</a>  </li></ul></td></tr><tr><td>Réponse</td><td>Résultats</td><td>Vide</td></tr></tbody></table>

</Accordion>

<div id="api-request::3f5b6d35" />

<div id="api-request::9504d16f" />

<Accordion title="Demande d'API">

**Méthode**

```http
DELETE https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/<app-id>
```

<div id="parameters-6" />

#### Paramètres

| Paramètre | Description |
| --- | --- |
| app-id | ID d'app à supprimer de la liste des applications exclues de la validation de signature par clic |

</Accordion>

<div id="remove-excluded-app-curl-example" />

<Accordion title="Supprimer l'exemple d'application curl exclue">

**Requête Curl**

```bash
curl --location --request DELETE 'https://hq1.appsflyer.com/api/p360-click-signing/config/excluded-app/appname.com' \
-H 'Authorization: Bearer {API V2.0 token available to the admin in the dashboard.}'
```

</Accordion>

<div id="http-response-codes::8454f45d" />

<div id="http-response-codes::7991b66" />

<div id="http-response-codes::b5e059da" />

<Accordion title="Codes de réponse HTTP">

<div id="response-codes-8" />

#### Codes de réponse

| Code | Message | Remarques |
| --- | --- | --- |
| 200 | OK |  |
| 401 | Non autorisé(e) | En-tête d'autorisation non valide ou manquant |

</Accordion>

<div id="code-sample" />

<Accordion title="Exemple de code">

```java
package sign;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import java.util.Base64;

.
.
.

String clickUrl = "https://app.appsflyer.com/com.app.id?pid=adnetwork_int&c=my_campaign&clickid=sdkfjasksjskdfj9845weh&af_site_id=12345";
String secretKey = "secret_key"; 
int ttlMinutes = 5;

//add expiration to the click URL
long expiration = System.currentTimeMillis() + (60000L * ttlMinutes);
clickUrl += "&expires="+expiration;

//create a SecretKey object from the given key string
SecretKeySpec signingKey = new SecretKeySpec(secretKey.getBytes(), "HmacSHA256");
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(signingKey);

//generate a signature from the click url and encode it with base64 without padding
String generatedSignature =     
Base64.getUrlEncoder().withoutPadding().encodeToString(mac.doFinal(clickUrl.getBytes()));

//add the signature to the click URL
String signedClickUrl = clickUrl + "&signature=" + generatedSignature;
```

</Accordion>

</Accordion>

<div id="additional-information" />

## Informations supplémentaires

<div id="troubleshooting" />

<Accordion title="Dépannage">

AppsFlyer revient au mode rapport uniquement et cesse la validation des signatures des clics lorsqueplus de 90 % des clics échouent à la validation de signature en une heure.

Cela permet de protéger votre entreprise d'un éventuel problème technique et de trouver la cause de l'anomalie :

* Si vous constatez que la signature fonctionne comme prévu et que les clics sont correctement bloqués, désactivez le disjoncteur à l'aide de la [méthode de configuration du disjoncteur.](/docs/click-signing-for-ad-networks#configurer-la-méthode-du-disjoncteur)
* Si vous constatez que des clics sont bloqués par erreur :
  1. Assurez-vous que vous disposez d'une clé secrète valide en vérifiant la configuration de signature par clic à l'aide de la[méthode d'obtention de la configuration.](/docs/click-signing-for-ad-networks#obtenir-la-méthode-de-configuration)
  2. Utilisez le [rapport de signature de clic](/docs/click-signing-for-ad-networks#méthode-de-rapport) pour obtenir plus d'informations sur les clics bloqués et enquêter sur les sources (identifiants d'agence/d'application) et les raisons des clics non valides.
* Si vous rencontrez un problème avec une application spécifique en raison d'une intégration non standard, excluez cette application de la validation de signature par clic à l'aide de l'[API d'exclusion d'application.](/docs/click-signing-for-ad-networks#méthode-dexclusion-de-lapplication)
* Si vous rencontrez un problème avec votre configuration :
  1. Continuez à utiliser le mode rapport uniquement.
  2. Corrigez le processus de signature par clic de votre côté.
  3. Vérifiez les résultats dans le [rapport de signature des clics](/docs/click-signing-for-ad-networks#méthode-de-rapport) et réactivez la validation de la signature des clics lorsque vous constatez que les clics sont validés comme prévu.

</Accordion>

<div id="faq" />

<Accordion title="FAQ">

| **Q : Comment tester la signature par clic sans impacter la production ?**<br /><br />**R** : Il existe deux manières de tester la signature par clic :<ol><li>Utiliser l'[API de test](/docs/click-signing-for-ad-networks#méthode-dessai). Cette méthode est utile pendant la phase de développement, pour tester les signatures de clics simples.</li><li>Utiliser le mode rapport uniquement. Le mode Rapport uniquement vérifie les signatures sur les clics de production et vous montre ce qui serait bloqué, mais ne bloque pas les clics non valides. Vous pouvez donc tester que la signature par clic fonctionne sans impacter le trafic réel.</li></ol> |
| --- |
| **Q : Quelle est la différence entre un jeton API et une clé secrète ?**<br /><br />**R** : **Jeton d’API** : utilisé pour autoriser et exécuter l'API de signature par clic. Il n'y en a qu'un par réseau publicitaire. Le <Anchor target="_blank" href="/marketers/fr/docs/managing-appsflyer-tokens">jeton AppsFlyer API V2.0</Anchor> doit être obtenu auprès de l'administrateur<br /><br />Clé secrète : utilisée pour générer la signature. Utilisez le [méthode de génération de clé secrète](/docs/click-signing-for-ad-networks#méthode-de-génération-de-clé-secrète) pour créer des clés secrètes. Le réseau publicitaire est responsable de la génération de nouvelles clés secrètes. Voir le [section des caractéristiques](/docs/click-signing-for-ad-networks#traits) pour plus d'informations. |
| **Q : Pouvons-nous appliquer la signature par clic uniquement à certaines campagnes ?**<br /><br />**R** : Non. La signature de clic s'applique à tous les clics provenant d'un réseau publicitaire. Vous pouvez exclure certaines applications de la signature par clic, mais vous ne pouvez pas exclure uniquement certaines campagnes. |

</Accordion>

<div id="traits" />

<Accordion title="Caractéristiques">

| Caractéristique | Description |
| --- | --- |
| Cliquez sur la signature | La signature doit apparaître sur les serveurs du réseau publicitaire. |
| Clé secrète | <ul><li>Les réseaux publicitaires peuvent avoir un maximum de deux clés secrètes actives simultanément.</li><li>Chaque clé secrète a une date d'expiration.</li><li>Les clics signés avec des clés secrètes expirées sont rejetés.</li></ul> |
| API de rapport | Les statistiques mises à jour sur la validité des clics sont agrégées toutes les heures. |

</Accordion>

<div data-zendesk-anchors="about-click-signing=%C3%A0-propos-de-la-signature-par-clic h_01HNWC70BPGDJAG3X8M5Z2RHQ4=%C3%A0-propos-de-la-signature-par-clic click-signature-integration=cliquez-sur-lint%C3%A9gration-de-la-signature h_01HNWC70BPFYMZ56GTPV3W6DXA=cliquez-sur-lint%C3%A9gration-de-la-signature flow=flux h_01HNWC70BPMXTKF9NZBYGCB874=flux procedure=marche-%C3%A0-suivre h_01HNWC70BPHCAGD1ECA56CC1Q6=marche-%C3%A0-suivre h_01HNWC70BPAR4QNTNSFE1JZM2J=remarque list-of-attributes=cr%C3%A9er-une-signature-de-clic h_01HP4A42YYFFF6M4VEH84KRTTK=cr%C3%A9er-une-signature-de-clic h_01HNWD3XYWFRY262HZZVAVWACR=liste-des-attributs attribute-rules=attributs-et-r%C3%A8gles-json h_01HNWE3A19RM7757B707TWZ6G0=attributs-et-r%C3%A8gles-json order-and-appearance-of-attributes=ordre-et-apparence-des-attributs h_01HNWE3A1920YQGZX2VG4X3M4B=ordre-et-apparence-des-attributs empty-attributes=attributs-vides h_01HNYRZ1DPDDQ5H8RFYKAQWVKP=attributs-vides json-data-structure=structure-de-donn%C3%A9es-json h_01HNYS6R7F0MNPBN08TXKQS5DV=structure-de-donn%C3%A9es-json attribute-value-escaping=%C3%A9chappement-de-la-valeur-dattribut h_01HNYSEBGD1DBSV2MHS7DZ75HS=%C3%A9chappement-de-la-valeur-dattribut json-spaces=espaces-json h_01HNYSY42HS1RXFG7T7QS9B0TK=espaces-json signature-algorithm=algorithme-de-signature h_01HNYSJDFWAM9RREYH4M8DZQJA=algorithme-de-signature signature-example=exemple-de-signature h_01HP3YAN03BWVA30JP1JAFZYAG=exemple-de-signature h_01HP3Y2Z65BN0SZ56XSHD52MSY=building-a-signature-example code-example=exemples-de-code h_01HNYT8Z33M69JAS72MQ03YX0M=exemples-de-code h_01HP3XVEJTBBVKZYEBZT62PR20=signingsupportedparamsjson h_01HP3XVEJTWWJVDBK5PGQH7DJY=signatureexamplego click-signature-apis=api-de-signature-de-clics h_01HNWC70BPNEVT00S040TQ9KVD=api-de-signature-de-clics click-signature-apis::58bf03c7=api-de-signature-de-clics-1 h_01HNWC70BPR8XXC3TQCAZSGFZS=api-de-signature-de-clics-1 legacy-versions=versions-h%C3%A9rit%C3%A9es h_01HNZ3YMFRWFDY751EBA58V6Q0=versions-h%C3%A9rit%C3%A9es h_01HNWCYB2YXCVGCP38GRBAJYQ4=v1-legacy generate-secret-key-method=m%C3%A9thode-de-g%C3%A9n%C3%A9ration-de-cl%C3%A9-secr%C3%A8te h_01HNWC70BPBPSX1WKJJC2W6H69=m%C3%A9thode-de-g%C3%A9n%C3%A9ration-de-cl%C3%A9-secr%C3%A8te h_01HNWC70BPPBK2S38KA6RQSTCN=generate-secret-key-basics h_01HNWC70BP40D5XN8DZQHSDZ5K=api-request parameters=param%C3%A8tres h_01HNWC70BPS83JD78JWQYK1NX9=param%C3%A8tres h_01HNWC70BPQC37602GV8GQPSEQ=json-response h_01HNWC70BP7V8KRW4861PXC2PX=generate-secret-key-curl-example-and-response h_01HNWC70BPKTPZEKFD37B6YQMH=http-response-codes response-codes=codes-de-r%C3%A9ponse h_01HNWC70BPMQ8Q94JD5CBT5RHZ=codes-de-r%C3%A9ponse revoke-secret-key-method=m%C3%A9thode-de-r%C3%A9vocation-de-la-cl%C3%A9-secr%C3%A8te h_01HNWC70BP8V05Q04J6EVGAS9T=m%C3%A9thode-de-r%C3%A9vocation-de-la-cl%C3%A9-secr%C3%A8te h_01HNWC70BP69ZJERY1Z03A5V4C=revoke-secrete-key-basics h_01HNWC70BPN01BNKKC7T9QMF44=api-request::3f5b6d35 parameters::f8e4d5cf=param%C3%A8tres-1 h_01HNWC70BPQ5S06E210RTE7E6R=param%C3%A8tres-1 h_01HNWC70BPBQA0ME8D6TZEM2EB=generate-secret-key-curl-example-and-response::5a4174fc h_01HNWC70BP9AV6PPEZNPQWJN85=http-response-codes::7dc4ee64 response-codes::d802debd=codes-de-r%C3%A9ponse-1 h_01HNWC70BPN18MB98KWND886QN=codes-de-r%C3%A9ponse-1 test-method=m%C3%A9thode-dessai h_01HNWC70BPKEVRDMT8N4HMC98W=m%C3%A9thode-dessai h_01HNWC70BPX4TH2MNE4GJBGHRG=test-basics h_01HNWC70BP5X2MZ3AC8BF69XYK=api-request::b2432cce parameters::7d3f0c33=param%C3%A8tres-2 h_01HNWC70BPKQFVEGWR9QT566YX=param%C3%A8tres-2 h_01HNWC70BPM50T2JEGJF41GGX4=json-response::cd966b82 h_01HNWC70BPSQYQ5R7PJE4CAKYG=test-curl-example-and-response h_01HNWC70BP8SSK2E5DFAD2Q6NP=http-response-codes::22d1011c response-codes::a79c47f4=codes-de-r%C3%A9ponse-2 h_01HNWC70BPC43F5H85F56DDSQR=codes-de-r%C3%A9ponse-2 configure-mode-method=m%C3%A9thode-du-mode-de-configuration h_01HNWC70BP6NPF7NSF0MGA4BJ3=m%C3%A9thode-du-mode-de-configuration h_01HNWC70BPKNAVCD57D2E7FX8F=configure-mode-basics h_01HNWC70BQFCJCHHVQHKWB57GF=api-request::1ede8b9c parameters::2fff2a1b=param%C3%A8tres-3 h_01HNWC70BQSQ7YWZVQB9A4DZQW=param%C3%A8tres-3 h_01HNWC70BQF0J2TZF181BW0MKT=configure-mode-curl-example h_01HNWC70BQ9HNQV7HA45ZXA2Z3=http-response-codes::b3328f8b response-codes::fe5a5b10=codes-de-r%C3%A9ponse-3 h_01HNWC70BQZ657X25N8JGM57A1=codes-de-r%C3%A9ponse-3 configure-circuit-breaker-method=configurer-la-m%C3%A9thode-du-disjoncteur h_01HNWC70BQVSFS7G330NF4XHEP=configurer-la-m%C3%A9thode-du-disjoncteur h_01HNWC70BQ097J2VXW0XKSH3M9=configure-circuit-breaker-basics h_01HNWC70BQJWZYZEDJJ5J7JX6X=api-request::ef73eae0 request-body-json=corps-de-la-requ%C3%AAte-json h_01HNWC70BQ6R955776Y6H4EZRG=corps-de-la-requ%C3%AAte-json h_01HNWC70BQRZEZ4PTV59FGYS4Z=configure-circuit-breaker-curl-example-and-response h_01HNWC70BQPP5X9JH1HJ1K58H4=http-response-codes::d35e3a62 response-codes::b056f2a3=codes-de-r%C3%A9ponse-4 h_01HNWC70BQWQ5KWZX8BM0A7BC5=codes-de-r%C3%A9ponse-4 get-configuration-method=obtenir-la-m%C3%A9thode-de-configuration h_01HNWC70BQZY6TYSQBWZ17S0W5=obtenir-la-m%C3%A9thode-de-configuration h_01HNWC70BQY6CPZA5A56J3TET0=get-configuration-basics h_01HNWC70BQ444XNRRCZZH2GFJH=api-request::a2a93b39 h_01HNWC70BQJ8J2WGXE2QF144FK=json-response::fee92c h_01HNWC70BQ701HZR6PYC0CW88T=get-configuration-curl-example-and-response h_01HNWC70BQ8R5GR906Y9W79E81=http-response-codes::90a409c response-codes::ebf1292a=codes-de-r%C3%A9ponse-7 h_01HNWC70BQDGVBZ94F0N49FF40=codes-de-r%C3%A9ponse-7 report-method=m%C3%A9thode-de-rapport h_01HNWC70BQTBMNKHV4RH4ZQ0AE=m%C3%A9thode-de-rapport h_01HNWC70BQ4K7T3FXZWV5KW3FM=report-basics h_01HNWC70BQMBD2WNVQH69FMSPR=api-request::b28cedb0 parameters::e6795217=param%C3%A8tres-4 h_01HNWC70BQ0FDT4T2RAJEPAHNC=param%C3%A8tres-4 h_01HNWC70BQRZTXMKD30V7QQPE4=csv-response h_01HNWC70BQV61TVE65TQ3WWGCP=test-curl-example-and-response::66e922 h_01HNWC70BQQ3MP256QK0JT2K78=http-response-codes::8454f45d response-codes::a8a9822d=codes-de-r%C3%A9ponse-8 h_01HNWC70BQTPPWA4SNG25E8FFB=codes-de-r%C3%A9ponse-8 exclude-app-method=m%C3%A9thode-dexclusion-de-lapplication h_01HNWC70BQ9SK2XCBGGHXVMRDV=m%C3%A9thode-dexclusion-de-lapplication h_01HNWC70BQ8GGRTQ1RW1KCY0SQ=exclude-app-method-basics h_01HNWC70BQ4D62SZCHKGEP6RMJ=api-request::1054abca parameters::f5e3c6ce=param%C3%A8tres-5 h_01HNWC70BREG4XQJV3X9518FC5=param%C3%A8tres-5 h_01HNWC70BR2PVDHTG64WZ36KPV=exclude-app-curl-example h_01HNWC70BR7XCTW6N69GEB4ARF=http-response-codes::7991b66 response-codes::addfcfd8=codes-de-r%C3%A9ponse-8 h_01HNWC70BRN8BHWF6WGY2RH45X=codes-de-r%C3%A9ponse-8 remove-excluded-app-method=supprimer-la-m%C3%A9thode-dexclusion-dapp h_01HNWC70BR18P0H96VN64RS05G=supprimer-la-m%C3%A9thode-dexclusion-dapp h_01HNWC70BRAWBGC5EE0Q8XBTW1=remove-excluded-app-method-basics h_01HNWC70BRD885KN6YDXQ9GXS2=api-request::9504d16f parameters::34936c8f=param%C3%A8tres-6 h_01HNWC70BR4ADH7T3AFG58FZH6=param%C3%A8tres-6 h_01HNWC70BRK7DM7MW150AFVKG2=remove-excluded-app-curl-example h_01HNWC70BRMFN4RM65YV2NWR29=http-response-codes::b5e059da response-codes::e8de940a=codes-de-r%C3%A9ponse-8 h_01HNWC70BRHA8AA7ZV1R4EBYJH=codes-de-r%C3%A9ponse-8 h_01HNWC70BRTZZWME7QCP8HV9AY=code-sample additional-information=informations-suppl%C3%A9mentaires h_01HNWC70BRN0NGTQVWED6VG81Y=informations-suppl%C3%A9mentaires h_01HNWC70BRS884G8RCMAPFPV1N=troubleshooting h_01HNWC70BRP3BVJSHSD1CPCB9S=faq h_01HNWC70BRDN37MBTEKT0DH8CT=traits" />
