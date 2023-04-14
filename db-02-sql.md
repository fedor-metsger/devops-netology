# Домашнее задание к занятию 2. «SQL»

1. **Используя Docker, поднимите инстанс PostgreSQL (версию 12) c 2 volume, в который будут складываться данные БД и бэкапы. Приведите получившуюся команду или docker-compose-манифест.**

      Ответ:
      ```
      root@server1:/home/vagrant/Netology/DevOps/hw_sql# cat docker-compose-pg.yaml
      version: '3.3'
      services:
        db:
          image: postgres:12.0-alpine
          restart: always
        environment:
          - POSTGRES_USER=postgres
          - POSTGRES_PASSWORD=postgres
          - PGDATA=/var/lib/postgresql/data
        ports:
          - '5432:5432'
        volumes:
          - ./db:/var/lib/postgresql/data
          - ./backup:/var/lib/postgresql/backup
      root@server1:/home/vagrant/Netology/DevOps/hw_sql# 
      ```
2. **В БД из задачи 1:**
      - **создайте пользователя test-admin-user и БД test_db;**
      - **в БД test_db создайте таблицу orders и clients (спeцификация таблиц ниже);**
      - **предоставьте привилегии на все операции пользователю test-admin-user на таблицы БД test_db;**
      - **создайте пользователя test-simple-user;**
      - **предоставьте пользователю test-simple-user права на SELECT/INSERT/UPDATE/DELETE этих таблиц БД test_db.**  
      
    **Приведите:**
      - **итоговый список БД после выполнения пунктов выше;**

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
       test_db   | postgres | UTF8     | en_US.utf8 | en_US.utf8 |            | libc            |     
      (4 rows)
      ```
      - **описание таблиц (describe);**
      ```
      test_db=# \d
                     List of relations
       Schema |      Name      |   Type   |  Owner
      --------+----------------+----------+----------
       public | clients        | table    | postgres
       public | clients_id_seq | sequence | postgres
       public | orders         | table    | postgres
       public | orders_id_seq  | sequence | postgres
      (4 rows)


      test_db=# \d orders
                                   Table "public.orders"
       Column |         Type          | Collation | Nullable |              Default
      --------+-----------------------+-----------+----------+------------------------------------
       id     | integer               |           | not null | nextval('orders_id_seq'::regclass)
       title  | character varying(40) |           | not null |
       price  | integer               |           | not null |
      Indexes:
          "orders_pkey" PRIMARY KEY, btree (id)
      Referenced by:
          TABLE "clients" CONSTRAINT "clients_order_id_fkey" FOREIGN KEY (order_id) REFERENCES orders(id)


      test_db=# \d clients
                                    Table "public.clients"
        Column  |         Type          | Collation | Nullable |               Default
      ----------+-----------------------+-----------+----------+-------------------------------------
       id       | integer               |           | not null | nextval('clients_id_seq'::regclass)
       name     | character varying(40) |           | not null |
       country  | character varying(40) |           | not null |
       order_id | integer               |           |          |
      Indexes:
          "clients_pkey" PRIMARY KEY, btree (id)
      Foreign-key constraints:
          "clients_order_id_fkey" FOREIGN KEY (order_id) REFERENCES orders(id)


      test_db=#
      ```
      - **SQL-запрос для выдачи списка пользователей с правами над таблицами test_db;**
      ```
      SELECT DISTINCT grantee
        FROM information_schema.role_table_grants
       WHERE table_catalog = 'test_db'
         AND grantee != 'PUBLIC'
      ```
      - **список пользователей с правами над таблицами test_db.**
      ```
      test_db=# SELECT DISTINCT grantee
      test_db-#   FROM information_schema.role_table_grants
      test_db-#  WHERE table_catalog = 'test_db'
      test_db-#    AND grantee != 'PUBLIC';
       grantee
      ------------------
       postgres
       test_admin_user
       test_simple_user
      (3 rows)


      test_db=#
      ```
      
2. **Используя SQL-синтаксис, наполните таблицы следующими тестовыми данными:**  
      **Используя SQL-синтаксис: вычислите количество записей для каждой таблицы.**  
      **Приведите в ответе:**  
      - **запросы,**  
            
      ```
      INSERT INTO orders (title, price)
           VALUES ('Шоколад', 10),
                  ('Принтер', 3000),
                  ('Книга', 500),
                  ('Монитор', 7000),
                  ('Гитара', 4000);
       
      INSERT INTO clients (name, country)
           VALUES ('Иванов Иван Иванович', 'USA'),
                  ('Петров Петр Петрович', 'Canada'),
                  ('Иоганн Себастьян Бах', 'Japan'),
                  ('Ронни Джеймс Дио', 'Russia'),
                  ('Ritchie Blackmore', 'Russia');
      SELECT * FROM orders;
      SELECT * FROM clients;
      SELECT COUNT(*) FROM orders;
      SELECT COUNT(*) FROM clients;
      ```
      
             
      - **результаты их выполнения.**
      ```
      test_db=# select * from orders;
       id |  title  | price
      ----+---------+-------
        7 | Шоколад |    10
        8 | Принтер |  3000
        9 | Книга   |   500
       10 | Монитор |  7000
       11 | Гитара  |  4000
      (5 rows)


      test_db=# select * from clients;
       id |         name         | country | order_id
      ----+----------------------+---------+----------
        1 | Иванов Иван Иванович | USA     |
        2 | Петров Петр Петрович | Canada  |
        3 | Иоганн Себастьян Бах | Japan   |
        4 | Ронни Джеймс Дио     | Russia  |
        5 | Ritchie Blackmore    | Russia  |
      (5 rows)


      test_db=# SELECT COUNT(*) FROM clients;
       count
      -------
           5
      (1 row)


      test_db=# SELECT COUNT(*) FROM orders;
       count
      -------
           5
      (1 row)


      test_db=#
      ```
            
            
