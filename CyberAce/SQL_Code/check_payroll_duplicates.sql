DROP TRIGGER IF EXISTS check_payroll_duplicates;

DELIMITER //

CREATE TRIGGER check_payroll_duplicates
    BEFORE INSERT ON payroll

    FOR EACH ROW
    BEGIN
    DECLARE duplicateCount INT;

    SELECT COUNT(*) INTO duplicateCount FROM payroll WHERE pay_employee = NEW.pay_employee AND salary = NEW.salary;

    IF duplicateCount > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate entry found.';
    
    END IF;
    
END //
DELIMITER ;