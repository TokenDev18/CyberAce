DROP PROCEDURE IF EXISTS delete_data;

DELIMITER //

CREATE PROCEDURE delete_data(IN tName VARCHAR(25), IN row_id INT)
BEGIN

    DECLARE idColumn VARCHAR(25) DEFAULT '';
    
    SET idColumn = getIdColumn(tName);
    
    SET @query = CONCAT('DELETE FROM ', tName, ' WHERE ', idColumn , ' = ', row_id);
    SELECT @query as Variable; 
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

END //
DELIMITER ;

