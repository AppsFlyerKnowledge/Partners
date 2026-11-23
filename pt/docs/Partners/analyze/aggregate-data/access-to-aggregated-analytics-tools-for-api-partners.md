---
title: Acesso a ferramentas de análise agregadas para parceiros API
metadata:
  keywords:
    - Anunciantes
    - Redes de anúncios
    - Parceiros
    - Premium API
    - Comerciantes
    - Análise de marketing
x-zendesk:
  category: Parceiros
  category_id: 6550456653457
  content_tags:
    - pm-nohar-avigal
    - Comerciantes
    - Análise de marketing
    - Redes de anúncios
  created_at: '2020-02-17T10:50:10Z'
  edited_at: '2026-08-13T13:36:27Z'
  id: 360005854857
  locale: ptbr
  section: Dados agregados
  section_id: 6551715006353
  url: >-
    https://support.appsflyer.com/hc/pt-br/articles/360005854857-Access-to-aggregated-analytics-tools-for-API-partners
---
> **Em instância:** parceiros API podem usar seu token de API para acessar os dados de anunciantes quando concedidos permissões pelo anunciante, permitindo que extraam métricas de desempenho da plataforma.

<div id="api-token-permissions" />

## Permissões do token API

<Image align="center" alt="api-access-permissions.jpg" src="https://files.readme.io/7961394cb39cf1e6f85d77cd732183edea5fb1408c220ca05b23ae7bbb50138e-23701010316689.jpg" width="439px" />

Anunciantes podem conceder as seguintes permissões a nível de app:

| Tipo de permissão             | Ferramenta de relatórios                                                                                                                                                                                                                                                          | Limitações                                                                                         |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Relatório de análise agregada | <Anchor target="_blank" href="/marketers/docs/cohort-analytics-via-data-locker">Dados de análise Cohort via DataLocker</Anchor>                                                                                                                                                   | Dados das campanhas de anúncios não estão disponíveis para parceiros API devido a suas restrições. |
| Relatório SKAN                | <ul><li><Anchor target="_blank" href="/marketers/docs/skan-aggregated-performance-report-api">SKAN de desempenho reportando</Anchor></li><li><Anchor target="_blank" href="/marketers/docs/skan-aggregated-postback-arrival-date-api">SKAN agregado publicando</Anchor></li></ul> | --                                                                                                 |

<div id="considerations" />

### Considerações

- **Perspectiva do anunciante**
  - Os anunciantes podem conceder permissões para parceiros API como listados na tabela anterior.
- **perspectiva dos parceiros**
  - Extraia dados por API. **Nota**: Segurança está implementada através de uma autenticação<Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">token</Anchor> disponível no painel AppsFlyer. O mesmo token é válido para todos os aplicativos e anunciantes.
  - Obter dados via Data Locker
  - Anunciantes podem revogar permissões para acessar seus dados de aplicativos. Isso não afetará suas credenciais de parceiros.

<Accordion title="Granting access to the partner">

<div id="important" />

> 🚧 **Importante**
>
> **aviso**
>
> - O tipo de permissão permite que o parceiro acesse dados, incluindo o tráfego trazido por outros parceiros e dados orgânicos.
> - Não compartilhe seu token com parceiros.

**Conceda acesso da API ao parceiro:**

1. Em AppsFlyer, no menu lateral, selecione **Colaborar** > **Parceiros integrados**.
2. Pesquisar pelo parceiro e selecioná-lo.
3. Clique **Configurar integração**. Você está direcionado para a página de configuração de integração.
4. Na guia **Acesso à API**, ative uma ou mais permissões. Selecione de:
   - **Relatórios de análise agregados**
   - **Relatórios do SKAdNetwork** (para aplicativos iOS, não relevantes para o Localizador de Dados)
5. Clique em **Salvar acesso de API**.
6. Notificar o parceiro que você ativou o necessário acesso à API.

</Accordion>

<div data-zendesk-anchors="api-access-permissions=api-token-permissions h_01HGG3N6KVF9MCQRW8594YG0HV=api-token-permissions h_01HT2J7ZFVDA812R35948XXEM1=considerations h_01KZXND2TWVKK51RH3JWNMFENK=considerations" />
