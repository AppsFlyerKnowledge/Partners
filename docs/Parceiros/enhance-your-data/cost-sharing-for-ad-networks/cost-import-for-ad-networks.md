---
title: Cost Import para ad networks
metadata:
  keywords:
    - Ad Networks
    - Partners
    - Gray
    - ROI360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-maytav-avnat
    - ROI360
    - Ad Networks
  created_at: '2019-10-20T06:03:13Z'
  edited_at: '2026-08-18T00:38:36Z'
  id: 360002868097
  locale: pt
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/pt/articles/360002868097
---
> **Resumo:** descubra como as ad networks podem relatar os custos de campanha diretamente para a AppsFlyer, através de arquivos CSV.

<div id="cost-import-for-ad-networks" />

## Cost Import para ad networks

![AdspendIngestion.jpg](https://files.readme.io/e870005c5f20531a2d06cc78b47a82a8a1f730f2c04728f5d0a5674c1c70129a-24507313816337.jpg)

<div id="overview" />

#### Visão geral

* Prepare um arquivo CSV com as informações de ad spend da seguinte forma:
  * Data do investimento
  * App ID (são permitidos várias aplicativos por arquivo, se esses aplicativos pertencerem ao mesmo proprietário)
  * Canal de mídia (um por arquivo)
  * Nome da campanha
  * Gasto total
  * [Opcional] Geo
  * [Opcional] Moeda (por padrão, a moeda é USD)
* Envie o arquivo por e-mail/upload de arquivo utilizando a conta da ad network na AppsFlyer.   
  **Atenção:**
  * Antes de enviar os arquivos pela primeira vez, o anunciante deve conceder à ad network uma permissão de acesso ao Cost Import. Esse é um processo rápido, que deve ser feito uma vez para cada app.
  * Quando um arquivo é enviado, ele não pode ser alterado.
* Verifique se o arquivo não possui nenhum erro.

<div id="submitting-ad-spend-files-for-ad-networks" />

### Envio de arquivos de ad spend para ad networks

* Use o método de upload ou e-mail para ingerir arquivos de ad spend.
* [Prática recomendada] A princípio, use o método de upload - com ele, é mais fácil solucionar problemas de formatação do CSV.
* Ad networks não podem importar dados de custo da agência; apenas anunciantes podem.

<div id="submission-by-file-upload" />

#### Envio por upload de arquivo

**Para transferir arquivos de Cost Import por upload:**

1. [Para cada app, essa ação deve ser feita uma vez] <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-permissions-for-ad-networks">Peça ao anunciante que ele lhe conceda a permissão de acesso ao Cost Import</Anchor>.
2. <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#prepare-csv-file-with-cost-data">Prepare o arquivo CSV utilizando esse formato e esquema</Anchor>.
3. Clique aqui para fazer o <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">login na sua conta da AppsFlyer.</Anchor>
4. <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#upload-file">Faça o upload e a ingestão do arquivo</Anchor>.
5. No dashboard da AppsFlyer, monitore a ingestão:

   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">Estado</Anchor>
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#matched-rows">Correspondência de linhas</Anchor>
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">Ações de Cost Import</Anchor>
6. Procedimentos adicionais:
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">Substitua a ingestão anterior</Anchor>
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">Reverter (cancelar)</Anchor>

<div id="submission-by-email" />

#### Envio por e-mail

**Para enviar arquivos de Cost Import por e-mail:**

1. [Para cada app, essa ação deve ser feita uma vez] <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-permissions-for-ad-networks">Peça ao anunciante que ele lhe conceda a permissão de acesso ao Cost Import</Anchor>.
2. <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#prepare-csv-file-with-cost-data">Prepare o arquivo CSV utilizando esse formato e esquema</Anchor>.
3. Se não você não tiver um token de Cost Import (que será necessário para enviar o arquivo por e-mail):
   * Clique aqui para fazer o <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">login na sua conta da AppsFlyer.</Anchor>
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#token-for-email-import">Obtenha um token de Ad Spend.</Anchor> Atenção: O mesmo token é usado para todos os anunciantes.
4. Envie o arquivo por <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#email-file">e-mail</Anchor>
5. A AppsFlyer envia por e-mail um relatório de status que informa se a ingestão foi bem-sucedida ou se foram encontrados problemas. **Atenção:** se você não receber um e-mail com o relatório de status, verifique o <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">dashboard de Cost Import</Anchor>.
6. No dashboard da AppsFlyer, monitore a ingestão:

   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">Estado</Anchor>
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#matched-rows">Correspondência de linhas</Anchor>
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">Ações de Cost Import</Anchor>
7. Procedimentos adicionais:
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">Substitua a ingestão anterior</Anchor>
   * <Anchor target="_blank" href="/marketers/pt/docs/import-cost-data#cost-import-dashboard">Reverter (cancelar)</Anchor>

<div data-zendesk-anchors="ad-spend-ingestion-for-ad-networks=cost-import-para-ad-networks h_01HX94WSX07YEG40X66TMRFJGA=cost-import-para-ad-networks overview=vis%C3%A3o-geral h_01HX94WSX0HR2KTGRT7MQ481Y6=vis%C3%A3o-geral submitting-ad-spend-files-for-ad-networks=envio-de-arquivos-de-ad-spend-para-ad-networks h_01HX94WSX0G429FTHKYCG07BB9=envio-de-arquivos-de-ad-spend-para-ad-networks submission-by-file-upload=envio-por-upload-de-arquivo h_01HX94WSX0ENTJEDMXWRHDCP0D=envio-por-upload-de-arquivo submission-by-email=envio-por-e-mail h_01HX94WSX0HVTMFQQ0NMW0VSKP=envio-por-e-mail" />
