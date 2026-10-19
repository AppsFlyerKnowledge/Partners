---
title: User management for ad networks
excerpt: >-
  Create and manage your ad network account's AppsFlyer users, and assign them a
  role defining which features they can access.
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
  created_at: '2021-12-19T11:16:28Z'
  edited_at: '2025-12-31T08:41:51Z'
  id: 4414238502289
  locale: en-us
  section: Ad network onboarding
  section_id: 6551058566033
  url: >-
    https://support.appsflyer.com/hc/en-us/articles/4414238502289-User-management-for-ad-networks
---
## Background

AppsFlyer ad network accounts allow for multiple users, each with a role that defines their access to features and functions.

The **Admin** role has access to all capabilities. The **Marketing** role has access to a more limited set of features. A full list of capabilities per role is available on the [Roles tab](/docs/user-management-for-ad-networks#roles-tab) of the **User management** page.

## More about roles

As a general rule, all roles are predefined, and each role’s functional capabilities are fixed: no "mixing and matching" allowed. However, you can change a user’s functional capabilities at any time by changing their role (except for the [account owner](/docs/user-management-for-ad-networks#admina-special-role), as discussed below).

> 📘 **Example**
>
> You have assigned Bill Bates to the **Marketing** role. This role gives Bill the ability to manage **Validation Rules** but does not allow him access to the **Audit log.**
>
> **Question:** Can I keep Bill in the Marketing role but also give him the ability to access the Audit log? Can I take away his ability to manage Validation Rules?
>
> **Answer:** No. As long as Bill stays in the Marketing role, you cannot give him the ability to access the Audit log. Nor can you remove his ability to manage Validation Rules. Of course, you can assign Bill to a different role, and his capabilities will change to those defined by that role.

### Temp roles—an exception to the rule

If your AppsFlyer account existed under our prior user management system (when the only available account types were Admin and Team member), all users were brought into the new system with unchanged capabilities. As a result, most of these users appear in the current system with **temp roles**.

Learn more about [managing temp roles](/docs/user-management-for-ad-networks#managing-temp-roles).

### Admin—a special role

An AppsFlyer account can have **one or more** Admins, but every account has at least one. This special role has several unique characteristics:

* The Admin role has access to **all** account capabilities, including:

  * All features and functions
  * All current and future apps
  * All media sources and geos

  This "all-access" characteristic of the Admin role cannot be changed or limited.
* <span id="account-owner"></span>**Account owner:** The user created at the time the account was opened is assigned the Admin role by default.
  * The account owner cannot be deleted, removed from the Admin role, or otherwise edited from the [User management](/docs/user-management-for-ad-networks#user-management-page) page. Likewise, the account owner’s email address cannot be changed.
    * If you do need to change the account owner, follow the [steps listed below](/docs/user-management-for-ad-networks#changing-the-account-owner).
  * The account owner is initially responsible for creating additional users (until additional users with user management capabilities are created).
* Admins can [manage API and S2S tokens](/appsflyer-marketers/docs/managing-appsflyer-tokens).
* Any Admin other than the account owner **can** be changed to a different role or deleted from the AppsFlyer account through the User management page.

## User management page

**To access the User management page:**

1. In the top menu bar, click on the email address dropdown.
2. Select **User management.**

### Users tab

The **Users** tab displays a table of all existing users in your account. It is the starting point for creating, managing, and deleting users.

* Click the **User** column heading to sort the table alphabetically (ascending/descending).
* Use the search box to find and display specific users.
* Click the filter icon ![filter_icon.png](https://files.readme.io/00fa39bef5e51bf9a8a0b2ae2dee4b631b57d423e261883bff1199d7293c0458-17387375698833.png) in the **Role** column heading to filter users by their role (including temp roles).
  * To clear the filter, select **None** in the filter dropdown list.
* Use the checkboxes to select and [edit multiple users](/docs/user-management-for-ad-networks#multi-user-editing) at the same time.

### Roles tab

The **Roles** tab displays a list of all roles defined in your account, including:

* The 3 [predefined roles](/docs/user-management-for-ad-networks#more-about-roles) of Admin, Marketing, and Team manager
* Any [temp roles](/docs/user-management-for-ad-networks#temp-rolesan-exception-to-the-rule) currently assigned to users

Click on the name of any role in the left panel to see:

* Full details of the role’s capabilities
* The number of users currently assigned that role (in the top-right corner of the screen)
  * Hover over the user icon ![user_icon.png](https://files.readme.io/70d626cc0d2888c46c0e080dc76e4f005312fe5dea7e7811336e0324e4a846ad-17387375703569.png) to see a list of the first 20.

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

     > 📘 **Important!**
     >
     > A user’s email address is what identifies them in the AppsFlyer platform, meaning:
     >
     > * It cannot later be changed without deleting and recreating the user.
     > * It must be a valid email address at which the user can receive email.
     > * It cannot be associated with another user in any AppsFlyer account.
     > * If the email address is already in use (either in your account or a different one), you will see the message *Can't create this user.* Follow the [troubleshooting steps below](/docs/user-management-for-ad-networks#troubleshooting-can-t-create-this-user) to resolve this issue.

4. Select the user’s department (optional).
5. Select the user’s role (required).
6. Select the apps the user can access:
   1. The default setting allows access to all current and future apps in the account. To change this setting, use the checkboxes to select and deselect apps.
   2. A user can be given access to all future apps only if they have access to all current apps.
7. Click **Save** to create the user.
8. **On the user's side:** To become an active user (team member), the user must [activate their account](#becoming-an-active-user) from the email invitation they received.

#### Becoming an active user

After clicking **Save** to finish the procedure of [creating a user](/docs/user-management-for-ad-networks#creating-a-user) (above), the user receives an email invitation to activate their account. The activation link is valid for 48 hours. If the user didn’t receive the invitation or if the link has expired, you can [resend the invitation](/docs/user-management-for-ad-networks#resending-a-user-invitation).

You can see the new user on the User management page, with an envelope icon ![pending_invitation_icon.png](https://files.readme.io/1e334edd433f9ac13a175cdd48345adebe02892215896ea967768dc3cabf0349-17387375704209.png) near their name. This indicates that an invitation has been sent and the account is awaiting activation. Once the user activates their account, the envelope disappears.

## Editing users

Users can be edited either one at a time or in groups.

### Individual editing

**To edit an individual user:**

1. On the **Users** tab, click the **Actions** ![actions_icon.png](https://files.readme.io/7bdbda083da16718b90246b7d915ebee2e164fa402a143e0c6cc9be95ca34dca-17387343712017.png) button on the far-right side of the user’s row.
2. Select **Edit** from the menu.
3. Edit user settings as required.
   * All settings other than email address are editable.
4. Click **Save**.

### Multi-user editing

Multi-user editing is an efficient way to change the role of several users at one time. Using this feature in combination with the search and filtering capabilities of the **Users** tab can make it particularly helpful for managing large numbers of users.

> 📘 **Note**
>
> You cannot delete users or assign them to the Admin role using multi-user editing.

**To edit multiple users:**

1. On the **Users** tab, select the checkboxes of the user or users you want to edit.
   * Select the checkbox in the column heading to select all visible users.
   * The number of currently-selected users is displayed on the right side of the search box. Note that the [account owner](/docs/user-management-for-ad-networks#admina-special-role) cannot be selected and is not included in the number of selected users.
2. Click the **Role** button that is displayed at the top-right of the table.
3. Make the necessary changes. Remember that your changes apply to all selected users!
4. The edited users are highlighted in the table, and the users appear as they will once the changes are saved. However, you still have the opportunity to review your changes and confirm or cancel them in the next step.
5. Review your changes. Click **Save** to confirm or **Cancel** to undo them.

## Deleting users

**To delete a user:**

1. On the **Users** tab, click the **Actions** button ![actions_icon.png](https://files.readme.io/7bdbda083da16718b90246b7d915ebee2e164fa402a143e0c6cc9be95ca34dca-17387343712017.png) on the far-right side of the user’s row.
2. Select **Delete** from the menu.

## Special situations and additional procedures

<div id="managing-temp-roles" />

<Accordion title="Managing temp roles">

If your account previously used our prior user management system, [temp roles](/docs/user-management-for-ad-networks#temp-rolesan-exception-to-the-rule) were assigned to existing users to ensure that they were brought into the new system with unchanged capabilities.

* Users with the same capabilities were assigned the same temp role.
* Use the features of the [Roles tab](/docs/user-management-for-ad-networks#roles-tab) to review the capabilities of each temp role and a list of users currently in it.

#### Temp role limitations

Temp roles were designed specifically to allow seamless transition from our prior user management system. As such, they are available only in limited situations:

* Temp roles cannot be assigned to other users (whether new or existing).
* A user with a temp role cannot be assigned a different temp role.
* When a user with a temp role is changed to a predefined role, they cannot be returned to the previously-assigned temp role (or to any other temp role).
* If the last user in a temp role is removed from it, the role will no longer appear in your account.

> 📘 **Example**
>
> Your account previously used our prior user management system. Diana and Edward were existing users at the time your account was moved to the new system. Diana is now in Temp role 1, and Edward is in Temp role 2.
>
> * You hire a new employee, Fiona. You can assign Fiona to either the Admin or Marketing role. However, you cannot assign Fiona to Temp role 1 or Temp role 2.
> * Diana cannot be moved from Temp role 1 to Temp role 2. However, you can assign her to either the Admin or Marketing role.
> * If you move Diana from Temp role 1 to the Marketing role, she can’t later be moved back to Temp role 1.
> * If Diana was the last user in Temp role 1 when you moved her to the Marketing role, Temp role 1 will no longer appear in your account.

<div id="changing-the-account-owner" />

<Accordion title="Changing the account owner">

Because all Admins have the same permissions as the account owner, changing the account owner is not usually necessary. But if you find that you must change the account owner, follow these steps to do so.

> 📘 **Important!**
>
> A few things to consider before you begin:
>
> Changing the account owner must be completed manually according to these steps. It cannot be done from the **User management** page.

#### #1–Send your request via the chat widget

To begin the process of changing the account owner, open the chat widget [using this link](https://hq1.appsflyer.com/apps/search?openAssistant=true) or by clicking the Help button on the top-right of the menu bar. Include the following information in the chat:

* Name of the account owner you would like to replace
* Name, title, and email of the new account owner

#### #2–Next steps

Once the change has been processed, you will receive an email notification from AppsFlyer.

* If you want the prior account owner to continue using your AppsFlyer account, [create a new user](/appsflyer-marketers/docs/user-management#creating-users) for them and assign them a new role.
* APIs using token v2 aren't affected by changing the account owner.  [Learn more about managing tokens](/appsflyer-marketers/docs/managing-appsflyer-tokens).

</Accordion>

<div id="troubleshooting-can-t-create-this-user" />

<Accordion title="Troubleshooting 'Can’t create this user'">

If you receive the error message *Can’t create this user* when entering the email address of a new user, it generally means that the email is already associated with an AppsFlyer user (either in your account or a different one). Follow the steps relevant to your situation:

If the user is in your account:

* Check to see if the user has activated their account. If not, [resend the invitation](/docs/user-management-for-ad-networks#resending-a-user-invitation) if required.
* If the user has activated their account, ask them to try to log in again using the email address associated with their user. Advise them to follow the **Forgot password** steps if required.

If the user’s email is used in a different account or you can’t determine the account in which the user’s email is used, select one of the following options:

* Delete them from the other account and add them to yours (requires that either you or the user has the required permissions in the other account); or
* Add them to your account using a different email address. This must be a valid email address at which they can actually receive an email; or
* Contact AppsFlyer support for partners through the [partner assistant chatbot](/docs/using-the-partner-assistant-chatbot).

</Accordion>

<div id="resending-a-user-invitation" />

<Accordion title="Resending a user invitation">

If a new user did not receive their [account activation invitation](/docs/user-management-for-ad-networks#becoming-an-active-user) or if they did not activate within 48 hours, you can resend the email as follows:

1. On the **Users** tab, click the **Actions** button ![actions_icon.png](https://files.readme.io/7bdbda083da16718b90246b7d915ebee2e164fa402a143e0c6cc9be95ca34dca-17387343712017.png) on the far-right side of the user’s row.
   * Note that the user is still shown with an envelope icon ![pending_invitation_icon.png](https://files.readme.io/1e334edd433f9ac13a175cdd48345adebe02892215896ea967768dc3cabf0349-17387375704209.png), indicating that they have not yet activated their account).
2. Select **Resend email invite** from the menu.

</Accordion>

<div id="resetting-twofactor-authentication-2fa" />

<Accordion title="Resetting two-factor authentication (2FA)">

If your account uses 2FA, there may be occasions on which you need to reset a user’s 2FA settings. Do so as follows:

1. On the **Users** tab, click the **Actions** button ![actions_icon.png](https://files.readme.io/7bdbda083da16718b90246b7d915ebee2e164fa402a143e0c6cc9be95ca34dca-17387343712017.png) on the far-right side of the user’s row.
2. Select **Reset 2FA** from the menu.

**Note:** An admin can reset any other admin's 2FA other than their own or the [account owner's](/docs/user-management-for-ad-networks#admina-special-role). To reset the account owner's 2FA, contact AppsFlyer support for partners through the [partner assistant chatbot](/docs/using-the-partner-assistant-chatbot).

</Accordion>

</Accordion>

<div data-zendesk-anchors="h_01HEN51924E23493MKXPEKHS03=background h_01HEN51924R007XNM3N45CA73A=more-about-roles h_01HEN51924WBY63ASRGH7ZQFP4=example temp-roles%E2%80%94an-exception-to-the-rule=temp-rolesan-exception-to-the-rule h_01HEN51924DT5GVPMJBQD3ZY9R=temp-rolesan-exception-to-the-rule admin%E2%80%94a-special-role=admina-special-role h_01HEN51924G6GXVH8HH5DAWZ26=admina-special-role h_01HEN51924PQEM4R974HMWPH98=user-management-page h_01HEN51924RDZFSJN0KN0YJFND=users-tab h_01HEN519249AHVKGM5CDTXPEP7=roles-tab h_01HEN51924C56PAKQYTQM05DMV=creating-a-user h_01HEN519241VD35W7AYQ08NMHJ=important h_01HEN51924F0G8287RP08EB464=becoming-an-active-user 01HEPXYXV78HEXK5SD4QBDGEGH=editing-users h_01HEN51924AP4TT97C2X5CRB35=individual-editing multiuser-editing=multi-user-editing h_01HEN519246HC2M4BB35GR29SQ=multi-user-editing h_01HEN51925ZWQ8V3XJNAD4F4V9=note h_01HEN51925Q9P2GFJWWWW9MMQ2=deleting-users h_01HEN51925JBC3R887CVFNFA27=special-situations-and-additional-procedures h_01HEN519258745RNY4RNT4MWK6=managing-temp-roles h_01HEN51925REZEKBA501T0RMME=temp-role-limitations h_01HEN51925FMKJ5D7BE93GVN2G=example-1 h_01HEN51925J3NKAJSKYEF9AMMJ=changing-the-account-owner h_01HEN51925FR6AGT1M2YHJJB6A=important-1 1%E2%80%93send-an-email-request=1send-your-request-via-the-chat-widget h_01HEN51925GQGFAZYRTHPBBXA2=1send-your-request-via-the-chat-widget 2%E2%80%93next-steps=2next-steps h_01HEN51925SPRA034581N8BWYK=2next-steps troubleshooting-can%E2%80%99t-create-this-user=troubleshooting-can-t-create-this-user h_01HEN51925YAY0E37S799S7S1J=troubleshooting-can-t-create-this-user h_01HEN519253VMNBPNW61M10QZW=resending-a-user-invitation h_01HEN51925C7X1AEM2FJ6152Z1=resetting-twofactor-authentication-2fa" />
