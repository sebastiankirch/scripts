#!/bin/sh
if [ "$1" == "true" ]; then
  if [[ ! -z "`mysql -u guest -pguest -qfsBe "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='doculib'" 2>&1`" ]];
  then
    echo "false"
    exit 1
  else
    mysql -u guest -pguest -e "create database doculib"
    mysql -u guest -pguest -e "GRANT ALL PRIVILEGES ON doculib.* TO 'guest'@'localhost';"
    echo "true"
    exit 0
  fi
else
  if [[ ! -z "`mysql -u root -qfsBe "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='doculib'" 2>&1`" ]];
  then
    echo "false"
    exit 1
  else
    mysql -u root -e "create database doculib"
    mysql -u root -e "GRANT ALL PRIVILEGES ON doculib.* TO 'root'@'localhost';"
    echo "true"
    exit 0
  fi
fi
