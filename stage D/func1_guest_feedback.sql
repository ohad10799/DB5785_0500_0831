-- Function: get_guest_feedbacks
-- Purpose: Returns the name of a guest and a refcursor to all feedbacks
--          that the guest has written in the system.
-- Parameters:
--   - guest_id (INTEGER): The unique ID (gid) of the guest
-- Returns:
--   - REFCURSOR pointing to all feedbacks (with rating, date, description)
--     written by the given guest
CREATE OR REPLACE FUNCTION get_guest_feedbacks(p_gid INTEGER)
RETURNS refcursor AS
$$
DECLARE
    feedback_cursor REFCURSOR;  -- -- Declare a named refcursor
BEGIN
    -- Open the cursor on the result set of the guest's feedbacks
    OPEN feedback_cursor FOR
        SELECT rating, date, description
        FROM feedback
        WHERE gid = p_gid;

    -- Return the cursor to the caller
    RETURN feedback_cursor;
END;
$$ LANGUAGE plpgsql;
