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

### 2. Посмотрите на сценарий ниже и ответьте на вопрос: «Подходит ли в этом сценарии использование Docker-контейнеров или лучше подойдёт виртуальная машина, физическая машина? Может быть, возможны разные варианты?» Детально опишите и обоснуйте свой выбор.**

**Сценарии:**

- **высоконагруженное монолитное Java веб-приложение;**
  Здесь, пожалуй, усместно будет применить физическую машину, для обеспечения максимальной производительности.
  
- **Nodejs веб-приложение;**  
  Node JS это программная платформа, реализованная на JavaScript. Позволяет разработчикам создавать масштабируемые веб-приложения.
  Исходя из стандартных практик для таких веб приложений, думаю, что в зависимости от проекта лучше использовать контейнеры Docker
  или виртуальные машины.

- **мобильное приложение c версиями для Android и iOS;**  если это приложение рассчитано на большое количество пользователей, думаю,
  оптимальным будет использование большого количества недорогих физических серверов, как, например, это просходит у **Telegram**.
  Если количество пользователей небольшое (до нескольких тысяч, можно использовать виртуальные машины)

- **шина данных на базе Apache Kafka;**  
  Я плохо знаком с Apahe Kafka, прочитал, что это ПО реализовано на Java, что у него большие требования
  к обьёмам памяти, скорости работы сети и скорости дискового ввода вывода. В связи с этим, думаю, оптимально будет разместить на физических
  машинах или в контейнерах Docker.

- **Elasticsearch-кластер для реализации логирования продуктивного веб-приложения — три ноды elasticsearch, два logstash и две ноды kibana**  
  Здесь мне представляется разумным применить docker-контейнеры и виртуальные машины, что бы можно было легко добавлять и убирать количество нод.
  так же переносить их с места на место.
- **мониторинг-стек на базе Prometheus и Grafana**  
  аналогично предыдущему случаю, по тем же причинам.
- MongoDB как основное хранилище данных для Java-приложения
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

### 4. Воспроизведите практическую часть лекции самостоятельно. Соберите Docker-образ с Ansible, загрузите на Docker Hub и пришлите ссылку вместе с остальными ответами к задачам.

Ответ: https://hub.docker.com/r/femetsger/ansible

```
root@server1:/home/fedor/Netology/DevOps/docker-ansible# cat Dockerfile
# Манифест Docker образа.
FROM alpine:3.16
RUN  CARGO_NET_GIT_FETCH_WITH_CLI=1 && \
     apk --no-cache add sudo python3 py3-pip openssl ca-certificates \
         sshpass openssh-client rsync git && \
     apk --no-cache add --virtual build-dependencies python3-dev libffi-dev \
         musl-dev gcc cargo openssl-dev libressl-dev build-base && \
     apk del py3-packaging && \
     pip install --upgrade pip wheel && \
     pip install --upgrade cryptography cffi && \
     pip install ansible==2.9.24 && \
     pip install mitogen && \
     apk add ansible-lint && \
     pip install jmespath && \
     pip install --upgrade pywinrm && \
     apk del build-dependencies && \
     rm -rf /var/cache/apk/* && \
     rm -rf /root/.cache/pip && \
     rm -rf /root/.cargo

RUN  mkdir /ansible && \
     mkdir -p /etc/ansible && \
     echo 'localhost' > /etc/ansible/hosts

WORKDIR /ansible

CMD  [ "ansible-playbook", "--version" ]
root@server1:/home/fedor/Netology/DevOps/docker-ansible#
```
```
root@server1:/home/fedor/Netology/DevOps/docker-ansible# docker build -t femetsger/ansible:2.9.24 .
[+] Building 1.2s (4/4) FINISHED
 => [internal] load build definition from Dockerfile                                                                              0.0s
 => => transferring dockerfile: 989B                                                                                              0.0s
 => [internal] load .dockerignore                                                                                                 0.0s
 => => transferring context: 2B                                                                                                   0.0s
 => ERROR [internal] load metadata for docker.io/library/alpine:3.16.4                                                            1.1s
 => [auth] library/alpine:pull token for registry-1.docker.io                                                                     0.0s
------
 > [internal] load metadata for docker.io/library/alpine:3.16.4:
------
ERROR: failed to solve: Canceled: context canceled
root@server1:/home/fedor/Netology/DevOps/docker-ansible# vi Dockerfile
root@server1:/home/fedor/Netology/DevOps/docker-ansible# docker build -t femetsger/ansible:2.9.24 .
[+] Building 253.7s (9/9) FINISHED
 => [internal] load build definition from Dockerfile                                                                              0.1s
 => => transferring dockerfile: 987B                                                                                              0.0s
 => [internal] load .dockerignore                                                                                                 0.0s
 => => transferring context: 2B                                                                                                   0.0s
 => [internal] load metadata for docker.io/library/alpine:3.16                                                                    1.0s
 => [auth] library/alpine:pull token for registry-1.docker.io                                                                     0.0s
 => CACHED [1/4] FROM docker.io/library/alpine:3.16@sha256:2cf17aa35fbcb6ece81692a64bfbadaf096590241ed9f95dd5f94f0e9f674784       0.0s
 => [2/4] RUN  CARGO_NET_GIT_FETCH_WITH_CLI=1 &&      apk --no-cache add sudo python3 py3-pip openssl ca-certificates           245.3s
 => [3/4] RUN  mkdir /ansible &&      mkdir -p /etc/ansible &&      echo 'localhost' > /etc/ansible/hosts                         1.0s
 => [4/4] WORKDIR /ansible                                                                                                        0.1s
 => exporting to image                                                                                                            6.1s
 => => exporting layers                                                                                                           6.1s
 => => writing image sha256:397ad4af1f88c22713f1f4e6bc9c6850e35e034a070fa43dcb4b2c27df7d433c                                      0.0s
 => => naming to docker.io/femetsger/ansible:2.9.24                                                                               0.0s
root@server1:/home/fedor/Netology/DevOps/docker-ansible#
```
```
root@server1:/home/fedor/Netology/DevOps/docker-ansible# docker run femetsger/ansible:2.9.24
ansible-playbook [core 2.13.6]
  config file = None
  configured module search path = ['/root/.ansible/plugins/modules', '/usr/share/ansible/plugins/modules']
  ansible python module location = /usr/lib/python3.10/site-packages/ansible
  ansible collection location = /root/.ansible/collections:/usr/share/ansible/collections
  executable location = /usr/bin/ansible-playbook
  python version = 3.10.10 (main, Feb  9 2023, 02:08:34) [GCC 11.2.1 20220219]
  jinja version = 3.0.3
  libyaml = True
root@server1:/home/fedor/Netology/DevOps/docker-ansible# docker push femetsger/ansible:2.9.24
The push refers to repository [docker.io/femetsger/ansible]
5f70bf18a086: Pushed
797e8ec3d75b: Pushed
0b02b9f8649b: Pushed
aa5968d388b8: Mounted from library/alpine
2.9.24: digest: sha256:ed8cdba1a9fe933d513478c18777d1785a0772f31ffa44f75f328a78103ae644 size: 1153
root@server1:/home/fedor/Netology/DevOps/docker-ansible#
```
