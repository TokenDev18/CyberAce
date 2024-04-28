DROP TRIGGER IF EXISTS check_duplicates;

DELIMITER //

CREATE TRIGGER check_duplicates
    BEFORE INSERT ON employees

    FOR EACH ROW 
    BEGIN
    DECLARE duplicateCount INT;

    SELECT COUNT(*) INTO duplicateCount FROM employees WHERE first_name = NEW.first_name AND last_name = NEW.last_name AND job_title = NEW.job_title; 

    IF duplicateCount > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate entry found.';
    
    END IF;

END //
DELIMITER ;