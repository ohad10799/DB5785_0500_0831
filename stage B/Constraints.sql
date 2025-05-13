-- אילוץ 1: חובה להזין מספר טלפון לאורח
ALTER TABLE Guest
ALTER COLUMN phone_number SET NOT NULL;

-- אילוץ 2: ברירת מחדל לסטטוס תקרית - 'open'
ALTER TABLE IncidentReport
ALTER COLUMN Status_ SET DEFAULT TRUE;

-- אילוץ 3: תאריך הכניסה חייב להיות לפני תאריך היציאה
ALTER TABLE check_in_out
ADD CONSTRAINT check_in_before_check_out
CHECK (check_in_date <= check_out_date);