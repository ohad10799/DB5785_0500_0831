**Hotel Management System - README**

**Submitted by:** Ohad Kahlon and Meir Revivo\
**System Component:** Guests management.

**Table of Contents**

1.  Introduction

2.  Entity-Relationship Diagram (ERD)

3.  Data Structure Diagram (DSD)

4.  Data Input Methods

5.  Backup and Restore Procedures

6.  Queries

7. Constraints

8. Rollback and Commit:


**1) Introduction**

The Hotel Management System is designed to store and manage
guest-related data efficiently. It provides functionalities such as
guest check-in and check-out, room assignments, billing, and service
requests. The goal of the system is to streamline hotel operations and
enhance customer service.

**2) Entity-Relationship Diagram (ERD)**

![](images/image1.png)

**3) Data Structure Diagram (DSD)**

![](images/image2.png)


**4) Data input methods**

> **First tool: using [mockaro](https://www.mockaroo.com/)o to create
> csv file**
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
> **5) Backup**

-   **backups files are kept with the date of the backup:**

> ![](images/image9.png)
>
> **6) Queries**
>
> **Select:**

1)  [רשימת האורחים שהיו להם תקריות פתוחות, ופרטי התקרית ביחד עם פרטי
    האורח]

> ![](images/image10.png)
>
> ![](images/image11.png)

2)  [מספר ההזמנות לפי סוג חדר]

![](images/image12.png)

![](images/image13.png)

3)  [כל המשובים מתחת לדירוג 3 שנכתבו בחודשים שונים]

![](images/image14.png)
![](images/image15.png)



4)  [מספר הלילות שכל אורח שהה במלון]

![](images/image16.png)



5)  [רשימת אורחים עם מנוי ברמה גבוהה מ7]

![](images/image18.png)

![](images/image19.png)



6)  [אורחים שהשאירו פידבק על יותר מהזמנה אחת]

> ![](images/image20.png)


7)  ![](images/image22.png)[תאריכי הדיווחים לפי סוג
    התקרית]

> ![](images/image23.png)

8)  [דירוג ממוצע של פידבק לפי רמת המנוי]

> ![](images/image24.png)

![](images/image25.png)

**Delete:**

1.  [מחיקת כל הפידבקים מתחת לדירוג 2]

(images/image26.png)
>
> [מסד הנתונים לפני השינוי:]
>
> ![](images/image27.png)
>
> [מסד הנתונים לאחר השינוי:]
>
> ![](images/image28.png)

2.  [מחיקת מנויים שאין להם נקודות כלל]

> ![](images/image29.png)

[מסד הנתונים לפני השינוי:]

(images/image30.png)

[מסד הנתונים לאחר השינוי:]

(images/image31.png)

3.  [מחיקת תקריות שנסגרו לפני יותר משנה]

> ![](images/image32.png)[מסד הנתונים לפני השינוי:]
>
> ![](images/image33.png)
>
> [מסד הנתונים לאחר השינוי:]
>
> ![](images/image34.png)

**Update:**

1.  [עדכון סטטוס התקריות שגילן מעל חודש לסגורות]

> ![](images/image35.png)

[מסד הנתונים לפני השינוי:]

![](images/image36.png)

[מסד הנתונים לאחר השינוי:]

(images/image37.png)

2.  [עדכון דירוג של פידבקים בלי תיאור לדירוג 3]

> ![](images/image38.png)
>
> [מסד הנתונים לפני השינוי:]
>
> ![](images/image39.png)

[מסד הנתונים לאחר השינוי:]

![](images/image40.png)

3.  ![](images/image41.png)[העלאת רמת המנוי לכל מי שיש לו מעל 80
    נקודות]

[מסד הנתונים לפני השינוי:]

![](images/image42.png)

[מסד הנתונים לאחר השינוי:]

![](images/image43.png)

**7) Constraints:**

1.  [חובה להכניס מספר טלפון לאורח]

> ![](images/image44.png)
>
> [ניסיון הכנסת נתון שסותר את האילוץ:]
>
(images/image45.png)

2.  [ברירת מחדל לסטטוס תקרית יהיה \'פתוח\']

> ![](images/image46.png)

[ניסיון להכנסת נתונים:]

![](images/image47.png)

![](images/image49.png)

3.  [אילוץ שתאריך הכניסה יהיה לפני תאריך היציאה]

> ![](images/image50.png)

[ניסיון להכנסת נתונים וסתירת האילוץ:]

![](images/image51.png)

**8) Rollback and Commit:**

![](images/image52.png)

[הנתונים לפני הטרנזקציה:]

![](images/image53.png)

[השינוי:]

![](images/image54.png)

[לאחר]ROLLBACK[:]

![](images/image55.png)

![](images/image56.png)



[המצב לפני השינוי:]

![](images/image57.png)

[המצב אחרי השינוי:]

![](images/image58.png)

[המצב לאחר] commit[:]

![](images/image59.png)
