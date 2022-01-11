

-- drop table doctor,room,nurse,patient,equipment,dependent;

CREATE TABLE room (
    R_NAME VARCHAR(255),
    R_NUMBER INT,
    FLOOR_NUMBER INT,

    PRIMARY KEY (R_NUMBER)
);

CREATE TABLE Doctor(
    DOC_FNAME VARCHAR(255),
    DOC_LNAME VARCHAR(255),
    DOC_ADDRESS VARCHAR(255),
    DOC_SSN INT,
    DOC_GENDER VARCHAR(255),
    DOC_AGE INT,
    DOC_PHONE INT,
    DOC_SALARY INT,

    DOC_ROOM_NUMBER INT,

    username varchar(255) DEFAULT "username",
    password varchar(255) DEFAULT "password",

    PRIMARY KEY (DOC_SSN),
    FOREIGN KEY (DOC_ROOM_NUMBER) REFERENCES room(R_NUMBER)
);

CREATE TABLE nurse(
    NUR_SSN int,
    NUR_FNAME varchar(255),
    NUR_LNAME varchar(255),
    NUR_AGE int,
    NUR_PHONE int,
    NUR_ADDRESS varchar(255),
    NUR_GENDER varchar(255),
    NUR_SALARY int,

    NUR_ROOM_NUMBER int,
    NUR_DOC_SSN int,

    username varchar(255) DEFAULT "username",
    password varchar(255) DEFAULT "password",

    PRIMARY KEY (NUR_SSN),
    FOREIGN KEY (NUR_ROOM_NUMBER) REFERENCES room(R_NUMBER),
    FOREIGN KEY (NUR_DOC_SSN) REFERENCES doctor(DOC_SSN)


);

CREATE TABLE patient(
	PAT_FNAME varchar(255),
    PAT_LNAME varchar(255),
    PAT_SSN int,
    PAT_AGE int,
    PAT_PHONE int,
    PAT_DISEASE varchar(255),
    PAT_MEDICINE varchar(255),
    PAT_ADDRESS varchar(255),
    PAT_GENDER varchar(255),

    PAT_ROOM_NUMBER int,
    PAT_DOC_SSN int,
    PAT_NUR_SSN int,

    username varchar(255) DEFAULT "username",
    password varchar(255) DEFAULT "password",

    PRIMARY KEY (PAT_SSN),
    FOREIGN KEY (PAT_ROOM_NUMBER) REFERENCES room(R_NUMBER),
    FOREIGN KEY (PAT_DOC_SSN) REFERENCES doctor(DOC_SSN),
    FOREIGN KEY (PAT_NUR_SSN) REFERENCES nurse(NUR_SSN)


);

CREATE TABLE Dependent (
    DEP_SSN int,
    DEP_NAME VARCHAR(255),
    DEP_RELATIONSHIP VARCHAR(255),
    DEP_GENDER VARCHAR(255),
    DEP_AGE INT,
    DEP_PHONE INT,

    DEP_PAT_SSN INT,

    PRIMARY KEY (DEP_SSN),
    FOREIGN KEY (DEP_PAT_SSN) REFERENCES patient(PAT_SSN)
);

CREATE TABLE Equipment(
    EQ_CODE int,
    EQ_MANUFACTURER VARCHAR(255),
    EQ_NAME VARCHAR(255),
    EQ_MODEL VARCHAR(255),
    EQ_PAT_SSN INT,

    PRIMARY KEY (EQ_CODE),
    FOREIGN KEY (EQ_PAT_SSN) REFERENCES patient(PAT_SSN)
);

CREATE TABLE complaint(
    id int,
    email varchar(255),
    firstname varchar(255),
    lastname varchar(255),
    role varchar(255),
    ssn int,
    complainttext varchar(3000),
    PRIMARY KEY (id)--,
--  FOREIGN KEY (ssn) REFERENCES doctor(DOC_ssn),
--   FOREIGN KEY (ssn) REFERENCES nurse(NUR_ssn),
--    FOREIGN KEY (ssn) REFERENCES patient(PAT_ssn)
);

CREATE TABLE visit(
    V_CODE int AUTO_INCREMENT,
    V_STARTDATE date,
    V_ENDDATE date,
    V_PAT_SSN int,
    PRIMARY KEY (V_CODE),
    FOREIGN KEY (V_PAT_SSN) REFERENCES patient(PAT_SSN)

);







