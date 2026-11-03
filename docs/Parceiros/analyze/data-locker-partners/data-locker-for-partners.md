---
title: Data Locker para parceiros
metadata:
  keywords:
    - Agencies
    - Ad Networks
    - Partners
    - Data Locker
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-rona-einat
    - Data Locker
    - Agencies
    - Ad Networks
  created_at: '2021-05-28T15:37:04Z'
  edited_at: '2026-08-18T00:38:04Z'
  id: 360020818517
  locale: pt
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/pt/articles/360020818517
---
> **Resumo:** o Data Locker para parceiros (ad networks e agências) fornece dados de aplicativos para o armazenamento do parceiro na AWS, GCS ou BigQuery.

![6133DataLockerForPartners.png](https://files.readme.io/f6cad12250fe07cf2b0a12b64eeaa597c83527b4b4e09aea11cc2a52ab53339b-4637680455313.png)

## Data Locker para parceiros

O Data Locker para parceiros envia dados de aplicativos para o armazenamento em nuvem. Os anunciantes definem permissões que fazem com que a AppsFlyer possa compartilhar dados selecionados com um determinado parceiro.

<div id="data-locker-features" />

<Accordion title="Recursos do Data Locker">

| Funcionalidade | Descrição |
| --- | --- |
| Opções de armazenamento (nuvem) | Armazenamento (bucket) de sua propriedade em:<ul><li>AWS</li><li>GCS</li><li>Yandex</li><li>BigQuery</li></ul><Anchor target="_blank" href="/marketers/pt/docs/data-locker-for-marketers#storage-options">Sobre opções de armazenamento</Anchor> |
| Suporte para vários aplicativos | Compatível com dados de aplicativos que são integrados com você. O anunciante deve permitir que você acesse cada relatório para que você obtenha os dados. |
| Opções de formato | <ul><li>Para armazenamento em bucket na nuvem:<ul><li>CSV</li><li>PARQUET</li><li>Adobe</li></ul></li><li>Data warehouse</li></ul> |
| Atualização dos dados | A atualização depende do tipo de relatório:<ul><li>**Por hora:** Dados gerados continuamente</li><li>**Diária:** alguns relatórios são preparados diariamente e ficam prontos no dia seguinte</li></ul> |

</Accordion>

<div id="reports-available-for-partners" />

<Accordion title="Relatórios disponíveis para parceiros">

Os relatórios disponíveis e as permissões necessárias para obter os relatórios são diferentes para cada tipo de parceiro. No entanto, o mecanismo do Data Locker, as opções de armazenamento e as configurações necessárias são as mesmas, independentemente do tipo de parceiro. Consulte os artigos por tipo de parceiro abaixo:

* <Anchor target="_blank" href="/partners/pt/docs/data-locker-reports-available-for-ad-networks">Redes de anúncios</Anchor>
* <Anchor target="_blank" href="/partners/pt/docs/data-locker-reports-for-agencies">Agências</Anchor>
* <Anchor target="_blank" href="/partners/pt/docs/data-locker-reports-for-api-partners">Parceiros de marketing</Anchor>

</Accordion>

## Arquitetura de armazenamento de dados

<div id="overview" />

<Accordion title="Visão geral">

Os dados são registrados na opção de armazenamento selecionada por você. Você pode alternar de uma opção para outra a qualquer momento. A mudança ocorre em poucas horas.

Os dados no armazenamento em bucket na nuvem são organizados em uma estrutura de pastas hierárquica, de acordo com o tipo de relatório, data e hora. A figura a seguir contém um exemplo dessa estrutura:

![DLFolderOVerview.png](https://files.readme.io/78f360ec1df72253e5b2cd725f3eecf4e17548a7f06b544a94a75a2c319d77a0-18107910420369.png)

Os dados de um determinado relatório estão contidos nas pastas de hora (h) associadas a esse relatório.

* O número de pastas de hora varia se o relatório é transmitido por hora ou por dia.
* Os dados são fornecidos em arquivos compactados Snappy ou GZIP, ou arquivos não compactados, com formato Parquet ou CSV.
* Os arquivos de dados consistem em colunas (campos).
* A estrutura da coluna é definida por tipo de relatório.

</Accordion>

<div id="folder-structure" />

<Accordion title="Estrutura de pastas">

| Pasta | Descrição |
| --- | --- |
| data-locker-hourly | ![DLHourly.png](https://files.readme.io/c257b82d22622d97808a6c23603ac4eee9f2ab091bcb68a33637ac4fb749fdff-18107874510353.png)<ul><li>A pasta de nível superior no bucket depende do provedor do armazenamento.</li><li>A pasta *data-locker-hourly* contém os tópicos do relatório.</li></ul>**Exemplos de estrutura de pastas com base no proprietário do bucket e no provedor de nuvem**:<ul><li>**Seu repositório AWS**: *&lt;af-datalocker-your bucket prefix>/&lt;generated-home-folder>&lt;subscription-id>*</li><li>**Seu repositório GCS:** &lt;your bucket name>/&lt;generated-home-folder>/&lt;subscription-id></li></ul> |
| t (tópico) | O tipo de relatório está relacionado ao assunto do relatório. |
| dt (date) | Essa é a data dos dados relacionados. Na maioria dos casos, isso significa a data em que o evento ocorreu. |
| h (hora) | As pastas h estão relacionadas ao horário em que a AppsFlyer recebeu os dados. Por exemplo, eventos de instalação recebidos entre 14:00-15:00 UTC são transmitidos para o arquivo h=14. Atenção! Há um atraso, de cerca de 6 horas, entre o momento em que os dados chegam à AppsFlyer até o momento em que a pasta h é transmitida para o Data Locker. Por exemplo, a pasta h=14 é transmitida seis horas depois, às 23:00 UTC.<br /><br />**Características da pasta**:<ul><li>Existem 24 pastas h enumeradas de 0 a 23. Por exemplo, h=0, h=1 e assim por diante.</li><li>Além disso, a pasta "late" contém eventos do dia anterior que chegaram depois da meia-noite (em outras palavras, eventos que chegam entre 00:00 - 02:00 UTC do dia seguinte). Por exemplo, se um usuário instalar um aplicativo na segunda-feira às 08:00 e o evento chegar na terça-feira às 01:00, o evento será registrado na pasta "late" de segunda-feira.</li><li>Os dados que chegam depois das 02:00 UTC são gravados na pasta da data e hora reais de chegada.</li><li>Você deve usar os dados na pasta "late". Eles não estão contidos em nenhuma outra pasta.</li><li>Pasta \_temporary: Em alguns casos, geramos uma pasta temporária (temporary) dentro de uma pasta h. Desconsidere pastas e subpastas temporárias. Exemplo: /t=impressions/dt=2021-04-11/h=18/**\_temporary**.</li></ul> |
| Dados unificados | Os dados de todos os aplicativos são fornecidos em arquivos de dados unificados. Ao carregar os dados, use o campo app\_id no nível da linha para distinguir entre aplicativos.<br /><br />**Exemplo de arquivos de dados estão na pasta h=2**<br /><br />![UnifiedByApp.png](https://files.readme.io/dbc39c2ce99c1ff607fd553b9c9034e55728c102f31fd18a501cc00910267b28-18107874522513.png)<ul><li>No processo de carregamento dos dados, certifique-se do seguinte:<ul><li>Você começa a consumir dados somente após a flag \_SUCCESS ser configurada.</li><li>Você carrega todos os arquivos com uma extensão *.gz*</li></ul></li></ul> |
| Flag de conclusão | O último sinalizador de arquivo (conclusão) é definido quando todos os dados de uma determinada pasta h tiverem sido gravados.<ul><li>Não leia dados em uma pasta antes de verificar se a flag \_SUCCESS existe.</li><li>A flag \_SUCCESS é definida mesmo em casos onde nenhum dado é escrito na pasta. Isso significa que a pasta está vazia.</li></ul> |
| Compactar | Os arquivos são compactados usando o GZ. Depois de descompactar:<ul><li>Os arquivos não têm extensão.</li><li>Cada arquivo tem uma linha de cabeçalho contendo os nomes da coluna (campo).</li></ul> |
| Sequência de coluna | A sequência de campos nos relatórios é sempre a mesma. Novos campos são adicionados à direita dos campos existentes.<br /><br />As definições de coluna (campo) são definidas por relatório. Verifique o artigo do relatório relevante para a descrição. |
| Considerações sobre o preenchimento de campos | **Campos em branco ou vazios:** Alguns campos são preenchidos com *null* ou estão vazios. Isso significa que, no contexto de um certo relatório, não há dados a reportar. Em geral, *null* significa que esse campo não é preenchido no contexto de um determinado relatório e tipo de aplicativo. Em branco "" significa que o campo é relevante em seu contexto, mas nenhum dado foi encontrado para preenchê-lo.<br /><br />**Fuso horário e moeda**:<br /><br />As configurações de fuso horário e moeda específicas do aplicativo não afetam os dados gravados no Data Locker. Tais como:<ul><li>**Fuso horário**: As datas e horas estão em UTC.</li><li>**Moeda**: o campo event\_revenue\_usd fica em USD.</li></ul>**Valores com vírgulas:** As vírgulas estão contidas entre aspas duplas ", por exemplo,`` `"iPhone6,1"` ``. |

</Accordion>

<div id="data-files" />

<Accordion title="Arquivos de dados">

Os arquivos de dados dependem do tipo de segregação.

<table><thead><tr><th>Conteúdo</th><th colspan="2">Detalhes</th></tr></thead><tbody><tr><td>Flag de conclusão</td><td colspan="2"><p>A última flag de arquivo (conclusão) é definida quando todos os dados de uma determinada pasta h tiverem sido gravados. </p><ul><li><p>Não leia dados em uma pasta antes de verificar se a flag _SUCCESS existe.</p></li><li><p>A flag _SUCCESS é definida mesmo nos casos em que não há dados para gravar em uma determinada pasta e a pasta está vazia. </p></li><li>Atenção! Na opção segregação por aplicativo, a flag é definida na pasta h e não nas pastas individuais do aplicativo. Consulte as figuras na seção anterior. </li></ul></td></tr><tr><td>Tipos de arquivo</td><td colspan="2"><ul><li>Os dados são fornecidos em arquivos compactados Snappy ou GZIP, ou arquivos não compactados, com formato Parquet ou CSV.</li><li>Depois de descompactar, os arquivos de dados estarão no formato Parquet ou CSV de acordo com suas configurações.</li></ul></td></tr><tr><td>Sequência de colunas (arquivos CSV) </td><td colspan="2"><p>No caso de arquivos CSV, a sequência de campos nos relatórios é sempre a mesma. Quando adicionamos novos campos, eles são adicionados à direita dos campos existentes. </p><p>Sobre isso: </p><ul><li>A estrutura de colunas dos relatórios de jornada do usuário é idêntica. Isso significa que você pode ter procedimentos de carregamento de dados semelhantes para diferentes tipos de relatório. Você seleciona os campos contidos nos relatórios. O significado do campo é detalhado no <a href="/marketers/pt/docs/raw-data-field-dictionary" target="_blank">dicionário de dados brutos</a>. </li><li>Os relatórios que têm uma indicação de FF na seção de disponibilidade do relatório não aderem à estrutura de coluna comum. </li></ul></td></tr><tr><td>Considerações sobre o preenchimento de campos</td><td colspan="2"><p><strong>Campos em branco ou vazios:</strong> Alguns campos são preenchidos com <em>null</em> ou estão vazios. Isso significa que, no contexto de um certo relatório, não há dados a reportar. Em geral, <em>null</em> significa que esse campo não é preenchido no contexto de um determinado relatório e tipo de aplicativo. Em branco "" significa que o campo é relevante em seu contexto, mas nenhum dado foi encontrado para preenchê-lo. </p><p>No caso da fonte de mídia restrita, o conteúdo dos campos restritos é definido como null. </p><p>No geral, considere null e em branco como a mesma coisa. Não há dados disponíveis. </p><p><strong>Fuso horário e moeda</strong></p><p>As configurações de fuso horário e moeda específicas do aplicativo não afetam os dados gravados no Data Locker. O seguinte se aplica: </p><ul><li> <strong>Fuso horário</strong>: As datas e horas estão em UTC.</li><li> <strong>Moeda</strong>: o campo event_revenue_usd fica em USD.</li></ul><p><strong>Valores com vírgulas:</strong> As vírgulas estão contidas entre aspas duplas ", por exemplo,<code>`"iPhone6,1"`</code>.</p></td></tr></tbody></table>

</Accordion>

<div id="storage-options" />

<Accordion title="Opções de armazenamento">

* Os dados são registrados em um proprietário de armazenamento de sua escolha da seguinte forma: AWS, GCS e BigQuery.
* Você pode alterar a seleção de armazenamento a qualquer momento.
* Se você alterar o armazenamento, acontecerá o seguinte:
  * Começamos a registrar no armazenamento recém-selecionado dentro de uma hora.
  * Continuamos registrando no armazenamento existente durante um período de transição de 7 dias. O tempo de expiração do período de transição é exibido na interface do usuário. Use o período de transição para atualizar seus processos de carregamento de dados.
  * **Alterar buckets**: se você alterar o armazenamento, os dados serão enviados para ambos por um período de transição de 7 dias, permitindo que você alinhe o processo de consumo de dados.

|  | Partner-owned storage (GCS, AWS, BigQuery) |
| --- | --- |
| Nome do bucket | <ul><li>GCS: Sem restrição</li><li>AWS: Definido por você. Deve ter o prefixo af-.</li></ul>Exemplo: `af-datalocker-your-bucket-name` |
| Proprietário do armazenamento | Parceiro |
| Plataforma de armazenamento | AWS, GCS, Yandex, BigQuery |
| Credenciais para acessar dados por você | Não conhecido pela AppsFlyer. Use credenciais fornecidas pelo provedor de armazenamento. |
| Retenção de dados | Controlado por você |
| Segurança | Você controla o armazenamento.<ul><li>**AWS**: AppsFlyer requer a permissão getObject, ListBucket, DeleteObject, PutObject para o bucket. O bucket deve ser dedicado ao uso da AppsFlyer. Não o use para outros fins.</li><li><Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor></li></ul> |

#### **Aviso aos agentes de segurança**

Considere:

* O bucket ou destino é para uso exclusivo da AppsFlyer. Nenhuma outra entidade pode fazer registros no bucket.
* Você pode excluir dados no bucket cerca de 25 horas após gravarmos os dados.
* Os dados que gravamos no destino são uma cópia dos dados que já estão em nossos servidores. Os dados continuam em nossos servidores de acordo com nossa política de retenção.
* Por razões técnicas, às vezes deletamos e reescrevemos os dados. Por isso, temos permissões de excluir e listar. Isso não implica em um risco de segurança para você. No caso da lista, somos a única entidade que escreve no bucket. No caso de exclusão, podemos gerar os dados novamente.

</Accordion>

<div id="multipleconnection-principles-more-than-one-destination" />

<Accordion title="Princípios de conexões múltiplas (mais de um destino)">

No Data Locker você pode enviar alguns ou todos os seus dados para mais de um destino (definido nas configurações de conexão). Por exemplo, você pode enviar dados do App A para AWS, e dados do App B para GCS.

Cada conexão consiste em um conjunto completo de configurações do Data Locker, incluindo um destino. As configurações de conexão são independentes umas das outras.

Ao administrar suas conexões, considere:

* Nas configurações do Data Locker, as conexões são mostradas em abas. Cada conexão tem sua própria aba de configurações a partir da qual você pode gerenciar a conexão. A aba padrão é "Data Locker".
* Para criar uma nova conexão:
  1. Clique em **Adicionar conexão**.
  2. Forneça um nome para a conexão e escolha o tipo de armazenamento.
  3. Clique em **Salvar**.  
     Uma vez salva, a conexão é exibida ao lado da aba padrão "Data Locker". O ícone de cada aba representa o tipo de armazenamento.
* Para ver os detalhes da conexão, duplicar uma conexão, ou excluir uma conexão, clique em ⋮ (opções).

</Accordion>

## Procedimentos

<div id="set-up-data-locker" />

<Accordion title="Configure o Data Locker">

Use este procedimento para configurar o Data Locker. As alterações nas configurações entram em vigor dentro de 3 horas.

**Pré-requisito:**

Complete um ou mais dos seguintes procedimentos de armazenamento:

* Bucket da <Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor>
* Bucket do <Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor>
* [Beta] Bucket dp <Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#yandex">Yandex</Anchor>
* Data warehouse do <Anchor target="_blank" href="/marketers/pt/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor>

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png)  Para configurar o Data Locker:**

1. Faça login no <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">dashboard da AppsFlyer.</Anchor>
2. Vá para:
   * **Anunciantes:** No AppsFlyer, na barra lateral, abra **Exportar** > **Data Locker**.
   * **Parceiros de marketing**: Clique no botão **Menu da conta** > Data Locker.
3. Siga as etapas 3 a 16 das <Anchor target="_blank" href="/marketers/pt/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">instruções de configuração do Data Locker</Anchor>.

</Accordion>

## Informações adicionais

<div id="traits-and-limitations" />

<Accordion title="Características e limitações">

| **Caraterística** | Observações |
| --- | --- |
| Fuso horário específico do aplicativo | Não aplicável |
| Moeda específica da aplicação | Não suportado |
| Limitações de tamanho | Não aplicável |
| Atualização dos dados | Os dados são atualizados de acordo com a atualização específica dos dados do relatório, detalhada neste artigo. |
| Dados históricos | Não suportado |
| Acesso de membro da equipe | Os membros da equipe não podem configurar o Data Locker. |

</Accordion>

<div id="troubleshooting" />

<Accordion title="Resolução de problemas">

<Anchor target="_blank" href="/marketers/pt/docs/data-locker-for-marketers#troubleshooting">Use este guia de solução de problemas</Anchor>.

</Accordion>

<div data-zendesk-anchors="data-locker-for-partners=data-locker-para-parceiros h_01H8Y0DGS4Y2N99YNYEEJA6RSF=data-locker-para-parceiros h_01H8Y0DGS4EM06PYNS1DRMZM6Y=data-locker-features h_01H8Y0DGS4A0MYGVZ9XQ49EBT2=reports-available-for-partners data-storage-architecture=arquitetura-de-armazenamento-de-dados h_01H8Y0DGS4WTAJV7QE2DX3VGBP=arquitetura-de-armazenamento-de-dados h_01H8Y0DGS4BQHBKNHZ4CD9ZMT4=overview h_01H8Y0DGS43JAREX23YX1F125K=folder-structure h_01H8Y0DGS524WNXY63351XGJKA=data-files h_01H8Y0DGS5MV6J1MMJJS8G4HC4=storage-options notice-to-security-officers=aviso-aos-agentes-de-seguran%C3%A7a h_01H8Y0DGS5R4QX01WBK2S33QP5=aviso-aos-agentes-de-seguran%C3%A7a h_01H8Y0DGS56GN6TVTSEV713DWQ=multipleconnection-principles-more-than-one-destination procedures=procedimentos h_01H8Y0DGS5588GQPZT7MQ686T3=procedimentos h_01H8Y0DGS57YK2PZ9ENZ80EWRJ=set-up-data-locker additional-information=informa%C3%A7%C3%B5es-adicionais h_01H8Y0DGS5SYZRWFAXDSKE3YHX=informa%C3%A7%C3%B5es-adicionais h_01H8Y0DGS540HK8MSCFYT9Q1RM=traits-and-limitations h_01H8Y0DGS55PJ7HV1PQ72XDDAB=troubleshooting" />
