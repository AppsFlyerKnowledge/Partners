---
title: Set up your list of authorized agencies
metadata:
  keywords:
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
  created_at: '2024-06-09T19:29:56Z'
  edited_at: '2026-10-13T01:50:23Z'
  id: 25774607860113
  locale: ja
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/ja/articles/25774607860113
---
> **At a glance:** Manage which agencies you authorize to run campaigns through your network integration.

## Overview

To prevent unauthorized use of your network, all agencies running campaigns through your network integration must be pre-approved. This is done by adding their agency ID (`af_prt`) to your list of authorized agencies. Agencies that don't appear in the list are unable to configure the integration, as the partner configuration window is grayed out. This prevents them from managing campaigns. After they're added to the list, the approval applies account-wide, allowing them to run campaigns with all apps on your network.

As of July 31, 2024, only traffic from agencies authorized by the ad networks will be recorded and measured in AppsFlyer. Unauthorized traffic will result in a 403 (Forbidden) response from AppsFlyer.

> 📘 **Note**
>
> * This doesn't apply to agencies working with <Anchor target="_blank" href="/marketers/ja/docs/self-reporting-networks-srns">SRNs</Anchor>
> * Only admins have access to this page
> * The list of authorized agencies can include up to 200 agencies

[![authorized-agencies-5.jpg](https://files.readme.io/10012bde55cffa967f2e581420a9c32b7ce8b9cb120e203ba230bf7f271b0d9a-25977984018833.jpg)](https://files.readme.io/10012bde55cffa967f2e581420a9c32b7ce8b9cb120e203ba230bf7f271b0d9a-25977984018833.jpg)

## Manage authorized agencies

From the **Authorized agencies** page, you can add agencies, view the existing list of agencies you've approved to run campaigns on your network, and delete agencies you don't approve. The page includes two sections:

* Left pane: Add new agencies
* Right pane:
  * View the list of approved agencies
  * Delete agencies

**To access the Authorized agencies page:**

1. From the top bar, open the account menu (email address dropdown) > **Security center.**
2. In the **Authorized agencies** section, click **Manage authorized agencies**.

### Add an agency to the list

1. From the left pane of the **Authorized agencies** page, enter the agency ID.
2. Click **Add to list**. The agency now appears on the right pane.
3. [Optional] Repeat steps 1-2 for adding more agencies.
4. Click **Save list**.

> 📘 **Note**
>
> Make sure to enter a valid agency ID. For example (af\_prt=) `my_agency_123`

### Delete an agency from the list

1. From the right pane of the **Authorized agencies** page, hover over the agency you want to delete and click the dustbin icon.
2. Confirm the deletion. An indication confirms the successful deletion of the agency.
3. [Optional] Repeat steps 1-2 for deleting more agencies.

<div data-zendesk-anchors="h_01HJR00RGQ2PK3T8BB2ZG3PFQN=overview h_01HJR00RGQX0CQEHDS9BHBGJD4=note accessing-the-allowlists=manage-authorized-agencies h_01HZZ5FP1560HJYDVDNSJ8WAAP=manage-authorized-agencies h_01HZZ691KMKTYVAETT4RM3AD97=add-an-agency-to-the-list h_01HZZ7QGY0VTS0FY0HJJAZ2AXV=note-1 h_01HJR00RGQ4ZEGE0RDK01S5SQQ=delete-an-agency-from-the-list" />
