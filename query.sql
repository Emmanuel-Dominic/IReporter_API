CREATE DATABASE IF NOT EXISTS "ireporter_Database"
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1;

    
CREATE TABLE IF NOT EXISTS "users" (
   user_Id BIGSERIAL  PRIMARY KEY  NOT NULL,
   first_Name VARCHAR (255)   NOT NULL,
   last_Name VARCHAR (255)   NOT NULL,
   other_Name VARCHAR (255)   NULL,
   email  VARCHAR (255)  UNIQUE  NOT NULL,
   user_Name  VARCHAR (255)  NOT NULL ,
   phone_Number   VARCHAR (255)   NOT NULL, 
   passwd VARCHAR (255)   NOT NULL,
   isAdmin  BOOLEAN   NOT NULL,      
   join_Date  timestamp   NOT NULL
);

INSERT INTO users (
	user_Id,first_Name,last_Name,other_Name,email,
	user_Name,phone_Number,passwd,isAdmin,join_Date)
 VALUES (1,'Admin','Adminlast_Name','other_Name',
 	'admin@ireporter_Database.com','admin',256788084708,
  'pbkdf2:sha256:50000$Mxe0PmNZ$b3048ca190fbb746536b0642f3219f428361e506607bd7eec21f5ec35c777fa6'
  ,TRUE, now());

-- admin123
INSERT INTO users (
	user_Id,first_Name,last_Name,other_Name,email,
	user_Name,phone_Number,passwd,isAdmin,join_Date)
 VALUES (2,'manuel','manuellast_Name','manuelother_Name',
 	'manuel@ireporter_Database.com','manuel',256700701616,'manuel123',FALSE, now());


CREATE TABLE IF NOT EXISTS "incidents" (
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

INSERT INTO "incidents" (incident_Id,created_By,incident_Type,comment,status_View,
	images,videos,created_On,latitude,longititude)
 VALUES (1,2,'redflag','Arnold was caught stealing jack fruit in hassan Garden','draft',
 	'1.jpeg','1.gif', now(),5.38974,0.33737);

INSERT INTO "incidents" (incident_Id,created_By,incident_Type,comment,status_View,
images,videos,created_On,latitude,longititude)
 VALUES (4,2,'redflag','james was caught idle and disorderly','draft',
	'1.jpeg','1.gif', now(),5.38974,0.33737);


INSERT INTO "incidents" (incident_Id,created_By,incident_Type,comment,status_View,
	images,videos,created_On,latitude,longititude)
 VALUES (2,2,'interventon','Mbale highway needs construction','draft',
 	'1.jpeg','1.gif', now(),5.38974,0.33737);

INSERT INTO "incidents" (incident_Id,created_By,incident_Type,comment,status_View,
images,videos,created_On,latitude,longititude)
 VALUES (3,2,'interventon','Mbarara highway needs construction','draft',
	'1.jpeg','1.gif', now(),5.38974,0.33737);

