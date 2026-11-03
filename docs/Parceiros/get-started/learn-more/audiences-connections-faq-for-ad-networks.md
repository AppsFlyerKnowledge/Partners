---
title: FAQ sobre conexões do Audiences para ad networks
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Audience Segmentation
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-neama-benhabib
    - Marketers
    - Audience Segmentation
    - Ad Networks
  created_at: '2023-11-27T08:25:39Z'
  edited_at: '2026-08-19T00:38:53Z'
  id: 20459388348305
  locale: pt
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/pt/articles/20459388348305
---
> **Visão geral:** Você é uma ad network? Encontre respostas para perguntas frequentes sobre conexões de parceiros do Audiências.

## Chave de API e chave de pull do parceiro

<div id="what-are-the-api-key-and-testing-api-key-used-for" />

<Accordion title="Para que servem a chave de API e a chave de API de teste?">

A **chave de API** é uma chave exclusiva emitida pelo parceiro para cada anunciante. A chave de API identifica o anunciante em cada chamada de API e geralmente é uma longa string hexadecimal (por exemplo, d41ac239b3b918e28fa0c). No processo de teste, precisaremos que você nos forneça uma **chave de API de teste**, que usaremos para testar sua integração de audiências.

</Accordion>

<div id="what-is-the-partner_pull_key" />

<Accordion title="O que é a PARTNER_PULL_KEY ?">

A `PARTNER_PULL_KEY` é uma chave gerada pela AppsFlyer e fornecida a cada parceiro. Ela é usada pelo parceiro na variável de modelo localizada na URL `{{PARTNER_PULL_KEY}}` para fazer o download do arquivo de segmento.

</Accordion>

<div id="how-and-when-does-the-partner-get-the-partner_pull_key" />

<Accordion title="Como e quando recebemos a PARTNER_PULL_KEY?">

A equipe de audiências da AppsFlyer enviará a você uma `PARTNER_PULL_KEY` quando testarmos seu endpoint `/sync` em uma fase posterior.

</Accordion>

## Arquivo de audiência, tamanho e limitações

<div id="is-there-a-limitation-on-segment-size" />

<Accordion title="Há alguma limitação no tamanho do segmento?">

Fazemos upload dos dados em um upload multipart para o AWS S3. Para ver os limites da AWS, consulte: https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html

</Accordion>

<div id="how-large-are-the-files" />

<Accordion title="Qual é o tamanho dos arquivos?">

Oferecemos suporte para arquivos grandes. No fim, são arquivos CSV armazenados no AWS S3. Para ver os limites da AWS, consulte: https://docs.aws.amazon.com/AmazonS3/latest/userguide/qfacts.html

</Accordion>

<div id="is-there-an-upper-limit-for-device-id-rows" />

<Accordion title="Existe um limite máximo de linhas de Device ID?">

O número máximo de linhas depende do limite de tamanho de arquivo de 5 TB da AWS.

</Accordion>

<div id="can-we-use-a-direct-amazon-aws-pathbucket-for-the-audience-api" />

<Accordion title="Podemos usar um caminho/bucket direto da Amazon AWS para a API de audiências?">

Sim, forneceremos um bucket da AWS e enviaremos uma URL pré-assinada para um caminho na AWS onde o arquivo está localizado.

</Accordion>

<div id="is-the-file-compressed" />

<Accordion title="O arquivo está compactado?">

Sem.

</Accordion>

<div id="does-the-audience-have-a-default-validity-period" />

<Accordion title="A audiência tem um período de validade padrão?">

Uma audiência não expira. Depois que uma audiência é criada e conectada, ela é enviada todos os dias. No entanto, uma audiência pode ser excluída; nesse caso, ela deixa de ser enviada.

</Accordion>

<div id="is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id" />

<Accordion title="O formato do arquivo é separado por quebra de linha (ou por vírgula)? A primeira linha é um cabeçalho como advertiser_id ?">

Ele é separado por quebra de linha, e a primeira linha é um cabeçalho como `advertiser_id_sha256` (com base no identificador enviado).

</Accordion>

<div id="will-each-sync-request-have-urls-to-all-3-files-adid-email-and-phone" />

<Accordion title="Cada solicitação para /sync terá URLs para todos os 3 arquivos (por exemplo, ADID, e-mail e telefone)?">

