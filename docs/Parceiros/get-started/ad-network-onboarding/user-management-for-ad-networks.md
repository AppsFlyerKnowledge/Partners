---
title: Gerenciamento de usuários para ad networks
metadata:
  keywords:
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
  created_at: '2021-12-19T11:16:28Z'
  edited_at: '2026-08-18T00:40:14Z'
  id: 4414238502289
  locale: pt
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/pt/articles/4414238502289
---
> **Visão geral:** Crie e gerencie os usuários da AppsFlyer da sua conta de ad network e atribua a eles uma função que define quais recursos eles podem acessar.

<div id="background" />

## CONTEXTO

As contas de ad network da AppsFlyer permitem vários usuários, cada um com uma função que define seu acesso a recursos e funções.

A função **Admin** tem acesso a todos os recursos. A função **Marketing** tem acesso a um conjunto mais limitado de recursos. A lista completa desses recursos por função está disponível na [aba funções](/docs/user-management-for-ad-networks#aba-funções) da página de **gerenciamento de usuários**.

<div id="more-about-roles" />

## Mais sobre funções

Como regra geral, todas as funções são predefinidas e as capacidades de cada função são fixas: não é permitido combiná-las. No entanto, você pode alterar os recursos funcionais de um usuário a qualquer momento alterando sua função (exceto para o [proprietário da conta](/docs/user-management-for-ad-networks#administrador--uma-função-especial), conforme discutido abaixo).

<div id="example" />

> 📄 **Exemplo**
>
> Você atribuiu José Santos à função de **Marketing**. Esta função permite que José gerencie as **Regras de validação**, mas não permite que ele acesse o log de **Auditoria.**
>
> **Pergunta:** Posso manter José na função de Marketing, mas também dar a ele a capacidade de acessar o log de Auditoria? Posso remover sua capacidade de gerenciar Regras de validação?
>
> **Resposta:** Não. Enquanto José permanecer na função de Marketing, você não poderá dar a ele a capacidade de acessar o log de Auditoria. Você também não poderá remover sua capacidade de gerenciar Regras de validação. Claro, você pode atribuir José a uma função diferente, e seus recursos mudarão para aqueles definidos por essa função.

<div id="temp-rolesan-exception-to-the-rule" />

### Funções temporárias — uma exceção à regra

Se você já tinha uma conta da AppsFlyer em nosso antigo sistema de gerenciamento de usuários (quando os únicos tipos de conta disponíveis eram administrador e membro da equipe), todos os usuários foram trazidos para o novo sistema com permissões inalteradas. Como resultado, a maioria desses usuários possui **funções temporárias**.

Saiba mais sobre como [gerenciar funções temporárias](/docs/user-management-for-ad-networks#managing-temp-roles).

<div id="admina-special-role" />

### Administrador — uma função especial

Uma conta da AppsFlyer pode ter **um ou mais** administradores, mas cada conta tem pelo menos um. Esse papel especial tem várias características únicas:

* A função de administrador tem acesso a **todos** os recursos da conta, incluindo:

  * Todos os recursos e funções
  * Todos os aplicativos atuais e futuros
  * Todas as fontes de mídia e geolocalizações

  Essa característica de "acesso total" da função de administrador não pode ser alterada ou limitada.
* <span id="account-owner"></span>**Proprietário da conta:** O usuário criado no momento em que a conta foi aberta recebe a função de Administrador por padrão.
  * O proprietário da conta não pode ser excluído, removido da função de administrador ou editado de outra forma da página [Gerenciamento de usuários](/docs/user-management-for-ad-networks#página-de-gerenciamento-de-usuários). Da mesma forma, o endereço de e-mail do titular da conta não pode ser alterado.
    * Se você precisar alterar o proprietário da conta, siga as [etapas listadas abaixo](/docs/user-management-for-ad-networks#changing-the-account-owner).
  * O proprietário da conta é inicialmente responsável por criar usuários adicionais (até que usuários adicionais com recursos de gerenciamento de usuários sejam criados).
* Os administradores podem <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">gerenciar tokens API e S2S</Anchor>.
* Qualquer administrador que não seja o proprietário da conta **pode** ser alterado para uma função diferente ou excluído da conta da AppsFlyer por meio da página de gerenciamento de usuários.

<div id="user-management-page" />

## Página de gerenciamento de usuários

**Para acessar a página de gerenciamento de usuários:**

1. Na barra de menus na parte superior, clique no menu suspenso do endereço de e-mail.
2. Selecione **Gerenciamento de usuários.**

<div id="users-tab" />

### Aba usuários

A aba **usuários** exibe uma tabela de todos os usuários existentes em sua conta. É o ponto de partida para criar, gerenciar e excluir usuários.

* Clique em **usuário** para classificar a tabela em ordem alfabética (ascendente/decrescente).
* Use a caixa de pesquisa para localizar e exibir usuários específicos.
* Clique no ícone de filtro <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> no cabeçalho da coluna **Função** para filtrar os usuários pela função (incluindo funções temporárias).
  * Para limpar o filtro, selecione **nenhum** na lista suspensa de filtros.
* Use as caixas de seleção para selecionar e [editar vários usuários](/docs/user-management-for-ad-networks#edição-multiusuário) ao mesmo tempo.

<div id="roles-tab" />

### Aba Funções

A aba **funções** exibe uma lista de todas as funções definidas na sua conta, incluindo:

* As 2 [Funções predefinidas](/docs/user-management-for-ad-networks#mais-sobre-funções) de Administrador e Marketing
* Qualquer [função temporária](/docs/user-management-for-ad-networks#funções-temporárias--uma-exceção-à-regra) atualmente atribuída aos usuários

Clique no nome de qualquer função no painel esquerdo para ver:

* Detalhes completos dos recursos da função
* O número de usuários atualmente atribuídos a essa função (no canto superior direito da tela)
  * Passe o mouse sobre o ícone do usuário <Image alt="user_icon.png" src="https://files.readme.io/afd47a11e82e0cfac3240fe39582bd141639465952f6eef76bcf1f6e7532d6a9-16162513473937.png" width="21px" /> para ver uma lista dos 20 primeiros.

<div id="creating-a-user" />

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

   <div id="important" />

   > 🚧 **Importante!**
   >
   > O endereço de e-mail de um usuário é o que o identifica na plataforma da AppsFlyer, o que significa que:
   >
   > * Ele não pode ser alterado posteriormente sem excluir e recriar o usuário.
   > * Deve ser um endereço de e-mail válido no qual o usuário possa receber e-mail.
   > * Ele não pode ser associado a outro usuário em nenhuma conta da AppsFlyer.
   >   * Se o endereço de e-mail já estiver em uso (na sua conta ou em outra), você verá a mensagem *Não é possível criar esse usuário.* Siga as [etapas de solução de problemas abaixo](/docs/user-management-for-ad-networks#troubleshooting-can-t-create-this-user) para resolver esse problema.

4. Selecione o departamento do usuário (opcional).
5. Selecione a função do usuário (obrigatório).
6. Selecione os aplicativos que o usuário pode acessar:
   1. A configuração padrão permite o acesso a todos os aplicativos atuais e futuros da conta. Para alterar essa configuração, use as caixas de seleção para marcar e desmarcar aplicativos.
   2. Um usuário pode ter acesso a todos os aplicativos futuros somente se tiver acesso a todos os aplicativos atuais.
7. Clique em **Salvar** para criar o usuário.
8. **O que o usuário deve fazer:** Para se tornar um usuário ativo (membro da equipe), o usuário deve [ativar sua conta](#tornando-se-um-usuário-ativo) a partir do convite por e-mail que recebeu.

<div id="becoming-an-active-user" />

#### Tornando-se um usuário ativo

Depois de clicar em **Salvar** para finalizar o procedimento de [criar um usuário](/docs/user-management-for-ad-networks#criando-um-usuário) (acima), o usuário recebe um convite por e-mail para ativar sua conta. O link de ativação é válido por 48 horas. Se o usuário não recebeu o convite ou se o link expirou, você pode [reenviar o convite](/docs/user-management-for-ad-networks#resending-a-user-invitation).

Você pode ver o novo usuário na página Gerenciamento de usuários, com um ícone de envelope ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png) perto de seu nome. Isso indica que um convite foi enviado e a conta está aguardando ativação. Depois que o usuário ativa sua conta, o envelope desaparece.

<div id="editing-users" />

## Editando usuários

Os usuários podem ser editados um de cada vez ou em grupos.

<div id="individual-editing" />

### Edição individual

**Para editar um usuário individual:**

1. Na aba **usuários**, clique no botão **ações** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> no lado direito da linha do usuário.
2. Selecione **Editar** no menu.
3. Edite as configurações do usuário conforme necessário.
   * Todas as configurações, exceto o endereço de e-mail, são editáveis.
4. Clique em **Salvar**.

<div id="multi-user-editing" />

### Edição multiusuário

A edição multiusuário é uma maneira eficiente de alterar a função de vários usuários ao mesmo tempo. O uso desse recurso em combinação com os recursos de pesquisa e filtragem da aba **Usuários** pode torná-lo particularmente útil para gerenciar um grande número de usuários.

<div id="note" />

> 📘 **Observação**
>
> Você não pode excluir usuários nem atribuí-los à função de administrador usando a edição multiusuário.

**Para editar vários usuários:**

1. Na aba **Usuários**, marque as caixas de seleção do usuário ou usuários que você deseja editar.
   * Marque a caixa de seleção no cabeçalho da coluna para selecionar todos os usuários visíveis.
   * O número de usuários selecionados atualmente é exibido no lado direito da caixa de pesquisa. Observe que o [proprietário da conta](/docs/user-management-for-ad-networks#administrador--uma-função-especial) não pode ser selecionado e não está incluído no número de usuários selecionados.
2. Clique no botão **Função** que é exibido no canto superior direito da tabela.
3. Faça as alterações necessárias. Lembre-se de que suas alterações se aplicam a todos os usuários selecionados!
4. Os usuários editados são destacados na tabela e aparecerão da forma devida assim que as alterações forem salvas. No entanto, você ainda tem a oportunidade de revisar suas alterações e confirmá-las ou cancelá-las na próxima etapa.
5. Revise suas alterações. Clique em **Salvar** para confirmar ou em **Cancelar** para desfazer.

<div id="deleting-users" />

## Excluindo usuários

**Para excluir um usuário:**

1. Na aba **Usuários**, clique no botão **Ações** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> no lado direito da linha do usuário.
2. Selecione **Excluir** no menu.

<div id="special-situations-and-additional-procedures" />

## Situações especiais e procedimentos adicionais

<div id="managing-temp-roles" />

<Accordion title="Gerenciando funções temporárias">

Se sua conta usou nosso sistema de gerenciamento de usuários anterior no passado, [as funções temporárias](/docs/user-management-for-ad-networks#funções-temporárias--uma-exceção-à-regra) foram atribuídas aos usuários existentes para garantir que eles fossem trazidos para o novo sistema com recursos inalterados.

* Os usuários com os mesmos recursos receberam a mesma função temporária.
* Use os recursos da aba [Funções](/docs/user-management-for-ad-networks#aba-funções) para revisar os recursos de cada função temporária e uma lista de usuários que está atualmente nela.

<div id="temp-role-limitations" />

#### Limitações da função temporária

As funções temporárias foram projetadas especificamente para permitir uma transição perfeita do nosso sistema anterior de gerenciamento de usuários. Como tal, eles estão disponíveis apenas em situações limitadas:

* As funções temporárias não podem ser atribuídas a outros usuários (sejam novos ou existentes).
* Um usuário com uma função temporária não pode receber uma função temporária diferente.
* Quando um usuário com uma função temporária é alterado para uma função pré-definida, ele não pode ser retornado para a função temporária atribuída anteriormente (ou para qualquer outra função temporária).
* Se o último usuário em uma função temporária for removido dela, a função não aparecerá mais na sua conta.

<div id="example-1" />

> 📄 **Exemplo**
>
> Sua conta já usou nosso sistema de gerenciamento de usuários anterior. Diana e Eduardo eram usuários existentes no momento em que sua conta foi movida para o novo sistema. Diana está agora na função Temporária 1, e Eduardo está na função Temporária 2.
>
> * Você contratou uma nova funcionária, Flávia. Você pode atribuir Flávia à função Administrador ou Marketing. No entanto, você não pode atribuir a Flávia as funções Temporária 1 ou a Temporária 2.
> * A Diana não pode ser transferida da função temporária 1 para a função temporária 2. No entanto, você pode atribuí-la à função Administrador ou Marketing.
> * Se você mover Diana da função Temporária 1 para a função Marketing, ela não poderá ser movida de volta para a função Temporária 1.
> * Se Diana foi a última usuária da função Temporária 1 quando a transferiu para a função Marketing, a função Temporária 1 deixará de aparecer na sua conta.

<div id="changing-the-account-owner" />

<Accordion title="Alterar o proprietário da conta">

Como todos os administradores têm as mesmas permissões que o proprietário da conta, geralmente não é necessário alterar o proprietário da conta. Mas se você achar que precisa fazer essa alteração, siga as etapas abaixo.

<div id="important-1" />

> 🚧 **Importante!**
>
> Algumas coisas a considerar antes de começar:
>
> A alteração do proprietário da conta deve ser concluída manualmente de acordo com essas etapas. Não pode ser feito a partir da página **Gerenciamento de usuários**.

<div id="1send-your-request-via-the-chat-widget" />

#### #1–Envie sua solicitação através do widget de chat

Para iniciar o processo de alteração do proprietário da conta, abra o widget de chat <Anchor target="_blank" href="https://hq1.appsflyer.com/apps/search?openAssistant=true">usando este link</Anchor> ou clicando no botão Ajuda no canto superior direito da barra de menus. Inclua as seguintes informações no chat:

* Nome do proprietário da conta que você deseja substituir
* Nome, cargo e e-mail do novo proprietário da conta

<div id="2next-steps" />

#### #2–Próximas etapas

Depois que a alteração for processada, você receberá uma notificação por e-mail da AppsFlyer.

* Se você quiser que o proprietário da conta anterior continue usando sua conta da AppsFlyer, <Anchor target="_blank" href="/marketers/pt/docs/user-management#creating-users">crie um novo usuário</Anchor> para ele e atribua a ele uma nova função.
* As APIs que usam o token v2 não são afetadas pela alteração do proprietário da conta.    <Anchor target="_blank" href="/marketers/pt/docs/managing-appsflyer-tokens">Saiba mais sobre como gerenciar tokens.</Anchor>

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="Solução de problemas 'Não é possível criar este usuário'">

Se você receber a mensagem de erro *Não é possível criar esse usuário* ao inserir o endereço de e-mail de um novo usuário, isso geralmente significa que o e-mail já está associado a um usuário da AppsFlyer (na sua conta ou em uma conta diferente). Siga as etapas relevantes para sua situação:

Se o usuário estiver em sua conta:

* Verifique se o usuário ativou sua conta. Caso contrário, [reenvie o convite](/docs/user-management-for-ad-networks#resending-a-user-invitation), se necessário.
* Se o usuário ativou sua conta, peça que ele tente fazer login novamente usando o endereço de e-mail associado ao usuário. Aconselhe-os a seguir as etapas **Esqueci minha senha**, se necessário.

Se o e-mail do usuário for usado em uma conta diferente ou você não conseguir determinar a conta na qual o e-mail do usuário é usado, selecione uma das seguintes opções:

* Exclua-o da outra conta e adicione-o à sua (requer que você ou o usuário tenha as permissões necessárias na outra conta); ou
* Adicione-o à sua conta usando um endereço de e-mail diferente. Deve ser um endereço de e-mail válido no qual ele possa realmente receber um e-mail; ou
* Entre em contato com o suporte da AppsFlyer para Parceiros pelo <Anchor target="_blank" href="/partners/pt/docs/using-the-partner-assistant-chatbot">chatbot do assistente de parceiros</Anchor>.

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="Reenviar um convite de usuário">

Se um novo usuário não recebeu o [convite de ativação da conta](/docs/user-management-for-ad-networks#tornando-se-um-usuário-ativo) ou se ele não o ativou em 48 horas, você pode reenviar o e-mail da seguinte maneira:

1. Na aba **Usuários**, clique no botão **Ações** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> no lado direito da linha do usuário.
   * Observe que o usuário ainda é mostrado com um ícone de envelope ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png), indicando que ele ainda não ativou sua conta.
2. Selecione **Reenviar convite por e-mail** no menu.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="Redefinindo a autenticação de dois fatores (2FA)">

Se sua conta usa 2FA, pode haver ocasiões em que você precise redefinir as configurações de 2FA de um usuário. Faça o seguinte:

1. Na aba **Usuários**, clique no botão **Ações** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> no lado direito da linha do usuário.
2. Selecione **Redefinir 2FA** no menu.

**Observação:** Um administrador pode redefinir a 2FA de qualquer outro administrador que não seja a sua própria ou a do [proprietário da conta](/docs/user-management-for-ad-networks#administrador--uma-função-especial). Para redefinir a 2FA do proprietário da conta, entre em contato com a equipe de suporte da AppsFlyer.

</Accordion>

</Accordion>

<div data-zendesk-anchors="background=contexto h_01HEN51924E23493MKXPEKHS03=contexto more-about-roles=mais-sobre-fun%C3%A7%C3%B5es h_01HEN51924R007XNM3N45CA73A=mais-sobre-fun%C3%A7%C3%B5es h_01HEN51924WBY63ASRGH7ZQFP4=exemplo temp-roles%E2%80%94an-exception-to-the-rule=fun%C3%A7%C3%B5es-tempor%C3%A1rias--uma-exce%C3%A7%C3%A3o-%C3%A0-regra h_01HEN51924DT5GVPMJBQD3ZY9R=fun%C3%A7%C3%B5es-tempor%C3%A1rias--uma-exce%C3%A7%C3%A3o-%C3%A0-regra admin%E2%80%94a-special-role=administrador--uma-fun%C3%A7%C3%A3o-especial h_01HEN51924G6GXVH8HH5DAWZ26=administrador--uma-fun%C3%A7%C3%A3o-especial user-management-page=p%C3%A1gina-de-gerenciamento-de-usu%C3%A1rios h_01HEN51924PQEM4R974HMWPH98=p%C3%A1gina-de-gerenciamento-de-usu%C3%A1rios users-tab=aba-usu%C3%A1rios h_01HEN51924RDZFSJN0KN0YJFND=aba-usu%C3%A1rios roles-tab=aba-fun%C3%A7%C3%B5es h_01HEN519249AHVKGM5CDTXPEP7=aba-fun%C3%A7%C3%B5es creating-a-user=criando-um-usu%C3%A1rio h_01HEN51924C56PAKQYTQM05DMV=criando-um-usu%C3%A1rio h_01HEN519241VD35W7AYQ08NMHJ=importante becoming-an-active-user=tornando-se-um-usu%C3%A1rio-ativo h_01HEN51924F0G8287RP08EB464=tornando-se-um-usu%C3%A1rio-ativo editing-users=editando-usu%C3%A1rios 01HEPXYXV78HEXK5SD4QBDGEGH=editando-usu%C3%A1rios individual-editing=edi%C3%A7%C3%A3o-individual h_01HEN51924AP4TT97C2X5CRB35=edi%C3%A7%C3%A3o-individual multiuser-editing=edi%C3%A7%C3%A3o-multiusu%C3%A1rio h_01HEN519246HC2M4BB35GR29SQ=edi%C3%A7%C3%A3o-multiusu%C3%A1rio h_01HEN51925ZWQ8V3XJNAD4F4V9=observa%C3%A7%C3%A3o deleting-users=excluindo-usu%C3%A1rios h_01HEN51925Q9P2GFJWWWW9MMQ2=excluindo-usu%C3%A1rios special-situations-and-additional-procedures=situa%C3%A7%C3%B5es-especiais-e-procedimentos-adicionais h_01HEN51925JBC3R887CVFNFA27=situa%C3%A7%C3%B5es-especiais-e-procedimentos-adicionais h_01HEN519258745RNY4RNT4MWK6=managing-temp-roles temp-role-limitations=limita%C3%A7%C3%B5es-da-fun%C3%A7%C3%A3o-tempor%C3%A1ria h_01HEN51925REZEKBA501T0RMME=limita%C3%A7%C3%B5es-da-fun%C3%A7%C3%A3o-tempor%C3%A1ria h_01HEN51925FMKJ5D7BE93GVN2G=exemplo-1 h_01HEN51925J3NKAJSKYEF9AMMJ=changing-the-account-owner h_01HEN51925FR6AGT1M2YHJJB6A=importante-1 1%E2%80%93send-an-email-request=1envie-sua-solicita%C3%A7%C3%A3o-atrav%C3%A9s-do-widget-de-chat h_01HEN51925GQGFAZYRTHPBBXA2=1envie-sua-solicita%C3%A7%C3%A3o-atrav%C3%A9s-do-widget-de-chat 2%E2%80%93next-steps=2pr%C3%B3ximas-etapas h_01HEN51925SPRA034581N8BWYK=2pr%C3%B3ximas-etapas troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HEN51925YAY0E37S799S7S1J=troubleshooting-can-t-create-this-user h_01HEN519253VMNBPNW61M10QZW=resending-a-user-invitation h_01HEN51925C7X1AEM2FJ6152Z1=resetting-twofactor-authentication-2fa" />
