DROP TRIGGER IF EXISTS check_service_duplicates;

DELIMITER //

CREATE TRIGGER check_service_duplicates
    BEFORE INSERT ON services

    FOR EACH ROW
    BEGIN
    DECLARE duplicateCount INT;

    SELECT COUNT(*) INTO duplicateCount FROM services WHERE serv_name = NEW.serv_name AND service_sla = NEW.service_sla;

    IF duplicateCount > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate entry found.';
    
    END IF;
    
END //
DELIMITER ;