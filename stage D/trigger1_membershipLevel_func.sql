-- Trigger Function: update_membership_level
-- Purpose: Automatically updates the membershipLevel field based on the pointsBalance value
-- Triggered: BEFORE UPDATE on subscription.pointsBalance
-- Logic:
--   - pointsBalance >= 60 → membershipLevel = 'Gold'
--   - pointsBalance >= 20 → membershipLevel = 'Silver'
--   - pointsBalance < 20  → membershipLevel = 'Bronze'
-- Returns:
--   - NEW record with updated membershipLevel
CREATE OR REPLACE FUNCTION update_membership_level()
RETURNS TRIGGER
LANGUAGE plpgsql
AS
$$
BEGIN
    IF NEW.pointsBalance >= 60 THEN
        NEW.membershipLevel := 'Gold';
    ELSIF NEW.pointsBalance >= 20 THEN
        NEW.membershipLevel := 'Silver';
    ELSE
        NEW.membershipLevel := 'Bronze';
    END IF;

    RETURN NEW;
END;
$$;
