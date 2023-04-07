# Домашнее задание к занятию 5. «Оркестрация кластером Docker контейнеров на примере Docker Swarm»


### 1. Дайте письменые ответы на вопросы:
### В чём отличие режимов работы сервисов в Docker Swarm-кластере: replication и global?

В режиме **global** одна реблика сервиса запускается на каждом узле. Число реплик равно числу узлов.
В режиме **replication** запускается необходимое число реплик, безотносительно к количеству узлов.

### Какой алгоритм выбора лидера используется в Docker Swarm-кластере?

Используется **Raft consensus Algorithm**. Этот алгоримт позволяет нескольким узлам работать сплочённой группой при условии отказа некоторых её членов.
Алгоритм позволяет выдержать отказ **(N-1)/2** узлов (где **N** - максимальное количество узлов)

### Что такое Overlay Network?

**Overlay network** — это виртуальная сеть, работающая поверх другой сети. Устройства в этой сети "не знают", что они находятся в оверлее.
Примером такой сети являются традиционные VPN-сети, работающие через Интернет.
В **docker**-e используется для связи между собой контейнеров, работающих на разных узлах.

### 2. Создайте ваш первый Docker Swarm-кластер в Яндекс Облаке. Чтобы получить зачёт, предоставьте скриншот из терминала (консоли) с выводом команды: `docker node ls`

Ответ:
```
[root@node01 centos]# docker node ls
ID                            HOSTNAME             STATUS    AVAILABILITY   MANAGER STATUS   ENGINE VERSION
e411bahxh6d86i38z3ql7b4pl *   node01.netology.yc   Ready     Active         Leader           23.0.2
cbf54qszds3o7gehlk1xvk9ze     node02.netology.yc   Ready     Active         Reachable        23.0.2
0s7z5ztmtls9iabgvs0wvowoz     node03.netology.yc   Ready     Active         Reachable        23.0.2
15x5xf33m0kgpeti1qjfjmg2r     node04.netology.yc   Ready     Active                          23.0.2
iw1by9ivgkh5ayzl5s3xinvox     node05.netology.yc   Ready     Active                          23.0.2
xvrr0khmu8hlv51koyn37uplj     node06.netology.yc   Ready     Active                          23.0.2
[root@node01 centos]#
```
### 3. Создайте ваш первый, готовый к боевой эксплуатации кластер мониторинга, состоящий из стека микросервисов. Чтобы получить зачёт, предоставьте скриншот из терминала (консоли), с выводом команды: `docker service ls`
```
[root@node01 centos]# docker service ls
ID             NAME                                MODE         REPLICAS   IMAGE                                          PORTS
0dcturd15tya   swarm_monitoring_alertmanager       replicated   1/1        stefanprodan/swarmprom-alertmanager:v0.14.0
1oy5cqrnrwro   swarm_monitoring_caddy              replicated   1/1        stefanprodan/caddy:latest                      *:3000->3000/tcp, *:9090->9090/tcp, *:9093-9094->9093-9094/tcp
wnzctkx1czon   swarm_monitoring_cadvisor           global       6/6        google/cadvisor:latest
pd7ge54ormzh   swarm_monitoring_dockerd-exporter   global       6/6        stefanprodan/caddy:latest
un3940ajutap   swarm_monitoring_grafana            replicated   1/1        stefanprodan/swarmprom-grafana:5.3.4
gj2s9194tnid   swarm_monitoring_node-exporter      global       6/6        stefanprodan/swarmprom-node-exporter:v0.16.0
2a13t6dsx37y   swarm_monitoring_prometheus         replicated   1/1        stefanprodan/swarmprom-prometheus:v2.5.0
38wbmqug52os   swarm_monitoring_unsee              replicated   1/1        cloudflare/unsee:v0.8.0
[root@node01 centos]#
```
### 4. Выполните на лидере Docker Swarm-кластера команду, указанную ниже, и дайте письменное описание её функционала — что она делает и зачем нужна (см.документацию: https://docs.docker.com/engine/swarm/swarm_manager_locking/) `docker swarm update --autolock=true`
```
[root@node01 centos]# docker swarm update --autolock=true
Swarm updated.
To unlock a swarm manager after it restarts, run the `docker swarm unlock`
command and provide the following key:

    SWMKEY-1-wP6Gth0qC+4CmXsN9qexpOVsT5hOIIEICB25ch3dQY4

Please remember to store this key in a password manager, since without it you
will not be able to restart the manager.
[root@node01 centos]#
```
**Docker** может защитить общий ключ шифрования TLS и ключ, используемый для шифрования и расшифровки журналов Raft в хранилище,
позволяя пользователю стать владельцем этих ключей и требовать ручной разблокировки. Эта функция называется **autolock**.
Когда **Docker** будет перезапускаться, необходимо будет сначала разблокировать **swarm**, используя ключ шифрования,
сгенерированный **Docker**, когда ключи были заблокированы.  
Эта команда блокирует ключи и генерирует ключ, который будет требоваться для разблокировки.

