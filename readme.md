# **Richard_Noh_T3A3**

Data structure of Trello extension API

User

Board

List

Card




## **R2 - Hash passwords, Use ORMs to handle SQLs**

Discuss how the application will handle the privacy of user data within the system, and how security features of the frameworks you are utilising will assist to mitigate security concerns.  
  
Example: discuss how the use of ORMs mitigate SQL injection attacks, and how API frameworks such as ExpressJS can handle the sanitisation of user input.

 **- User passwords are to be hashed.**

 **- SQL will be handled by ORM minimise SQL injection attacks.**
 
 **- API frameworks will sanitise user input.**




## **R3 - General security, CITD**

Discuss how you will address the following obligations as a developer:  
- professional obligations (delivering the project on time, being explicit about ongoing maintenance of the system)  
**CITD**

- ethical obligations: ensuring that the application conforms with ethical codes of conduct approved by industry  
**Thorough terms and conditions. Handling of offensive material.** 

- legal obligations: that you have assessed whether the application is subject to any legal regulation, if none, consider any privacy implications
**Compliance.** 
**Legal requirements for data storage (PCI DSS)**



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