Cada solicitação para `/sync` conterá as URLs dos arquivos compatíveis com a integração. Se houver suporte para ADID, e-mail e telefone, ela conterá essas 3 URLs.

</Accordion>

<div id="as-a-result-of-step-3-sync-we-get-a-link-to-download-an-audience-file-is-it-possible-to-generate-and-share-such-url-templates-without-an-api-synchronization" />

<Accordion title="Como resultado da etapa 3 ( /sync ), recebemos um link para baixar um arquivo de audiência. É possível gerar e compartilhar esses modelos de URL sem uma sincronização de API?">

No momento, não. As URLs são geradas com base na sua `PARTNER_PULL_KEY` exclusiva. Na fase de teste, as URLs serão fornecidas e poderão ser testadas.

Aqui está um exemplo de URL:

`https://audiencespull.appsflyer.com/{{PARTNER_PULL_KEY}}/12cjv4dq1zyxz3nh-HASHED.csv?` X-Amz-A lgorithm=AWS1-HMAC-SHA256&X-Amz-Date=20190503T091923Z&X-Amz-SignedHeaders=host&X-Amz-Expires=3599&X-Amz-Credential=AKIB22QYTATEGB2HBFJR%2F20190603%2Feu-west-1%2Fs3%2Faws4\_request&X-Amz-Signature=c8287819a21d2f7832154df609c55ab8c0afe53540d542918b2739a9234923a

</Accordion>

<div id="what-do-we-need-container_id-for" />

<Accordion title="Para que precisamos de container_id ?">

Enviaremos os IDs de dispositivo da audiência para o ID do contêiner especificado por você via API. A criação do contêiner de audiência é obrigatória para o desenvolvimento da integração de audiências.

</Accordion>

## Chamadas de API, respostas e códigos de status

<div id="when-should-the-partner-return-a-response" />

<Accordion title="Quando devemos retornar uma resposta?">

`/validate`: quando a chave de API corresponder à que foi fornecida a você.

`/create`: quando o contêiner tiver sido criado no seu sistema.

`/sync`: Esperamos receber uma resposta depois que você receber a nossa chamada e conseguir acessar o arquivo. Você pode fazer o download e processar o arquivo depois de enviar a resposta. O link fica disponível para download por um período de 2 horas.

</Accordion>

<div id="how-should-partners-handle-failed-requests" />

<Accordion title="Como devemos lidar com solicitações com falha?">

Por meio de códigos de status:

200 - quando a solicitação for bem-sucedida

401 - para chave de API inválida - autenticação

Não oferecemos suporte a outros casos imediatamente. Nesses casos, o anunciante verá que um upload falhou devido a um erro geral. Se houver problemas recorrentes, entre em contato conosco para discutir esses casos.

</Accordion>

<div id="when-are-these-endpoints-being-called-by-appsflyer" />

<Accordion title="Quando a AppsFlyer chama nossos endpoints?">

`/validate`: A AppsFlyer chamará esse endpoint uma vez sempre que um anunciante criar uma nova conexão com você.

`/create`: Esse endpoint é chamado apenas uma vez por contêiner, ou seja, para cada nova audiência que se conecta a você pela primeira vez, chamamos o endpoint `/create` e armazenamos o ID do contêiner. Esperamos receber um ID de contêiner diferente para cada chamada para `/create`. Separamos as plataformas e os nomes das audiências do nosso lado (em outras palavras, cada plataforma terá sua própria audiência do nosso lado e iniciará uma chamada para `/create`).

`/sync`: Esse endpoint é chamado sempre que um upload é iniciado: seja durante o processo diário que realiza um upload programado de todas as audiências da AppsFlyer, seja sempre que um anunciante inicia um upload manual pela nossa UI ou por uma chamada de API.

</Accordion>

<div id="are-sync-requests-made-only-once-or-will-appsflyer-rerun-the-requests-later" />

<Accordion title="As solicitações para /sync são feitas apenas uma vez ou a AppsFlyer executará as solicitações novamente mais tarde?">

A solicitação para `/sync` é feita sempre que um upload é iniciado. Isso ocorre durante o processo diário que realiza um upload programado de todas as audiências da AppsFlyer ou sempre que um anunciante inicia um upload manual pela nossa UI ou por uma chamada de API.

