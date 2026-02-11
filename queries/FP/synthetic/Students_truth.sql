SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 101 and university = 'UT';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 102 and university = 'UT';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 103 and university = 'EIND';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 104 and university = 'EIND';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 105 and university = 'AMS';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 101 and university = 'EIND';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 103 and university = 'AMS';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 106 and university = 'UT';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 102 and university = 'AMS';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age FROM prototype_fp_1.students_truth WHERE sid = 104 and university = 'UT';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'John Bell';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'Claire Stevens';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'Pet Norton';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'George Bailey';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'Leah Murphy';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'David Wong';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'Maria Rossi';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'Rahul Mehta';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'Aisha Khan';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where sname = 'Sofia Janssen';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where university = 'UT';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where university = 'AMS';

SELECT sid,sname,university,address,emailid,phonenum,postcode,age from prototype_fp_1.students_truth st where university = 'EIND';

SELECT DISTINCT university,sname FROM prototype_fp_1.students_truth;

SELECT DISTINCT sid,sname FROM prototype_fp_1.students_truth;

SELECT DISTINCT sname FROM prototype_fp_1.students_truth;

SELECT DISTINCT address,sname FROM prototype_fp_1.students_truth;

SELECT DISTINCT emailid,sname FROM prototype_fp_1.students_truth;

SELECT DISTINCT phonenum,sname FROM prototype_fp_1.students_truth;

SELECT DISTINCT postcode,sname FROM prototype_fp_1.students_truth;

select sid,sname from prototype_fp_1.students_truth st where university = 'UT' group by sid,sname;

select sid,sname from prototype_fp_1.students_truth st where university = 'AMS' group by sid,sname;

select sid,sname from prototype_fp_1.students_truth st where university = 'EIND' group by sid,sname;

select sname, university  from prototype_fp_1.students_truth st where sid = 101 group by sname, university ;

select sname, university  from prototype_fp_1.students_truth st where sid = 102 group by sname, university ;

select sname, university  from prototype_fp_1.students_truth st where sid = 103 group by sname, university ;

select sname, university  from prototype_fp_1.students_truth st where sid = 104 group by sname, university ;

select sname, university  from prototype_fp_1.students_truth st where sid = 105 group by sname, university ;

select sname, university  from prototype_fp_1.students_truth st where sid = 106 group by sname, university ;