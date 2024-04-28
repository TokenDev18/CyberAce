DROP PROCEDURE IF EXISTS create_payroll_entry;
DELIMITER //

CREATE PROCEDURE create_payroll_entry(IN tableName VARCHAR(50), IN pay_employee INT)
BEGIN

    SET @query = CONCAT('INSERT INTO ', tableName , ' (payroll_id, pay_employee, salary) ', 'VALUES (DEFAULT, ' ,pay_employee, ', 0.00)');
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

END //
DELIMITER ;
