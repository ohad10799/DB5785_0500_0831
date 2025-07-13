-- Main Program 2
--   1. Grant bonus points to guests with high feedback ratings.
--   2. Display available rooms of a specific type and date range.

DO
$$
DECLARE
    room_cursor REFCURSOR;
    room_record RECORD;
    room_type TEXT := 'Double';  -- Can be 'Suite', 'Single', etc.
    check_in DATE := CURRENT_DATE + 3;
    check_out DATE := CURRENT_DATE + 7;
BEGIN
    -- Step 1: Call procedure to reward high-rating guests
    CALL reward_high_rating_guests();

    -- Step 2: Get available rooms of the given type and range
    room_cursor := get_available_rooms_by_type(room_type, check_in, check_out);

    -- Step 3: Only try to fetch if the cursor is not NULL
    IF room_cursor IS NOT NULL THEN
        LOOP
            FETCH room_cursor INTO room_record;
            EXIT WHEN NOT FOUND;
            RAISE NOTICE 'Available Room: %', room_record."roomNumber";
        END LOOP;

        CLOSE room_cursor;
    ELSE
        RAISE NOTICE 'No room data returned due to an internal error.';
    END IF;

END;
$$;
