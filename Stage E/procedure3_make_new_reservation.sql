CREATE OR REPLACE PROCEDURE add_reservation_with_guest(
    p_gid INT,
    p_roomNumber INT,
    p_preferences INT,
    p_check_in DATE,
    p_check_out DATE
)
LANGUAGE plpgsql
AS $$
DECLARE
    new_res_id INT;
BEGIN
    -- Step 1: Insert reservation (get new resID)
    INSERT INTO reservation ("roomNumber", preferences)
    VALUES (p_roomNumber, p_preferences)
    RETURNING resID INTO new_res_id;

    -- Step 2: Insert into check_in_out
    INSERT INTO check_in_out (resID, gid, check_in_date, check_out_date)
    VALUES (new_res_id, p_gid, p_check_in, p_check_out);

    RAISE NOTICE 'Reservation % added for guest %', new_res_id, p_gid;
END;
$$;
