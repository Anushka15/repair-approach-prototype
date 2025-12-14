SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 101 and s1.university = 'UT' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 102 and s1.university = 'UT' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 103 and s1.university = 'EIND' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 104 and s1.university = 'EIND' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 105 and s1.university = 'AMS' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 101 and s1.university = 'EIND' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 103 and s1.university = 'AMS' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 106 and s1.university = 'UT' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 102 and s1.university = 'AMS' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.sid = 104 and s1.university = 'UT' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'John Bell' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'Claire Stevens' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'Pet Norton' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'George Bailey' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'Leah Murphy' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'David Wong' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'Maria Rossi' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'Rahul Mehta' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'Aisha Khan' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.SName  = 'Sofia Janssen' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.University  = 'UT' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.University  = 'AMS' and d.name = 'students_dict' order by probability desc;

SELECT s1.SID ,s1.SName ,s1.University ,s1.Address ,s1.EmailId ,s1.PhoneNum ,s1.Postcode, s1.age, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d  WHERE s1.University  = 'EIND' and d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1.University,s1.SName, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1.SID,s1.SName, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1.SName, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1.Address,s1.SName, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1.EmailId,s1.SName, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1.PhoneNum,s1.SName, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d where d.name = 'students_dict' order by probability desc;

SELECT DISTINCT s1.Postcode,s1.SName, ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability FROM prototype_fp.students_prob s1, prototype_fp._dict d where d.name = 'students_dict' order by probability desc;

CREATE OR REPLACE VIEW prototype_fp.students_UT_Uni as select s1.SID,s1.SName,agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.University = 'UT' group by s1.SID,s1.SName ;
select s1.SID,s1.SName ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_UT_Uni s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype_fp.students_AMS_Uni as select s1.SID,s1.SName, agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.University = 'AMS' group by s1.SID,s1.SName ;
select s1.SID,s1.SName ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_AMS_Uni s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype_fp.students_EIND_Uni as select s1.SID,s1.SName,agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.University = 'EIND' group by s1.SID ,s1.SName;
select s1.SID,s1.SName ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_EIND_Uni s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype_fp.students_101_SID as select s1.University,s1.SName, agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.SID = 101 group by s1.SName,s1.University ;
select s1.SName,s1.University ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_101_SID s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype_fp.students_102_SID as select s1.University,s1.SName, agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.SID = 102 group by s1.SName,s1.University ;
select s1.SName,s1.University ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_102_SID s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype_fp.students_103_SID as select s1.University,s1.SName, agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.SID = 103 group by s1.SName,s1.University ;
select s1.SName,s1.University ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_103_SID s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype_fp.students_104_SID as select s1.University,s1.SName, agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.SID = 104 group by s1.SName,s1.University;
select s1.SName,s1.University ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_104_SID s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype_fp.students_105_SID as select s1.University,s1.SName, agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.SID = 105 group by s1.SName,s1.University ;
select s1.SName,s1.University ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_105_SID s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;

CREATE OR REPLACE VIEW prototype_fp.students_106_SID as select s1.University,s1.SName, agg_or(s1._sentences::Bdd) as _sentences from prototype_fp.students_prob s1 where s1.SID = 106 group by s1.SName,s1.University ;
select s1.SName,s1.University ,ROUND(prob(d.dict, s1._sentences::Bdd)::numeric, 4) AS probability from prototype_fp.students_106_SID s1 ,prototype_fp._dict d where d.name = 'students_dict' order by probability desc ;