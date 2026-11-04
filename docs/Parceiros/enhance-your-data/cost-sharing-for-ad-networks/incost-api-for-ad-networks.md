---
title: API InCost para ad networks
metadata:
  keywords:
    - Advertisers
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
  created_at: '2020-04-26T19:13:47Z'
  edited_at: '2026-09-16T00:35:58Z'
  id: 360007714957
  locale: pt
  section: Cost sharing for ad networks
  section_id: 6551141756177
  url: https://support.appsflyer.com/hc/pt/articles/360007714957
---
> **Visão geral:** A API InCost, parte do AppsFlyer ROI360, permite que ad networks enviem programaticamente dados de custos de publicidade para a AppsFlyer. Isso fornece aos anunciantes dados de custo agregados e permite que eles entendam o verdadeiro impacto da sua rede.

<div id="about-incost-api" />

## Sobre a API InCost

A API InCost é a solução ideal para redes de anúncios enviarem dados de custo para a AppsFlyer. Os parceiros da ad network enviam dados detalhados de custos de publicidade para a AppsFlyer usando a API. A AppsFlyer ingere e processa os dados e os disponibiliza para anunciantes e parceiros por meio de painéis e relatórios.

<div id="benefits" />

#### Benefícios

* Ajude seus clientes a entender o verdadeiro impacto da sua rede com relatórios de custos sem atrito. Sem dados de custo, seus clientes perdem uma peça crucial do quebra-cabeça de mensuração e não conseguem medir o ROAS com precisão. Dessa forma, eles podem investir erroneamente em outros canais de mídia, impactando negativamente seus resultados financeiros.
* Comprove seu ROI com uma solução que garante mensuração de custos precisa, completa e em tempo real.
* A API InCost é rápida e simples de implantar, e o impacto é quase imediato. Você também obtém controle total sobre como e quando envia os dados, incluindo a capacidade de enviar dados de custo de até 90 dias atrás.
* A API InCost é compatível com todos os modelos de preços de campanha, não apenas ao CPI (que é o único modelo disponível ao enviar custo por clique).
* Destaque-se na AppsFlyer Partner Marketplace com um selo de “Custo” que indica que este é um recurso compatível.

<div id="implementing-incost-api" />

## Implementando a API InCost

**Pré-requisitos**: Para elegibilidade à API InCost, sua ad network requer:

* Que 90% das campanhas contêm o ID da campanha na atribuição.
* Capacidade de enviar dados pelo menos 6 vezes por dia para maior atualização dos dados. Os horários específicos ficam a critério da ad network.
* [Se a ad network atualizar dados retroativamente] A capacidade de enviar dados dos últimos 7 dias sempre, para maior conclusão de dados.

**Para implementar a API InCost e começar a enviar dados de custo para o AppsFlyer**:

* Siga as etapas na tabela a seguir.

| Passo # | Ação |
| --- | --- |
| 1 | Solicitar o InCost:<ol><li>Na AppsFlyer, no menu superior, selecione **Ajuda** > **Entre em contato com nossa equipe**.<br />O widget Assistente de parceiro é aberto.</li><li>Selecione **Habilitar mensuração de custos** e envie suas informações.<br />Após o envio, um ticket será aberto e um engenheiro de soluções para parceiros da AppsFlyer entrará em contato com você.</li></ol> |
| 2 | Certifique-se de que as hierarquias de campanha (ID da campanha e, opcionalmente, ID do conjunto de anúncios e ID do anúncio) estejam incluídas nos seus links de atribuição para mais de 90% do seu tráfego. |
| 3 | Obtenha o  <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">Token de API</Anchor> da AppsFlyer no dashboard da AppsFlyer. |
| 4 | Envie o token da API ao seu desenvolvedor para usar no cabeçalho de autorização da API e peça que ele siga <Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-overview">as instruções</Anchor> para implementar os três métodos da API:<ol><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/app-list-ad-nets-api-get">Obtenha a lista de aplicativos</Anchor>.</li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-uploader-post">Upload do inCost</Anchor>: Informe ao desenvolvedor com quais campos preencher o JSON:<ul><li>Campos obrigatórios devem ser preenchidos. Ou seja, não envie campos vazios.</li><li>O canal de mídia é restrito aos canais de mídia associados (registrados) à sua conta de ad network. Obtenha a lista com seu gerente de desenvolvimento de parceiros.</li><li>Leve em consideração o <Anchor target="_blank" href="/marketers/pt/docs/about-data-freshness-and-timezone-support#fuso-horário-específico-do-aplicativo">fuso horário</Anchor> do aplicativo (conforme relatado pela API Obter lista de permissões do aplicativo) para alinhar as datas dos dados de custo com as do aplicativo.</li><li>Se houver campos que não fazem parte da hierarquia de relatórios de custos da sua campanha, não os inclua. Por exemplo, ID do conjunto de anúncios, nome do ativo, ID do anúncio, nome do anúncio.</li></ul></li><li><Anchor target="_blank" href="https://dev.appsflyer.com/hc/reference/incost-jobstatus-get">Obtenha o status de trabalho</Anchor>.</li></ol> |
| 5 | Teste a integração:<ol><li>No tópico do ticket (da etapa 1), notifique a AppsFlyer que a implementação da API foi concluída e obtenha permissões para os aplicativos a seguir, que podem ser usados para testar a API sem usar dados reais:<ul><li>com.cost.app</li><li>id888123456</li></ul></li><li>Na AppsFlyer, no menu lateral, selecione **Colaborar** > **Partner Marketplace** e selecione o parceiro.</li><li>Clique em **Configurar Integração**.</li><li>Selecione 1 dos aplicativos de teste.</li><li>Abra a aba de **Custo** do parceiro integrado</li><li>Ative a alavanca **Obter dados de custo**.</li><li>Clique em **Salvar custo**.</li><li>Clique em **Testar conexão**.<br />A API está ativa.</li></ol> |
| 6 | No tópico do ticket (da etapa 1), notifique a AppsFlyer que a implementação da API foi concluída e aguarde a confirmação de que sua integração está operacional. |
| 7 | Certifique-se de que seus anunciantes habilitem <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#cost-tab">Obter dados de custo</Anchor> na aba de custo da página de parceiro integrado da AppsFlyer. Dessa forma, eles começarão a receber dados de custos. |

