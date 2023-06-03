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


   
   
   
