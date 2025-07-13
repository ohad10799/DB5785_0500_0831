-- Main Program 1
-- Purpose: 
--   1. Resolve old unresolved incidents (older than 30 days).
--   2. Display all feedbacks for a guest with a given ID.

DO
$$
DECLARE
    feedback_cursor REFCURSOR;
    feedback_record RECORD;
    guest_id INT := 213517251;  -- You can change this to any guest ID
BEGIN
    -- Step 1: Call the procedure to resolve old incident reports
    CALL resolve_old_incidents();

    -- Step 2: Get feedbacks for a specific guest
    feedback_cursor := get_guest_feedbacks(guest_id);

    -- Fetch and display the results
    LOOP
        FETCH feedback_cursor INTO feedback_record;
        EXIT WHEN NOT FOUND;
        RAISE NOTICE 'Feedback: % stars on %, "%"', 
            feedback_record.rating, 
            feedback_record.date, 
            feedback_record.description;
    END LOOP;

    CLOSE feedback_cursor;
END;
$$;
