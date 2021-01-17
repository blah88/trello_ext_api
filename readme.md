# **Richard_Noh_T3A3**

AWS database @ 35.175.102.155
Github link: https://github.com/blah88/trello_ext_api

This is an attempt at creating an extension to Trello boards which attempts to enable users to add parent-child relationship to lists and cards in terms of property and visually to create a mind-map. Lists and cards may be placed at all directions instead of just orthogonal postions as per current set up. It is still WIP and database is not properly set up yet although you can connect to it since it is still deployed at AWS.   


## **R2 - Hash passwords, Use ORMs to handle SQLs**

Discuss how the application will handle the privacy of user data within the system, and how security features of the frameworks you are utilising will assist to mitigate security concerns.  
  
Object Relational Mapping (ORM) frameworks to make the translation of SQL result sets into code objects more seamless. ORM tools often mean developers will rarely have to write SQL statements in their code which use parameterized statements under the hood. This will lessen the likelihood of SQL injection attacks.

The API framework will sanitise user input.

User passwords will be hashed which add a layer of protection.

The combination of these measures will give some level of security and enhence user's privacy.




## **R3 - General security, CITD**

Discuss how you will address the following obligations as a developer:  
- professional obligations (delivering the project on time, being explicit about ongoing maintenance of the system)  
**CITD** WIP

- ethical obligations: ensuring that the application conforms with ethical codes of conduct approved by industry  
**Thorough terms and conditions. Handling of offensive material.** 

- legal obligations: that you have assessed whether the application is subject to any legal regulation, if none, consider any privacy implications
**Compliance.** 
**Legal requirements for data storage (PCI DSS)**

Terms and Conditions 

Ethical Obligations as a User: By joining our service you as a user agree to use our service that offensive materials defined by the Summary Offences Act 1988. Further information on what can be considered offensive or harmful is outlined by the following link:
https://www.esafety.gov.au/report/illegal-harmful-content/what-we-can-investigate

If an ample number of complaints are made the content in question will be investigated and dealt with.

This application adhere to all Australian laws. Some of these legislations include the Privacy Act 1988, the Privacy and Personal Information Act 1998 (NSW), the Telecommunications Act 1997 (Cth) and the Telecommunications (Intercetion and Access) Act 1979 (Cth). 

We respect user privacy until incriminating evidence against a user is found. 





## R4 - Develop a server-side application on Python which implements a data model and validates data in terms of its type and whether it is required.

**User input validation - Day 11**
schema and main


## R5 - Implement code using a Python framework to create, read, update and delete records, and export all data from the database from the database.

**Use flask and CRUD resource. Modular programming.**




## R6 - Develop a user interface using an HTML template that replicates user functionalities and displays data in a tabular format.

**Display data. HTML, CSS, JINJA (DO IT LAST)**




## R7 - Develop an API endpoint which requires a query that retrieves data from the database and does a SUM, AVERAGE, MIN, MAX or other operation requiring data to be parsed and aggregated.

**Extra class method in the admin model. Just one method only.**




## R8 - Checks for null values and provides error checking to ensure integrity of information in the database. 
For example: clearly indicate how you have tested the integrity of the data for entities to ensure that data will not lead to a database with incomplete data, or data that is not appropriate (for example: properties should have a size limit appropriate for the data held)

**Error messages for wrong input**




# R9 - Write a SQL script to implement a database. The script must define:
 tables  
- fields with validation  
- relationships between tables  
  
Your database must have at least FIVE tables which demonstrate:  
- one to many relationships  
- one to one relationships

**Use of Flask migrate**



## R10 - Write at least THREE SQL queries which involve the selecting, filtering, grouping and ordering data.

**SQL Alchemy , Day 10**



## R11 - Write TWO SQL queries which join tables.

**SQL Alchemy , Day 10**
Outer left etc. 


## R12 - Write a SQL statement which retrieves all data from the database.
