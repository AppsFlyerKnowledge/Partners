---
title: >-
  Rapport SSOT (Single Source of Truth) Data Locker pour les réseaux
  publicitaires
metadata:
  keywords:
    - Advertisers
    - Ad Networks
    - Partners
    - Marketers
    - SKAdNetwork (SKAN)
x-zendesk:
  category: Partners
  category_id: 6550456653457
  content_tags:
    - pm-gil-or
    - Marketers
    - SKAdNetwork (SKAN)
    - Ad Networks
  created_at: '2024-07-31T19:51:34Z'
  edited_at: '2024-08-11T14:32:30Z'
  id: 27168206416017
  locale: fr
  section: Data Locker
  section_id: 6551591547409
  url: https://support.appsflyer.com/hc/fr/articles/27168206416017
---
> **En bref :** Le rapport SSOT (Single Source of Truth) de Data Locker offre une vue d’ensemble détaillée des performances des campagnes d’app en assemblant les données des différentes méthodes d’attribution, comme la correspondance d’ID et SKAN.  Il permet de transférer les données dans vos systèmes BI pour que leur traitement soit le plus précise possible.

<div id="note" />

> 📘 **Remarque**
>
> Avant de pouvoir partager les données avec vous, les annonceurs doivent accorder leurs [Autorisations](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions) dans le tableau de bord

<div id="what-is-data-locker" />

## Qu’est-ce que Data Locker ?

Data Locker est une solution sécurisée qui envoie les données directement aux principales plateformes sur le cloud, comme AWS, GCS et Snowflake. Vous pouvez ainsi intégrer et gérer simplement les données dans vos propres systèmes BI pour produire une analyse et des rapports complets. <Anchor target="_blank" href="/partners/fr/docs/data-locker-for-partners">En savoir plus.</Anchor>

<div id="what-is-single-source-of-truth-ssot" />

## Qu’est-ce que la Single source of truth (SSOT) ?

La SSOT (Single Source of Truth) permet d’éviter les problèmes de fragmentation des données en offrant une vue d’ensemble détaillée des performances des campagnes d’app grâce à l’assemblage des données des différentes méthodes d’attribution, comme la correspondance d’ID et SKAN. <Anchor target="_blank" href="/marketers/fr/docs/single-source-of-truth-ssot-guide-for-ios-attribution">En savoir plus.</Anchor>

<div id="benefits-of-ssot-reports-in-data-locker" />

## Intérêts des rapports SSOT dans Data Locker

Le rapport SSOT offre les mêmes éléments que ceux utilisés par les marketeurs pour analyser et mesurer les performances.

* **Obtenir une vue d’attribution précise et complète :** la SSOT assemble les données issues de différentes méthodes d’attribution, elle empêche ainsi de compter deux fois les installations attribuées par plusieurs méthodes d’attribution. Vous avez ainsi la garantie que les données sont exactes et reflètent le comportement et l’attribution véritables des utilisateurs.
* **Charger des données dans vos systèmes BI :** la SSOT permet de transférer efficacement les données agrégées dans vos systèmes BI internes. Les éléments transférés incluent les attributions, événements in-app et données de revenus, ce qui couvre l’ensemble des dimensions et métriques.

<div id="setting-up-data-locker" />

<Accordion title="Configuration de Data Locker">

Utilisez cette procédure pour mettre en place Data Locker. Les modifications apportées aux paramètres prennent effet dans les 3 heures.

**Conditions minimum :**

Suivez une ou plusieurs des procédures de stockage suivantes :

* Compartiment <Anchor target="_blank" href="/marketers/fr/docs/data-locker-cloud-service-setup#aws-storage">AWS</Anchor>
* Compartiment <Anchor target="_blank" href="/marketers/fr/docs/data-locker-cloud-service-setup#gcs-storage">GCS</Anchor>
* Compartiment Yandex [Beta]
* Centre de données <Anchor target="_blank" href="/marketers/fr/docs/data-locker-cloud-service-setup#bigquery">BigQuery</Anchor>

