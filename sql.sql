-- DROP TABLE IF NOT EXISTS "users";
DROP TABLE "users" CASCADE;
-- DROP TABLE IF NOT EXISTS "incidents";
DROP TABLE "incidents" CASCADE;

-- CREATE TABLE IF NOT EXISTS "users" (
CREATE TABLE users (
   user_Id BIGSERIAL  PRIMARY KEY  NOT NULL,
   first_Name VARCHAR (255)   NOT NULL,
   last_Name VARCHAR (255)   NOT NULL,
   other_Name VARCHAR (255)   NULL,
   email  VARCHAR (255)  UNIQUE  NOT NULL,
   user_Name  VARCHAR (255)  NOT NULL ,
   phone_Number   VARCHAR (255)   NOT NULL, 
   passwd VARCHAR (255)   NOT NULL,
   isAdmin  BOOLEAN   NOT NULL,      
   joinning  timestamp   NOT NULL
);

INSERT INTO users (
  user_Id,first_Name,last_Name,other_Name,email,
  user_Name,phone_Number,passwd,isAdmin,joinning)
 VALUES (1,'Admin','Adminlast_Name','other_Name',
  'ireporterManuelDominic@gmail.com','admin',256788084708,
  'pbkdf2:sha256:50000$Mxe0PmNZ$b3048ca190fbb746536b0642f3219f428361e506607bd7eec21f5ec35c777fa6'
  ,TRUE, now());


-- CREATE TABLE IF NOT EXISTS "incidents" (
CREATE TABLE incidents (
   incident_Id BIGSERIAL  PRIMARY KEY  NOT NULL,
   created_By  BIGSERIAL REFERENCES users (user_Id),
   incident_Type VARCHAR (255)   NOT NULL,
   comment  VARCHAR (255) UNIQUE  NOT NULL,
   status_View  VARCHAR (255)  NOT NULL ,
   images   VARCHAR (255)   NOT NULL, 
   videos VARCHAR (255)   NOT NULL,
   created_On  timestamp   NOT NULL,
   latitude FLOAT(6) NOT NULL ,
   longititude  FLOAT(6) NOT NULL   
);
