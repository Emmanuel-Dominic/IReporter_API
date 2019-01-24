
INSERT INTO users (
   user_Id,first_Name,last_Name,other_Name,email,
   user_Name,phone_Number,passwd,isAdmin,joinning)
 VALUES (2,'manuel','manuellast_Name','manuelother_Name',
   'ematembu2@gmail.com','manuel',256700701616,
   'pbkdf2:sha256:50000$kEBD7Z97$97db32267f5d0956994c5db567ffda9f45cd6f136a7e2d0f9029f3d68b882b1c',
   FALSE,'Thu, 10 Jan 2019 04:01:14 GMT');


INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (1,'Theift',2,'redflag','Arnold stole hassan phone and laptop from his car',
   'draft','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (2,'Smuggling',2,'redflag','Every night at malamba boarders, people smuggle kenya rice into the country',
 'draft','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (3,'Rape',2,'redflag','Timothy raped Jane last night at 11pm after breaking into her apartment',
 'Rejected','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (4,'Rape',2,'redflag','Hadrico raped lona last month at 11pm after breaking into her apartment',
 'Rejected','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);



INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (5,'Road Breakdown',2,'intervention','Mbale highway broken down after a previous track accident last month amonth ',
 'draft','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (6,'Incoprate hospital services',2,'intervention','Mbarara medical facilities lack proper medication and labour ward services',
 'draft','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);

INSERT INTO incidents (incident_id,title,created_By,incident_Type,
   comment,status_,images,videos,created_On,latitude,longtitude)
 VALUES (7,'Bridge construction',2,'intervention','Jinja bridge needs replacement because it is past its deadline date',
 'draft','1.jpeg','1.gif', 'Thu, 10 Jan 2019 04:01:14 GMT',5.38974,0.33737);


