DROP PROCEDURE IF EXISTS update_table_data;
DELIMITER //

CREATE PROCEDURE update_table_data(IN tName VARCHAR(25), IN columne_name VARCHAR(25), IN new_value VARCHAR(255), IN row_id INT)
BEGIN

    DECLARE idColumn VARCHAR(25) DEFAULT '';
    SET @value = new_value;
    
    SET idColumn = getIdColumn(tName);
    
    SET @query = CONCAT('UPDATE ', tName, ' SET ', columne_name, ' = ', '@value', ' WHERE ', idColumn, ' = ', row_id);
    SELECT @query as Variable; 
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

END //
DELIMITER ;