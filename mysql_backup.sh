var=$(date +"%m-%d-%Y_%H-%M-%S")
mysqldump --default-character-set=utf8 --password=vidas --user=vidas weltkrieg > /data/vidas/backup/backup_$var.sql
