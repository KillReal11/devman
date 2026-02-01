import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

link=("https://dvmn.org/profession-ref-program/dawiduk2013/xab6J/")
email_from=("dawiduk2013@yandex.ru")
email_to=("malina1999@yandex.ru")

email=(f"""\
From: {email_from}
To: {email_to}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашаю тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""")

edited_email=email.replace("%website%",link)
edited_email=edited_email.replace("%friend_name%","Алексей")
edited_email=edited_email.replace("%my_name%","Я, Кирилл, ")
edited_email=edited_email.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru',465)
server.login((os.getenv("LOGIN")), (os.getenv("TOKEN")))
server.sendmail(email_from, email_to, edited_email)
server.quit()
