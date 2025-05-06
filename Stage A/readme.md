**Hotel Management System - README**

**Submitted by:** Ohad Kahlon and Meir Revivo\
**System Component:** Guests management.

**Table of Contents**

1.  Introduction

2.  Entity-Relationship Diagram (ERD)

3.  Data Structure Diagram (DSD)

4.  Design Decisions

5.  Data Input Methods

6.  Backup and Restore Procedures

7.  Screenshots

**Introduction**

The Hotel Management System is designed to store and manage
guest-related data efficiently. It provides functionalities such as
guest check-in and check-out, room assignments, billing, and service
requests. The goal of the system is to streamline hotel operations and
enhance customer service.

**Entity-Relationship Diagram (ERD)**

![](images/image1.png)

**Data Structure Diagram (DSD)**

![](images/image2.png)


**Data**

> **First tool: using [mockaro](https://www.mockaroo.com/) to create csv
> file**
>
> **Entering a data to guest table:**
>
> ![](images/image3.png)
>
> ![](images/image4.png)
>
> **Second tool:
> using [generatedata](https://generatedata.com/generator). to create
> csv file**
>
> **Entering a data to incidentType table:**
>
> ![](images/image5.png)
> ![](images/image6.png)
>
> **Third tool: using python to create csv file**
>
> **Part of Python code:**
>
> ![](images/image7.png)
>
> **Sql file made from the python script:**
>
> ![](images/image8.png)
>
> **Backup**

-   **backups files are kept with the date of the backup:**

> ![](images/image9.png)
