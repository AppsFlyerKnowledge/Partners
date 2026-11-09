---
title: Acesso a ferramentas de análises agregadas para parceiros de API
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Premium API
    - Marketers
    - Marketing Analytics
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Marketers
    - Marketing Analytics
    - Ad Networks
  created_at: '2020-02-17T10:50:10Z'
  edited_at: '2026-08-19T00:36:18Z'
  id: 360005854857
  locale: pt
  section: Aggregate data
  section_id: 6551715006353
  url: https://support.appsflyer.com/hc/pt/articles/360005854857
---
> **At a glance:** Os parceiros de API podem usar o token de API para acessar os dados dos anunciantes quando a permissão é concedida pelo anunciante, permitindo extrair métricas de performance da plataforma.

<div id="api-token-permissions" />

## Permissões de token da API

<Image align="center" alt="api-access-permissions.jpg" src="https://files.readme.io/7961394cb39cf1e6f85d77cd732183edea5fb1408c220ca05b23ae7bbb50138e-23701010316689.jpg" width="439px" />

Os anunciantes podem conceder as seguintes permissões no nível do aplicativo:

| Tipo de permissão | Ferramenta de relatório | Limitações |
| --- | --- | --- |
| Relatórios de analytics agregados | <Anchor target="_blank" href="/marketers/pt/docs/cohort-analytics-via-data-locker">Dados de analytics de coorte via DataLocker</Anchor> | Os dados de campanhas de anúncios do X não estão disponíveis para parceiros de API devido às restrições do X. |
| Relatórios SKAN | <ul><li><Anchor target="_blank" href="/marketers/pt/docs/skan-aggregated-performance-report-api">Relatório de performance da SKAN</Anchor></li><li><Anchor target="_blank" href="/marketers/pt/docs/skan-aggregated-postback-arrival-date-api">Relatório de postback agregado da SKAN</Anchor></li></ul> | -- |


<div id="considerations" />

### considerações

* **Perspectiva do anunciante**
  * Os anunciantes podem conceder ao parceiro de API as permissões listadas na tabela anterior.
* **Perspectiva do parceiro**
  * Extrair dados por API. **Observação**: a segurança é implementada por meio de um <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">token</Anchor> de autenticação disponível no dashboard da AppsFlyer. O mesmo token é válido para todos os aplicativos e anunciantes.
  * Obter dados via Data Locker
  * Os anunciantes podem revogar as permissões de acesso aos dados do aplicativo. Isso não terá impacto nas suas credenciais de parceiro.

<Accordion title="Conceder acesso ao parceiro">

> 🚧 **Important**
>
> **atenção**
>
> * O tipo de permissão permite que o parceiro acesse os dados, incluindo o tráfego gerado por outros parceiros e os dados orgânicos.
> * Não compartilhe seu token com parceiros.

**Para conceder acesso à API ao parceiro:**

1. Na AppsFlyer, no menu lateral, selecione **Collaborate** > **Integrated partners**.
2. Pesquise o parceiro e selecione-o.
3. Clique em **Configurar Integração**. Você será direcionado para a página de configuração da integração.
4. Na guia **acesso à API**, ative uma ou mais permissões. Selecione entre:
   * **Relatórios analíticos agregados**
   * **Relatórios da SKAdNetwork** (para aplicativos iOS, não relevante para o Data Locker)
5. Clique em **Salvar acesso à API**.
6. Notifique o parceiro de que você habilitou o acesso à API necessário.

</Accordion>

<div data-zendesk-anchors="api-access-permissions=permiss%C3%B5es-de-token-da-api h_01HGG3N6KVF9MCQRW8594YG0HV=permiss%C3%B5es-de-token-da-api considerations=considera%C3%A7%C3%B5es h_01HT2J7ZFVDA812R35948XXEM1=considera%C3%A7%C3%B5es h_01KZXND2TWVKK51RH3JWNMFENK=considera%C3%A7%C3%B5es" />
