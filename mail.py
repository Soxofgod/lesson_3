import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

LOGIN = os.getenv('LOGIN')
TOKEN = os.getenv('TOKEN')

name_to = 'Иван'
my_name = 'Егор'
website = 'https://dvmn.org/profession-ref-program/egormeln/Z3DSm/'
letter = """
From: {0}
To: {1}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, {2}! {3} приглашает тебя на сайт {4}!

{4} — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на {4}? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → {4}  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""".format('devmanorg@yandex.ru','melnichenkoegorka@yandex.ru', name_to, my_name, website)
print(letter)
letter = letter.encode('UTF-8')
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(LOGIN,TOKEN)
server.sendmail('devmanorg@yandex.ru','melnichenkoegorka@yandex.ru',letter)
server.quit()