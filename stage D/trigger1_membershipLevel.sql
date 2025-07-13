-- Trigger: trg_update_membership_level
-- Purpose: Fires BEFORE UPDATE of pointsBalance on subscription table
-- Calls: update_membership_level()
-- Condition: Only fires if pointsBalance value changes
CREATE TRIGGER trg_update_membership_level
BEFORE UPDATE OF pointsBalance ON subscription
FOR EACH ROW
WHEN (NEW.pointsBalance IS DISTINCT FROM OLD.pointsBalance)
EXECUTE FUNCTION update_membership_level();
