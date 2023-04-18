# Домашнее задание к занятию 4. «PostgreSQL»

1. **Используя Docker, поднимите инстанс PostgreSQL (версию 13). Данные БД сохраните в volume.**
**Подключитесь к БД PostgreSQL, используя psql. Воспользуйтесь командой \? для вывода подсказки по имеющимся в psql управляющим командам.**
**Найдите и приведите управляющие команды для:**
- **вывода списка БД,**

    Ответ: **\l**
```
postgres=# \l
                                                List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    | ICU Locale | Locale Provider |   Access privileges
-----------+----------+----------+------------+------------+------------+-----------------+-----------------------
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            |
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            | =c/postgres          +
           |          |          |            |            |            |                 | postgres=CTc/postgres
(3 rows)


postgres=#
```
- **подключения к БД,**

    Ответ: **\c**
```
postgres=# \c postgres
psql (15.2, server 13.0)
You are now connected to database "postgres" as user "postgres".
postgres=#
```
- **вывода списка таблиц,**

    Ответ: **\d**
```
postgres=# \d
         List of relations
 Schema |  Name  | Type  |  Owner
--------+--------+-------+----------
 public | table1 | table | postgres
(1 row)


postgres=#
```
- **вывода описания содержимого таблиц,**
 
    Ответ: **\d <имя таблицы>**
```
postgres=# \d table1
                      Table "public.table1"
 Column |         Type          | Collation | Nullable | Default
--------+-----------------------+-----------+----------+---------
 field1 | integer               |           |          |
 field2 | character varying(20) |           |          |


postgres=#
```
- **выхода из psql.**

    Ответ: **\q**
```
postgres-# \q

C:\Users\User>
```

