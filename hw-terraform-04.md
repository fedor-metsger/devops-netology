# Домашнее задание к занятию «Продвинутые методы работы с Terraform»

1. **Создайте 1 ВМ, используя данный модуль. В файле cloud-init.yml необходимо использовать переменную для ssh ключа вместо хардкода. Передайте ssh-ключ в функцию template_file в блоке vars ={} .**
   **Воспользуйтесь примером. Обратите внимание что ssh-authorized-keys принимает в себя список, а не строку!**

   **Добавьте в файл cloud-init.yml установку nginx.**
   
   Привожу файл **cloud-init.yml**:

```
#cloud-config
users:
  - name: ubuntu
    groups: sudo
    shell: /bin/bash
    sudo: ['ALL=(ALL) NOPASSWD:ALL']
    ssh-authorized-keys:
      - ${ssh_public_key}
package_update: true
package_upgrade: false
packages:
  - vim
  - nginx
```

   **Предоставьте скриншот подключения к консоли и вывод команды** `sudo nginx -t`
   
  ```
  fedor@fedor-Z68P-DS3:~/CODE/Netology/DevOps/ter-homeworks/04/src$ ssh ubuntu@51.250.73.175
The authenticity of host '51.250.73.175 (51.250.73.175)' can't be established.
ED25519 key fingerprint is SHA256:GkoDpnz53dS4GfPysge0t6XFFTPE+iEdV1CAuxf3xYc.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '51.250.73.175' (ED25519) to the list of known hosts.
Welcome to Ubuntu 20.04.6 LTS (GNU/Linux 5.4.0-149-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Ubuntu comes with ABSOLUTELY NO WARRANTY, to the extent permitted by
applicable law.

To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

ubuntu@develop-web-0:~$ nginx -t

Command 'nginx' not found, but can be installed with:

sudo apt install nginx-core    # version 1.18.0-0ubuntu1.4, or
sudo apt install nginx-extras  # version 1.18.0-0ubuntu1.4
sudo apt install nginx-full    # version 1.18.0-0ubuntu1.4
sudo apt install nginx-light   # version 1.18.0-0ubuntu1.4

ubuntu@develop-web-0:~$
  ```

2. **Напишите локальный модуль vpc, который будет создавать 2 ресурса: одну сеть и одну подсеть в зоне, объявленной при вызове модуля. например: ru-central1-a.**
   
   **Модуль должен возвращать значения vpc.id и subnet.id**
   
   Прилагаю ссылку на модуль: [vpc](https://github.com/fedor-metsger/ter-homeworks/tree/terraform-04/04/src/vpc)

   **Замените ресурсы yandex_vpc_network и yandex_vpc_subnet, созданным модулем.**
   
   Прилагаю файл [main.tf](https://github.com/fedor-metsger/ter-homeworks/blob/terraform-04/04/src/main.tf):
   ```
   module "vpc" {
     source    = "./vpc"
     env_name  = "develop"
     zone      = "ru-central1-a"
     cidr      = "10.0.1.0/24"
   }

   module "test-vm" {
     source          = "git::https://github.com/udjin10/yandex_compute_instance.git?ref=main"
     env_name        = "develop"
     network_id      = module.vpc.vpc_id
     subnet_zones    = ["ru-central1-a"]
     subnet_ids      = [ module.vpc.subnet_id ]
     instance_name   = "web"
     instance_count  = 1
     image_family    = "ubuntu-2004-lts"
     public_ip       = true
  
     metadata = {
       user-data          = data.template_file.userdata.rendered
       serial-port-enable = 1
     }
   }

   data template_file "userdata" {
     template = file("${path.module}/cloud-init.yml")

     vars = {
       ssh_public_key = file("~/.ssh/id_rsa.pub")
     }
   }
   ```

   **Сгенерируйте документацию к модулю с помощью terraform-docs.**
