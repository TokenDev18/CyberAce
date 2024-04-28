DROP TRIGGER IF EXISTS check_customer_duplicates;

DELIMITER //

CREATE TRIGGER check_customer_duplicates
    BEFORE INSERT ON customers

    FOR EACH ROW 
    BEGIN
    DECLARE duplicateCount INT;

    SELECT COUNT(*) INTO duplicateCount FROM customers WHERE customer_name = NEW.customer_name AND phone_number = NEW.phone_number AND company_address = NEW.company_address; 

    IF duplicateCount > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate entry found.';
    
    END IF;
    
END //
DELIMITER ;