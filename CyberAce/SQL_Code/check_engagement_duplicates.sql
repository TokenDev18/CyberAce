DROP TRIGGER IF EXISTS check_engagement_duplicates;

DELIMITER //

CREATE TRIGGER check_engagement_duplicates
    BEFORE INSERT ON engagements

    FOR EACH ROW 
    BEGIN
    DECLARE duplicateCount INT;

    SELECT COUNT(*) INTO duplicateCount FROM engagements WHERE eng_customer = NEW.eng_customer AND service_id = NEW.service_id AND begin_date = NEW.begin_date; 

    IF duplicateCount > 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Duplicate entry found.';
    
    END IF;
    
END //
DELIMITER ;