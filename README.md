** Development of ETL pipeline that generated a report on customers upgraded to Fibre Internet service and still have active DSL Internet service **




BACKGROUND

The client was carrying out a campaign to upgrade residential customers with DSL Internet service to Fibre Internet service in a number of locations. 

While the installation of the Fibre service for customers who opted to upgrade their DSL service was carried out without problems, there was an issue where many customers DSL accounts that were marked for termination were not being forwarded to the customer accounts termination team. This caused a backlogs of DSL accounts to be terminated and resulted in those customers being billed for both Fibre and DSL services.

This issue was, in part due to the campaign bundling of two separate services into one – installation of a new service, and termination of a service – and not having a system in place to automatically identify those DSL accounts to be terminated and sending those accounts to the termination team.


MY ROLE

My role as a Data Engineer was to develop a system of identifying those residential DSL customers who were upgraded to Fibre service but still had an active DSL service that was marked for termination.


WHAT I DID

I built an ETL pipeline that generated a report that identified and provided details on customers that were upgraded to Fibre Internet service but still had an active DSL accounts, despite the customer requested the DSL account be terminated



DEVELOPMENT PROCESS

-	Generate a dataset of new Fibre accounts that have active DSL accounts. This was done by checking if the ‘contact number’ fields (contact_no1, contact_no2, constact_no3 fields) of the Fibre account has a valid and active DSL telephone number. If one of the ‘contact number’ has an active DSL number, this validate that Fibre account and the DSL account belong to the same customer

-	For further validate that the two accounts belong to the same customer, extract the name and address columns (and primary key fields) of the Fibre account and corresponding DSL account from the dataset to a CSV file 

-	Write a Python script to read the CSV file to check if the NAME field of each Fibre account corresponds with the NAME field of its related DSL account and similarly, to check if the ADDRESS field of the Fibre account corresponds with the ADDRESS field its related DSL account. 

Specifically, the script did the following:


o	Calculates the number of non-blank strings in each NAME field of each Fibre account that matches with a non-blank string in corresponding NAME field of the DSL account
o	Calculates the number of non-blank strings in the ADDRESS field of each Fibre account that matches with a non-blank string in the corresponding ADDRESS field of the DSL account 
o	Outputs the results to a new CSV file


-	Load the CSV file to a new table in Snowflake and merged it with original dataset 

-	With the new merged dataset, use SQL to generate a final dataset that output all the fields in the merged dataset, along with generate two additional fields (e.g. NAME_MATCH_PERCENT, ADDRESS_MATCH_PERCENT) that calculate the match percentage between the two NAME fields and the two ADDRESS fields respectively

-	Write an SQL script to generate the final report based on the final dataset that includes a condition that specifies the same minimum value for both the NAME_MATCH_PERCENT and ADDRESS_MATCH_PERCENT_MATCH fields (e.g. NAME_MATCH_PERCENT > 20)



TOOLS USED

Python, SQL, Pentaho Data Integration and Snowflake data warehouse
<pre>
</pre>
SUMMARY OF PROJECT’S SUCCESS
More than 10 hours of manual work was save on a weekly basis by having this process developed and automated. Moreover, the backlogs of request to terminate DSL accounts were reduced significantly within a month.

