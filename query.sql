
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
   'pbkdf2:sha256:50000$LuGTCgii$fd0a6cc9c7e7f70f1b2b76af0a76f217e3ce90b603068d0bb27b67f190de8eb3',
   TRUE,'Thu, 10 Jan 2019 04:01:14 GMT');

INSERT INTO users (
   user_Id,first_Name,last_Name,other_Name,email,
   user_Name,phone_Number,passwd,joinning)
 VALUES (2,'manuel','manuellast_Name','manuelother_Name',
   'ematembu2@gmail.com','manuel',256700701616,
   'pbkdf2:sha256:50000$sQueRoWd$816cacdef85cee03292df7cb84af19f9a0fb10a547d31178d9fccdf55fe80698',
   'Thu, 10 Jan 2019 04:01:14 GMT');




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


INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (1,'Theift',2,'redflag','Arnold stole hassan phone and laptop from his car',DEFAULT,
   '1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (2,'Smuggling',2,'redflag','Every night at malamba boarders, people smuggle kenya rice into the country',
 DEFAULT,'1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (3,'Rape',2,'redflag','Timothy raped Jane last night at 11pm after breaking into her apartment',
 'Rejected','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (4,'Rape',2,redflag,'Hadrico raped lona last month at 11pm after breaking into her apartment',
 'Rejected','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);



INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (1,'Road Breakdown',2,'intervention','Mbale highway broken down after a previous track accident last month amonth ',
 DEFAULT,'1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (2,'Incoprate hospital services',2,'intervention','Mbarara medical facilities lack proper medication and labour ward services',
 DEFAULT,'1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (3,'Bridge construction',2,'intervention','Jinja bridge needs replacement because it is past its deadline date',
 DEFAULT,'1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);


