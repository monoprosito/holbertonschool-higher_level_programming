# SQL Introduction

# Learning Objectives

* What’s a database
* What’s a relational database
* What does SQL stand for
* What’s MySQL
* How to create a database in MySQL
* What does `DDL` and `DML` stand for
* How to `CREATE` or `ALTER` a table
* How to `SELECT` data from a table
* How to `INSERT`, `UPDATE` or `DELETE` data
* What are `subqueries`
* How to use MySQL functions

# Tasks

## List databases

Write a script that lists all databases of your MySQL server.

**Solution:** [0-list_databases.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/0-list_databases.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
$ amonkeyprogramer@ubuntu:~/$
```

## Create a database

Write a script that creates the database `hbtn_0c_0` in your MySQL server.

* If the database `hbtn_0c_0` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

**Solution:** [1-create_database_if_missing.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/1-create_database_if_missing.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
$ amonkeyprogramer@ubuntu:~/$ cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
Enter password: 
$ amonkeyprogramer@ubuntu:~/$
```

## Delete a database

Write a script that deletes the database `hbtn_0c_0` in your MySQL server.

* If the database `hbtn_0c_0` doesn’t exist, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

**Solution:** [2-remove_database.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/2-remove_database.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
hbtn_0c_0
mysql
performance_schema
$ amonkeyprogramer@ubuntu:~/$ cat 2-remove_database.sql | mysql -hlocalhost -uroot -p
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
Enter password: 
Database
information_schema
mysql
performance_schema
$ amonkeyprogramer@ubuntu:~/$
```

## List tables

Write a script that lists all the tables of a database in your MySQL server.

* The database name will be passed as argument of `mysql` command (in the following example: `mysql` is the name of the database)

**Solution:** [3-list_tables.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/3-list_tables.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
Enter password: 
Tables_in_mysql
columns_priv
db
event
func
general_log
help_category
help_keyword
help_relation
help_topic
host
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
servers
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
$ amonkeyprogramer@ubuntu:~/$
```

## First table

Write a script that creates a table called `first_table` in the current database in your MySQL server.

* `first_table` description:
    * `id` INT
    * `name` VARCHAR(256)
* The database name will be passed as an argument of the `mysql` command
* If the table `first_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` or `SHOW` statements

**Solution:** [4-first_table.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/4-first_table.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 3-list_tables.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Tables_in_hbtn_0c_0
first_table
$ amonkeyprogramer@ubuntu:~/$
```

## Full description

Write a script that prints the full description of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

* The database name will be passed as an argument of the `mysql` command
* You are not allowed to use the `DESCRIBE` or `EXPLAIN` statements

**Solution:** [5-full_table.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/5-full_table.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=latin1
$ amonkeyprogramer@ubuntu:~/$
```

## List all in table

Write a script that lists all rows of the table `first_table` from the database `hbtn_0c_0` in your MySQL server.

* All fields should be printed
* The database name will be passed as an argument of the `mysql` command

**Solution:** [6-list_values.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/6-list_values.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
$ amonkeyprogramer@ubuntu:~/$
```

## First add

Write a script that inserts a new row in the table `first_table` (database `hbtn_0c_0`) in your MySQL server.

* New row:
    * `id` = `89`
    * `name` = `Holberton School`
* The database name will be passed as an argument of the `mysql` command

**Solution:** [7-insert_value.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/7-insert_value.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Holberton School
$ amonkeyprogramer@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
id  name
89  Holberton School
89  Holberton School
89  Holberton School
$ amonkeyprogramer@ubuntu:~/$
```

## Count 89

Write a script that displays the number of records with `id = 89` in the table `first_table` of the database `hbtn_0c_0` in your MySQL server.

* The database name will be passed as an argument of the `mysql` command

**Solution:** [8-count_89.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/8-count_89.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
Enter password: 
3
$ amonkeyprogramer@ubuntu:~/$
```

## Full creation

Write a script that creates a table `second_table` in the database `hbtn_0c_0` in your MySQL server and add multiples rows.

* `second_table` description:
    * `id` INT
    * `name` VARCHAR(256)
    * `score` INT
* The database name will be passed as an argument to the `mysql` command
* If the table `second_table` already exists, your script should not fail
* You are not allowed to use the `SELECT` and `SHOW` statements
* Your script should create these records:
    * `id` = 1, `name` = “John”, `score` = 10
    * `id` = 2, `name` = “Alex”, `score` = 3
    * `id` = 3, `name` = “Bob”, `score` = 14
    * `id` = 4, `name` = “George”, `score` = 8

**Solution:** [9-full_creation.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/9-full_creation.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
$ amonkeyprogramer@ubuntu:~/$
```

## List by best

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command

**Solution:** [10-top_score.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/10-top_score.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
8   George
3   Alex
$ amonkeyprogramer@ubuntu:~/$
```

## Select the best

Write a script that lists all records with a `score >= 10` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* Results should display both the score and the name (in this order)
* Records should be ordered by score (top first)
* The database name will be passed as an argument of the `mysql` command

**Solution:** [11-best_score.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/11-best_score.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
14  Bob
10  John
$ amonkeyprogramer@ubuntu:~/$
```

## Cheating is bad
``
Write a script that updates the score of Bob to `10` in the table `second_table`.

* You are not allowed to use Bob’s id value, only the `name` field
* The database name will be passed as an argument of the `mysql` command

**Solution:** [12-no_cheating.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/12-no_cheating.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
3   Alex
$ amonkeyprogramer@ubuntu:~/$
```

## Score too low

Write a script that removes all records with a `score <= 5` in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* The database name will be passed as an argument of the `mysql` command

**Solution:** [13-change_class.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/13-change_class.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 13-change_class.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
10  John
10  Bob
8   George
$ amonkeyprogramer@ubuntu:~/$
```

## Average

Write a script that computes the score average of all records in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* The result column name should be `average`
* The database name will be passed as an argument of the `mysql` command

**Solution:** [14-average.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/14-average.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
average
9.3333
$ amonkeyprogramer@ubuntu:~/$
```

## Number by score

Write a script that lists the number of records with the same score in the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* The result should display:
    * the `score`
    * the number of records for this `score` with the label `number`
* The list should be sorted by the number of records (descending)
* The database name will be passed as an argument to the `mysql` command

**Solution:** [15-groups.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/15-groups.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   number
10  2
8   1
$ amonkeyprogramer@ubuntu:~/$
```

## Say my name

Write a script that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server.

* Don’t list rows without a `name` value
* Results should display the score and the name (in this order)
* Records should be listed by descending score
* The database name will be passed as an argument to the `mysql` command

In this example, new data have been added to the table `second_table`.

**Source:** [16-no_link.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/16-no_link.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
score   name
18  Aria
12  Aria
10  John
10  Bob
$ amonkeyprogramer@ubuntu:~/$
```

## Go to UTF8

Write a script that converts `hbtn_0c_0` database to UTF8 (`utf8mb4`, collate `utf8mb4_unicode_ci`) in your MySQL server.

You need to convert all of the following to `UTF8`:

* Database `hbtn_0c_0`
* Table `first_table`
* Field `name` in `first_table`

**Solution:** [100-move_to_utf8.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/100-move_to_utf8.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 100-move_to_utf8.sql | mysql -hlocalhost -uroot -p 
Enter password: 
$ amonkeyprogramer@ubuntu:~/$ cat 5-full_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
Table   Create Table
first_table CREATE TABLE `first_table` (\n  `id` int(11) DEFAULT NULL,\n  `name` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL\n) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
$ amonkeyprogramer@ubuntu:~/$
```

## Temperatures #0

Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql)

Write a script that displays the average temperature (Fahrenheit) by city ordered by temperature (descending).

**Solution:** [101-avg_temperatures.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/101-avg_temperatures.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 101-avg_temperatures.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Chandler    72.8627
Gilbert 71.8088
Pismo beach 71.5147
San Francisco   71.4804
Sedona  70.7696
Phoenix 70.5882
Oakland 70.5637
Sunnyvale   70.5245
Chicago 70.4461
San Diego   70.1373
Glendale    70.1225
Sonoma  70.0392
Yuma    69.3873
San Jose    69.2990
Tucson  69.0245
Joliet  68.6716
Naperville  68.1029
Tempe   67.0441
Peoria  66.5392
$ amonkeyprogramer@ubuntu:~/$
```

## Temperatures #1

Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)

Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

**Solution:** [102-top_city.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/102-top_city.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 102-top_city.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
city    avg_temp
Naperville  76.9412
San Diego   73.7941
Sunnyvale   73.2353
$ amonkeyprogramer@ubuntu:~/$
```

## Temperatures #2

Import in `hbtn_0c_0` database this table dump: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) (same as `Temperatures #0`)

Write a script that displays the max temperature of each state (ordered by State name).

**Solution:** [103-max_state.sql](https://github.com/monoprosito/holbertonschool-higher_level_programming/blob/master/0x0D-SQL_introduction/103-max_state.sql)

```
$ amonkeyprogramer@ubuntu:~/$ cat 103-max_state.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
Enter password: 
state   max_temp
AZ  110
CA  110
IL  110
$ amonkeyprogramer@ubuntu:~/$
```
