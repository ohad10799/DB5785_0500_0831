-- Procedure: reward_high_rating_guests
-- Purpose: For every feedback with rating >= 7, grant the guest 10 bonus points.
-- Notes:
--   - Uses an explicit cursor to iterate through feedbacks
--   - Updates the pointsBalance in the subscription table
--   - Includes error handling

CREATE OR REPLACE PROCEDURE reward_high_rating_guests()
LANGUAGE plpgsql
AS
$$
DECLARE
    rec RECORD;
    cur CURSOR FOR
        SELECT DISTINCT f.gid
        FROM feedback f
        WHERE f.rating >= 7;
BEGIN
    OPEN cur;

    LOOP
        FETCH cur INTO rec;
        EXIT WHEN NOT FOUND;

        -- Bonus logic: Add 10 points for guests with a 7+ feedback
        UPDATE subscription
        SET pointsBalance = pointsBalance + 10
        WHERE gid = rec.gid;

    END LOOP;

    CLOSE cur;

    RAISE NOTICE 'Bonus points granted to guests with 7-star or more feedback.';

EXCEPTION
    WHEN OTHERS THEN
        RAISE NOTICE 'An error occurred: %', SQLERRM;
END;
$$;
