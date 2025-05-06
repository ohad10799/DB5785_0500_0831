import random
import datetime

# פונקציה ליצירת תאריכים רנדומליים
def random_date(start_year=2020, end_year=2025):
    start_date = datetime.date(start_year, 1, 1)
    end_date = datetime.date(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)

# יצירת רשומות עבור IncidentReport
incident_reports = []
for i in range(1, 401):
    incident_date = random_date()
    incident_type = random.randint(1, 5)
    status = random.choice([True, False])
    incident_reports.append(f"INSERT INTO IncidentReport VALUES ({i}, '{incident_date}', {incident_type}, {status});")

# יצירת רשומות עבור Guest
guests = []
for i in range(1, 401):
    name = f"Guest_{i}"
    phone = random.randint(1000000000, 9999999999)
    preferences = random.randint(1, 3)
    incident_id = random.choice(range(1, 401)) if random.random() < 0.5 else 'NULL'
    guests.append(f"INSERT INTO Guest VALUES ({i}, '{name}', {phone}, {preferences}, {incident_id});")

# יצירת רשומות עבור Reservation
reservations = []
for i in range(1, 401):
    room_type = random.randint(1, 5)
    preferences = random.randint(1, 3)
    guest_id = random.randint(1, 400)
    reservations.append(f"INSERT INTO Reservation VALUES ({i}, {room_type}, {preferences}, {guest_id});")

# יצירת רשומות עבור check_in_out
check_ins = []
for i in range(1, 401):
    check_in = random_date()
    check_out = check_in + datetime.timedelta(days=random.randint(1, 14))
    check_ins.append(f"INSERT INTO check_in_out VALUES ({i}, '{check_in}', '{check_out}');")

# יצירת רשומות עבור Feedback
feedbacks = []
for i in range(1, 401):
    rating = random.randint(1, 5)
    feedback_date = random_date()
    description = f"Feedback for reservation {i}"
    guest_id = random.randint(1, 400)
    feedbacks.append(f"INSERT INTO Feedback VALUES ({rating}, '{feedback_date}', '{description}', {i}, {guest_id});")

# יצירת רשומות עבור subscription
subscriptions = []
for i in range(1, 401):
    membership_level = random.randint(1, 3)
    points_balance = random.randint(0, 5000)
    subscriptions.append(f"INSERT INTO subscription VALUES ({i}, {membership_level}, {points_balance});")

# שמירת הפקודות לקובץ
with open("insert_statements.sql", "w", encoding="utf-8") as file:
    file.write("\n".join(incident_reports) + "\n")
    file.write("\n".join(guests) + "\n")
    file.write("\n".join(reservations) + "\n")
    file.write("\n".join(check_ins) + "\n")
    file.write("\n".join(feedbacks) + "\n")
    file.write("\n".join(subscriptions) + "\n")

print("insert_statements.sql created!")
