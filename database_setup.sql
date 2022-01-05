
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




CREATE TABLE Doctor (
    Fname VARCHAR(255),
    Lname VARCHAR(255),
    address VARCHAR(255),
    DSSN INT,
    gender VARCHAR(255),
    age INT,
    phone INT,
    Salary INT,
    RNum INT,

    username varchar(255) DEFAULT "username",
    password varchar(255) DEFAULT "password"
 );



create table patient(
	PAT_FNAME varchar(255),
    PAT_LNAME varchar(255),
    PAT_SSN int,
    PAT_AGE int,
    PAT_PHONE int,
    PAT_DISEASE varchar(255),
    PAT_MEDICINE varchar(255),
    PAT_ADDRESS varchar(255),
    PATIENT_GENDER varchar(255),
    NOROOM int,
    SSN_DOCTOR int,
    SSN_NURSE int,

    username varchar(255) DEFAULT "username",
    password varchar(255) DEFAULT "password"
);



create table nurse(
    NUR_SSN int,
    NUR_FNAME varchar(255),
    NUR_LNAME varchar(255),
    NUR_AGE int,
    NUR_PHONE int,
    NUR_ADDRESS varchar(255),
    NUR_GENDER varchar(255),
    NUR_SALARY int,
    NUR_CARE_R int,
    NURSE_SUPERVISOR varchar(255), // ??????????????????

    username varchar(255) DEFAULT "username",
    password varchar(255) DEFAULT "password"
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