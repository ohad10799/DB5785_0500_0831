-- Procedure: resolve_old_incidents
-- Purpose: Finds all incident reports marked as unresolved (status = TRUE)
--          and, if older than 30 days, appends an expiration note to the description.
-- Notes:
--   - status = TRUE → unresolved
--   - status = FALSE → resolved
--   - Uses an explicit cursor and loops over the results
--   - Includes basic error handling (EXCEPTION block)

CREATE OR REPLACE PROCEDURE resolve_old_incidents()
LANGUAGE plpgsql
AS
$$
DECLARE
    rec RECORD;
    cur CURSOR FOR
        SELECT "incidentId" AS incidentid, report_date, description
        FROM incidentreport
        WHERE status = TRUE;
BEGIN
    OPEN cur;

    LOOP
        FETCH cur INTO rec;
        EXIT WHEN NOT FOUND;

        -- If the incident was reported over 30 days ago
        IF rec.report_date < CURRENT_DATE - INTERVAL '30 days' THEN
            UPDATE incidentreport
            SET description = rec.description || ' [Auto-expired: not resolved within 30 days]'
            WHERE "incidentId" = rec.incidentid;
        END IF;

    END LOOP;

    CLOSE cur;

    RAISE NOTICE 'Old unresolved incidents marked with expiry note.';

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'An error occurred: %', SQLERRM;
END;
$$;
