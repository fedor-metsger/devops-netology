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
2. **Используя psql, создайте БД test_database.**
```
/ # createdb -U postgres -T template0 test_database
/ #
```

**Изучите бэкап БД.**

**Восстановите бэкап БД в test_database.**
```
/var/lib/postgresql/backup # psql -U postgres -d test_database < test_dump.sql
SET
SET
SET
SET
SET
 set_config
------------

(1 row)

SET
SET
SET
SET
SET
SET
CREATE TABLE
ALTER TABLE
CREATE SEQUENCE
ALTER TABLE
ALTER SEQUENCE
ALTER TABLE
COPY 8
 setval
--------
      8
(1 row)

ALTER TABLE
/var/lib/postgresql/backup #
```

**Перейдите в управляющую консоль psql внутри контейнера.**
```
root@server1:/home/vagrant/Netology/DevOps/hw_postgresql# docker exec -it hw_postgresql_db_1 /bin/sh
/ # psql -U postgres -d test_database
psql (13.0)
Type "help" for help.

test_database=#
```

**Подключитесь к восстановленной БД и проведите операцию ANALYZE для сбора статистики по таблице.**
```
test_database-# \d orders
                                   Table "public.orders"
 Column |         Type          | Collation | Nullable |              Default
--------+-----------------------+-----------+----------+------------------------------------
 id     | integer               |           | not null | nextval('orders_id_seq'::regclass)
 title  | character varying(80) |           | not null |
 price  | integer               |           |          | 0
Indexes:
    "orders_pkey" PRIMARY KEY, btree (id)

test_database-# ANALYZE VERBOSE orders;
INFO:  analyzing "public.orders"
INFO:  "orders": scanned 1 of 1 pages, containing 8 live rows and 0 dead rows; 8 rows in sample, 8 estimated total rows
ANALYZE
test_database=#
```

**Используя таблицу pg_stats, найдите столбец таблицы orders с наибольшим средним значением размера элементов в байтах.**

  Ответ: **title**

**Приведите в ответе команду, которую вы использовали для вычисления, и полученный результат.**
```
test_database=# SELECT attname, avg_width FROM pg_stats
test_database-#  WHERE tablename = 'orders'
test_database-#    AND avg_width = (SELECT MAX(avg_width)
test_database(#                      FROM pg_stats
test_database(#                     WHERE tablename = 'orders');
 attname | avg_width
---------+-----------
 title   |        16
(1 row)

test_database=#
```

3. **Архитектор и администратор БД выяснили, что ваша таблица orders разрослась до невиданных размеров и поиск по ней занимает долгое время. Вам как успешному выпускнику курсов DevOps в Нетологии предложили провести разбиение таблицы на 2: шардировать на orders_1 - price>499 и orders_2 - price<=499.**

**Предложите SQL-транзакцию для проведения этой операции.**
```
BEGIN;
CREATE TABLE new_orders (
    id serial,
    title character varying(80) NOT NULL,
    price integer DEFAULT 0,
    CONSTRAINT new_orders_pkey PRIMARY KEY (id, price) 
) PARTITION BY RANGE(price);

CREATE TABLE orders_1 PARTITION OF new_orders
    FOR VALUES FROM (500) TO (MAXVALUE);
ALTER TABLE ONLY orders_1
    ADD CONSTRAINT orders_1_check CHECK (price > 499);

CREATE TABLE orders_2 PARTITION OF new_orders
    FOR VALUES FROM (MINVALUE) TO (500);
ALTER TABLE ONLY orders_2
    ADD CONSTRAINT orders_2_check CHECK (price <= 499);

INSERT INTO new_orders (SELECT * FROM orders);
DROP TABLE orders;
ALTER TABLE new_orders RENAME TO orders;
COMMIT;
```

**Можно ли было изначально исключить ручное разбиение при проектировании таблицы orders?**

Ответ: Ручного разбиения можно было избежать, если изначально сделать таблицу партиционированной по полю **price**.

4 **Используя утилиту pg_dump, создайте бекап БД test_database.**
```
/ # pg_dump -U postgres test_database > test_database.dump
/ #
```

**Как бы вы доработали бэкап-файл, чтобы добавить уникальность значения столбца title для таблиц test_database?**

Ответ: Я бы добавил в конец команду `ALTER TABLE ONLY public.orders ADD CONSTRAINT orders_title UNIQUE (title);`
```
/ # diff test_database*
--- test_database.dump
+++ test_database_new.dump
@@ -94,6 +94,14 @@


 --
+-- Name: orders orders_title; Type: CONSTRAINT; Schema: public; Owner: postgres
+--
+
+ALTER TABLE ONLY public.orders
+    ADD CONSTRAINT orders_title UNIQUE (title);
+
+
+--
 -- PostgreSQL database dump complete
 --

/ #
```


