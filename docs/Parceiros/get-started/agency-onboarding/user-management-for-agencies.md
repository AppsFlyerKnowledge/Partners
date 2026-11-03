---
title: Gerenciamento de usuários para agências
metadata:
  keywords:
    - Agencies
    - Partners
    - Platform essentials
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-roy-negri
    - Platform essentials
    - Agencies
  created_at: '2021-12-19T11:18:09Z'
  edited_at: '2026-08-18T00:40:28Z'
  id: 4414231896337
  locale: pt
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/pt/articles/4414231896337
---
> **Visão geral:** crie e gerencie os usuários da conta da sua agência na AppsFlyer e atribua permissões para acessar recursos e aplicativos.

## Funções de usuário e permissões de acesso

As contas da AppsFlyer permitem vários usuários, cada um com permissões gerenciadas individualmente. As permissões de cada usuário são definidas com 2 dimensões principais:

* **Função** (capacidade de acessar recursos e executar funções)
* **Acesso ao aplicativo** para aplicativos atuais e futuros

As permissões dentro de cada uma dessas dimensões são atribuídas de forma independente. Ou seja, você pode atribuir uma **função** com amplos recursos funcionais a um usuário, mas permitir que ele exerça esses recursos apenas em um conjunto definido de **aplicativos.**

