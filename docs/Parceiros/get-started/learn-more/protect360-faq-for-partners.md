---
title: Protect360-Perguntas frequentes para parceiros
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Protect360
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-yanai
    - Protect360
    - Agencies
    - Ad Networks
  created_at: '2023-06-12T12:43:34Z'
  edited_at: '2026-08-18T00:40:43Z'
  id: 16091549732497
  locale: pt
  section: Learn more
  section_id: 6551121200017
  url: https://support.appsflyer.com/hc/pt/articles/16091549732497
---
> **Visão geral:** Encontre as respostas às perguntas mais frequentes dos parceiros sobre o Protect360.

<div id="impression-level-anomalies" />

## Anomalias ao nível do clique/impressão

<div id="why-are-impressionsclicks-being-capped" />

<Accordion title="Por que as impressões estão sendo limitadas?">

O sistema Protect360 da AppsFlyer leva em conta vários parâmetros ao tomar decisões sobre o limite de engajamentos de anúncios, incluindo, entre outros, o volume de impressões/cliques, o CVR, a taxa de anomalias detectadas, as flutuações normais na atividade, bem como os parâmetros de referência geográficos e da indústria. O algoritmo é dinâmico e atualizado de hora em hora, para levar em consideração tendências sofrendo mudanças.

Quando o mecanismo de limitação é acionado, o Protect360 bloqueia as impressões ou cliques da ad network para o aplicativo relacionado no ciclo atual de 24 horas. Isso significa que todas as impressões/cliques que ocorrem após o limite ser atingido não são registrados pela AppsFlyer, nem são elegíveis para atribuição.

Uma rede pode evitar ultrapassar o limiar, interrompendo campanhas e editores com volumes raramente elevados de engajamentos de anúncios que não mostrem qualquer impacto nos resultados de desempenho.

Recomendamos que você consulte estes artigos:  
<Anchor target="_blank" href="/partners/pt/docs/protect360-for-integrated-partners#limitação-de-impressões">Limitação de impressões e cliques</Anchor>  
<Anchor target="_blank" href="/partners/pt/docs/protect360-for-integrated-partners#faq">Perguntas frequentes sobre limitação</Anchor>

</Accordion>

<div id="the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate" />

<Accordion title="Porque é as instalações são bloqueadas devido ao flooding de cliques, mas a taxa de conversão é elevada?">

Os nossos algoritmos de inundação de cliques são executados em vários intervalos ao longo do dia e, sempre que o limite é ultrapassado, com base em parâmetros e lógica internos, os compromissos de anúncios do publisher não são elegíveis para atribuição.

**Por favor, observe que:** Alguns dos nossos algoritmos do flooding de cliques funcionam entre apps, o que implica que as anomalias provenientes de fontes fraudulentas idênticas também seriam reconhecidas para outros aplicativos anunciados.

Recomendamos a leitura de: <Anchor target="_blank" href="https://www.appsflyer.com/glossary/click-flooding/">O que é o flooding de cliques?</Anchor>

</Accordion>

<div id="installin-app-event-level-anomalies" />

## Anomalias no nível da instalação/evento in-app

<div id="why-was-my-test-install-rejected-from-attribution" />

<Accordion title="Por que a minha instalação de teste foi rejeitada da atribuição?">

A deteção antifraude da AppsFlyer aplica diferentes metodologias em várias camadas de proteção, como instalações únicas e clusters de instalação. Os clusters estão sendo analisados em várias agregações: por publisher, fonte de media, aplicativo, etc. Os clusters estão sendo analisados em várias agregações: por publisher, fonte de media, aplicativo, etc. A atividade fraudulenta é examinada usando vários algoritmos estatísticos e algoritmos de machine learning que consideram cada cluster como um todo. Assim, se um cluster for considerado fraudulento com elevada significância estatística, todas as instalações nesse cluster são consideradas fraudulentas. É uma tática bem conhecida dos autores de fraudes misturar algumas instalações legítimas com grandes volumes de atividade fraudulenta, na esperança de que a fraude seja suficientemente "diluída" para evitar o acionamento de mecanismos de bloqueio.

Por predefinição, todas as instalações recebidas são consideradas como tráfego LIVE - por isso, para garantir que a sua instalação de teste não seja categorizada nos algoritmos do Protect360, você deve seguir as etapas mencionadas neste <Anchor target="_blank" href="/marketers/pt/docs/registering-test-devices">artigo</Anchor> para registrar o seu dispositivo como um dispositivo de teste antes de realizar um teste.

</Accordion>

<div id="What-detection-methods-are-used-to-detect-install-rejections" />

<Accordion title="Que métodos de deteção são usados para detetar rejeições de instalações?">

Para maior clareza, é favor rever o "motivo secundário da fraude" associado à rejeição. Estes dados também estão disponíveis nos relatórios do Protect360 e no dashboard do Protect360, sujeitos ao acesso concedido pelo respetivo anunciante.

