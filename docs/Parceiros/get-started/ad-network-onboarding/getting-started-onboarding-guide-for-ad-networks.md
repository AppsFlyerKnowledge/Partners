---
title: Primeiros passos - guia de integração para redes de publicidade
metadata:
  keywords:
    - Ad Network
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - Mobile Attribution
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-ravid-naori
    - Marketers
    - Mobile Attribution
    - Ad Networks
  created_at: '2019-03-28T08:41:59Z'
  edited_at: '2026-08-18T00:39:57Z'
  id: 360001300998
  locale: pt
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/pt/articles/360001300998
---
> **Visão geral:** Conclua a integração com a AppsFlyer configurando e testando o seu link de atribuição e as integrações de postback. Entenda as etapas, prazos e dependências do processo.

<Image align="center" alt="AdNetworks_-_Onboarding__2_.png" src="https://files.readme.io/33217648d1f5c1ef327871b9b2ccfaadb6b9ae34fb2645ffcfbe187c378dd054-30603793569297.png" />

<div id="what-is-appsflyer" />

## O que é a AppsFlyer?

A AppsFlyer, líder em atribuição móvel, dá-lhe as boas-vindas como nosso parceiro integrado de rede publicitária. Este artigo destina-se às redes de publicidade que já concluíram o registo como parceiro na AppsFlyer. Se deseja registar-se como parceiro, deve solicitar a um <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#convide-novos-parceiros-para-a-appsflyer">cliente (anunciante) da AppsFlyer que o convide.</Anchor>

<div id="ad-network-onboarding" />

## Integração de redes de publicidade

As etapas necessárias para a integração e o tempo estimado para completá-las estão listados na secção **Etapas de integração** deste artigo.

A integração implica que:

* A AppsFlyer regista as suas interações (cliques e impressões). As interações são atribuídas de acordo com o <Anchor target="_blank" href="/marketers/pt/docs/appsflyer-attribution-model">modelo de atribuição da AppsFlyer</Anchor>.
* Os postbacks no formato que necessita são enviados para os seus endpoints.
* Pode aceder a funcionalidades da AppsFlyer como a assinatura de cliques, Protect360, Data Locker, entre outras.

<div id="if-you-need-help" />

<Accordion title="Se precisar de ajuda">

* Consulte as <Anchor target="_blank" href="/partners/pt/docs/integrated-partners-faq">Perguntas Frequentes</Anchor> do parceiro
* Consulte o artigo <Anchor target="_blank" href="/partners/pt/docs/integration-requests-for-partners">Pedidos de alteração de integração</Anchor>

</Accordion>

Considere:

* As estimativas de tempo neste artigo são baseadas na nossa experiência com redes de publicidade. Cada integração é ligeiramente diferente, por isso os tempos reais podem variar.
* A AppsFlyer suporta várias <Anchor target="_blank" href="/partners/pt/docs/platforms-for-ad-networks">plataformas de desempenho</Anchor>. Se utiliza uma das plataformas listadas, deve rever as instruções específicas antes da integração.

<div id="onboarding-steps" />

## Etapas de integração

**Para integrar com a AppsFlyer**:

