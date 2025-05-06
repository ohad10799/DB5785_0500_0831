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

![](images/image2.png){width="5.768055555555556in"
height="2.2708333333333335in"}

**SQL Scripts**

Provide the following SQL scripts:

-   **Create Tables Script** - The SQL script for creating the database
    tables is available in the repository:

```{=html}
<!-- -->
```
-   **Insert Data Script** - The SQL script for insert data to the
    database tables is available in the repository:

```{=html}
<!-- -->
```
-   **Drop Tables Script** - The SQL script for droping all tables is
    available in the repository:

```{=html}
<!-- -->
```
-   **Select All Data Script** - The SQL script for selectAll tables is
    available in the repository:

**Data**

> **First tool: using [mockaro](https://www.mockaroo.com/) to create csv
> file**
>
> **Entering a data to guest table:**
>
> ![](images/image3.png){width="5.768055555555556in"
> height="1.9444444444444444in"}
>
> ![](images/image4.png){width="5.768055555555556in"
> height="3.109027777777778in"}
>
> **Second tool:
> using [generatedata](https://generatedata.com/generator). to create
> csv file**
>
> **Entering a data to incidentType table:**
>
> ![](images/image5.png){width="5.768055555555556in"
> height="1.2590277777777779in"}
> ![](images/image6.png){width="4.46696741032371in"
> height="2.807853237095363in"}
>
> **Third tool: using python to create csv file**
>
> **Part of Python code:**
>
> ![](images/image7.png){width="5.768055555555556in"
> height="2.4180555555555556in"}
>
> **Sql file made from the python script:**
>
> ![](images/image8.png){width="3.1223600174978126in"
> height="3.62834208223972in"}
>
> **Backup**

-   **backups files are kept with the date of the backup:**

> ![](images/image9.png){width="5.768055555555556in"
> height="0.22291666666666668in"}
