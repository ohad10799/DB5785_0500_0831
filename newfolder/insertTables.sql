-- הכנסת נתונים לטבלת Guest
INSERT INTO Guest (gID, name, phone_number, preferences) VALUES
(1, 'David', 123456789, 2),
(2, 'Sarah', 987654321, 1),
(3, 'John', 555666777, 3);

-- הכנסת נתונים לטבלת Reservation
INSERT INTO Reservation (resID, room_type, preferences, gID) VALUES
(101, 1, 2, 1),
(102, 2, 1, 2),
(103, 3, 3, 3);

-- הכנסת נתונים לטבלת IncidentReport
INSERT INTO IncidentReport (IncidentID_, report_date, IncidentType_, Status_) VALUES
(201, '2024-03-01', 1, 0),
(202, '2024-03-02', 2, 1),
(203, '2024-03-03', 1, 0);

-- הכנסת נתונים לטבלת check_in_out
INSERT INTO check_in_out (resID, check_in_date, check_out_date) VALUES
(101, '2024-03-05', '2024-03-10'),
(102, '2024-03-06', '2024-03-12'),
(103, '2024-03-07', '2024-03-14');

-- הכנסת נתונים לטבלת Feedback
INSERT INTO Feedback (resID, gID, rating, date, descreption) VALUES
(101, 1, 5, '2024-03-11', 'Great stay!'),
(102, 2, 4, '2024-03-13', 'Very nice.'),
(103, 3, 3, '2024-03-15', 'Average experience.');

-- הכנסת נתונים לטבלת subscription
INSERT INTO subscription (gID, MembershipLevel, PointsBalance) VALUES
(1, 3, 500),
(2, 2, 300),
(3, 1, 100);
