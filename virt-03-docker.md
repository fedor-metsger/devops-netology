# Домашнее задание к занятию 3. «Введение. Экосистема. Архитектура. Жизненный цикл Docker-контейнера»

### 1. Сценарий выполнения задачи:
- Создайте свой репозиторий на https://hub.docker.com;
- выберите любой образ, который содержит веб-сервер Nginx;
- создайте свой fork образа;
- реализуйте функциональность: запуск веб-сервера в фоне с индекс-страницей, содержащей HTML-код ниже:
```
<html>
<head>
Hey, Netology
</head>
<body>
<h1>I’m DevOps Engineer!</h1>
</body>
</html>
```
### Опубликуйте созданный fork в своём репозитории и предоставьте ответ в виде ссылки hub.docker.com

Ответ: https://hub.docker.com/r/femetsger/nginx

### 2. Посмотрите на сценарий ниже и ответьте на вопрос: «Подходит ли в этом сценарии использование Docker-контейнеров или лучше подойдёт виртуальная машина, физическая машина? Может быть, возможны разные варианты?»

Детально опишите и обоснуйте свой выбор.

Сценарии:

- высоконагруженное монолитное Java веб-приложение;
- Nodejs веб-приложение;
- мобильное приложение c версиями для Android и iOS;
- шина данных на базе Apache Kafka;
- Elasticsearch-кластер для реализации логирования продуктивного веб-приложения — три ноды elasticsearch, два logstash и две ноды kibana;
- мониторинг-стек на базе Prometheus и Grafana;
- MongoDB как основное хранилище данных для Java-приложения;
- Gitlab-сервер для реализации CI/CD-процессов и приватный (закрытый) Docker Registry.

### 3. Запустите первый контейнер из образа centos c любым тегом в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера.
```
root@server1:/home/fedor/Netology/DevOps# docker run -v ./data:/data --name centos1 -t -d centos bash
Unable to find image 'centos:latest' locally
latest: Pulling from library/centos
a1d0c7532777: Pull complete
Digest: sha256:a27fd8080b517143cbbbab9dfb7c8571c40d67d534bbdee55bd6c473f432b177
Status: Downloaded newer image for centos:latest
d8ace206a092fac33a5f2f949c4fc51f8c65170b2f031dff7905b840493ff729
root@server1:/home/fedor/Netology/DevOps# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED          STATUS          PORTS     NAMES
d8ace206a092   centos    "bash"    16 seconds ago   Up 13 seconds             centos1
root@server1:/home/fedor/Netology/DevOps#
```
### Запустите второй контейнер из образа debian в фоновом режиме, подключив папку /data из текущей рабочей директории на хостовой машине в /data контейнера.
```
root@server1:/home/fedor/Netology/DevOps# docker run -v ./data:/data --name debian1 -t -d debian bash
Unable to find image 'debian:latest' locally
latest: Pulling from library/debian
32fb02163b6b: Pull complete
Digest: sha256:f81bf5a8b57d6aa1824e4edb9aea6bd5ef6240bcc7d86f303f197a2eb77c430f
Status: Downloaded newer image for debian:latest
dfc071afd6e7ba9fd11ebaedae935b0013756651ce233780727502c7c3db2f5c
root@server1:/home/fedor/Netology/DevOps# docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED         STATUS         PORTS     NAMES
d8ace206a092   centos    "bash"    3 minutes ago   Up 13 seconds            centos1
dfc071afd6e7   debian    "bash"    6 seconds ago   Up 4 seconds             debian1
root@server1:/home/fedor/Netology/DevOps#
```
### Подключитесь к первому контейнеру с помощью docker exec и создайте текстовый файл любого содержания в /data.
```
root@server1:/home/fedor/Netology/DevOps# docker exec -it centos1 bash
[root@d8ace206a092 /]# touch /data/file_from_centos
[root@d8ace206a092 /]# ls -l /data
total 0
-rw-r--r-- 1 root root 0 Mar 20 12:34 file_from_centos
[root@d8ace206a092 /]#
```
### Добавьте ещё один файл в папку /data на хостовой машине.
```
root@server1:/home/fedor/Netology/DevOps# touch ./data/file_from_host
root@server1:/home/fedor/Netology/DevOps# ls -l ./data
total 0
-rw-r--r-- 1 root root 0 Mar 20 12:34 file_from_centos
-rw-r--r-- 1 root root 0 Mar 20 12:35 file_from_host
root@server1:/home/fedor/Netology/DevOps#
```
### Подключитесь во второй контейнер и отобразите листинг и содержание файлов в /data контейнера.
```
root@server1:/home/fedor/Netology/DevOps# docker exec -it debian1 bash
root@dfc071afd6e7:/# ls -l /data
total 0
-rw-r--r-- 1 root root 0 Mar 20 12:34 file_from_centos
-rw-r--r-- 1 root root 0 Mar 20 12:35 file_from_host
root@dfc071afd6e7:/#
```