<div id="note" />

> 📘 **Importante!**
>
> Prática recomendada: reenviar dados para uma determinada data apenas se o custo tiver mudado. Você pode enviar os últimos 7 dias em todas as chamadas, mas não precisa reenviar registros inalterados.

<div id="fields-for-incost-upload-json" />

### Campos para InCost Upload JSON

<table><thead><tr><th>Campo</th><th>Obrigatório</th><th>Observações</th></tr></thead><tbody><tr><td>data</td><td><span>Sim</span></td><td><ul><li><span>Data do gasto</span></li><li> Formato: <code>YYYY-MM-DD</code> </li><li> <span>Exemplo:</span><code><span>2019-12-30</span></code> </li></ul></td></tr><tr><td>ativado</td><td>Sim</td><td><ul><li>O ID do aplicativo conforme aparece na plataforma AppsFlyer</li><li><span>Formato: String de até 250 caracteres</span></li><li> <span>Exemplo: </span><span>Android:<code>com.app.name</code>, </span>iOS: <code>id123456789</code> </li></ul></td></tr><tr><td><span>fonte_de_mídia</span></td><td><span>Sim</span></td><td><ul><li><span>Nome da rede (ID) que exibe o anúncio associado à sua conta de parceiro de ad network da AppsFlyer</span></li><li><span>Formato: String 50 caracteres</span></li><li> Exemplo: <code>network_int</code> </li></ul></td></tr><tr><td><span>af_prt</span></td><td><span>Não\*</span></td><td><ul><li>Obrigatório para atribuição de agência e dados de custo. </li><li>Nome da agência conforme exibido no link de atribuição e associado à conta da agência na AppsFlyer. </li><li>Formato: String 50 caracteres </li><li>Exemplo: <code>agencya</code> </li><li>Se os dados de custo forem reenviados para as mesmas datas e <code>af_prt</code> for incluído em uma chamada subsequente da API, quando estava ausente na original, isso resultará em dados de custo duplicados.</li></ul></td></tr><tr><td><span>id_da_campanha</span></td><td><span>Sim</span></td><td><ul><li> Deve ser idêntico ao <code>af_c_id</code>parâmetro enviado no link de atribuição </li><li><span>Não é permitido um string vazio</span></li><li><span>Formato: String 24 caracteres</span></li><li> <span>Exemplo: <code>123abc</code></span><span></span> </li></ul></td></tr><tr><td><span>campaign_name</span></td><td><span>Sim</span></td><td><ul><li><span>Formato: String 100 caracteres</span></li><li> Exemplo: <code>my_campaign123</code> </li></ul></td></tr><tr><td><span>id_conjunto_de_anúncios</span></td><td>Não\*</td><td><ul><li> Obrigatório se você enviar <span><code>ad_name</code></span>. </li><li> Deve ser idêntico ao <code>af_adset_id</code>parâmetro enviado no link de atribuição </li><li> Se o seu relatório de custos não for compatível <code>adset_id</code>, nunca o envie </li><li><span>Formato: String 24 caracteres</span></li><li> <span>Exemplo: </span><code><span>123A</span></code> </li></ul></td></tr><tr><td><span>adset_name</span></td><td><span>Não</span></td><td><ul><li> Se você enviar este campo, você também deve enviar <code>adset_id</code> </li><li><span>Formato: String 100 caracteres</span></li><li> Exemplo:<code>my_adset_name</code> </li></ul></td></tr><tr><td><span>id_anúncio</span></td><td>Não\*</td><td><ul><li>Obrigatório se você enviar <code>adset_name</code> </li><li> Esse campo deve ser idêntico ao parâmetro <code>af_ad_id</code> enviado no link de atribuição </li><li> Se o seu relatório de custos não for compatível <code>adset_id</code>, nunca o envie </li><li><span>Formato: String 24 caracteres</span></li><li>Exemplo:<code>123AB</code> </li></ul></td></tr><tr><td><span>id_do_site</span></td><td>Não</td><td><ul><li>ID exclusivo que identifica o publisher que exibe o anúncio.</li><li>Formato: String 24 caracteres.</li></ul></td></tr><tr><td><span>ad_name</span></td><td><span>Etapa #</span></td><td><ul><li> Se você enviar este campo, você também deve enviar <code>ad_id</code> </li><li><span>Formato: String 100 caracteres</span></li><li>Exemplo:<code>Ad-name</code> </li></ul></td></tr><tr><td><span>geo</span></td><td><span>Sem</span></td><td><ul><li><span>O país que você registrou como associado ao custo</span></li><li><span>Sempre que possível, isso deve representar o país onde o anúncio foi exibido</span></li><li><span>Formato: <span>Código de país ISO 3166 de 2 caracteres</span></span></li><li> Exemplo:<code>US, CN, ZA</code> </li></ul></td></tr><tr><td>símbolos monetários</td><td><span>Sim</span></td><td><ul><li><span>Tipo de moeda do gasto</span></li><li><span>Formato: <span>Código de moeda ISO 4217 de 3 caracteres</span></span></li><li> <span>Exemplo:</span> <span><code>USD, EUR, ZAR</code></span> </li></ul></td></tr><tr><td>gasto</td><td>Sim</td><td><ul><li>Valor do gasto usando a moeda especificada </li><li>Cinco dígitos permitidos após a vírgula</li><li>O valor 0 (zero) é permitido</li><li>Valores negativos NÃO são permitidos</li><li>Não envie<code>,</code>delimitadores</li><li>Não envie valores entre aspas. </li><li>Formato: Número decimal</li><li>Valores de exemplo: <code>1</code> <code>1.2</code> <code>1234.20</code> </li></ul></td></tr><tr><td>Canal</td><td>Não</td><td><ul><li> <span>Deve ser idêntico ao parâmetro</span> <span><code>af_channel</code></span> enviado no link de atribuição</li><li>Formato: String 20 caracteres</li><li>Exemplo:<code>my_channel</code> </li></ul></td></tr><tr><td>keywords</td><td>Não</td><td><ul><li>Formato: String 100 caracteres</li><li>Exemplo:<code>abc app</code> </li></ul></td></tr><tr><td>reported_clicks</td><td>Não</td><td><ul><li>Número de cliques reportado pela network para este registro.</li><li>Não envie valores entre aspas.</li><li>Exemplo: <code>123A</code> </li><li>OPCIONAL. Se estiver vazio ou for omitido, será reportado como 0.</li><li>Valores decimais ou negativos são rejeitados (erro 422: <code>Reported clicks can be positive integer</code>).</li></ul></td></tr><tr><td>reported_impressions</td><td>Não</td><td><ul><li>Número de impressões reportado pela network para este registro.</li><li>Não envie valores entre aspas.</li><li>Exemplo:<code>2019-12-30</code> </li><li>OPCIONAL. Se estiver vazio ou for omitido, será reportado como 0.</li><li>Valores decimais ou negativos são rejeitados (erro 422: <code>Reported impression can be positive integer</code>).</li></ul></td></tr><tr><td colspan="3">\* Veja a coluna de observações, pois em alguns casos é necessário enviar este campo.</td></tr></tbody></table>

<div data-zendesk-anchors="incost-api=sobre-a-api-incost h_01HE0WCBD9GD66KB1QGQ9MEXBJ=sobre-a-api-incost benefits=benef%C3%ADcios h_01HKVW85AYFG91PGYE5BDQVJNR=benef%C3%ADcios implementing-incost-api=implementando-a-api-incost h_01HKVWSWTWETTES5ZTNZ05X9VA=implementando-a-api-incost h_01M2J3GBMFJW7XT08MK5JR3D3Y=importante fields-for-incost-upload-json=campos-para-incost-upload-json h_01HM8VCV81GQ6XQ4NA1EDCZ4K7=campos-para-incost-upload-json" />
