
CREATE TABLE complaint (
    id int NOT NULL,
    email varchar(255) NOT NULL,
    firstname varchar(255) NOT NULL,
    lastname varchar(255) NOT NULL,
    role varchar(255) NOT NULL,
    ssn varchar(255) NOT NULL,
    complainttext varchar(3000),
    PRIMARY KEY (id),
    FOREIGN KEY (ssn) REFERENCES doctor(ssn),
    FOREIGN KEY (ssn) REFERENCES nurse(ssn),
    FOREIGN KEY (ssn) REFERENCES patient(ssn)
);




CREATE TABLE Doctors (
    Fname VARCHAR(255),
    Lname VARCHAR(255),
    address VARCHAR(255),
    DSSN INT,
    gender VARCHAR(255),
    age INT,
    phone INT,
    Salary INT,
    RNum INT
 );

CREATE TABLE Equipment (
    code VARCHAR(255),
    manufacturer VARCHAR(255),
    Ename VARCHAR(255),
    Emodel INT,
    PSSN INT
);
CREATE TABLE Dependent (
    Dname VARCHAR(255),
    relationship VARCHAR(255),
    gender VARCHAR(255),
    age INT,
    phone INT,
    PSSN INT
);

