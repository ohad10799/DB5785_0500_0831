CREATE TABLE IncidentReport
(
  IncidentID_ INT NOT NULL,
  report_date DATE NOT NULL,
  IncidentType_ INT NOT NULL,
  Status_ BOOLEAN NOT NULL,
  PRIMARY KEY (IncidentID_)
);

CREATE TABLE Guest
(
  gID INT NOT NULL,
  name VARCHAR(50) NOT NULL,
  phone_number NUMERIC NOT NULL,
  preferences INT NOT NULL,
  IncidentID_ INT,
  PRIMARY KEY (gID),
  FOREIGN KEY (IncidentID_) REFERENCES IncidentReport(IncidentID_)
);

CREATE TABLE Reservation
(
  resID INT NOT NULL,
  room_type INT NOT NULL,
  preferences INT NOT NULL,
  gID INT NOT NULL,
  PRIMARY KEY (resID),
  FOREIGN KEY (gID) REFERENCES Guest(gID)
);

CREATE TABLE check_in_out
(
  resID INT NOT NULL,
  check_in_date DATE NOT NULL,
  check_out_date DATE NOT NULL,
  PRIMARY KEY (resID),
  FOREIGN KEY (resID) REFERENCES Reservation(resID)
);

CREATE TABLE Feedback
(
  rating INT NOT NULL,
  date DATE NOT NULL,
  descreption VARCHAR(500) NOT NULL,
  resID INT NOT NULL,
  gID INT NOT NULL,
  PRIMARY KEY (resID),
  FOREIGN KEY (resID) REFERENCES Reservation(resID),
  FOREIGN KEY (gID) REFERENCES Guest(gID)
);

CREATE TABLE subscription
(
  gID INT NOT NULL,
  MembershipLevel INT NOT NULL,
  PointsBalance INT NOT NULL,
  PRIMARY KEY (gID),
  FOREIGN KEY (gID) REFERENCES Guest(gID)
);