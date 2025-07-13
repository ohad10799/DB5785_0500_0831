-- Function: get_available_rooms_by_type
-- Purpose: Returns a refcursor to the list of room numbers that are available
--          (not reserved) for a given room type and date range.
-- Parameters:
--   - desired_type (TEXT): the type of room to search for (e.g. 'Double', 'Suite')
--   - desired_check_in (DATE): desired start date of stay
--   - desired_check_out (DATE): desired end date of stay
-- Returns:
--   - REFCURSOR pointing to all available room numbers that match the criteria
CREATE OR REPLACE FUNCTION get_available_rooms_by_type(
    desired_type TEXT,
    desired_check_in DATE,
    desired_check_out DATE
)
RETURNS refcursor AS
$$
DECLARE
    available_rooms_cursor REFCURSOR;
BEGIN
 	-- Open a cursor that selects all room numbers of the given type
    -- that are not reserved in the desired date range
    OPEN available_rooms_cursor FOR
    SELECT r."roomNumber"
    FROM room r
    WHERE r."roomType" = desired_type
      AND r."roomNumber" NOT IN (
	  -- Exclude rooms with any reservation that overlaps the requested dates
          SELECT res."roomNumber"
          FROM reservation res
          JOIN check_in_out cio ON cio.resid = res.resid
          WHERE cio."check_in_date" < desired_check_out
            AND cio."check_out_date" > desired_check_in
      );
      
    RETURN available_rooms_cursor;
    
EXCEPTION
	-- Handle any error by showing a notice and returning NULL
    WHEN OTHERS THEN
        RAISE NOTICE 'Error occurred: %', SQLERRM;
        RETURN NULL;
END;
$$ LANGUAGE plpgsql;
