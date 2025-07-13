-- Trigger Function: set_feedback_date_if_null
-- Purpose: Set feedback date to current date if not provided
-- Triggered: BEFORE INSERT on feedback table

CREATE OR REPLACE FUNCTION set_feedback_date_if_null()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
BEGIN
    IF NEW.date IS NULL THEN
        NEW.date := CURRENT_DATE;
    END IF;

    RETURN NEW;
END;
$$;
