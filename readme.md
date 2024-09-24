# Stanisla home bot


## Настройка автозапуска

В файле systemd_script.sh:
- в ExecStart указать путь к main.py проекта
- в WorkingDirectory указать путь к папке проекта

В systemd linux нужно создать сервис:
```sh
sudo touch /etc/systemd/system/<script_name>.service
```
скопировать данные из systemd_script.sh в <script_name>.service

Перезапускаем демона:
```sh
sudo systemctl daemon-reload
```

Запускаем сервис:
```sh
sudo systemctl start <script_name>.service
```

Проверяем статус:
```sh
sudo systemctl status startscript.service
```

В файле config.py указать токен бота.