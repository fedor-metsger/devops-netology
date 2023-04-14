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
