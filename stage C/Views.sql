-- Create view 1
SELECT *
CREATE VIEW room_usage_summary_view AS
SELECT
    rm."roomNumber",
    rm."roomType",
    rm."floor",
    COUNT(r."resID") AS total_reservations
FROM room rm
LEFT JOIN reservation r ON r."roomNumber" = rm."roomNumber"
GROUP BY rm."roomNumber", rm."roomType", rm."floor";

-- Selects all rooms from the summary view that have no reservations
SELECT *
FROM room_usage_summary_view
WHERE total_reservations = 0;

-- Summarizes total reservations per floor, ordered by floor number
SELECT "floor", SUM(total_reservations) AS total
FROM room_usage_summary_view
GROUP BY "floor"
ORDER BY "floor";

-- create view 2
SELECT *
CREATE VIEW preferences_stats_view AS
SELECT
    p.description AS preference_description,
    COUNT(*) AS preference_count
FROM reservation r
JOIN preference p ON r.preferences = p.id
GROUP BY p.description
ORDER BY preference_count DESC;

-- Retrieves the most 5 popular preferences with the highest reservation count
SELECT preference_description, preference_count
FROM preferences_stats_view
ORDER BY preference_count DESC
LIMIT 1;

-- Retrieves all preferences that have more than 5 reservations, ordered by popularity
SELECT preference_description, preference_count
FROM preferences_stats_view
WHERE preference_count > 30
ORDER BY preference_count DESC;