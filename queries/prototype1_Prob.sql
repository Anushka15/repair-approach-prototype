SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SID"  = 101 and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SID"  = 102 and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SID"  = 103 and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SID"  = 104 and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SID"  = 105 and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SName"  = 'John Bell' and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SName"  = 'Claire Stevens' and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SName"  = 'Pet Nortan' and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SName"  = 'George Bailey' and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."SName"  = 'Leah Murphy' and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."University"  = 'UT' and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."University"  = 'AMS' and d.name = 'students_dict' order by probability desc;

SELECT s1."SID" ,s1."SName" ,s1."University" ,s1."Address" ,s1."EmailId" ,s1."PhoneNum" ,s1."Postcode", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d  WHERE s1."University"  = 'EIND' and d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1."University",s1."SName", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1."SID",s1."SName", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1."SName", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1."Address",s1."SName", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1."EmailId",s1."SName", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1."PhoneNum",s1."SName", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1."Postcode",s1."SName", ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype1.students_prob s1, prototype1."_dict" d where d.name = 'students_dict' order by probability desc;

CREATE OR REPLACE VIEW prototype1.students_UT_Uni as select s1."SID",s1."SName",agg_or(s1._sentences::Bdd) as _sentences from prototype1.students_prob s1 where s1."University" = 'UT' group by s1."SID",s1."SName" ;
select s1."SID",s1."SName" ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype1.students_UT_Uni s1 ,prototype1."_dict" d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype1.students_AMS_Uni as select s1."SID",s1."SName", agg_or(s1._sentences::Bdd) as _sentences from prototype1.students_prob s1 where s1."University" = 'AMS' group by s1."SID",s1."SName" ;
select s1."SID",s1."SName" ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype1.students_AMS_Uni s1 ,prototype1."_dict" d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype1.students_EIND_Uni as select s1."SID",s1."SName",agg_or(s1._sentences::Bdd) as _sentences from prototype1.students_prob s1 where s1."University" = 'EIND' group by s1."SID" ,s1."SName";
select s1."SID",s1."SName" ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype1.students_EIND_Uni s1 ,prototype1."_dict" d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype1.students_101_SID as select s1."University",s1."SName", agg_or(s1._sentences::Bdd) as _sentences from prototype1.students_prob s1 where s1."SID" = 101 group by s1."University",s1."SName" ;
select s1."University",s1."SName" ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype1.students_101_SID s1 ,prototype1."_dict" d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype1.students_102_SID as select s1."University",s1."SName", agg_or(s1._sentences::Bdd) as _sentences from prototype1.students_prob s1 where s1."SID" = 102 group by s1."University",s1."SName" ;
select s1."University",s1."SName" ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype1.students_102_SID s1 ,prototype1."_dict" d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype1.students_103_SID as select s1."University",s1."SName", agg_or(s1._sentences::Bdd) as _sentences from prototype1.students_prob s1 where s1."SID" = 103 group by s1."University",s1."SName" ;
select s1."University",s1."SName" ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype1.students_103_SID s1 ,prototype1."_dict" d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype1.students_104_SID as select s1."University",s1."SName", agg_or(s1._sentences::Bdd) as _sentences from prototype1.students_prob s1 where s1."SID" = 104 group by s1."University" ,s1."SName";
select s1."University",s1."SName" ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype1.students_104_SID s1 ,prototype1."_dict" d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype1.students_105_SID as select s1."University",s1."SName", agg_or(s1._sentences::Bdd) as _sentences from prototype1.students_prob s1 where s1."SID" = 105 group by s1."University",s1."SName" ;
select s1."University",s1."SName" ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype1.students_105_SID s1 ,prototype1."_dict" d where d.name = 'students_dict' order by probability desc ;