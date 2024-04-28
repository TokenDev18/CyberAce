DELIMITER //

CREATE PROCEDURE get_table_data(IN tableName VARCHAR(25))
BEGIN

    SET @query = CONCAT('SELECT * FROM `', tableName, '`');
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

END //
DELIMITER ;

CALL get_table_data('payroll');
SELECT @query as query;