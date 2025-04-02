-- מחיקת טבלאות שתלויות באחרות
DROP TABLE IF EXISTS subscription CASCADE;
DROP TABLE IF EXISTS Feedback CASCADE;
DROP TABLE IF EXISTS check_in_out CASCADE;
DROP TABLE IF EXISTS IncidentReport CASCADE;

-- מחיקת טבלת הזמנות
DROP TABLE IF EXISTS Reservation CASCADE;

-- מחיקת טבלת האורחים
DROP TABLE IF EXISTS Guest CASCADE;
