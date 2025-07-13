-- Trigger: trg_set_feedback_date_if_null
-- Fires BEFORE INSERT on feedback table
-- Calls set_feedback_date_if_null()

CREATE TRIGGER trg_set_feedback_date_if_null
BEFORE INSERT ON feedback
FOR EACH ROW
EXECUTE FUNCTION set_feedback_date_if_null();
