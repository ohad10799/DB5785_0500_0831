BEGIN;

-- 1. רשימת האורחים שהיו להם תקריות פתוחות (status = 'open') עם פרטי התקרית
SELECT g.name, g.phone_number, ir.incidenttype_, ir.report_date, ir.description
FROM Guest g
JOIN IncidentReport ir ON g.incidentid_ = ir.incidentid_
WHERE ir.status_ = TRUE;

-- 2. מספר ההזמנות לכל סוג חדר
SELECT room_type, COUNT(*) AS total_reservations
FROM Reservation
GROUP BY room_type
ORDER BY total_reservations DESC;

-- 3. משובים עם דירוג מתחת ל-3 בחודשים שונים
SELECT g.name, f.rating, f.descreption, EXTRACT(MONTH FROM f.date) AS month
FROM Feedback f
JOIN Guest g ON f.gID = g.gID
WHERE f.rating < 3
ORDER BY f.date DESC;

--4 מספר הלילות שכל אורח שהה במלון
SELECT g.name, SUM(ci.check_out_date - ci.check_in_date) AS total_nights
FROM Guest g
JOIN Reservation r ON g.gID = r.gID
JOIN check_in_out ci ON r.resID = ci.resID
GROUP BY g.name;

-- 5. רשימת אורחים עם מנוי ברמה גבוהה מ-7
SELECT g.name, s.MembershipLevel, s.PointsBalance
FROM subscription s
JOIN Guest g ON s.gID = g.gID
WHERE s.MembershipLevel > 7;

--6 אורחים שהשאירו פידבק על יותר מהזמנה אחת
SELECT g.name, COUNT(DISTINCT f.resID) AS feedback_count
FROM Feedback f
JOIN Guest g ON f.gID = g.gID
GROUP BY g.gID, g.name
HAVING COUNT(DISTINCT f.resID) > 1;

--7 תאריכי הדיווחים לפי סוג התקרית
SELECT 
    incidenttype_, 
    EXTRACT(YEAR FROM report_date) AS year, 
    EXTRACT(MONTH FROM report_date) AS month, 
    COUNT(*) AS total
FROM IncidentReport
GROUP BY 
    incidenttype_, 
    EXTRACT(YEAR FROM report_date), 
    EXTRACT(MONTH FROM report_date)
ORDER BY year DESC, month DESC;

--8 דירוג ממוצע של פידבק לפי רמת מנוי
SELECT 
    s.MembershipLevel,
    COUNT(f.rating) AS total_feedbacks,
    ROUND(AVG(f.rating), 2) AS avg_rating,
    COUNT(DISTINCT g.gID) AS unique_guests
FROM Feedback f
JOIN Guest g ON f.gID = g.gID
JOIN subscription s ON g.gID = s.gID
GROUP BY s.MembershipLevel
ORDER BY avg_rating DESC;


-- 1. מחיקת כל הפידבקים מתחת לדירוג 2
DELETE FROM Feedback
WHERE rating < 2;
 
-- 2. מחיקת מנויים שאין להם נקודות כלל
DELETE FROM subscription
WHERE PointsBalance = 0;


--3. מחיקת תקריות שנסגרו לפני יותר משנה 
-- שינוי אילוץ foreign key כדי שיאפשר מחיקה של התקרית
ALTER TABLE Guest
DROP CONSTRAINT guest_incidentid__fkey;

ALTER TABLE Guest
ADD CONSTRAINT guest_incidentid__fkey
FOREIGN KEY (incidentID_)
REFERENCES IncidentReport(incidentID_)
ON DELETE SET NULL;

DELETE FROM IncidentReport
WHERE status_ = FALSE AND report_date < CURRENT_DATE - INTERVAL '1 year';

-- 1. עדכון סטטוס התקריות שגילן מעל חודש ל-FALSE
UPDATE IncidentReport
SET status_ = FALSE
WHERE status_ = TRUE
  AND report_date < CURRENT_DATE - INTERVAL '30 days';

-- 2. עדכון דירוג של פידבקים בלי תיאור לדירוג 3
UPDATE Feedback
SET rating = 3
WHERE description IS NULL OR description = '' OR description = ' ';


-- 3. העלאת רמת המנוי לכל מי שיש לו יותר מ-80 נקודות
UPDATE subscription
SET MembershipLevel = MembershipLevel + 1
WHERE PointsBalance > 80;
