-- change membershiplevel from int to text
ALTER TABLE subscription
ALTER COLUMN membershiplevel TYPE VARCHAR(10);

-- Alter roomType from numeric to descriptive text
ALTER TABLE room
ALTER COLUMN "roomType" TYPE TEXT USING 
  CASE "roomType"
    WHEN 0 THEN 'Single'
    WHEN 1 THEN 'Double'
    WHEN 2 THEN 'Suite'
    WHEN 3 THEN 'Deluxe'
    WHEN 4 THEN 'Family'
    WHEN 5 THEN 'King'
    WHEN 6 THEN 'Queen'
    WHEN 7 THEN 'Twin'
    WHEN 8 THEN 'Penthouse'
    WHEN 9 THEN 'Accessible'
    ELSE 'Unknown'
  END;

-- enforce valid room types
ALTER TABLE room
ADD CONSTRAINT valid_roomtype
CHECK ("roomType" IN (
  'Single', 'Double', 'Suite', 'Deluxe',
  'Family', 'King', 'Queen', 'Twin',
  'Penthouse', 'Accessible'
));

-- delete "incidentType column from incidentreport table"
ALTER TABLE incidentreport
DROP COLUMN "incidentType";

-- Add 'description' column to 'incidentreport' table
ALTER TABLE incidentreport
ADD COLUMN description VARCHAR(500);