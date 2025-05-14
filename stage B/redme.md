**Hotel Management System - README**

**Submitted by:** Ohad Kahlon and Meir Revivo
**System Component:** Guests management.

**Table of Contents**

1. Introduction
1. Entity-Relationship Diagram (ERD)
1. Data Structure Diagram (DSD)
1. Design Decisions
1. Data Input Methods
1. Backup and Restore Procedures
1. Screenshots

**Introduction**

The Hotel Management System is designed to store and manage guest-related data efficiently. It provides functionalities such as guest check-in and check-out, room assignments, billing, and service requests. The goal of the system is to streamline hotel operations and enhance customer service.

**Entity-Relationship Diagram (ERD)**

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.001.png)











**Data Structure Diagram (DSD)**

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.002.png)







**SQL Scripts**

Provide the following SQL scripts:

- **Create Tables Script** - The SQL script for creating the database tables is available in the repository: 
- **Insert Data Script** - The SQL script for insert data to the database tables is available in the repository:
- **Drop Tables Script** - The SQL script for droping all tables is available in the repository:
- **Select All Data Script** - The SQL script for selectAll tables is available in the repository:

**Data**

**First tool: using [mockaro](https://www.mockaroo.com/)o to create csv file**

**Entering a data to guest table:**

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.003.png)


![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.004.png)







**Second tool: using [generatedata](https://generatedata.com/generator). to create csv file**

**Entering a data to incidentType table:**

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.005.png) ![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.006.png)

**Third tool: using python to create csv file**

**Part of Python code:**

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.007.png)





**Sql file made from the python script:**

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.008.png)

**Backup**

- **backups files are kept with the date of the backup:**

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.009.png)


**Queries**

**Select:**

1) רשימת האורחים שהיו להם תקריות פתוחות, ופרטי התקרית ביחד עם פרטי האורח

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.010.png)

![תמונה שמכילה טקסט, גופן, מספר, קו

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.011.png)







1) מספר ההזמנות לפי סוג חדר

![תמונה שמכילה טקסט, גופן, צילום מסך, קו

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.012.png)



![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.013.png)








1) כל המשובים מתחת לדירוג 3 שנכתבו בחודשים שונים

   ![תמונה שמכילה טקסט, גופן, צילום מסך

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.014.png)![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.015.png)





1) מספר הלילות שכל אורח שהה במלון

   ![תמונה שמכילה טקסט, צילום מסך, גופן, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.016.png)![תמונה שמכילה טקסט, גופן, צילום מסך, קו

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.017.png)




1) רשימת אורחים עם מנוי ברמה גבוהה מ7

   ![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.018.png)

![תמונה שמכילה טקסט, צילום מסך, גופן, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.019.png)







1) אורחים שהשאירו פידבק על יותר מהזמנה אחת

![תמונה שמכילה טקסט, צילום מסך, גופן, קו

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.020.png)![תמונה שמכילה טקסט, גופן, צילום מסך, קו

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.021.png)




1) ![תמונה שמכילה טקסט, גופן, צילום מסך

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.022.png)תאריכי הדיווחים לפי סוג התקרית









![תמונה שמכילה טקסט, צילום מסך, גופן, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.023.png)





1) דירוג ממוצע של פידבק לפי רמת המנוי

![תמונה שמכילה טקסט, צילום מסך, גופן

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.024.png)







![תמונה שמכילה טקסט, צילום מסך, גופן, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.025.png)





**Delete:**

- מחיקת כל הפידבקים מתחת לדירוג 2

![תמונה שמכילה טקסט, גופן, עיצוב

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.026.png)

מסד הנתונים לפני השינוי:

![תמונה שמכילה טקסט, צילום מסך, גופן, קו

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.027.png)


מסד הנתונים לאחר השינוי:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.028.png)


- מחיקת מנויים שאין להם נקודות כלל

  ![תמונה שמכילה טקסט, גופן, גרפיקה

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.029.png)



מסד הנתונים לפני השינוי:

![תמונה שמכילה טקסט, צילום מסך, גופן, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.030.png)

מסד הנתונים לאחר השינוי:

![תמונה שמכילה טקסט, צילום מסך, גופן, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.031.png)

- מחיקת תקריות שנסגרו לפני יותר משנה

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.032.png)מסד הנתונים לפני השינוי:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.033.png)


מסד הנתונים לאחר השינוי:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.034.png)



**Update:**

- עדכון סטטוס התקריות שגילן מעל חודש לסגורות

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.035.png)

מסד הנתונים לפני השינוי:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.036.png)

מסד הנתונים לאחר השינוי:

![תמונה שמכילה טקסט, צילום מסך, גופן, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.037.png)

- ` `עדכון דירוג של פידבקים בלי תיאור לדירוג 3

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.038.png)

מסד הנתונים לפני השינוי:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.039.png)


מסד הנתונים לאחר השינוי:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.040.png)

- ![תמונה שמכילה טקסט, גופן, צילום מסך

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.041.png)העלאת רמת המנוי לכל מי שיש לו מעל 80 נקודות




מסד הנתונים לפני השינוי:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.042.png)



מסד הנתונים לאחר השינוי:

![תמונה שמכילה טקסט, צילום מסך, גופן, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.043.png)




**Constraints:**

- חובה להכניס מספר טלפון לאורח

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.044.png)

ניסיון הכנסת נתון שסותר את האילוץ:

![תמונה שמכילה טקסט, צילום מסך, גופן, תוכנה

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.045.png)

- ברירת מחדל לסטטוס תקרית יהיה 'פתוח'

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.046.png)

ניסיון להכנסת נתונים:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.047.png)

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.048.png)![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.049.png)



- ` `אילוץ שתאריך הכניסה יהיה לפני תאריך היציאה

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.050.png)



ניסיון להכנסת נתונים וסתירת האילוץ:

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.051.png)

**Rollback and Commit:**

![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.052.png)





הנתונים לפני הטרנזקציה:

![ref1]![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.054.png)

השינוי:

![ref1]![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.055.png)

לאחר ROLLBACK: 

![ref1]![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.056.png)

![תמונה שמכילה טקסט, צילום מסך, תוכנה, מספר

תוכן שנוצר על-ידי בינה מלאכותית עשוי להיות שגוי.](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.057.png)











המצב לפני השינוי:

![ref1]![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.058.png)

המצב אחרי השינוי:

![ref1]![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.059.png)


המצב לאחר commit:

![ref1]![](images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.060.png)

[ref1]: images/Aspose.Words.a5b42203-2a7d-45ed-bad4-b466be016fba.053.png
