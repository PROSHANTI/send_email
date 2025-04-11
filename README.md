# send email

## Описание
```text
Программа отправки ежедневных отчетов по электронной почте на указанный адрес.
```

## Технологии
- Python3.11
- tkinter
- smtplib
  
## Подготовка
- Скачать программу
```bash
git clone https://github.com/PROSHANTI/send_email.git
```
- Перейти в папку с программой и установить зависимости
```bash
pip install -r requirements.txt 
```

- Подготовить `.env` файл
```bash
## env
send_from = '_отправитель_'
my_pass = '_пароль_'
addr_to = '_кому_'
bcc_to = '_копия_'
```

- Запустить программу
```bash
python3 send_email.py 
```