A única exceção é a [função de administrador](/docs/user-management-for-agencies#administrador--uma-função-especial), conforme discutido abaixo, que tem acesso a todos os recursos e aplicativos.

### Funções predefinidas

#### hash de funções predefinidas

Cada usuário da AppsFlyer de uma conta de agência recebe uma das 4 funções predefinidas:

* Administrador
* Gerente de equipe
* marketing
* Contribuinte

Cada uma dessas funções define os recursos específicos da AppsFlyer que o usuário pode acessar e as funções que ele pode executar. A lista completa desses recursos por função está disponível na [aba funções](/docs/user-management-for-agencies#aba-funções) da página de **gerenciamento de usuários**.

Como regra geral, todas as funções são predefinidas e as capacidades de cada função são fixas: não é permitido combiná-las. No entanto, você pode alterar os recursos funcionais de um usuário a qualquer momento alterando sua função (exceto para o [proprietário da conta](/docs/user-management-for-agencies#hash-do-proprietário-da-conta), conforme discutido abaixo).

> 📄 **Exemplo**
>
> Você atribuiu a José Silva a função de **gerente de equipe.** Esta função permite que José gerencie as **Configurações do aplicativo**, mas não permite que ele acesse o **Log de auditoria.**
>
> **Pergunta:** Posso manter José na função de Gerente da equipe, mas também dar a ele a capacidade de acessar o log de Auditoria? Posso remover sua capacidade de gerenciar as configurações do Aplicativo?
>
> **Resposta:** Não. Enquanto José permanecer na função de Gerente da equipe, você não poderá dar a ele a capacidade de acessar o log de Auditoria. Você também não pode remover a capacidade dele de gerenciar as configurações do aplicativo. Claro, você pode atribuir José a uma função diferente, e seus recursos mudarão para aqueles definidos por essa função.

### Funções temporárias — uma exceção à regra

Se você já tinha uma conta da AppsFlyer em nosso antigo sistema de gerenciamento de usuários (quando os únicos tipos de conta disponíveis eram administrador e membro da equipe), todos os usuários foram trazidos para o novo sistema com permissões inalteradas. Como resultado, a maioria desses usuários possui **funções temporárias**.

Saiba mais sobre como [gerenciar funções temporárias](/docs/user-management-for-agencies#managing-temp-roles).

### Administrador — uma função especial

Uma conta da AppsFlyer pode ter **um ou mais** administradores, mas cada conta tem pelo menos um. Esse papel especial tem várias características únicas:

* A função de administrador tem acesso a **todos** os recursos da conta, incluindo:
  * Todos os recursos e funções
  * Todos os aplicativos atuais e futuros
  * Todas as fontes de mídia e geolocalizaçõesEssa característica de "acesso total" da função de administrador não pode ser alterada ou limitada.

  #### hash do proprietário da conta
* O usuário criado no momento em que a conta foi aberta (o **"proprietário da conta"**) recebe o papel de administrador por padrão.
  * O proprietário da conta não pode ser excluído, removido da função de administrador ou editado de outra forma da página [**Gerenciamento de usuários**](/docs/user-management-for-agencies#página-de-gerenciamento-de-usuários). Da mesma forma, o endereço de e-mail do titular da conta não pode ser alterado.
    * Se você precisar alterar o proprietário da conta, siga as [etapas listadas abaixo](/docs/user-management-for-agencies#changing-the-account-owner).
  * O proprietário da conta é inicialmente responsável por criar usuários adicionais (até que usuários adicionais com recursos de gerenciamento de usuários sejam criados).
* Somente um usuário com função de administrador pode <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">gerenciar tokens de API e S2S</Anchor>.
* Qualquer administrador que não seja o proprietário da conta **pode** ser alterado para uma função diferente ou excluído da conta da AppsFlyer por meio da página de gerenciamento de usuários.

## Página de gerenciamento de usuários

**Para acessar a página de gerenciamento de usuários:**

1. Na barra de menus na parte superior, abra o menu da conta (dropdown do endereço de e-mail).
2. Selecione **Gerenciamento de usuários.**

### Aba usuários

A aba **usuários** exibe uma tabela de todos os usuários existentes em sua conta. É o ponto de partida para criar, gerenciar e excluir usuários.

* Clique em **usuário** para classificar a tabela em ordem alfabética (ascendente/decrescente).
* Use a caixa de pesquisa para localizar e exibir usuários específicos.
* Clique no ícone de filtro <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> no cabeçalho da coluna **Função** para filtrar os usuários por sua função (incluindo funções temporárias).
  * Para limpar o filtro, selecione **nenhum** na lista suspensa de filtros.
* Use as caixas de seleção para selecionar e [editar vários usuários](/docs/user-management-for-agencies#edição-multiusuário) ao mesmo tempo.

### Aba Funções

A aba **funções** exibe uma lista de todas as funções definidas na sua conta, incluindo:

* As 4 [funções predefinidas](#funções-predefinidas)
* Qualquer [função temporária](/docs/user-management-for-agencies#funções-temporárias--uma-exceção-à-regra) atualmente atribuída aos usuários

Clique no nome de qualquer função no painel esquerdo para ver:

* Detalhes completos dos recursos da função
* O número de usuários atualmente atribuídos a essa função (no canto superior direito da tela)
  * Passe o mouse sobre o ícone do usuário <Image alt="user_icon.png" src="https://files.readme.io/afd47a11e82e0cfac3240fe39582bd141639465952f6eef76bcf1f6e7532d6a9-16162513473937.png" width="21px" /> para ver uma lista dos 20 primeiros.

## Criando um usuário

**Para criar um novo usuário:**

1. Na aba **usuários**, clique no botão **novo usuário**.
2. Digite o nome do usuário (obrigatório):
   * Pode incluir letras, números, espaços, pontos (.), hífens (-), sublinhados (\_) e aspas simples (') ou duplas (").
   * Outros caracteres especiais não são permitidos.
3. Digite o endereço de e-mail do usuário (obrigatório):
   * Você pode incluir letras, números, apóstrofes ('), e comercial (&), cifrões ($), símbolos hash (#), hífens (-), sublinhados (\_) e pontos (.)
   * Dois pontos consecutivos (..) e outros caracteres especiais não são permitidos.
   * Você deve inserir um e-mail válido.

   > 🚧 **Importante!**
   >
   > O endereço de e-mail de um usuário é o que o identifica na plataforma da AppsFlyer, o que significa que:
   >
   > * Ele não pode ser alterado posteriormente sem excluir e recriar o usuário.
   > * Deve ser um endereço de e-mail válido no qual o usuário possa receber e-mail.
   > * Ele não pode ser associado a outro usuário em nenhuma conta da AppsFlyer.
   >   * Se o endereço de e-mail já estiver em uso (na sua conta ou em outra), você verá a mensagem *Não é possível criar esse usuário.* Siga as [etapas de solução de problemas abaixo](/docs/user-management-for-agencies#troubleshooting-can-t-create-this-user) para resolver esse problema.

4. Selecione o departamento do usuário (opcional).
5. Selecione a função do usuário (obrigatório).
6. Selecione os aplicativos que o usuário pode acessar:
   * A configuração padrão permite o acesso a todos os aplicativos atuais e futuros da conta. Para alterar essa configuração, use as caixas de seleção para marcar e desmarcar aplicativos.
   * Um usuário pode ter acesso a todos os aplicativos futuros somente se tiver acesso a todos os aplicativos atuais.
7. Clique em **Salvar** para criar o usuário.

   * O usuário recebe um convite por e-mail para ativar sua conta.

   #### hash de ativação da conta

   * O usuário é exibido na tabela do usuário. O ícone de envelope ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png) indica que um convite foi enviado e a conta está aguardando ativação. Depois que o usuário ativar sua conta, o envelope desaparecerá.
   * O link de ativação enviado ao usuário é válido por 48 horas. Se o usuário não recebeu o convite ou se o link expirou, você pode [reenviar o convite](/docs/user-management-for-agencies#resending-a-user-invitation).

## Editando usuários

Os usuários podem ser editados um de cada vez ou em grupos.

### Edição individual

**Para editar um usuário individual:**

1. Na aba **Usuários**, clique no botão **Ações** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> no lado direito da linha do usuário.
2. Selecione **Editar** no menu.
3. Edite as configurações do usuário conforme necessário.
4. Todas as configurações, exceto o endereço de e-mail, são editáveis.
5. Clique em **Salvar**.

### Edição multiusuário

A edição multiusuário é uma maneira eficiente de alterar as permissões da conta de vários usuários ao mesmo tempo. O uso desse recurso em combinação com os recursos de pesquisa e filtragem da aba **Usuários** pode torná-lo particularmente útil para gerenciar um grande número de usuários.

> 📘 **Observação**
>
> Você não pode excluir usuários nem atribuí-los à função de administrador usando a edição multiusuário.

**Para editar vários usuários:**

1. Na aba **Usuários**, marque as caixas de seleção do usuário ou usuários que você deseja editar.
   * Marque a caixa de seleção no cabeçalho da coluna para selecionar todos os usuários visíveis.
   * O número de usuários selecionados atualmente é exibido no lado direito da caixa de pesquisa. Observe que o [proprietário da conta](/docs/user-management-for-agencies#hash-do-proprietário-da-conta) não pode ser selecionado e não está incluído no número de usuários selecionados.
2. Os botões **Função** e **Aplicativos** são exibidos no canto superior direito da tabela.
   * Se um ou mais usuários selecionados tiverem acesso a aplicativos futuros, o botão **Aplicativos** não estará disponível. (Consulte [Limitações da função temporária](/docs/user-management-for-agencies#limitações-da-função-temporária), abaixo.)
3. Clique no botão das permissões que você deseja alterar.
4. Faça as alterações necessárias usando a caixa de diálogo ou as listas suspensas exibidas.
   * Lembre-se de que suas alterações se aplicam a todos os usuários selecionados!
5. Os usuários editados são destacados na tabela e aparecerão da forma devida assim que as alterações forem salvas. No entanto, você ainda tem a oportunidade de revisar suas alterações e confirmá-las ou cancelá-las na próxima etapa.
6. Revise suas alterações. Clique em **Salvar** para confirmar ou em **Cancelar** para desfazer.

> 📄 **Exemplo**
>
> **Cenário:**
>
> * Existem 10 usuários na sua conta. Seis deles estão na função **Marketing**.
> * Alice, José e Pedro acabaram de ser promovidos, e você quer mudá-los da função **Marketing** para a função **Gerente da equipe**.
> * Alice trabalhará com o aplicativo Astounding. José trabalhará com o aplicativo Beautiful. Pedro trabalhará com o aplicativo Charming.
>
> **Cenário:**
>
> 1. Use o filtro de função <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> para ver somente os usuários na função **Marketing**.
> 2. Mude Alice, José e Pedro para a função **Gerente de equipe**:
>    * Marque as caixas de seleção para Alice, José e Pedro.
>    * Clique no botão **Função**.
>    * Selecione **Gerente de equipe** na lista dropdown.
>    * Clique em **Salvar** para confirmar.
>    * Observe que, depois de confirmar as alterações, o filtro **Função** é limpo e a tabela exibe todos os usuários.
> 3. Dê a Alice, José e Pedro acesso ao aplicativo apropriado:
>    * Use a caixa de pesquisa para encontrar Alice e, em seguida, edite seu usuário individualmente para dar a ela acesso ao aplicativo Astounding.
>    * Repita essas etapas para José e Pedro para dar a eles acesso a Beautiful and Charming, respectivamente.

## Excluindo usuários

**Para excluir um usuário:**

1. Na aba **Usuários**, clique no botão **Ações** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> no lado direito da linha do usuário.
2. Selecione **Excluir** no menu.

## Situações especiais e procedimentos adicionais

<div id="managing-temp-roles" />

<Accordion title="Gerenciando funções temporárias">

Se sua conta usou nosso sistema de gerenciamento de usuários anterior no passado, [**as funções temporárias**](/docs/user-management-for-agencies#funções-temporárias--uma-exceção-à-regra) foram atribuídas aos usuários existentes para garantir que eles fossem trazidos para o novo sistema com recursos inalterados.

* Os usuários com os mesmos recursos receberam a mesma função temporária.
* Use os recursos da aba [Funções](/docs/user-management-for-agencies#aba-funções) para revisar os recursos de cada função temporária e uma lista de usuários que está atualmente nela.

#### Limitações da função temporária

As funções temporárias foram projetadas especificamente para permitir uma transição perfeita do nosso sistema anterior de gerenciamento de usuários. Como tal, eles estão disponíveis apenas em situações limitadas:

* As funções temporárias não podem ser atribuídas a outros usuários (sejam novos ou existentes).
* Um usuário com uma função temporária não pode receber uma função temporária diferente (embora você possa alterar os aplicativos às quais ele tem acesso).
  * Observe que o acesso de um usuário a aplicativos futuros **não pode** ser alterado enquanto o usuário estiver em uma função temporária.
* Quando um usuário com uma função temporária é alterado para uma função pré-definida, ele não pode ser retornado para a função temporária atribuída anteriormente (ou para qualquer outra função temporária).
* Se o último usuário em uma função temporária for removido dela, a função não aparecerá mais na sua conta.

> 📄 **Exemplo**
>
> Sua conta já usou nosso sistema de gerenciamento de usuários anterior. Diana e Eduardo eram usuários existentes no momento em que sua conta foi movida para o novo sistema. Diana está agora na função Temporária 1, e Eduardo está na função Temporária 2.
>
> * Você contratou uma nova funcionária, Flávia. Você pode atribuir a Flávia qualquer uma das 4 [funções predefinidas](#funções-predefinidas). No entanto, você não pode atribuir a Flávia as funções Temporária 1 ou a Temporária 2.
> * A Diana não pode ser transferida da função temporária 1 para a função temporária 2. No entanto, você pode atribuir qualquer uma das 4 funções predefinidas a ela. Você também pode alterar o acesso dela ao aplicativo conforme necessário.
> * Se você mover Diana da função Temporária 1 para a função Gerente de equipe, ela não poderá ser movida de volta para a função Temporária 1.
> * Se Diana foi a última usuária da função Temporária 1 quando a transferiu para a função Gerente de equipe, a função Temporária 1 deixará de aparecer na sua conta.

</Accordion>

<div id="changing-the-account-owner" />

<Accordion title="Alterar o proprietário da conta">

Como todos os administradores têm as mesmas permissões que o proprietário da conta, geralmente não é necessário alterar o proprietário da conta. Mas se você achar que precisa fazer essa alteração, siga as etapas abaixo.

> 🚧 **Importante!**
>
> Algumas coisas a considerar antes de começar:
>
> * Se você ainda estiver usando as APIs Pull, Master ou GDPR com token v1, alterar o proprietário da conta redefine automaticamente esses serviços. Para evitar a perda de dados, <Anchor target="_blank" href="/marketers/pt/docs/bulletin-api-token-changes">faça a transição para começar a usar essas APIs com o token v2</Anchor> **antes de alterar o proprietário da conta**.
> * A alteração do proprietário da conta deve ser concluída manualmente de acordo com essas etapas. Não pode ser feito a partir da página **Gerenciamento de usuários**.

#### #1–Envie sua solicitação através do widget de chat

Para iniciar o processo de alteração do proprietário da conta, abra o widget de chat <Anchor target="_blank" href="https://hq1.appsflyer.com/apps/search?openAssistant=true">usando este link</Anchor> ou clicando no botão Ajuda na barra da parte superior. Inclua as seguintes informações no chat:

* Nome do proprietário da conta que você deseja substituir
* Nome, cargo e e-mail do novo proprietário da conta

#### #2–Próximas etapas

Depois que a alteração for processada, você receberá uma notificação por e-mail da AppsFlyer.

* Se você quiser que o proprietário da conta anterior continue usando sua conta da AppsFlyer, <Anchor target="_blank" href="/marketers/pt/docs/user-management#creating-users">crie um novo usuário</Anchor> para ele e atribua a ele uma nova função.
* As APIs que usam o token v2 não são afetadas pela alteração do proprietário da conta. <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">Saiba mais sobre como gerenciar tokens</Anchor>.

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="Solução de problemas 'Não é possível criar este usuário'">

Se você receber a mensagem de erro *Não é possível criar esse usuário* ao inserir o endereço de e-mail de um novo usuário, isso geralmente significa que o e-mail já está associado a um usuário da AppsFlyer (na sua conta ou em uma conta diferente). Siga as etapas relevantes para sua situação:

Se o usuário estiver em sua conta:

* Verifique se o usuário ativou sua conta. Caso contrário, [reenvie o convite](/docs/user-management-for-agencies#resending-a-user-invitation), se necessário.
* Se o usuário ativou sua conta, peça que ele tente fazer login novamente usando o endereço de e-mail associado ao usuário. Aconselhe-os a seguir as etapas **Esqueci minha senha**, se necessário.

Se o e-mail do usuário for usado em uma conta diferente ou você não conseguir determinar a conta na qual o e-mail do usuário é usado, selecione uma das seguintes opções:

* Exclua-o da outra conta e adicione-o à sua (requer que você ou o usuário tenha as permissões necessárias na outra conta); ou
* Adicione-o à sua conta usando um endereço de e-mail diferente. Deve ser um endereço de e-mail válido no qual ele possa realmente receber um e-mail; ou
* Entre em contato com seu Customer Success Manager (CSM) ou envie um e-mail para nossa equipe de Engajamento do Cliente em [hello@appsflyer.com](mailto:hello@appsflyer.com).

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="Reenviar um convite de usuário">

Se um novo usuário não recebeu o [convite de ativação da conta](/docs/user-management-for-agencies#hash-de-ativação-da-conta) ou se ele não o ativou em 48 horas, você pode reenviar o e-mail da seguinte maneira:

1. Na aba **Usuários**, clique no botão **Ações** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> no lado direito da linha do usuário.
   * Observe que o usuário ainda é mostrado com um ícone de envelope ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png), indicando que ele ainda não ativou sua conta.
2. Selecione **Reenviar convite por e-mail** no menu.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="Redefinindo a autenticação de dois fatores (2FA) de um usuário">

Para contas que usam 2FA, pode haver ocasiões em que você precise redefinir a 2FA de um usuário. Veja <Anchor target="_blank" href="/marketers/pt/docs/implementing-and-using-2fa-login#reset">aqui</Anchor> como fazer isso.

</Accordion>

<div data-zendesk-anchors="background=fun%C3%A7%C3%B5es-de-usu%C3%A1rio-e-permiss%C3%B5es-de-acesso h_01HC72J0H988V27YCTWPFGF7EP=fun%C3%A7%C3%B5es-de-usu%C3%A1rio-e-permiss%C3%B5es-de-acesso predefined-roles=fun%C3%A7%C3%B5es-predefinidas h_01HC72J0H98447W34RD0ND2MC0=fun%C3%A7%C3%B5es-predefinidas predefined-roles-hash=hash-de-fun%C3%A7%C3%B5es-predefinidas h_01HC72J0H9RVA83J9F5QN4YS79=hash-de-fun%C3%A7%C3%B5es-predefinidas h_01HC72J0H9Y54Q2Y6AGP6H1DG0=exemplo temp-roles%E2%80%94an-exception-to-the-rule=fun%C3%A7%C3%B5es-tempor%C3%A1rias--uma-exce%C3%A7%C3%A3o-%C3%A0-regra h_01HC72J0H9NXMKJN64C73ZXZN1=fun%C3%A7%C3%B5es-tempor%C3%A1rias--uma-exce%C3%A7%C3%A3o-%C3%A0-regra admin%E2%80%94a-special-role=administrador--uma-fun%C3%A7%C3%A3o-especial h_01HC72J0HANGXV4GVJCQ5X2T84=administrador--uma-fun%C3%A7%C3%A3o-especial account-owner-hash=hash-do-propriet%C3%A1rio-da-conta h_01HC72J0HA5RFZE1G0KNKR30KV=hash-do-propriet%C3%A1rio-da-conta user-management-page=p%C3%A1gina-de-gerenciamento-de-usu%C3%A1rios h_01HC72J0HANQ3Z6FCWXA0TF3TN=p%C3%A1gina-de-gerenciamento-de-usu%C3%A1rios users-tab=aba-usu%C3%A1rios h_01HC72J0HAFBMYM792GXMCEY3T=aba-usu%C3%A1rios roles-tab=aba-fun%C3%A7%C3%B5es h_01HC72J0HAXC2NAVQC4J2PMB0Z=aba-fun%C3%A7%C3%B5es creating-a-user=criando-um-usu%C3%A1rio h_01HC72J0HATN656W4B9DT82M60=criando-um-usu%C3%A1rio h_01HC72J0HAP1GDH8JKGMT6XH67=importante account-activation-hash=hash-de-ativa%C3%A7%C3%A3o-da-conta h_01HC72J0HA3QJ2CH8TGEMJBY3A=hash-de-ativa%C3%A7%C3%A3o-da-conta editing-users=editando-usu%C3%A1rios h_01HC72J0HAG2XF42NSYRZDEKVN=editando-usu%C3%A1rios individual-editing=edi%C3%A7%C3%A3o-individual h_01HC72J0HAF739MQPF482T0WVA=edi%C3%A7%C3%A3o-individual multiuser-editing=edi%C3%A7%C3%A3o-multiusu%C3%A1rio h_01HC72J0HA3BKXJCAVRQ5SJYYE=edi%C3%A7%C3%A3o-multiusu%C3%A1rio h_01HC72J0HAZM2NBXN5ZHZET4BS=observa%C3%A7%C3%A3o h_01HC72J0HAE70AMWSDP5BXGWK9=exemplo-1 deleting-users=excluindo-usu%C3%A1rios h_01HC72J0HAQFD33VT0ARRWG0ZF=excluindo-usu%C3%A1rios special-situations-and-additional-procedures=situa%C3%A7%C3%B5es-especiais-e-procedimentos-adicionais h_01HC72J0HAF5QFC5ZR7EHFMBM6=situa%C3%A7%C3%B5es-especiais-e-procedimentos-adicionais h_01HC72J0HAD8JXPPFET4N2P3EK=managing-temp-roles temp-role-limitations=limita%C3%A7%C3%B5es-da-fun%C3%A7%C3%A3o-tempor%C3%A1ria h_01HC72J0HA8PP79VV1F03E5AXV=limita%C3%A7%C3%B5es-da-fun%C3%A7%C3%A3o-tempor%C3%A1ria h_01HC72J0HAJES0N195DZ797C4V=exemplo-2 h_01HC72J0HAVXK83AK99NQVDT8T=changing-the-account-owner h_01HC72J0HANXBK4T1SD6V2KHE4=importante-1 1%E2%80%93send-an-email-request=1envie-sua-solicita%C3%A7%C3%A3o-atrav%C3%A9s-do-widget-de-chat h_01HC72J0HAJ3C8WJ767KG2307C=1envie-sua-solicita%C3%A7%C3%A3o-atrav%C3%A9s-do-widget-de-chat 2%E2%80%93next-steps=2pr%C3%B3ximas-etapas h_01HC72J0HAM13NY9EKNKG8R1CA=2pr%C3%B3ximas-etapas troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HC72J0HAWRBVWGVT12W6M711=troubleshooting-can-t-create-this-user h_01HC72J0HANPD39FRCWSPMRY5D=resending-a-user-invitation h_01HC72J0HARYRSXHKX41A41MPG=resetting-twofactor-authentication-2fa" />