**![AppsFlyerAdmin_us-en.png](https://files.readme.io/d67fdedd94c56e8da776e590b12883503f47d36f0d58b996c4c64cc5d0e9c675-16281491712785.png) Pour configurer Data Locker :**

1. Connectez-vous à votre <Anchor target="_blank" href="https://hq1.appsflyer.com/auth/login">Tableau de bord des partenaires AppsFlyer.</Anchor>
2. Allez dans :
   * **Annonceurs** : **Rapport**>**Data Locker**.
   * **Partenaires marketing :** Cliquez sur l’icône **Menu du compte** > **Data Locker**.
3. Suivez les étapes 3 à 16 des <Anchor target="_blank" href="/marketers/fr/docs/data-locker-for-marketers?query=data%20locker%20for#set-up-data-locker">instructions de configuration de Data Locker</Anchor>

</Accordion>

<div id="permissions" />

<Accordion title="Autorisations">

Réseaux publicitaires désignés (activés) par les agences : L’agence ne peut pas accorder d’autorisation. L’agence doit demander à l’annonceur de pouvoir accorder les autorisations.

**Pour permettre au réseau publicitaire d’obtenir des données SSOT (Single Source of Truth) :**

1. Dans AppsFlyer, dans le menu latéral, sélectionnez **Collaborer** > **Partenaires intégrés**.
2. Sélectionnez le partenaire de votre choix.
3. Cliquez sur Configurer l'intégration. Vous êtes alors dirigé vers la page de configuration de l'intégration.
4. Vérifiez que Activer le partenaire  est coché. Si l'option n'est pas activée, les données ne seront pas partagées.
5. Allez dans l'onglet Autorisations.
6. Activez les autorisations de réseau publicitaire suivantes :
   * **Accéder aux données agrégées de conversion**
   * **Accéder aux données agrégées des événements in-app**
   * **Accéder aux données agrégées des revenus**
7. Cliquez sur **Enregistrer les autorisations**.
8. Informez le réseau publicitaire que vous lui avez accordé les autorisations.
9. Si vous avez plusieurs applications, répétez cette procédure pour chacune des apps intégrées au partenaire.

</Accordion>

<div id="ssot-report-facts" />

<Accordion title="Contenu des rapports SSOT">

| Nom | Description |
| --- | --- |
| Rapports disponibles | Les rapports suivants sont disponibles :<ul><li>Acquisition d’utilisateurs : attribue les conversions aux canaux d’acquisition d’utilisateurs. Inclut les activités post-installation qui ont lieu dans les fenêtres de réengagement.</li><li>Retargeting : attribue les conversions aux canaux de retargeting pour les événements qui ont lieu :<ul><li>Suite à une réattribution</li><li>Au cours d’une fenêtre de réengagement</li></ul></li><li>Unifié : attribue les conversions au dernier canal de touch, selon les règles de <Anchor target="_blank" href="/marketers/fr/docs/resolve-retargeting-double-attribution">Double attribution</Anchor> d’AppsFlyer. Cela signifie qu’une activité post-installation qui se produit lors des réengagements s’affichera dans la source de média de retargeting, et non dans la source média AU.</li></ul> |
| Période de reporting | Le rapport fournit des mesures de cohorte jusqu’à 7 jours après l’installation. |
| Structure du répertoire | La structure du répertoire repose sur la date d’installation. Chaque dossier de jour d’installation contient plusieurs versions créées quotidiennement. Chaque version présente le cumul des données mises à jour pour le jour d’installation concerné. Cela signifie que vous ne devez vous occuper que la toute dernière version du rapport. <Anchor target="_blank" href="/marketers/fr/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#structure-du-répertoire">En savoir plus</Anchor> |
| Structure du rapport | Le schéma du rapport (dimensions et métriques comprises) est fixe et ne peut pas être modifié. |
| Fuseau horaire | UTC |
| Actualisation des données | <ul><li>Quotidiennement.</li><li>Les mesures sont calculées à l’aide des données disponibles à minuit UTC (fin de la journée).</li><li>SLA : les nouveaux rapports sont disponibles dans Data Locker à 16:00 UTC. Une nouvelle version est créée chaque jour pour les 15 derniers jours d’installation. <Anchor target="_blank" href="/marketers/fr/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#report-folder-hierarchy">Lire plus</Anchor></li></ul> |

</Accordion>

<div id="report-structure" />

## Structure du rapport

Le rapport se compose de dimensions et métriques.

Les métriques couvrent les données des attributions, des revenus et des utilisateurs uniques qui produisent un événement.

<div id="field-formats" />

<Accordion title="Formats de champs">

<Table>
  <thead>
    <tr>
      <th>
        Nom de format
      </th>
      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        String [n]
      </td>
      <td>
        La longueur maximale de la chaîne. En général, nous ne limitons pas la longueur des champs à la réception des données, mais les données peuvent être tronquées ensuite.
      </td>
    </tr>
    <tr>
      <td>
        Time string
      </td>
      <td>
        Les chaînes ont le format :

        ```
        yyyy-mm-dd hh:mm:ss.
        ```

        ex.

        ```
        2019-09-17 00:09:25
        ```
      </td>
    </tr>
    <tr>
      <td>
        Enum [n]
      </td>
      <td>
        Les champs Enum ne peuvent contenir que des valeurs spécifiques. Par exemple, selected\_currency a 3 caractères et ne peut contenir que les codes de devise spécifiés
      </td>
    </tr>
    <tr>
      <td>
        Horodatage
      </td>
      <td>
        Horodatage UNIX à 10 chiffres. Ex.  
        4 août 2020, 07:25 UTC se traduit par

        ```
         "timestamp": "1596525944"
        ```
      </td>
    </tr>
    <tr>
      <td>
        Booléen
      </td>
      <td>
        *La valeur du champ peut* être*TRUE* ou FALSE.
      </td>
    </tr>
    <tr>
      <td>
        Integer
      </td>
      <td>
        Integer
      </td>
    </tr>
    <tr>
      <td>
        Float
      </td>
      <td>
        Nombre réel flottant qui peut contenir une décimale et des chiffres après la virgule.
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="dimensions" />

<Accordion title="Dimensions">

<Table>
  <thead>
    <tr>
      <th>
        Nom du champ
      </th>
      <th>
        Description
      </th>
      <th>
        Format
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        af\_ad\_id
      </td>
      <td>
        Identifiant publicitaire. Hiérarchie de la campagne.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        af\_ad
      </td>
      <td>
        Nom publicitaire.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        af\_adset\_id
      </td>
      <td>
        Identifiant de l’adset. Hiérarchie de la campagne.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        af\_adset
      </td>
      <td>
        Nom de l'adset.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        app\_id
      </td>
      <td>
        ID d'app (app de l'annonceur) avec le préfixe ID.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        attribution\_method
      </td>
      <td>
        Méthode utilisée pour attribuer l’événement. Parmi ces procédés, citons les méthodes AppsFlyer, SKAdNetwork (SKAN) et organique.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        attributed\_touch\_type
      </td>
      <td>
        Valeurs possibles : impression de clic, null.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        campagne
      </td>
      <td>
        Nom de la campagne communiqué par le réseau publicitaire à AppsFlyer.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        af\_c\_id
      </td>
      <td>
        Identifiant de la campagne.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        days\_post\_attribution
      </td>
      <td>
        Le nombre de jours écoulés depuis la date de conversion (non l'horodatage de la conversion).  
        Astuce ! Vous pouvez l’utiliser pour calculer les jours de rétention et de KPI.
      </td>
      <td>
        int
      </td>
    </tr>
    <tr>
      <td>
        event\_name
      </td>
      <td>
        Identifie l’événement. Certains noms d’événements ont une signification précise, tandis que d’autres sont liés à des événements in-app définis par l’annonceur dans l’application.

        | event\_name | Action de l’utilisateur |
        | --- | --- |
        | af\_conversion | Utilisateur converti. Utilisez conversion\_type pour identifier s’il s’agit d’une installation, d’un réengagement ou d’une réattribution. |
        | Événement in-app défini par l’annonceur | a effectué un événement in-app |
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        geo
      </td>
      <td>
        Le code pays ISO. Dérivé de l’adresse IP de l’utilisateur dans les méthodes d’attribution classiques d’AppsFlyer. Dans SKAN, les données sont soit enrichies à partir de réseaux publicitaires, soit modélisées.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        install\_date
      </td>
      <td>
        SKAN : estimé par AppsFlyer d’après l'heure d'arrivée du postback.

        AF :

        * AU : Premier lancement après l’installation
        * Retargeting : Premier lancement après le réengagement/ la réattribution
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        is\_primary\_attribution
      </td>
      <td>
        AU : True

        Retargeting : Au cours d'une fenêtre de réengagement, nous attribuons à la fois la source média d'origine (qui précède le réengagement) et la source média de réengagement. Pendant que l'événement se trouve dans la fenêtre de réengagement. La source média d'origine sera FALSE (pas d'attribution principale). La source média de réengagement sera TRUE.
      </td>
      <td>
        Bool
      </td>
    </tr>
    <tr>
      <td>
        media\_source
      </td>
      <td>
        Réseau publicitaire attribué à un événement.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        selected\_currency
      </td>
      <td>
        Code de devise à 3 lettres (USD, EUR) que vous définissez dans les paramètres de l’application. Format ISO-4217. Il s’agit de la même devise que celle dans laquelle s’affichent les revenus dans l’interface utilisateur SSOT.
      </td>
      <td>
        chaîne
      </td>
    </tr>
    <tr>
      <td>
        conversion\_type
      </td>
      <td>
        Valeurs possibles :  
        Installation : L’utilisateur télécharge et ouvre une app pour la première fois.  
        Réattribution : L’utilisateur réinstalle et il est est attribué à une nouvelle campagne.  
        Re-téléchargement (SKAN) : L’utilisateur réinstalle l’application après l’avoir désinstallée.  
        Réengagement : Réengagement : L’utilisateur ouvre à nouveau l’app après interaction avec une publicité de retargeting.
      </td>
      <td>
        chaîne
      </td>
    </tr>
  </tbody>
</Table>

</Accordion>

<div id="metrics" />

<Accordion title="Métriques">

| Nom dl choisi | Description | Format |
| --- | --- | --- |
| revenue\_selected\_currency | Cumul des revenus dans la devise sélectionnée. Maximum 2 chiffres après la virgule.  <br />Ex. Pour event\_name=achat avec days\_post\_attribution=2, la valeur reflète le revenu total des événements d’achat dans les deux jours qui suivent l’installation (et pas uniquement le deuxième jour). | double |
| revenue\_usd | Le montant cumulé des revenus en USD.  <br />Ex. Pour event\_name=achat avec days\_post\_attribution=2, la valeur reflète le revenu total des événements d’achat dans les deux jours qui suivent l’installation (et pas uniquement le deuxième jour). | double |
| skan\_duplicates | Les installations attribuées simultanément par SKAN et par d’autres méthodes AF sont ensuite supprimées pour éviter de compter les données SSOT deux fois. | long |
| uninstalls\_count | Nombre d'utilisateurs qui installent l'app et qui la désinstallent (la suppriment) par la suite (valable pour l'acquisition d'utilisateurs uniquement) | long |
| unique\_users | Nombre d’utilisateurs uniques qui produisent un événement. Les valeurs s’additionnent.  <br />Ex. Pour event\_name=achat avec days\_post\_attribution=2, la valeur reflète le nombre total d’utilisateurs qui ont acheté dans les deux jours qui suivent l’installation (et pas uniquement le deuxième jour). | int |

</Accordion>

<div id="modeled-data" />

<Accordion title="Données modélisées">

AppsFlyer modélise des données que les rapports de base de SKAdNetwork ne peuvent pas fournir.

* Valeurs de conversion (CV) nulles : Dans SKAN, Apple peut remplacer les données réelles par une valeur « Null » afin de protéger la confidentialité de l’utilisateur. Pour s’assurer qu’aucune donnée n’est omise, ces valeurs nulles sont modélisées dans la SSOT. <Anchor target="_blank" href="/marketers/fr/docs/skan-modeled-data#null-conversion-values">En savoir plus.</Anchor>
* Métriques post-installation plus longues : Il y a une diminution dans la précision des données de SKAN pour les périodes post-installation qui dépassent des deux premiers jours, ce qui peut entraîner des inexactitudes. Pour maintenir un haut niveau des données, nous modélisons les revenus et les utilisateurs uniques d’événements in-app avec une days\_post\_attribution supérieure à 2. <Anchor target="_blank" href="/marketers/fr/docs/skan-modeled-data#revenue-ltv">En savoir plus.</Anchor>

Données géographiques : SKAN limite la granularité des données, de fait les données géo sont souvent indisponibles. Lorsque cela se produit, nous modélisons les données pour permettre une bonne analyse des performances. <Anchor target="_blank" href="/marketers/fr/docs/skan-modeled-data#geo">En savoir plus.</Anchor>

</Accordion>

<div id="partial-data" />

<Accordion title="Données partielles">

Lors de l’analyse des jours d’installation récents, les mesures relatives aux périodes post-installation plus longues (ex. 7 jours) peuvent être approximatives. Dans ce cas, les mesures sont disponibles mais correspondent à des données partielles.

Quelques règles de base :

* Le rapport affiche toutes les données dès lors qu’elles sont disponibles.
* Après 5 jours, les mesures pour les deux jours post-installation sont complètes*.
* Après 7 jours, les mesures pour les sept jours post-installation sont complètes*. Jusqu’à 15 jours post-installation, le modèle peut continuer à affiner la valeur.

Pourquoi les données partielles apparaissent :

* Maturité des données : lorsque la période écoulée depuis le jour d’installation est plus courte que le nombre de jours analysés, les données continuent à arriver et ne sont pas complètes.
* Retards SKAN : Les données SKAN sont reçues avec un décalage aléatoire. Par exemple, l’activité post-installation des deux premiers jours peut être reçue jusqu’à 96 heures (4 jours) après l’installation.
* Synchronisation des données modélisées : Les données SKAN pour les périodes qui dépassent les 2 jours post-installation sont modélisées. Nos modèles génèrent la première estimation de valeur après 7 jours. Sur cette période (jours 2 à 7), les données issues des méthodes d’attribution classiques AppsFlyer sont disponibles, ce qui n’est pas le cas des données modélisées par SKAN.

Exemples (pour une date d’installation au 1er janvier) :

* Le 2 janvier : Les données SKAN n’ont pas encore été reçues. Les données des 2 jours post-installation seront égales aux données sur moins de 7 jours après l’installation. Toutes les données seront partielles, et composées des données issues des méthodes d’attribution classiques AppsFlyer.
* Le 3 janvier : Les données SKAN sont partiellement reçues. Les données des 2 jours post-installation sont toujours partielles, et contiennent alors partiellement des données SKAN. Les données des 7 jours suivant l’installation n’incluent pas encore de données SKAN modélisées (la première valeur modélisée est disponible 7 jours après l’installation). Par conséquent, entre 2 et 7 jours après l’installation, il est possible d’avoir un résultat plus petit pour les 7 jours post-installation que pour la période des 2 jours post-installation.
* Le 6 janvier : Les données SKAN des deux premiers jours qui suivent l’installation ont été entièrement reçues, y compris les postbacks qui ont le décalage le plus long. Les mesures des deux jours suivant l’installation sont terminées. À ce stade, les mesures des 7 jours suivant l’installation ne sont pas encore complètes.
* Le 8 janvier : Les données modélisées par SKAN pour les 7 jours post-installation sont terminées. Notre modèle continuera à affiner la valeur jusqu’au 16 janvier.

</Accordion>

<div id="directory-structure" />

## Structure du répertoire

<div id="report-folder-hierarchy" />

<Accordion title="Hiérarchie des dossiers d’un rapport">

* Les dossiers principaux sont organisés par type de rapport. Valeurs possibles : 'ssot\_unified', 'ssot\_retargeting' et 'ssot\_user\_acquisition.
* Dans ces dossiers, les sous-dossiers sont créés selon la date d’installation.

**Gérer les versions**

* Chaque dossier de jour d’installation contient plusieurs versions, qui sont créées quotidiennement.
* Chaque version présente le cumul des données mises à jour pour ce jour d’installation.
* Les rapports incluent toutes les données qui sont disponibles pour la date d’installation. Par exemple, au 18 avril, la dernière version de chaque jour d’installation contient toutes les données qui vont jusqu’au 18 avril.
* Conseil : Basez vous toujours sur la dernière version du rapport disponible pour garantir un résultat précis.

Chaque jour d’installation contient au maximum 15 versions. Après 15 jours, toutes les mesures ont été entièrement corrigées et sont terminées. <Anchor target="_blank" href="/marketers/fr/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">En savoir plus.</Anchor>

</Accordion>

<div id="directory-and-filename-structure" />

<Accordion title="Structure des répertoires et noms des fichiers">

Le chemin d’accès au rapport a le format suivant :

`<bucket-name>`/t=`<ssot_unified OR ssot_retargeting OR ssot_user_acquisition>`/install\_date=`<yyyy-mm-dd>`/version=`<unix timestamp>`/`<parquet file number>`

Exemple de structure de dossier dans le compartiment d’un annonceur :

```
bucket
|
└── t=ssot_unified
    |
    ├── install_date=2024-05-05
    |   |
    |   └── version=1714890235
    |   |    |
    |   |    ├── part-00000-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    |
    |   |    ├── part-00001-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |    │
    |   |    └── part-00002-4762858-d62a-446e-b499-dd05f2d5434d-c000.csv.gz
    |   |
    |   |
    |   └── version=1714890286
    |        |
    |        ├── part-00000-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        |
    |        ├── part-00001-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |        │
    |        └── part-00002-1d295376-d024-4321-8d34-1fbb37cbb58d-c000.csv.gz
    |   |
    .   . 
    .   .
```

Légende :

* t : Sujet du rapport (type).
* install\_date : La date de l’installation de l’application. Ce qui signifie que l’activité post-installation s’affiche en fonction du jour d’installation (où l’utilisateur a téléchargé l’app), et non en fonction du jour où l’action de l’utilisateur s’est produite.
* Version : Horodatage Unix indiquant quand la version a été créée.

</Accordion>

<div id="bi-developer-considerations" />

## Remarques pour les développeurs BI

**Portée des données dans le rapport :**

Les rapports contiennent des données sur les installations d’acquisition d’utilisateurs, les réattributions de retargeting (re-téléchargements dans SKAN) et les réengagements, ainsi que leurs événements in-app.

<div id="loading-reports" />

<Accordion title="Chargement des rapports">

Vous pouvez charger des rapports unifiés, rapports d’acquisition d’utilisateurs ou de retargeting, ensemble ou séparément, dans votre BI. Si vous les chargez ensemble et que vous souhaitez filtrer les vues par vous-même :

* Rapports unifiés : Utilisez is\_primary\_attribution=true ou le champ null.
* Rapports d’acquisition d’utilisateurs : Utilisez conversion\_type=Install.
* Rapports de retargeting : Utilisez conversion\_type=re-engagement ou re-attribution.
* Vue unifiée : Si vous utilisez la vue unifiée lors du chargement des données, vous pouvez classer les données par types de campagnes :

* Utilisez conversion\_type=install, re-engagement, ou re-attribution (re-téléchargements dans SKAN).
* Pour en savoir plus, consultez la section « Double attribution des événements de retargeting »

</Accordion>

<div id="days-postattribution" />

<Accordion title="Jours post-attribution">

<div id="important" />

> 🚧 **Attention !**
>
> Le rapport comprend une dimension (days\_post\_attribution) qui associe les revenus et les données d’utilisateurs uniques à un nombre défini de jours post-installation

* Pour les attributions (installations, réengagements, etc.), la valeur est 0.
* Pour les événements de revenus et les événements in-app, les données sont classées en cohortes prédéfinies, actuellement limitées à «2» jours et «7» jours après l’installation.

**Pour analyser avec précision les événements et revenus in-app, vous devez appliquer un filtre pour la dimension days\_post\_attribution.** Vous pouvez consulter l’exemple de requête ci-dessous.

Une erreur courante consiste à utiliser une méthode simplifiée qui additionne dans la colonne des revenus les chiffres pour un ensemble de dimensions donné. Ce calcul donne des chiffres incorrects, car certaines données de revenus sont comptées deux fois (une fois pour days\_post\_install=2 et une autre fois pour days\_post\_install=7). Cet exemple vaut également dans le cas de l’analyse des utilisateurs uniques pour des événements in-app précis.

</Accordion>

<div id="considerations" />

<Accordion title="Attention">

**N’oubliez pas** :

* Dernière version : Interrogez toujours la dernière version disponible pour chaque date d’installation afin de vous assurer que vous utilisez les données les plus récentes et précises pour votre analyse.
* Calcul des revenus : Les revenus en USD sont calculés en utilisant le taux de change au jour de l’événement.
* Analyser les attributions : les enregistrements où event\_name=af\_conversion reflètent les attributions (installations, réattributions (re-téléchargements dans SKAN) et les réengagements). Le nombre d’attributions s’affiche dans la mesure des utilisateurs uniques, et les données de revenus pour ces champs seront vides. La valeur pour days\_post\_attribution sera 0.
* Comparer les résultats avec le tableau de bord : Lorsque vous comparez les installations avec le tableau de bord, additionnez les types de conversion de téléchargement et d’installation, car le tableau de bord inclut les deux dans la colonne des installations.
* Analyser les événements in-app : Les enregistrements où event\_name n’est pas égal à « af\_conversion » indiquent des événements in-app. Le nombre d’utilisateurs uniques qui ont exécuté l’événement apparaît dans la mesure des utilisateurs uniques, tandis que les revenus générés par ces événements apparaissent dans les mesures du revenu.
* Type de conversion : cette dimension vous permet de faire la différence entre l’acquisition d’utilisateurs et les conversions de retargeting. Notez qu’une division supplémentaire pour les données SKAN est disponible (installations et re-téléchargements). Lorsque l’on compare les données au tableau de bord SSOT, les deux types sont vus comme des installations.
* Événement de revenus publicitaires : ils sont inclus lorsque disponibles.
* Segmentation des données : Toutes les données de l’app sont fournies dans un même fichier. Utilisez le champ ID d’app pour séparer les données par application, ou configurez Data Locker pour séparer chaque application.

</Accordion>

<div id="example-use-cases" />

<Accordion title="Exemple de cas d'utilisation">

Voici quelques exemples d’utilisation des données que les développeurs BI peuvent extraire via Data Locker. Chaque exemple propose une requête SQL et un exemple de visuel Excel.

<div id="calculating-total-attributions-per-campaign" />

<Accordion title="Calcul du nombre total d’attributions par campagne">

Dans cette requête, nous allons :

* Additionner le nombre total d’attributions uniques par campagne pour chaque jour d’installation.
* Filtrer les conversions avec le nom d’événement « af\_conversion » et un ID de campagne (af\_c\_id).

```sql
SELECT install_date, SUM(unique_users) AS total_attributions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign" />

<Accordion title="Calcul des conversions (installations et re-téléchargements) pour comparer aux installations par campagne unique dans le tableau de bord">

Dans cette requête, nous allons :

* Compter le nombre de conversions en séparant les nouvelles installations et les nouveaux téléchargements pour chaque campagne unique et par date d’installation.
* Comparer les installations avec la mesure des installations du tableau de bord, qui rassemble les types de conversion *install* (installation) et *re-download* (re-téléchargements).

```sql
SELECT install_date, conversion_type, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND af_c_id = '4475903638579'  -- Change to your specific campaign
    AND conversion_type IN ('install', 're-download')    
-- The dashboard sums both under the install field
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type;
```

</Accordion>

<div id="calculating-retargeting-conversions-per-geo" />

<Accordion title="Calcul des conversions de retargeting par zone géo">

Dans cette requête, nous allons :

* Compter le nombre de conversions provenant des campagnes de retargeting, réparties par zone géo.
* En considérant les types *re-attribution* et *re-engagement* pour ces conversions.

```sql
SELECT install_date, conversion_type, geo, SUM(unique_users) AS total_conversions
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type IN ('re-attribution', 're-engagement')    
-- Both types are relevant for re-targeting
    AND app_id = 'YOUR_APP'
GROUP BY install_date, conversion_type, geo;
```

</Accordion>

<div id="calculating-installs-by-attribution-method-per-media-source" />

<Accordion title="Calcul des installations par méthode d’attribution et source média">

Dans cette requête, nous allons :

* Compter le nombre d’installations par méthodes d’attribution (méthodes SKAN, AppsFlyer et organique) et les répartir par source média.
* Filtrer en fonction des événements af\_conversion avec le type de conversion *install*.

```sql
SELECT install_date, attribution_method, media_source, SUM(unique_users)   
AS total_installs
FROM ssot_unified
WHERE event_name = 'af_conversion'
    AND conversion_type = 'install'
    AND app_id = 'YOUR_APP'
GROUP BY install_date, attribution_method, media_source;
```

</Accordion>

<div id="calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset" />

<Accordion title="Calcul de l’ensemble des revenus 7 jours après l’installation pour Facebook par adset.">

Dans cette requête, nous mesurons le total des revenus dans les 7 jours qui suivent l’installation pour les publicités diffusées sur Facebook.

```sql
SELECT install_date,
       af_adset,
       SUM(revenue_usd) AS total_revenue_day_7
FROM ssot_unified
WHERE media_source = 'facebook'
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_adset;
```

</Accordion>

<div id="calculating-cumulative-revenue-for-selected-postinstall-periods" />

<Accordion title="Calcul des revenus cumulés pour des périodes post-installation données">

Dans cette requête, nous allons :

* Calculer l’ensemble des revenus sur plusieurs jours post-installation définis, en ventilant les chiffres au jour 2 et au jour 7.
* Notez que lors de l’analyse des installations des 7 derniers jours, les données des 7 jours suivant l’installation peuvent être incomplètes. <Anchor target="_blank" href="/marketers/fr/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">En savoir plus</Anchor>

```sql
SELECT install_date,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) AS total_revenue_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) AS total_revenue_day7
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source" />

