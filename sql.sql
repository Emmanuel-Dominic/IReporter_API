
CREATE TABLE IF NOT EXISTS "users" (
   user_Id BIGSERIAL  PRIMARY KEY  NOT NULL,
   first_Name VARCHAR (255)   NOT NULL,
   last_Name VARCHAR (255)   NOT NULL,
   other_Name VARCHAR (255)  NULL,
   email  VARCHAR (255) NOT NULL,
   user_Name  VARCHAR (255)  NOT NULL ,
   phone_Number   VARCHAR (255)  NOT NULL, 
   Passwd VARCHAR (255)   NOT NULL,
   isAdmin  BOOLEAN   NOT NULL  DEFAULT FALSE,
   joinning  timestamp   NOT NULL,
   UNIQUE(email)
);

TRUNCATE TABLE users CASCADE;

INSERT INTO users (
   user_Id,first_Name,last_Name,other_Name,email,
   user_Name,phone_Number,passwd,isAdmin,joinning)
 VALUES (1,'Admin','Adminlast_Name','Adminother_Name',
   'ireporterManuelDominic@gmail.com','admin',256788084708,
   'pbkdf2:sha256:50000$pBGAhyZb$d0405efaf8d3bc9287e36cfd1594789b85193ddf07739886cc69b71a7e509032',
   TRUE,'Thu, 10 Jan 2019 04:01:14 GMT');


CREATE TABLE IF NOT EXISTS "incidents" (
   incident_Id BIGSERIAL  PRIMARY KEY  NOT NULL,
   title  VARCHAR (50) NOT NULL,
   created_By  BIGSERIAL,
   incident_Type VARCHAR (255) NOT NULL,
   comment  VARCHAR (255) UNIQUE NOT NULL,
   status_  VARCHAR (255)  NOT NULL DEFAULT 'draft',
   images   VARCHAR (255)  NULL, 
   videos VARCHAR (255)   NULL,
   created_On  timestamp NOT NULL,
   latitude FLOAT(6) NOT NULL ,
   longtitude  FLOAT(6) NOT NULL,
   FOREIGN KEY (created_By) REFERENCES users (user_Id) ON DELETE CASCADE,
   FOREIGN KEY (created_By) REFERENCES users (user_Id) ON UPDATE CASCADE
);

TRUNCATE TABLE incidents CASCADE;

