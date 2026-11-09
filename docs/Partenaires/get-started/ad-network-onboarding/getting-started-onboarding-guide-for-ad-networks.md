---
title: Mise en route - Guide d’intégration pour les réseaux publicitaires
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
  edited_at: '2024-10-30T11:14:47Z'
  id: 360001300998
  locale: fr
  section: Ad network onboarding
  section_id: 6551058566033
  url: https://support.appsflyer.com/hc/fr/articles/360001300998
---
> **En bref :** Complétez l'intégration avec AppsFlyer en configurant et en testant votre lien d'attribution et vos intégrations de postbacks. Comprendre les étapes, les délais et les dépendances du processus.

<Image align="center" alt="AdNetworks_-_Onboarding__2_.png" src="https://files.readme.io/33217648d1f5c1ef327871b9b2ccfaadb6b9ae34fb2645ffcfbe187c378dd054-30603793569297.png" />

<div id="what-is-appsflyer" />

## Qu'est-ce qu'AppsFlyer ?

AppsFlyer, leader de l'attribution mobile, vous souhaite la bienvenue en tant que partenaire intégré de notre réseau publicitaire. Cet article s'adresse aux réseaux publicitaires qui ont complété l'enregistrement de partenaire AppsFlyer. Si vous souhaitez vous enregistrer en tant que partenaire, vous devez demander à un <Anchor target="_blank" href="/marketers/fr/docs/set-up-an-integrated-partner#inviter-de-nouveaux-partenaires-dans-appsflyer">client d'AppsFlyer (annonceur) de vous y inviter</Anchor>.

<div id="ad-network-onboarding" />

## Intégration des réseaux publicitaires

Les étapes nécessaires à l'intégration et le temps estimé pour les réaliser sont énumérés dans la section **Étapes de l'intégration** de cet article.

L'intégration signifie que :

* AppsFlyer enregistre vos engagements (clics et impressions). Les engagements sont attribués selon le <Anchor target="_blank" href="/marketers/fr/docs/appsflyer-attribution-model">modèle d'attribution d'AppsFlyer</Anchor>.
* Les postbacks au format que vous avez demandé sont envoyés à vos terminaux..
* Vous pouvez accéder aux fonctionnalités d'AppsFlyer telles que la signature par clic, Protect360, Data Locker, etc.

<div id="if-you-need-help" />

<Accordion title="Si vous avez besoin d'aide :">

* Consultez la <Anchor target="_blank" href="/partners/fr/docs/integrated-partners-faq">FAQ des</Anchor> partenaires
* Consultez l'article sur les <Anchor target="_blank" href="/partners/fr/docs/integration-requests-for-partners">demandes de modification de l'intégration</Anchor>

</Accordion>

N'oubliez pas :

* Les estimations de temps dans cet article sont basées sur notre expérience de travail avec les réseaux publicitaires. Chaque intégration étant légèrement différente, les durées réelles peuvent varier.
* AppsFlyer prend en charge de nombreuses <Anchor target="_blank" href="/partners/fr/docs/platforms-for-ad-networks">plates-formes de performance</Anchor>. Si vous utilisez l'une des plateformes de la liste, vous devez consulter les instructions spécifiques à la plateforme avant de l'intégrer.

<div id="onboarding-steps" />

## Étapes de l’intégration

**L'intégration avec AppsFlyer** :

