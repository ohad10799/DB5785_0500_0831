CREATE TABLE Room (
    RoomNumber INT PRIMARY KEY,
    RoomType VARCHAR(50),
    Floor INT
);

ALTER TABLE Reservation
ADD COLUMN RoomNumber INT;

ALTER TABLE Reservation
ADD CONSTRAINT fk_room
FOREIGN KEY (RoomNumber) REFERENCES Room(RoomNumber);

ALTER TABLE Reservation
DROP COLUMN Room_type;

WITH numbered_reservations AS (
    SELECT ctid, ROW_NUMBER() OVER (ORDER BY ctid) AS rn
    FROM reservation
),
numbered_rooms AS (
    SELECT "roomNumber", ROW_NUMBER() OVER (ORDER BY ctid) AS rn
    FROM room
)
UPDATE reservation
SET "roomNumber" = r2."roomNumber"
FROM numbered_reservations r
JOIN numbered_rooms r2 ON r.rn = r2.rn
WHERE reservation.ctid = r.ctid;

