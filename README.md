# Data Engineering Project
## Project Description
This project implemented a an ETL pipeline to produce a report that identified and provided customer account details on customers that were upgraded to Fibre Internet service but still had an active DSL accounts, despite the customer requesting the DSL account to be terminated
<br></br>

## Problem Definition
The company was carrying out a campaign to upgrade residential customers with DSL Internet service to Fibre Internet service in a number of locations. 

While the installation of the Fibre service for customers who opted to upgrade their DSL service was carried out without problems, there was an issue where many customers DSL accounts that were marked for termination were not being forwarded to the customer accounts termination team. This caused a backlogs of DSL accounts to be terminated and resulted in those customers being billed for both Fibre and DSL services.

This issue was, in part due to the campaign bundling of two separate services into one – installation of a new service, and termination of a service – and not having a system in place to automatically identify those DSL accounts to be terminated, and subsequently, sending those accounts to the termination team.
<br></br>


## solution implemented
Because there was no information in a given customer’s Fibre account record that indicated if such account has a corresponding DSL account, and secondly, if that DSL account is active, a method developed to get this information.

This was done by checking if any of the ‘contact number’ fields (contact_no1, contact_no2, constact_no3 fields) of each new Fibre account had an active DSL telephone number (active means not terminated). 

If any of the ‘contact number’ had an active DSL telephone number, then the Fibre account was then linked to the DSL account. This meant that Fibre account and the DSL account was assumed to belong to the same customer.

To further test this hypothesis, the name and address of the Fibre account was checked against the corresponding name and address of DSL account. In cases where there was a predefined minimum percentage match (e.g., 20% match) between the name of the Fibre account and the name in the DSL account, and similarly, a predefined minimum percentage match between the address of the Fibre account and the address DSL account, it was concluded that those accounts belong to the same customers.
<br></br>


## Data Architecture Diagram
![data_pipeline_architecture](https://github.com/shwcl/ETL-pipeline_DSL-customer-accounts/assets/52106536/89b8816e-f3c1-42ed-b1ac-962a9bf6dd97)
<br></br>


## Pentaho Data Integration ETL Job
![Pentaho_ETL](https://github.com/shwcl/ETL-pipeline_DSL-customer-accounts/assets/52106536/7a1159b4-fd95-41b0-b83f-e78083c69a41)
<br></br>


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