<Accordion title="Calcul des revenus d’un événement in-app défini (achat) par source média">

Dans cette requête, nous allons :

* Mesurez la valeur des revenus d’un événement in-app donné (comme af\_purchase) et additionnez ces données par source média.
* Filtrer les résultats par jour post-installation pour vérifier que les données ne sont pas comptées en double.

```sql
SELECT install_date, media_source, SUM(revenue_usd) AS total_purchase_revenue
FROM ssot_unified
WHERE event_name = 'af_purchase'  -- Change to your specific event
    AND days_post_attribution = 7  -- Choose a specific post-install period (cohort)
    AND app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

<div id="calculating-inapp-event-conversion-rate-for-2-days-postinstalls" />

<Accordion title="Calcul du taux de conversion des événements in-app pour les 2 jours post-installation">

Dans cette requête, nous calculons le taux de conversion d’un événement in-app donné (comme af\_complete\_tutorial) par rapport à l’ensemble des installations.

```sql
SELECT install_date,
  SUM(IF(days_post_attribution = 2 AND   
event_name = 'af_complete_tutorial', unique_users, 0)) 
  / SUM(IF(event_name = 'af_conversion', unique_users, 0))   
AS conversion_rate_day2_af_tutorial_conversion
FROM ssot_unified
WHERE conversion_type = 'install'    
-- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date;
```

</Accordion>

<div id="calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id" />

<Accordion title="Calcul de l’ARPU pour les 7 jours et 2 jours post-installation par ID de campagne">

Dans cette requête, nous allons :

* Calculer le revenu moyen par utilisateur (ARPU) pour le jour 2 et le jour 7 post-installation dans l’ensemble des campagnes.
* Notez que lors de l’analyse des installations des 7 derniers jours, les données des 7 jours suivant l’installation peuvent être incomplètes. <Anchor target="_blank" href="/marketers/fr/docs/single-source-of-truth-ssot-data-locker-report-for-marketers#partial-data">En savoir plus</Anchor>

```sql
SELECT install_date,
       af_c_id,
       SUM(IF(days_post_attribution = 2, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day2,
       SUM(IF(days_post_attribution = 7, revenue_usd, 0)) 
       / SUM(IF(event_name = 'af_conversion', unique_users, 0)) AS ARPU_day7
FROM ssot_unified
WHERE conversion_type = 'install'  
       -- Choose the conversion types for the sample group you want to measure
    AND app_id = 'YOUR_APP'
GROUP BY install_date, af_c_id;
```

</Accordion>

<div id="calculating-amount-of-duplicates-per-media-source-in-this-query" />

<Accordion title="Calcul du nombre de doublons par source média dans cette requête">

Dans cette requête, nous calculons le nombre total d’attributions d’utilisateurs dupliquées par source média et date d’installation, afin de voir quels canaux média ont le plus de doublons dans l’attribution d’utilisateur.

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
    AND event_name = 'af_conversion'
GROUP BY install_date, media_source;
```

```sql
SELECT install_date, media_source, SUM(skan_duplicates)
FROM ssot_unified
WHERE app_id = 'YOUR_APP'
GROUP BY install_date, media_source;
```

</Accordion>

</Accordion>

<div id="traits-and-limitations" />

<Accordion title="Caractéristiques et limitations">

| Col a | Col b |
| --- | --- |
| Disponibilité des rapports par jour | Seuls les jours d’installation où la SSOT a été activée en fin de journée auront un rapport SSOT pour ce jour-là |
| Mesures 2 jours post-installation | <ul><li>Pour SKAN 4 dans Conversion Studio : les données correspondent aux 2 jours post-installation.</li><li>Pour SKAN 3 dans Conversion Studio : les données sont basées sur la fenêtre d’activité SKAN définie.<br />Ex. Si la fenêtre d’activité est de 24 heures, les événements qui se produisent dans cette fenêtre (même au jour X+1) sont comptés.</li></ul> |
| Disponibilité des événements in-app | <ul><li>Disponible uniquement pour les événements configurés dans SKAN Conversion Studio.</li><li>Disponible uniquement pour les événements qui se sont produits pendant la fenêtre 1.</li></ul> |
| Revenus | Si le revenu SKAN n'est configuré que pour certains événements, la mesure du revenu SSOT prend en compte uniquement les événements de revenu transmis par AF qui correspondent. |
| Répartition des re-téléchargements SKAN | Disponible. Dans le tableau de bord SSOT, cette répartition n’est pas disponible et les installations et re-téléchargements sont compris dans la mesure des installations. |
| Modifications de la configuration de SKAN Conversion Studio | Modifier la configuration de SKAN Conversion Studio peut entraîner des inexactitudes dans les données SSOT pendant environ 96 heures, puisque les postbacks des installations encodées avec le précédent schéma continuent à arriver. |
| Fuseau horaire | Le fuseau horaire spécifique à l’application n’est pas disponible. |
| Données organiques | <ul><li>Disponible pour les mesures des 2 jours post-installation.</li><li>Indisponible pour les mesures des 7 jours post-installation.</li></ul> |
| Données des jours post-conversion (installation, réattribution, réengagement) | Limité à 7 jours après la conversion |
| Transparence de l'agence | Pris en charge |
| Changements de nom de campagne | Pas de prise en charge. Utilisez l’ID de campagne pour regrouper et filtrer si les noms de campagne ont été modifiés. |
| Réseaux publicitaires | <ul><li>Peut accéder aux rapports DataLocker SSOT pour voir les données attribuées à leur source média si :<ul><li>L’annonceur a activé la SSOT dans Conversion Studio.</li><li>Le réseau publicitaire mène des campagnes SKAN.</li><li>Le réseau publicitaire doit disposer des [autorisations](/docs/single-source-of-truth-ssot-data-locker-report-for-ad-networks#permissions) données par l'annonceur pour accéder aux données agrégées.</li></ul></li></ul> |
| Autorisations de l'agence | Non disponible. Les utilisateurs de l’agence peuvent afficher les données SSOT dans le tableau de bord SSOT. |
| Mesures du J7 | <ul><li>Peuvent être manquantes ou inférieures aux mesures du J2 si :<ul><li>La période comprend des dates qui ont moins de 8 jours.</li><li>Les données modélisées ne sont pas disponibles (ex. moins de 14 jours de données sur les revenus). <Anchor target="_blank" href="/marketers/fr/docs/skan-modeled-data#revenue-ltv">En savoir plus.</Anchor></li><li>La configuration de SKAN Conversion Studio a été modifiée au cours des 14 derniers jours.</li><li>Il y a moins de 10 installations pour une date donnée.</li></ul></li></ul> |
| Nom d'événement prédéfini | Comme le nom d’événement af\_conversion est utilisé pour indiquer différents types de conversions, les apps qui ont un événement spécifiquement nommé af\_conversion verront le nom de leur événement d’origine changé en af\_conversion\_event. |
| Différences pour la devise locale | Comme le tableau de bord SSOT et le rapport DataLocker SSOT ne sont pas calculés simultanément, de petits écarts peuvent exister entre les revenus en devise locale dans le tableau de bord, et la devise définie dans le rapport. Cela est dû aux légères différences dans le taux de change utilisé au moment des calculs. |
| Données partielles de SKAN au J7 | Étant donné que les données SKAN au J7 sont modélisées et que la version initiale est prête 7 jours après l’installation, les données au J7 seront partielles lors de l’analyse des mesures au J7. Pour les enregistrements dont la méthode d’attribution est SKAN, les mesures au J7 seront inférieures aux mesures du J2. |
| Granularité limitée pour les revenus J7 et les mesures d’événements in-app | Les mesures des revenus et des événements d’utilisateurs uniques pour les 7 jours post-installation ne sont pas disponibles aux niveaux adset, publicité et type de conversion. Comme ce degrés de précision n’est généralement pas disponible dans SKAN, le modèle ne tient pas compte ces dimensions. |

</Accordion>

<div data-zendesk-anchors="h_01J455DHWAB1J9611A4KA40PZM=remarque ssot-reports-in-data-locker=quest-ce-que-data-locker- h_01J454K90GWKME8F4JCDQKM3CK=quest-ce-que-data-locker- what-is-single-source-of-truth-ssot=quest-ce-que-la-single-source-of-truth-ssot- h_01J454K90GRCFR3PSAQRTX98B4=quest-ce-que-la-single-source-of-truth-ssot- benefits-of-ssot-reports-in-data-locker=int%C3%A9r%C3%AAts-des-rapports-ssot-dans-data-locker h_01J454PANH9J6ZZ069RS6FVWZM=int%C3%A9r%C3%AAts-des-rapports-ssot-dans-data-locker h_01J46C54ZB4YYTZ6CDHHC0EC8P=setting-up-data-locker h_01J455Q07J5XPYEBVP3BZ1FMVH=permissions h_01J29BTC9CESJF592P616WMK46=ssot-report-facts report-structure::673746b9=structure-du-rapport h_01J29CQ5K4JBEP4X8YQ0V32WYR=structure-du-rapport h_01J29CHBX2QNFTAQSA1W01PFH0=field-formats h_01J29BTC9CJ8GZDDCHK9NBZ4YX=dimensions h_01J29BTC9C86YMVEY17QQZNZCV=metrics h_01J29BTC9CH3DAA7ZRHG8C04MF=modeled-data h_01J29M72WAPH3KEW9N60JHTT3W=partial-data directory-structure=structure-du-r%C3%A9pertoire h_01J29MB7B7Q3PJ9YWFQESWN0KD=structure-du-r%C3%A9pertoire h_01J29MCSH4V41CPB7ZG41751QW=report-folder-hierarchy h_01J29MCSH40ATHNAJMY8KR7ANZ=directory-and-filename-structure bi-developer-considerations=remarques-pour-les-d%C3%A9veloppeurs-bi h_01J29MS6XV7XYTA9Q81454WEQN=remarques-pour-les-d%C3%A9veloppeurs-bi h_01J2F4HG8YHDGYFKHBBC5KSN2G=loading-reports h_01J2F4HG8YKNEVGEWTR91ADSDS=days-postattribution h_01J3YT1X908JVMDXKRQBCRD1JR=attention- h_01J2F4HG8YAAE0E04Y6Q9Z62NZ=considerations h_01J3A82HZF14CCS027FE991M0T=example-use-cases h_01J3A883DQFQE0WTTY4FMX3AQ4=calculating-total-attributions-per-campaign h_01J3A883DQ82K71XY408M2BW0B=calculating-conversions-installs-redownloads-to-compare-to-the-installs-in-the-dashboard-per-unique-campaign h_01J3A883DQ5QAVH6AX7CGCBSWG=calculating-retargeting-conversions-per-geo h_01J3A883DQE25X31SPPF166BRH=calculating-installs-by-attribution-method-per-media-source h_01J3A883DQ8QVR8WKPPX1QF414=calculating-cumulative-revenue-of-7-days-postinstall-for-facebook-per-adset h_01J3A883DQ51T3Z6H239P5JDJ1=calculating-cumulative-revenue-for-selected-postinstall-periods h_01J3A883DQXRCQ4NWY0BCX886E=calculating-revenue-from-a-specific-inapp-event-purchase-per-media-source h_01J3A883DQRR62BWQ6JBTZ7238=calculating-inapp-event-conversion-rate-for-2-days-postinstalls h_01J3A883DRPEVDQCWKCT9M3EC1=calculating-arpu-for-7-days-and-2-days-postinstall-per-campaign-id h_01J3A883DRRZ9Y8F3KNAAPZT2S=calculating-amount-of-duplicates-per-media-source-in-this-query h_01J29MV69M667QDHMS5WGYKPCZ=traits-and-limitations" />
