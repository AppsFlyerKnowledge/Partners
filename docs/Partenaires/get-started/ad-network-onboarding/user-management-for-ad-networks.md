---
title: Gestion des utilisateurs pour les réseaux publicitaires
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
  edited_at: '2024-08-29T07:35:21Z'
  id: 4414238502289
  locale: fr
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/fr/articles/4414238502289
---
> **En bref :** créez et gérez les utilisateurs AppsFlyer de votre compte de réseau publicitaire, puis attribuez-leur un rôle pour définir les fonctionnalités auxquelles ils pourront accéder.

<div id="background" />

## Avant de commencer

Les comptes de réseau publicitaire AppsFlyer autorisent plusieurs utilisateurs, chacun avec un rôle qui définit leur accès aux fonctionnalités et paramètres.

Le rôle d’**Admin** donne accès à l’ensemble des fonctionnalités et paramètres. Le rôle de **Marketing** donne accès à un nombre de fonctionnalités plus limité. La liste complète des capacités accordées à chaque rôle est disponible dans l'onglet [Rôles](/docs/user-management-for-ad-networks#onglet-rôles) de la page **Gestion des utilisateurs**.

<div id="more-about-roles" />

## À propos des rôles

En règle générale, tous les rôles sont prédéfinis et les possibilités de chaque rôle sont fixes : aucun réarrangement n'est autorisé. Par contre, vous pouvez modifier les capacités d'un utilisateur à tout moment en modifiant son rôle (à l'exception du [propriétaire du compte](/docs/user-management-for-ad-networks#admin---un-rôle-particulier), comme expliqué ci-dessous).

<div id="example" />

> 📄 **Exemple**
>
> Vous avez attribué à Bill Bates le rôle **Marketing**. Ce rôle donne à Bill la possibilité de gérer **les règles de validation**, mais il ne lui permet pas d'accéder au **journal d'audit.**
>
> **Question :** Puis-je maintenir le rôle Marketing pour Bill, tout en lui donnant en plus la possibilité d'accéder au journal d'audit ? Puis-je lui retirer la capacité de gérer les règles de validation ?
>
> **Réponse** : Non. Tant que Bill conserve le rôle de Marketing, vous ne pouvez pas lui donner la possibilité d'accéder au journal d'audit. Vous ne pouvez pas non plus supprimer sa capacité à gérer les règles de validation. Bien entendu, vous pouvez donner à Bill un autre rôle prédéfini, et ses capacités seront celles qu’autorise ce nouveau rôle.

<div id="temp-rolesan-exception-to-the-rule" />

### Les rôles provisoire : une exception à la règle

Si votre compte AppsFlyer existait dans notre ancien système de gestion des utilisateurs (lorsque les seuls types de comptes disponibles étaient Admin et Membre d'équipe), tous les utilisateurs ont été envoyés dans le nouveau système avec les mêmes autorisations. Par conséquent, la plupart de ces utilisateurs apparaissent dans le système actuel avec des **rôles provisoire**.

En savoir plus sur la [gestion des rôles provisoires.](/docs/user-management-for-ad-networks#managing-temp-roles)

<div id="admina-special-role" />

### Admin - un rôle particulier

Un compte AppsFlyer peut avoir **un ou plusieurs** admins, mais il doit forcément en avoir au moins un. Ce rôle particulier a plusieurs caractéristiques uniques :

* Le rôle d'admin permet d'accéder à **toutes les fonctionnalités du compte**, notamment :
  * Toutes les caractéristiques et fonctions
  * Toutes les applications actuelles et futures
  * Toutes les sources média et zones géoCette particularité qui donne un accès illimité au rôle d'admin ne peut être ni modifiée, ni réduite.
* <span id="account-owner"></span>**Propriétaire de compte :** l'utilisateur créé au moment de l'ouverture du compte se voit attribuer par défaut le rôle d'admin.
  * Le propriétaire du compte ne peut pas être supprimé, il ne peut être extrait du rôle d'admin ni modifié d'une quelconque manière depuis la page [Gestion des utilisateurs](/docs/user-management-for-ad-networks#page-de-gestion-des-utilisateurs). De même, l'e-mail du propriétaire du compte ne peut pas être modifié.
    * Si vous devez changer le propriétaire du compte, suivez les étapes [indiquées ci-dessous](/docs/user-management-for-ad-networks#changing-the-account-owner).
  * Le propriétaire du compte est en premier lieu celui qui crée de nouveaux utilisateurs (jusqu'à ce que des utilisateurs disposant de capacités de gestion des utilisateurs soient créés).
* Les admins peuvent <Anchor target="_blank" href="/marketers/fr/docs/managing-appsflyer-tokens">gérer les jetons d’API et S2S</Anchor>.
* Tout admin autre que le propriétaire du compte **peut** se voir attribuer un autre rôle, ou être supprimé du compte AppsFlyer via la page de gestion des utilisateurs.

<div id="user-management-page" />

## Page de gestion des utilisateurs

**Pour accéder à la page de gestion des utilisateurs :**

1. Dans la barre de menu (en haut), cliquez sur l'adresse e-mail pour voir le menu déroulant.
2. Sélectionnez **Gestion des utilisateurs.**

<div id="users-tab" />

### Onglet Utilisateurs

L'onglet **Utilisateurs** affiche un tableau de tous les utilisateurs existants dans votre compte. C'est le point de départ de la création, de la gestion et de la suppression des utilisateurs.

* Cliquez sur le titre de colonne **Utilisateurs** pour trier le tableau par ordre alphabétique (croissant/décroissant).
* Utilisez le champ de recherche pour trouver et afficher des utilisateurs spécifiques.
* Cliquez sur l'icône de filtre <Image alt="filter_icon.png" src="https://files.readme.io/00fa39bef5e51bf9a8a0b2ae2dee4b631b57d423e261883bff1199d7293c0458-17387375698833.png" width="25px" /> dans l'en-tête de la colonne **Rôle** pour filtrer les utilisateurs par rôle (y compris les rôles provisoires).
  * Pour supprimer le filtre, sélectionnez **Aucun** dans la liste déroulante du filtre.
* Utilisez les cases à cocher pour sélectionner et [modifier plusieurs utilisateurs](/docs/user-management-for-ad-networks#modification-par-groupes) en même temps.

<div id="roles-tab" />

### Onglet Rôles

L'onglet **Rôles** affiche une liste de tous les rôles définis dans votre compte, notamment :

* Les 2 [rôles prédéfinis](/docs/user-management-for-ad-networks#à-propos-des-rôles) Admin et Marketing
* Tous les [Rôles provisoires](/docs/user-management-for-ad-networks#les-rôles-provisoire--une-exception-à-la-règle) en cours pour les utilisateurs

Cliquez sur le nom de n’importe quel rôle dans le panneau de gauche pour voir :

* Toutes les infos sur les capacités du rôle
* Le nombre d'utilisateurs actuellement affectés à ce rôle (en haut à droite de l'écran)
  * Passez la souris sur l'icône Utilisateur <Image alt="user_icon.png" src="https://files.readme.io/70d626cc0d2888c46c0e080dc76e4f005312fe5dea7e7811336e0324e4a846ad-17387375703569.png" width="21px" /> pour voir la liste des 20 premiers utilisateurs.

<div id="creating-a-user" />

## Créer un utilisateur

**Pour créer un nouvel utilisateur :**

1. Dans l'onglet **Utilisateurs**, cliquez sur le bouton **Nouvel utilisateur**.
2. Saisissez le nom de l'utilisateur (obligatoire) :
   * Il peut s'agir de lettres, de chiffres, d'espaces, de points (.), de traits d'union (-), de caractères de soulignement (\_) et de guillemets simples (') ou doubles (").
   * Les caractères spéciaux ne sont pas autorisés.
3. Saisissez l'e-mail de l'utilisateur (obligatoire) :
   * Peut inclure des lettres, des chiffres, des apostrophes ('), des esperluettes (&), des signes du dollar ($), des hashtags (#), des traits d'union (-), des traits de soulignement (\_) et des points (.).
   * Deux points à la suite (..) ou tout autre caractère spécial ne sont pas autorisés.
   * Doit se terminer par un domaine e-mail valide.

   <div id="important" />

   > 🚧 **Attention !**
   >
   > L'e-mail d'un utilisateur est ce qui permet de l'identifier sur la plateforme AppsFlyer :
   >
   > * Il sera impossible de le modifier ultérieurement : vous devrez supprimer et recréer l'utilisateur.
   > * L'adresse e-mail doit être valide, l’utilisateur doit pouvoir accéder à la boîte de réception.
   > * Elle ne doit pas être associée à un autre utilisateur dans un autre compte AppsFlyer.
   >   * Si l'e-mail est déjà utilisé (dans votre compte ou dans un autre), le message suivant s'affiche : *Impossible de créer cet utilisateur.* Suivez les [étapes de dépannage ci-dessous](/docs/user-management-for-ad-networks#troubleshooting-can-t-create-this-user) pour résoudre le problème.

4. Sélectionnez le département de l'utilisateur (facultatif).
5. Sélectionnez le rôle de l'utilisateur (obligatoire).
6. Cliquez sur **Enregistrer** pour créer l'utilisateur.
7. **Du côté de l'utilisateur :** pour devenir un utilisateur actif (membre d'équipe), l'utilisateur doit [activer son compte](#devenir-un-utilisateur-actif) depuis l’e-mail d’invitation qu'il a reçu.

<div id="becoming-an-active-user" />

#### Devenir un utilisateur actif

Après avoir cliqué **sur Enregistrer** pour terminer la [création de l’utilisateur](/docs/user-management-for-ad-networks#créer-un-utilisateur) (ci-dessus), l'utilisateur reçoit une invitation par e-mail pour activer son compte. Le lien d'activation est valable pendant 48 heures. Si l'utilisateur ne reçoit pas l'invitation ou si le lien expire, vous pouvez [renvoyer l'invitation](/docs/user-management-for-ad-networks#resending-a-user-invitation).

Vous pouvez voir le nouvel utilisateur sur la page de gestion des utilisateurs, à côté de son nom s’affiche une icône en forme d'enveloppe ![pending_invitation_icon.png](https://files.readme.io/1e334edd433f9ac13a175cdd48345adebe02892215896ea967768dc3cabf0349-17387375704209.png) à côté de son nom. L’icône indique qu'une invitation a été envoyée et que le compte est en attente d'activation. Une fois que l'utilisateur aura activé son compte, l'enveloppe disparaîtra.

<div id="editing-users" />

## Modification des utilisateurs

Les utilisateurs peuvent être modifiés un par un, ou par groupes.

<div id="individual-editing" />

### Modification individuelle

**Pour modifier un seul utilisateur :**

1. Dans l’onglet **Utilisateurs**, cliquez sur **Actions** <Image alt="actions_icon.png" src="https://files.readme.io/7bdbda083da16718b90246b7d915ebee2e164fa402a143e0c6cc9be95ca34dca-17387343712017.png" width="25px" />bouton tout à droite de la ligne de l'utilisateur.
2. Sélectionnez **Modifier** dans le menu.
3. Modifiez les paramètres de l'utilisateur.
   * Tous les paramètres en dehors de l'adresse e-mail sont modifiables.
4. Cliquez sur **Enregistrer**.

<div id="multi-user-editing" />

### Modification par groupes

La modification multi-utilisateur permet de modifier rapidement le rôle de plusieurs utilisateurs à la fois. Cette fonction associée au filtrage dans l'onglet **Utilisateurs** peut s'avérer particulièrement utile pour la gestion d'un grand nombre d'utilisateurs.

<div id="note" />

> 📘 **Remarque**
>
> Vous ne pouvez pas supprimer des utilisateurs ou les affecter au rôle d'admin en utilisant l'édition par groupes.

**Pour modifier plusieurs utilisateurs :**

1. Dans l'onglet **Utilisateurs**, cochez l'utilisateur ou les utilisateurs que vous souhaitez modifier.
   * Cochez la case du titre de colonne pour sélectionner tous les utilisateurs visibles.
   * Le nombre d'utilisateurs sélectionnés s'affiche à droite de la boîte de recherche. Notez que le [propriétaire du compte](/docs/user-management-for-ad-networks#admin---un-rôle-particulier) ne peut pas être sélectionné, il n'est donc pas inclus dans le nombre d'utilisateurs sélectionnés.
2. Cliquez sur le bouton **Rôle** (en haut à droite du tableau).
3. Effectuez les modifications nécessaires. N'oubliez pas que vos modifications s'appliquent à tous les utilisateurs sélectionnés !
4. Les utilisateurs modifiés s’affichent surlignés dans le tableau, et tels qu'ils seront une fois les modifications enregistrées. Cependant, vous aurez toujours la possibilité de revoir vos modifications et de les confirmer ou les annuler à l'étape suivante.
5. Vérifiez vos modifications. Cliquez sur **Sauvegarder** ou sur **Annuler**.

<div id="deleting-users" />

## Supprimer des utilisateurs

**Pour supprimer un utilisateur :**

1. Dans l’onglet **Utilisateurs**, cliquez sur le bouton **Actions** <Image alt="actions_icon.png" src="https://files.readme.io/7bdbda083da16718b90246b7d915ebee2e164fa402a143e0c6cc9be95ca34dca-17387343712017.png" width="25px" /> tout à droite de la ligne de l'utilisateur.
2. Sélectionnez **Supprimer** dans le menu.

<div id="special-situations-and-additional-procedures" />

## Situations particulières et procédures complémentaires

<div id="managing-temp-roles" />

<Accordion title="Gestion des rôles provisoires">

Si votre compte utilisait précédemment notre ancien système de gestion des utilisateurs, [les rôles temporaires](/docs/user-management-for-ad-networks#les-rôles-provisoire--une-exception-à-la-règle) ont été attribués aux utilisateurs existants afin d'assurer leur transfert dans le nouveau système avec les mêmes capacités.

* Les utilisateurs avec les mêmes capacités se sont vu attribuer le même rôle provisoire.
* Utilisez les fonctionnalités de l'onglet [Rôles](/docs/user-management-for-ad-networks#onglet-rôles) pour consulter les capacités de chaque rôle provisoire, ainsi que la liste des utilisateurs avec un rôle provisoire.

<div id="temp-role-limitations" />

#### Limitations du rôle provisoire

Les rôles provisoires ont été créés uniquement pour permettre un passage en douceur depuis notre ancien système de gestion des utilisateurs. Ils ne sont donc disponibles que dans des situations précises :

* Les rôles provisoires ne peuvent pas être attribués à un autre utilisateur (nouveau ou existant).
* Un utilisateur avec un rôle provisoire ne peut pas se voir attribuer un rôle provisoire différent.
* Lorsqu'un utilisateur ayant un rôle provisoire passe à un rôle prédéfini, il ne peut pas retrouver le rôle provisoire qui lui avait été attribué précédemment (ni d’ailleurs aucun autre rôle provisoire).
* Si le dernier utilisateur avec un rôle provisoire quitte ce rôle, le rôle n'apparaîtra plus dans votre compte.

<div id="example-1" />

> 📄 **Exemple**
>
> Votre compte utilisait auparavant notre système de gestion des utilisateurs. Diana et Edward étaient des utilisateurs au moment où votre compte a été transféré vers le nouveau système. Diana a maintenant le rôle provisoire 1, et Edward le rôle provisoire 2.
>
> * Vous embauchez une nouvelle personne, Fiona. Vous pouvez attribuer Fiona au rôle d'admin ou de marketing. Toutefois, vous ne pouvez donner à Fiona ni rôle provisoire 1, ni le rôle provisoire 2.
> * Diana ne peut pas passer du rôle provisoire 1 au rôle provisoire 2. Cependant, vous pouvez lui attribuer le rôle d'admin ou de marketing.
> * Si vous transférer Diana du rôle provisoire 1 au rôle marketing, vous ne pourrez pas lui réattribuer ensuite le rôle provisoire 1.
> * Si Diana était la dernière utilisatrice du rôle provisoire 1 lorsque vous lui avez assigné le rôle marketing, le rôle provisoire 1 n'apparaîtra plus dans votre compte.

<div id="changing-the-account-owner" />

<Accordion title="Modifier le propriétaire du compte">

Comme tous les admins disposent des mêmes autorisations que le propriétaire du compte, il n'est généralement pas nécessaire de modifier le propriétaire du compte. Mais si vous devez changer le propriétaire du compte, procédez comme suit.

<div id="important-1" />

> 🚧 **Attention !**
>
> Quelques éléments à prendre en compte avant de commencer :
>
> Le changement de propriétaire du compte doit être effectué manuellement en suivant ces étapes. Il n'est pas possible de le faire depuis la page **Gestion des utilisateurs**.

<div id="1send-your-request-via-the-chat-widget" />

#### #1–Envoyez votre demande en passant par le widget de Chat

Pour lancer la procédure de changement de propriétaire du compte, ouvrez le widget de Chat <Anchor target="_blank" href="https://hq1.appsflyer.com/apps/search?openAssistant=true">en utilisant ce lien</Anchor>, ou en cliquant sur le bouton Assistance (en haut à droite de la barre de menu). Veuillez donner au Chat les informations suivantes :

* Nom du propriétaire du compte que vous souhaitez remplacer
* Nom, titre et e-mail du nouveau propriétaire du compte

<div id="2next-steps" />

#### #2-Étapes suivantes

Une fois le changement effectué, AppsFlyer vous enverra un e-mail de confirmation.

* Si vous souhaitez que l'ancien propriétaire du compte continue à utiliser votre compte AppsFlyer, <Anchor target="_blank" href="/marketers/fr/docs/user-management#creating-users">créez un nouvel utilisateur</Anchor> pour lui, et donnez-lui un nouveau rôle.
* Les API qui reposent sur le jeton v2 ne sont pas impactées par le changement de propriétaire d’un compte.  <Anchor target="_blank" href="/marketers/fr/docs/managing-appsflyer-tokens">En savoir plus sur la gestion des jetons</Anchor>.

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="Résolution du problème 'Impossible de créer cet utilisateur'.">

Si vous recevez le message d'erreur *Impossible de créer cet utilisateur* lorsque vous saisissez l'e-mail d'un nouvel utilisateur, c’est généralement que l'e-mail est déjà associé à un utilisateur AppsFlyer (soit dans votre compte, soit dans un autre). Choisissez la procédure suivant votre cas :

Si l'utilisateur fait partie de votre compte :

* Vérifiez si l'utilisateur a bien activé son compte. Si ce n'est pas le cas, vous pouvez lui [renvoyer l'invitation](/docs/user-management-for-ad-networks#resending-a-user-invitation).
* Si l'utilisateur a bien activé son compte, demandez-lui de se connecter à nouveau en utilisant l'e-mail associé à son utilisateur. Vous pouvez lui recommander de suivre les étapes du **Mot de passe oublié** si besoin est.

Si l'e-mail de l'utilisateur est utilisé dans un autre compte, ou si vous ne pouvez pas trouver le compte dans lequel l'e-mail de l'utilisateur est utilisé, effectuez l'une des opérations suivantes :

* Supprimez l’utilisateur de l'autre compte puis ajoutez-le au vôtre (vous - ou l'utilisateur - devez disposer des autorisations nécessaires dans l'autre compte) ; OU
* Ajoutez l’utilisateur à votre compte en définissant un autre e-mail. L'adresse e-mail doit être valide ; OU
* Contactez votre Responsable Réussite client (CSM), ou envoyez un e-mail à notre équipe Engagement client à [hello@appsflyer.com](mailto:hello@appsflyer.com).

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="Renvoyer une invitation à un utilisateur">

Si un nouvel utilisateur n'a pas reçu [l'invitation pour activer](/docs/user-management-for-ad-networks#devenir-un-utilisateur-actif) son compte, ou s'il n'a pas activé son compte sous 48 heures, vous pouvez lui renvoyer l'e-mail en suivant cette procédure :

1. Dans l’onglet **Utilisateurs**, cliquez sur le bouton **Actions** <Image alt="actions_icon.png" src="https://files.readme.io/7bdbda083da16718b90246b7d915ebee2e164fa402a143e0c6cc9be95ca34dca-17387343712017.png" width="25px" /> tout à droite de la ligne de l'utilisateur.
   * Notez que l'utilisateur porte toujours l’icône en forme d'enveloppe ![pending_invitation_icon.png](https://files.readme.io/1e334edd433f9ac13a175cdd48345adebe02892215896ea967768dc3cabf0349-17387375704209.png), qui indique qu'il n'a toujours pas activé son compte).
2. Sélectionnez **Renvoyer l'e-mail d’invitation** dans le menu.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="Réinitialiser l'authentification à double facteurs (2FA)">

Si votre compte utilise la 2FA, il pourra vous être demandé de réinitialiser les paramètres 2FA d'un utilisateur. Procédez comme suit :

1. Dans l’onglet **Utilisateurs**, cliquez sur le bouton **Actions** <Image alt="actions_icon.png" src="https://files.readme.io/7bdbda083da16718b90246b7d915ebee2e164fa402a143e0c6cc9be95ca34dca-17387343712017.png" width="25px" /> tout à droite de la ligne de l'utilisateur.
2. Sélectionnez **Réinitialiser la 2FA** dans le menu.

**Remarque :** Un admin peut réinitialiser la 2FA de tout autre admin autre que lui, ou celui du [propriétaire du compte](/docs/user-management-for-ad-networks#admin---un-rôle-particulier). Pour réinitialiser la 2FA du propriétaire du compte, contactez l'équipe d'assistance AppsFlyer.

</Accordion>

</Accordion>

<div data-zendesk-anchors="background=avant-de-commencer h_01HEN51924E23493MKXPEKHS03=avant-de-commencer more-about-roles=%C3%A0-propos-des-r%C3%B4les h_01HEN51924R007XNM3N45CA73A=%C3%A0-propos-des-r%C3%B4les h_01HEN51924WBY63ASRGH7ZQFP4=exemple temp-roles%E2%80%94an-exception-to-the-rule=les-r%C3%B4les-provisoire--une-exception-%C3%A0-la-r%C3%A8gle h_01HEN51924DT5GVPMJBQD3ZY9R=les-r%C3%B4les-provisoire--une-exception-%C3%A0-la-r%C3%A8gle admin%E2%80%94a-special-role=admin---un-r%C3%B4le-particulier h_01HEN51924G6GXVH8HH5DAWZ26=admin---un-r%C3%B4le-particulier user-management-page=page-de-gestion-des-utilisateurs h_01HEN51924PQEM4R974HMWPH98=page-de-gestion-des-utilisateurs users-tab=onglet-utilisateurs h_01HEN51924RDZFSJN0KN0YJFND=onglet-utilisateurs roles-tab=onglet-r%C3%B4les h_01HEN519249AHVKGM5CDTXPEP7=onglet-r%C3%B4les creating-a-user=cr%C3%A9er-un-utilisateur h_01HEN51924C56PAKQYTQM05DMV=cr%C3%A9er-un-utilisateur h_01HEN519241VD35W7AYQ08NMHJ=attention- becoming-an-active-user=devenir-un-utilisateur-actif h_01HEN51924F0G8287RP08EB464=devenir-un-utilisateur-actif editing-users=modification-des-utilisateurs 01HEPXYXV78HEXK5SD4QBDGEGH=modification-des-utilisateurs individual-editing=modification-individuelle h_01HEN51924AP4TT97C2X5CRB35=modification-individuelle multiuser-editing=modification-par-groupes h_01HEN519246HC2M4BB35GR29SQ=modification-par-groupes h_01HEN51925ZWQ8V3XJNAD4F4V9=remarque deleting-users=supprimer-des-utilisateurs h_01HEN51925Q9P2GFJWWWW9MMQ2=supprimer-des-utilisateurs special-situations-and-additional-procedures=situations-particuli%C3%A8res-et-proc%C3%A9dures-compl%C3%A9mentaires h_01HEN51925JBC3R887CVFNFA27=situations-particuli%C3%A8res-et-proc%C3%A9dures-compl%C3%A9mentaires h_01HEN519258745RNY4RNT4MWK6=managing-temp-roles temp-role-limitations=limitations-du-r%C3%B4le-provisoire h_01HEN51925REZEKBA501T0RMME=limitations-du-r%C3%B4le-provisoire h_01HEN51925FMKJ5D7BE93GVN2G=exemple-1 h_01HEN51925J3NKAJSKYEF9AMMJ=changing-the-account-owner h_01HEN51925FR6AGT1M2YHJJB6A=attention--1 1%E2%80%93send-an-email-request=1envoyez-votre-demande-en-passant-par-le-widget-de-chat h_01HEN51925GQGFAZYRTHPBBXA2=1envoyez-votre-demande-en-passant-par-le-widget-de-chat 2%E2%80%93next-steps=2-%C3%A9tapes-suivantes h_01HEN51925SPRA034581N8BWYK=2-%C3%A9tapes-suivantes troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HEN51925YAY0E37S799S7S1J=troubleshooting-can-t-create-this-user h_01HEN519253VMNBPNW61M10QZW=resending-a-user-invitation h_01HEN51925C7X1AEM2FJ6152Z1=resetting-twofactor-authentication-2fa" />
