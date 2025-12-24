* student
    * rollno
    * name
    * email
    * course

* create table students(rollno INT, name VARCHAR(32), email VARCHAR(32), course VARCHAR(32));

* insert into students values(1, "abc", "abc@abc.com", "etc");

* insert into students(name, email, rollno, course) values("xyz", "xyz@xyz.com", 2, "csml");

* select * from students;

* update students SET email = "xyz02@xyz.com" where name = "xyz";

* delete from students where rollno = 2;

* To install mysql connector for python
    * pip install mysql-connector-python

* To install flask
    * pip install flask