Recomendamos a leitura dos <Anchor target="_blank" href="/marketers/pt/docs/protect360-raw-data-reports#razões-para-bloqueio">motivos de bloqueio do Protect360</Anchor>.

</Accordion>

<div id="protect360-data-visibility-and-comprehension" />

## Visibilidade e compreensão dos dados do Protect360

<div id="how-do-i-gain-visibility-into-the-protect360-results" />

<Accordion title="Como é que posso ter visibilidade dos resultados do Protect360?">

Pode ver os resultados dos nossos esforços de deteção através do dashboard do Protect360 e dos relatórios de dados brutos, sujeitos ao acesso concedido pelo respectivo anunciante.

Recomendamos que você consulte estes artigos:  
<Anchor target="_blank" href="/marketers/pt/docs/protect360-dashboard">Painel do Protect360</Anchor>  
<Anchor target="_blank" href="/marketers/pt/docs/protect360-raw-data-reports#obtenção-de-relatórios-de-dados-brutos">Dados brutos do Protect360</Anchor>

</Accordion>

<div id="how-can-i-get-notified-in-realtime-about-blocked-traffic" />

<Accordion title="Como posso ser notificado em tempo real sobre o tráfego bloqueado?">

A AppsFlyer fornece postbacks de atribuição rejeitados para ad networks para cada instalação que o Protect360 rejeita da atribuição.

Você pode ativar o "postback rejeitado" anexando parâmetros de "postback rejeitado" ao seu template de postback usando o <Anchor target="_blank" href="/partners/pt/docs/self-serve-integration-management-for-ad-networks">Gerenciamento de integração</Anchor>.

</Accordion>

<div id="why-do-i-see-spikes-in-postattribution-detections" />

<Accordion title="Por que vejo picos nas detecções pós-atribuição?">

A deteção em tempo real antes da atribuição e a deteção pós-atribuição pertencem ao mecanismo de deteção de anomalias Protect360 da AppsFlyer, que se aplica em diferentes dimensões temporais.

Em comparação com a deteção em tempo real, a deteção pós-atribuição baseia-se mais nos indicadores de dados recolhidos após a instalação, durante a qual, se forem observadas anomalias, o Protect360 registará as atividades anómalas e irá apresentá-las na categoria pós-atribuição.

Considerando o que foi mencionado acima, certos métodos de deteção (timestamp\_anomalies, behavioral\_anomalies, etc.) são mais susceptíveis de serem detectados na fase de pós-atribuição do que em tempo real, uma vez que os dados são inconclusivos ao nível de uma instalação individual, mas ganham significado quando examinados quanto à sua distribuição na análise estatística.

Saiba mais sobre a <Anchor target="_blank" href="/marketers/pt/docs/protect360-anti-fraud-guide#postattribution-detection">deteção pós-atribuição</Anchor>.

</Accordion>

<div data-zendesk-anchors="click-impression-level-anomalies=anomalias-ao-n%C3%ADvel-do-cliqueimpress%C3%A3o 01H8GKS08Y22PX2SBTW5ME02C4=anomalias-ao-n%C3%ADvel-do-cliqueimpress%C3%A3o 01H8GKS08YXVK4CPNW9TX9XBYN=why-are-impressionsclicks-being-capped 01H8GKS08ZGNTMNZ5JH846T9Q9=the-attribution-of-installs-is-being-blocked-due-to-click-flooding-click-spamming-but-i-see-a-good-conversion-rate install-inapp-event-level-anomalies=anomalias-no-n%C3%ADvel-da-instala%C3%A7%C3%A3oevento-in-app 01H8GKS08ZRA7YT9FWJNBBSV4Q=anomalias-no-n%C3%ADvel-da-instala%C3%A7%C3%A3oevento-in-app 01H8GKS08Z2M0RTMR4GM1BJE7G=why-was-my-test-install-rejected-from-attribution What-detection-methods-are-used-to-detect-install-rejections%3F=What-detection-methods-are-used-to-detect-install-rejections 01H8H30KARRPAPT9XRREDYKHVT=What-detection-methods-are-used-to-detect-install-rejections protect360-data-visibility-and-understanding=visibilidade-e-compreens%C3%A3o-dos-dados-do-protect360 01H8GKS08ZX2W1G0K165H96N4Z=visibilidade-e-compreens%C3%A3o-dos-dados-do-protect360 01H8GKS08ZGEEK0HQVCRD546MW=how-do-i-gain-visibility-into-the-protect360-results 01H8GKS08ZC6SB4PT53JG5QKHG=how-can-i-get-notified-in-realtime-about-blocked-traffic 01H8GKS08Z673WG6C6JGW31F42=why-do-i-see-spikes-in-postattribution-detections" />
