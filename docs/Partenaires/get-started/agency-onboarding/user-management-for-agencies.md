---
title: Gestion des utilisateurs pour les agences
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
  edited_at: '2024-09-09T14:44:17Z'
  id: 4414231896337
  locale: fr
  section: Agency onboarding
  section_id: 6551110223889
  url: https://support.appsflyer.com/hc/fr/articles/4414231896337
---
> **En bref :** Créez et gérez les utilisateurs AppsFlyer de votre compte agence et attribuez-leur des autorisations d'accès aux fonctionnalités et aux apps.

## Rôles des utilisateurs et autorisations d'accès

Les comptes AppsFlyer permettent d'avoir plusieurs utilisateurs, chacun ayant des autorisations gérées individuellement. Les autorisations de chaque utilisateur sont définies en fonction de 2 dimensions principales :

* **Rôle** (capacités d'accès aux fonctionnalités et d'exécution des fonctions)
* **Accès aux apps** pour les apps actuelles et futures

Les autorisations au sein de chacune de ces dimensions sont attribuées de manière indépendante. En d'autres termes, vous pouvez attribuer à un utilisateur **un rôle** avec des capacités fonctionnelles étendues, mais lui permettre d'exercer ces capacités uniquement dans un cadre étroitement défini **d’apps**.