1. [Conclua a parte 1 - integração e testes.](/docs/getting-started-onboarding-guide-for-ad-networks#parte-1-integração-e-testes)
2. [Conclua a parte 2 - testes com aplicações de anunciantes.](/docs/getting-started-onboarding-guide-for-ad-networks#parte-2-teste-usando-aplicações-de-anunciantes)
3. [Conclua a parte 3 - utilize o painel de controlo e as ferramentas de relatórios da AppsFlyer.](/docs/getting-started-onboarding-guide-for-ad-networks#parte-3-painel-da-appsflyer-e-opções-de-relatórios)

<div id="part-1-integration-and-testing" />

### Parte 1: Integração e testes

<table><thead><tr><th>Ação</th><th>Minutos necessários</th></tr></thead><tbody><tr><td>Aguarde o e-mail de aprovação do registo que o convidará a completar as etapas obrigatórias de integração.</td><td>--</td></tr><tr><td colspan="2"> <strong>Etapas obrigatórias de integração</strong> </td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#link-de-atribuição" target="_blank">Especifique o seu link de atribuição</a>: Os links de atribuição são URLs com macros. Estas macros são preenchidas por si com valores reais e enviadas para a AppsFlyer sempre que um utilizador clica num link. <br/>Atenção! Se utilizar uma plataforma de rede de desempenho suportada pela AppsFlyer, considere as instruções específicas fornecidas para cada plataforma. Consulte os <a href="./platforms-for-ad-networks" target="_blank">Guias de redes de desempenho.</a> </td><td>60</td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#postback-padrão" target="_blank">Especifique as macros de postback</a>: Os postbacks são URLs com macros preenchidas pela AppsFlyer e enviadas para os seus servidores em tempo real após cada conversão.</td><td>60</td></tr><tr><td>Aceda ao <a href="https://hq1.appsflyer.com/auth/login" target="_blank">dashboard da AppsFlyer</a> utilizando as credenciais fornecidas. </td><td> </td></tr><tr><td><p>Carregue o logótipo da sua empresa. O logótipo deve ser um PNG transparente com o formato 200 X 50. </p><ol><li>Na AppsFlyer, na barra de menus, selecione o seu endereço de e-mail &gt; <strong>Configuração de Parceiro</strong>. </li><li>No separador <strong>Perfil</strong>, carregue o logótipo da sua empresa. </li><li>Clique em <strong>Guardar</strong>.</li></ol></td><td>5</td></tr><tr><td><p>Teste a integração utilizando as aplicações de teste da AppsFlyer:</p><ul><li><a href="./android-integration-testing-for-ad-networks" target="_blank">com o Android</a></li><li><a href="./ios-integration-testing-for-ad-networks" target="_blank">/docs/ctv-pc-and-console-platform-attribution-concepts</a></li></ul></td><td>10</td></tr><tr><td colspan="2"><strong>Passos opcionais de integração</strong></td></tr><tr><td>[iOS] Se os seus anunciantes exigirem Privacidade Avançada Agregada da AppsFlyer, finalize a integração de <a href="./self-serve-integration-management-for-ad-networks#privacidade-avançada-e-postbacks-skan" target="_blank">Privacidade Avançada</a>.</td><td>60</td></tr><tr><td>[iOS] Se conduzir campanhas SKAdNetwork, complete a <a href="./self-serve-integration-management-for-ad-networks#privacidade-avançada-e-postbacks-skan" target="_blank">integração SKAdNetwork.</a> </td><td>60</td></tr><tr><td><h4><strong><span id="authorized-agencies"></span>Agências autorizadas</strong></h4><p>Crie e gerencie uma lista de agências aprovadas para executar campanhas através da integração de sua rede. Faça isto inserindo o ID da agência (af_prt) na seção <a href="./set-up-your-list-of-authorized-agencies" target="_blank"><strong>Agências autorizadas</strong></a>  do Centro de Segurança. Para obter o ID da agência, a agência deve contatar você e fornecê-lo.</p></td><td>2</td></tr><tr><td colspan="2"><p><strong>Funcionalidades opcionais e considerações</strong><br/> </p><p>Considere implementar integrações e opções baseadas nos requisitos dos anunciantes.</p></td></tr><tr><td>Para garantir que cliques fraudulentos não sejam enviados com o identificador do seu parceiro, implemente a <a href="./click-signing-for-ad-networks" target="_blank">assinatura de cliques.</a> </td><td>60+</td></tr><tr><td>Para anunciantes que implementam Protect360 ou regras de validação, adicione <a href="./postback-macros-for-ad-networks#macrosinstalações-eventos-in-app-e-eventos-rejeitados" target="_blank">postbacks de atribuição rejeitados</a>.</td><td>15</td></tr><tr><td>Envie o custo para a AppsFlyer via API. Veja a <a href="./incost-api-for-ad-networks" target="_blank">API InCost</a>.</td><td>60+</td></tr><tr><td> <a href="/marketers/pt/docs/retargeting-attribution-guide" target="_blank">Integração de redirecionamento</a>.</td><td>15</td></tr><tr><td> <a href="/marketers/pt/docs/measure-view-through-engagements" target="_blank">Integração de atribuição por visualização</a>.</td><td>15</td></tr></tbody></table>

<div id="part-2-test-using-advertiser-apps" />

### Parte 2: Teste usando aplicações de anunciantes

Nesta etapa, irá testar a sua integração utilizando uma aplicação que pertence a um anunciante. Assim, é necessário que contacte o anunciante e peça que complete alguns dos passos desta seção. Nesta seção, referências aos anunciantes também podem referir-se a agências, caso atuem em nome de um anunciante.

| Executado por | Ação | Minutos necessários |
| --- | --- | --- |
| AppsFlyer | Ligue <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#integration-tab">ativar parceiro.</Anchor><br /><br />Quando ligado, a AppsFlyer considera os envolvimentos trazidos por si como candidatos à atribuição. | 2 |
| Anunciantes | Conceda <Anchor target="_blank" href="/marketers/pt/docs/set-up-an-integrated-partner#permissões-da-ad-network">permissões à rede de publicidade*</Anchor> e adicione os seus membros de equipa.<br /><br />Quando ligado, os dados de desempenho da aplicação ficam visíveis no painel da AppsFlyer. Apenas os membros da equipa listados têm acesso aos dados. | 2 |
| Rede de anúncios | <Anchor target="_blank" href="/marketers/pt/docs/user-management#creating-users">Adicione os membros da equipa à sua conta</Anchor>. | 2 |
| Anunciante (administrador) | <Anchor target="_blank" href="/marketers/pt/docs/registering-test-devices">Registe os seus dispositivos de teste</Anchor>. Solicite ao anunciante que o faça em seu nome. | 3 |
| Redes de anúncios | <Anchor target="_blank" href="/partners/pt/docs/test-marketer-campaign-integration-with-the-ad-network">Teste a integração utilizando aplicações dos anunciantes.</Anchor> | 60 |

<div id="part-3-appsflyer-dashboard-and-reporting-options" />

### Parte 3: Painel da AppsFlyer e opções de relatórios

| Opção |
| --- |
| <Anchor target="_blank" href="/partners/pt/docs/integrated-partners-dashboard">Utilize o painel do parceiro</Anchor>. |
| Obtenha dados de desempenho agregados através do armazenamento em nuvem com o <Anchor target="_blank" href="/partners/pt/docs/data-locker-for-partners">Data Locker</Anchor> para redes de anúncios. |
| Obtenha os dados brutos do Protect360<Anchor target="_blank" href="/marketers/pt/docs/raw-data-export-page">.</Anchor> |

<div id="integration-validation-period" />

## Período de validação da integração

Para garantir a integridade do ecossistema da AppsFlyer e proteger os sistemas internos do tráfego inválido, todas as novas integrações de redes de anúncios passam por um período de validação. Durante este tempo, a AppsFlyer verifica detalhadamente o tráfego e a sua qualidade antes de tornar a integração disponível a outros anunciantes no <Anchor target="_blank" href="/marketers/pt/docs/partner-integrations">Marketplace</Anchor>. As integrações de redes de anúncios que não satisfazem os critérios de qualidade de tráfego após a validação podem resultar no encerramento da conta.

<div id="validation-periodfaq" />

### Período de validação — FAQ

| **Pergunta** | **Resposta** |
| --- | --- |
| <span id="why-cant-advertisers-find-me-on-the-marketplace"></span>Porque é que os anunciantes não conseguem encontrar-me no Marketplace, mesmo depois de eu ter concluído a integração? | No período de validação, a sua integração é visível apenas para o anunciante que o referenciou. Após validarmos a qualidade do seu tráfego, receberá um email a informar que a sua integração está acessível a todos os anunciantes. |
| <span id="what-should-i-do-to-make-the-integration-available-for-all-advertiers"></span>O que posso fazer para garantir que a minha integração será aprovada? | Forneça um volume significativo de tráfego de alta qualidade ao anunciante que o recomendou. |
| <span id="when-should-i-expect-to-receive-the-validation-completion-email"></span>Quando posso esperar receber o e-mail de conclusão da validação? | Após conseguirmos validar tráfego suficiente, receberá um e-mail a informar que o período de validação terminou. |
| <span id="can-i-know-the-current-status-of-the-validation-period"></span>Posso verificar o estado atual da minha avaliação de validação? | Só ficará a saber quando o período de validação terminar, após receber a notificação por e-mail. |
| <span id="what-are-the-validation-criteria-based-on"></span>Quais são os critérios de validação baseados? | Os critérios de validação têm por base algoritmos de aprendizagem automática dinâmica do <Anchor target="_blank" href="/marketers/pt/docs/protect360-anti-fraud-guide">Protect360</Anchor>. São considerados fatores como a qualidade do tráfego, o volume e a validade global dos dados, em conjunto com as melhores práticas do setor. |
| <span id="another-adviertiser-wants-to-work-with-me"></span>E se outro anunciante quiser iniciar colaboração comigo durante o período de validação? | Durante o período de validação, a sua integração será visível apenas para o anunciante que o indicou. Outros anunciantes poderão trabalhar consigo depois do seu período de validação terminar com êxito. |
| <span id="my-integration-fails"></span>O que acontece se a minha integração não passar na validação? | O período de validação pode ser estendido para monitorizar melhorias na qualidade do tráfego ou a sua integração pode ser removida permanentemente da plataforma AppsFlyer. Será notificado em qualquer dos casos. |

<div data-zendesk-anchors="what-is-appsflyer=o-que-%C3%A9-a-appsflyer h_01J09255QNBFRV8DYZPGG990A0=o-que-%C3%A9-a-appsflyer ad-network-onboarding=integra%C3%A7%C3%A3o-de-redes-de-publicidade h_01J09255QN61VPW292PC2CH9KN=integra%C3%A7%C3%A3o-de-redes-de-publicidade h_01J09255QNGD66T140ERW4WP8Z=if-you-need-help onboarding-steps=etapas-de-integra%C3%A7%C3%A3o h_01J09255QNZ9QXXFB54YRYCM8P=etapas-de-integra%C3%A7%C3%A3o part-1-integration-and-testing=parte-1-integra%C3%A7%C3%A3o-e-testes h_01J09255QN35ZBKE2R2HDDZWSZ=parte-1-integra%C3%A7%C3%A3o-e-testes h_01J0JS136CTYEF6F29H8R1NV29=authorized-agencies part-2-test-using-advertiser-apps=parte-2-teste-usando-aplica%C3%A7%C3%B5es-de-anunciantes h_01J09255QP11XJD3C83VZZXXQZ=parte-2-teste-usando-aplica%C3%A7%C3%B5es-de-anunciantes part-3-appsflyer-dashboard-and-reporting-options=parte-3-painel-da-appsflyer-e-op%C3%A7%C3%B5es-de-relat%C3%B3rios h_01J09255QPSSD8CF0HR059RWXZ=parte-3-painel-da-appsflyer-e-op%C3%A7%C3%B5es-de-relat%C3%B3rios integration-validation-period=per%C3%ADodo-de-valida%C3%A7%C3%A3o-da-integra%C3%A7%C3%A3o h_01J09255QP82ZYZDJMA74SRYGZ=per%C3%ADodo-de-valida%C3%A7%C3%A3o-da-integra%C3%A7%C3%A3o validation-period%E2%80%94faq=per%C3%ADodo-de-valida%C3%A7%C3%A3o--faq h_01J09255QP77BME57P9B7S222V=per%C3%ADodo-de-valida%C3%A7%C3%A3o--faq" />
