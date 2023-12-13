![data_pipeline_architecture](https://github.com/shwcl/ETL-pipeline_DSL-customer-accounts/assets/52106536/61341d2c-3af6-45f5-b16e-c49a5fb40f88)# Data Engineering Project
This project implemented a an ETL pipeline to produce a report that identified and provided customer account details on customers that were upgraded to Fibre Internet service but still had an active DSL accounts, despite the customer requesting the DSL account to be terminated


## Background
The company was carrying out a campaign to upgrade residential customers with DSL Internet service to Fibre Internet service in a number of locations. 

While the installation of the Fibre service for customers who opted to upgrade their DSL service was carried out without problems, there was an issue where many customers DSL accounts that were marked for termination were not being forwarded to the customer accounts termination team. This caused a backlogs of DSL accounts to be terminated and resulted in those customers being billed for both Fibre and DSL services.

This issue was, in part due to the campaign bundling of two separate services into one – installation of a new service, and termination of a service – and not having a system in place to automatically identify those DSL accounts to be terminated and sending those accounts to the termination team.


## Data Architecture Diagram
![Upl{"payload":{"allShortcutsEnabled":true,"fileTree":{"":{"items":[{"name":".gitattributes","path":".gitattributes","contentType":"file"},{"name":"ETL-Pipeline-Architecture.pdf","path":"ETL-Pipeline-Architecture.pdf","contentType":"file"},{"name":"ETL_pipeline_DSL_cust_diag.png","path":"ETL_pipeline_DSL_cust_diag.png","contentType":"file"},{"name":"Python_script_validate_DSL_accounts.py","path":"Python_script_validate_DSL_accounts.py","contentType":"file"},{"name":"README.md","path":"README.md","contentType":"file"},{"name":"sql_script-generate_final_report.sql","path":"sql_script-generate_final_report.sql","contentType":"file"}],"totalCount":6}},"fileTreeProcessingTime":2.4341749999999998,"foldersToFetch":[],"reducedMotionEnabled":"system","repo":{"id":707841601,"defaultBranch":"main","name":"ETL-pipeline_DSL-customer-accounts","ownerLogin":"shwcl","currentUserCanPush":true,"isFork":false,"isEmpty":false,"createdAt":"2023-10-20T15:32:05.000-04:00","ownerAvatar":"https://avatars.githubusercontent.com/u/52106536?v=4","public":false,"private":true,"isOrgOwned":false},"symbolsExpanded":true,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1702462584.0","canEdit":true,"refType":"branch","currentOid":"2e491eb1fe47df367f685b9c92bc3e597d08fdf7"},"path":"ETL_pipeline_DSL_cust_diag.png","currentUser":{"id":52106536,"login":"shwcl","userEmail":"shw_cl@hotmail.com"},"blob":{"rawLines":null,"stylingDirectives":null,"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":null,"configFilePath":null,"networkDependabotPath":"/shwcl/ETL-pipeline_DSL-customer-accounts/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":false,"repoAlertsPath":"/shwcl/ETL-pipeline_DSL-customer-accounts/security/dependabot","repoSecurityAndAnalysisPath":"/shwcl/ETL-pipeline_DSL-customer-accounts/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":true},"displayName":"ETL_pipeline_DSL_cust_diag.png","displayUrl":"https://github.com/shwcl/ETL-pipeline_DSL-customer-accounts/blob/main/ETL_pipeline_DSL_cust_diag.png?raw=true","headerInfo":{"blobSize":"48 KB","deleteInfo":{"deleteTooltip":"Delete this file"},"editInfo":{"editTooltip":"Edit this file"},"ghDesktopPath":"x-github-client://openRepo/https://github.com/shwcl/ETL-pipeline_DSL-customer-accounts?branch=main&filepath=ETL_pipeline_DSL_cust_diag.png","gitLfsPath":null,"onBranch":true,"shortPath":"c85a2ea","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fshwcl%2FETL-pipeline_DSL-customer-accounts%2Fblob%2Fmain%2FETL_pipeline_DSL_cust_diag.png","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":null,"truncatedSloc":null},"mode":"file"},"image":true,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":null,"languageID":null,"large":false,"loggedIn":true,"newDiscussionPath":"/shwcl/ETL-pipeline_DSL-customer-accounts/discussions/new","newIssuePath":"/shwcl/ETL-pipeline_DSL-customer-accounts/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/shwcl/ETL-pipeline_DSL-customer-accounts/blob/main/ETL_pipeline_DSL_cust_diag.png","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/shwcl/ETL-pipeline_DSL-customer-accounts/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"rawBlobUrl":"https://github.com/shwcl/ETL-pipeline_DSL-customer-accounts/raw/main/ETL_pipeline_DSL_cust_diag.png","renderImageOrRaw":true,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"shwcl","repoName":"ETL-pipeline_DSL-customer-accounts","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":null,"actionsOnboardingTip":null},"truncated":false,"viewable":false,"workflowRedirectUrl":null,"symbols":null},"copilotInfo":{"documentationUrl":"https://docs.github.com/copilot/overview-of-github-copilot/about-github-copilot-for-individuals","notices":{"codeViewPopover":{"dismissed":false,"dismissPath":"/settings/dismiss-notice/code_view_copilot_popover"}},"userAccess":{"accessAllowed":false,"hasSubscriptionEnded":false,"orgHasCFBAccess":false,"userHasCFIAccess":false,"userHasOrgs":false,"userIsOrgAdmin":false,"userIsOrgMember":false,"business":null,"featureRequestInfo":null}},"copilotAccessAllowed":false,"csrf_tokens":{"/shwcl/ETL-pipeline_DSL-customer-accounts/branches":{"post":"HEDVbstNJZgqmJY-La2s9abTT0FubcJWIUtMH_TsIzON2kuke6QNW0YYKvLsDvfGD92SFkge4cD6aZwT3gbZIQ"},"/repos/preferences":{"post":"9jYgYEa7-kBDHlg9id0tirnMHkZzynUFDNbb3d1O4SpPNPGxAOmwVd89Lw92SIrJehF9PaAUdf40gC5CYTX2_Q"}}},"title":"ETL-pipeline_DSL-customer-accounts/ETL_pipeline_DSL_cust_diag.png at main · shwcl/ETL-pipeline_DSL-customer-accounts"}oading data_pipeline_architecture.png…]()


![stamp_paid](https://github.com/shwcl/ETL-pipeline_DSL-customer-accounts/assets/52106536/50eb380f-8454-4c69-9eba-971ac7c19205)


## Development Process
1. Generate a dataset of new Fibre accounts that have active DSL accounts. This was done by checking if the ‘contact number’ fields (contact_no1, contact_no2, constact_no3 fields) of the Fibre account has a valid and active DSL telephone number. If one of the ‘contact number’ has an active DSL number, this validate that Fibre account and the DSL account belong to the same customer

2. For further validate that the two accounts belong to the same customer, extract the name and address columns (and primary key fields) of the Fibre account and corresponding DSL account from the dataset to a CSV file 

3. Write a Python script to read the CSV file to check if the NAME field of each Fibre account corresponds with the NAME field of its related DSL account and similarly, to check if the ADDRESS field of the Fibre account corresponds with the ADDRESS field its related DSL account. Specifically, the script did the following:
    - Calculates the number of non-blank strings in each NAME field of each Fibre account that matches with a non-blank string in corresponding NAME field of the DSL account</li>
    - Calculates the number of non-blank strings in the ADDRESS field of each Fibre account that matches with a non-blank string in the corresponding ADDRESS field of the DSL account </li>
    - Outputs the results to a new CSV file </li>


4. Load the CSV file to a new table in Snowflake and merged it with original dataset 

5. With the new merged dataset, use SQL to generate a final dataset that output all the fields in the merged dataset, along with generate two additional fields (e.g. NAME_MATCH_PERCENT, ADDRESS_MATCH_PERCENT) that calculate the match percentage between the two NAME fields and the two ADDRESS fields respectively

6. Write an SQL script to generate the final report based on the final dataset that includes a condition that specifies the same minimum value for both the NAME_MATCH_PERCENT and ADDRESS_MATCH_PERCENT_MATCH fields (e.g. NAME_MATCH_PERCENT > 20)
<br> </br>


## Tools Used

Python, SQL, Pentaho Data Integration and Snowflake data warehouse
<br></br>

## Summary

More than 10 hours of manual work was save on a weekly basis by having this process developed and automated. Moreover, the backlogs of request to terminate DSL accounts were reduced significantly within a month.

