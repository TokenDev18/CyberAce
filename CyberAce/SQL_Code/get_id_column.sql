DELIMITER $$

CREATE FUNCTION getIdColumn(tName VARCHAR(25)) RETURNS VARCHAR(25)
DETERMINISTIC
BEGIN

    DECLARE id_column VARCHAR(25) DEFAULT '';

    IF (STRCMP(tName, "customers") = 0) THEN 
        SET id_column = 'customer_id';
    ELSEIF (STRCMP(tName, "employees") = 0) THEN 
        SET id_column = "employee_id"; 
    ELSEIF (STRCMP(tName, "engagements") = 0) THEN
        SET id_column = "engagment_id"; 
    ELSEIF (STRCMP(tName, "payroll") = 0) THEN
        SET id_column = "pay_employee";
    ELSEIF (STRCMP(tName, "requests") = 0) THEN
        SET id_column = "request_id";
    ELSEIF (STRCMP(tName, "services") = 0) THEN
        SET id_column = "service_id";
    ELSE
        SET id_column = "vuln_id"; 
    END IF;

    RETURN (id_column);

END$$

DELIMITER ; 