La seule exception est le [rôle d'admin](/docs/user-management-for-agencies#admin---un-rôle-particulier), comme indiqué ci-dessous, qui a accès à toutes les capacités et à toutes les apps.

### Rôles prédéfinis

#### hachage pour les rôles prédéfinis

Chaque utilisateur AppsFlyer d'un compte d'agence se voit attribuer l'un des 4 rôles prédéfinis :

* Admin
* Responsable d'équipe
* Marketing
* Contributeur

Chacun de ces rôles définit les fonctionnalités spécifiques d'AppsFlyer auxquelles l'utilisateur peut accéder et les fonctions qu'il peut exécuter. La liste complète des capacités accordées à chaque rôle est disponible dans l'onglet [Rôles](/docs/user-management-for-agencies#onglet-rôles) de la page **Gestion des utilisateurs**.

En règle générale, tous les rôles sont prédéfinis et les possibilités de chaque rôle sont fixes : aucun réarrangement n'est autorisé. Par contre, vous pouvez modifier les capacités d'un utilisateur à tout moment en modifiant son rôle (à l'exception du [propriétaire du compte](/docs/user-management-for-agencies#hachage-pour-le-propriétaire-du-compte), comme expliqué ci-dessous).

> 📄 **Exemple**
>
> Vous avez confié à Bill Bates le rôle de **responsable d'équipe.** Ce rôle permet à Bill de gérer les **paramètres d’app** mais ne lui permet pas d’accéder au **journal d’audit.**
>
> **Question :** Puis-je maintenir le rôle Responsable d’équipe pour Bill, tout en lui donnant en plus la possibilité d'accéder au journal d'audit ? Puis-je lui retirer la possibilité de gérer les paramètres de l'app ?
>
> **Réponse :** Non. Tant que Bill conserve le rôle Marketing, vous ne pouvez pas lui donner la possibilité d'accéder au journal d'audit. Vous ne pouvez pas non plus lui retirer la possibilité de gérer les paramètres de l'app. Bien entendu, vous pouvez donner à Bill un autre rôle prédéfini, et ses capacités seront celles qu’autorise ce nouveau rôle.

### Les rôles temporaire : une exception à la règle

Si votre compte AppsFlyer existait dans notre ancien système de gestion des utilisateurs (lorsque les seuls types de comptes disponibles étaient Admin et Membre d'équipe), tous les utilisateurs ont été envoyés dans le nouveau système avec les mêmes autorisations. Par conséquent, la plupart de ces utilisateurs apparaissent dans le système actuel avec des **rôles temporaire**.

En savoir plus sur la [gestion des rôles temporaires.](/docs/user-management-for-agencies#managing-temp-roles)

### Admin - un rôle particulier

Un compte AppsFlyer peut avoir **un ou plusieurs** admins, mais il doit forcément en avoir au moins un. Ce rôle particulier a plusieurs caractéristiques uniques :

* Le rôle d'admin permet d'accéder à **toutes les fonctionnalités du compte**, notamment :
  * Toutes les caractéristiques et fonctions
  * Toutes les applications actuelles et futures
  * Toutes les sources média et zones géoCette particularité qui donne un accès illimité au rôle d'admin ne peut être ni modifiée, ni réduite.

  #### Hachage pour le propriétaire du compte
* L'utilisateur créé au moment de l'ouverture du compte (**le propriétaire du compte**) se voit attribuer par défaut le rôle d'admin.
  * Le propriétaire du compte ne peut pas être supprimé, retiré du rôle d'admin ou modifié d'une autre manière à partir de la page [**Gestion des utilisateurs**](/docs/user-management-for-agencies#page-de-gestion-des-utilisateurs). De même, l'e-mail du propriétaire du compte ne peut pas être modifié.
    * Si vous devez changer le propriétaire du compte, suivez les étapes [indiquées ci-dessous](/docs/user-management-for-agencies#changing-the-account-owner).
  * Le propriétaire du compte est en premier lieu celui qui crée de nouveaux utilisateurs (jusqu'à ce que des utilisateurs disposant de capacités de gestion des utilisateurs soient créés).
* Seul un utilisateur ayant un rôle d'admin peut <Anchor target="_blank" href="/marketers/fr/docs/managing-appsflyer-tokens">gérer les jetons API et S2S.</Anchor>
* Tout admin autre que le propriétaire du compte **peut** se voir attribuer un autre rôle, ou être supprimé du compte AppsFlyer via la page de gestion des utilisateurs.

## Page de gestion des utilisateurs

**Pour accéder à la page de gestion des utilisateurs :**

1. Dans la barre de menu supérieure, cliquez, ouvrez le menu du compte (liste déroulante de l'adresse e-mail).
2. Sélectionnez **Gestion des utilisateurs.**

### Onglet Utilisateurs

L'onglet **Utilisateurs** affiche un tableau de tous les utilisateurs existants dans votre compte. C'est le point de départ de la création, de la gestion et de la suppression des utilisateurs.

* Cliquez sur le titre de colonne **Utilisateurs** pour trier le tableau par ordre alphabétique (croissant/décroissant).
* Utilisez le champ de recherche pour trouver et afficher des utilisateurs spécifiques.
* Cliquez sur l'icône de filtre <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> dans l'en-tête de la colonne **Rôle** pour filtrer les utilisateurs par rôle (y compris les rôles temporaires).
  * Pour supprimer le filtre, sélectionnez **Aucun** dans la liste déroulante du filtre.
* Utilisez les cases à cocher pour sélectionner et [modifier plusieurs utilisateurs](/docs/user-management-for-agencies#modification-par-groupes) en même temps.

### Onglet Rôles

L'onglet **Rôles** affiche une liste de tous les rôles définis dans votre compte, notamment :

* Les 4 [rôles prédéfinis](#rôles-prédéfinis)
* Tous les [Rôles temporaires](/docs/user-management-for-agencies#les-rôles-temporaire--une-exception-à-la-règle) en cours pour les utilisateurs

Cliquez sur le nom de n’importe quel rôle dans le panneau de gauche pour voir :

* Détails complets sur les capacités du rôle
* Le nombre d'utilisateurs actuellement affectés à ce rôle (en haut à droite de l'écran)
  * Passez la souris sur l'icône Utilisateur <Image alt="user_icon.png" src="https://files.readme.io/afd47a11e82e0cfac3240fe39582bd141639465952f6eef76bcf1f6e7532d6a9-16162513473937.png" width="21px" /> pour voir la liste des 20 premiers utilisateurs.

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

   > 🚧 **Attention !**
   >
   > L'e-mail d'un utilisateur est ce qui permet de l'identifier sur la plateforme AppsFlyer :
   >
   > * Il sera impossible de le modifier ultérieurement : vous devrez supprimer et recréer l'utilisateur.
   > * L'adresse e-mail doit être valide, l’utilisateur doit pouvoir accéder à la boîte de réception.
   > * Elle ne doit pas être associée à un autre utilisateur dans un autre compte AppsFlyer.
   >   * Si l'e-mail est déjà utilisé (dans votre compte ou dans un autre), le message suivant s'affiche : *Impossible de créer cet utilisateur.* Suivez les [étapes de dépannage ci-dessous](/docs/user-management-for-agencies#troubleshooting-can-t-create-this-user) pour résoudre le problème.

4. Sélectionnez le département de l'utilisateur (facultatif).
5. Sélectionnez le rôle de l'utilisateur (obligatoire).
6. Sélectionnez les applications auxquelles l'utilisateur peut accéder :
   * Le paramètre par défaut permet d'accéder à toutes les apps actuelles et futures du compte. Pour modifier ce paramètre, utilisez les cases à cocher pour sélectionner et désélectionner les applications.
   * Un utilisateur ne peut avoir accès à toutes les applications futures que s'il a accès à toutes les applications actuelles.
7. Cliquez sur **Enregistrer** pour créer l'utilisateur.

   * L'utilisateur reçoit un e-mail l'invitant à activer son compte.

   #### hachage pour activation du compte

   * L'utilisateur s'affiche dans le tableau des utilisateurs. L'icône de l'enveloppe ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png) indique qu'une invitation a été envoyée et que le compte est en attente d'activation. Une fois que l'utilisateur aura activé son compte, l'enveloppe disparaîtra.
   * Le lien d'activation envoyé à l'utilisateur est valable pendant 48 heures. Si l'utilisateur ne reçoit pas l'invitation ou si le lien expire, vous pouvez [renvoyer l'invitation](/docs/user-management-for-agencies#resending-a-user-invitation).

## Modification des utilisateurs

Les utilisateurs peuvent être modifiés un par un, ou par groupes.

### Modification individuelle

**Pour modifier un seul utilisateur :**

1. Dans l’onglet **Utilisateurs**, cliquez sur le bouton **Actions** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> tout à droite de la ligne de l'utilisateur.
2. Sélectionnez **Modifier** dans le menu.
3. Modifiez les paramètres de l'utilisateur.
4. Tous les paramètres en dehors de l'adresse e-mail sont modifiables.
5. Cliquez sur **Enregistrer**.

### Modification par groupes

La modification par groupes est idéale pour modifier les autorisations de compte de plusieurs utilisateurs en même temps. Cette fonction associée au filtrage dans l'onglet **Utilisateurs** peut s'avérer particulièrement utile pour la gestion d'un grand nombre d'utilisateurs.

> 📘 **Remarque**
>
> Vous ne pouvez pas supprimer des utilisateurs ou les affecter au rôle d'admin en utilisant la modification par groupes.

**Pour modifier plusieurs utilisateurs :**

1. Dans l'onglet **Utilisateurs**, cochez l'utilisateur ou les utilisateurs que vous souhaitez modifier.
   * Cochez la case du titre de colonne pour sélectionner tous les utilisateurs visibles.
   * Le nombre d'utilisateurs sélectionnés s'affiche à droite de la boîte de recherche. Notez que le [propriétaire du compte](/docs/user-management-for-agencies#hachage-pour-le-propriétaire-du-compte) ne peut pas être sélectionné, il n'est donc pas inclus dans le nombre d'utilisateurs sélectionnés.
2. Les boutons **Rôle** et **Apps** sont affichés en haut à droite du tableau.
   * Si un ou plusieurs des utilisateurs sélectionnés ont accès aux applications futures, le bouton **Apps** n'est pas disponible (voir [Limitations du rôle temporaire](/docs/user-management-for-agencies#limitations-du-rôle-temporaire) ci-dessous).
3. Cliquez sur le bouton correspondant aux autorisations que vous souhaitez modifier.
4. Effectuez les modifications nécessaires à l'aide de la boîte de dialogue ou des listes déroulantes qui s'affichent.
   * N'oubliez pas que vos modifications s'appliquent à tous les utilisateurs sélectionnés !
5. Les utilisateurs modifiés s’affichent surlignés dans le tableau, et tels qu'ils seront une fois les modifications enregistrées. Cependant, vous aurez toujours la possibilité de revoir vos modifications et de les confirmer ou les annuler à l'étape suivante.
6. Vérifiez vos modifications. Cliquez sur **Sauvegarder** ou sur **Annuler**.

> 📄 **Exemple**
>
> **Scénario :**
>
> * Votre compte inclut 10 utilisateurs. Six d'entre eux occupent le rôle **Marketing**.
> * Alice, Bill et Charlie viennent d'être promus et vous souhaitez les faire passer du rôle **Marketing - limité** au rôle Responsable d’équipe.
> * Alice travaillera avec l'application Astounding. Bill travaillera avec l'application Beautiful. Charlie travaillera avec l'application Charming.
>
> **Étapes :**
>
> 1. Utilisez le filtre de rôle <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> pour ne voir que les utilisateurs ayant le rôle **Marketing**.
> 2. Faites passer Alice, Bill et Charlie au rôle de **responsable d'équipe**:
>    * Cochez les cases pour Alice, Bill et Charlie.
>    * Cliquez sur le bouton **Rôle**.
>    * Sélectionnez **Responsable d'équipe** dans la liste déroulante.
>    * Cliquez sur **Enregistrer** pour confirmer.
>    * Notez qu'une fois les modifications confirmées, le filtre **Rôle** est supprimé et le tableau affiche tous les utilisateurs.
> 3. Donnez à Alice, Bill et Charlie l'accès à l'app appropriée :
>    * Utilisez la boîte de recherche pour trouver Alice, puis modifiez individuellement son utilisateur pour lui donner accès à l'app Astounding.
>    * Répétez ces étapes pour Bill et Charlie afin de leur donner accès à Beautiful et Charming, respectivement.

## Supprimer des utilisateurs

**Pour supprimer un utilisateur :**

1. Dans l’onglet **Utilisateurs**, cliquez sur le bouton **Actions** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> tout à droite de la ligne de l'utilisateur.
2. Sélectionnez **Supprimer** dans le menu.

## Situations particulières et procédures complémentaires

<div id="managing-temp-roles" />

<Accordion title="Gestion des rôles temporaires">

Si votre compte utilisait précédemment notre ancien système de gestion des utilisateurs, [**les rôles temporaires**](/docs/user-management-for-agencies#les-rôles-temporaire--une-exception-à-la-règle) ont été attribués aux utilisateurs existants afin d'assurer leur transfert dans le nouveau système avec les mêmes capacités.

* Les utilisateurs avec les mêmes capacités se sont vu attribuer le même rôle temporaire.
* Utilisez les fonctionnalités de l'onglet [Rôles](/docs/user-management-for-agencies#onglet-rôles) pour consulter les capacités de chaque rôle temporaire, ainsi que la liste des utilisateurs avec un rôle temporaire.

#### Limitations du rôle temporaire

Les rôles temporaires ont été créés uniquement pour permettre un passage en douceur depuis notre ancien système de gestion des utilisateurs. Ils ne sont donc disponibles que dans des situations précises :

* Les rôles temporaires ne peuvent pas être attribués à un autre utilisateur (nouveau ou existant).
* Un utilisateur ayant un rôle temporaire ne peut pas se voir attribuer un autre rôle temporaire (mais vous pouvez modifier les apps auxquelles il a accès).
  * Notez que l'accès d'un utilisateur aux futures apps **ne peut pas** être modifié lorsque l'utilisateur a un rôle temporaire.
* Lorsqu'un utilisateur ayant un rôle temporaire passe à un rôle prédéfini, il ne peut pas retrouver le rôle temporaire qui lui avait été attribué précédemment (ni d’ailleurs aucun autre rôle temporaire).
* Si le dernier utilisateur avec un rôle temporaire quitte ce rôle, le rôle n'apparaîtra plus dans votre compte.

> 📄 **Exemple**
>
> Votre compte utilisait auparavant notre système de gestion des utilisateurs. Diana et Edward étaient des utilisateurs au moment où votre compte a été transféré vers le nouveau système. Diana a maintenant le rôle temporaire 1, et Edward le rôle temporaire 2.
>
> * Vous embauchez une nouvelle personne, Fiona. Vous pouvez attribuer à Fiona l'un des 4 [rôles prédéfinis](#rôles-prédéfinis). Toutefois, vous ne pouvez pas attribuer à Fiona le rôle temporaire 1 ou le rôle temporaire 2.
> * Diana ne peut pas passer du rôle temporaire 1 au rôle temporaire 2. Cependant, vous pouvez lui attribuer n'importe lequel des 4 rôles prédéfinis. Vous pouvez également modifier son accès à l'app si nécessaire.
> * Si vous transférez Diana du rôle temporaire 1 au rôle Marketing, vous ne pourrez pas lui réattribuer ensuite le rôle temporaire 1.
> * Si Diana était le dernier utilisateur dans le rôle temporaire 1 lorsque vous l'avez transférée dans le rôle de responsable d'équipe, le rôle temporaire 1 n'apparaîtra plus dans votre compte.

</Accordion>

<div id="changing-the-account-owner" />

<Accordion title="Modifier le propriétaire du compte">

Comme tous les admins disposent des mêmes autorisations que le propriétaire du compte, il n'est généralement pas nécessaire de modifier le propriétaire du compte. Mais si vous devez changer le propriétaire du compte, procédez comme suit.

> 🚧 **Attention !**
>
> Quelques éléments à prendre en compte avant de commencer :
>
> * Si vous utilisez encore les API Pull, Master ou GDPR avec le jeton v1, le changement de propriétaire du compte réinitialise automatiquement ces services. Pour éviter toute perte de données, <Anchor target="_blank" href="/marketers/fr/docs/bulletin-api-token-changes">commencez à utiliser ces API avec le jeton v2</Anchor> **avant de changer le propriétaire du compte**.
> * Le changement de propriétaire du compte doit être effectué manuellement en suivant ces étapes. Il n'est pas possible de le faire depuis la page **Gestion des utilisateurs**.

#### #1–Envoyez votre demande en passant par le widget de Chat

Pour commencer la procédure de changement de propriétaire du compte, ouvrez le widget de chat <Anchor target="_blank" href="https://hq1.appsflyer.com/apps/search?openAssistant=true">en utilisant ce lien</Anchor> ou en cliquant sur le bouton Aide dans la barre de menu supérieure. Veuillez donner au Chat les informations suivantes :

* Nom du propriétaire du compte que vous souhaitez remplacer
* Nom, titre et e-mail du nouveau propriétaire du compte

#### #2-Étapes suivantes

Une fois le changement effectué, AppsFlyer vous enverra un e-mail de confirmation.

* Si vous souhaitez que l'ancien propriétaire du compte continue à utiliser votre compte AppsFlyer, <Anchor target="_blank" href="/marketers/fr/docs/user-management#creating-users">créez un nouvel utilisateur</Anchor> pour lui, et donnez-lui un nouveau rôle.
* Les API qui reposent sur le jeton v2 ne sont pas impactées par le changement de propriétaire d’un compte. <Anchor target="_blank" href="/marketers/fr/docs/managing-appsflyer-tokens">En savoir plus sur la gestion des jetons</Anchor>.

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="Résolution du problème « Impossible de créer cet utilisateur ».">

Si vous recevez le message d'erreur *Impossible de créer cet utilisateur* lorsque vous saisissez l'e-mail d'un nouvel utilisateur, c’est généralement que l'e-mail est déjà associé à un utilisateur AppsFlyer (soit dans votre compte, soit dans un autre). Choisissez la procédure suivant votre cas :

Si l'utilisateur fait partie de votre compte :

* Vérifiez si l'utilisateur a bien activé son compte. Si ce n'est pas le cas, vous pouvez lui [renvoyer l'invitation](/docs/user-management-for-agencies#resending-a-user-invitation).
* Si l'utilisateur a bien activé son compte, demandez-lui de se connecter à nouveau en utilisant l'e-mail associé à son utilisateur. Vous pouvez lui recommander de suivre les étapes du **Mot de passe oublié** si besoin est.

Si l'e-mail de l'utilisateur est utilisé dans un autre compte, ou si vous ne pouvez pas trouver le compte dans lequel l'e-mail de l'utilisateur est utilisé, effectuez l'une des opérations suivantes :

* Supprimez l’utilisateur de l'autre compte puis ajoutez-le au vôtre (vous - ou l'utilisateur - devez disposer des autorisations nécessaires dans l'autre compte) ; ou
* Ajoutez l’utilisateur à votre compte en définissant un autre e-mail. L'adresse e-mail doit être valide ; ou
* Contactez votre Responsable Réussite client (CSM), ou envoyez un e-mail à notre équipe Engagement client à [hello@appsflyer.com](mailto:hello@appsflyer.com).

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="Renvoyer une invitation à un utilisateur">

Si un nouvel utilisateur n'a pas reçu [l'invitation pour activer](/docs/user-management-for-agencies#hachage-pour-activation-du-compte) son compte, ou s'il n'a pas activé son compte sous 48 heures, vous pouvez lui renvoyer l'e-mail en suivant cette procédure :

1. Dans l’onglet **Utilisateurs**, cliquez sur le bouton **Actions** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> tout à droite de la ligne de l'utilisateur.
   * Notez que l'utilisateur porte toujours l’icône en forme d'enveloppe ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png), qui indique qu'il n'a toujours pas activé son compte).
2. Sélectionnez **Renvoyer l'e-mail d’invitation** dans le menu.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="Réinitialisation de l'authentification à deux facteurs (2FA) d'un utilisateur">

Pour les comptes utilisant la technologie 2FA, il peut arriver que vous deviez réinitialiser le 2FA d'un utilisateur. Voir <Anchor target="_blank" href="/marketers/fr/docs/implementing-and-using-2fa-login#reset">ici</Anchor> comment procéder.

</Accordion>

<div data-zendesk-anchors="background=r%C3%B4les-des-utilisateurs-et-autorisations-dacc%C3%A8s h_01HC72J0H988V27YCTWPFGF7EP=r%C3%B4les-des-utilisateurs-et-autorisations-dacc%C3%A8s predefined-roles=r%C3%B4les-pr%C3%A9d%C3%A9finis h_01HC72J0H98447W34RD0ND2MC0=r%C3%B4les-pr%C3%A9d%C3%A9finis predefined-roles-hash=hachage-pour-les-r%C3%B4les-pr%C3%A9d%C3%A9finis h_01HC72J0H9RVA83J9F5QN4YS79=hachage-pour-les-r%C3%B4les-pr%C3%A9d%C3%A9finis h_01HC72J0H9Y54Q2Y6AGP6H1DG0=exemple temp-roles%E2%80%94an-exception-to-the-rule=les-r%C3%B4les-temporaire--une-exception-%C3%A0-la-r%C3%A8gle h_01HC72J0H9NXMKJN64C73ZXZN1=les-r%C3%B4les-temporaire--une-exception-%C3%A0-la-r%C3%A8gle admin%E2%80%94a-special-role=admin---un-r%C3%B4le-particulier h_01HC72J0HANGXV4GVJCQ5X2T84=admin---un-r%C3%B4le-particulier account-owner-hash=hachage-pour-le-propri%C3%A9taire-du-compte h_01HC72J0HA5RFZE1G0KNKR30KV=hachage-pour-le-propri%C3%A9taire-du-compte user-management-page=page-de-gestion-des-utilisateurs h_01HC72J0HANQ3Z6FCWXA0TF3TN=page-de-gestion-des-utilisateurs users-tab=onglet-utilisateurs h_01HC72J0HAFBMYM792GXMCEY3T=onglet-utilisateurs roles-tab=onglet-r%C3%B4les h_01HC72J0HAXC2NAVQC4J2PMB0Z=onglet-r%C3%B4les creating-a-user=cr%C3%A9er-un-utilisateur h_01HC72J0HATN656W4B9DT82M60=cr%C3%A9er-un-utilisateur h_01HC72J0HAP1GDH8JKGMT6XH67=attention- account-activation-hash=hachage-pour-activation-du-compte h_01HC72J0HA3QJ2CH8TGEMJBY3A=hachage-pour-activation-du-compte editing-users=modification-des-utilisateurs h_01HC72J0HAG2XF42NSYRZDEKVN=modification-des-utilisateurs individual-editing=modification-individuelle h_01HC72J0HAF739MQPF482T0WVA=modification-individuelle multiuser-editing=modification-par-groupes h_01HC72J0HA3BKXJCAVRQ5SJYYE=modification-par-groupes h_01HC72J0HAZM2NBXN5ZHZET4BS=remarque h_01HC72J0HAE70AMWSDP5BXGWK9=exemple-1 deleting-users=supprimer-des-utilisateurs h_01HC72J0HAQFD33VT0ARRWG0ZF=supprimer-des-utilisateurs special-situations-and-additional-procedures=situations-particuli%C3%A8res-et-proc%C3%A9dures-compl%C3%A9mentaires h_01HC72J0HAF5QFC5ZR7EHFMBM6=situations-particuli%C3%A8res-et-proc%C3%A9dures-compl%C3%A9mentaires h_01HC72J0HAD8JXPPFET4N2P3EK=managing-temp-roles temp-role-limitations=limitations-du-r%C3%B4le-temporaire h_01HC72J0HA8PP79VV1F03E5AXV=limitations-du-r%C3%B4le-temporaire h_01HC72J0HAJES0N195DZ797C4V=exemple-2 h_01HC72J0HAVXK83AK99NQVDT8T=changing-the-account-owner h_01HC72J0HANXBK4T1SD6V2KHE4=attention--1 1%E2%80%93send-an-email-request=1envoyez-votre-demande-en-passant-par-le-widget-de-chat h_01HC72J0HAJ3C8WJ767KG2307C=1envoyez-votre-demande-en-passant-par-le-widget-de-chat 2%E2%80%93next-steps=2-%C3%A9tapes-suivantes h_01HC72J0HAM13NY9EKNKG8R1CA=2-%C3%A9tapes-suivantes troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HC72J0HAWRBVWGVT12W6M711=troubleshooting-can-t-create-this-user h_01HC72J0HANPD39FRCWSPMRY5D=resending-a-user-invitation h_01HC72J0HARYRSXHKX41A41MPG=resetting-twofactor-authentication-2fa" />
