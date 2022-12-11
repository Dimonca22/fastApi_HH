
### Локальный запуск приложения
Установка пакетов
```shell
pip install Pipfile
```

#### Что бы поднять контейнер БД
```shell
docker-compose -f docker-compose.dev.yaml up
```
### Запуск проекта 
```shell
export FH_DATABASE_URL="postgresql://dima:658941@localhost:32700/fastAPI_hour"
```
```shell
python3 main.py
```
