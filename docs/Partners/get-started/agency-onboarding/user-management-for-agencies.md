---
title: User management for agencies
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
  edited_at: '2024-01-04T11:08:46Z'
  id: 4414231896337
  locale: en-us
  section: Agency onboarding
  section_id: 6551110223889
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/4414231896337-User-management-for-agencies
---
**At a glance:** Create and manage your agency account's AppsFlyer users, and assign them permissions to access features and apps.

## User roles and access permissions

AppsFlyer accounts allow for multiple users, each with individually-managed permissions. Each user’s permissions are defined along 2 primary dimensions:

* **Role** (capabilities to access features and perform functions)
* **App access** for current and future apps

Permissions within each of these dimensions are assigned independently. In other words, you may assign a user a **role** with broad functional capabilities but allow them to exercise those capabilities only within a narrowly-defined set of **apps.**

The only exception is the [Admin role](/docs/user-management-for-agencies#admina-special-role), as discussed below, which has access to all capabilities and apps.

### Predefined roles

#### predefined roles hash

Each AppsFlyer user of an agency account is assigned one of 4 predefined roles:

* Admin
* Team manager
* Marketing
* Contributor

Each of these roles defines the specific AppsFlyer features the user can access and the functions they can perform. A full list of capabilities per role is available on the [Roles tab](/docs/user-management-for-agencies#roles-tab) of the **User management** page.

As a general rule, all roles are predefined, and each role’s functional capabilities are fixed: no "mixing and matching" allowed. However, you can change a user’s functional capabilities at any time by changing their role (except for the [account owner](/docs/user-management-for-agencies#account-owner-hash), as discussed below).

> 📄 **Example**
>
> You have assigned Bill Bates the role of **Team manager.** This role gives Bill the ability to manage **App settings** but does not allow him access to the **Audit log.**
>
> **Question:** Can I keep Bill in the Team manager role but also give him the ability to access the Audit log? Can I take away his ability to manage App settings?
>
> **Answer:** No. As long as Bill stays in the Team manager role, you cannot give him the ability to access the Audit log. Nor can you remove his ability to manage App settings. Of course, you can assign Bill to a different role, and his capabilities will change to those defined by that role.

### Temp roles—an exception to the rule

If your AppsFlyer account existed under our prior user management system (when the only available account types were Admin and Team member), all users were brought into the new system with unchanged capabilities. As a result, most of these users appear in the current system with **temp roles**.

Learn more about [managing temp roles](/docs/user-management-for-agencies#managing-temp-roles).

### Admin—a special role

An AppsFlyer account can have **one or more** Admins, but every account has at least one. This special role has several unique characteristics:

* The Admin role has access to **all** account capabilities, including:
  * All features and functions
  * All current and future apps
  * All media sources and geosThis "all-access" characteristic of the Admin role cannot be changed or limited.

  #### account owner hash
* The user created at the time the account was opened (the **"account owner"**) is assigned the Admin role by default.
  * The account owner cannot be deleted, removed from the Admin role, or otherwise edited from the [**User management**](/docs/user-management-for-agencies#user-management-page) page. Likewise, the account owner’s email address cannot be changed.
    * If you do need to change the account owner, follow the [steps listed below](/docs/user-management-for-agencies#changing-the-account-owner).
  * The account owner is initially responsible for creating additional users (until additional users with user management capabilities are created).
* Only a user with an admin role can <Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">manage API and S2S tokens</Anchor>.
* Any Admin other than the account owner **can** be changed to a different role or deleted from the AppsFlyer account through the User management page.

## User management page

**To access the User management page:**

1. In the top menu bar, click, open the account menu (email address dropdown).
2. Select **User management.**

### Users tab

The **Users** tab displays a table of all existing users in your account. It is the starting point for creating, managing, and deleting users.

* Click the **User** column heading to sort the table alphabetically (ascending/descending).
* Use the search box to find and display specific users.
* Click the filter icon <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> in the **Role** column heading to filter users by their role (including temp roles).
  * To clear the filter, select **None** in the filter dropdown list.
* Use the checkboxes to select and [edit multiple users](/docs/user-management-for-agencies#multi-user-editing) at the same time.

### Roles tab

The **Roles** tab displays a list of all roles defined in your account, including:

* The 4 [predefined roles](#predefined-roles)
* Any [temp roles](/docs/user-management-for-agencies#temp-rolesan-exception-to-the-rule) currently assigned to users

Click on the name of any role in the left panel to see:

* Full details of the role’s capabilities
* The number of users currently assigned that role (in the top-right corner of the screen)
  * Hover over the user icon <Image alt="user_icon.png" src="https://files.readme.io/afd47a11e82e0cfac3240fe39582bd141639465952f6eef76bcf1f6e7532d6a9-16162513473937.png" width="21px" /> to see a list of the first 20.

## Creating a user

**To create a new user:**

1. On the **Users** tab, click the **New user** button.
2. Enter the user’s name (required):
   * Can include letters, numbers, spaces, periods (.), hyphens (-), underscores (\_), and single (') or double (") quotation marks.
   * Other special characters are not allowed.
3. Enter the user’s email address (required):
   * Can include letters, numbers, apostrophes ('), ampersands (&), dollar signs ($), hash symbols (#), hyphens (-), underscores (\_), and periods (.)
   * Two consecutive periods (..) and other special characters are not allowed.
   * Must end with a valid email domain.

   > 🚧 **Important!**
   >
   > A user’s email address is what identifies them in the AppsFlyer platform, meaning:
   >
   > * It cannot later be changed without deleting and recreating the user.
   > * It must be a valid email address at which the user can receive email.
   > * It cannot be associated with another user in any AppsFlyer account.
   >   * If the email address is already in use (either in your account or a different one), you will see the message *Can't create this user.* Follow the [troubleshooting steps below](/docs/user-management-for-agencies#troubleshooting-can-t-create-this-user) to resolve this issue.

4. Select the user’s department (optional).
5. Select the user’s role (required).
6. Select the apps the user can access:
   * The default setting allows access to all current and future apps in the account. To change this setting, use the checkboxes to select and deselect apps.
   * A user can be given access to all future apps only if they have access to all current apps.
7. Click **Save** to create the user.

   * The user is sent an email invitation to activate their account.

   #### account activation hash

   * The user is displayed in the user table. The envelope icon ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png) indicates that an invitation has been sent and the account is awaiting activation. Once the user activates their account, the envelope will disappear.
   * The activation link sent to the user is valid for 48 hours. If the user didn’t receive the invitation or if the link has expired, you can [resend the invitation](/docs/user-management-for-agencies#resending-a-user-invitation).

## Editing users

Users can be edited either one at a time or in groups.

### Individual editing

**To edit an individual user:**

1. On the **Users** tab, click the **Actions** <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> button on the far-right side of the user’s row.
2. Select **Edit** from the menu.
3. Edit user settings as required.
4. All settings other than email address are editable.
5. Click **Save**.

### Multi-user editing

Multi-user editing is an efficient way to change the account permissions of several users at one time. Using this feature in combination with the search and filtering capabilities of the **Users** tab can make it particularly helpful for managing large numbers of users.

> 📘 **Note**
>
> You cannot delete users or assign them to the Admin role using multi-user editing.

**To edit multiple users:**

1. On the **Users** tab, select the checkboxes of the user or users you want to edit.
   * Select the checkbox in the column heading to select all visible users.
   * The number of currently-selected users is displayed on the right side of the search box. Note that the [account owner](/docs/user-management-for-agencies#account-owner-hash) cannot be selected and is not included in the number of selected users.
2. The **Role** and **Apps** buttons are displayed at the top-right of the table.
   * If one or more of the selected users has access to future apps, the **Apps** button is not available. (See [Temp role limitations](/docs/user-management-for-agencies#temp-role-limitations), below.)
3. Click the button for the permissions you want to change.
4. Make the necessary changes using the dialog box or dropdown lists that are displayed.
   * Remember that your changes apply to all selected users!
5. The edited users are highlighted in the table, and the users appear as they will once the changes are saved. However, you still have the opportunity to review your changes and confirm or cancel them in the next step.
6. Review your changes. Click **Save** to confirm or **Cancel** to undo them.

> 📄 **Example**
>
> **Scenario:**
>
> * There are 10 users in your account. Six of these are in the **Marketing** role.
> * Alice, Bill, and Charlie have just received promotions, and you want to change them from the **Marketing** role to the **Team manager** role.
> * Alice will be working with the Astounding app. Bill will be working with the Beautiful app. Charlie will be working with the Charming app.
>
> **Steps:**
>
> 1. Use the Role filter <Image alt="filter_icon.png" src="https://files.readme.io/1ceaac3efead3a218909988be1d50a2f0af93b07360f7197cd398b11d661992b-16162502598417.png" width="25px" /> to see only the users in the **Marketing** role.
> 2. Change Alice, Bill, and Charlie to the **Team manager** role:
>    * Select the checkboxes for Alice, Bill, and Charlie.
>    * Click the **Role** button.
>    * Select **Team manager** from the dropdown list.
>    * Click **Save** to confirm.
>    * Note that once you confirm the changes, the **Role** filter is cleared, and the table displays all users.
> 3. Give Alice, Bill, and Charlie the appropriate app access:
>    * Use the search box to find Alice, then individually edit her user to give her access to the Astounding app.
>    * Repeat these steps for Bill and Charlie to give them access to Beautiful and Charming, respectively.

## Deleting users

**To delete a user:**

1. On the **Users** tab, click the **Actions** button <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> on the far-right side of the user’s row.
2. Select **Delete** from the menu.

## Special situations and additional procedures

<div id="managing-temp-roles" />

<Accordion title="Managing temp roles">

If your account previously used our prior user management system, [**temp roles**](/docs/user-management-for-agencies#temp-rolesan-exception-to-the-rule) were assigned to existing users to ensure that they were brought into the new system with unchanged capabilities.

* Users with the same capabilities were assigned the same temp role.
* Use the features of the [Roles tab](/docs/user-management-for-agencies#roles-tab) to review the capabilities of each temp role and a list of users currently in it.

#### Temp role limitations

Temp roles were designed specifically to allow seamless transition from our prior user management system. As such, they are available only in limited situations:

* Temp roles cannot be assigned to other users (whether new or existing).
* A user with a temp role cannot be assigned a different temp role (though you can change the apps to which they have access).
  * Note that a user's access to future apps **cannot** be changed while the user is in a temp role.
* When a user with a temp role is changed to a predefined role, they cannot be returned to the previously-assigned temp role (or to any other temp role).
* If the last user in a temp role is removed from it, the role will no longer appear in your account.

> 📄 **Example**
>
> Your account previously used our prior user management system. Diana and Edward were existing users at the time your account was moved to the new system. Diana is now in Temp role 1, and Edward is in Temp role 2.
>
> * You hire a new employee, Fiona. You can assign Fiona any one of the 4 [predefined roles](#predefined-roles). However, you cannot assign Fiona Temp role 1 or Temp role 2.
> * Diana cannot be moved from Temp role 1 to Temp role 2. However, you can assign her any of the 4 predefined roles. You can also change her app access as necessary.
> * If you move Diana from Temp role 1 to the Team manager role, she can’t later be moved back to Temp role 1.
> * If Diana was the last user in Temp role 1 when you moved her to the Team manager role, Temp role 1 will no longer appear in your account.

</Accordion>

<div id="changing-the-account-owner" />

<Accordion title="Changing the account owner">

Because all Admins have the same permissions as the account owner, changing the account owner is not usually necessary. But if you find that you must change the account owner, follow these steps to do so.

> 🚧 **Important!**
>
> A few things to consider before you begin:
>
> * If you're still using Pull, Master, or GDPR APIs with token v1, changing the account owner automatically resets these services. To avoid data loss, <Anchor target="_blank" href="/marketers/docs/bulletin-api-token-changes">transition to start using these APIs with token v2</Anchor> **before changing the account owner**.
> * Changing the account owner must be completed manually according to these steps. It cannot be done from the **User management** page.

#### #1–Send your request via the chat widget

To begin the process of changing the account owner, open the chat widget <Anchor target="_blank" href="https://hq1.appsflyer.com/apps/search?openAssistant=true">using this link</Anchor> or by clicking the Help button in the top menu bar. Include the following information in the chat:

* Name of the account owner you would like to replace
* Name, title, and email of the new account owner

#### #2–Next steps

Once the change has been processed, you will receive an email notification from AppsFlyer.

* If you want the prior account owner to continue using your AppsFlyer account, <Anchor target="_blank" href="/marketers/docs/user-management#creating-users">create a new user</Anchor> for them and assign them a new role.
* APIs using token v2 aren't affected by changing the account owner. <Anchor target="_blank" href="/marketers/docs/managing-appsflyer-tokens">Learn more about managing tokens</Anchor>.

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="Troubleshooting 'Can’t create this user'">

If you receive the error message *Can’t create this user* when entering the email address of a new user, it generally means that the email is already associated with an AppsFlyer user (either in your account or a different one). Follow the steps relevant to your situation:

If the user is in your account:

* Check to see if the user has activated their account. If not, [resend the invitation](/docs/user-management-for-agencies#resending-a-user-invitation) if required.
* If the user has activated their account, ask them to try to log in again using the email address associated with their user. Advise them to follow the **Forgot password** steps if required.

If the user’s email is used in a different account or you can’t determine the account in which the user’s email is used, select one of the following options:

* Delete them from the other account and add them to yours (requires that either you or the user has the required permissions in the other account); or
* Add them to your account using a different email address. This must be a valid email address at which they can actually receive an email; or
* Contact your Customer Success Manager (CSM) or send an email to our Customer Engagement team at [hello@appsflyer.com](mailto:hello@appsflyer.com).

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="Resending a user invitation">

If a new user did not receive their [account activation invitation](/docs/user-management-for-agencies#account-activation-hash) or if they did not activate within 48 hours, you can resend the email as follows:

1. On the **Users** tab, click the **Actions** button <Image alt="actions_icon.png" src="https://files.readme.io/24ad987d1e77d9dfa8559a370733a7b62a6d86954ec1d552eac9c406445ed927-16162502616593.png" width="25px" /> on the far-right side of the user’s row.
   * Note that the user is still shown with an envelope icon ![pending_invitation_icon.png](https://files.readme.io/68ac08ab6e52191a592350f82996f7ade9d181773d0bdbc6e2cb60315b60a8f2-16162502609553.png), indicating that they have not yet activated their account).
2. Select **Resend email invite** from the menu.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="Resetting two-factor authentication (2FA) of a user">

For accounts using a 2FA, there may be occasions on which you need to reset a user’s 2FA. See <Anchor target="_blank" href="/marketers/docs/implementing-and-using-2fa-login#reset">here</Anchor> how to do this.

</Accordion>

<div data-zendesk-anchors="background=user-roles-and-access-permissions h_01HC72J0H988V27YCTWPFGF7EP=user-roles-and-access-permissions h_01HC72J0H98447W34RD0ND2MC0=predefined-roles h_01HC72J0H9RVA83J9F5QN4YS79=predefined-roles-hash h_01HC72J0H9Y54Q2Y6AGP6H1DG0=example temp-roles%E2%80%94an-exception-to-the-rule=temp-rolesan-exception-to-the-rule h_01HC72J0H9NXMKJN64C73ZXZN1=temp-rolesan-exception-to-the-rule admin%E2%80%94a-special-role=admina-special-role h_01HC72J0HANGXV4GVJCQ5X2T84=admina-special-role h_01HC72J0HA5RFZE1G0KNKR30KV=account-owner-hash h_01HC72J0HANQ3Z6FCWXA0TF3TN=user-management-page h_01HC72J0HAFBMYM792GXMCEY3T=users-tab h_01HC72J0HAXC2NAVQC4J2PMB0Z=roles-tab h_01HC72J0HATN656W4B9DT82M60=creating-a-user h_01HC72J0HAP1GDH8JKGMT6XH67=important h_01HC72J0HA3QJ2CH8TGEMJBY3A=account-activation-hash h_01HC72J0HAG2XF42NSYRZDEKVN=editing-users h_01HC72J0HAF739MQPF482T0WVA=individual-editing multiuser-editing=multi-user-editing h_01HC72J0HA3BKXJCAVRQ5SJYYE=multi-user-editing h_01HC72J0HAZM2NBXN5ZHZET4BS=note h_01HC72J0HAE70AMWSDP5BXGWK9=example-1 h_01HC72J0HAQFD33VT0ARRWG0ZF=deleting-users h_01HC72J0HAF5QFC5ZR7EHFMBM6=special-situations-and-additional-procedures h_01HC72J0HAD8JXPPFET4N2P3EK=managing-temp-roles h_01HC72J0HA8PP79VV1F03E5AXV=temp-role-limitations h_01HC72J0HAJES0N195DZ797C4V=example-2 h_01HC72J0HAVXK83AK99NQVDT8T=changing-the-account-owner h_01HC72J0HANXBK4T1SD6V2KHE4=important-1 1%E2%80%93send-an-email-request=1send-your-request-via-the-chat-widget h_01HC72J0HAJ3C8WJ767KG2307C=1send-your-request-via-the-chat-widget 2%E2%80%93next-steps=2next-steps h_01HC72J0HAM13NY9EKNKG8R1CA=2next-steps troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HC72J0HAWRBVWGVT12W6M711=troubleshooting-can-t-create-this-user h_01HC72J0HANPD39FRCWSPMRY5D=resending-a-user-invitation h_01HC72J0HARYRSXHKX41A41MPG=resetting-twofactor-authentication-2fa" />
