/*/
ROLLBACK
*/

BEGIN;

UPDATE guest
SET preferences = preferences + 1
WHERE gid = 3720065;

SELECT * FROM guest WHERE gid = 3720065;

ROLLBACK;

SELECT * FROM guest WHERE gid = 3720065;

/*/
COMMIT
*/

SELECT * FROM guest WHERE gid = 3763742;

BEGIN;

UPDATE guest

SET name = 'Meir Revivo'

WHERE gid = 3763742;

SELECT * FROM guest WHERE gid = 3763742;

COMMIT;

SELECT * FROM guest WHERE gid = 3763742;