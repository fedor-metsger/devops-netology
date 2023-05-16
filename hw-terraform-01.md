# Домашнее задание к занятию «Введение в Terraform»

1. **Приложите скриншот вывода команды** `terraform --version`.

```
root@server1:/home/vagrant/Netology/DevOps/ter-homeworks/01/src# terraform --version
Terraform v1.4.6
on linux_amd64
root@server1:/home/vagrant/Netology/DevOps/ter-homeworks/01/src#
```

**В каком terraform файле согласно этому .gitignore допустимо сохранить личную, секретную информацию?**

Ответ: В файле **personal.auto.tfvars**

**Найдите в State-файле секретное содержимое созданного ресурса random_password, пришлите в качестве ответа конкретный ключ и его значение.**
   
```
"result": "Tdu3IOJ4NNd8I9Hu"
```

**Объясните в чем заключаются намеренно допущенные ошибки? Исправьте их.**

Ошибка:
 ```
│ Error: Missing name for resource
│
│   on main.tf line 23, in resource "docker_image":
│   23: resource "docker_image" {
│
│ All resource blocks must have 2 labels (type, name).
╵
```

Эта ошибка обозначает, что пропущена вторая метка в описании ресурса **docker_image**. Правильно будет написать так:
   
```
resource "docker_image" "nginx" {
```

Ошибка:
```
│ Error: Invalid resource name
│
│   on main.tf line 28, in resource "docker_container" "1nginx":
│   28: resource "docker_container" "1nginx" {
│
│ A name must start with a letter or underscore and may contain only letters, digits, underscores, and dashes.
```

Эта ошибка обозначает, что имя в описании ресурса **docker_container** должно начинаться с буквы. Правильно будет написать так:

```
resource "docker_container" "nginx" {
```

Ошибка:
```
│ Error: Reference to undeclared resource
│
│   on main.tf line 30, in resource "docker_container" "nginx":
│   30:   name  = "example_${random_password.random_string_fake.resuld}"
│
│ A managed resource "random_password" "random_string_fake" has not been declared in the root module.
```

Эта ошибка обозначает, что ресурс **random_string_fake** не был определён. Правильно будет написать так:

```
name  = "example_${random_password.random_string.resuld}"
```

Ошибка:
```
│ Error: Unsupported attribute
│
│   on main.tf line 30, in resource "docker_container" "nginx":
│   30:   name  = "example_${random_password.random_string.resuld}"
│
│ This object has no argument, nested block, or exported attribute named "resuld". Did you mean "result"?
```

Эта ошибка обозначает, что объект **random_password.random_string** не имеет аттрибута **resuld**. Правильно будет написать так:

```
name  = "example_${random_password.random_string.result}"
```

**Выполните код. В качестве ответа приложите вывод команды** `docker ps`

```
vagrant@server1:~/Netology/DevOps/ter-homeworks/01/src$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED         STATUS                          PORTS                                       NAMES
cb7ce9d39b8c   448a08f1d2f9           "/docker-entrypoint.…"   2 minutes ago   Up 2 minutes                    0.0.0.0:8000->80/tcp                        example_Tdu3IOJ4NNd8I9Hu
vagrant@server1:~/Netology/DevOps/ter-homeworks/01/src$
```

**Объясните своими словами, в чем может быть опасность применения ключа -auto-approve ?**

Ответ: Опция **--auto-approve** пропускает интерактивное подтвержнение плана перед применением. Опасность её использования заключается в возможности внесения необдуманных изменений.