1. [Compléter la partie 1 - intégration et tests.](/docs/getting-started-onboarding-guide-for-ad-networks#partie-1--intégration-et-essais)
2. [Compléter la partie 2 - test avec les applications des annonceurs.](/docs/getting-started-onboarding-guide-for-ad-networks#partie-2--tester-lutilisation-des-applications-des-annonceurs)
3. [Compléter la partie 3 - utiliser le tableau de bord et les outils de reporting d'AppsFlyer.](/docs/getting-started-onboarding-guide-for-ad-networks#partie-3--tableau-de-bord-et-options-de-rapport-dappsflyer)

<div id="part-1-integration-and-testing" />

### Partie 1 : Intégration et essais

<table><thead><tr><th>Action</th><th>Procès-verbal requis</th></tr></thead><tbody><tr><td>Attendez l’email d'approbation de votre inscription vous invitant à compléter les étapes d'intégration obligatoires.</td><td>--</td></tr><tr><td colspan="2"><p><strong>Étapes d'intégration obligatoires</strong> </p></td></tr><tr><td><p><a href="./self-serve-integration-management-for-ad-networks#lien-dattribution" target="_blank">Indiquez votre lien d'attribution</a> : <span>Les liens d'attribution sont des URL avec des macros. Ces macros sont alimentées par vos soins avec des valeurs réelles et envoyées à AppsFlyer chaque fois qu'un utilisateur clique sur un lien. <br/>Attention ! Si vous utilisez une plateforme de réseau de performance prise en charge par AppsFlyer, vous devez tenir compte des instructions spécifiques à cette plateforme. Voir les <a href="./platforms-for-ad-networks" target="_blank">guides du réseau de performance</a>.</span></p></td><td>60</td></tr><tr><td> <a href="./self-serve-integration-management-for-ad-networks#postback-par-défaut" target="_blank">Spécifier les macros de postback</a> : <span>Les postbacks sont des URL contenant des macros alimentées par AppsFlyer et envoyées à vos serveurs en temps réel après chaque conversion.</span> </td><td>60</td></tr><tr><td><p>Connectez-vous au <a href="https://hq1.appsflyer.com/auth/login" target="_blank">tableau de bord d'AppsFlyer</a> en utilisant les informations d'identification fournies. </p></td><td> </td></tr><tr><td><p>Téléchargez le logo de votre entreprise. Votre logo doit avoir le format 200 X 50 PNG transparent. </p><ol><li>Dans AppsFlyer, dans la barre de menu, sélectionnez votre adresse email &gt; <strong>Configuration du partenaire</strong>. </li><li>Dans l'onglet <strong>Profil</strong>, téléchargez le logo de votre entreprise. </li><li>Cliquez sur <strong>Enregistrer</strong>.</li></ol></td><td>5</td></tr><tr><td><p>Testez l'intégration à l'aide des applications de test AppsFlyer :</p><ul><li><a href="./android-integration-testing-for-ad-networks" target="_blank">Android</a></li><li><a href="./ios-integration-testing-for-ad-networks" target="_blank">iOS</a></li></ul></td><td>10</td></tr><tr><td colspan="2"><strong>Étapes d'intégration facultatives</strong></td></tr><tr><td><p>[iOS] Si vos annonceurs ont besoin d'AppsFlyer Aggregated Advanced Privacy, complétez l'intégration <a href="./self-serve-integration-management-for-ad-networks#confidentialité-avancée-et-postbacks-skan" target="_blank">Confidentialité avancée</a> d’AppsFlyer.</p></td><td>60</td></tr><tr><td><p>[iOS] Si vous menez des campagnes SKAdNetwork, terminez <a href="./self-serve-integration-management-for-ad-networks#confidentialité-avancée-et-postbacks-skan" target="_blank">l’intégration de SKAdNetwork</a>.</p></td><td>60</td></tr><tr><td><h4><strong><span id="authorized-agencies"></span>Agences autorisées</strong></h4><p>Créez et gérez une liste d'agences que vous autorisez à mener des campagnes par l'intermédiaire de votre réseau d'intégration. Pour ce faire, il suffit de saisir l'identifiant de l'agence (af_prt) dans l'espace réservé aux agences autorisées. <a href="./set-up-your-list-of-authorized-agencies" target="_blank"><strong>Agences autorisées</strong></a> du centre de sécurité. Pour obtenir l'identifiant de l'agence, cette dernière doit vous contacter et vous le fournir.</p></td><td>2</td></tr><tr><td colspan="2"><p><strong>Caractéristiques et considérations optionnelles</strong><br/></p><p>Il est possible de mettre en œuvre des intégrations et options basées sur les exigences des annonceurs.</p></td></tr><tr><td><p>Pour vous assurer que des clics frauduleux ne sont pas envoyés en utilisant l'identifiant de votre partenaire, mettez en place une <a href="./click-signing-for-ad-networks" target="_blank">signature des clics</a>.</p></td><td>60+</td></tr><tr><td><p>Pour les annonceurs qui utilisent Protect360 ou des règles de validation, ajoutez des <a href="./postback-macros-for-ad-networks#macros%E2%80%94installs-inapp-events-and-rejected-events" target="_blank">postbacks sur les attributions rejetées</a>.</p></td><td>15</td></tr><tr><td><p>Envoyer les coûts à AppsFlyer par API. <a href="./incost-api-for-ad-networks" target="_blank">API InCost</a></p></td><td>60+</td></tr><tr><td> <a href="/marketers/fr/docs/retargeting-attribution-guide" target="_blank">Intégration du retargeting</a>.</td><td>15</td></tr><tr><td><p><a href="/marketers/fr/docs/measure-view-through-engagements" target="_blank">Intégration de l'attribution post-vue</a>.</p></td><td>15</td></tr></tbody></table>

<div id="part-2-test-using-advertiser-apps" />

### Partie 2 : Tester l'utilisation des applications des annonceurs

Dans cette partie, vous testerez votre intégration à l'aide d'une application appartenant à un annonceur. À ce titre, vous devez contacter l'annonceur et lui demander de réaliser certaines des étapes de cette partie. Dans cette partie, les références aux annonceurs peuvent également concerner les agences si elles agissent pour le compte d'un annonceur.

| Exécuté par | Action | Procès-verbal requis |
| --- | --- | --- |
| Annonceur | Cochez <Anchor target="_blank" href="/marketers/fr/docs/set-up-an-integrated-partner#integration-tab">Activer le partenaire.</Anchor><br /><br />Lorsque cette option est activée, AppsFlyer considère les engagements apportés par vous comme des candidats à l'attribution. | 2 |
| Annonceurs | Accordez des <Anchor target="_blank" href="/marketers/fr/docs/set-up-an-integrated-partner#autorisations-pour-le-réseau-publicitaire">autorisations au réseau publicitaire*</Anchor> et ajoutez les membres de votre équipe.<br /><br />Lorsque cette option est activée, les données de performance de l'application sont disponibles dans votre tableau de bord AppsFlyer. Seuls les membres de l'équipe figurant sur la liste peuvent accéder aux données. | 2 |
| Réseau publicitaire | <Anchor target="_blank" href="/marketers/fr/docs/user-management#creating-users">Ajouter un membre d'équipe à votre compte</Anchor>. | 2 |
| Annonceur (admin) | <Anchor target="_blank" href="/marketers/fr/docs/registering-test-devices">Enregistrer votre appareil de test</Anchor>. Demandez à l'annonceur de le faire en votre nom. | 3 |
| Réseaux publicitaires | <Anchor target="_blank" href="/partners/fr/docs/test-marketer-campaign-integration-with-the-ad-network">Testez l'intégration en utilisant les applications des annonceurs.</Anchor> | 60 |

<div id="part-3-appsflyer-dashboard-and-reporting-options" />

### Partie 3 : Tableau de bord et options de rapport d'AppsFlyer

| Option |
| --- |
| <Anchor target="_blank" href="/partners/fr/docs/integrated-partners-dashboard">Utiliser le tableau de bord du partenaire</Anchor>. |
| Obtenez des données de performance agrégées via un stockage sur le cloud avec <Anchor target="_blank" href="/partners/fr/docs/data-locker-for-partners">Data Locker</Anchor> pour les réseaux publicitaires. |
| <Anchor target="_blank" href="/marketers/fr/docs/raw-data-export-page">Données brutes</Anchor> Protect360 |

<div id="integration-validation-period" />

## Période de validation de l'intégration

Pour garantir l'intégrité de l'écosystème AppsFlyer et protéger les systèmes internes contre le trafic non valide, toutes les nouvelles intégrations de réseaux publicitaires sont soumises à une période de validation. Pendant cette période, AppsFlyer vérifie minutieusement le trafic et évalue sa qualité avant de mettre l'intégration à la disposition d'autres annonceurs sur le <Anchor target="_blank" href="/marketers/fr/docs/partner-integrations">Marketplace</Anchor>. Les intégrations de réseaux publicitaires qui ne répondent pas aux critères de trafic de haute qualité après validation peuvent faire l'objet d'une résiliation de compte.

<div id="validation-periodfaq" />

### Période de validation — FAQ

| **Question** | **Réponse** |
| --- | --- |
| <span id="why-cant-advertisers-find-me-on-the-marketplace"></span>Pourquoi les annonceurs ne me trouvent-ils pas sur le Marketplace alors que j'ai terminé l'intégration ? | Pendant la période de validation, votre intégration n'est visible que par l'annonceur qui vous a référencé. Une fois que nous aurons validé la qualité de votre trafic, vous recevrez un email vous informant que votre intégration est disponible pour tous les annonceurs. |
| <span id="what-should-i-do-to-make-the-integration-available-for-all-advertiers"></span>Que puis-je faire pour m'assurer que mon intégration sera approuvée ? | Fournir un volume significatif de trafic de haute qualité à l'annonceur qui vous a recommandé. |
| <span id="when-should-i-expect-to-receive-the-validation-completion-email"></span>Quand dois-je m'attendre à recevoir l’email de validation ? | Lorsque nous aurons validé suffisamment de trafic, vous recevrez un email vous informant que la période de validation est terminée. |
| <span id="can-i-know-the-current-status-of-the-validation-period"></span>Puis-je connaître l'état d'avancement de ma validation ? | Vous ne le saurez que lorsque la période de validation aura pris fin, après avoir reçu une notification par email. |
| <span id="what-are-the-validation-criteria-based-on"></span>Sur quoi se fondent les critères de validation ? | Les critères de validation sont basés sur les algorithmes d'apprentissage automatique dynamique <Anchor target="_blank" href="/marketers/fr/docs/protect360-anti-fraud-guide">Protect360</Anchor>. |
| <span id="another-adviertiser-wants-to-work-with-me"></span>Que se passe-t-il si un autre annonceur souhaite commencer à travailler avec moi pendant ma période de validation ? | Pendant la période de validation, votre intégration n'est visible que par l'annonceur référent. D'autres annonceurs pourront travailler avec vous après la fin de votre période de validation. |
| <span id="my-integration-fails"></span>Que se passe-t-il si mon intégration échoue à la validation ? | La période de validation peut être prolongée pour surveiller les améliorations de la qualité du trafic, ou votre intégration peut être définitivement supprimée de la plateforme AppsFlyer. Dans les deux cas, vous serez informé. |
| <span id="replace-advertiser"></span>Puis-je remplacer l'annonceur référent par un autre annonceur avec lequel je travaille ? | Vous pouvez le faire, à condition que ce soit pendant la période de validation de 30 jours. |

<div data-zendesk-anchors="what-is-appsflyer=quest-ce-quappsflyer- h_01J09255QNBFRV8DYZPGG990A0=quest-ce-quappsflyer- ad-network-onboarding=int%C3%A9gration-des-r%C3%A9seaux-publicitaires h_01J09255QN61VPW292PC2CH9KN=int%C3%A9gration-des-r%C3%A9seaux-publicitaires h_01J09255QNGD66T140ERW4WP8Z=if-you-need-help onboarding-steps=%C3%A9tapes-de-lint%C3%A9gration h_01J09255QNZ9QXXFB54YRYCM8P=%C3%A9tapes-de-lint%C3%A9gration part-1-integration-and-testing=partie-1--int%C3%A9gration-et-essais h_01J09255QN35ZBKE2R2HDDZWSZ=partie-1--int%C3%A9gration-et-essais h_01J0JS136CTYEF6F29H8R1NV29=authorized-agencies part-2-test-using-advertiser-apps=partie-2--tester-lutilisation-des-applications-des-annonceurs h_01J09255QP11XJD3C83VZZXXQZ=partie-2--tester-lutilisation-des-applications-des-annonceurs part-3-appsflyer-dashboard-and-reporting-options=partie-3--tableau-de-bord-et-options-de-rapport-dappsflyer h_01J09255QPSSD8CF0HR059RWXZ=partie-3--tableau-de-bord-et-options-de-rapport-dappsflyer integration-validation-period=p%C3%A9riode-de-validation-de-lint%C3%A9gration h_01J09255QP82ZYZDJMA74SRYGZ=p%C3%A9riode-de-validation-de-lint%C3%A9gration validation-period%E2%80%94faq=p%C3%A9riode-de-validation--faq h_01J09255QP77BME57P9B7S222V=p%C3%A9riode-de-validation--faq" />