</Accordion>

<div id="how-often-does-appsflyer-send-out-calls-to-the-sync-endpoint" />

<Accordion title="Com que frequência a AppsFlyer envia chamadas para o endpoint /sync ?">

Isso depende do número de anunciantes com que você trabalha e do número de audiências que eles enviam. Para cada audiência enviada, o endpoint `/sync` será chamado. Isso ocorre durante o processo diário que realiza um upload programado de todas as audiências da AppsFlyer ou sempre que um anunciante inicia um upload manual pela nossa UI ou por uma chamada de API.

</Accordion>

<div id="if-it-has-high-traffic-can-partners-have-a-different-api-than-the-other-two-ie-routes-or-even-domain" />

<Accordion title="Se tivermos alto tráfego, podemos manter vários endpoints de API (por exemplo, várias rotas ou até domínios diferentes)?">

A solução preferencial é garantir que a API atual consiga lidar com um tráfego relativamente alto. Há uma modificação de API disponível; no entanto, isso pode resultar em atrasos de semanas ou meses para concluir a integração.

</Accordion>

## Regras de nomenclatura

<div id="in-the-validate-interface-is-the-api_key-field-a-string-or-string-array" />

<Accordion title="Na interface /validate , o campo api_key é uma string ou uma matriz de strings?">

É uma string.

</Accordion>

<div id="in-the-create-interface-does-the-name-field-audience-name-only-need-to-support-pure-english-or-does-it-need-to-support-other-character-sets-what-are-the-validation-rules-for-names" />

<Accordion title="Na interface /create , o campo name (nome da audiência) deve oferecer suporte apenas a caracteres em inglês ou precisa oferecer suporte a outros conjuntos de caracteres? Quais são as regras de validação para nomes?">

O nome da audiência é idêntico ao nome na UI da AppsFlyer.

* Deve ser um nome exclusivo entre 2 e 100 caracteres
* Todos os idiomas com suporte
* Símbolos especiais com suporte (por exemplo, $, %, ^, @ etc.)

</Accordion>

<div id="in-the-create-interface-must-container_id-be-pure-numbers-or-can-it-support-english" />

<Accordion title="Na interface /create , o container_id deve conter apenas números ou pode oferecer suporte a caracteres em inglês?">

Há suporte a números e caracteres em inglês.

</Accordion>

## SHA256 e URL com hash

<div id="we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded" />

<Accordion title="Por que nossa tentativa de decodificar o GAID/IDFA SHA256 das audiências falhou?">

O SHA256 não foi feito para ser decodificado. Esse mecanismo foi projetado para que você e a AppsFlyer codifiquem o ID do dispositivo (o que permite a você corresponder valores codificados se tiver acesso ao ID original do dispositivo).

</Accordion>

<div id="does-appsflyer-provide-nonhashed-identifiers" />

<Accordion title="A AppsFlyer nos fornece identificadores sem hash?">

Não, IDs de dispositivo sem hash estão disponíveis apenas para anunciantes. Para garantir a privacidade de dados, aplicamos hash aos IDs do anunciante nos arquivos de segmento usando o algoritmo SHA256. Os IDs do anunciante serão enviados usando esta chave no payload da solicitação: `url_adid_sha256`.

</Accordion>

<div id="if-all-gaids-are-hashed-how-can-the-partner-know-which-gaid-they-received" />

<Accordion title="Se todos os GAIDs tiverem hash, como podemos saber quais GAIDs recebemos?">

Se você tiver um GAID em texto simples do aplicativo e um GAID com hash da AppsFlyer, poderá aplicar hash ao GAID em texto simples com SHA256 e, em seguida, correspondê-lo ao GAID com hash da AppsFlyer.

</Accordion>

