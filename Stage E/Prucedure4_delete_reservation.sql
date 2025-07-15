CREATE OR REPLACE PROCEDURE delete_reservation(p_resid INT)
LANGUAGE plpgsql
AS $$
BEGIN
    -- delete from check_in_out table
    DELETE FROM check_in_out
    WHERE resid = p_resid;

    -- delete from reservation table
    DELETE FROM reservation
    WHERE resid = p_resid;

    RAISE NOTICE 'Reservation % deleted successfully.', p_resid;
END;
$$;
