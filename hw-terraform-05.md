# Домашнее задание к занятию «Использование Terraform в команде»

1. **Проверьте код с помощью tflint и checkov. Вам не нужно инициализировать этот проект.**

   **Перечислите какие типы ошибок обнаружены в проекте (без дублей).**
   
   Ответ:  
   Ошибки **tflint**:
   - Module source "..." uses a default branch as ref (main)
   - Missing version constraint for provider "..." in "..."
   - variable "..." is declared but not used
   
   Ошибки **checkov**:
   - CKV_YC_4: "Ensure compute instance does not have serial console enabled."
   - CKV_YC_2: "Ensure compute instance does not have public IP."
   - CKV_YC_11: "Ensure security group is assigned to network interface."
   
2. **Повторите демонстрацию лекции: настройте YDB, S3 bucket, yandex service account, права доступа и мигрируйте State проекта в S3 с блокировками. Предоставьте скриншоты процесса в качестве ответа.**

   Настройка сервисного эккаунта:
   ![](https://github.com/fedor-metsger/devops-netology/blob/main/Screenshot%20at%202023-06-03%2017-31-15.png)

   Настройка доступа к корзине:
   ![](https://github.com/fedor-metsger/devops-netology/blob/main/Screenshot%20at%202023-06-03%2017-32-34.png)

   Переинициализация бекенда:
   ![](https://github.com/fedor-metsger/devops-netology/blob/main/Screenshot%20at%202023-06-03%2017-35-29.png)

   Создание БД для записи блокировок:
   ![](https://github.com/fedor-metsger/devops-netology/blob/main/Screenshot%20at%202023-06-03%2018-55-27.png)

   Миграция на конфигурацию с блокировками:
   ![](https://github.com/fedor-metsger/devops-netology/blob/main/Screenshot%20at%202023-06-03%2019-38-24.png)

   Записи блокировок в БД:
   ![](https://github.com/fedor-metsger/devops-netology/blob/main/Screenshot%20at%202023-06-03%2019-39-10.png)

   **Откройте в проекте terraform console, а в другом окне из этой же директории попробуйте запустить terraform apply.**
   **Пришлите ответ об ошибке доступа к State.**

   Ошибка **terraform apply** при заблокированной БД:
   ![](https://github.com/fedor-metsger/devops-netology/blob/main/Screenshot%20at%202023-06-03%2019-39-42.png)

   **Принудительно разблокируйте State. Пришлите команду и вывод.**

   Принудительное снятие блокировки:
   ![](https://github.com/fedor-metsger/devops-netology/blob/main/Screenshot%20at%202023-06-03%2019-41-39.png)
   