<div data-zendesk-anchors="api-key-and-partner_pull_key=chave-de-api-e-chave-de-pull-do-parceiro h_01HG7Y7M665JKBJEQK5Z48KYWT=chave-de-api-e-chave-de-pull-do-parceiro h_01HG7YC3NBYN46DXCGJRBZKQ8N=what-are-the-api-key-and-testing-api-key-used-for h_01HG7YC3NB8KW79307GPATW5AH=what-is-the-partner_pull_key h_01HG7YC3NB71TV7EBKX7JH2DVB=how-and-when-does-the-partner-get-the-partner_pull_key audience-file-size-and-limitations=arquivo-de-audi%C3%AAncia-tamanho-e-limita%C3%A7%C3%B5es h_01HG7Z1DS1P6VDHEGDM2DMENYK=arquivo-de-audi%C3%AAncia-tamanho-e-limita%C3%A7%C3%B5es h_01HG7Z5PQFMJQXRF9EQ89RZRF8=is-there-a-limitation-on-segment-size h_01HG7Z5PQFBQGT9STXQ4XVEWEM=how-large-are-the-files h_01HG7Z5PQFN91RC6GDWAGDJS9V=is-there-an-upper-limit-for-device-id-rows h_01HG7Z5PQFPBJPFKD0T38AM7SK=can-we-use-a-direct-amazon-aws-pathbucket-for-the-audience-api h_01HG7Z5PQFZB6F3H917JHH8QR4=is-the-file-compressed h_01HG7Z5PQFVFA8GXVD7HND7AV1=does-the-audience-have-a-default-validity-period is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like-%E2%80%98advertiser_id%E2%80%99=is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id h_01HG7Z5PQF349SS37F3X5ESNBH=is-the-file-format-linebreak-separated-or-comma-separated-and-is-the-first-line-a-heading-like--advertiser_id h_01HG7Z5PQFQAN19PD09GQMSF06=will-each-sync-request-have-urls-to-all-3-files-adid-email-and-phone h_01HGTJD9HQ4ZSZ1GQ9PH4NP6B5=as-a-result-of-step-3-sync-we-get-a-link-to-download-an-audience-file-is-it-possible-to-generate-and-share-such-url-templates-without-an-api-synchronization h_01HG7Z5PQFV6RZJ9PMBETRCM3G=what-do-we-need-container_id-for api-calls-responses-and-status-codes=chamadas-de-api-respostas-e-c%C3%B3digos-de-status h_01HG7ZMJ4FS76K8HF7PP4PJGY3=chamadas-de-api-respostas-e-c%C3%B3digos-de-status h_01HG7ZQCBXRKMRYTC8PB2YDTQ1=when-should-the-partner-return-a-response h_01HG7ZQCBXRHF78ZSBP4RZ8JE3=how-should-partners-handle-failed-requests h_01HG7ZQCBXXPZZ4V7361H43WVX=when-are-these-endpoints-being-called-by-appsflyer h_01HG7ZQCBX5GGP0KFGKZG8N27R=are-sync-requests-made-only-once-or-will-appsflyer-rerun-the-requests-later h_01HG7ZQCBXEFAYE0KJN4DTTVBG=how-often-does-appsflyer-send-out-calls-to-the-sync-endpoint h_01HG7ZQCBXC765AFJSPTE2CC6Z=if-it-has-high-traffic-can-partners-have-a-different-api-than-the-other-two-ie-routes-or-even-domain naming-rules=regras-de-nomenclatura h_01HG800JBTMXQS4GPEFCK64D7H=regras-de-nomenclatura h_01HG80352MXGGZ6KVG0REGN12Q=in-the-validate-interface-is-the-api_key-field-a-string-or-string-array h_01HG80352MYBAWEQQJT4GSR36G=in-the-create-interface-does-the-name-field-audience-name-only-need-to-support-pure-english-or-does-it-need-to-support-other-character-sets-what-are-the-validation-rules-for-names h_01HG80352MYFPQF3SZ05J58VCB=in-the-create-interface-must-container_id-be-pure-numbers-or-can-it-support-english sha256-and-hashed-url=sha256-e-url-com-hash h_01HG814F103B5M3Q2K5110WDEM=sha256-e-url-com-hash we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can%E2%80%99t-sha256-be-decoded=we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded h_01HG816BDJPN86WVFE5RM09KZ8=we-tried-to-decode-audiences-sha256-gaididfa-but-failed-can-t-sha256-be-decoded h_01HG816BDJN9WJZTDG0TG930G9=does-appsflyer-provide-nonhashed-identifiers h_01HG816BDJ7A6GMZC14RKERQB1=if-all-gaids-are-hashed-how-can-the-partner-know-which-gaid-they-received" />
