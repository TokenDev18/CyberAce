DROP DATABASE IF EXISTS ace_sec_consulting; 
CREATE DATABASE ace_sec_consulting; 
USE ace_sec_consulting;

CREATE TABLE services(
    service_id INT PRIMARY KEY AUTO_INCREMENT,
    serv_name VARCHAR(30) NOT NULL,
    service_sla VARCHAR(10) NOT NULL,
    date_added DATETIME DEFAULT NULL
); 

CREATE TABLE customers(
    customer_id INT PRIMARY KEY AUTO_INCREMENT, 
    customer_name VARCHAR(255) NOT NULL, 
    phone_number VARCHAR(20) NOT NULL, 
    company_address VARCHAR(255) NOT NULL, 
    industry VARCHAR(25) NOT NULL
);

CREATE TABLE engagements(
    engagement_id INT PRIMARY KEY AUTO_INCREMENT,
    eng_customer INT NOT NULL, 
    service_id INT NOT NULL, 
    begin_date DATETIME DEFAULT NULL,
    end_date DATETIME DEFAULT NULL, 
    CONSTRAINT engagements_fk_customers
        FOREIGN KEY (eng_customer)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE
); 

CREATE TABLE vulnerabilities(
    vuln_id INT PRIMARY KEY AUTO_INCREMENT,
    vuln_description TEXT NOT NULL, 
    date_found DATETIME NOT NULL, 
    severity VARCHAR(10) NOT NULL
);

CREATE TABLE requests(
    request_id INT PRIMARY KEY AUTO_INCREMENT, 
    req_customer INT NOT NULL,
    customer_req TEXT NOT NULL,
    date_requested DATETIME NOT NULL,
    CONSTRAINT requests_fk_customers
        FOREIGN KEY (req_customer)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE
); 

CREATE TABLE employees(
    employee_id INT PRIMARY KEY AUTO_INCREMENT, 
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL,
    job_title VARCHAR(50) NOT NULL, 
    specialization VARCHAR(50) NOT NULL,
    date_hired DATETIME NOT NULL, 
    date_terminated DATETIME NULL
); 

CREATE TABLE payroll(
    payroll_id INT PRIMARY KEY AUTO_INCREMENT,
    pay_employee INT NOT NULL, 
    salary DECIMAL(10,2) NOT NULL,
    CONSTRAINT payroll_fk_employees
        FOREIGN KEY (pay_employee)
        REFERENCES employees(employee_id)
        ON DELETE CASCADE
);

INSERT INTO services (service_id, serv_name, service_sla, date_added) VALUES
(1, 'Web Application Testing', '10 days', '2023-01-01 12:30:45'), 
(2, 'Network Pentesting', '15 days', '2023-01-01 12:30:45'), 
(3, 'Red Teaming', '15 days', '2023-01-01 12:30:45'), 
(4, 'Incident Response', '20 days', '2023-01-01 12:30:45'), 
(5, 'Malware Analysis', '10 days', '2023-01-01 12:30:45'), 
(6, 'Vulnerability Testing', '10 days', '2023-01-01 12:30:45');

INSERT INTO customers (customer_id, customer_name, phone_number, company_address, industry) VALUES 
(1, '123_HealthCare', '678-123-4567', '123 HealthCare Drive, Boston, MA 02108', 'Healthcare'),
(2, 'Tech 4U', '123-789-8792', '789 Tech4U Rd, Princeton, NJ 23467', 'Technology'),
(3, 'WeFix Cars', '732-987-3454', '923 Automotive Lane, Elizabth, NJ 07208', 'Automotive');

INSERT INTO engagements (engagement_id, eng_customer, service_id, begin_date, end_date) VALUES 
(1, 2, 1, '2023-11-01 8:00:45', '2023-11-11 12:30:45'),
(2, 2, 2, '2023-08-01 10:00:45', '2023-08-16 13:00:40'),
(3, 1, 2, '2024-01-06 14:00:45', '2024-01-21 15:30:45'),
(4, 1, 3, '2023-11-10 11:00:45', '2023-11-25 11:30:45'),
(5, 3, 1, '2023-10-15 8:00:45', '2023-10-25 9:45:50');

INSERT INTO vulnerabilities (vuln_id, vuln_description, date_found, severity) VALUES
(1, 'Remote Code Execution (RCE) allow an attacker to execute arbitrary code on a remote system.', '2023-11-09 12:30:45', 'critical'), 
(2, 'Server Side Request Forgery is a web security vulnerability that allows an attacker to cause the server-side application to make requests to an unintended location', '2023-08-14 13:00:40', 'critical'), 
(3, 'Cross Site Scripting is a web security vulnerability that allows an attacker to compromise the interactions that users have with a vulnerable application','2023-08-16 13:00:40', 'high');

INSERT INTO requests (request_id, req_customer, customer_req, date_requested) VALUES
(1, 2, 'The customer would like for ACE Secuirty consulting to perform network pentest and web application testing to determine their overall security posture.', '2023-03-01 12:30:45'), 
(2, 1, 'Customer would like for ACE Security Consulting to perform red team testing and network pentesting to identify and remediate any holes in their systems.', '2023-04-01 12:30:45'), 
(3, 3, 'Customer would like for ACE Security Consulting to perform web application testing on their web application to ensure its secure from common web threats', '2023-06-01 12:30:45'); 

INSERT INTO employees (employee_id, first_name, last_name, job_title, specialization, date_hired, date_terminated) VALUES
(201, 'Jonah', 'Williams', 'CTO', 'Strategy and Technology', '2022-11-01 8:30:45', NULL),
(202, 'PWNed', 'Jones', 'Master Hacker', 'Hacking and breaking into stuff', '2022-11-01 8:30:45', NULL), 
(203, 'Tizzle', 'Thomas', 'CEO', 'Former Master Hacker and make the company go', '2022-11-01 8:30:45', NULL),
(204, 'Shantel', 'Smith', 'Master Hacker', 'Hack anything that moves and coding genius', '2022-11-01 8:30:45', NULL);

INSERT INTO payroll (payroll_id, pay_employee, salary) VALUES 
(1, 201, '350000.00'), 
(2, 202, '250000.00'), 
(3, 203, '550000.00'), 
(4, 204, '250000.00'); 

-- Creating DB user
CREATE USER IF NOT EXISTS db_user@localhost IDENTIFIED BY 'DBpAss12_43';

-- Grant Privileges
GRANT SELECT, INSERT, UPDATE, DELETE, DROP, TRIGGER, CREATE VIEW, CREATE ROUTINE, EXECUTE ON ace_sec_consulting.* TO db_user@localhost;