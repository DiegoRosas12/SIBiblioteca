# Definition of the schema of the DB
# This s a DB for managing information about a library

# Create the DB
CREATE DATABASE IF NOT EXISTS library_db;

# Select the database to work with
USE library_db;

# Create the kernel tables
CREATE TABLE IF NOT EXISTS zips(
	zip VARCHAR(6) NOT NULL,
    z_city VARCHAR(50) NOT NULL,
    z_state VARCHAR(40) NOT NULL,
    PRIMARY KEY(zip)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS books(
	isbn INT NOT NULL,
    b_title VARCHAR(50) NOT NULL,
    b_author VARCHAR(50) NOT NULL,
    b_editorial VARCHAR(50) NOT NULL,
    b_edition VARCHAR(15) NOT NULL,
    b_publidate DATE NOT NULL,
    b_category VARCHAR(25) NOT NULL,
    b_description VARCHAR(400),
    b_language VARCHAR(25) NOT NULL,
    b_pages INT,
    b_shelving VARCHAR(15) NOT NULL,
    b_quantity INT NOT NULL,
    PRIMARY KEY(isbn)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS users(
	id_user INT NOT NULL AUTO_INCREMENT,
    u_fname VARCHAR(50) NOT NULL,
    u_lname1 VARCHAR(50) NOT NULL,
    u_lname2 VARCHAR(50) NOT NULL,
    u_email VARCHAR(50) NOT NULL,
    u_phone VARCHAR(13) NOT NULL,
    u_street VARCHAR(40) NOT NULL,
    u_noext VARCHAR(8) NOT NULL,
    u_noint VARCHAR(8),
    u_col VARCHAR(50) NOT NULL,
    u_zip VARCHAR(6),
    PRIMARY KEY(id_user),
    CONSTRAINT fkzip_users FOREIGN KEY(u_zip)
		REFERENCES zips(zip)
        ON DELETE SET NULL
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS loans(
	id_loan INT NOT NULL AUTO_INCREMENT,
    id_user INT NOT NULL,
    loan_date DATE NOT NULL,
    expiration_date DATE NOT NULL,
    PRIMARY KEY(id_loan),
    CONSTRAINT fkuser_loans FOREIGN KEY(id_user)
		REFERENCES users(id_user)
        ON DELETE CASCADE
        ON UPDATE CASCADE 
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS loans_details(
	id_loan INT NOT NULL,
    isbn INT NOT NULL,
    lds_status ENUM('UNDELIVERED','DELIVERED','LATE') NOT NULL,
    delivery_date DATE,
    PRIMARY KEY(id_loan, isbn),
    CONSTRAINT fkloan_lds FOREIGN KEY(id_loan)
		REFERENCES loans(id_loan)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fkisbn_lds FOREIGN KEY(isbn)
		REFERENCES books(isbn)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

